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
from shapely.geometry import Point
from test_bess_planning_feature_policy import (
    _checked_in_policy_result,
    _compiled_fixture,
)

from landscout import stages
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
)

APPLICATION_SCOPE = "FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"
POLICY_COLUMNS = (
    "bess_cnig_policy_application_status",
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
    "bess_cnig_application_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
)
ARTIFACT_FILES = {
    "SURFACE_FEATURES": ("surface.parquet", True),
    "LINE_FEATURES": ("line.parquet", True),
    "POINT_FEATURES": ("point.parquet", True),
    "RELATIONS": ("relations.parquet", False),
}


def _application_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    BessPlanningFeatureApplicationResult,
]:
    inputs, coded, config, policy = _compiled_fixture()
    result = apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    return inputs, coded, config, policy, result


def _small_catalog(*rows: tuple[str, str, str, str, str]) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "planning_feature_id": [row[0] for row in rows],
            "feature_family": [row[1] for row in rows],
            "type_code_raw": [row[2] for row in rows],
            "subtype_code_raw": [row[3] for row in rows],
            "official_code_status": [row[4] for row in rows],
        },
        geometry=[Point(position, position) for position in range(len(rows))],
        crs="EPSG:2154",
    )


def _write_application_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    frames = {
        "SURFACE_FEATURES": result.surface_features,
        "LINE_FEATURES": result.line_features,
        "POINT_FEATURES": result.point_features,
        "RELATIONS": result.relations,
    }
    paths: dict[str, Path] = {}
    records: list[dict[str, object]] = []
    for role, (filename, geospatial) in ARTIFACT_FILES.items():
        path = tmp_path / filename
        frame = frames[role]
        frame.to_parquet(path, index=True)
        paths[role] = path
        signature = deterministic_frame_schema_signature(frame)
        records.append(
            {
                "artifact_role": role,
                "filename": filename,
                "row_count": len(frame),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path.read_bytes()).hexdigest(),
                "frame_schema_signature": signature,
                "geospatial": geospatial,
                "crs": signature.get("crs"),
            }
        )
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeatureApplicationResult)
        if field.name
        not in {"surface_features", "line_features", "point_features", "relations"}
    )
    manifest = {
        "schema_version": 1,
        "artifact_kind": "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT",
        **{name: getattr(result, name) for name in scalar_names},
        "artifacts": records,
    }
    validated = BessPlanningFeatureApplicationArtifactManifest.model_validate(manifest)
    assert validated.schema_version == 1
    manifest_path = tmp_path / "application.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    assert module is not None
    return manifest_path, paths, manifest


def test_exact_policy_is_applied_to_every_feature_and_relation() -> None:
    _, coded, policy_config, policy, result = _application_fixture()
    assert result.result_hash_schema_version == 1
    assert result.application_scope == APPLICATION_SCOPE
    assert result.policy_profile == policy.policy_profile
    assert result.policy_sha256 == policy.policy_sha256
    assert result.policy_complete_result_content_sha256 == (
        policy.complete_result_content_sha256
    )
    lookup = policy.policy_table.set_index(
        ["feature_family", "type_code", "subtype_code"]
    )
    for source, applied in (
        (coded.surface_features, result.surface_features),
        (coded.line_features, result.line_features),
        (coded.point_features, result.point_features),
    ):
        assert tuple(applied.columns[: len(source.columns)]) == tuple(source.columns)
        assert (
            applied["bess_cnig_policy_application_status"]
            .eq("APPLIED_EXACT_POLICY")
            .all()
        )
        for row in applied.itertuples(index=False):
            expected = lookup.loc[
                (row.feature_family, row.type_code_raw, row.subtype_code_raw)
            ]
            assert row.bess_cnig_precheck_status == expected.precheck_status
            assert row.bess_cnig_precheck_confidence == expected.confidence
            assert row.bess_cnig_status_priority == expected.status_priority
            assert row.bess_cnig_rationale == expected.rationale
            assert row.bess_cnig_required_human_action == (
                expected.required_human_action
            )
            assert row.bess_cnig_limitations == expected.limitations
    assert (
        result.relations["bess_cnig_policy_application_status"]
        .eq("APPLIED_EXACT_POLICY")
        .all()
    )
    assert policy_config.policy_scope == result.policy_scope


