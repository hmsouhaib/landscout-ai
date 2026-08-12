from __future__ import annotations

import importlib
import json
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
import yaml  # type: ignore[import-untyped]
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)
from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    _result_with_hashes,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
)

P_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"
I_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"
TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"


def _records_hash(records: list[dict[str, object]]) -> str:
    ordered = sorted(
        records,
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"]),
    )
    payload = json.dumps(
        ordered,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return sha256(payload).hexdigest()


def _payload_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return sha256(encoded).hexdigest()


def _record(
    family: str,
    type_code: str,
    subtype_code: str,
    label: str,
) -> dict[str, object]:
    return {
        "feature_family": family,
        "type_code": type_code,
        "subtype_code": subtype_code,
        "official_label": label,
        "legal_reference": None,
        "regulation_or_annex_reference": None,
        "official_source_url": P_URL if family == "PRESCRIPTION" else I_URL,
    }


def _profile_payload() -> dict[str, object]:
    records = [
        _record("INFORMATION", "02", "00", "Information two"),
        _record("INFORMATION", "99", "00", "Other information"),
        _record("PRESCRIPTION", "07", "00", "Prescription seven"),
        _record("PRESCRIPTION", "07", "04", "Prescription seven subtype four"),
    ]
    return {
        "schema_version": 2,
        "profile": "synthetic_cnig_plu_2017",
        "standard_model": "CNIG PLU v2017",
        "official_text_normalization": TEXT_NORMALIZATION,
        "official_sources": {
            "prescription": P_URL,
            "information": I_URL,
        },
        "retrieval_date": "2026-08-12",
        "canonical_records_sha256": _records_hash(records),
        "records": records,
    }


def _profile() -> CnigFeatureCodeProfile:
    return CnigFeatureCodeProfile.model_validate(_profile_payload())


def _planning_document(standard: str = "CNIG PLU v2017") -> GpuPlanningDocument:
    document = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="https://www.geoportail-urbanisme.gouv.fr",
        commune_code="31395",
        partition="DU_31395",
        document_id="doc-1",
        document_family="DU",
        document_type="PLU",
        document_title=None,
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name="31395_PLU_20240215",
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-08-12T00:00:00Z",
        filename="31395_PLU_20240215.zip",
        archive_format="zip",
        file_size=1,
        sha256="a" * 64,
        path=Path("synthetic.zip"),
        cache_hit=True,
    )
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=Path("synthetic"),
        files=(),
        standard_models=(standard,),
        cache_hit=True,
    )
    zoning_data = gpd.GeoDataFrame(
        {"LIB_IDZONE": ["Z1"]},
        geometry=[Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])],
        crs="EPSG:2154",
    )
    reference = GpuSpatialLayerReference(Path("zones.gpkg"), "ZONE", "GPKG")
    summary = GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer="ZONE",
        crs="EPSG:2154",
        feature_count=1,
        columns=("LIB_IDZONE", "geometry"),
        dtypes=(),
        null_counts=(),
        geometry_types=(("Polygon", 1),),
        null_geometry_count=0,
        empty_geometry_count=0,
        invalid_geometry_count=0,
    )
    zoning = GpuInspectedLayer("zoning", reference, zoning_data, summary)
    return GpuPlanningDocument(extraction, (reference,), zoning, ())


def _base_row(
    feature_id: str,
    source_id: str,
    family: str,
    layer: str,
    kind: str,
    type_code: str,
    subtype_code: str,
) -> dict[str, object]:
    return {
        "planning_feature_id": feature_id,
        "source_feature_id": source_id,
        "source_identity_kind": "CNIG_ATTRIBUTE",
        "source_identity_field": "LIB_IDPSC"
        if family == "PRESCRIPTION"
        else "LIB_IDINFO",
        "logical_layer": layer,
        "feature_family": family,
        "geometry_kind": kind,
        "type_code_raw": type_code,
        "subtype_code_raw": subtype_code,
        "label_raw": None,
        "text_raw": None,
        "regulation_filename_raw": None,
        "regulation_url_raw": None,
        "source_document_reference_raw": "31395_PLU_20240215",
        "source_validity_date_raw": "20240215",
        "source_provider": "Géoportail de l'Urbanisme",
        "source_portal": "https://www.geoportail-urbanisme.gouv.fr",
        "source_commune_code": "31395",
        "source_document_id": "doc-1",
        "source_document_type": "PLU",
        "source_archive_name": "31395_PLU_20240215",
        "source_archive_sha256": "a" * 64,
        "source_layer": layer.upper(),
        "source_standard_model": "CNIG PLU v2017",
        "source_crs": "EPSG:2154",
    }


