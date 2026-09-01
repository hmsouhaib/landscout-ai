from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout import stages
from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)
from landscout.sources import gpu_fr as gpu_source_module
from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)
from landscout.stages import enrich_planning_features as planning_features_module
from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)

DOCUMENT_ID = "doc-1"
ARCHIVE_NAME = "31395_PLU_20240215"
ARCHIVE_SHA = "a" * 64
STANDARD = "CNIG PLU v2017"
LOCAL_ENGINEERING_CRS = (
    'ENGCRS["Local",EDATUM["Unknown"],CS[Cartesian,2],'
    'AXIS["x",east,LENGTHUNIT["metre",1]],'
    'AXIS["y",north,LENGTHUNIT["metre",1]]]'
)


def _rectangle(x1: float, y1: float, x2: float, y2: float) -> Polygon:
    return Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)])


def _parcels(
    geometries: list[object] | None = None,
    *,
    ids: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    values = geometries or [_rectangle(0, 0, 10, 10)]
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ids or [f"P-{index + 1}" for index in range(len(values))],
            "existing_zoning_fact": np.arange(len(values), dtype="int64") + 7,
        },
        geometry=values,
        crs="EPSG:2154",
        index=[50 + index for index in range(len(values))],
    )
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    return frame if crs == "EPSG:2154" else frame.to_crs(crs)


def _source_frame(
    logical: str,
    geometries: list[object],
    *,
    ids: list[object] | None = None,
    type_codes: list[object] | None = None,
    subtype_codes: list[object] | None = None,
    document_refs: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    count = len(geometries)
    prescription = logical.startswith("prescription")
    identity = "LIB_IDPSC" if prescription else "LIB_IDINFO"
    type_field = "TYPEPSC" if prescription else "TYPEINF"
    subtype_field = "STYPEPSC" if prescription else "STYPEINF"
    data: dict[str, object] = {
        "LIBELLE": [f"Label {index}" for index in range(count)],
        "TXT": [None if index % 2 else f"Text {index}" for index in range(count)],
        type_field: type_codes or [f"T{index}" for index in range(count)],
        subtype_field: subtype_codes or [f"S{index}" for index in range(count)],
        "NOMFIC": [
            None if index % 2 else f"rule-{index}.pdf" for index in range(count)
        ],
        "URLFIC": [None] * count,
        "IDURBA": document_refs or [ARCHIVE_NAME] * count,
        "DATVALID": ["20240215"] * count,
        identity: ids or [f"SRC-{logical}-{index}" for index in range(count)],
    }
    frame = gpd.GeoDataFrame(data, geometry=geometries, crs="EPSG:2154")
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    if crs == "IGNF:LAMB93":
        return frame.set_crs(crs, allow_override=True)
    return frame if crs == "EPSG:2154" else frame.to_crs(crs)


def _summary(
    frame: gpd.GeoDataFrame,
    source_layer: str,
    *,
    document_id: str = DOCUMENT_ID,
    archive_sha: str = ARCHIVE_SHA,
) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id=document_id,
        source_archive_sha256=archive_sha,
        source_layer=source_layer,
        crs="UNKNOWN" if frame.crs is None else frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(key), int(value))
            for key, value in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )


def _inspected(logical: str, frame: gpd.GeoDataFrame) -> GpuInspectedLayer:
    source_layer = f"SOURCE_{logical.upper()}"
    reference = GpuSpatialLayerReference(
        dataset_path=Path(f"synthetic-{logical}.gpkg"),
        source_layer=source_layer,
        driver="GPKG",
    )
    return GpuInspectedLayer(
        logical_name=logical,  # type: ignore[arg-type]
        reference=reference,
        data=frame,
        summary=_summary(frame, source_layer),
    )


def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    records: list[GpuExtractedFile] = []
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=str):
        if path.parent == root and path.name == EXTRACTION_MANIFEST_NAME:
            continue
        suffix = path.suffix.casefold()
        records.append(
            GpuExtractedFile(
                relative_path=path.relative_to(root).as_posix(),
                file_type=suffix.lstrip(".") or "none",
                size_bytes=path.stat().st_size,
                sha256=sha256(path.read_bytes()).hexdigest(),
                category="SPATIAL_DATA",
            )
        )
    return tuple(records)


def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
    payload = {
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
    }
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(payload, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )


def _materialize_layer(root: Path, layer: GpuInspectedLayer) -> GpuInspectedLayer:
    reference = layer.reference
    if reference.dataset_path.is_file():
        path = reference.dataset_path.resolve()
    else:
        path = root / f"{layer.logical_name}.gpkg"
        layer.data.to_file(
            path,
            layer=reference.source_layer,
            driver="GPKG",
            engine="pyogrio",
            index=False,
        )
        reference = replace(reference, dataset_path=path, driver="GPKG")
    reread = gpd.read_file(
        path,
        layer=reference.source_layer if reference.driver == "GPKG" else None,
        engine="pyogrio",
    )
    return replace(
        layer,
        reference=replace(reference, dataset_path=path),
        data=reread,
        summary=_summary(reread, reference.source_layer),
    )


def _planning_document(
    layers: list[GpuInspectedLayer] | None = None,
) -> GpuPlanningDocument:
    requested_layers = list(layers or [])
    existing_paths = [
        layer.reference.dataset_path.resolve()
        for layer in requested_layers
        if layer.reference.dataset_path.is_file()
    ]
    extraction_root = (
        existing_paths[0].parent
        if existing_paths
        else Path(tempfile.mkdtemp(prefix="landscout-feature-source-"))
    )
    related = tuple(
        _materialize_layer(extraction_root, layer) for layer in requested_layers
    )
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
        commune_code="31395",
        partition="DU_31395",
        document_id=DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Muret PLU",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name=ARCHIVE_NAME,
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=STANDARD,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=metadata,
        download_timestamp="2026-08-12T12:00:00+00:00",
        filename=f"{ARCHIVE_NAME}.zip",
        archive_format="zip",
        file_size=1,
        sha256=ARCHIVE_SHA,
        path=Path("synthetic.zip"),
        cache_hit=True,
    )
    zoning_frame = gpd.GeoDataFrame(
        {"zone": ["Z"]}, geometry=[_rectangle(-10, -10, 20, 20)], crs="EPSG:2154"
    )
    zoning_path = extraction_root / "zoning.gpkg"
    zoning_frame.to_file(
        zoning_path,
        layer="ZONING",
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    zoning_frame = gpd.read_file(zoning_path, layer="ZONING", engine="pyogrio")
    zoning_ref = GpuSpatialLayerReference(zoning_path, "ZONING", "GPKG")
    zoning = GpuInspectedLayer(
        logical_name="zoning",
        reference=zoning_ref,
        data=zoning_frame,
        summary=_summary(zoning_frame, "ZONING"),
    )
    inventory = _physical_inventory(extraction_root)
    _write_extraction_manifest(extraction_root, ARCHIVE_SHA, inventory)
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=extraction_root,
        files=inventory,
        standard_models=(STANDARD,),
        cache_hit=True,
    )
    config_payload = load_gpu_source_config(
        Path("configs/sources/gpu_fr.yaml")
    ).model_dump(mode="python")
    for role in config_payload["spatial_layers"]:
        config_payload["spatial_layers"][role]["match_tokens"] = [f"unused_{role}"]
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONING"]
    for layer in related:
        config_payload["spatial_layers"][layer.logical_name]["match_tokens"] = [
            layer.reference.source_layer
        ]
    source_config = GpuSourceConfig.model_validate(config_payload)
    related_by_logical_name = {layer.logical_name: layer for layer in related}
    related = tuple(
        related_by_logical_name[logical_name]
        for logical_name in gpu_source_module._GPU_LOGICAL_LAYER_NAMES
        if logical_name != "zoning" and logical_name in related_by_logical_name
    )
    return GpuPlanningDocument(
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(extraction),
        zoning=zoning,
        related_layers=related,
    )


