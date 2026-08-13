from __future__ import annotations

import importlib
import json
from dataclasses import fields, replace
from hashlib import sha256
from io import BytesIO
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import Polygon
from test_apply_bess_planning_feature_policy import _application_fixture

from landscout import stages
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)

PARCEL_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_formal_review_required",
    "bess_cnig_aggregation_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
    "bess_cnig_application_result_sha256",
)
RELATION_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_selected_for_parcel_status",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
    "bess_cnig_resulting_parcel_status_priority",
)


def _aggregation_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    object,
    BessPlanningFeatureParcelAggregationResult,
]:
    inputs, coded, config, policy, application = _application_fixture()
    result = aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
    return inputs, coded, config, policy, application, result


def _build_from_relations(
    relations: pd.DataFrame,
    *,
    parcel_ids: tuple[str, ...] = ("PARCEL-1", "PARCEL-2"),
) -> BessPlanningFeatureParcelAggregationResult:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, application = _application_fixture()
    parcels = gpd.GeoDataFrame(
        {"parcel_id": list(parcel_ids), "prior": range(len(parcel_ids))},
        geometry=[
            Polygon([(i * 3, 0), (i * 3 + 2, 0), (i * 3 + 2, 2), (i * 3, 2)])
            for i in range(len(parcel_ids))
        ],
        crs="EPSG:2154",
        index=pd.Index(range(10, 10 + len(parcel_ids)), name="parcel_row"),
    )
    application = replace(application, relations=relations.reset_index(drop=True))
    application = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )._result_with_hashes(application)
    return module._build_result(parcels, application)


def _relation(
    *,
    parcel_id: str = "PARCEL-1",
    feature_id: str = "F-1",
    relation_type: str = "AREA_OVERLAP",
    application_status: str = "APPLIED_EXACT_POLICY",
    status: str | None = "MATERIAL_REVIEW_REQUIRED",
    confidence: str | None = "HIGH",
    priority: int | None = 30,
    area: float = 0.000001,
) -> dict[str, object]:
    _, _, _, _, application = _application_fixture()
    row = application.relations.iloc[0].to_dict()
    row.update(
        parcel_id=parcel_id,
        planning_feature_id=feature_id,
        relation_type=relation_type,
        bess_cnig_policy_application_status=application_status,
        bess_cnig_precheck_status=status,
        bess_cnig_precheck_confidence=confidence,
        bess_cnig_status_priority=priority,
        intersection_area_m2=area if relation_type == "AREA_OVERLAP" else None,
        intersection_length_m=area if relation_type == "LENGTH_OVERLAP" else None,
    )
    return row


def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureParcelAggregationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
    frames = {
        "PARCELS": (result.parcels, "parcels.parquet", True),
        "RELATION_ASSESSMENTS": (
            result.relation_assessments,
            "relations.parquet",
            False,
        ),
    }
    paths: dict[str, Path] = {}
    records: list[dict[str, object]] = []
    for role, (frame, filename, geospatial) in frames.items():
        path = tmp_path / filename
        frame.to_parquet(path, index=True)
        paths[role] = path
        signature = deterministic_frame_schema_signature(frame)
        payload = path.read_bytes()
        records.append(
            {
                "artifact_role": role,
                "filename": filename,
                "row_count": len(frame),
                "size_bytes": len(payload),
                "sha256": sha256(payload).hexdigest(),
                "frame_schema_signature": signature,
                "geospatial": geospatial,
                "crs": signature.get("crs"),
            }
        )
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeatureParcelAggregationResult)
        if field.name not in {"parcels", "relation_assessments"}
    )
    manifest = {
        "schema_version": 1,
        "artifact_kind": "BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT",
        **{name: getattr(result, name) for name in scalar_names},
        "artifacts": records,
    }
    BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(manifest)
    manifest_path = tmp_path / "aggregation.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest_path, paths, manifest


