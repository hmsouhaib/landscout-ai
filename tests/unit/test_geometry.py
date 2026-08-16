import pytest
from shapely.affinity import rotate
from shapely.geometry import MultiPolygon, Point, Polygon

from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)


@pytest.fixture
def square() -> Polygon:
    return Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])


def test_valid_polygon_in_lambert93(square: Polygon) -> None:
    assert area_m2(square, LAMBERT93) > 0


def test_area_in_square_metres(square: Polygon) -> None:
    assert area_m2(square, LAMBERT93) == pytest.approx(100.0)


def test_perimeter_in_metres(square: Polygon) -> None:
    assert perimeter_m(square, LAMBERT93) == pytest.approx(40.0)


def test_centroid(square: Polygon) -> None:
    center = centroid(square)

    assert center.x == pytest.approx(5.0)
    assert center.y == pytest.approx(5.0)


@pytest.mark.parametrize("metric_function", [area_m2, perimeter_m])
def test_metric_calculation_in_wgs84_fails(
    square: Polygon, metric_function: object
) -> None:
    with pytest.raises(MetricCrsError):
        metric_function(square, WGS84)  # type: ignore[operator]


def test_empty_geometry_fails() -> None:
    with pytest.raises(EmptyGeometryError):
        area_m2(Polygon(), LAMBERT93)


def test_invalid_geometry_fails() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    assert not bow_tie.is_valid
    with pytest.raises(InvalidGeometryError):
        area_m2(bow_tie, LAMBERT93)


def test_multipolygon() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
    geometry = MultiPolygon([first, second])

    assert area_m2(geometry, LAMBERT93) == pytest.approx(200.0)
    assert perimeter_m(geometry, LAMBERT93) == pytest.approx(80.0)


def test_square_shape_metrics(square: Polygon) -> None:
    assert approximate_length_m(square, LAMBERT93) == pytest.approx(10.0)
    assert approximate_width_m(square, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(square, LAMBERT93) == pytest.approx(1.0)
    assert compactness_score(square, LAMBERT93) == pytest.approx(0.785398)


def test_simple_rectangle_shape_metrics() -> None:
    rectangle = Polygon([(0, 0), (20, 0), (20, 10), (0, 10)])

    assert approximate_length_m(rectangle, LAMBERT93) == pytest.approx(20.0)
    assert approximate_width_m(rectangle, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(rectangle, LAMBERT93) == pytest.approx(2.0)


def test_rotated_rectangle_is_orientation_independent() -> None:
    rectangle = Polygon([(0, 0), (30, 0), (30, 10), (0, 10)])
    rotated = rotate(rectangle, 37)

    assert approximate_length_m(rotated, LAMBERT93) == pytest.approx(30.0)
    assert approximate_width_m(rotated, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(rotated, LAMBERT93) == pytest.approx(3.0)


def test_elongated_rectangle_is_less_compact_than_square(square: Polygon) -> None:
    elongated = Polygon([(0, 0), (100, 0), (100, 2), (0, 2)])

    assert length_width_ratio(elongated, LAMBERT93) == pytest.approx(50.0)
    assert compactness_score(square, LAMBERT93) > compactness_score(
        elongated, LAMBERT93
    )


def test_multipolygon_shape_metrics() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
    geometry = MultiPolygon([first, second])

    assert approximate_length_m(geometry, LAMBERT93) == pytest.approx(30.0)
    assert approximate_width_m(geometry, LAMBERT93) == pytest.approx(10.0)
    assert 0 < compactness_score(geometry, LAMBERT93) <= 1


def test_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
    with pytest.raises(MetricCrsError):
        approximate_length_m(square, WGS84)
    with pytest.raises(MetricCrsError):
        approximate_width_m(square, WGS84)
    with pytest.raises(MetricCrsError):
        length_width_ratio(square, WGS84)
    with pytest.raises(MetricCrsError):
        compactness_score(square, WGS84)


def test_shape_metrics_reject_invalid_geometry() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    with pytest.raises(InvalidGeometryError):
        approximate_length_m(bow_tie, LAMBERT93)


def test_shape_metrics_reject_empty_geometry() -> None:
    with pytest.raises(EmptyGeometryError):
        compactness_score(Polygon(), LAMBERT93)


def test_zero_area_geometry_raises_controlled_error() -> None:
    zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])

    with pytest.raises(GeometryError):
        length_width_ratio(zero_area, LAMBERT93)


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),
        Polygon([(0, 0), (40, 0), (40, 5), (0, 5)]),
        rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 23),
    ],
)
def test_length_is_always_at_least_width(geometry: Polygon) -> None:
    assert approximate_length_m(geometry, LAMBERT93) >= approximate_width_m(
        geometry, LAMBERT93
    )


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),
        Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]),
    ],
)
def test_compactness_range(geometry: Polygon) -> None:
    assert 0 < compactness_score(geometry, LAMBERT93) <= 1


@pytest.mark.parametrize(
    ("geometry", "expected_length", "expected_width"),
    [
        (Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]), 10.0, 10.0),
        (Polygon([(0, 0), (20, 0), (20, 10), (0, 10)]), 20.0, 10.0),
        (
            rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 37),
            30.0,
            10.0,
        ),
        (Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]), 100.0, 2.0),
    ],
)
def test_centralized_shape_metrics(
    geometry: Polygon, expected_length: float, expected_width: float
) -> None:
    metrics = parcel_shape_metrics_m(geometry, LAMBERT93)

    assert metrics.length_m == pytest.approx(expected_length)
    assert metrics.width_m == pytest.approx(expected_width)
    assert metrics.length_m >= metrics.width_m
    assert metrics.length_width_ratio == pytest.approx(expected_length / expected_width)
    assert 0 < metrics.compactness <= 1


def test_centralized_shape_metrics_support_multipolygon() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])

    metrics = parcel_shape_metrics_m(MultiPolygon([first, second]), LAMBERT93)

    assert metrics.length_m == pytest.approx(30.0)
    assert metrics.width_m == pytest.approx(10.0)


def test_centralized_shape_metrics_reject_invalid_geometry() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    with pytest.raises(InvalidGeometryError):
        parcel_shape_metrics_m(bow_tie, LAMBERT93)


def test_centralized_shape_metrics_reject_zero_area_geometry() -> None:
    zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])

    with pytest.raises(GeometryError):
        parcel_shape_metrics_m(zero_area, LAMBERT93)


def test_centralized_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
    with pytest.raises(MetricCrsError):
        parcel_shape_metrics_m(square, WGS84)


@pytest.mark.parametrize("geometry", [None, "polygon", 123, [], object()])
def test_non_geometry_inputs_raise_controlled_error(geometry: object) -> None:
    with pytest.raises(UnsupportedGeometryError):
        area_m2(geometry, LAMBERT93)  # type: ignore[arg-type]


def test_unsupported_geometry_family_raises_controlled_error() -> None:
    with pytest.raises(UnsupportedGeometryError):
        area_m2(Point(0, 0), LAMBERT93)


def test_three_dimensional_parcel_is_rejected() -> None:
    polygon_z = Polygon([(0, 0, 1), (10, 0, 1), (10, 10, 1), (0, 10, 1)])

    with pytest.raises(UnsupportedGeometryError, match="two-dimensional"):
        area_m2(polygon_z, LAMBERT93)


@pytest.mark.parametrize("crs", [None, object(), [], "not-a-crs"])
def test_malformed_crs_inputs_raise_controlled_error(
    square: Polygon,
    crs: object,
) -> None:
    with pytest.raises(MetricCrsError):
        area_m2(square, crs)  # type: ignore[arg-type]