def _run(
    layers: list[GpuInspectedLayer],
    parcels: gpd.GeoDataFrame | None = None,
) -> ParcelPlanningFeaturesResult:
    return intersect_parcels_with_gpu_planning_features(
        parcels if parcels is not None else _parcels(),
        _planning_document(layers),
    )


def test_only_high_level_api_is_exported() -> None:
    assert (
        stages.intersect_parcels_with_gpu_planning_features
        is intersect_parcels_with_gpu_planning_features
    )
    assert "intersect_parcels_with_gpu_planning_features" in stages.__all__
    assert stages.PlanningFeaturesError is PlanningFeaturesError
    assert stages.ParcelPlanningFeaturesResult is ParcelPlanningFeaturesResult
    assert "PlanningFeaturesError" in stages.__all__
    assert "ParcelPlanningFeaturesResult" in stages.__all__


def test_result_is_frozen() -> None:
    result = _run([])
    with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()  # type: ignore[misc]


def test_surface_full_overlap_normalizes_raw_values_and_lineage() -> None:
    layer = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10)],
            ids=["PSC-1"],
            type_codes=["DYNAMIC-18"],
            subtype_codes=["04"],
            crs="IGNF:LAMB93",
        ),
    )
    result = _run([layer])

    feature = result.surface_features.iloc[0]
    assert feature["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:PSC-1"
    )
    assert feature["source_feature_id"] == "PSC-1"
    assert feature["source_identity_kind"] == "CNIG_ATTRIBUTE"
    assert feature["source_identity_field"] == "LIB_IDPSC"
    assert feature["feature_family"] == "PRESCRIPTION"
    assert feature["geometry_kind"] == "SURFACE"
    assert feature["type_code_raw"] == "DYNAMIC-18"
    assert feature["subtype_code_raw"] == "04"
    assert feature["label_raw"] == "Label 0"
    assert feature["text_raw"] == "Text 0"
    assert feature["source_document_id"] == DOCUMENT_ID
    assert feature["source_archive_sha256"] == ARCHIVE_SHA
    assert feature["source_layer"] == "SOURCE_PRESCRIPTION_SURFACE"
    # The physical GPKG round-trip exposes the equivalent canonical CRS identity.
    assert feature["source_crs"] == "EPSG:2154"
    assert feature["feature_area_m2"] == pytest.approx(100.0)
    assert result.surface_features.crs.to_epsg() == 2154

    relation = result.relations.iloc[0]
    assert relation["source_identity_kind"] == "CNIG_ATTRIBUTE"
    assert relation["source_identity_field"] == "LIB_IDPSC"
    assert relation["relation_type"] == "AREA_OVERLAP"
    assert relation["intersection_area_m2"] == pytest.approx(100.0)
    assert relation["parcel_share_pct"] == pytest.approx(100.0)
    assert relation["feature_share_pct"] == pytest.approx(100.0)
    assert pd.isna(relation["intersection_length_m"])
    parcel = result.parcels.iloc[0]
    assert parcel["planning_surface_relation_count"] == 1
    assert parcel["planning_surface_area_overlap_count"] == 1
    assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)
    assert parcel["prescription_surface_relation_count"] == 1
    assert parcel["information_surface_relation_count"] == 0


def test_surface_partial_and_touch_relations() -> None:
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 5, 10), _rectangle(10, 0, 20, 10)],
        ids=["PART", "TOUCH"],
    )
    result = _run([_inspected("prescription_surface", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert relations.loc["PART", "relation_type"] == "AREA_OVERLAP"
    assert relations.loc["PART", "intersection_area_m2"] == pytest.approx(50.0)
    assert relations.loc["TOUCH", "relation_type"] == "TOUCH_ONLY"
    assert relations.loc["TOUCH", "intersection_area_m2"] == pytest.approx(0.0)
    assert result.parcels.iloc[0]["planning_surface_touch_count"] == 1


def test_overlapping_surface_union_is_not_double_counted() -> None:
    prescription = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10)],
            ids=["WHOLE"],
        ),
    )
    information = _inspected(
        "information_surface",
        _source_frame(
            "information_surface",
            [_rectangle(0, 0, 5, 10)],
            ids=["HALF"],
            type_codes=["99"],
            subtype_codes=["00"],
        ),
    )
    parcel = _run([prescription, information]).parcels.iloc[0]
    assert parcel["planning_surface_intersection_area_sum_m2"] == pytest.approx(150.0)
    assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)
    assert parcel["prescription_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["information_surface_covered_union_area_m2"] == pytest.approx(50.0)


@pytest.mark.parametrize(
    "geometry",
    [
        _rectangle(0, 0, 10, 10),
        MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),
    ],
)
def test_polygon_and_multipolygon_surfaces(geometry: object) -> None:
    result = _run(
        [
            _inspected(
                "information_surface", _source_frame("information_surface", [geometry])
            )
        ]
    )
    assert len(result.relations) == 1
    assert result.relations.iloc[0]["intersection_area_m2"] > 0