def test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    policy = _checked_in_policy_result()
    catalog = _small_catalog(
        ("F-1500", "PRESCRIPTION", "15", "00", "RESOLVED_OFFICIAL"),
        ("F-1501", "PRESCRIPTION", "15", "01", "RESOLVED_OFFICIAL"),
        ("F-NO-SUBTYPE", "PRESCRIPTION", "15", "99", "UNKNOWN_CODE_PAIR"),
        ("F-NO-FAMILY", "INFORMATION", "15", "00", "UNKNOWN_CODE_PAIR"),
        ("F-0100", "PRESCRIPTION", "01", "00", "RESOLVED_OFFICIAL"),
    )
    applied = module._apply_feature_catalog(catalog, policy)
    assert applied.loc[0, "bess_cnig_precheck_confidence"] == "MEDIUM"
    assert applied.loc[1, "bess_cnig_precheck_confidence"] == "HIGH"
    assert applied.loc[0, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"
    assert applied.loc[1, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"
    assert applied.loc[2, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
    assert applied.loc[3, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
    assert applied.loc[4, "type_code_raw"] == "01"
    assert applied.loc[4, "subtype_code_raw"] == "00"


def test_unknown_pair_remains_present_with_true_null_decision_fields() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    policy = _checked_in_policy_result()
    catalog = _small_catalog(
        ("F-UNKNOWN", "PRESCRIPTION", "98", "00", "UNKNOWN_CODE_PAIR"),
    )
    applied = module._apply_feature_catalog(catalog, policy)
    assert applied["planning_feature_id"].tolist() == ["F-UNKNOWN"]
    assert applied.loc[0, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
    for column in POLICY_COLUMNS[1:7]:
        assert pd.isna(applied.loc[0, column])
        assert not isinstance(applied.loc[0, column], str)


@pytest.mark.parametrize(
    "row",
    [
        ("F-MISSING", "PRESCRIPTION", "98", "00", "RESOLVED_OFFICIAL"),
        ("F-UNEXPECTED", "PRESCRIPTION", "15", "00", "UNKNOWN_CODE_PAIR"),
    ],
)
def test_inconsistent_official_status_and_policy_match_is_rejected(
    row: tuple[str, str, str, str, str],
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="policy|official"):
        module._apply_feature_catalog(_small_catalog(row), _checked_in_policy_result())


def test_feature_and_relation_inputs_are_preserved_and_not_mutated() -> None:
    inputs, coded, config, policy = _compiled_fixture()
    coded_copies = (
        coded.surface_features.copy(deep=True),
        coded.line_features.copy(deep=True),
        coded.point_features.copy(deep=True),
        coded.relations.copy(deep=True),
    )
    parcels_copy = inputs[1].copy(deep=True)
    result = apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    assert_geodataframe_equal(coded_copies[0], coded.surface_features)
    assert_geodataframe_equal(coded_copies[1], coded.line_features)
    assert_geodataframe_equal(coded_copies[2], coded.point_features)
    assert_frame_equal(coded_copies[3], coded.relations)
    assert_geodataframe_equal(parcels_copy, inputs[1])
    for source, applied in (
        (coded.surface_features, result.surface_features),
        (coded.line_features, result.line_features),
        (coded.point_features, result.point_features),
    ):
        prefix = applied.loc[:, source.columns]
        assert_geodataframe_equal(source, prefix, check_dtype=True, check_crs=True)
        assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
        assert type(applied.index) is type(source.index)
        assert applied.index.equals(source.index)
    relation_prefix = result.relations.loc[:, coded.relations.columns]
    assert_frame_equal(coded.relations, relation_prefix, check_dtype=True)
    assert tuple(result.relations.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS


def test_relations_inherit_only_from_referenced_enriched_feature() -> None:
    _, _, _, _, result = _application_fixture()
    features = pd.concat(
        [
            result.surface_features.drop(columns="geometry"),
            result.line_features.drop(columns="geometry"),
            result.point_features.drop(columns="geometry"),
        ],
        ignore_index=True,
    ).set_index("planning_feature_id")
    for relation in result.relations.itertuples(index=False):
        feature = features.loc[relation.planning_feature_id]
        for column in POLICY_COLUMNS:
            assert getattr(relation, column) == feature[column]


def test_unknown_relation_feature_id_is_rejected() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, coded, _, policy, result = _application_fixture()
    relations = coded.relations.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "GPU:UNKNOWN"
    with pytest.raises(BessPlanningFeatureApplicationError, match="feature ID"):
        module._apply_relations(
            relations,
            result.surface_features,
            result.line_features,
            result.point_features,
        )
    assert policy is not None


def test_scope_has_no_parcel_output_aggregation_rejection_or_score() -> None:
    inputs, _, _, _, result = _application_fixture()
    assert not hasattr(result, "parcels")
    assert result.local_feature_text_interpreted is False
    assert result.local_regulation_content_interpreted is False
    assert result.legal_conclusion_produced is False
    assert result.parcel_status_aggregated is False
    assert result.parcel_rejection_performed is False
    assert result.score_calculated is False
    assert "parcel_id" not in result.surface_features.columns
    assert len(inputs[1]) > 0


def test_coordinated_feature_or_relation_policy_mutation_is_rejected() -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "bess_cnig_precheck_status"] = "UNKNOWN"
    coordinated = module._result_with_hashes(replace(result, surface_features=surface))
    with pytest.raises(BessPlanningFeatureApplicationError, match="rebuilt|feature"):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, coordinated
        )
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "bess_cnig_precheck_confidence"] = "LOW"
    coordinated = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="relation|rebuilt"):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, coordinated
        )


def test_application_and_public_validator_heavy_validation_counts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy = _compiled_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    actual = module.validate_bess_planning_feature_policy_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    result = module.apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    assert calls == 1
    module.validate_bess_planning_feature_application_result(
        *inputs, coded, config, policy, result
    )
    assert calls == 2


def test_malformed_local_result_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    invalid = replace(result, complete_result_content_sha256="f" * 64)
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="hash|SHA|sha256|invalid"
    ):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, invalid
        )
    assert calls == 0


