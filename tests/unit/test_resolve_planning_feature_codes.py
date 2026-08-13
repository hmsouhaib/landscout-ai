from __future__ import annotations

import importlib
import inspect
import json
import shutil
import tempfile
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
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)
from landscout.stages.enrich_planning_features import (
    RELATION_COLUMNS,
    intersect_parcels_with_gpu_planning_features,
)
from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)
from landscout.stages.resolve_planning_feature_codes import (
    resolve_planning_feature_codes as _public_resolve_planning_feature_codes,
)
from landscout.stages.resolve_planning_feature_codes import (
    validate_planning_feature_code_result as _public_validate_planning_feature_code_result,
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


def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    return tuple(
        GpuExtractedFile(
            relative_path=path.relative_to(root).as_posix(),
            file_type=path.suffix.casefold().lstrip(".") or "none",
            size_bytes=path.stat().st_size,
            sha256=sha256(path.read_bytes()).hexdigest(),
            category="SPATIAL_DATA",
        )
        for path in sorted((item for item in root.rglob("*") if item.is_file()), key=str)
        if not (path.parent == root and path.name == EXTRACTION_MANIFEST_NAME)
    )


def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(
            {
                "schema_version": 2,
                "archive_sha256": archive_sha256,
                "files": [
                    {
                        "relative_path": item.relative_path,
                        "size_bytes": item.size_bytes,
                        "sha256": item.sha256,
                    }
                    for item in files
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )


def _layer_summary(frame: gpd.GeoDataFrame, source_layer: str) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )


def _planning_document(
    standard: str = "CNIG PLU v2017",
    related_layers: tuple[GpuInspectedLayer, ...] = (),
) -> GpuPlanningDocument:
    extraction_root = Path(tempfile.mkdtemp(prefix="landscout-code-source-"))
    physical_layers: list[GpuInspectedLayer] = []
    for layer in related_layers:
        path = extraction_root / f"{layer.logical_name}.gpkg"
        layer.data.to_file(
            path,
            layer=layer.reference.source_layer,
            driver="GPKG",
            engine="pyogrio",
            index=False,
        )
        reread = gpd.read_file(
            path, layer=layer.reference.source_layer, engine="pyogrio"
        )
        reference = replace(
            layer.reference,
            dataset_path=path,
            driver="GPKG",
        )
        physical_layers.append(
            replace(
                layer,
                reference=reference,
                data=reread,
                summary=_layer_summary(reread, reference.source_layer),
            )
        )
    related_layers = tuple(physical_layers)
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
    zoning_data = gpd.GeoDataFrame(
        {"LIB_IDZONE": ["Z1"]},
        geometry=[Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])],
        crs="EPSG:2154",
    )
    zoning_path = extraction_root / "zones.gpkg"
    zoning_data.to_file(
        zoning_path,
        layer="ZONE",
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    zoning_data = gpd.read_file(zoning_path, layer="ZONE", engine="pyogrio")
    reference = GpuSpatialLayerReference(zoning_path, "ZONE", "GPKG")
    summary = _layer_summary(zoning_data, "ZONE")
    zoning = GpuInspectedLayer("zoning", reference, zoning_data, summary)
    inventory = _physical_inventory(extraction_root)
    _write_extraction_manifest(extraction_root, archive.sha256, inventory)
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=extraction_root,
        files=inventory,
        standard_models=(standard,),
        cache_hit=True,
    )
    return GpuPlanningDocument(
        extraction,
        (reference, *(layer.reference for layer in related_layers)),
        zoning,
        related_layers,
    )


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


def _legacy_inputs():
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
    relations = relations.loc[:, list(RELATION_COLUMNS)]
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


def _integration_source_frame(
    logical_layer: str,
    geometries: list[object],
    source_ids: list[str],
    type_codes: list[str],
    subtype_codes: list[str],
) -> gpd.GeoDataFrame:
    prescription = logical_layer.startswith("prescription")
    return gpd.GeoDataFrame(
        {
            "LIBELLE": [f"Label {identifier}" for identifier in source_ids],
            "TXT": [None] * len(source_ids),
            ("TYPEPSC" if prescription else "TYPEINF"): type_codes,
            ("STYPEPSC" if prescription else "STYPEINF"): subtype_codes,
            "NOMFIC": [None] * len(source_ids),
            "URLFIC": [None] * len(source_ids),
            "IDURBA": ["31395_PLU_20240215"] * len(source_ids),
            "DATVALID": ["20240215"] * len(source_ids),
            ("LIB_IDPSC" if prescription else "LIB_IDINFO"): source_ids,
        },
        geometry=geometries,
        crs="EPSG:2154",
    )