def test_line_crossing_and_partly_inside() -> None:
    frame = _source_frame(
        "prescription_line",
        [LineString([(-5, 5), (15, 5)]), LineString([(5, 5), (15, 5)])],
        ids=["CROSS", "PART"],
        type_codes=["15", "15"],
        subtype_codes=["01", "00"],
    )
    result = _run([_inspected("prescription_line", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert relations.loc["CROSS", "relation_type"] == "LENGTH_OVERLAP"
    assert relations.loc["CROSS", "intersection_length_m"] == pytest.approx(10.0)
    assert relations.loc["CROSS", "source_line_length_m"] == pytest.approx(20.0)
    assert relations.loc["PART", "intersection_length_m"] == pytest.approx(5.0)
    parcel = result.parcels.iloc[0]
    assert parcel["planning_line_relation_count"] == 2
    assert parcel["planning_line_intersection_length_sum_m"] == pytest.approx(15.0)


def test_line_boundary_touch_is_zero_length() -> None:
    frame = _source_frame(
        "prescription_line",
        [LineString([(10, 5), (15, 5)])],
        ids=["TOUCH"],
    )
    result = _run([_inspected("prescription_line", frame)])
    assert result.relations.iloc[0]["relation_type"] == "TOUCH_ONLY"
    assert result.relations.iloc[0]["intersection_length_m"] == pytest.approx(0.0)
    assert result.parcels.iloc[0]["planning_line_touch_count"] == 1


@pytest.mark.parametrize(
    "geometry",
    [
        LineString([(-1, 5), (11, 5)]),
        MultiLineString([[(-1, 2), (11, 2)], [(-1, 8), (11, 8)]]),
    ],
)
def test_linestring_and_multilinestring(geometry: object) -> None:
    result = _run(
        [
            _inspected(
                "prescription_line", _source_frame("prescription_line", [geometry])
            )
        ]
    )
    assert result.relations.iloc[0]["intersection_length_m"] > 0


def test_points_inside_boundary_outside_and_multipoint() -> None:
    frame = _source_frame(
        "prescription_point",
        [
            Point(5, 5),
            Point(10, 5),
            Point(20, 20),
            MultiPoint([(3, 3), (10, 4), (30, 30)]),
        ],
        ids=["IN", "BOUNDARY", "OUT", "MULTI"],
        type_codes=["07"] * 4,
        subtype_codes=["00"] * 4,
    )
    result = _run([_inspected("prescription_point", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert set(relations.index) == {"IN", "BOUNDARY", "MULTI"}
    assert relations.loc["IN", "relation_type"] == "INSIDE"
    assert relations.loc["BOUNDARY", "relation_type"] == "BOUNDARY_TOUCH"
    assert relations.loc["MULTI", "point_member_count"] == 3
    assert relations.loc["MULTI", "point_members_inside_count"] == 1
    assert relations.loc["MULTI", "point_members_boundary_count"] == 1
    parcel = result.parcels.iloc[0]
    assert parcel["planning_point_relation_count"] == 3
    assert parcel["planning_point_inside_count"] == 2
    assert parcel["planning_point_boundary_count"] == 2


def test_missing_optional_layer_families_return_stable_empty_catalogs() -> None:
    result = _run([])
    assert result.surface_features.empty
    assert result.line_features.empty
    assert result.point_features.empty
    assert result.relations.empty
    assert result.surface_features.crs.to_epsg() == 2154
    assert str(result.relations["point_member_count"].dtype) == "Int64"
    assert result.parcels.iloc[0]["planning_surface_relation_count"] == 0


def test_optional_raw_source_fields_are_not_fabricated() -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(
        columns=["LIBELLE", "TXT", "NOMFIC", "URLFIC", "DATVALID"]
    )
    result = _run([_inspected("prescription_line", frame)])
    feature = result.line_features.iloc[0]
    for column in (
        "label_raw",
        "text_raw",
        "regulation_filename_raw",
        "regulation_url_raw",
        "source_validity_date_raw",
    ):
        assert pd.isna(feature[column])


def test_epsg4326_parcels_are_measured_in_lambert93_but_preserved() -> None:
    parcel = _parcels(crs="EPSG:4326")
    original = parcel.copy(deep=True)
    result = _run(
        [
            _inspected(
                "prescription_surface",
                _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]),
            )
        ],
        parcel,
    )
    assert result.parcels.crs == original.crs
    assert np.array_equal(result.parcels.geometry.to_wkb(), original.geometry.to_wkb())
    assert result.relations.iloc[0]["intersection_area_m2"] == pytest.approx(100.0)


@pytest.mark.parametrize("bad_id", [None, "", "   ", " X", "X ", 7])
def test_invalid_parcel_ids_are_rejected(bad_id: object) -> None:
    with pytest.raises(PlanningFeaturesError, match="parcel_id"):
        _run([], _parcels(ids=[bad_id]))


def test_duplicate_parcel_ids_are_rejected() -> None:
    with pytest.raises(PlanningFeaturesError, match="unique"):
        _run(
            [],
            _parcels([_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)], ids=["P", "P"]),
        )


def test_duplicate_source_ids_are_rejected() -> None:
    frame = _source_frame(
        "information_surface",
        [_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)],
        ids=["SAME", "SAME"],
    )
    with pytest.raises(PlanningFeaturesError, match="unique"):
        _run([_inspected("information_surface", frame)])


def test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent(
    tmp_path: Path,
) -> None:
    source_layer = "PRESCRIPTION_SURFACE"
    path = tmp_path / f"{source_layer}.shp"
    frame = _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(
        columns="LIB_IDPSC"
    )
    frame.to_file(path, engine="pyogrio")
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = _inspected("prescription_surface", loaded)
    reference = replace(
        layer.reference,
        dataset_path=path,
        source_layer=source_layer,
        driver="ESRI Shapefile",
    )
    layer = replace(
        layer,
        reference=reference,
        summary=_summary(loaded, source_layer),
    )
    result = _run([layer])
    assert result.surface_features.iloc[0]["source_feature_id"] == "OGR_FID:0"
    assert (
        result.surface_features.iloc[0]["source_identity_kind"]
        == "ARCHIVE_SCOPED_OGR_FID"
    )
    assert result.surface_features.iloc[0]["source_identity_field"] == "OGR_FID"
    assert result.surface_features.iloc[0]["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:0"
    )


def test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback() -> None:
    frame = _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(
        columns="LIB_IDPSC"
    )
    result = _run([_inspected("prescription_surface", frame)])
    feature = result.surface_features.iloc[0]
    assert feature["source_feature_id"] == "OGR_FID:1"
    assert feature["source_identity_kind"] == "ARCHIVE_SCOPED_OGR_FID"
    assert feature["source_identity_field"] == "OGR_FID"
    assert feature["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:1"
    )


def test_idurba_mismatch_is_rejected() -> None:
    frame = _source_frame(
        "prescription_line", [LineString([(0, 5), (10, 5)])], document_refs=["OTHER"]
    )
    with pytest.raises(PlanningFeaturesError, match="IDURBA"):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize("missing", ["TYPEPSC", "STYPEPSC", "IDURBA", "LIB_IDPSC"])
def test_missing_required_source_fields_fail(missing: str) -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(
        columns=missing
    )
    with pytest.raises(PlanningFeaturesError, match=missing):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize(
    ("logical", "geometry"),
    [
        ("prescription_surface", LineString([(0, 0), (1, 1)])),
        ("prescription_line", Point(1, 1)),
        ("prescription_point", LineString([(0, 0), (1, 1)])),
    ],
)
def test_wrong_geometry_kind_is_rejected(logical: str, geometry: object) -> None:
    with pytest.raises(PlanningFeaturesError, match="geometry"):
        _run([_inspected(logical, _source_frame(logical, [geometry]))])


def test_invalid_surface_geometry_is_rejected_without_repair() -> None:
    bowtie = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
    with pytest.raises(PlanningFeaturesError, match="valid"):
        _run(
            [
                _inspected(
                    "information_surface",
                    _source_frame("information_surface", [bowtie]),
                )
            ]
        )


@pytest.mark.parametrize("geometry", [None, Polygon()])
def test_null_or_empty_source_geometry_is_rejected(geometry: object) -> None:
    frame = _source_frame("information_surface", [_rectangle(0, 0, 1, 1)])
    frame.geometry = [geometry]
    layer = _inspected("information_surface", frame)
    with pytest.raises(PlanningFeaturesError, match="geometry"):
        _run([layer])


@pytest.mark.parametrize("target", ["parcel", "source"])
def test_missing_crs_is_rejected(target: str) -> None:
    parcel = _parcels(crs=None) if target == "parcel" else _parcels()
    frame = _source_frame(
        "prescription_line",
        [LineString([(0, 5), (10, 5)])],
        crs=None if target == "source" else "EPSG:2154",
    )
    with pytest.raises(PlanningFeaturesError, match="CRS|physical revalidation"):
        _run([_inspected("prescription_line", frame)], parcel)


def test_unusable_source_crs_is_rejected() -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).set_crs(
        LOCAL_ENGINEERING_CRS, allow_override=True
    )
    with pytest.raises(PlanningFeaturesError, match="CRS"):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_document_id", "other"),
        ("source_archive_sha256", "b" * 64),
        ("source_layer", "other"),
        ("feature_count", 99),
        ("geometry_types", (("Point", 1),)),
    ],
)
def test_mutated_source_summary_is_rejected(field: str, value: object) -> None:
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    planning_document = _planning_document([layer])
    stored = planning_document.related_layers[0]
    corrupted = replace(stored, summary=replace(stored.summary, **{field: value}))
    changed = replace(planning_document, related_layers=(corrupted,))
    with pytest.raises(PlanningFeaturesError, match="summary|physical revalidation"):
        intersect_parcels_with_gpu_planning_features(_parcels(), changed)


