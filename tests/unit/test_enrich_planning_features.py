from __future__ import annotations

from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
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
from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)
from landscout.stages import enrich_planning_features as planning_features_module
from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
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
        "NOMFIC": [None if index % 2 else f"rule-{index}.pdf" for index in range(count)],
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


def _planning_document(
    layers: list[GpuInspectedLayer] | None = None,
) -> GpuPlanningDocument:
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="GPU",
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
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=Path("synthetic"),
        files=(),
        standard_models=(STANDARD,),
        cache_hit=True,
    )
    zoning_frame = gpd.GeoDataFrame(
        {"zone": ["Z"]}, geometry=[_rectangle(-10, -10, 20, 20)], crs="EPSG:2154"
    )
    zoning_ref = GpuSpatialLayerReference(Path("zoning.gpkg"), "ZONING", "GPKG")
    zoning = GpuInspectedLayer(
        logical_name="zoning",
        reference=zoning_ref,
        data=zoning_frame,
        summary=_summary(zoning_frame, "ZONING"),
    )
    related = tuple(layers or [])
    return GpuPlanningDocument(
        extraction=extraction,
        all_spatial_layers=(zoning_ref, *(layer.reference for layer in related)),
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
    assert not hasattr(stages, "PlanningFeaturesError")
    assert not hasattr(stages, "ParcelPlanningFeaturesResult")


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
    assert feature["source_crs"] == "IGNF:LAMB93"
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
        [_inspected("information_surface", _source_frame("information_surface", [geometry]))]
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
        [_inspected("prescription_line", _source_frame("prescription_line", [geometry]))]
    )
    assert result.relations.iloc[0]["intersection_length_m"] > 0


def test_points_inside_boundary_outside_and_multipoint() -> None:
    frame = _source_frame(
        "prescription_point",
        [Point(5, 5), Point(10, 5), Point(20, 20), MultiPoint([(3, 3), (10, 4), (30, 30)])],
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
    frame = _source_frame(
        "prescription_line", [LineString([(0, 5), (10, 5)])]
    ).drop(columns=["LIBELLE", "TXT", "NOMFIC", "URLFIC", "DATVALID"])
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
        [_inspected("prescription_surface", _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]))],
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
        _run([], _parcels([_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)], ids=["P", "P"]))


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
    frame = _source_frame(
        "prescription_surface", [_rectangle(0, 0, 10, 10)]
    ).drop(columns="LIB_IDPSC")
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


def test_idurba_mismatch_is_rejected() -> None:
    frame = _source_frame(
        "prescription_line", [LineString([(0, 5), (10, 5)])], document_refs=["OTHER"]
    )
    with pytest.raises(PlanningFeaturesError, match="IDURBA"):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize("missing", ["TYPEPSC", "STYPEPSC", "IDURBA", "LIB_IDPSC"])
def test_missing_required_source_fields_fail(missing: str) -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(columns=missing)
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
        _run([_inspected("information_surface", _source_frame("information_surface", [bowtie]))])


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
        "prescription_line", [LineString([(0, 5), (10, 5)])], crs=None if target == "source" else "EPSG:2154"
    )
    with pytest.raises(PlanningFeaturesError, match="CRS"):
        _run([_inspected("prescription_line", frame)], parcel)


def test_unusable_source_crs_is_rejected() -> None:
    frame = _source_frame(
        "prescription_line", [LineString([(0, 5), (10, 5)])]
    ).set_crs(LOCAL_ENGINEERING_CRS, allow_override=True)
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
    corrupted = replace(layer, summary=replace(layer.summary, **{field: value}))
    with pytest.raises(PlanningFeaturesError, match="summary"):
        _run([corrupted])


@pytest.mark.parametrize("bad_count", [True, -1, 1.5, float("inf"), "1"])
def test_source_summary_counts_are_strict_integers(bad_count: object) -> None:
    layer = _inspected(
        "prescription_line",
        _source_frame(
            "prescription_line", [LineString([(0, 5), (10, 5)])]
        ),
    )
    corrupted = replace(layer, summary=replace(layer.summary, feature_count=bad_count))
    with pytest.raises(PlanningFeaturesError, match="integer count|non-negative"):
        _run([corrupted])


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
    assert result.parcels["existing_zoning_fact"].equals(parcels["existing_zoning_fact"])
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
        ((result.relations["parcel_id"] == "P-B") & (result.relations["geometry_kind"] == "SURFACE")).sum()
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
        "prescription_line", _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])])
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
    if logical == "prescription_surface":
        frame = frame.drop(columns="LIB_IDPSC")

        def unexpected_fid_read(*args: object, **kwargs: object) -> object:
            raise AssertionError("zero-row layers must not reopen OGR source FIDs")

        monkeypatch.setattr(
            planning_features_module.pyogrio,
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


def _contract_result() -> tuple[gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
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
            _source_frame(
                "prescription_point", [Point(5, 5)], ids=["POINT"]
            ),
        ),
    ]
    return parcels, _run(layers, parcels)


