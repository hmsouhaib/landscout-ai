import pytest
from shapely.geometry import Polygon

from landscout.geo import LAMBERT93, WGS84, MetricCrsError, centroid_to_latlon
from landscout.geo.geometry import reproject_to_lambert93


def test_crs_constants() -> None:
    assert WGS84.to_epsg() == 4326
    assert LAMBERT93.to_epsg() == 2154


def test_reproject_to_lambert93_and_back_to_latlon() -> None:
    polygon = Polygon([(2.0, 48.0), (2.01, 48.0), (2.01, 48.01), (2.0, 48.01)])

    projected = reproject_to_lambert93(polygon, WGS84)
    latitude, longitude = centroid_to_latlon(projected, LAMBERT93)

    assert latitude == pytest.approx(48.005, abs=0.001)
    assert longitude == pytest.approx(2.005, abs=0.001)


@pytest.mark.parametrize("crs", [None, object(), [], "invalid-crs"])
def test_reprojection_rejects_malformed_crs_with_controlled_error(
    crs: object,
) -> None:
    polygon = Polygon([(2, 48), (2.01, 48), (2.01, 48.01), (2, 48.01)])

    with pytest.raises(MetricCrsError):
        reproject_to_lambert93(polygon, crs)  # type: ignore[arg-type]
