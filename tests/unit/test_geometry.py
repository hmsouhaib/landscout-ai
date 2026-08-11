import pytest
from shapely.geometry import MultiPolygon, Polygon

from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    InvalidGeometryError,
    MetricCrsError,
    area_m2,
    centroid,
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
