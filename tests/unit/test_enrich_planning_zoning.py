from __future__ import annotations

from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.api.types import is_float_dtype, is_integer_dtype
from pandas.testing import assert_frame_equal
from shapely.geometry import (
    LineString,
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
from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    _stabilize_area_relationships,
    intersect_parcels_with_gpu_zoning,
)
from landscout.stages.planning_overlay import technical_overlay_tolerance

ARCHIVE_SHA256 = "a" * 64
ARCHIVE_NAME = "31395_PLU_20240215"
DOCUMENT_ID = "doc-1"
SOURCE_LAYER = "31395_ZONE_URBA_20240215"
STANDARD_MODEL = "CNIG PLU v2017"
SOURCE_FIELDS = (
    "LIB_IDZONE",
    "LIBELLE",
    "LIBELONG",
    "TYPEZONE",
    "NOMFIC",
    "URLFIC",
    "IDURBA",
    "DATVALID",
)
LOCAL_ENGINEERING_CRS = (
    'ENGCRS["Local",EDATUM["Unknown"],CS[Cartesian,2],'
    'AXIS["x",east,LENGTHUNIT["metre",1]],'
    'AXIS["y",north,LENGTHUNIT["metre",1]]]'
)


def test_shared_overlay_tolerance_preserves_zoning_numerical_behavior() -> None:
    assert technical_overlay_tolerance(100.0) == pytest.approx(1e-6)
    covered, gap, excess = _stabilize_area_relationships(
        100.0, 100.0 + 5e-7, 100.0 + 5e-7
    )
    assert covered == pytest.approx(100.0)
    assert gap == pytest.approx(0.0)
    assert excess == pytest.approx(5e-7)
    with pytest.raises(PlanningZoningError, match="materially exceeds"):
        _stabilize_area_relationships(100.0, 100.0 + 2e-6, 100.0 + 2e-6)


def _rectangle(x_min: float, y_min: float, x_max: float, y_max: float) -> Polygon:
    return Polygon(
        [
            (x_min, y_min),
            (x_min, y_max),
            (x_max, y_max),
            (x_max, y_min),
            (x_min, y_min),
        ]
    )


def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    values = geometries or [_rectangle(0, 0, 10, 10)]
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(len(values))]
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ids,
            "existing_grid_value": [100 + position for position in range(len(values))],
        },
        geometry=values,
        crs="EPSG:2154",
        index=[50 + position for position in range(len(values))],
    )
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    if crs == "EPSG:2154":
        return frame
    return frame.to_crs(crs)


