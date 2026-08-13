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
from shapely.geometry import LineString, MultiPolygon, Point, Polygon
from test_apply_bess_planning_feature_policy import _application_fixture

from landscout import stages
from landscout.common.bess_application_contract import POLICY_SUFFIX_DTYPES
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
    canonicalize_application_dtypes: bool = True,
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
    relations = relations.reset_index(drop=True)
    relations["bess_cnig_policy_profile"] = application.policy_profile
    relations["bess_cnig_policy_sha256"] = application.policy_sha256
    relations["bess_cnig_policy_result_sha256"] = (
        application.policy_complete_result_content_sha256
    )
    if canonicalize_application_dtypes:
        for column, dtype in POLICY_SUFFIX_DTYPES.items():
            relations[column] = pd.array(relations[column].tolist(), dtype=dtype)
    application = replace(application, relations=relations)
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
        official_code_status=(
            "UNKNOWN_CODE_PAIR"
            if application_status == "UNRESOLVED_CODE_PAIR"
            else "RESOLVED_OFFICIAL"
        ),
        bess_cnig_policy_application_status=application_status,
        bess_cnig_precheck_status=status,
        bess_cnig_precheck_confidence=confidence,
        bess_cnig_status_priority=priority,
        bess_cnig_rationale=(
            None
            if application_status == "UNRESOLVED_CODE_PAIR"
            else row["bess_cnig_rationale"]
        ),
        bess_cnig_required_human_action=(
            None
            if application_status == "UNRESOLVED_CODE_PAIR"
            else row["bess_cnig_required_human_action"]
        ),
        bess_cnig_limitations=(
            None
            if application_status == "UNRESOLVED_CODE_PAIR"
            else row["bess_cnig_limitations"]
        ),
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


def _rehash_coordinated_result(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    source_parcels = result.parcels.drop(columns=list(PARCEL_COLUMNS))
    source_relations = result.relation_assessments.drop(columns=list(RELATION_COLUMNS))
    updated = replace(
        result,
        source_parcels_content_sha256=module._frame_sha256(
            source_parcels,
            "landscout.bess_cnig_parcel_aggregation.source_parcels",
        ),
        source_application_relations_content_sha256=module._frame_sha256(
            source_relations,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
    )
    return module._result_with_hashes(updated)


def _duplicate_selected_pair_result() -> BessPlanningFeatureParcelAggregationResult:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A"),
                _relation(feature_id="B"),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    relations.loc[relations.index[1], "planning_feature_id"] = "A"
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_selected_feature_ids_json"] = '["A"]'
    return _rehash_coordinated_result(
        replace(result, parcels=parcels, relation_assessments=relations)
    )


def _invalid_lower_feature_id_result() -> BessPlanningFeatureParcelAggregationResult:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(feature_id="HIGH", priority=30),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "/tmp/feature"
    return _rehash_coordinated_result(replace(result, relation_assessments=relations))


def _cross_parcel_priority_conflict_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    parcel_id="PARCEL-1",
                    feature_id="A",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    parcel_id="PARCEL-2",
                    feature_id="B",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=30,
                ),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    mask = relations["parcel_id"].eq("PARCEL-2")
    relations.loc[mask, "bess_cnig_status_priority"] = 50
    relations.loc[mask, "bess_cnig_resulting_parcel_status_priority"] = 50
    parcels = result.parcels.copy(deep=True)
    parcels.loc[
        parcels["parcel_id"].eq("PARCEL-2"), "bess_cnig_parcel_status_priority"
    ] = 50
    return _rehash_coordinated_result(
        replace(result, parcels=parcels, relation_assessments=relations)
    )


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
            module._result_with_hashes(replace(result, relation_assessments=relations))
        )
    parcels = result.parcels.copy(deep=True)
    geometry = parcels.geometry.iloc[0]
    parcels.at[parcels.index[0], parcels.geometry.name] = Polygon(
        [(x, y, 5) for x, y in geometry.exterior.coords]
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="2D"):
        module._validate_result_envelope(replace(result, parcels=parcels))