def test_exact_relations_select_configured_max_priority_and_lowest_confidence() -> None:
    relations = pd.DataFrame(
        [
            _relation(
                feature_id="LOW",
                priority=10,
                status="CONTEXT_REVIEW_REQUIRED",
                area=1000.0,
            ),
            _relation(
                feature_id="HIGH-A",
                priority=50,
                status="LIKELY_MATERIAL_CONSTRAINT",
                confidence="HIGH",
            ),
            _relation(
                feature_id="HIGH-B",
                priority=50,
                status="LIKELY_MATERIAL_CONSTRAINT",
                confidence="LOW",
            ),
        ]
    )
    result = _build_from_relations(relations)
    parcel = result.parcels.iloc[0]
    assert parcel.bess_cnig_parcel_aggregation_status == "AGGREGATED_EXACT_POLICY"
    assert parcel.bess_cnig_parcel_precheck_status == "LIKELY_MATERIAL_CONSTRAINT"
    assert parcel.bess_cnig_parcel_precheck_confidence == "LOW"
    assert parcel.bess_cnig_parcel_status_priority == 50
    assert parcel.bess_cnig_selected_feature_ids_json == '["HIGH-A","HIGH-B"]'
    assert parcel.bess_cnig_distinct_exact_status_count == 2
    assert bool(parcel.bess_cnig_multiple_exact_statuses) is True
    assert parcel.bess_cnig_selected_relation_count == 2
    assert parcel.bess_cnig_lower_priority_controlling_relation_count == 1
    assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "LOWER_PRIORITY_CONTROLLING",
        "SELECTED_CONTROLLING",
        "SELECTED_CONTROLLING",
    ]


def test_policy_unknown_is_exact_but_unresolved_controlling_overrides() -> None:
    exact_unknown = _build_from_relations(
        pd.DataFrame([_relation(status="UNKNOWN", confidence="LOW", priority=40)])
    )
    assert exact_unknown.parcels.iloc[0].bess_cnig_parcel_precheck_status == "UNKNOWN"
    unresolved = _relation(
        feature_id="UNRESOLVED",
        application_status="UNRESOLVED_CODE_PAIR",
        status=None,
        confidence=None,
        priority=None,
    )
    mixed = _build_from_relations(pd.DataFrame([_relation(), unresolved]))
    parcel = mixed.parcels.iloc[0]
    assert (
        parcel.bess_cnig_parcel_aggregation_status == "UNRESOLVED_CONTROLLING_CODE_PAIR"
    )
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert pd.isna(parcel.bess_cnig_parcel_precheck_confidence)
    assert pd.isna(parcel.bess_cnig_parcel_status_priority)
    assert parcel.bess_cnig_unresolved_feature_ids_json == '["UNRESOLVED"]'
    assert mixed.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "DEFERRED_BY_UNRESOLVED_CONTROLLING",
        "UNRESOLVED_CONTROLLING",
    ]


@pytest.mark.parametrize("relation_type", ["AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"])
def test_every_positive_relation_type_controls_without_threshold(
    relation_type: str,
) -> None:
    result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type, area=1e-15)])
    )
    assert result.parcels.iloc[0].bess_cnig_controlling_relation_count == 1
    assert (
        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role
        == "SELECTED_CONTROLLING"
    )


@pytest.mark.parametrize("relation_type", ["TOUCH_ONLY", "BOUNDARY_TOUCH"])
def test_boundary_only_relations_are_contextual(relation_type: str) -> None:
    result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type)])
    )
    parcel = result.parcels.iloc[0]
    assert parcel.bess_cnig_parcel_aggregation_status == "TOUCH_ONLY_RELATIONS_ONLY"
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert parcel.bess_cnig_touch_only_feature_ids_json == '["F-1"]'
    assert (
        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role
        == "TOUCH_ONLY_CONTEXT"
    )


