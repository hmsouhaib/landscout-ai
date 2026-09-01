from __future__ import annotations

import importlib
import inspect
import json
from collections.abc import Mapping
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
    _canonical_empty_policy_result,
    _checked_in_policy_result,
    _compiled_fixture,
)
from test_resolve_planning_feature_codes import _canonical_empty_coded_result

from landscout import stages
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationArtifactRecord,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)
from landscout.stages.apply_bess_planning_feature_policy import (
    load_bess_planning_feature_application_artifacts as _load_application_artifacts,
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
_LAST_CODED_RESULT: object | None = None
_LAST_POLICY_RESULT: object | None = None


def _application_artifact_record_payload() -> dict[str, object]:
    crs = {
        "type": "ProjectedCRS",
        "name": "RGF93 v1 / Lambert-93",
        "coordinate_system": {"axis": [{"name": "Easting"}]},
    }
    return {
        "artifact_role": "SURFACE_FEATURES",
        "filename": "surface.parquet",
        "row_count": 1,
        "size_bytes": 1,
        "sha256": "a" * 64,
        "frame_schema_signature": {
            "columns": ["geometry"],
            "dtypes": ["geometry"],
            "index_class": "pandas.core.indexes.range.RangeIndex",
            "index_names": [None],
            "index_level_dtypes": ["int64"],
            "geometry_column": "geometry",
            "crs": crs,
        },
        "geospatial": True,
        "crs": crs,
    }


def test_application_artifact_record_is_deeply_immutable_without_aliases() -> None:
    payload = _application_artifact_record_payload()
    record = BessPlanningFeatureApplicationArtifactRecord.model_validate(payload)

    payload_signature = payload["frame_schema_signature"]
    assert isinstance(payload_signature, dict)
    payload_columns = payload_signature["columns"]
    assert isinstance(payload_columns, list)
    payload_columns.append("caller_mutation")
    payload_crs = payload["crs"]
    assert isinstance(payload_crs, dict)
    payload_crs["caller_mutation"] = True

    assert record.frame_schema_signature["columns"] == ("geometry",)
    assert record.crs is not None
    assert "caller_mutation" not in record.crs
    assert record.model_dump(mode="json", warnings="error") == (
        _application_artifact_record_payload()
    )
    with pytest.raises(TypeError, match="frozen"):
        record.frame_schema_signature["new"] = "value"
    with pytest.raises(AttributeError):
        record.frame_schema_signature["columns"].append("new")
    with pytest.raises(TypeError, match="frozen"):
        record.crs["new"] = "value"
    coordinate_system = record.crs["coordinate_system"]
    assert isinstance(coordinate_system, Mapping)
    with pytest.raises(TypeError, match="frozen"):
        coordinate_system["new"] = "value"


def _application_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    BessPlanningFeatureApplicationResult,
]:
    global _LAST_CODED_RESULT, _LAST_POLICY_RESULT
    inputs, coded, config, policy = _compiled_fixture()
    result = apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    _LAST_CODED_RESULT = coded
    _LAST_POLICY_RESULT = policy
    return inputs, coded, config, policy, result


def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
    coded_result: object | None = None,
    policy_result: object | None = None,
) -> BessPlanningFeatureApplicationResult:
    """Test adapter supplying the newly mandatory exact upstream envelopes."""

    if coded_result is None or policy_result is None:
        coded_result = _LAST_CODED_RESULT
        policy_result = _LAST_POLICY_RESULT
    assert coded_result is not None
    assert policy_result is not None
    return _load_application_artifacts(
        manifest_path,
        surface_features_path,
        line_features_path,
        point_features_path,
        relations_path,
        coded_result,
        policy_result,
    )


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
    relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
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


@pytest.mark.parametrize(
    "document",
    [
        '{"schema_version": 2, "schema_version": 2}\n',
        '{"schema_version": NaN}\n',
        '{"schema_version": Infinity}\n',
        "[]\n",
    ],
    ids=["duplicate-key", "nan", "infinity", "non-object"],
)
def test_application_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    manifest_path.write_text(document, encoding="utf-8")
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    artifact_reads = 0
    original_read_bytes = Path.read_bytes

    def counted_bytes(path: Path) -> bytes:
        nonlocal artifact_reads
        if path in paths.values():
            artifact_reads += 1
        return original_read_bytes(path)

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal artifact_reads
        artifact_reads += 1
        raise AssertionError("Artifact read preceded strict manifest validation")

    monkeypatch.setattr(Path, "read_bytes", counted_bytes)
    monkeypatch.setattr(module.pd, "read_parquet", counted)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="Duplicate JSON|finite|top-level|invalid",
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
    assert artifact_reads == 0


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
        "validate_bess_planning_feature_application_result_envelope",
    }
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
    assert not any(name.startswith("_") for name in module.__all__)