@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(status="AUTHORIZED")]),
        pd.DataFrame([_relation(status="FORBIDDEN")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="PROHIBITED",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    confidence="CERTAIN",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    relation_type="TOUCH_ONLY",
                    application_status="INVALID_APPLICATION_STATUS",
                )
            ]
        ),
    ],
    ids=[
        "selected-authorized",
        "selected-forbidden",
        "lower-prohibited",
        "lower-certain-confidence",
        "contextual-invalid-application-status",
    ],
)
def test_every_inherited_application_relation_domain_is_validated_locally(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(relations)


def test_unresolved_relation_cannot_contain_a_decision() -> None:
    row = _relation(
        application_status="UNRESOLVED_CODE_PAIR",
        status="UNKNOWN",
        confidence="LOW",
        priority=40,
    )
    row["official_code_status"] = "UNKNOWN_CODE_PAIR"
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("feature_family", "OTHER"),
        ("type_code_raw", "7"),
        ("subtype_code_raw", "AA"),
        ("bess_cnig_application_scope", "WRONG_SCOPE"),
        ("bess_cnig_local_feature_text_interpreted", True),
    ],
)
def test_all_application_identity_scope_and_boundary_fields_are_intrinsic(
    column: str, value: object
) -> None:
    row = _relation(relation_type="TOUCH_ONLY")
    row[column] = value
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))


def test_application_relation_suffix_dtype_is_validated_locally() -> None:
    relations = pd.DataFrame([_relation()])
    relations["bess_cnig_precheck_status"] = relations[
        "bess_cnig_precheck_status"
    ].astype("category")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        _build_from_relations(relations, canonicalize_application_dtypes=False)


@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="MAX",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="LOW-A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW-B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=10,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=10,
                ),
            ]
        ),
    ],
    ids=[
        "same-maximum-priority-two-statuses",
        "same-lower-priority-two-statuses",
        "same-status-two-priorities",
    ],
)
def test_status_and_priority_mapping_is_one_to_one_at_every_level(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="priority"):
        _build_from_relations(relations)


def test_valid_repeated_status_and_priority_mapping_selects_every_exact_match() -> None:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A", priority=30),
                _relation(feature_id="B", priority=30),
            ]
        )
    )
    assert result.parcels.iloc[0].bess_cnig_selected_relation_count == 2
    assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "SELECTED_CONTROLLING",
        "SELECTED_CONTROLLING",
    ]


@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(feature_id="A"), _relation(feature_id="A")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(feature_id="HIGH", priority=30),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="DEFERRED"),
                _relation(feature_id="DEFERRED"),
                _relation(
                    feature_id="UNRESOLVED",
                    application_status="UNRESOLVED_CODE_PAIR",
                    status=None,
                    confidence=None,
                    priority=None,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="A", relation_type="AREA_OVERLAP"),
                _relation(feature_id="A", relation_type="LENGTH_OVERLAP"),
            ]
        ),
    ],
    ids=[
        "selected",
        "lower-priority",
        "contextual",
        "deferred",
        "different-relation-types",
    ],
)
def test_duplicate_parcel_feature_identity_is_rejected_for_every_role(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="duplicate|unique"
    ):
        _build_from_relations(relations)


@pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature"],
)
def test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role(
    feature_id: object,
) -> None:
    relations = pd.DataFrame(
        [
            _relation(
                feature_id=feature_id,
                status="CONTEXT_REVIEW_REQUIRED",
                priority=10,
            ),
            _relation(feature_id="HIGH", priority=30),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="feature|identity"
    ):
        _build_from_relations(relations)


@pytest.mark.parametrize("feature_id", [r"C:\feature", " GPU:F "])
def test_invalid_deferred_feature_id_is_rejected_independently_of_json_role(
    feature_id: str,
) -> None:
    relations = pd.DataFrame(
        [
            _relation(feature_id=feature_id),
            _relation(
                feature_id="UNRESOLVED",
                application_status="UNRESOLVED_CODE_PAIR",
                status=None,
                confidence=None,
                priority=None,
            ),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="feature|identity"
    ):
        _build_from_relations(relations)


@pytest.mark.parametrize("parcel_id", [None, " PARCEL-1 "])
def test_invalid_relation_parcel_id_is_rejected(parcel_id: object) -> None:
    relation = _relation()
    relation["parcel_id"] = parcel_id
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel|identity"
    ):
        _build_from_relations(pd.DataFrame([relation]))


def test_unknown_relation_type_is_rejected_by_shared_relation_contract() -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="relation type"
    ):
        _build_from_relations(pd.DataFrame([_relation(relation_type="NEARBY")]))


@pytest.mark.parametrize("context_type", [None, "TOUCH_ONLY", "BOUNDARY_TOUCH"])
def test_document_wide_same_priority_cannot_map_to_two_statuses(
    context_type: str | None,
) -> None:
    second_type = context_type or "AREA_OVERLAP"
    relations = pd.DataFrame(
        [
            _relation(
                parcel_id="PARCEL-1",
                feature_id="A",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=50,
            ),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="B",
                relation_type=second_type,
                status="MATERIAL_REVIEW_REQUIRED",
                priority=50,
            ),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="priority|mapping"
    ):
        _build_from_relations(relations)


def test_document_wide_same_status_cannot_map_to_two_priorities() -> None:
    relations = pd.DataFrame(
        [
            _relation(
                parcel_id="PARCEL-1",
                feature_id="A",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=50,
            ),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="B",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=10,
            ),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="priority|mapping"
    ):
        _build_from_relations(relations)


def test_document_wide_repeated_mapping_and_unresolved_rows_are_valid() -> None:
    relations = pd.DataFrame(
        [
            _relation(parcel_id="PARCEL-1", feature_id="A", priority=30),
            _relation(parcel_id="PARCEL-2", feature_id="B", priority=30),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="U",
                application_status="UNRESOLVED_CODE_PAIR",
                status=None,
                confidence=None,
                priority=None,
            ),
        ]
    )
    result = _build_from_relations(relations)
    assert len(result.relation_assessments) == 3


def test_complete_five_status_policy_mapping_is_globally_valid() -> None:
    mapping = (
        ("LIKELY_MATERIAL_CONSTRAINT", 50, "HIGH"),
        ("UNKNOWN", 40, "LOW"),
        ("MATERIAL_REVIEW_REQUIRED", 30, "HIGH"),
        ("DESIGN_REVIEW_REQUIRED", 20, "MEDIUM"),
        ("CONTEXT_REVIEW_REQUIRED", 10, "HIGH"),
    )
    relations = pd.DataFrame(
        [
            _relation(
                parcel_id=f"PARCEL-{position}",
                feature_id=f"FEATURE-{position}",
                status=status,
                priority=priority,
                confidence=confidence,
            )
            for position, (status, priority, confidence) in enumerate(mapping, start=1)
        ]
    )
    result = _build_from_relations(
        relations,
        parcel_ids=tuple(f"PARCEL-{position}" for position in range(1, 6)),
    )
    assert len(result.relation_assessments) == 5


def test_selected_relation_role_requires_selected_status_and_priority() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    relations.loc[relations.index[0], "bess_cnig_parcel_relation_role"] = (
        "SELECTED_CONTROLLING"
    )
    relations.loc[relations.index[0], "bess_cnig_selected_for_parcel_status"] = True
    corrupted = module._result_with_hashes(
        replace(result, relation_assessments=relations)
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)