@pytest.mark.parametrize("bad_count", [True, -1, 1.5, float("inf"), "1"])
def test_source_summary_counts_are_strict_integers(bad_count: object) -> None:
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    planning_document = _planning_document([layer])
    stored = planning_document.related_layers[0]
    corrupted = replace(
        stored, summary=replace(stored.summary, feature_count=bad_count)
    )
    changed = replace(planning_document, related_layers=(corrupted,))
    with pytest.raises(
        PlanningFeaturesError,
        match="integer count|non-negative|summary|physical revalidation",
    ):
        intersect_parcels_with_gpu_planning_features(_parcels(), changed)


def test_reserved_output_column_collision_is_rejected() -> None:
    parcels = _parcels()
    parcels["planning_surface_relation_count"] = 99
    with pytest.raises(PlanningFeaturesError, match="output columns"):
        _run([], parcels)


def test_inputs_and_all_existing_parcel_fields_are_preserved() -> None:
    parcels = _parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)])
    frame = _source_frame(
        "prescription_surface", [_rectangle(0, 0, 5, 10)], ids=["PSC"]
    )
    planning = _planning_document([_inspected("prescription_surface", frame)])
    parcels_before = parcels.copy(deep=True)
    zoning_before = planning.related_layers[0].data.copy(deep=True)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning)
    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(planning.related_layers[0].data, zoning_before)
    assert result.parcels["parcel_id"].tolist() == parcels["parcel_id"].tolist()
    assert result.parcels.index.equals(parcels.index)
    assert result.parcels["existing_zoning_fact"].equals(
        parcels["existing_zoning_fact"]
    )
    assert np.array_equal(result.parcels.geometry.to_wkb(), parcels.geometry.to_wkb())


def test_relations_are_unique_deterministic_and_summaries_agree() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)], ids=["P-B", "P-A"]
    )
    surface = _inspected(
        "information_surface",
        _source_frame("information_surface", [_rectangle(-1, -1, 31, 31)], ids=["I"]),
    )
    line = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(-1, 5), (11, 5)])], ids=["L"]),
    )
    result = _run([surface, line], parcels)
    assert not result.relations.duplicated(["parcel_id", "planning_feature_id"]).any()
    assert result.relations["parcel_id"].tolist() == ["P-B", "P-B", "P-A"]
    first = result.parcels.iloc[0]
    assert first["planning_surface_relation_count"] == int(
        (
            (result.relations["parcel_id"] == "P-B")
            & (result.relations["geometry_kind"] == "SURFACE")
        ).sum()
    )
    assert first["planning_line_intersection_length_sum_m"] == pytest.approx(
        result.relations.loc[
            (result.relations["parcel_id"] == "P-B")
            & (result.relations["geometry_kind"] == "LINE"),
            "intersection_length_m",
        ].sum()
    )


def test_result_frames_are_independent_from_mutable_inputs() -> None:
    parcels = _parcels()
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    result = _run([layer], parcels)
    snapshot = deepcopy(result.relations)
    parcels.loc[50, "existing_zoning_fact"] = -1
    layer.data.loc[0, "LIBELLE"] = "mutated"
    assert_frame_equal(result.relations, snapshot)


@pytest.mark.parametrize(
    ("logical", "catalog_name"),
    [
        ("prescription_surface", "surface_features"),
        ("prescription_line", "line_features"),
        ("prescription_point", "point_features"),
    ],
)
def test_present_empty_optional_layer_is_valid(
    logical: str,
    catalog_name: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    frame = _source_frame(logical, [])
    fid_reads = 0
    if logical == "prescription_surface":
        frame = frame.drop(columns="LIB_IDPSC")
        real_read_dataframe = gpu_source_module.pyogrio.read_dataframe

        def unexpected_fid_read(*args: object, **kwargs: object) -> object:
            nonlocal fid_reads
            if kwargs.get("fid_as_index"):
                fid_reads += 1
            return real_read_dataframe(*args, **kwargs)

        monkeypatch.setattr(
            gpu_source_module.pyogrio,
            "read_dataframe",
            unexpected_fid_read,
        )
    result = _run([_inspected(logical, frame)])
    catalog = getattr(result, catalog_name)
    assert catalog.empty
    assert catalog.crs.to_epsg() == 2154
    assert result.relations.empty
    assert len(result.parcels) == 1
    assert result.parcels.iloc[0]["planning_feature_document_id"] == DOCUMENT_ID
    if logical == "prescription_surface":
        assert fid_reads == 1


def _contract_result() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    parcels = _parcels()
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(-1, 5), (11, 5)])],
                ids=["LINE"],
            ),
        ),
        _inspected(
            "prescription_point",
            _source_frame("prescription_point", [Point(5, 5)], ids=["POINT"]),
        ),
    ]
    planning_document = _planning_document(layers)
    return (
        planning_document,
        parcels,
        intersect_parcels_with_gpu_planning_features(parcels, planning_document),
    )


def _source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    parcels = _parcels()
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
                type_codes=["07"],
                subtype_codes=["04"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(-1, 5), (11, 5)])],
                ids=["LINE"],
                type_codes=["15"],
                subtype_codes=["00"],
            ),
        ),
        _inspected(
            "prescription_point",
            _source_frame(
                "prescription_point",
                [Point(5, 5)],
                ids=["POINT"],
                type_codes=["07"],
                subtype_codes=["00"],
            ),
        ),
    ]
    planning_document = _planning_document(layers)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    return planning_document, parcels, result


def _two_parcel_source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    """Build equal-area parcels so relation identity cannot hide behind area checks."""

    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        ids=["P-1", "P-2"],
    )
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
                type_codes=["07"],
                subtype_codes=["04"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(0, 5), (10, 5)])],
                ids=["LINE"],
                type_codes=["15"],
                subtype_codes=["00"],
            ),
        ),
    ]
    planning_document = _planning_document(layers)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    return planning_document, parcels, result


def _validate_source_complete(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
) -> PlanningFeatureInputValidation:
    return validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    )


def _replace_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    frame: gpd.GeoDataFrame,
) -> GpuPlanningDocument:
    related: list[GpuInspectedLayer] = []
    for layer in planning_document.related_layers:
        if layer.logical_name != logical_name:
            related.append(layer)
            continue
        related.append(
            replace(
                layer,
                data=frame,
                summary=_summary(frame, layer.reference.source_layer),
            )
        )
    return replace(planning_document, related_layers=tuple(related))


def _without_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
) -> GpuPlanningDocument:
    return replace(
        planning_document,
        related_layers=tuple(
            layer
            for layer in planning_document.related_layers
            if layer.logical_name != logical_name
        ),
    )


def _refresh_extraction_inventory(
    planning_document: GpuPlanningDocument,
) -> GpuPlanningDocument:
    extraction = planning_document.extraction
    files = _physical_inventory(extraction.extraction_root)
    _write_extraction_manifest(
        extraction.extraction_root,
        extraction.archive.sha256,
        files,
    )
    updated_extraction = replace(extraction, files=files)
    return replace(
        planning_document,
        extraction=updated_extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(
            updated_extraction
        ),
    )


def _replace_layer_reference(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    reference: GpuSpatialLayerReference,
) -> GpuPlanningDocument:
    related = tuple(
        replace(layer, reference=reference)
        if layer.logical_name == logical_name
        else layer
        for layer in planning_document.related_layers
    )
    old_reference = next(
        layer.reference
        for layer in planning_document.related_layers
        if layer.logical_name == logical_name
    )
    spatial = tuple(
        reference if item == old_reference else item
        for item in planning_document.all_spatial_layers
    )
    return replace(
        planning_document,
        related_layers=related,
        all_spatial_layers=spatial,
    )


