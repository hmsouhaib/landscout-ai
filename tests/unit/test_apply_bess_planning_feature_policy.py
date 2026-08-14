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
from shapely import from_wkt, get_coordinate_dimension, to_wkb
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
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
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
)
BOUNDARY_FLAG_COLUMNS = (
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
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
        "schema_version": 2,
        "artifact_kind": "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT",
        **{name: getattr(result, name) for name in scalar_names},
        "artifacts": records,
    }
    validated = BessPlanningFeatureApplicationArtifactManifest.model_validate(manifest)
    assert validated.schema_version == 2
    manifest_path = tmp_path / "application.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    assert module is not None
    return manifest_path, paths, manifest


def _coordinated_policy_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: object,
    *,
    dtype: str | None = None,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    feature_id = str(result.relations.iloc[0]["planning_feature_id"])
    changed = result
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            values = frame[column].tolist()
            for position, selected in enumerate(mask.tolist()):
                if selected:
                    values[position] = value
            if dtype == "category":
                frame[column] = pd.Series(pd.Categorical(values), index=frame.index)
            elif dtype is not None:
                frame[column] = pd.Series(values, index=frame.index, dtype=dtype)
            else:
                frame.loc[mask, column] = value
            changed = replace(changed, **{frame_name: frame})
    relation_frame = changed.relations.copy(deep=True)
    relation_mask = relation_frame["planning_feature_id"].eq(feature_id)
    relation_values = relation_frame[column].tolist()
    for position, selected in enumerate(relation_mask.tolist()):
        if selected:
            relation_values[position] = value
    if dtype == "category":
        relation_frame[column] = pd.Series(
            pd.Categorical(relation_values), index=relation_frame.index
        )
    elif dtype is not None:
        relation_frame[column] = pd.Series(
            relation_values, index=relation_frame.index, dtype=dtype
        )
    else:
        relation_frame.loc[relation_mask, column] = value
    return module._result_with_hashes(replace(changed, relations=relation_frame))