def _integration_layer(
    logical_layer: str,
    frame: gpd.GeoDataFrame,
) -> GpuInspectedLayer:
    source_layer = logical_layer.upper()
    reference = GpuSpatialLayerReference(
        Path(f"{logical_layer}.gpkg"), source_layer, "GPKG"
    )
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    summary = GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
    return GpuInspectedLayer(logical_layer, reference, frame, summary)  # type: ignore[arg-type]


def _integration_inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
    layers = (
        _integration_layer(
            "prescription_surface",
            _integration_source_frame(
                "prescription_surface",
                [Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
                ["P-1"],
                ["07"],
                ["00"],
            ),
        ),
        _integration_layer(
            "information_surface",
            _integration_source_frame(
                "information_surface",
                [Polygon([(3, 0), (5, 0), (5, 2), (3, 2)])],
                ["I-1"],
                ["02"],
                ["00"],
            ),
        ),
        _integration_layer(
            "prescription_line",
            _integration_source_frame(
                "prescription_line",
                [LineString([(0, 1), (2, 1)])],
                ["P-2"],
                ["07"],
                ["04"],
            ),
        ),
        _integration_layer(
            "information_point",
            _integration_source_frame(
                "information_point",
                [Point(10, 10)],
                ["I-2"],
                ["99"],
                ["00"],
            ),
        ),
    )
    planning_document = _planning_document(related_layers=layers)
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(
        parcels, planning_document
    )
    return (
        planning_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )


def _integration_parcels() -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {"parcel_id": ["PARCEL-1"], "existing_fact": [7]},
        geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
        crs="EPSG:2154",
        index=pd.Index([91], name="parcel_row"),
    )


def _inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
    document, _, surface, line, point, relations, profile = _integration_inputs()
    return document, surface, line, point, relations, profile


def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
    """Exercise the new bound API while keeping legacy unit call sites compact."""

    return _public_resolve_planning_feature_codes(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
    )


def validate_planning_feature_code_result(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
    _public_validate_planning_feature_code_result(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
        result,
    )


def test_exact_family_pair_resolution_and_leading_zeros() -> None:
    result = resolve_planning_feature_codes(*_inputs())
    surface = result.surface_features.set_index("planning_feature_id")
    assert (
        surface.loc["GPU:doc-1:prescription_surface:P-1", "official_code_label"]
        == "Prescription seven"
    )
    assert (
        surface.loc["GPU:doc-1:information_surface:I-1", "official_code_label"]
        == "Information two"
    )
    assert (
        result.line_features.iloc[0]["official_code_label"]
        == "Prescription seven subtype four"
    )
    assert result.line_features.iloc[0]["type_code_raw"] == "07"
    assert result.line_features.iloc[0]["subtype_code_raw"] == "04"
    assert set(surface["official_code_status"]) == {"RESOLVED_OFFICIAL"}


def test_no_type_only_or_cross_family_fallback_and_unknown_is_retained() -> None:
    document, surface, line, point, relations, profile = _inputs()
    payload = _profile_payload()
    payload["records"] = [
        record
        for record in payload["records"]
        if not (
            (record["feature_family"], record["type_code"], record["subtype_code"])
            in {("PRESCRIPTION", "07", "04"), ("INFORMATION", "99", "00")}
        )
    ]
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    profile = CnigFeatureCodeProfile.model_validate(payload)
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


@pytest.mark.parametrize(
    ("catalog_position", "column"),
    [
        (1, "feature_area_m2"),
        (2, "feature_length_m"),
        (3, "point_member_count"),
        (1, "label_raw"),
        (1, "source_crs"),
    ],
)
def test_complete_normalized_catalog_schema_is_required(
    catalog_position: int,
    column: str,
) -> None:
    inputs = list(_inputs())
    inputs[catalog_position] = inputs[catalog_position].drop(columns=column)
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)


def test_unexpected_factual_catalog_column_is_rejected() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface["unexpected_fact"] = "not-produced-by-step-7d-3-1"
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "UNKNOWN_KIND"),
        ("source_identity_field", "LIB_IDINFO"),
    ],
)
def test_cnig_identity_provenance_is_exact(column: str, value: str) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[0], column] = value
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("logical_layer", "feature_family", "source_feature_id"),
    [
        ("information_surface", "INFORMATION", "OGR_FID:1"),
        ("prescription_surface", "PRESCRIPTION", "1"),
    ],
)
def test_ogr_fid_provenance_is_restricted(
    logical_layer: str,
    feature_family: str,
    source_feature_id: str,
) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    row_index = surface.index[0]
    surface.loc[row_index, "logical_layer"] = logical_layer
    surface.loc[row_index, "feature_family"] = feature_family
    surface.loc[row_index, "source_identity_kind"] = "ARCHIVE_SCOPED_OGR_FID"
    surface.loc[row_index, "source_identity_field"] = "OGR_FID"
    surface.loc[row_index, "source_feature_id"] = source_feature_id
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="OGR|identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)