def test_touch_relation_remains_context_beside_a_controlling_relation() -> None:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="EXACT"),
                _relation(
                    feature_id="TOUCH",
                    relation_type="TOUCH_ONLY",
                    priority=50,
                    status="LIKELY_MATERIAL_CONSTRAINT",
                ),
            ]
        )
    )
    assert result.parcels.iloc[0].bess_cnig_parcel_precheck_status == (
        "MATERIAL_REVIEW_REQUIRED"
    )
    assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "SELECTED_CONTROLLING",
        "TOUCH_ONLY_CONTEXT",
    ]


def test_no_relation_parcel_is_retained_without_a_decision() -> None:
    result = _build_from_relations(pd.DataFrame([_relation()]))
    parcel = result.parcels.iloc[1]
    assert parcel.bess_cnig_parcel_aggregation_status == "NO_PLANNING_FEATURE_RELATION"
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert bool(parcel.bess_cnig_formal_review_required) is True


def test_parcel_and_relation_prefixes_order_and_inputs_are_preserved() -> None:
    inputs, coded, config, policy, application = _application_fixture()
    parcels_copy = inputs[1].copy(deep=True)
    relations_copy = application.relations.copy(deep=True)
    result = aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
    assert_geodataframe_equal(inputs[1], parcels_copy)
    assert_frame_equal(application.relations, relations_copy)
    assert_geodataframe_equal(
        inputs[1], result.parcels.loc[:, inputs[1].columns], check_dtype=True
    )
    assert_frame_equal(
        application.relations,
        result.relation_assessments.loc[:, application.relations.columns],
        check_dtype=True,
    )
    assert tuple(result.parcels.columns[-len(PARCEL_COLUMNS) :]) == PARCEL_COLUMNS
    assert (
        tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS) :])
        == RELATION_COLUMNS
    )


def test_local_corruption_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, result = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_selected_relation_count"] = 999
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs, coded, config, policy, application, corrupted
        )
    assert calls == 0


@pytest.mark.parametrize(
    ("frame_name", "column", "value"),
    [
        ("parcels", "bess_cnig_selected_relation_count", 999),
        ("parcels", "bess_cnig_parcel_precheck_status", "UNKNOWN"),
        ("parcels", "bess_cnig_parcel_status_priority", 999),
        ("parcels", "bess_cnig_parcel_precheck_confidence", "HIGH"),
        ("parcels", "bess_cnig_selected_feature_ids_json", "[]"),
        (
            "relation_assessments",
            "bess_cnig_parcel_relation_role",
            "TOUCH_ONLY_CONTEXT",
        ),
        ("relation_assessments", "parcel_id", "PARCEL-OTHER"),
    ],
)
def test_coordinated_local_cross_table_corruption_is_rejected(
    frame_name: str,
    column: str,
    value: object,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    frame.loc[frame.index[0], column] = value
    corrupted = module._result_with_hashes(replace(result, **{frame_name: frame}))
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)


def test_invalid_output_dtype_and_non_2d_parcel_fail_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    parcels = result.parcels.copy(deep=True)
    parcels["bess_cnig_selected_relation_count"] = parcels[
        "bess_cnig_selected_relation_count"
    ].astype("object")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, parcels=parcels))
        )
    relations = result.relation_assessments.copy(deep=True)
    relations["bess_cnig_selected_for_parcel_status"] = relations[
        "bess_cnig_selected_for_parcel_status"
    ].astype("object")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        module._validate_result_envelope(
            module._result_with_hashes(
                replace(result, relation_assessments=relations)
            )
        )
    parcels = result.parcels.copy(deep=True)
    geometry = parcels.geometry.iloc[0]
    parcels.at[parcels.index[0], parcels.geometry.name] = Polygon(
        [(x, y, 5) for x, y in geometry.exterior.coords]
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="2D"):
        module._validate_result_envelope(replace(result, parcels=parcels))