def test_public_normalized_input_contract_validates_step_7d_3_1_result() -> None:
    planning_document, parcels, result = _source_complete_contract()
    validation = validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    )
    assert isinstance(validation, PlanningFeatureInputValidation)
    assert validation.related_source_layer_count == 3
    assert validation.related_source_file_count == 3
    assert validation.expected_relation_count == len(result.relations)
    for value in (
        validation.gpu_related_source_files_sha256,
        validation.expected_relations_content_sha256,
    ):
        assert len(value) == 64
        int(value, 16)


def test_public_normalized_input_contract_wraps_malformed_document_context() -> None:
    planning_document, parcels, result = _source_complete_contract()
    malformed = replace(planning_document, related_layers=(None,))  # type: ignore[arg-type]
    with pytest.raises(PlanningFeaturesError) as caught:
        _validate_source_complete(malformed, parcels, result)
    assert isinstance(caught.value.__cause__, (AttributeError, TypeError))


def test_source_complete_contract_binds_inspected_spatial_inventory() -> None:
    planning_document, parcels, result = _source_complete_contract()
    missing_inventory = replace(planning_document, all_spatial_layers=())
    with pytest.raises(PlanningFeaturesError, match="inventory|reference"):
        _validate_source_complete(missing_inventory, parcels, result)


def test_public_normalized_input_contract_is_exported() -> None:
    from landscout import stages

    assert (
        stages.validate_normalized_planning_feature_inputs
        is validate_normalized_planning_feature_inputs
    )
    assert "validate_normalized_planning_feature_inputs" in stages.__all__
    assert stages.PlanningFeatureInputValidation is PlanningFeatureInputValidation
    assert "PlanningFeatureInputValidation" in stages.__all__


def test_public_source_validation_hashes_survive_parquet_readback(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    original = _validate_source_complete(planning_document, parcels, result)
    paths = {
        "surface_features": tmp_path / "surface.parquet",
        "line_features": tmp_path / "line.parquet",
        "point_features": tmp_path / "point.parquet",
        "relations": tmp_path / "relations.parquet",
    }
    result.surface_features.to_parquet(paths["surface_features"], index=False)
    result.line_features.to_parquet(paths["line_features"], index=False)
    result.point_features.to_parquet(paths["point_features"], index=False)
    result.relations.to_parquet(paths["relations"], index=False)
    validation = validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        gpd.read_parquet(paths["surface_features"]),
        gpd.read_parquet(paths["line_features"]),
        gpd.read_parquet(paths["point_features"]),
        pd.read_parquet(paths["relations"]),
    )
    assert validation == original


def test_public_normalized_input_contract_rejects_stripped_catalog() -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.drop(columns="label_raw")
    with pytest.raises(PlanningFeaturesError, match="schema|label_raw"):
        validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            surface,
            result.line_features,
            result.point_features,
            result.relations,
        )


def test_empty_and_nonempty_catalogs_have_identical_kind_schemas() -> None:
    _, _, populated = _contract_result()
    empty = _run([])
    for populated_catalog, empty_catalog in zip(
        (
            populated.surface_features,
            populated.line_features,
            populated.point_features,
        ),
        (empty.surface_features, empty.line_features, empty.point_features),
        strict=True,
    ):
        assert list(empty_catalog.columns) == list(populated_catalog.columns)


@pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])
def test_strict_relation_integer_counts_are_enforced(bad_count: object) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    relations["point_member_count"] = relations["point_member_count"].astype(object)
    point_index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[point_index, "point_member_count"] = bad_count
    with pytest.raises(
        PlanningFeaturesError, match="integer count|non-negative|dtype|schema"
    ):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


@pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])
def test_strict_parcel_summary_integer_counts_are_enforced(
    bad_count: object,
) -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels["planning_line_relation_count"] = parcels[
        "planning_line_relation_count"
    ].astype(object)
    parcels.loc[parcels.index[0], "planning_line_relation_count"] = bad_count
    with pytest.raises(PlanningFeaturesError, match="integer count|non-negative"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )


@pytest.mark.parametrize(
    ("kind", "column", "value"),
    [
        ("SURFACE", "relation_type", "TOUCH_ONLY"),
        ("SURFACE", "parcel_share_pct", 42.0),
        ("SURFACE", "intersection_area_m2", None),
        ("SURFACE", "source_line_length_m", 0.0),
        ("LINE", "relation_type", "TOUCH_ONLY"),
        ("LINE", "intersection_length_m", 999.0),
        ("POINT", "relation_type", "BOUNDARY_TOUCH"),
    ],
)
def test_corrupted_relation_semantics_are_rejected(
    kind: str,
    column: str,
    value: object,
) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == kind][0]
    relations[column] = relations[column].astype(object)
    relations.loc[index, column] = value
    with pytest.raises(PlanningFeaturesError):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


def test_point_member_relation_semantics_are_exact() -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[index, "point_members_inside_count"] = 0
    relations.loc[index, "point_members_boundary_count"] = 1
    with pytest.raises(PlanningFeaturesError, match="relation type"):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


@pytest.mark.parametrize(
    "case",
    [
        "surface-inside",
        "line-area",
        "point-touch",
        "area-zero",
        "surface-touch-positive",
        "length-zero",
        "line-touch-positive",
        "inside-zero",
        "boundary-with-inside",
        "area-exceeds-feature",
        "share-inconsistent",
        "non-finite",
        "negative",
    ],
)
def test_shared_intrinsic_relation_semantics_reject_every_invalid_case(
    case: str,
) -> None:
    _, _, result = _contract_result()
    relations = result.relations.copy(deep=True)
    surface = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    line = relations.index[relations["geometry_kind"].eq("LINE")][0]
    point = relations.index[relations["geometry_kind"].eq("POINT")][0]
    if case == "surface-inside":
        relations.loc[surface, "relation_type"] = "INSIDE"
    elif case == "line-area":
        relations.loc[line, "relation_type"] = "AREA_OVERLAP"
    elif case == "point-touch":
        relations.loc[point, "relation_type"] = "TOUCH_ONLY"
    elif case == "area-zero":
        relations.loc[
            surface, ["intersection_area_m2", "parcel_share_pct", "feature_share_pct"]
        ] = 0.0
    elif case == "surface-touch-positive":
        relations.loc[surface, "relation_type"] = "TOUCH_ONLY"
    elif case == "length-zero":
        relations.loc[line, "intersection_length_m"] = 0.0
    elif case == "line-touch-positive":
        relations.loc[line, "relation_type"] = "TOUCH_ONLY"
    elif case == "inside-zero":
        relations.loc[point, "point_members_inside_count"] = 0
    elif case == "boundary-with-inside":
        relations.loc[point, "relation_type"] = "BOUNDARY_TOUCH"
        relations.loc[point, "point_members_boundary_count"] = 1
    elif case == "area-exceeds-feature":
        relations.loc[surface, "intersection_area_m2"] = (
            float(relations.loc[surface, "feature_area_m2"]) + 1.0
        )
    elif case == "share-inconsistent":
        relations.loc[surface, "parcel_share_pct"] = 42.0
    elif case == "non-finite":
        relations.loc[surface, "feature_share_pct"] = float("inf")
    else:
        relations.loc[surface, "intersection_area_m2"] = -1.0
    with pytest.raises((TypeError, ValueError)):
        validate_intrinsic_planning_feature_relations(relations)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "NOT_A_KIND"),
        ("source_identity_field", "WRONG_FIELD"),
        ("feature_family", "INFORMATION"),
        ("geometry_kind", "LINE"),
        ("type_code_raw", "MUTATED"),
        ("source_archive_sha256", "b" * 64),
    ],
)
def test_relation_must_match_feature_catalog(
    column: str,
    value: object,
) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[0]
    if column == "geometry_kind":
        index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    relations.loc[index, column] = value
    with pytest.raises(
        PlanningFeaturesError,
        match="catalog|geometry kind|LINE relation|unrelated metric",
    ):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