def test_source_feature_id_is_unique_inside_logical_layer() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[1], "logical_layer"] = surface.iloc[0]["logical_layer"]
    surface.loc[surface.index[1], "feature_family"] = surface.iloc[0]["feature_family"]
    surface.loc[surface.index[1], "source_identity_field"] = surface.iloc[0][
        "source_identity_field"
    ]
    surface.loc[surface.index[1], "source_feature_id"] = surface.iloc[0][
        "source_feature_id"
    ]
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="source_feature_id|unique"):
        resolve_planning_feature_codes(*inputs)


def test_catalog_crs_must_be_canonical_epsg_2154() -> None:
    inputs = list(_inputs())
    inputs[1] = inputs[1].to_crs("EPSG:4326")
    with pytest.raises(PlanningFeatureCodeError, match="EPSG:2154|CRS"):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("catalog_position", "column", "value"),
    [
        (1, "feature_area_m2", 99.0),
        (2, "feature_length_m", 99.0),
        (3, "point_member_count", 2),
    ],
)
def test_catalog_geometry_metrics_are_revalidated(
    catalog_position: int,
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    catalog = inputs[catalog_position].copy(deep=True)
    catalog.loc[catalog.index[0], column] = value
    inputs[catalog_position] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="metric|area|length|member"):
        resolve_planning_feature_codes(*inputs)


def test_complete_relation_schema_is_required() -> None:
    inputs = list(_inputs())
    inputs[4] = inputs[4].drop(columns="intersection_length_m")
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema|column"):
        resolve_planning_feature_codes(*inputs)


def test_unexpected_factual_relation_column_is_rejected() -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations["unexpected_metric"] = 0.0
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema"):
        resolve_planning_feature_codes(*inputs)