def _coordinated_feature_id_mutation(
    result: BessPlanningFeatureApplicationResult,
    feature_id: object,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    original = result.relations.iloc[0]["planning_feature_id"]
    changed = result
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        frame.loc[frame["planning_feature_id"].eq(original), "planning_feature_id"] = (
            feature_id
        )
        changed = replace(changed, **{frame_name: frame})
    relations = changed.relations.copy(deep=True)
    relations.loc[
        relations["planning_feature_id"].eq(original), "planning_feature_id"
    ] = feature_id
    return module._result_with_hashes(replace(changed, relations=relations))


def _zero_relation_feature(
    result: BessPlanningFeatureApplicationResult,
) -> tuple[str, gpd.GeoDataFrame, object]:
    related = set(result.relations["planning_feature_id"])
    for name in ("surface_features", "line_features", "point_features"):
        frame = getattr(result, name)
        unmatched = frame.loc[~frame["planning_feature_id"].isin(related)]
        if not unmatched.empty:
            return name, frame, unmatched.index[0]
    raise AssertionError("fixture must contain a feature having zero relations")


def _surface_touch_with_positive_area(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    assert relations.loc[index, "intersection_area_m2"] > 0
    relations.loc[index, "relation_type"] = "TOUCH_ONLY"
    return module._result_with_hashes(replace(result, relations=relations))


def _z_geometry(kind: str) -> object:
    polygon = Polygon([(0, 0, 7), (2, 0, 7), (2, 2, 7), (0, 2, 7)])
    line = LineString([(0, 0, 7), (2, 0, 7)])
    point = Point(1, 1, 7)
    return {
        "Polygon": polygon,
        "MultiPolygon": MultiPolygon([polygon]),
        "LineString": line,
        "MultiLineString": MultiLineString([line]),
        "Point": point,
        "MultiPoint": MultiPoint([point]),
    }[kind]


def test_exact_policy_is_applied_to_every_feature_and_relation() -> None:
    _, coded, policy_config, policy, result = _application_fixture()
    assert result.result_hash_schema_version == 2
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


def test_every_output_row_has_all_six_false_boundary_flags() -> None:
    _, _, _, _, result = _application_fixture()
    for frame in (
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    ):
        assert all(column in frame.columns for column in BOUNDARY_FLAG_COLUMNS)
        for column in BOUNDARY_FLAG_COLUMNS:
            assert str(frame[column].dtype) == "bool"
            assert frame[column].notna().all()
            assert frame[column].eq(False).all()


def test_policy_suffix_has_one_exact_deterministic_dtype_schema() -> None:
    _, _, _, _, result = _application_fixture()
    expected = {
        column: "str"
        for column in POLICY_COLUMNS
        if column
        not in {
            "bess_cnig_status_priority",
            *BOUNDARY_FLAG_COLUMNS,
        }
    }
    expected["bess_cnig_status_priority"] = "Int64"
    expected.update({column: "bool" for column in BOUNDARY_FLAG_COLUMNS})
    for frame in (
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    ):
        assert tuple(frame.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
        assert {column: str(frame[column].dtype) for column in POLICY_COLUMNS} == (
            expected
        )


def test_schema_v1_dimension_blind_hash_representation_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    original = surface.geometry.iloc[0]
    polygon_z = Polygon([(x, y, 7) for x, y in original.exterior.coords])
    assert get_coordinate_dimension(original) == 2
    assert get_coordinate_dimension(polygon_z) == 3
    assert to_wkb(original, hex=True, output_dimension=2) == to_wkb(
        polygon_z, hex=True, output_dimension=2
    )
    surface.at[surface.index[0], surface.geometry.name] = polygon_z
    blind = replace(result, surface_features=surface)
    assert blind.surface_features_content_sha256 == (
        result.surface_features_content_sha256
    )
    assert blind.complete_result_content_sha256 == result.complete_result_content_sha256
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._validate_result_envelope(blind)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._result_with_hashes(blind)


@pytest.mark.parametrize(
    ("frame_name", "geometry_kind"),
    [
        ("surface_features", "Polygon"),
        ("surface_features", "MultiPolygon"),
        ("line_features", "LineString"),
        ("line_features", "MultiLineString"),
        ("point_features", "Point"),
        ("point_features", "MultiPoint"),
    ],
)
def test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
    frame_name: str,
    geometry_kind: str,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    frame = getattr(result, frame_name).copy(deep=True)
    frame.at[frame.index[0], frame.geometry.name] = _z_geometry(geometry_kind)
    changed = replace(result, **{frame_name: frame})
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0


@pytest.mark.parametrize("wkt", ["POINT M (1 1 7)", "POINT ZM (1 1 7 8)"])
def test_m_and_zm_application_geometries_are_rejected(wkt: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    point = result.point_features.copy(deep=True)
    point.at[point.index[0], point.geometry.name] = from_wkt(wkt)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._validate_result_envelope(replace(result, point_features=point))


def test_valid_empty_optional_application_catalog_retains_schema_and_crs() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, coded, _, policy, _ = _application_fixture()
    empty = coded.point_features.iloc[0:0].copy()
    applied = module._apply_feature_catalog(empty, policy)
    assert applied.empty
    assert tuple(applied.columns[: len(empty.columns)]) == tuple(empty.columns)
    assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
    assert applied.geometry.name == empty.geometry.name
    assert applied.crs == empty.crs
    module._validate_application_geometry(applied, "empty point features")


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


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_feature_id", "MUTATED"),
        ("source_identity_kind", "MUTATED"),
        ("source_identity_field", "MUTATED"),
        ("logical_layer", "information_surface"),
        ("label_raw", "MUTATED"),
        ("text_raw", "MUTATED"),
        ("source_document_id", "MUTATED"),
        ("source_archive_sha256", "f" * 64),
        ("source_layer", "MUTATED"),
        ("source_validity_date_raw", "2099-01-01"),
        ("regulation_filename_raw", "MUTATED.pdf"),
        ("official_code_label", "MUTATED"),
        ("official_code_profile", "MUTATED"),
        ("feature_area_m2", 999.0),
    ],
)
def test_complete_relation_facts_must_match_referenced_feature(
    column: str, value: object
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    relations.loc[index, column] = value
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="relation|feature"):
        module._validate_result_envelope(changed)


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


def test_duplicate_application_relation_pair_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = pd.concat([result.relations, result.relations.iloc[[0]]])
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature", r"C:\feature", " GPU:F "],
)
def test_application_relation_feature_id_is_exact_and_portable(
    feature_id: object,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_feature_id_mutation(result, feature_id)
    with pytest.raises(BessPlanningFeatureApplicationError, match="feature|identity"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize("parcel_id", [None, "", "None", " PARCEL-1 "])
def test_application_relation_parcel_id_is_exact(parcel_id: object) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = parcel_id
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="parcel|identity"):
        module._validate_result_envelope(changed)


def test_unknown_application_relation_type_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "relation_type"] = "BUFFERED_NEARBY"
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="relation type"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("bess_cnig_precheck_status", "AUTHORIZED", "status|domain"),
        ("bess_cnig_precheck_status", "FORBIDDEN", "status|domain"),
        ("bess_cnig_precheck_status", "PROHIBITED", "status|domain"),
        ("bess_cnig_precheck_confidence", "CERTAIN", "confidence|domain"),
        ("bess_cnig_status_priority", 0, "priority|positive"),
        ("bess_cnig_status_priority", -1, "priority|positive"),
        ("bess_cnig_rationale", "", "rationale|exact|non-empty"),
        ("bess_cnig_rationale", " leading", "rationale|exact|whitespace"),
        ("bess_cnig_required_human_action", "trailing ", "action|exact|whitespace"),
        ("bess_cnig_limitations", "", "limitations|exact|non-empty"),
    ],
)
def test_coordinated_invalid_policy_domains_fail_local_validation(
    column: str,
    value: object,
    message: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, value)
    with pytest.raises(BessPlanningFeatureApplicationError, match=message):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize("literal", ["None", "nan", "<NA>"])