def _zones(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    labels: list[object] | None = None,
    long_labels: list[object] | None = None,
    zone_types: list[object] | None = None,
    document_references: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    values = geometries or [_rectangle(-10, -10, 20, 20)]
    count = len(values)
    source_ids = identifiers or [f"ZONE-{position + 1}" for position in range(count)]
    source_labels = labels or [f"U{position + 1}" for position in range(count)]
    source_long_labels = long_labels or [
        f"Zone urbaine {position + 1}" for position in range(count)
    ]
    source_types = zone_types or ["U"] * count
    source_documents = document_references or [ARCHIVE_NAME] * count
    frame = gpd.GeoDataFrame(
        {
            "LIB_IDZONE": source_ids,
            "LIBELLE": source_labels,
            "LIBELONG": source_long_labels,
            "TYPEZONE": source_types,
            "NOMFIC": [f"reglement-{position + 1}.pdf" for position in range(count)],
            "URLFIC": [
                f"https://www.geoportail-urbanisme.gouv.fr/reglement/{position + 1}"
                for position in range(count)
            ],
            "IDURBA": source_documents,
            "DATVALID": ["2024-02-15"] * count,
        },
        geometry=values,
        crs="EPSG:2154",
        index=[200 + position for position in range(count)],
    )
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    if crs == "EPSG:2154":
        return frame
    if crs == "IGNF:LAMB93":
        return frame.set_crs(crs, allow_override=True)
    if crs == LOCAL_ENGINEERING_CRS:
        return frame.set_crs(crs, allow_override=True)
    return frame.to_crs(crs)


def _planning_document(
    zoning: gpd.GeoDataFrame | None = None,
    *,
    archive_name: str = ARCHIVE_NAME,
    document_id: str = DOCUMENT_ID,
    source_layer: str = SOURCE_LAYER,
) -> GpuPlanningDocument:
    data = zoning if zoning is not None else _zones()
    document = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="GPU",
        commune_code="31395",
        partition="DU_31395",
        document_id=document_id,
        document_family="DU",
        document_type="PLU",
        document_title="Plan local d'urbanisme de Muret",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name=archive_name,
        publication_timestamp="2024-03-26T08:52:34+01:00",
        update_timestamp="2024-03-26T08:52:34+01:00",
        revision_date="2024-02-15",
        producer="Mairie de Muret",
        standard_model=STANDARD_MODEL,
        projection="IGNF:LAMB93",
        metadata_identifier="fr-000031395-plu20240215",
        source_url=(
            "https://www.geoportail-urbanisme.gouv.fr/api/"
            "document/download-by-partition/DU_31395"
        ),
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-08-12T10:00:00+00:00",
        filename=f"{archive_name}.zip",
        archive_format="zip",
        file_size=1234,
        sha256=ARCHIVE_SHA256,
        path=Path("data/cache/gpu/synthetic.zip"),
        cache_hit=True,
    )
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=Path("data/cache/gpu/extracted/synthetic"),
        files=(),
        standard_models=(STANDARD_MODEL,),
        cache_hit=True,
    )
    reference = GpuSpatialLayerReference(
        dataset_path=Path("data/cache/gpu/extracted/synthetic/planning.gpkg"),
        source_layer=source_layer,
        driver="GPKG",
    )
    geometry = data.geometry
    non_null = pd.Series(
        [value is not None for value in geometry], index=geometry.index, dtype=bool
    )
    non_empty = non_null & ~geometry.is_empty
    summary = GpuLayerSummary(
        source_document_id=document_id,
        source_archive_sha256=ARCHIVE_SHA256,
        source_layer=source_layer,
        crs="UNKNOWN" if data.crs is None else data.crs.to_string(),
        feature_count=len(data),
        columns=tuple(str(column) for column in data.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in data.dtypes.items()),
        null_counts=tuple(
            (str(column), int(data[column].isna().sum())) for column in data.columns
        ),
        geometry_types=tuple(
            (str(key), int(value))
            for key, value in geometry[non_null].geom_type.value_counts().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
    inspected = GpuInspectedLayer(
        logical_name="zoning",
        reference=reference,
        data=data,
        summary=summary,
    )
    return GpuPlanningDocument(
        extraction=extraction,
        all_spatial_layers=(reference,),
        zoning=inspected,
        related_layers=(),
    )


def _run(
    parcels: gpd.GeoDataFrame | None = None,
    zones: gpd.GeoDataFrame | None = None,
) -> ParcelZoningResult:
    return intersect_parcels_with_gpu_zoning(
        parcels if parcels is not None else _parcels(),
        _planning_document(zones),
    )


def _row_for_source_zone(result: ParcelZoningResult, source_id: str) -> pd.Series:
    return result.zones.loc[result.zones["source_zone_id"] == source_id].iloc[0]


def test_clean_high_level_api_is_exported() -> None:
    assert stages.intersect_parcels_with_gpu_zoning is intersect_parcels_with_gpu_zoning
    assert "intersect_parcels_with_gpu_zoning" in stages.__all__
    assert not hasattr(stages, "PlanningZoningError")
    assert not hasattr(stages, "ParcelZoningResult")


def test_result_container_is_frozen() -> None:
    result = _run()

    with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()  # type: ignore[misc]


def test_one_parcel_fully_inside_one_zone() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)], identifiers=["P-1"]),
        _zones(
            [_rectangle(0, 0, 10, 10)],
            identifiers=["SOURCE-ZONE"],
            labels=["UAa"],
            long_labels=["Zone urbaine centrale"],
            zone_types=["U"],
        ),
    )

    assert isinstance(result, ParcelZoningResult)
    assert len(result.parcels) == 1
    assert len(result.zones) == 1
    assert len(result.intersections) == 1
    zone = result.zones.iloc[0]
    assert zone["planning_zone_id"] == f"GPU:{DOCUMENT_ID}:ZONE:SOURCE-ZONE"
    assert zone["source_zone_id"] == "SOURCE-ZONE"
    assert zone["zone_label_raw"] == "UAa"
    assert zone["zone_long_label_raw"] == "Zone urbaine centrale"
    assert zone["zone_type_raw"] == "U"
    assert zone["regulation_filename_raw"] == "reglement-1.pdf"
    assert zone["regulation_url_raw"].endswith("/1")
    assert zone["source_document_reference_raw"] == ARCHIVE_NAME
    assert zone["source_validity_date_raw"] == "2024-02-15"
    assert zone["source_provider"] == "Géoportail de l'Urbanisme"
    assert zone["source_portal"] == "GPU"
    assert zone["source_commune_code"] == "31395"
    assert zone["source_document_id"] == DOCUMENT_ID
    assert zone["source_document_type"] == "PLU"
    assert zone["source_archive_name"] == ARCHIVE_NAME
    assert zone["source_archive_sha256"] == ARCHIVE_SHA256
    assert zone["source_layer"] == SOURCE_LAYER
    assert zone["source_standard_model"] == STANDARD_MODEL
    assert zone["zone_area_m2"] == pytest.approx(100.0)
    assert zone.geometry.area == pytest.approx(100.0)
    assert result.zones.crs.to_epsg() == 2154

    relation = result.intersections.iloc[0]
    assert {
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_type_raw",
        "zone_label_raw",
        "zone_long_label_raw",
        "relation_type",
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "source_validity_date_raw",
        "regulation_filename_raw",
    }.issubset(result.intersections.columns)
    assert relation["relation_type"] == "AREA_OVERLAP"
    assert relation["parcel_metric_area_m2"] == pytest.approx(100.0)
    assert relation["zone_area_m2"] == pytest.approx(100.0)
    assert relation["intersection_area_m2"] == pytest.approx(100.0)
    assert relation["parcel_share_pct"] == pytest.approx(100.0)
    assert relation["zone_share_pct"] == pytest.approx(100.0)
    assert relation["source_document_id"] == DOCUMENT_ID
    assert relation["source_archive_sha256"] == ARCHIVE_SHA256
    assert relation["source_layer"] == SOURCE_LAYER
    assert relation["source_validity_date_raw"] == "2024-02-15"
    assert relation["regulation_filename_raw"] == "reglement-1.pdf"

    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 1
    assert parcel["zoning_touch_only_count"] == 0
    assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(100.0)
    assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)
    assert parcel["zoning_gap_area_m2"] == pytest.approx(0.0)
    assert parcel["zoning_overlap_excess_area_m2"] == pytest.approx(0.0)
    assert parcel["dominant_source_zone_id"] == "SOURCE-ZONE"
    assert parcel["dominant_zone_type_raw"] == "U"
    assert parcel["dominant_zone_label_raw"] == "UAa"
    assert parcel["dominant_zone_long_label_raw"] == "Zone urbaine centrale"
    assert parcel["dominant_zone_intersection_area_m2"] == pytest.approx(100.0)
    assert parcel["dominant_zone_share_pct"] == pytest.approx(100.0)
    assert parcel["dominant_zone_tie_count"] == 1
    assert parcel["planning_document_id"] == DOCUMENT_ID
    assert parcel["planning_document_type"] == "PLU"
    assert parcel["planning_archive_name"] == ARCHIVE_NAME
    assert parcel["planning_archive_sha256"] == ARCHIVE_SHA256
    assert parcel["planning_source_layer"] == SOURCE_LAYER
    assert parcel["planning_standard_model"] == STANDARD_MODEL