def _inputs():
    surface_rows = [
        _base_row(
            "F-P-0700",
            "P-1",
            "PRESCRIPTION",
            "prescription_surface",
            "SURFACE",
            "07",
            "00",
        ),
        _base_row(
            "F-I-0200",
            "I-1",
            "INFORMATION",
            "information_surface",
            "SURFACE",
            "02",
            "00",
        ),
    ]
    surface = gpd.GeoDataFrame(
        surface_rows,
        geometry=[
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
            Polygon([(3, 0), (5, 0), (5, 2), (3, 2)]),
        ],
        crs="EPSG:2154",
        index=pd.Index([11, 22], name="source_row"),
    )
    surface["feature_area_m2"] = [4.0, 4.0]
    line = gpd.GeoDataFrame(
        [
            _base_row(
                "F-P-0704",
                "P-2",
                "PRESCRIPTION",
                "prescription_line",
                "LINE",
                "07",
                "04",
            )
        ],
        geometry=[LineString([(0, 0), (2, 0)])],
        crs="EPSG:2154",
        index=pd.Index([33], name="source_row"),
    )
    line["feature_length_m"] = [2.0]
    point = gpd.GeoDataFrame(
        [
            _base_row(
                "F-I-9900",
                "I-2",
                "INFORMATION",
                "information_point",
                "POINT",
                "99",
                "00",
            )
        ],
        geometry=[Point(1, 1)],
        crs="EPSG:2154",
        index=pd.Index([44], name="source_row"),
    )
    point["point_member_count"] = [1]
    relations = pd.DataFrame(
        [
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: surface.iloc[0][key]
                    for key in (
                        "planning_feature_id",
                        "source_feature_id",
                        "source_identity_kind",
                        "source_identity_field",
                        "logical_layer",
                        "feature_family",
                        "geometry_kind",
                        "type_code_raw",
                        "subtype_code_raw",
                        "label_raw",
                        "text_raw",
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "AREA_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": 4.0,
                "source_line_length_m": None,
                "intersection_area_m2": 4.0,
                "intersection_length_m": None,
                "parcel_share_pct": 100.0,
                "feature_share_pct": 100.0,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: line.iloc[0][key]
                    for key in (
                        "planning_feature_id",
                        "source_feature_id",
                        "source_identity_kind",
                        "source_identity_field",
                        "logical_layer",
                        "feature_family",
                        "geometry_kind",
                        "type_code_raw",
                        "subtype_code_raw",
                        "label_raw",
                        "text_raw",
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "LENGTH_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": None,
                "source_line_length_m": 2.0,
                "intersection_area_m2": None,
                "intersection_length_m": 2.0,
                "parcel_share_pct": None,
                "feature_share_pct": None,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
        ],
        index=pd.Index([101, 102], name="relation_row"),
    )
    return _planning_document(), surface, line, point, relations, _profile()


def _mutated_profile(**updates: object) -> CnigFeatureCodeProfile:
    """Build a deliberately unvalidated frozen profile for boundary tests."""

    profile = _profile()
    return profile.model_copy(update=updates)


def _empty_catalog(kind: str) -> gpd.GeoDataFrame:
    """Return an optional empty catalog with the deterministic source schema."""

    _, surface, line, point, _, _ = _inputs()
    template = {"SURFACE": surface, "LINE": line, "POINT": point}[kind]
    return template.iloc[0:0].copy()


def test_exact_family_pair_resolution_and_leading_zeros() -> None:
    result = resolve_planning_feature_codes(*_inputs())
    surface = result.surface_features.set_index("planning_feature_id")
    assert surface.loc["F-P-0700", "official_code_label"] == "Prescription seven"
    assert surface.loc["F-I-0200", "official_code_label"] == "Information two"
    assert (
        result.line_features.iloc[0]["official_code_label"]
        == "Prescription seven subtype four"
    )
    assert result.line_features.iloc[0]["type_code_raw"] == "07"
    assert result.line_features.iloc[0]["subtype_code_raw"] == "04"
    assert set(surface["official_code_status"]) == {"RESOLVED_OFFICIAL"}


def test_no_type_only_or_cross_family_fallback_and_unknown_is_retained() -> None:
    document, surface, line, point, relations, profile = _inputs()
    line = line.copy(deep=True)
    line.loc[line.index[0], "subtype_code_raw"] = "09"
    relations = relations.copy(deep=True)
    relations.loc[
        relations["planning_feature_id"].eq("F-P-0704"), "subtype_code_raw"
    ] = "09"
    point = point.copy(deep=True)
    point.loc[point.index[0], ["type_code_raw", "subtype_code_raw"]] = ["07", "00"]
    result = resolve_planning_feature_codes(
        document, surface, line, point, relations, profile
    )
    assert result.line_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert pd.isna(result.line_features.iloc[0]["official_code_label"])
    assert result.point_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1


def test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated() -> None:
    inputs = list(_inputs())
    inputs[-1] = _mutated_profile(canonical_records_sha256="f" * 64)
    with pytest.raises(PlanningFeatureCodeError, match="profile|canonical"):
        resolve_planning_feature_codes(*inputs)


def test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{**profile.model_dump(mode="python"), "schema_version": 1}
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="schema|profile"):
        resolve_planning_feature_codes(*inputs)


def test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{
            **profile.model_dump(mode="python"),
            "records": (*profile.records, profile.records[0]),
        }
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|profile"):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("family", "url"),
    [
        ("prescription", "https://www.geoportail-urbanisme.gouv.fr/another/path"),
        ("prescription", f"{P_URL}?format=json"),
        (
            "prescription",
            "https://www.geoportail-urbanisme.gouv.fr:444/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://user@www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        ("prescription", I_URL),
        ("information", P_URL),
        ("information", f"{I_URL}#codes"),
        ("information", f"{I_URL}/"),
        ("information", I_URL.replace("https://", "http://")),
    ],
)
def test_official_family_endpoints_require_exact_identity(
    family: str, url: str
) -> None:
    payload = _profile_payload()
    payload["official_sources"][family] = url
    family_name = family.upper()
    for record in payload["records"]:
        if record["feature_family"] == family_name:
            record["official_source_url"] = url
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(ValueError, match="official|source|URL"):
        CnigFeatureCodeProfile.model_validate(payload)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("official_label", "Repeated  whitespace"),
        ("official_label", "Decomposed e\u0301"),
        ("legal_reference", "L151-1\n  L151-2"),
        ("regulation_or_annex_reference", " R151-1"),
    ],
)
def test_official_text_must_already_be_canonical(field: str, value: str) -> None:
    payload = _profile_payload()
    payload["records"][0][field] = value
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(
        ValueError,
        match="GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1|canonical|normalization|exact",
    ):
        CnigFeatureCodeProfile.model_validate(payload)