def test_feature_ids_are_globally_unique_across_catalogs() -> None:
    planning_document, source, result = _contract_result()
    points = result.point_features.copy(deep=True)
    points.loc[points.index[0], "planning_feature_id"] = result.surface_features.iloc[
        0
    ]["planning_feature_id"]
    with pytest.raises(PlanningFeaturesError, match="globally unique|deterministic"):
        _validate_result(
            source,
            replace(result, point_features=points),
            planning_document=planning_document,
        )


def test_same_source_id_is_allowed_in_distinct_logical_layers() -> None:
    result = _run(
        [
            _inspected(
                "prescription_line",
                _source_frame(
                    "prescription_line",
                    [LineString([(0, 2), (10, 2)])],
                    ids=["SHARED"],
                ),
            ),
            _inspected(
                "prescription_point",
                _source_frame("prescription_point", [Point(5, 5)], ids=["SHARED"]),
            ),
        ]
    )
    assert len(result.relations) == 2
    assert result.relations["planning_feature_id"].nunique() == 2


def test_corrupted_parcel_summary_is_rejected() -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "planning_surface_relation_count"] += 1
    with pytest.raises(PlanningFeaturesError, match="inconsistent with relations"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )


def test_corrupted_surface_union_contract_is_rejected() -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "planning_surface_covered_union_area_m2"] = 1000.0
    with pytest.raises(PlanningFeaturesError, match="union"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )


def test_geospatial_operation_failure_is_controlled_and_chained(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_join(*args: object, **kwargs: object) -> object:
        raise RuntimeError("synthetic spatial-index failure")

    monkeypatch.setattr(planning_features_module.gpd, "sjoin", fail_join)
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    with pytest.raises(PlanningFeaturesError, match="spatial join") as caught:
        _run([layer])
    assert isinstance(caught.value.__cause__, RuntimeError)


def test_source_complete_contract_rejects_unknown_relation_parcel() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = "NOT-A-SOURCE-PARCEL"
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="parcel|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_coherent_parcel_metric_mutation() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    surface_mask = relations["geometry_kind"].eq("SURFACE")
    relations.loc[surface_mask, "parcel_metric_area_m2"] = 200.0
    relations.loc[surface_mask, "parcel_share_pct"] = 50.0
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="parcel|metric|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_same_area_wrong_parcel_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = "P-2"
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|parcel|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_missing_expected_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    corrupted = replace(result, relations=result.relations.iloc[1:].copy())
    with pytest.raises(PlanningFeaturesError, match="relation|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_extra_geometrically_false_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    extra = result.relations.iloc[[0]].copy(deep=True)
    extra.loc[extra.index[0], "parcel_id"] = "P-2"
    relations = pd.concat([result.relations, extra], ignore_index=True)
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_reordered_relations() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.iloc[::-1].reset_index(drop=True)
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|order|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)


@pytest.mark.parametrize(
    ("column", "dtype"),
    [
        ("intersection_area_m2", "object"),
        ("point_member_count", "object"),
        ("relation_type", "category"),
    ],
)
def test_source_complete_contract_rejects_noncanonical_relation_dtype(
    column: str,
    dtype: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations[column] = relations[column].astype(dtype)
    with pytest.raises(PlanningFeaturesError, match="schema|dtype|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )


def test_source_complete_contract_rejects_relation_index_name_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.index = relations.index.rename("changed_relation_row")
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )


def test_source_complete_contract_rejects_relation_index_dtype_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.index = pd.Index(
        np.asarray(relations.index, dtype="int32"),
        name=relations.index.name,
    )
    assert str(relations.index.dtype) == "int32"
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )


def test_source_complete_contract_rejects_relation_index_class_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    assert type(result.relations.index) is pd.RangeIndex
    relations = result.relations.copy(deep=True)
    relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
    assert type(relations.index) is pd.Index
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            result.surface_features,
            result.line_features,
            result.point_features,
            relations,
        )


def test_expected_relation_hash_binds_dtype_and_index_metadata() -> None:
    _, _, result = _source_complete_contract()
    original = planning_features_module._expected_relations_content_sha256(
        result.relations
    )
    object_dtype = result.relations.copy(deep=True)
    object_dtype["intersection_area_m2"] = object_dtype["intersection_area_m2"].astype(
        "object"
    )
    named_index = result.relations.copy(deep=True)
    named_index.index = named_index.index.rename("relation_row")
    int32_index = result.relations.copy(deep=True)
    int32_index.index = pd.Index(
        np.asarray(int32_index.index, dtype="int32"),
        name=int32_index.index.name,
    )
    index_class = result.relations.copy(deep=True)
    index_class.index = pd.Index(index_class.index.to_numpy(), dtype="int64")
    assert original != planning_features_module._expected_relations_content_sha256(
        object_dtype
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        named_index
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        int32_index
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        index_class
    )


def test_source_complete_contract_rejects_coherent_but_wrong_line_metric() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.copy(deep=True)
    line_mask = relations["geometry_kind"].eq("LINE")
    relations.loc[line_mask, "intersection_length_m"] = 5.0
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|metric|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_accepts_complete_parcel_output_summaries() -> None:
    planning_document, _, result = _source_complete_contract()
    _validate_source_complete(planning_document, result.parcels, result)


def test_source_complete_contract_rejects_partial_parcel_output_columns() -> None:
    planning_document, parcels, result = _source_complete_contract()
    partial = parcels.copy(deep=True)
    partial["planning_surface_relation_count"] = 1
    with pytest.raises(PlanningFeaturesError, match="[Pp]arcel|output|summary|columns"):
        _validate_source_complete(planning_document, partial, result)


def test_source_complete_contract_rejects_corrupted_complete_parcel_summaries() -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted.loc[corrupted.index[0], "planning_surface_relation_count"] += 1
    with pytest.raises(PlanningFeaturesError, match="parcel|summary|relation"):
        _validate_source_complete(planning_document, corrupted, result)


def test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype() -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted["planning_surface_covered_pct"] = corrupted[
        "planning_surface_covered_pct"
    ].astype("float32")
    with pytest.raises(PlanningFeaturesError, match="parcel|schema|dtype|summary"):
        _validate_source_complete(planning_document, corrupted, result)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_document_id", "other-document"),
        ("planning_feature_archive_sha256", "f" * 64),
        ("planning_surface_covered_union_area_m2", 50.0),
        ("planning_surface_covered_pct", 50.0),
        ("planning_line_intersection_length_sum_m", 5.0),
        ("planning_point_inside_count", 0),
    ],
)
def test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact(
    column: str,
    value: object,
) -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted.loc[corrupted.index[0], column] = value
    with pytest.raises(
        PlanningFeaturesError,
        match="parcel|summary|relation|lineage|document|archive|union|percentage",
    ):
        _validate_source_complete(planning_document, corrupted, result)


def test_source_complete_contract_rejects_duplicate_parcel_ids() -> None:
    planning_document, parcels, result = _source_complete_contract()
    duplicate = pd.concat([parcels, parcels], ignore_index=True)
    duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=parcels.crs)
    with pytest.raises(PlanningFeaturesError, match="parcel_id|unique"):
        _validate_source_complete(planning_document, duplicate, result)