def _replace_application_frame(
    result: BessPlanningFeatureApplicationResult,
    frame_name: str,
    frame: pd.DataFrame,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    return module._result_with_hashes(replace(result, **{frame_name: frame}))


def _coordinated_referenced_lineage_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: str,
    *,
    rename_id: bool = False,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    feature_id = str(result.relations.iloc[0]["planning_feature_id"])
    changed = result
    replacement_id = feature_id
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            frame.loc[mask, column] = value
            if rename_id:
                row = frame.loc[mask].iloc[0]
                replacement_id = (
                    f"GPU:{row['source_document_id']}:"
                    f"{row['logical_layer']}:{row['source_feature_id']}"
                )
                frame.loc[mask, "planning_feature_id"] = replacement_id
            changed = replace(changed, **{frame_name: frame})
    relations = changed.relations.copy(deep=True)
    mask = relations["planning_feature_id"].eq(feature_id)
    relations.loc[mask, column] = value
    if rename_id:
        relations.loc[mask, "planning_feature_id"] = replacement_id
    return module._result_with_hashes(replace(changed, relations=relations))


def test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, "source_document_id"] = "MUTATED-DOCUMENT"
    frame.loc[index, "planning_feature_id"] = (
        f"GPU:MUTATED-DOCUMENT:{frame.loc[index, 'logical_layer']}:"
        f"{frame.loc[index, 'source_feature_id']}"
    )
    changed = _replace_application_frame(result, name, frame)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="document|lineage"):
        load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