@pytest.mark.parametrize("code", ["1", "001", "A1", " 01", "01 ", 1])
def test_malformed_code_is_rejected(code: object) -> None:
    payload = _profile_payload()
    payload["records"][0]["type_code"] = code
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)


def test_duplicate_pair_and_profile_hash_mutation_are_rejected() -> None:
    payload = _profile_payload()
    payload["records"].append(dict(payload["records"][0]))
    with pytest.raises(ValueError, match="duplicate"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["canonical_records_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="canonical"):
        CnigFeatureCodeProfile.model_validate(payload)


def test_wrong_official_host_and_unknown_field_are_rejected() -> None:
    payload = _profile_payload()
    payload["official_sources"]["prescription"] = "https://example.com/codes"
    with pytest.raises(ValueError, match="official|exact"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["semantic_policy"] = "BLOCK"
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)


def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "codes.yaml"
    path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
    with pytest.raises(PlanningFeatureCodeError, match="Duplicate YAML"):
        load_cnig_feature_code_profile(path)


def test_wrong_planning_standard_is_rejected() -> None:
    inputs = list(_inputs())
    inputs[0] = _planning_document("CNIG PLU v2022")
    with pytest.raises(PlanningFeatureCodeError, match="standard"):
        resolve_planning_feature_codes(*inputs)


def test_catalogs_and_relations_are_preserved_and_inputs_immutable() -> None:
    inputs = _inputs()
    snapshots = [frame.copy(deep=True) for frame in inputs[1:5]]
    result = resolve_planning_feature_codes(*inputs)
    for original, snapshot, coded in zip(
        inputs[1:4],
        snapshots[:3],
        (result.surface_features, result.line_features, result.point_features),
        strict=True,
    ):
        assert_geodataframe_equal(original, snapshot)
        assert_geodataframe_equal(coded.loc[:, original.columns], original)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )
    pd.testing.assert_frame_equal(inputs[4], snapshots[3])
    pd.testing.assert_frame_equal(result.relations.loc[:, inputs[4].columns], inputs[4])
    assert tuple(result.code_dictionary.columns) == CODE_DICTIONARY_COLUMNS
    assert result.relations.index.equals(inputs[4].index)


def test_duplicate_catalog_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([surface, surface[["planning_feature_id"]]], axis=1)
    duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=surface.crs)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, duplicate, line, point, relations, profile
        )