def test_parcel_split_across_two_zones() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(0, 0, 4, 10), _rectangle(4, 0, 10, 10)],
            identifiers=["LEFT", "RIGHT"],
            labels=["UA", "UB"],
        ),
    )

    assert len(result.intersections) == 2
    assert set(result.intersections["relation_type"]) == {"AREA_OVERLAP"}
    assert sorted(result.intersections["intersection_area_m2"]) == pytest.approx(
        [40.0, 60.0]
    )
    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 2
    assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)
    assert parcel["dominant_source_zone_id"] == "RIGHT"
    assert parcel["dominant_zone_share_pct"] == pytest.approx(60.0)
    assert parcel["dominant_zone_tie_count"] == 1


def test_dominant_zone_tie_is_deterministic() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(5, 0, 10, 10), _rectangle(0, 0, 5, 10)],
            identifiers=["Z-ZONE", "A-ZONE"],
            labels=["UZ", "UA"],
        ),
    )

    parcel = result.parcels.iloc[0]
    assert parcel["dominant_source_zone_id"] == "A-ZONE"
    assert parcel["dominant_planning_zone_id"] == f"GPU:{DOCUMENT_ID}:ZONE:A-ZONE"
    assert parcel["dominant_zone_intersection_area_m2"] == pytest.approx(50.0)
    assert parcel["dominant_zone_share_pct"] == pytest.approx(50.0)
    assert parcel["dominant_zone_tie_count"] == 2