def _validate_parcel_geometries(geometries: list[object]) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, application = _application_fixture()
    parcels = gpd.GeoDataFrame(
        {"parcel_id": [f"P-{index}" for index in range(len(geometries))]},
        geometry=geometries,
        crs="EPSG:2154",
    )
    result = module._build_result(
        parcels, replace(application, relations=application.relations.iloc[0:0])
    )
    module._validate_result_envelope(result)


@pytest.mark.parametrize(
    "geometry",
    [
        Point(0, 0),
        LineString([(0, 0), (1, 1)]),
        Polygon(),
        Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        None,
    ],
    ids=["point", "line", "empty", "invalid", "null"],
)
def test_malformed_parcel_geometry_is_rejected_intrinsically(geometry: object) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _validate_parcel_geometries([geometry])


def test_valid_polygon_and_multipolygon_parcels_are_accepted() -> None:
    polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
    _validate_parcel_geometries([polygon, MultiPolygon([polygon])])


@pytest.mark.parametrize("frame_name", ["parcels", "relation_assessments"])
def test_duplicate_output_columns_are_rejected_intrinsically(frame_name: str) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    frame = getattr(result, frame_name)
    duplicate = pd.concat([frame, frame.iloc[:, [0]]], axis=1)
    if frame_name == "parcels":
        duplicate = gpd.GeoDataFrame(
            duplicate, geometry=frame.geometry.name, crs=frame.crs
        )
    corrupted = replace(result, **{frame_name: duplicate})
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="duplicate"):
        module._validate_result_envelope(corrupted)


@pytest.mark.parametrize("version", [1, 3, 999])
def test_only_application_result_schema_two_is_accepted(version: int) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    corrupted = module._result_with_hashes(
        replace(result, application_result_hash_schema_version=version)
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="application.*schema"
    ):
        module._validate_result_envelope(corrupted)


def test_application_result_schema_two_remains_accepted() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    assert result.application_result_hash_schema_version == 2
    module._validate_result_envelope(result)


@pytest.mark.parametrize(
    "feature_id",
    ["None", "nan", "<NA>", "/tmp/feature", r"C:\feature", " GPU:F "],
)
def test_noncanonical_feature_ids_are_rejected(feature_id: str) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="Feature ID"):
        _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))


def test_current_gpu_feature_id_is_canonical() -> None:
    feature_id = "GPU:DOC:prescription_surface:FEATURE-01"
    result = _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))
    assert result.parcels.iloc[0].bess_cnig_selected_feature_ids_json == (
        f'["{feature_id}"]'
    )