def test_literal_null_replacements_are_rejected(literal: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, "bess_cnig_rationale", literal)
    with pytest.raises(BessPlanningFeatureApplicationError, match="literal|missing"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("column", "dtype", "value"),
    [
        ("bess_cnig_precheck_status", "object", "UNKNOWN"),
        ("bess_cnig_precheck_confidence", "category", "HIGH"),
        ("bess_cnig_rationale", "object", "Still a factual policy rationale."),
        ("bess_cnig_status_priority", "Float64", 1.0),
        ("bess_cnig_status_priority", "str", "1"),
        ("bess_cnig_parcel_status_aggregated", "boolean", False),
    ],
)
def test_self_consistent_wrong_policy_suffix_dtype_is_rejected(
    column: str,
    dtype: str,
    value: object,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, value, dtype=dtype)
    with pytest.raises(BessPlanningFeatureApplicationError, match="dtype|schema"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("official_status", "application_status"),
    [
        ("RESOLVED_OFFICIAL", "UNRESOLVED_CODE_PAIR"),
        ("UNKNOWN_CODE_PAIR", "APPLIED_EXACT_POLICY"),
    ],
)
def test_official_and_application_statuses_cannot_contradict(
    official_status: str,
    application_status: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_policy_application_status",
        application_status,
    )
    feature_id = str(changed.relations.iloc[0]["planning_feature_id"])
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            frame.loc[mask, "official_code_status"] = official_status
            changed = replace(changed, **{frame_name: frame})
    relation_frame = changed.relations.copy(deep=True)
    relation_frame.loc[
        relation_frame["planning_feature_id"].eq(feature_id), "official_code_status"
    ] = official_status
    changed = module._result_with_hashes(replace(changed, relations=relation_frame))
    with pytest.raises(BessPlanningFeatureApplicationError, match="official|status"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize("column", BOUNDARY_FLAG_COLUMNS)
def test_any_true_row_boundary_flag_is_rejected(column: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, True)
    with pytest.raises(BessPlanningFeatureApplicationError, match="flag|false"):
        module._validate_result_envelope(changed)


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


def test_duplicate_relation_pair_artifact_fails_local_loading(tmp_path: Path) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = pd.concat([result.relations, result.relations.iloc[[0]]])
    changed = module._result_with_hashes(replace(result, relations=relations))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_document_wide_mapping_conflict_artifact_fails_local_loading(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    first = result.relations.iloc[0]
    different = result.relations[
        result.relations["bess_cnig_precheck_status"].ne(
            first["bess_cnig_precheck_status"]
        )
    ].iloc[0]
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_status_priority",
        int(different["bess_cnig_status_priority"]),
    )
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="priority|mapping"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    changed = _surface_touch_with_positive_area(result)
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="surface|metric|type"
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_wrong_2d_feature_geometry_fails_local_artifact_loading(tmp_path: Path) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    surface.at[surface.index[0], surface.geometry.name] = Point(0, 0)
    changed = module._result_with_hashes(replace(result, surface_features=surface))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="surface|geometry"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


@pytest.mark.parametrize(
    ("frame_name", "geometry"),
    [
        ("surface_features", Point(0, 0)),
        ("line_features", Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])),
        ("point_features", LineString([(0, 0), (1, 1)])),
        ("surface_features", Polygon()),
        (
            "surface_features",
            Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        ),
    ],
    ids=["surface-point", "line-polygon", "point-line", "empty", "invalid"],
)
def test_feature_catalog_geometry_role_is_intrinsic(
    frame_name: str, geometry: object
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    frame.at[frame.index[0], frame.geometry.name] = geometry
    changed = module._result_with_hashes(replace(result, **{frame_name: frame}))
    with pytest.raises(BessPlanningFeatureApplicationError, match="geometry"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("frame_name", "metric"),
    [
        ("surface_features", "feature_area_m2"),
        ("line_features", "feature_length_m"),
        ("point_features", "point_member_count"),
    ],
)
def test_feature_catalog_metric_must_match_geometry(
    frame_name: str, metric: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    frame.loc[frame.index[0], metric] += 1
    changed = module._result_with_hashes(replace(result, **{frame_name: frame}))
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="metric|geometry|count"
    ):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_id", "GPU:malformed"),
        ("logical_layer", "prescription_line"),
        ("geometry_kind", "LINE"),
    ],
)
def test_unreferenced_feature_catalog_identity_fields_are_intrinsic(
    column: str, value: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, column] = value
    changed = module._result_with_hashes(replace(result, **{name: frame}))
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="identity|layer|kind"
    ):
        module._validate_result_envelope(changed)