def test_touch_only_relation_is_preserved_but_never_dominant() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(0, 0, 10, 10), _rectangle(10, 0, 20, 10)],
            identifiers=["AREA", "TOUCH"],
        ),
    )

    relations = result.intersections.set_index("source_zone_id")
    assert relations.loc["AREA", "relation_type"] == "AREA_OVERLAP"
    assert relations.loc["TOUCH", "relation_type"] == "TOUCH_ONLY"
    assert relations.loc["TOUCH", "intersection_area_m2"] == pytest.approx(0.0)
    assert relations.loc["TOUCH", "parcel_share_pct"] == pytest.approx(0.0)
    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 1
    assert parcel["zoning_touch_only_count"] == 1
    assert parcel["dominant_source_zone_id"] == "AREA"


def test_parcel_with_no_positive_area_zone_is_preserved() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones([_rectangle(10, 0, 20, 10)], identifiers=["TOUCH"]),
    )

    assert len(result.intersections) == 1
    assert result.intersections.iloc[0]["relation_type"] == "TOUCH_ONLY"
    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 0
    assert parcel["zoning_touch_only_count"] == 1
    assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(0.0)
    assert parcel["zoning_covered_union_area_m2"] == pytest.approx(0.0)
    assert parcel["zoning_coverage_pct"] == pytest.approx(0.0)
    assert parcel["zoning_gap_area_m2"] == pytest.approx(100.0)
    assert pd.isna(parcel["dominant_planning_zone_id"])
    assert pd.isna(parcel["dominant_source_zone_id"])
    assert pd.isna(parcel["dominant_zone_intersection_area_m2"])
    assert pd.isna(parcel["dominant_zone_share_pct"])
    assert pd.isna(parcel["dominant_zone_tie_count"])


def test_parcel_with_no_intersecting_zone_has_zero_coverage() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones([_rectangle(20, 0, 30, 10)]),
    )

    assert result.intersections.empty
    parcel = result.parcels.iloc[0]
    assert parcel["zoning_area_match_count"] == 0
    assert parcel["zoning_touch_only_count"] == 0
    assert parcel["zoning_coverage_pct"] == pytest.approx(0.0)
    assert parcel["zoning_gap_area_m2"] == pytest.approx(100.0)
    assert tuple(result.intersections.columns) == (
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_type_raw",
        "zone_label_raw",
        "zone_long_label_raw",
        "relation_type",
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "source_validity_date_raw",
        "regulation_filename_raw",
    )
    for column in (
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
    ):
        assert is_float_dtype(result.intersections[column])
    assert is_integer_dtype(result.parcels["zoning_area_match_count"])
    assert is_integer_dtype(result.parcels["zoning_touch_only_count"])
    assert str(result.parcels["dominant_zone_tie_count"].dtype) == "Int64"