def test_missing_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.set_crs(None, allow_override=True)
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_unparseable_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.geometry.array._crs = "definitely-not-a-crs"  # type: ignore[attr-defined]
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_inactive_or_wrong_geometry_column_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface["alternate_geometry"] = surface.geometry.copy()
    surface = surface.set_geometry("alternate_geometry")
    with pytest.raises(PlanningFeatureCodeError, match="geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("geometry", "message"),
    [
        (None, "null|geometry"),
        (Polygon(), "empty|geometry"),
        (Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)]), "invalid|geometry"),
        (LineString([(0, 0), (1, 1)]), "type|geometry|SURFACE"),
    ],
)
def test_surface_geometry_contract_is_enforced(
    geometry: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.at[surface.index[0], "geometry"] = geometry
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("surface", MultiPolygon([Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])])),
        ("line", MultiLineString([[(0, 0), (1, 1)]])),
        ("point", MultiPoint([(0, 0), (1, 1)])),
    ],
)
def test_valid_multi_geometries_are_accepted(
    catalog_name: str, geometry: object
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"surface": surface, "line": line, "point": point}
    catalog = catalogs[catalog_name].copy(deep=True)
    catalog.at[catalog.index[0], "geometry"] = geometry
    catalogs[catalog_name] = catalog
    result = resolve_planning_feature_codes(
        document,
        catalogs["surface"],
        catalogs["line"],
        catalogs["point"],
        relations,
        profile,
    )
    assert getattr(result, f"{catalog_name}_features").geometry.iloc[0].equals(geometry)


@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("geometry_kind", "LINE", "geometry kind|SURFACE"),
        ("logical_layer", "prescription_line", "logical layer|surface"),
        ("feature_family", "INFORMATION", "family|logical layer"),
        ("source_identity_kind", None, "source identity|exact string"),
        ("source_layer", " SOURCE ", "source layer|exact string"),
    ],
)
def test_catalog_semantic_and_string_contracts_are_enforced(
    column: str,
    value: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.loc[surface.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    "column",
    [
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "source_layer",
    ],
)
def test_every_required_catalog_identity_is_an_exact_non_null_string(
    column: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    relations = relations.copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], column] = " invalid "
    if column in relations.columns:
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = (
            " invalid "
        )
    with pytest.raises(PlanningFeatureCodeError, match="exact string|non-empty"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("line", Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])),
        ("point", LineString([(0, 0), (1, 1)])),
    ],
)
def test_line_and_point_geometry_types_are_enforced(
    catalog_name: str,
    geometry: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"line": line.copy(deep=True), "point": point.copy(deep=True)}
    catalog = catalogs[catalog_name]
    catalog.at[catalog.index[0], "geometry"] = geometry
    catalogs[catalog_name] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="geometry|type"):
        resolve_planning_feature_codes(
            document,
            surface,
            catalogs["line"],
            catalogs["point"],
            relations,
            profile,
        )