def test_authorized_status_artifact_fails_local_verified_byte_loading(
    tmp_path: Path,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation()]))
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_parcel_precheck_status"] = "AUTHORIZED"
    assessed = result.relation_assessments.copy(deep=True)
    assessed.loc[assessed.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"
    assessed.loc[assessed.index[0], "bess_cnig_resulting_parcel_precheck_status"] = (
        "AUTHORIZED"
    )
    source = assessed.drop(columns=list(RELATION_COLUMNS))
    corrupted = replace(
        result,
        parcels=parcels,
        relation_assessments=assessed,
        source_application_relations_content_sha256=module._frame_sha256(
            source,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
    )
    corrupted = module._result_with_hashes(corrupted)
    manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


@pytest.mark.parametrize(
    "factory",
    [
        _duplicate_selected_pair_result,
        _invalid_lower_feature_id_result,
        _cross_parcel_priority_conflict_result,
    ],
    ids=["duplicate-pair", "invalid-lower-feature-id", "global-priority-conflict"],
)
def test_coordinated_relation_identity_artifact_corruption_fails_locally(
    tmp_path: Path,
    factory: object,
) -> None:
    assert callable(factory)
    corrupted = factory()
    manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


def test_relation_identity_and_global_mapping_fail_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, _ = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    for corrupted in (
        _duplicate_selected_pair_result(),
        _invalid_lower_feature_id_result(),
        _cross_parcel_priority_conflict_result(),
    ):
        with pytest.raises(BessPlanningFeatureParcelAggregationError):
            validate_bess_planning_feature_parcel_aggregation_result(
                *inputs, coded, config, policy, application, corrupted
            )
    assert calls == 0


@pytest.mark.parametrize(
    "status",
    [
        "ALLOWED",
        "AUTHORIZED",
        "COMPATIBLE",
        "CLEAR",
        "FORBIDDEN",
        "PROHIBITED",
        "BLOCKED",
        "BUILDABLE",
    ],
)
def test_parcel_decision_status_domain_rejects_forbidden_vocabulary(
    status: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    parcels = result.parcels.copy(deep=True)
    decision_index = parcels.index[
        parcels["bess_cnig_parcel_aggregation_status"] == "AGGREGATED_EXACT_POLICY"
    ][0]
    parcels.loc[decision_index, "bess_cnig_parcel_precheck_status"] = status
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="status"):
        module._validate_result_envelope(corrupted)


@pytest.mark.parametrize(
    "json_value",
    [
        '["None"]',
        '["nan"]',
        '["<NA>"]',
        '["/tmp/feature"]',
        r'["C:\\feature"]',
        '[" GPU:F "]',
        '["B","A"]',
        '["A", "B"]',
        '["A","A"]',
    ],
)
def test_persisted_feature_id_json_must_be_portable_and_canonical(
    json_value: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_selected_feature_ids_json"] = json_value
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)


def test_representative_intrinsic_failures_all_precede_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, result = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    invalid_results: list[BessPlanningFeatureParcelAggregationResult] = []

    inherited = result.relation_assessments.copy(deep=True)
    inherited.loc[inherited.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"
    invalid_results.append(
        _rehash_coordinated_result(replace(result, relation_assessments=inherited))
    )

    parcel_status = result.parcels.copy(deep=True)
    parcel_status.loc[parcel_status.index[0], "bess_cnig_parcel_precheck_status"] = (
        "AUTHORIZED"
    )
    invalid_results.append(
        module._result_with_hashes(replace(result, parcels=parcel_status))
    )

    ambiguous = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A", priority=50),
                _relation(
                    feature_id="B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=10,
                ),
            ]
        )
    )
    ambiguous_relations = ambiguous.relation_assessments.copy(deep=True)
    ambiguous_relations.loc[
        ambiguous_relations.index[1], "bess_cnig_status_priority"
    ] = 50
    invalid_results.append(
        _rehash_coordinated_result(
            replace(ambiguous, relation_assessments=ambiguous_relations)
        )
    )

    point_parcels = result.parcels.copy(deep=True)
    point_parcels.at[point_parcels.index[0], point_parcels.geometry.name] = Point(0, 0)
    invalid_results.append(replace(result, parcels=point_parcels))

    duplicate = pd.concat([result.parcels, result.parcels.iloc[:, [0]]], axis=1)
    invalid_results.append(
        replace(
            result,
            parcels=gpd.GeoDataFrame(
                duplicate,
                geometry=result.parcels.geometry.name,
                crs=result.parcels.crs,
            ),
        )
    )
    invalid_results.append(
        module._result_with_hashes(
            replace(result, application_result_hash_schema_version=3)
        )
    )

    json_parcels = result.parcels.copy(deep=True)
    json_parcels.loc[json_parcels.index[0], "bess_cnig_selected_feature_ids_json"] = (
        '["/tmp/feature"]'
    )
    invalid_results.append(
        module._result_with_hashes(replace(result, parcels=json_parcels))
    )

    for invalid in invalid_results:
        with pytest.raises(BessPlanningFeatureParcelAggregationError):
            validate_bess_planning_feature_parcel_aggregation_result(
                *inputs, coded, config, policy, application, invalid
            )
    assert calls == 0


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
        lambda value: value.update(application_result_hash_schema_version=1),
        lambda value: value.update(application_result_hash_schema_version=3),
        lambda value: value.update(application_result_hash_schema_version=999),
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