def test_coordinated_application_source_lock_mutation_fast_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    changed = replace(result, policy_sha256="f" * 64)
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        frame["bess_cnig_policy_sha256"] = pd.array(
            ["f" * 64] * len(frame), dtype="str"
        )
        changed = replace(changed, **{frame_name: frame})
    relation_frame = changed.relations.copy(deep=True)
    relation_frame["bess_cnig_policy_sha256"] = pd.array(
        ["f" * 64] * len(relation_frame), dtype="str"
    )
    changed = module._result_with_hashes(replace(changed, relations=relation_frame))
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError, match="source lock"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0


def test_valid_four_file_manifest_and_verified_byte_readback(tmp_path: Path) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    loaded = load_bess_planning_feature_application_artifacts(
        manifest_path,
        paths["SURFACE_FEATURES"],
        paths["LINE_FEATURES"],
        paths["POINT_FEATURES"],
        paths["RELATIONS"],
    )
    assert_geodataframe_equal(result.surface_features, loaded.surface_features)
    assert_geodataframe_equal(result.line_features, loaded.line_features)
    assert_geodataframe_equal(result.point_features, loaded.point_features)
    assert_frame_equal(result.relations, loaded.relations)
    validate_bess_planning_feature_application_result(
        *inputs, coded, config, policy, loaded
    )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value["artifacts"].pop(), "role|artifact"),
        (
            lambda value: value["artifacts"].append(
                {**value["artifacts"][0], "artifact_role": "EXTRA"}
            ),
            "role|artifact",
        ),
        (
            lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
            "duplicate|role|artifact",
        ),
        (
            lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
            "filename",
        ),
        (
            lambda value: value["artifacts"][1].update(
                filename=value["artifacts"][0]["filename"]
            ),
            "duplicate|filename",
        ),
        (
            lambda value: value["artifacts"][0].update(
                filename="C:/absolute/surface.parquet"
            ),
            "filename",
        ),
        (lambda value: value["artifacts"][0].update(size_bytes=1), "size"),
        (lambda value: value["artifacts"][0].update(sha256="f" * 64), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(sha256="bad"), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(row_count=999), "row"),
        (
            lambda value: value["artifacts"][0]["frame_schema_signature"].update(
                index_names=["wrong"]
            ),
            "schema",
        ),
        (lambda value: value["artifacts"][0].update(crs={"wrong": True}), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(crs=None), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(geospatial=False), "geospatial"),
        (lambda value: value.update(unknown=True), "manifest|artifact"),
    ],
)
def test_artifact_manifest_rejects_invalid_contract(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, manifest = _write_application_artifacts(tmp_path, result)
    assert callable(mutation)
    mutation(manifest)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match=message):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_manifest_rejects_duplicate_json_key(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    manifest_path.write_text(
        '{"schema_version": 1, "schema_version": 1}\n', encoding="utf-8"
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="Duplicate JSON"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_artifact_loader_parses_only_verified_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    target = paths["RELATIONS"]
    replacement = tmp_path / "replacement.parquet"
    result.relations.to_parquet(replacement, index=True, compression="gzip")
    original_read_bytes = Path.read_bytes
    verified = original_read_bytes(target)
    replacement_bytes = original_read_bytes(replacement)
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    original_read_parquet = module.pd.read_parquet
    replaced = False
    observed: list[tuple[str, bytes]] = []

    def replace_after_read(path: Path) -> bytes:
        nonlocal replaced
        payload = original_read_bytes(path)
        if path == target and not replaced:
            path.write_bytes(replacement_bytes)
            replaced = True
        return payload

    def observed_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(("buffer", source.getvalue()))
        return original_read_parquet(source, *args, **kwargs)

    monkeypatch.setattr(Path, "read_bytes", replace_after_read)
    monkeypatch.setattr(module.pd, "read_parquet", observed_read)
    loaded = load_bess_planning_feature_application_artifacts(
        manifest_path,
        paths["SURFACE_FEATURES"],
        paths["LINE_FEATURES"],
        paths["POINT_FEATURES"],
        paths["RELATIONS"],
    )
    assert replaced
    assert ("buffer", verified) in observed
    assert_frame_equal(result.relations, loaded.relations)


def test_physical_replacement_before_loading_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    paths["RELATIONS"].write_bytes(paths["RELATIONS"].read_bytes() + b"tamper")
    with pytest.raises(BessPlanningFeatureApplicationError, match="size|SHA|hash"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_public_application_api_exports_only_stable_symbols() -> None:
    required = {
        "BessPlanningFeatureApplicationArtifactManifest",
        "BessPlanningFeatureApplicationError",
        "BessPlanningFeatureApplicationResult",
        "apply_bess_planning_feature_policy",
        "load_bess_planning_feature_application_artifacts",
        "validate_bess_planning_feature_application_result",
    }
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
    assert not any(name.startswith("_") for name in module.__all__)