def test_planning_feature_ids_are_globally_unique_across_catalogs() -> None:
    document, surface, line, point, relations, profile = _inputs()
    line = line.copy(deep=True)
    line.loc[line.index[0], "planning_feature_id"] = surface.iloc[0][
        "planning_feature_id"
    ]
    with pytest.raises(PlanningFeatureCodeError, match="unique|catalog"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_valid_empty_optional_catalogs_preserve_schema_and_crs() -> None:
    document, surface, _, _, relations, profile = _inputs()
    line = _empty_catalog("LINE")
    point = _empty_catalog("POINT")
    relations = relations.loc[relations["geometry_kind"].eq("SURFACE")].copy()
    result = resolve_planning_feature_codes(
        document, surface, line, point, relations, profile
    )
    for original, coded in (
        (line, result.line_features),
        (point, result.point_features),
    ):
        assert coded.empty
        assert coded.crs == original.crs
        assert tuple(coded.columns[: len(original.columns)]) == tuple(original.columns)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )


def test_relation_catalog_code_mismatch_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], "subtype_code_raw"] = "04"
    with pytest.raises(PlanningFeatureCodeError, match="catalog"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_duplicate_relation_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([relations, relations[["parcel_id"]]], axis=1)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, surface, line, point, duplicate, profile
        )


@pytest.mark.parametrize("column", ["parcel_id", "planning_feature_id"])
@pytest.mark.parametrize("value", [None, " invalid "])
def test_relation_identity_must_be_an_exact_non_null_string(
    column: str,
    value: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match="relation|exact string"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_duplicate_parcel_feature_relation_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = pd.concat([relations, relations.iloc[[0]]], ignore_index=True)
    with pytest.raises(PlanningFeatureCodeError, match="unique|duplicate"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_unknown_relation_feature_id_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "UNKNOWN"
    with pytest.raises(PlanningFeatureCodeError, match="unknown"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "LENGTH_OVERLAP"),
        ("SURFACE", "NOT_A_RELATION"),
        ("LINE", "INSIDE"),
        ("POINT", "AREA_OVERLAP"),
    ],
)
def test_relation_type_must_match_catalog_geometry_kind(
    geometry_kind: str,
    relation_type: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"SURFACE": surface, "LINE": line, "POINT": point}
    feature = catalogs[geometry_kind].iloc[0]
    row = relations.iloc[0].copy()
    for column in (
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "type_code_raw",
        "subtype_code_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
    ):
        row[column] = feature[column]
    row["relation_type"] = relation_type
    candidate = pd.DataFrame([row], columns=relations.columns)
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation type|geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, candidate, profile
        )


@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "AREA_OVERLAP"),
        ("SURFACE", "TOUCH_ONLY"),
        ("LINE", "LENGTH_OVERLAP"),
        ("LINE", "TOUCH_ONLY"),
        ("POINT", "INSIDE"),
        ("POINT", "BOUNDARY_TOUCH"),
    ],
)
def test_valid_relation_types_are_retained(
    geometry_kind: str,
    relation_type: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"SURFACE": surface, "LINE": line, "POINT": point}
    feature = catalogs[geometry_kind].iloc[0]
    row = relations.iloc[0].copy()
    for column in (
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "type_code_raw",
        "subtype_code_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
    ):
        row[column] = feature[column]
    row["relation_type"] = relation_type
    candidate = pd.DataFrame([row], columns=relations.columns)
    result = resolve_planning_feature_codes(
        document, surface, line, point, candidate, profile
    )
    assert result.relations["relation_type"].tolist() == [relation_type]


def test_coordinated_output_hash_mutation_is_rejected() -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_label"] = "Mutated"
    mutated = _result_with_hashes(replace(result, surface_features=surface))
    with pytest.raises(PlanningFeatureCodeError, match="rebuilt"):
        validate_planning_feature_code_result(*inputs, mutated)


def test_parquet_readback_passes_source_complete_validation(tmp_path: Path) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
    for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
    persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
    validate_planning_feature_code_result(*inputs, persisted)


def test_record_order_must_be_deterministic() -> None:
    payload = _profile_payload()
    payload["records"] = list(reversed(payload["records"]))
    with pytest.raises(ValueError, match="deterministic order"):
        CnigFeatureCodeProfile.model_validate(payload)