def test_source_complete_contract_rejects_invalid_parcel_geometry() -> None:
    planning_document, parcels, result = _source_complete_contract()
    invalid = parcels.copy(deep=True)
    invalid.at[invalid.index[0], "geometry"] = Polygon(
        [(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]
    )
    with pytest.raises(PlanningFeaturesError, match="valid|geometry"):
        _validate_source_complete(planning_document, invalid, result)


def test_source_complete_contract_accepts_epsg4326_parcels() -> None:
    planning_document, parcels, _ = _source_complete_contract()
    geographic = parcels.to_crs("EPSG:4326")
    result = intersect_parcels_with_gpu_planning_features(geographic, planning_document)
    _validate_source_complete(planning_document, geographic, result)


def test_source_document_reference_allows_one_archive_zip_suffix() -> None:
    planning_document, parcels, _ = _source_complete_contract()
    archive = planning_document.extraction.archive
    metadata = replace(archive.document, archive_name=f"{ARCHIVE_NAME}.zip")
    suffixed = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=metadata),
        ),
    )
    result = intersect_parcels_with_gpu_planning_features(parcels, suffixed)
    assert (
        result.surface_features["source_archive_name"].eq(f"{ARCHIVE_NAME}.zip").all()
    )
    assert (
        result.surface_features["source_document_reference_raw"].eq(ARCHIVE_NAME).all()
    )
    _validate_source_complete(suffixed, parcels, result)


@pytest.mark.parametrize(
    "identity_column", ["planning_feature_id", "source_feature_id"]
)
def test_source_complete_contract_rejects_coherently_renamed_feature_identity(
    identity_column: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.copy(deep=True)
    relations = result.relations.copy(deep=True)
    old = surface.iloc[0][identity_column]
    new = (
        f"GPU:{DOCUMENT_ID}:prescription_surface:RENAMED"
        if identity_column == "planning_feature_id"
        else "RENAMED"
    )
    surface.loc[surface.index[0], identity_column] = new
    relations.loc[relations[identity_column].eq(old), identity_column] = new
    corrupted = replace(result, surface_features=surface, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="source|identity|rebuilt|catalog"):
        _validate_source_complete(planning_document, parcels, corrupted)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_provider", "Another provider"),
        ("source_portal", "https://example.invalid"),
        ("source_commune_code", "99999"),
        ("source_document_type", "CC"),
        ("source_archive_name", "OTHER_ARCHIVE"),
        ("source_document_reference_raw", "OTHER_ARCHIVE"),
        ("source_layer", "OTHER_SOURCE_LAYER"),
        ("source_crs", "EPSG:4326"),
    ],
)
def test_source_complete_contract_rejects_independent_gpu_lineage_mutation(
    column: str,
    value: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.copy(deep=True)
    relations = result.relations.copy(deep=True)
    surface.loc[surface.index[0], column] = value
    if column in relations.columns:
        feature_id = result.surface_features.iloc[0]["planning_feature_id"]
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = value
    corrupted = replace(result, surface_features=surface, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="source|lineage|catalog|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)


@pytest.mark.parametrize(
    ("metadata_field", "value"),
    [
        ("provider", "Another provider"),
        ("portal", "https://example.invalid"),
        ("commune_code", "99999"),
        ("document_type", "CC"),
        ("archive_name", "OTHER_ARCHIVE"),
    ],
)
def test_source_complete_contract_binds_gpu_document_context(
    metadata_field: str,
    value: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    archive = planning_document.extraction.archive
    metadata = replace(archive.document, **{metadata_field: value})
    changed = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=metadata),
        ),
    )
    with pytest.raises(
        PlanningFeaturesError,
        match="source|lineage|document|rebuilt|IDURBA|archive",
    ):
        _validate_source_complete(changed, parcels, result)


@pytest.mark.parametrize("mutation", ["geometry", "raw", "code", "remove", "extra"])
def test_source_complete_contract_reloads_and_compares_source_catalog(
    mutation: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = next(
        layer
        for layer in planning_document.related_layers
        if layer.logical_name == "prescription_surface"
    )
    frame = layer.data.copy(deep=True)
    if mutation == "geometry":
        frame.at[frame.index[0], "geometry"] = _rectangle(0, 0, 5, 10)
    elif mutation == "raw":
        frame.loc[frame.index[0], "LIBELLE"] = "Changed source label"
    elif mutation == "code":
        frame.loc[frame.index[0], ["TYPEPSC", "STYPEPSC"]] = ["01", "00"]
    elif mutation == "remove":
        frame = frame.iloc[0:0].copy()
    else:
        extra = frame.copy(deep=True)
        extra.loc[extra.index[0], "LIB_IDPSC"] = "EXTRA"
        extra.at[extra.index[0], "geometry"] = _rectangle(20, 20, 21, 21)
        frame = gpd.GeoDataFrame(
            pd.concat([frame, extra], ignore_index=True),
            geometry="geometry",
            crs=frame.crs,
        )
    changed = _replace_related_layer(planning_document, "prescription_surface", frame)
    with pytest.raises(
        PlanningFeaturesError, match="source|catalog|rebuilt|normalized"
    ):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_catalog_for_absent_gpu_layer() -> None:
    planning_document, parcels, result = _source_complete_contract()
    changed = _without_related_layer(planning_document, "prescription_surface")
    with pytest.raises(PlanningFeaturesError, match="source|layer|catalog|rebuilt"):
        _validate_source_complete(changed, parcels, result)


@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        (
            "surface_features",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
        ),
        ("line_features", LineString([(-1, 5, 1), (11, 5, 1)])),
        ("point_features", Point(5, 5, 1)),
    ],
)
def test_three_dimensional_normalized_catalogs_are_rejected(
    catalog_name: str,
    geometry: object,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    catalog = getattr(result, catalog_name).copy(deep=True)
    catalog.at[catalog.index[0], "geometry"] = geometry
    corrupted = replace(result, **{catalog_name: catalog})
    with pytest.raises(PlanningFeaturesError, match="2D|dimensional|Z"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_two_dimensional_normalized_catalogs_remain_valid() -> None:
    planning_document, parcels, result = _source_complete_contract()
    for catalog in (
        result.surface_features,
        result.line_features,
        result.point_features,
    ):
        assert not catalog.geometry.has_z.any()
    _validate_source_complete(planning_document, parcels, result)


@pytest.mark.parametrize(
    ("logical", "geometry", "catalog_name"),
    [
        (
            "prescription_surface",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
            "surface_features",
        ),
        (
            "prescription_line",
            LineString([(0, 5, 1), (10, 5, 1)]),
            "line_features",
        ),
        ("prescription_point", Point(5, 5, 1), "point_features"),
    ],
)
def test_gpu_source_z_is_normalized_to_canonical_2d(
    logical: str,
    geometry: object,
    catalog_name: str,
) -> None:
    result = _run([_inspected(logical, _source_frame(logical, [geometry]))])
    catalog = getattr(result, catalog_name)
    assert not catalog.geometry.has_z.any()


def test_source_complete_contract_rejects_tampered_gpkg_inventory_hash() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    relative = layer.reference.dataset_path.relative_to(
        planning_document.extraction.extraction_root
    ).as_posix()
    files = tuple(
        replace(item, sha256="f" * 64) if item.relative_path == relative else item
        for item in planning_document.extraction.files
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|SHA"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_tampered_gpkg_size() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    relative = layer.reference.dataset_path.relative_to(
        planning_document.extraction.extraction_root
    ).as_posix()
    files = tuple(
        replace(item, size_bytes=item.size_bytes + 1)
        if item.relative_path == relative
        else item
        for item in planning_document.extraction.files
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|size"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_changed_gpkg_bytes() -> None:
    planning_document, parcels, result = _source_complete_contract()
    path = planning_document.related_layers[0].reference.dataset_path
    with path.open("ab") as stream:
        stream.write(b"tamper")
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|size|SHA"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_rejects_same_size_gpkg_byte_tamper() -> None:
    planning_document, parcels, result = _source_complete_contract()
    path = planning_document.related_layers[0].reference.dataset_path
    payload = bytearray(path.read_bytes())
    payload[-1] ^= 1
    path.write_bytes(payload)
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|SHA"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_rejects_coherently_changed_physical_gpkg() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    changed_source = layer.data.copy(deep=True)
    changed_source.loc[changed_source.index[0], "LIBELLE"] = "Changed on disk"
    changed_source.to_file(
        layer.reference.dataset_path,
        layer=layer.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|file|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)


def test_source_complete_contract_rejects_changed_physical_gpkg_geometry() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    changed_source = layer.data.copy(deep=True)
    changed_source.at[changed_source.index[0], "geometry"] = _rectangle(0, 0, 5, 10)
    changed_source.to_file(
        layer.reference.dataset_path,
        layer=layer.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|geometry|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)


def test_source_complete_contract_rejects_reordered_physical_gpkg_rows() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        ids=["P-1", "P-2"],
    )
    layer = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            ids=["ONE", "TWO"],
            type_codes=["07", "07"],
            subtype_codes=["04", "04"],
        ),
    )
    planning_document = _planning_document([layer])
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    stored = planning_document.related_layers[0]
    stored.data.iloc[::-1].reset_index(drop=True).to_file(
        stored.reference.dataset_path,
        layer=stored.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|order|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)


