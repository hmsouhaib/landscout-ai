import geopandas as gpd
import pytest
from shapely.affinity import rotate
from shapely.geometry import Point, Polygon
from shapely.geometry.base import BaseGeometry

from landscout.geo import LAMBERT93, parcel_shape_metrics_m
from landscout.stages.enrich_shape import (
    DERIVED_METRIC_COLUMNS,
    ShapeEnrichmentError,
    enrich_parcel_shapes,
)


def _candidate_frame(geometries: list[BaseGeometry]) -> gpd.GeoDataFrame:
    projected = gpd.GeoSeries(geometries, crs="EPSG:2154")
    wgs84 = projected.to_crs("EPSG:4326")
    return gpd.GeoDataFrame(
        {
            "parcel_id": [f"parcel-{index}" for index in range(len(geometries))],
            "geometry_status": ["VALID"] * len(geometries),
            "area_m2": list(projected.area),
        },
        geometry=wgs84,
        crs="EPSG:4326",
    )


@pytest.fixture
def square() -> Polygon:
    return Polygon(
        [(600000, 6200000), (600010, 6200000), (600010, 6200010), (600000, 6200010)]
    )


def test_square_metrics(square: Polygon) -> None:
    enriched = enrich_parcel_shapes(_candidate_frame([square]))
    row = enriched.iloc[0]

    assert row["shape_status"] == "VALID"
    assert row["length_m"] == pytest.approx(10.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(1.0, abs=0.001)
    assert row["compactness"] == pytest.approx(0.785398)


def test_rectangle_metrics() -> None:
    rectangle = Polygon(
        [(600000, 6200000), (600020, 6200000), (600020, 6200010), (600000, 6200010)]
    )
    row = enrich_parcel_shapes(_candidate_frame([rectangle])).iloc[0]

    assert row["length_m"] == pytest.approx(20.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(2.0, abs=0.001)


def test_rotated_rectangle_metrics() -> None:
    rectangle = Polygon(
        [(600000, 6200000), (600030, 6200000), (600030, 6200010), (600000, 6200010)]
    )
    rotated = rotate(rectangle, 37)
    row = enrich_parcel_shapes(_candidate_frame([rotated])).iloc[0]

    assert row["length_m"] == pytest.approx(30.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(3.0, abs=0.001)


def test_elongated_parcel() -> None:
    elongated = Polygon(
        [(600000, 6200000), (600100, 6200000), (600100, 6200002), (600000, 6200002)]
    )
    row = enrich_parcel_shapes(_candidate_frame([elongated])).iloc[0]

    assert row["length_width_ratio"] == pytest.approx(50.0, abs=0.01)
    assert row["length_m"] >= row["width_m"]
    assert 0 <= row["compactness"] <= 1


def test_centroid_coordinates(square: Polygon) -> None:
    expected = gpd.GeoSeries([square.centroid], crs="EPSG:2154").to_crs("EPSG:4326").iloc[0]

    row = enrich_parcel_shapes(_candidate_frame([square])).iloc[0]

    assert row["centroid_lat"] == pytest.approx(expected.y)
    assert row["centroid_lon"] == pytest.approx(expected.x)


def test_output_geometry_remains_wgs84(square: Polygon) -> None:
    source = _candidate_frame([square])

    enriched = enrich_parcel_shapes(source)

    assert enriched.crs is not None
    assert enriched.crs.to_epsg() == 4326
    assert enriched.geometry.iloc[0].equals_exact(source.geometry.iloc[0], tolerance=0)


def test_missing_crs_fails(square: Polygon) -> None:
    source = _candidate_frame([square]).set_crs(None, allow_override=True)

    with pytest.raises(ShapeEnrichmentError, match="CRS"):
        enrich_parcel_shapes(source)


def test_missing_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square]).drop(columns=["parcel_id"])

    with pytest.raises(ShapeEnrichmentError, match="parcel_id"):
        enrich_parcel_shapes(source)


def test_null_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square])
    source.loc[0, "parcel_id"] = None

    with pytest.raises(ShapeEnrichmentError, match="null"):
        enrich_parcel_shapes(source)


def test_duplicate_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square, square])
    source.loc[1, "parcel_id"] = source.loc[0, "parcel_id"]

    with pytest.raises(ShapeEnrichmentError, match="unique"):
        enrich_parcel_shapes(source)


@pytest.mark.parametrize("parcel_id", [1, "", " parcel", "parcel "])
def test_enrichment_requires_exact_non_empty_parcel_ids(
    square: Polygon,
    parcel_id: object,
) -> None:
    source = _candidate_frame([square])
    source["parcel_id"] = source["parcel_id"].astype(object)
    source.loc[0, "parcel_id"] = parcel_id

    with pytest.raises(ShapeEnrichmentError, match="exact non-empty strings"):
        enrich_parcel_shapes(source)


@pytest.mark.parametrize("area", [-1, 0, float("inf"), float("nan"), "100", True])
def test_valid_candidate_area_requires_strict_positive_finite_number(
    square: Polygon,
    area: object,
) -> None:
    source = _candidate_frame([square])
    source["area_m2"] = source["area_m2"].astype(object)
    source.loc[0, "area_m2"] = area

    with pytest.raises(ShapeEnrichmentError, match="strict positive finite numeric"):
        enrich_parcel_shapes(source)


def test_failed_geometry_does_not_remove_other_rows(square: Polygon) -> None:
    source = _candidate_frame([square, Point(600000, 6200000)])
    source.loc[1, "geometry_status"] = "INVALID"

    enriched = enrich_parcel_shapes(source)

    assert list(enriched["shape_status"]) == ["VALID", "ERROR"]
    assert enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all()


def test_exact_parcel_ids_are_preserved(square: Polygon) -> None:
    source = _candidate_frame([square, Point(600000, 6200000)])
    source.loc[1, "geometry_status"] = "INVALID"

    enriched = enrich_parcel_shapes(source)

    assert len(enriched) == len(source)
    assert set(enriched["parcel_id"]) == set(source["parcel_id"])


def test_enrichment_matches_centralized_shape_metrics(square: Polygon) -> None:
    source = _candidate_frame([square])
    expected_geometry = source.to_crs(LAMBERT93).geometry.iloc[0]
    expected = parcel_shape_metrics_m(expected_geometry, LAMBERT93)

    row = enrich_parcel_shapes(source).iloc[0]

    assert row["length_m"] == pytest.approx(expected.length_m)
    assert row["width_m"] == pytest.approx(expected.width_m)
    assert row["length_width_ratio"] == pytest.approx(expected.length_width_ratio)
    assert row["compactness"] == pytest.approx(expected.compactness)