def test_one_aggregation_and_one_public_validation_each_call_heavy_once(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    actual = module.validate_bess_planning_feature_application_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    result = module.aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
    assert calls == 1
    module.validate_bess_planning_feature_parcel_aggregation_result(
        *inputs, coded, config, policy, application, result
    )
    assert calls == 2


def test_valid_two_file_verified_byte_artifacts_and_source_readback(
    tmp_path: Path,
) -> None:
    inputs, coded, config, policy, application, result = _aggregation_fixture()
    manifest, paths, _ = _write_artifacts(tmp_path, result)
    loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
    )
    assert_geodataframe_equal(result.parcels, loaded.parcels)
    assert_frame_equal(result.relation_assessments, loaded.relation_assessments)
    validate_bess_planning_feature_parcel_aggregation_result(
        *inputs, coded, config, policy, application, loaded
    )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda value: value.update(schema_version=2),
        lambda value: value["artifacts"].pop(),
        lambda value: value["artifacts"].append(
            {**value["artifacts"][0], "artifact_role": "EXTRA"}
        ),
        lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
        lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
        lambda value: value["artifacts"][1].update(
            filename=value["artifacts"][0]["filename"]
        ),
        lambda value: value["artifacts"][0].update(filename="C:/absolute.parquet"),
        lambda value: value["artifacts"][0].update(size_bytes=1),
        lambda value: value["artifacts"][0].update(sha256="f" * 64),
        lambda value: value["artifacts"][0].update(sha256="bad"),
        lambda value: value["artifacts"][0].update(row_count=999),
        lambda value: value["artifacts"][0]["frame_schema_signature"].update(
            index_names=["wrong"]
        ),
        lambda value: value["artifacts"][0].update(crs=None),
        lambda value: value["artifacts"][0].update(crs={"wrong": True}),
        lambda value: value["artifacts"][0].update(geospatial=False),
        lambda value: value.update(unknown=True),
    ],
)
def test_artifact_manifest_corruption_is_rejected(
    tmp_path: Path, mutation: object
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, manifest = _write_artifacts(tmp_path, result)
    assert callable(mutation)
    mutation(manifest)
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


def test_duplicate_json_and_physical_replacement_are_rejected(tmp_path: Path) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    original = manifest_path.read_text(encoding="utf-8")
    manifest_path.write_text(
        '{"schema_version":1,"schema_version":1}', encoding="utf-8"
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="Duplicate JSON"
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
    manifest_path.write_text(original, encoding="utf-8")
    paths["RELATION_ASSESSMENTS"].write_bytes(
        paths["RELATION_ASSESSMENTS"].read_bytes() + b"tamper"
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="size|SHA"):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


def test_verified_bytes_are_the_bytes_parsed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    target = paths["RELATION_ASSESSMENTS"]
    verified = target.read_bytes()
    replacement = tmp_path / "replacement.parquet"
    result.relation_assessments.to_parquet(replacement, compression="gzip", index=True)
    replacement_bytes = replacement.read_bytes()
    original_read_bytes = Path.read_bytes
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    original_read = module.pd.read_parquet
    observed: list[bytes] = []

    def replace_after_read(path: Path) -> bytes:
        payload = original_read_bytes(path)
        if path == target:
            path.write_bytes(replacement_bytes)
        return payload

    def inspect_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(source.getvalue())
        return original_read(source, *args, **kwargs)

    monkeypatch.setattr(Path, "read_bytes", replace_after_read)
    monkeypatch.setattr(module.pd, "read_parquet", inspect_read)
    loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
    )
    assert verified in observed
    assert_frame_equal(result.relation_assessments, loaded.relation_assessments)


def test_public_exports_are_stable() -> None:
    required = {
        "BessPlanningFeatureParcelAggregationArtifactManifest",
        "BessPlanningFeatureParcelAggregationError",
        "BessPlanningFeatureParcelAggregationResult",
        "aggregate_bess_planning_feature_policy_to_parcels",
        "load_bess_planning_feature_parcel_aggregation_artifacts",
        "validate_bess_planning_feature_parcel_aggregation_result",
    }
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