def test_overlapping_source_zones_expose_raw_sum_union_and_excess() -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones(
            [_rectangle(0, 0, 10, 10), _rectangle(0, 0, 5, 10)],
            identifiers=["WHOLE", "HALF"],
        ),
    )

    parcel = result.parcels.iloc[0]
    assert parcel["zoning_intersection_area_sum_m2"] == pytest.approx(150.0)
    assert parcel["zoning_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["zoning_overlap_excess_area_m2"] == pytest.approx(50.0)
    assert parcel["zoning_coverage_pct"] == pytest.approx(100.0)
    assert parcel["zoning_gap_area_m2"] == pytest.approx(0.0)


@pytest.mark.parametrize(
    "parcel_geometry",
    [
        _rectangle(0, 0, 10, 10),
        MultiPolygon([_rectangle(0, 0, 5, 10), _rectangle(10, 0, 15, 10)]),
    ],
)
def test_polygon_and_multipolygon_parcels_are_supported(
    parcel_geometry: object,
) -> None:
    result = _run(
        _parcels([parcel_geometry]),
        _zones([_rectangle(-5, -5, 20, 15)]),
    )

    assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(100.0)


@pytest.mark.parametrize(
    ("zone_geometry", "expected_area", "expected_coverage"),
    [
        (_rectangle(0, 0, 10, 10), 100.0, 100.0),
        (
            MultiPolygon(
                [_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]
            ),
            80.0,
            80.0,
        ),
    ],
)
def test_polygon_and_multipolygon_zones_are_supported(
    zone_geometry: object,
    expected_area: float,
    expected_coverage: float,
) -> None:
    result = _run(
        _parcels([_rectangle(0, 0, 10, 10)]),
        _zones([zone_geometry]),
    )

    assert result.parcels.iloc[0]["zoning_coverage_pct"] == pytest.approx(
        expected_coverage
    )
    assert result.zones.iloc[0]["zone_area_m2"] == pytest.approx(expected_area)


@pytest.mark.parametrize("parcel_crs", ["EPSG:2154", "EPSG:4326"])
def test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93(
    parcel_crs: str,
) -> None:
    parcels = _parcels([_rectangle(0, 0, 10, 10)], crs=parcel_crs)
    result = _run(parcels, _zones([_rectangle(0, 0, 10, 10)]))

    assert result.parcels.crs == parcels.crs
    assert result.intersections.iloc[0]["parcel_metric_area_m2"] == pytest.approx(
        100.0, abs=1e-5
    )
    assert result.intersections.iloc[0]["intersection_area_m2"] == pytest.approx(
        100.0, abs=1e-5
    )


def test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154() -> None:
    source = _zones([_rectangle(0, 0, 10, 10)], crs="IGNF:LAMB93")
    result = _run(_parcels(), source)

    assert source.crs.to_string() == "IGNF:LAMB93"
    assert result.zones.crs.to_epsg() == 2154
    assert result.zones.iloc[0].geometry.area == pytest.approx(100.0)


@pytest.mark.parametrize(
    ("parcels", "zones", "message"),
    [
        (_parcels(crs=None), _zones(), "CRS"),
        (_parcels(), _zones(crs=None), "CRS"),
        (_parcels(), _zones(crs=LOCAL_ENGINEERING_CRS), "CRS"),
    ],
)
def test_missing_or_unusable_crs_is_rejected(
    parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    message: str,
) -> None:
    with pytest.raises(PlanningZoningError, match=message):
        _run(parcels, zones)


@pytest.mark.parametrize(
    "geometry",
    [
        None,
        Polygon(),
        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),
        Point(0, 0),
        LineString([(0, 0), (10, 10)]),
    ],
)
def test_invalid_or_non_polygonal_parcel_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels([geometry]), _zones())


@pytest.mark.parametrize(
    "geometry",
    [
        None,
        Polygon(),
        Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]),
        Point(0, 0),
        LineString([(0, 0), (10, 10)]),
    ],
)
def test_invalid_or_non_polygonal_zone_geometry_is_rejected(
    geometry: object,
) -> None:
    with pytest.raises(PlanningZoningError, match="geometry|Polygon"):
        _run(_parcels(), _zones([geometry]))