def test_public_normalized_input_contract_validates_step_7d_3_1_result() -> None:
    _, result = _contract_result()
    validate_normalized_planning_feature_inputs(
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    )


def test_public_normalized_input_contract_is_exported() -> None:
    from landscout import stages

    assert (
        stages.validate_normalized_planning_feature_inputs
        is validate_normalized_planning_feature_inputs
    )
    assert "validate_normalized_planning_feature_inputs" in stages.__all__


def test_public_normalized_input_contract_rejects_stripped_catalog() -> None:
    _, result = _contract_result()
    surface = result.surface_features.drop(columns="label_raw")
    with pytest.raises(PlanningFeaturesError, match="schema|label_raw"):
        validate_normalized_planning_feature_inputs(
            surface,
            result.line_features,
            result.point_features,
            result.relations,
        )


def test_empty_and_nonempty_catalogs_have_identical_kind_schemas() -> None:
    _, populated = _contract_result()
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
    source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    relations["point_member_count"] = relations["point_member_count"].astype(object)
    point_index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[point_index, "point_member_count"] = bad_count
    with pytest.raises(PlanningFeaturesError, match="integer count|non-negative"):
        _validate_result(source, replace(result, relations=relations))


@pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])
def test_strict_parcel_summary_integer_counts_are_enforced(
    bad_count: object,
) -> None:
    source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels["planning_line_relation_count"] = parcels[
        "planning_line_relation_count"
    ].astype(object)
    parcels.loc[parcels.index[0], "planning_line_relation_count"] = bad_count
    with pytest.raises(PlanningFeaturesError, match="integer count|non-negative"):
        _validate_result(source, replace(result, parcels=parcels))


@pytest.mark.parametrize(
    ("kind", "column", "value"),
    [
        ("SURFACE", "relation_type", "TOUCH_ONLY"),
        ("SURFACE", "parcel_share_pct", 42.0),
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
    source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == kind][0]
    relations[column] = relations[column].astype(object)
    relations.loc[index, column] = value
    with pytest.raises(PlanningFeaturesError):
        _validate_result(source, replace(result, relations=relations))


def test_point_member_relation_semantics_are_exact() -> None:
    source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[index, "point_members_inside_count"] = 0
    relations.loc[index, "point_members_boundary_count"] = 1
    with pytest.raises(PlanningFeaturesError, match="relation type"):
        _validate_result(source, replace(result, relations=relations))


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "NOT_A_KIND"),
        ("source_identity_field", "WRONG_FIELD"),
        ("type_code_raw", "MUTATED"),
        ("source_archive_sha256", "b" * 64),
    ],
)
def test_relation_must_match_feature_catalog(
    column: str,
    value: object,
) -> None:
    source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], column] = value
    with pytest.raises(PlanningFeaturesError, match="catalog"):
        _validate_result(source, replace(result, relations=relations))


def test_feature_ids_are_globally_unique_across_catalogs() -> None:
    source, result = _contract_result()
    points = result.point_features.copy(deep=True)
    points.loc[points.index[0], "planning_feature_id"] = result.surface_features.iloc[0][
        "planning_feature_id"
    ]
    with pytest.raises(PlanningFeaturesError, match="globally unique"):
        _validate_result(source, replace(result, point_features=points))


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
    source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "planning_surface_relation_count"] += 1
    with pytest.raises(PlanningFeaturesError, match="inconsistent with relations"):
        _validate_result(source, replace(result, parcels=parcels))


def test_corrupted_surface_union_contract_is_rejected() -> None:
    source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[
        parcels.index[0], "planning_surface_covered_union_area_m2"
    ] = 1000.0
    with pytest.raises(PlanningFeaturesError, match="union"):
        _validate_result(source, replace(result, parcels=parcels))


def test_geospatial_operation_failure_is_controlled_and_chained(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_join(*args: object, **kwargs: object) -> object:
        raise RuntimeError("synthetic spatial-index failure")

    monkeypatch.setattr(planning_features_module.gpd, "sjoin", fail_join)
    layer = _inspected(
        "prescription_line",
        _source_frame(
            "prescription_line", [LineString([(0, 5), (10, 5)])]
        ),
    )
    with pytest.raises(PlanningFeaturesError, match="spatial join") as caught:
        _run([layer])
    assert isinstance(caught.value.__cause__, RuntimeError)