def test_cnig_resolver_invokes_shared_factual_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    calls = 0

    def reject_shared_contract(*args: object) -> None:
        nonlocal calls
        calls += 1
        raise ValueError("shared factual contract marker")

    monkeypatch.setattr(
        coding_module,
        "validate_normalized_planning_feature_inputs",
        reject_shared_contract,
    )
    with pytest.raises(
        PlanningFeatureCodeError, match="shared factual contract marker"
    ):
        resolve_planning_feature_codes(*_inputs())
    assert calls == 1


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("label_raw", "mutated label"),
        ("source_validity_date_raw", "19990101"),
        ("regulation_filename_raw", "other.pdf"),
        ("feature_area_m2", 3.0),
    ],
)
def test_complete_relation_catalog_agreement_is_required(
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="catalog|metric|normalized|feature share"
    ):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_area_m2", 0.0),
        ("intersection_area_m2", -1.0),
        ("intersection_area_m2", float("inf")),
        ("parcel_share_pct", 99.0),
    ],
)
def test_surface_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="relation|metric|finite|percentage"
    ):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_length_m", 0.0),
        ("relation_type", "TOUCH_ONLY"),
        ("source_line_length_m", 1.0),
    ],
)
def test_line_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    line_index = relations.index[relations["geometry_kind"].eq("LINE")][0]
    relations.loc[line_index, column] = value
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|length|catalog"):
        resolve_planning_feature_codes(*inputs)


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
        ("surface", MultiPolygon([Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])])),
        ("line", MultiLineString([[(0, 0), (2, 0)]])),
        ("point", MultiPoint([(0, 0), (1, 1)])),
    ],
)
def test_valid_multi_geometries_are_accepted(
    catalog_name: str, geometry: object
) -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    target_logical = {
        "surface": "prescription_surface",
        "line": "prescription_line",
        "point": "information_point",
    }[catalog_name]
    changed_layers: list[GpuInspectedLayer] = []
    for layer in document.related_layers:
        if layer.logical_name != target_logical:
            changed_layers.append(layer)
            continue
        source = layer.data.copy(deep=True)
        source.at[source.index[0], "geometry"] = geometry
        changed_layers.append(_integration_layer(target_logical, source))
    changed_document = _planning_document(related_layers=tuple(changed_layers))
    normalized = intersect_parcels_with_gpu_planning_features(parcels, changed_document)
    result = _public_resolve_planning_feature_codes(
        changed_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
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
    with pytest.raises(PlanningFeatureCodeError, match="unique|catalog|deterministic"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_valid_empty_optional_catalogs_preserve_schema_and_crs() -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    surface_layers = tuple(
        layer
        for layer in document.related_layers
        if layer.logical_name in {"prescription_surface", "information_surface"}
    )
    document = replace(document, related_layers=surface_layers)
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
    for original, coded in (
        (normalized.line_features, result.line_features),
        (normalized.point_features, result.point_features),
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
    relation_index = relations.index[0]
    original = relations.loc[relation_index, "subtype_code_raw"]
    relations.loc[relation_index, "subtype_code_raw"] = (
        "04" if original != "04" else "00"
    )
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
        "label_raw",
        "text_raw",
        "source_validity_date_raw",
        "regulation_filename_raw",
    ):
        row[column] = feature[column]
    row["relation_type"] = relation_type
    metric_columns = (
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    )
    for column in metric_columns:
        row[column] = None
    if geometry_kind == "SURFACE":
        area = 4.0 if relation_type == "AREA_OVERLAP" else 0.0
        row["feature_area_m2"] = 4.0
        row["intersection_area_m2"] = area
        row["parcel_share_pct"] = 100.0 if area else 0.0
        row["feature_share_pct"] = 100.0 if area else 0.0
    elif geometry_kind == "LINE":
        row["source_line_length_m"] = 2.0
        row["intersection_length_m"] = 2.0 if relation_type == "LENGTH_OVERLAP" else 0.0
    else:
        row["point_member_count"] = 1
        row["point_members_inside_count"] = 1 if relation_type == "INSIDE" else 0
        row["point_members_boundary_count"] = (
            1 if relation_type == "BOUNDARY_TOUCH" else 0
        )
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
    geometry: object
    if geometry_kind == "SURFACE":
        logical = "prescription_surface"
        geometry = (
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
            if relation_type == "AREA_OVERLAP"
            else Polygon([(2, 0), (4, 0), (4, 2), (2, 2)])
        )
    elif geometry_kind == "LINE":
        logical = "prescription_line"
        geometry = (
            LineString([(0, 1), (2, 1)])
            if relation_type == "LENGTH_OVERLAP"
            else LineString([(-1, 0), (0, 0)])
        )
    else:
        logical = "information_point"
        geometry = Point(1, 1) if relation_type == "INSIDE" else Point(0, 1)
    source = _integration_source_frame(
        logical,
        [geometry],
        ["FEATURE-1"],
        ["07" if logical.startswith("prescription") else "99"],
        ["00"],
    )
    document = _planning_document(
        related_layers=(_integration_layer(logical, source),)
    )
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
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
    ("field", "value"),
    [
        ("result_hash_schema_version", True),
        ("result_hash_schema_version", 0),
        ("result_hash_schema_version", 1),
        ("result_hash_schema_version", 2),
        ("result_hash_schema_version", 3),
        ("result_hash_schema_version", 5),
        ("result_hash_schema_version", 4.0),
        ("result_hash_schema_version", "4"),
        ("profile_schema_version", True),
        ("profile_schema_version", 0),
        ("profile_schema_version", 1),
        ("profile_schema_version", 3),
        ("profile_schema_version", 2.0),
        ("profile_schema_version", "2"),
    ],
)
def test_result_schema_versions_are_strict(field: str, value: object) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="schema version"):
        validate_planning_feature_code_result(
            *inputs, replace(result, **{field: value})
        )


def test_step_7d_3_1_output_integrates_with_public_coding_api() -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    assert result.result_hash_schema_version == 4
    assert result.profile_schema_version == 2
    assert len(result.surface_features) == 2
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1
    assert len(result.relations) == 2
    assert set(result.surface_features["official_code_status"]) == {"RESOLVED_OFFICIAL"}
    _public_validate_planning_feature_code_result(*inputs, result)


def test_coded_result_persists_all_source_input_hashes() -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    for hash_field in (
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ):
        value = getattr(result, hash_field)
        assert isinstance(value, str)
        assert len(value) == 64
        int(value, 16)


@pytest.mark.parametrize(
    "field",
    [
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ],
)
def test_source_input_hash_mutation_is_rejected(field: str) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="hash|rebuilt|source"):
        _public_validate_planning_feature_code_result(
            *inputs, replace(result, **{field: "f" * 64})
        )