@pytest.mark.parametrize(
    "mutation",
    ["archive", "official-profile", "envelope-document"],
)
def test_feature_row_lineage_must_match_application_envelope(mutation: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    if mutation == "envelope-document":
        changed = module._result_with_hashes(
            replace(result, source_document_id="MUTATED-DOCUMENT")
        )
    else:
        name, source, index = _zero_relation_feature(result)
        frame = source.copy(deep=True)
        if mutation == "archive":
            frame.loc[index, "source_archive_sha256"] = "f" * 64
        else:
            frame.loc[index, "official_code_profile"] = "mutated_profile"
            frame.loc[index, "official_code_profile_sha256"] = "f" * 64
        changed = _replace_application_frame(result, name, frame)
    with pytest.raises(BessPlanningFeatureApplicationError, match="lineage|document"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("column", "value", "rename_id"),
    [
        ("source_document_id", "MUTATED-DOCUMENT", True),
        ("source_archive_sha256", "f" * 64, False),
    ],
)
def test_coordinated_referenced_row_lineage_cannot_bypass_envelope(
    column: str,
    value: str,
    rename_id: bool,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_referenced_lineage_mutation(
        result, column, value, rename_id=rename_id
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="lineage|document"):
        module._validate_result_envelope(changed)


def test_resolved_official_row_requires_label_and_envelope_profile() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    for column, value in (
        ("official_code_label", pd.NA),
        ("official_code_profile", "wrong_profile"),
    ):
        frame = source.copy(deep=True)
        frame.loc[index, column] = value
        changed = _replace_application_frame(result, name, frame)
        with pytest.raises(
            BessPlanningFeatureApplicationError, match="official|profile|label"
        ):
            module._validate_result_envelope(changed)


def test_unknown_official_row_rejects_invented_label_or_url() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    for invented_column in ("official_code_label", "official_code_source_url"):
        frame = source.copy(deep=True)
        frame.loc[index, "official_code_status"] = "UNKNOWN_CODE_PAIR"
        frame.loc[index, "bess_cnig_policy_application_status"] = "UNRESOLVED_CODE_PAIR"
        for column in (
            "official_code_label",
            "official_legal_reference",
            "official_regulation_reference",
            "official_code_source_url",
            "bess_cnig_precheck_status",
            "bess_cnig_precheck_confidence",
            "bess_cnig_rationale",
            "bess_cnig_required_human_action",
            "bess_cnig_limitations",
        ):
            frame.loc[index, column] = pd.NA
        frame.loc[index, "bess_cnig_status_priority"] = pd.NA
        frame.loc[index, invented_column] = (
            "Invented label"
            if invented_column == "official_code_label"
            else "https://example.invalid/invented"
        )
        changed = _replace_application_frame(result, name, frame)
        with pytest.raises(BessPlanningFeatureApplicationError, match="official|null"):
            module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("frame_name", "mutation"),
    [
        ("surface_features", "missing-column"),
        ("surface_features", "unexpected-column"),
        ("surface_features", "reordered-columns"),
        ("surface_features", "metric-object"),
        ("line_features", "metric-object"),
        ("point_features", "metric-object"),
        ("surface_features", "official-object"),
        ("surface_features", "index-name"),
        ("surface_features", "index-dtype"),
        ("point_features", "malformed-empty"),
    ],
)
def test_application_feature_prefix_has_exact_canonical_schema(
    frame_name: str,
    mutation: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    if mutation == "missing-column":
        frame = frame.drop(columns="regulation_url_raw")
    elif mutation == "unexpected-column":
        position = frame.columns.get_loc(POLICY_COLUMNS[0])
        frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))
    elif mutation == "reordered-columns":
        columns = list(frame.columns)
        columns[0], columns[1] = columns[1], columns[0]
        frame = frame.loc[:, columns]
    elif mutation == "metric-object":
        metric = {
            "surface_features": "feature_area_m2",
            "line_features": "feature_length_m",
            "point_features": "point_member_count",
        }[frame_name]
        frame[metric] = pd.Series(
            frame[metric].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "official-object":
        frame["official_legal_reference"] = pd.Series(
            frame["official_legal_reference"].tolist(),
            index=frame.index,
            dtype="object",
        )
    elif mutation == "index-name":
        frame.index = frame.index.rename("wrong")
    elif mutation == "index-dtype":
        frame.index = pd.Index(frame.index.to_numpy(dtype="int32"), dtype="int32")
    else:
        frame = frame.iloc[0:0].copy()
        frame["point_member_count"] = pd.Series(dtype="object")
    changed = _replace_application_frame(result, frame_name, frame)
    with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype|index"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    "mutation",
    [
        "missing-column",
        "unexpected-column",
        "reordered-columns",
        "float-object",
        "count-object",
        "official-category",
        "malformed-empty",
    ],
)
def test_application_relation_prefix_has_exact_canonical_schema(
    mutation: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = result.relations.copy(deep=True)
    if mutation == "missing-column":
        frame = frame.drop(columns="label_raw")
    elif mutation == "unexpected-column":
        position = frame.columns.get_loc(POLICY_COLUMNS[0])
        frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))
    elif mutation == "reordered-columns":
        columns = list(frame.columns)
        columns[0], columns[1] = columns[1], columns[0]
        frame = frame.loc[:, columns]
    elif mutation == "float-object":
        frame["intersection_area_m2"] = pd.Series(
            frame["intersection_area_m2"].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "count-object":
        frame["point_member_count"] = pd.Series(
            frame["point_member_count"].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "official-category":
        frame["official_code_label"] = pd.Series(
            pd.Categorical(frame["official_code_label"]), index=frame.index
        )
    else:
        frame = frame.iloc[0:0].drop(columns="label_raw")
    changed = _replace_application_frame(result, "relations", frame)
    with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype"):
        module._validate_result_envelope(changed)


def test_self_consistent_factual_prefix_dtype_artifact_is_rejected(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    surface["feature_area_m2"] = pd.Series(
        surface["feature_area_m2"].tolist(), index=surface.index, dtype="object"
    )
    changed = _replace_application_frame(result, "surface_features", surface)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype"):
        load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_lineage_defect_fast_fails_before_policy_source_validation(
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

    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, "source_archive_sha256"] = "f" * 64
    changed = _replace_application_frame(result, name, frame)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0


def test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    assert tuple(
        inspect.signature(
            module.load_bess_planning_feature_application_artifacts
        ).parameters
    ) == (
        "manifest_path",
        "surface_features_path",
        "line_features_path",
        "point_features_path",
        "relations_path",
        "coded_result",
        "policy_result",
    )
    assert hasattr(module, "validate_bess_planning_feature_application_result_envelope")
    _, _, _, _, result = _application_fixture()
    module.validate_bess_planning_feature_application_result_envelope(result)
    with pytest.raises(BessPlanningFeatureApplicationError, match="hash|invalid"):
        module.validate_bess_planning_feature_application_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )


def test_source_bound_application_loader_rejects_locally_valid_rationale_change(
    tmp_path: Path,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_rationale",
        "A different exact non-empty rationale.",
    )
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream|rebuilt"):
        module.load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
            coded,
            policy,
        )


def test_application_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    _, _, payload = _write_application_artifacts(tmp_path, result)
    payload["artifacts"][1]["filename"] = str(
        payload["artifacts"][0]["filename"]
    ).upper()
    with pytest.raises(ValueError, match="filename|duplicate"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)


def _swap_referenced_feature_values(
    result: BessPlanningFeatureApplicationResult,
    columns: tuple[str, ...],
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    referenced = result.relations.loc[
        result.relations["bess_cnig_policy_application_status"].eq(
            "APPLIED_EXACT_POLICY"
        )
    ]
    first = referenced.iloc[0]
    second = referenced.loc[
        referenced["bess_cnig_precheck_status"].ne(first["bess_cnig_precheck_status"])
    ].iloc[0]
    first_id = str(first["planning_feature_id"])
    second_id = str(second["planning_feature_id"])
    changed = result
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        first_mask = frame["planning_feature_id"].eq(first_id)
        second_mask = frame["planning_feature_id"].eq(second_id)
        if first_mask.any() or second_mask.any():
            for column in columns:
                first_value = first[column]
                second_value = second[column]
                frame.loc[first_mask, column] = second_value
                frame.loc[second_mask, column] = first_value
            changed = replace(changed, **{frame_name: frame})
    relations = changed.relations.copy(deep=True)
    first_mask = relations["planning_feature_id"].eq(first_id)
    second_mask = relations["planning_feature_id"].eq(second_id)
    for column in columns:
        first_value = first[column]
        second_value = second[column]
        relations.loc[first_mask, column] = second_value
        relations.loc[second_mask, column] = first_value
    return module._result_with_hashes(replace(changed, relations=relations))


@pytest.mark.parametrize(
    "columns",
    [
        (
            "bess_cnig_precheck_status",
            "bess_cnig_precheck_confidence",
            "bess_cnig_status_priority",
            "bess_cnig_rationale",
            "bess_cnig_required_human_action",
            "bess_cnig_limitations",
        ),
        (
            "official_code_label",
            "official_legal_reference",
            "official_regulation_reference",
            "official_code_source_url",
        ),
    ],
)
def test_source_bound_loader_rejects_valid_domain_cross_pair_swaps(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    columns: tuple[str, ...],
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    changed = _swap_referenced_feature_values(result, columns)
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    heavy_calls = 0

    def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_policy_result", forbidden_heavy
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
            coded,
            policy,
        )
    assert heavy_calls == 0


@pytest.mark.parametrize("column", ["source_provider", "source_portal"])
def test_source_bound_loader_rejects_factual_prefix_lineage_change(
    tmp_path: Path, column: str
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], column] = f"changed-{column}"
    changed = module._result_with_hashes(replace(result, surface_features=surface))
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )


def test_source_bound_loader_rejects_all_null_raw_column_transition(
    tmp_path: Path,
) -> None:
    _, coded, _, policy, _ = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    policy_module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
    coded_surface = coded.surface_features.copy(deep=True)
    coded_surface["text_raw"] = pd.Series(
        ["source text"] * len(coded_surface), index=coded_surface.index, dtype="str"
    )
    coded_relations = coded.relations.copy(deep=True)
    surface_ids = set(coded_surface["planning_feature_id"])
    coded_relations.loc[
        coded_relations["planning_feature_id"].isin(surface_ids), "text_raw"
    ] = "source text"
    coded_relations["text_raw"] = pd.Series(
        coded_relations["text_raw"].tolist(),
        index=coded_relations.index,
        dtype="str",
    )
    coded = coding_module._result_with_hashes(
        replace(
            coded,
            surface_features=coded_surface,
            relations=coded_relations,
        )
    )
    policy_table = policy.policy_table.copy(deep=True)
    policy_table["cnig_complete_result_content_sha256"] = pd.array(
        [coded.complete_result_content_sha256] * len(policy_table), dtype="str"
    )
    policy = policy_module._result_with_hashes(
        replace(
            policy,
            cnig_complete_result_content_sha256=coded.complete_result_content_sha256,
            policy_table=policy_table,
        )
    )
    result = module._build_result(coded, policy)
    surface = result.surface_features.copy(deep=True)
    surface["text_raw"] = pd.Series(None, index=surface.index, dtype="object")
    relations = result.relations.copy(deep=True)
    mask = relations["geometry_kind"].eq("SURFACE")
    relations.loc[mask, "text_raw"] = pd.NA
    relations["text_raw"] = pd.Series(
        relations["text_raw"].tolist(), index=relations.index, dtype="str"
    )
    changed = module._result_with_hashes(
        replace(result, surface_features=surface, relations=relations)
    )
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )

    reordered = result.surface_features.iloc[::-1].copy(deep=True)
    changed = module._result_with_hashes(replace(result, surface_features=reordered))
    module._validate_result_envelope(changed)
    reordered_dir = tmp_path / "reordered"
    reordered_dir.mkdir()
    manifest, paths, _ = _write_application_artifacts(reordered_dir, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )


def test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering(
    tmp_path: Path,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    name, source, index = _zero_relation_feature(result)
    unreferenced = source.copy(deep=True)
    unreferenced.loc[index, "label_raw"] = "changed unreferenced label"
    changed = module._result_with_hashes(replace(result, **{name: unreferenced}))
    module._validate_result_envelope(changed)
    unreferenced_dir = tmp_path / "unreferenced"
    unreferenced_dir.mkdir()
    manifest, paths, _ = _write_application_artifacts(unreferenced_dir, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )


def test_application_loader_validates_upstreams_and_rebuilds_once_lightweight(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    coded_before = coded.surface_features.copy(deep=True)
    policy_before = policy.policy_table.copy(deep=True)
    actual_coded_envelope = module.validate_planning_feature_code_result_envelope
    actual_policy_envelope = (
        module.validate_bess_planning_feature_policy_result_envelope
    )
    actual_build = module._build_result
    calls = {"coded": 0, "policy": 0, "build": 0, "heavy": 0}

    def coded_envelope(value: object) -> None:
        calls["coded"] += 1
        actual_coded_envelope(value)

    def policy_envelope(value: object) -> None:
        calls["policy"] += 1
        actual_policy_envelope(value)

    def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        return actual_build(*args, **kwargs)

    def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1

    monkeypatch.setattr(
        module, "validate_planning_feature_code_result_envelope", coded_envelope
    )
    monkeypatch.setattr(
        module,
        "validate_bess_planning_feature_policy_result_envelope",
        policy_envelope,
    )
    monkeypatch.setattr(module, "_build_result", build)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
    loaded = module.load_bess_planning_feature_application_artifacts(
        manifest, *paths.values(), coded, policy
    )
    assert (
        loaded.complete_result_content_sha256 == result.complete_result_content_sha256
    )
    assert calls == {"coded": 1, "policy": 1, "build": 1, "heavy": 0}
    assert_geodataframe_equal(coded.surface_features, coded_before)
    assert_frame_equal(policy.policy_table, policy_before)


def test_application_loader_rejects_bad_upstream_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    reads = 0
    original = Path.read_bytes

    def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)

    monkeypatch.setattr(Path, "read_bytes", counted)
    forged = replace(coded, complete_result_content_sha256="0" * 64)
    with pytest.raises(Exception, match="hash|SHA|invalid"):
        _load_application_artifacts(manifest, *paths.values(), forged, policy)
    assert reads == 0


@pytest.mark.parametrize(
    "filename",
    [
        "/tmp/file.parquet",
        "../file.parquet",
        "subdir/file.parquet",
        r"C:\absolute\file.parquet",
        "C:/absolute/file.parquet",
        r"\\server\share\file.parquet",
        r"subdir\file.parquet",
        "CON.parquet",
        "con.PARQUET",
        "NUL.parquet",
        "PRN.parquet",
        "AUX.parquet",
        "CLOCK$.parquet",
        "COM1.parquet",
        "COM9.parquet",
        "LPT1.parquet",
        "LPT9.parquet",
        "COM¹.parquet",
        "COM².parquet",
        "COM³.parquet",
        "LPT¹.parquet",
        "LPT².parquet",
        "LPT³.parquet",
        "file:name.parquet",
        "base.parquet:stream.parquet",
        "file?.parquet",
        "file*.parquet",
        "file<.parquet",
        "file>.parquet",
        "file|.parquet",
        'file".parquet',
        "nul\x00.parquet",
        "line\nbreak.parquet",
        "del\x7f.parquet",
    ],
)
def test_application_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, _, result = _application_fixture()
    _, _, payload = _write_application_artifacts(tmp_path, result)
    payload["artifacts"][0]["filename"] = filename
    with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)