def test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    loaded = layer.data.copy(deep=True)
    loaded.attrs["unpersisted_source_note"] = "tampered"
    changed = replace(
        planning_document,
        related_layers=tuple(
            replace(item, data=loaded) if item is layer else item
            for item in planning_document.related_layers
        ),
    )
    with pytest.raises(PlanningFeaturesError, match="source|attrs|metadata|loaded"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_dataset_outside_extraction_root(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    outside = tmp_path / "outside.gpkg"
    shutil.copyfile(layer.reference.dataset_path, outside)
    reference = replace(layer.reference, dataset_path=outside)
    changed = _replace_layer_reference(planning_document, layer.logical_name, reference)
    with pytest.raises(PlanningFeaturesError, match="source|root|outside|contain"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_linked_spatial_dataset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    dataset = planning_document.related_layers[0].reference.dataset_path
    actual_link_check = gpu_source_module._is_link_or_junction

    def synthetic_link(path: Path) -> bool:
        return path == dataset or actual_link_check(path)

    monkeypatch.setattr(
        gpu_source_module,
        "_is_link_or_junction",
        synthetic_link,
    )
    with pytest.raises(PlanningFeaturesError, match="source|link|junction|dataset"):
        _validate_source_complete(planning_document, parcels, result)


def _shapefile_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
    source_layer = "PRESCRIPTION_SURFACE"
    path = root / f"{source_layer}.shp"
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 10, 10)],
        ids=["SHAPE-1"],
        type_codes=["07"],
        subtype_codes=["04"],
    )
    frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio", index=False)
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = replace(
        _inspected("prescription_surface", loaded),
        reference=GpuSpatialLayerReference(path, source_layer, "ESRI Shapefile"),
        summary=_summary(loaded, source_layer),
    )
    document = _planning_document([layer])
    parcels = _parcels()
    result = intersect_parcels_with_gpu_planning_features(parcels, document)
    return document, parcels, result


def _shapefile_ogr_fid_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
    source_layer = "PRESCRIPTION_SURFACE"
    path = root / f"{source_layer}.shp"
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
        ids=["DROP-ONE", "DROP-TWO"],
        type_codes=["07", "07"],
        subtype_codes=["04", "04"],
    ).drop(columns="LIB_IDPSC")
    frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio", index=False)
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = replace(
        _inspected("prescription_surface", loaded),
        reference=GpuSpatialLayerReference(path, source_layer, "ESRI Shapefile"),
        summary=_summary(loaded, source_layer),
    )
    document = _planning_document([layer])
    parcels = _parcels()
    result = intersect_parcels_with_gpu_planning_features(parcels, document)
    return document, parcels, result


def test_source_complete_contract_binds_every_shapefile_sidecar(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    sidecar = next(
        item
        for item in planning_document.extraction.files
        if item.relative_path.casefold().endswith(".prj")
    )
    files = tuple(
        item
        for item in planning_document.extraction.files
        if item.relative_path != sidecar.relative_path
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(
        PlanningFeaturesError,
        match="shapefile|sidecar|inventory|physical revalidation",
    ):
        _validate_source_complete(changed, parcels, result)


@pytest.mark.parametrize("changed_fids", [(10, 11), (1, 0)])
def test_source_complete_contract_rejects_changed_or_reordered_ogr_fids(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    changed_fids: tuple[int, int],
) -> None:
    planning_document, parcels, result = _shapefile_ogr_fid_source_complete_contract(
        tmp_path
    )
    actual_read = gpu_source_module.pyogrio.read_dataframe

    def changed_fid_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        reread = actual_read(*args, **kwargs)
        if kwargs.get("fid_as_index"):
            reread.index = pd.Index(changed_fids, name="fid")
        return reread

    monkeypatch.setattr(
        gpu_source_module.pyogrio,
        "read_dataframe",
        changed_fid_read,
    )
    with pytest.raises(PlanningFeaturesError, match="source|FID|identity|catalog"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_requires_shapefile_core_members(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    layer = planning_document.related_layers[0]
    layer.reference.dataset_path.with_suffix(".shx").unlink()
    with pytest.raises(PlanningFeaturesError, match="shapefile|shx|source|file"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    layer = planning_document.related_layers[0]
    cpg = layer.reference.dataset_path.with_suffix(".cpg")
    cpg.write_text("UTF-8\n", encoding="utf-8")
    with pytest.raises(
        PlanningFeaturesError,
        match="shapefile|sidecar|size|SHA|physical revalidation",
    ):
        _validate_source_complete(planning_document, parcels, result)


def test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    _validate_source_complete(planning_document, parcels, result)
    primary = planning_document.related_layers[0].reference.dataset_path
    sibling = primary.with_name(f"{primary.stem}.archive.shp")
    gpd.GeoDataFrame(
        {"sibling": [1]},
        geometry=[_rectangle(20, 20, 21, 21)],
        crs="EPSG:2154",
    ).to_file(sibling, driver="ESRI Shapefile", engine="pyogrio", index=False)
    refreshed = _refresh_extraction_inventory(planning_document)
    with pytest.raises(
        PlanningFeaturesError,
        match="Related GPU spatial sources failed physical revalidation",
    ):
        _validate_source_complete(refreshed, parcels, result)


@pytest.mark.parametrize("bad_item", [None, object()])
def test_batch_gpu_revalidation_rejects_malformed_layer_items(
    bad_item: object,
) -> None:
    planning_document, _, _ = _source_complete_contract()
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            planning_document,
            (bad_item,),  # type: ignore[arg-type]
        )


def test_batch_gpu_revalidation_rejects_malformed_planning_document() -> None:
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            object(),  # type: ignore[arg-type]
            (),
        )


def test_batch_gpu_revalidation_rejects_duplicate_logical_name() -> None:
    planning_document, _, _ = _source_complete_contract()
    layer = planning_document.related_layers[0]
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError, match="duplicate"):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            planning_document,
            (layer, layer),
        )


@pytest.mark.parametrize(
    "statement",
    [
        (
            "from landscout.common.planning_feature_contract import "
            "validate_intrinsic_planning_feature_relations"
        ),
        (
            "from landscout.common.bess_application_contract import "
            "validate_bess_application_feature_catalogs"
        ),
    ],
)
def test_common_planning_contracts_import_without_initializing_stages(
    statement: str,
) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            f"import sys; {statement}; assert 'landscout.stages' not in sys.modules",
        ],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        check=False,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