def test_gpu_related_source_hash_is_deterministic_across_cache_roots(
    tmp_path: Path,
) -> None:
    first_inputs = _integration_inputs()
    first_document = first_inputs[0]
    source_root = first_document.extraction.extraction_root
    relocated_root = tmp_path / "relocated-extraction"
    shutil.copytree(source_root, relocated_root)

    def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
        relative = reference.dataset_path.relative_to(source_root)
        return replace(reference, dataset_path=relocated_root / relative)

    reference_map = {
        reference: relocated_reference(reference)
        for reference in first_document.all_spatial_layers
    }
    relocated_document = replace(
        first_document,
        extraction=replace(
            first_document.extraction,
            extraction_root=relocated_root,
        ),
        all_spatial_layers=tuple(
            reference_map[reference]
            for reference in first_document.all_spatial_layers
        ),
        zoning=replace(
            first_document.zoning,
            reference=reference_map[first_document.zoning.reference],
        ),
        related_layers=tuple(
            replace(layer, reference=reference_map[layer.reference])
            for layer in first_document.related_layers
        ),
    )
    second_inputs = (relocated_document, *first_inputs[1:])
    first = _public_resolve_planning_feature_codes(*first_inputs)
    second = _public_resolve_planning_feature_codes(*second_inputs)
    assert (
        first.gpu_related_source_files_sha256
        == second.gpu_related_source_files_sha256
    )


@pytest.mark.parametrize(
    "field",
    ["gpu_related_source_files_sha256", "expected_relations_content_sha256"],
)
def test_source_binding_hashes_bind_every_component_hash(field: str) -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    changed = _result_with_hashes(replace(result, **{field: "f" * 64}))
    for hash_field in (
        "code_dictionary_content_sha256",
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        assert getattr(changed, hash_field) != getattr(result, hash_field)


def test_parcel_source_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    parcels = inputs[1].copy(deep=True)
    parcels.loc[parcels.index[0], "parcel_id"] = "CHANGED-PARCEL"
    inputs[1] = parcels
    with pytest.raises(PlanningFeatureCodeError, match="parcel|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


def test_gpu_document_context_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    planning_document = inputs[0]
    archive = planning_document.extraction.archive
    changed_document = replace(archive.document, provider="Changed provider")
    inputs[0] = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=changed_document),
        ),
    )
    with pytest.raises(PlanningFeatureCodeError, match="document|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


def test_normalized_catalog_change_invalidates_coded_result_even_when_coherent() -> (
    None
):
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    surface = inputs[2].copy(deep=True)
    relations = inputs[5].copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], "label_raw"] = "Coherently changed"
    relations.loc[relations["planning_feature_id"].eq(feature_id), "label_raw"] = (
        "Coherently changed"
    )
    inputs[2] = surface
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="normalized|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


def test_normalized_relation_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    relations = inputs[5].copy(deep=True)
    line_mask = relations["geometry_kind"].eq("LINE")
    relations.loc[line_mask, "parcel_metric_area_m2"] = 8.0
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "metric"])
def test_coding_api_rejects_relation_set_not_rebuilt_from_geometry(
    mutation: str,
) -> None:
    inputs = list(_integration_inputs())
    relations = inputs[5].copy(deep=True)
    if mutation == "missing":
        relations = relations.iloc[1:].copy()
    elif mutation == "extra":
        extra = relations.iloc[[0]].copy(deep=True)
        extra.loc[extra.index[0], "parcel_id"] = "PARCEL-OTHER"
        relations = pd.concat([relations, extra], ignore_index=True)
    elif mutation == "reordered":
        relations = relations.iloc[::-1].reset_index(drop=True)
    else:
        line_mask = relations["geometry_kind"].eq("LINE")
        relations.loc[line_mask, "intersection_length_m"] = 1.0
    inputs[5] = relations
    with pytest.raises(
        PlanningFeatureCodeError,
        match="relation|parcel|source|rebuilt|normalized",
    ):
        _public_resolve_planning_feature_codes(*inputs)


def test_schema_v4_parquet_readback_preserves_source_hash_envelope(
    tmp_path: Path,
) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"integrated-{name}.parquet"
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
    _public_validate_planning_feature_code_result(*inputs, persisted)


def test_schema_v4_public_api_signatures_remain_source_complete() -> None:
    assert tuple(
        inspect.signature(_public_resolve_planning_feature_codes).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
    )
    assert tuple(
        inspect.signature(_public_validate_planning_feature_code_result).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
        "result",
    )