@pytest.mark.parametrize(
    "identifier",
    [None, "", "   ", " PARCEL", "PARCEL ", 123],
)
def test_invalid_parcel_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(_parcels(identifiers=[identifier]), _zones())


def test_duplicate_parcel_id_is_rejected() -> None:
    with pytest.raises(PlanningZoningError, match="parcel_id.*unique|duplicate"):
        _run(
            _parcels(
                [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
                identifiers=["DUPLICATE", "DUPLICATE"],
            ),
            _zones(),
        )


def test_missing_parcel_id_is_rejected() -> None:
    parcels = _parcels().drop(columns=["parcel_id"])

    with pytest.raises(PlanningZoningError, match="parcel_id"):
        _run(parcels, _zones())


def test_geometry_must_be_the_active_parcel_geometry_column() -> None:
    parcels = _parcels().rename_geometry("shape")
    parcels["geometry"] = parcels["shape"]

    with pytest.raises(PlanningZoningError, match="active"):
        _run(parcels, _zones())


@pytest.mark.parametrize(
    "identifier",
    [None, "", "   ", " ZONE", "ZONE ", 123],
)
def test_invalid_source_zone_id_is_rejected(identifier: object) -> None:
    with pytest.raises(PlanningZoningError, match="LIB_IDZONE|zone"):
        _run(_parcels(), _zones(identifiers=[identifier]))


def test_duplicate_source_zone_id_is_rejected() -> None:
    with pytest.raises(PlanningZoningError, match="LIB_IDZONE.*unique|duplicate"):
        _run(
            _parcels(),
            _zones(
                [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
                identifiers=["DUPLICATE", "DUPLICATE"],
            ),
        )


def test_zoning_document_reference_must_match_loaded_archive() -> None:
    zones = _zones(document_references=["31395_PLU_WRONG"])

    with pytest.raises(PlanningZoningError, match="IDURBA|document"):
        _run(_parcels(), zones)


@pytest.mark.parametrize(
    ("summary_field", "bad_value", "message"),
    [
        ("source_document_id", "different-document", "document lineage"),
        ("source_archive_sha256", "b" * 64, "archive lineage"),
        ("source_layer", "different_layer", "source layer"),
        ("feature_count", 999, "feature count"),
    ],
)
def test_zoning_summary_lineage_and_count_must_match_bundle(
    summary_field: str,
    bad_value: object,
    message: str,
) -> None:
    document = _planning_document()
    summary = replace(document.zoning.summary, **{summary_field: bad_value})
    zoning = replace(document.zoning, summary=summary)
    corrupted = replace(document, zoning=zoning)

    with pytest.raises(PlanningZoningError, match=message):
        intersect_parcels_with_gpu_zoning(_parcels(), corrupted)


@pytest.mark.parametrize(
    "reserved_column",
    [
        "zoning_coverage_pct",
        "dominant_zone_label_raw",
        "planning_document_id",
    ],
)
def test_existing_parcel_output_field_collision_is_rejected(
    reserved_column: str,
) -> None:
    parcels = _parcels()
    parcels[reserved_column] = "pre-existing-value"

    with pytest.raises(PlanningZoningError, match="column|output|reserved|collision"):
        _run(parcels, _zones())


@pytest.mark.parametrize("field", SOURCE_FIELDS)
def test_every_source_zoning_field_is_required(field: str) -> None:
    zones = _zones().drop(columns=[field])

    with pytest.raises(PlanningZoningError, match=field):
        _run(_parcels(), zones)


def test_input_frames_are_not_mutated() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        identifiers=["P-2", "P-1"],
        crs="EPSG:4326",
    )
    zones = _zones(
        [_rectangle(0, 0, 15, 15), _rectangle(20, 0, 35, 15)],
        identifiers=["U-1", "N-1"],
        labels=["UA", "N"],
        zone_types=["U", "N"],
    )
    planning_document = _planning_document(zones)
    parcels_before = deepcopy(parcels)
    zones_before = deepcopy(planning_document.zoning.data)

    intersect_parcels_with_gpu_zoning(parcels, planning_document)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(planning_document.zoning.data, zones_before)


def test_parcel_count_order_geometry_crs_and_existing_columns_are_preserved() -> None:
    parcels = _parcels(
        [_rectangle(20, 0, 30, 10), _rectangle(0, 0, 10, 10)],
        identifiers=["P-2", "P-1"],
        crs="EPSG:4326",
    )
    result = _run(
        parcels,
        _zones(
            [_rectangle(-5, -5, 15, 15), _rectangle(15, -5, 35, 15)],
            identifiers=["LEFT", "RIGHT"],
        ),
    )

    assert len(result.parcels) == len(parcels)
    assert result.parcels["parcel_id"].tolist() == parcels["parcel_id"].tolist()
    assert result.parcels["existing_grid_value"].tolist() == parcels[
        "existing_grid_value"
    ].tolist()
    assert result.parcels.crs == parcels.crs
    assert result.parcels.geometry.reset_index(drop=True).equals(
        parcels.geometry.reset_index(drop=True)
    )
    assert not result.parcels["parcel_id"].duplicated().any()
    assert set(result.intersections["parcel_id"]).issubset(set(parcels["parcel_id"]))
    assert not result.intersections.duplicated(
        subset=["parcel_id", "planning_zone_id"]
    ).any()


def test_raw_zoning_values_are_preserved_exactly() -> None:
    zones = _zones(
        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
        identifiers=["ID-É", "id-lower"],
        labels=["AUf", "Nh"],
        long_labels=["Libellé Étendu", None],
        zone_types=["AUc", "N"],
    )
    zones.loc[zones.index[1], "NOMFIC"] = None
    zones.loc[zones.index[1], "URLFIC"] = None
    result = _run(_parcels(), zones)

    first = _row_for_source_zone(result, "ID-É")
    second = _row_for_source_zone(result, "id-lower")
    assert first["source_zone_id"] == "ID-É"
    assert first["zone_label_raw"] == "AUf"
    assert first["zone_long_label_raw"] == "Libellé Étendu"
    assert first["zone_type_raw"] == "AUc"
    assert second["source_zone_id"] == "id-lower"
    assert second["zone_label_raw"] == "Nh"
    assert pd.isna(second["zone_long_label_raw"])
    assert second["zone_type_raw"] == "N"
    assert pd.isna(second["regulation_filename_raw"])
    assert pd.isna(second["regulation_url_raw"])


def test_intersection_table_references_only_known_parcels_and_zones() -> None:
    result = _run(
        _parcels(
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            identifiers=["P-1", "P-2"],
        ),
        _zones(
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            identifiers=["Z-1", "Z-2"],
        ),
    )

    assert set(result.intersections["parcel_id"]) == {"P-1", "P-2"}
    assert set(result.intersections["planning_zone_id"]) == set(
        result.zones["planning_zone_id"]
    )
    assert not result.intersections.duplicated(
        subset=["parcel_id", "planning_zone_id"]
    ).any()
    numeric = result.intersections[
        [
            "parcel_metric_area_m2",
            "zone_area_m2",
            "intersection_area_m2",
            "parcel_share_pct",
            "zone_share_pct",
        ]
    ]
    assert numeric.notna().all().all()
    assert (numeric >= 0).all().all()


def test_result_frames_are_independent_from_inputs() -> None:
    parcels = _parcels()
    zones = _zones()
    result = _run(parcels, zones)
    parcel_snapshot = result.parcels.copy(deep=True)
    zone_snapshot = result.zones.copy(deep=True)
    intersections_snapshot = result.intersections.copy(deep=True)

    parcels.loc[parcels.index[0], "existing_grid_value"] = -1
    zones.loc[zones.index[0], "LIBELLE"] = "CHANGED"

    assert_frame_equal(result.parcels, parcel_snapshot)
    assert_frame_equal(result.zones, zone_snapshot)
    assert_frame_equal(result.intersections, intersections_snapshot)