def test_feature_catalog_requires_canonical_crs_and_global_identity() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.to_crs("EPSG:4326")
    with pytest.raises(BessPlanningFeatureApplicationError, match="EPSG:2154|CRS"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, surface_features=surface))
        )
    point = result.point_features.copy(deep=True)
    point.loc[point.index[0], "planning_feature_id"] = result.surface_features.iloc[0][
        "planning_feature_id"
    ]
    with pytest.raises(BessPlanningFeatureApplicationError, match="identity|unique"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, point_features=point))
        )


@pytest.mark.parametrize("feature_id", ["None", "/tmp/feature", r"C:\feature", " bad "])
def test_unreferenced_feature_identity_is_validated_locally(
    tmp_path: Path, feature_id: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, "planning_feature_id"] = feature_id
    changed = module._result_with_hashes(replace(result, **{name: frame}))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="feature|identity|GPU"
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_unreferenced_feature_participates_in_global_policy_mapping(
    tmp_path: Path,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    status = frame.loc[index, "bess_cnig_precheck_status"]
    conflicting = pd.concat(
        [result.surface_features, result.line_features, result.point_features],
        ignore_index=True,
    )
    conflicting = conflicting.loc[conflicting["bess_cnig_precheck_status"].ne(status)]
    frame.loc[index, "bess_cnig_status_priority"] = int(
        conflicting.iloc[0]["bess_cnig_status_priority"]
    )
    changed = module._result_with_hashes(replace(result, **{name: frame}))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="priority|mapping"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


@pytest.mark.parametrize("policy_schema", [0, 2, 999])
def test_application_locks_policy_result_schema_exactly(policy_schema: int) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = module._result_with_hashes(
        replace(result, policy_result_hash_schema_version=policy_schema)
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="policy.*schema"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize("cnig_schema", [1, 4, 6, 999])
def test_application_locks_cnig_result_schema_exactly(cnig_schema: int) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = module._result_with_hashes(
        replace(result, cnig_result_hash_schema_version=cnig_schema)
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="CNIG|cnig.*schema"):
        module._validate_result_envelope(changed)


def test_application_accepts_only_current_policy_and_cnig_source_schemas() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    assert result.policy_result_hash_schema_version == 1
    assert result.cnig_result_hash_schema_version == 5
    module._validate_result_envelope(result)


def test_duplicate_relation_identity_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    relations = pd.concat(
        [result.relations, result.relations.iloc[[0]]], ignore_index=True
    )
    changed = module._result_with_hashes(replace(result, relations=relations))
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0


def test_self_consistent_z_geoparquet_artifact_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    original = surface.geometry.iloc[0]
    surface.at[surface.index[0], surface.geometry.name] = Polygon(
        [(x, y, 9) for x, y in original.exterior.coords]
    )
    changed = replace(result, surface_features=surface)
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_self_consistent_wrong_dtype_artifact_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_precheck_status",
        "UNKNOWN",
        dtype="object",
    )
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="dtype|schema"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value.update(schema_version=1), "schema"),
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
        '{"schema_version": 2, "schema_version": 2}\n', encoding="utf-8"
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