def _compatible_policy_mutation(policy: object, mutation: str) -> object:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    table = policy.policy_table.copy(deep=True)
    scalar_changes: dict[str, object] = {}
    if mutation == "profile-schema":
        scalar_changes["cnig_profile_schema_version"] = 3
    elif mutation == "extra-pair":
        extra = table.iloc[[0]].copy(deep=True)
        extra["type_code"] = pd.array(["98"], dtype="str")
        table = pd.concat([table, extra], ignore_index=True).sort_values(
            ["feature_family", "type_code", "subtype_code"], kind="stable"
        )
        table.index = pd.Index(table.index.to_numpy(), dtype="int64")
    elif mutation == "missing-pair":
        table = table.iloc[:-1].copy(deep=True)
        table.index = pd.Index(range(len(table)), dtype="int64")
    elif mutation == "official-label":
        table.loc[table.index[0], "official_label"] = "Another exact official label"
    elif mutation == "legal-reference":
        table.loc[table.index[0], "official_legal_reference"] = "Changed legal ref"
    elif mutation == "regulation-reference":
        table.loc[table.index[0], "official_regulation_reference"] = (
            "Changed regulation ref"
        )
    elif mutation == "document":
        scalar_changes["source_document_id"] = "OTHER-DOCUMENT"
    elif mutation == "archive":
        scalar_changes["source_archive_sha256"] = "b" * 64
    elif mutation == "profile":
        scalar_changes["cnig_profile"] = "other-cnig-profile"
        table["cnig_profile"] = pd.array(
            ["other-cnig-profile"] * len(table), dtype="str"
        )
    elif mutation == "profile-sha":
        scalar_changes["cnig_profile_sha256"] = "a" * 64
        table["cnig_profile_sha256"] = pd.array(["a" * 64] * len(table), dtype="str")
    else:
        scalar_changes["cnig_complete_result_content_sha256"] = "a" * 64
        table["cnig_complete_result_content_sha256"] = pd.array(
            ["a" * 64] * len(table), dtype="str"
        )
    changed = replace(policy, policy_table=table, **scalar_changes)
    return module._result_with_hashes(changed)


@pytest.mark.parametrize(
    "mutation",
    [
        "profile-schema",
        "extra-pair",
        "missing-pair",
        "official-label",
        "legal-reference",
        "regulation-reference",
        "document",
        "archive",
        "profile",
        "profile-sha",
        "complete-result-sha",
    ],
)
def test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    changed_policy = _compatible_policy_mutation(policy, mutation)
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = {"manifest": 0, "read": 0, "build": 0, "heavy": 0}

    def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")

    def read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("artifact read must not run")

    def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")

    def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1

    monkeypatch.setattr(module, "_read_verified_artifact", read)
    monkeypatch.setattr(module, "_build_result", build)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
    monkeypatch.setattr(Path, "read_text", manifest_read)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="Policy|policy|CNIG|pair|source|schema|official|reference",
    ):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, changed_policy
        )
    assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}


@pytest.mark.parametrize("empty_upstream", ["coded", "policy", "both"])
def test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    empty_upstream: str,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    if empty_upstream in {"coded", "both"}:
        coded = _canonical_empty_coded_result(coded, empty_dictionary=True)
    if empty_upstream in {"policy", "both"}:
        policy = _canonical_empty_policy_result(policy)
    if empty_upstream == "both":
        policy_module = importlib.import_module(
            "landscout.stages.bess_planning_feature_policy"
        )
        policy = policy_module._result_with_hashes(
            replace(
                policy,
                cnig_complete_result_content_sha256=(
                    coded.complete_result_content_sha256
                ),
            )
        )
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = {"manifest": 0, "read": 0, "build": 0, "heavy": 0}

    def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")

    def artifact_read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("Parquet read must not run")

    def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")

    def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1

    monkeypatch.setattr(Path, "read_text", manifest_read)
    monkeypatch.setattr(module, "_read_verified_artifact", artifact_read)
    monkeypatch.setattr(module, "_build_result", build)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="dictionary|policy|table|pair|empty|record|entry",
    ):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
    assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}