def test_yaml_snapshot_loads_strictly(tmp_path: Path) -> None:
    payload = _profile_payload()
    path = tmp_path / "profile.yaml"
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    assert load_cnig_feature_code_profile(path) == _profile()


def test_stable_public_api_is_exported_from_module_and_stage_package() -> None:
    from landscout import stages

    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )

    required = {
        "CnigFeatureCodeProfile",
        "PlanningFeatureCodeError",
        "PlanningFeatureCodeResult",
        "load_cnig_feature_code_profile",
        "resolve_planning_feature_codes",
        "validate_planning_feature_code_result",
    }
    low_level = {
        "_canonical_json_sha256",
        "_coded_catalog",
        "_lookup",
        "_profile_sha256",
        "_result_with_hashes",
    }
    assert required.issubset(set(coding_module.__all__))
    assert required.issubset(set(stages.__all__))
    for name in required:
        assert getattr(stages, name) is getattr(coding_module, name)
    assert low_level.isdisjoint(coding_module.__all__)
    assert low_level.isdisjoint(stages.__all__)


def test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs() -> None:
    path = Path("configs/planning/cnig_plu_2017_feature_codes.yaml")
    profile = load_cnig_feature_code_profile(path)
    expected_records = (
        (
            "INFORMATION",
            "02",
            "00",
            "Zone d'aménagement concerté",
            "L311-1 code de l’urbanisme",
            "R151-52 8°",
            I_URL,
        ),
        (
            "INFORMATION",
            "14",
            "00",
            "Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)",
            "L571-10 code de l’environnement",
            "R151-53 5°",
            I_URL,
        ),
        (
            "INFORMATION",
            "27",
            "00",
            "Plan d'exposition au bruit des aérodromes",
            "L112-6 code de l’urbanisme",
            "R151-52 2°",
            I_URL,
        ),
        (
            "INFORMATION",
            "99",
            "00",
            "Autre périmètre, secteur, plan, document, site, projet, espace.",
            None,
            None,
            I_URL,
        ),
        (
            "PRESCRIPTION",
            "01",
            "00",
            "Espace boisé classé",
            "L113-1",
            "R151-31 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "05",
            "00",
            "Emplacement réservé",
            "L151-41 1° à 3°",
            "R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "00",
            "Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique",
            "L151-19 et L151-23",
            "R151-41 3° Et R151-43",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "04",
            "Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique",
            "L151-23",
            "R151-43 5°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "00",
            "Règles d’implantation des constructions",
            "L151-17 et L151-18",
            "R151-39 dernier al.",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "01",
            "Implantation des constructions par rapport aux voies et aux emprises publiques",
            "L151-17 et L151-18",
            "R151-39",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "17",
            "00",
            "Secteur à programme de logements mixité sociale en zone U et AU",
            "L151-15",
            "R151-38 3°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "18",
            "00",
            "Périmètre comportant des orientations d’aménagement et de programmation (OAP)",
            "L151-6 et L151-7",
            "R151-6 à R151-8-1",
            P_URL,
        ),
    )
    actual_records = tuple(
        (
            record.feature_family,
            record.type_code,
            record.subtype_code,
            record.official_label,
            record.legal_reference,
            record.regulation_or_annex_reference,
            record.official_source_url,
        )
        for record in profile.records
    )
    assert profile.schema_version == 2
    assert profile.profile == "cnig_plu_2017_muret_observed_pairs_v2"
    assert profile.standard_model == "CNIG PLU v2017"
    assert profile.official_text_normalization == TEXT_NORMALIZATION
    assert profile.retrieval_date.isoformat() == "2026-08-12"
    assert profile.official_sources.prescription == P_URL
    assert profile.official_sources.information == I_URL
    assert (
        profile.canonical_records_sha256
        == "5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c"
    )
    assert (
        _payload_hash(profile.model_dump(mode="json"))
        == "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    )
    assert actual_records == expected_records


@pytest.mark.parametrize(
    "field", ["result_hash_schema_version", "profile_schema_version"]
)
@pytest.mark.parametrize("value", [True, 0, 1, 3, 2.0, "2"])
def test_result_schema_versions_are_strict(field: str, value: object) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="schema version"):
        validate_planning_feature_code_result(
            *inputs, replace(result, **{field: value})
        )
