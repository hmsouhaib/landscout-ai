import geopandas as gpd
import pandas as pd
import pytest
from shapely.geometry import Point

from landscout.stages.profile_shape import (
    ShapeProfileError,
    profile_shape_distribution,
)


@pytest.fixture
def parcels() -> gpd.GeoDataFrame:
    count = 10
    return gpd.GeoDataFrame(
        {
            "parcel_id": [f"parcel-{index}" for index in range(count)],
            "shape_status": ["VALID"] * count,
            "area_m2": [100.0 * (index + 1) for index in range(count)],
            "length_m": [10.0 * (index + 1) for index in range(count)],
            "width_m": [4.0, 7.0, 12.0, 17.0, 22.0, 27.0, 35.0, 45.0, 55.0, 60.0],
            "length_width_ratio": [1.0, 2.5, 3.5, 4.5, 6.0, 8.0, 12.0, 20.0, 30.0, 5.0],
            "compactness": [0.02, 0.07, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85],
            "centroid_lat": [43.0 + index / 100 for index in range(count)],
            "centroid_lon": [2.0 + index / 100 for index in range(count)],
        },
        geometry=[Point(2.0 + index / 100, 43.0) for index in range(count)],
        crs="EPSG:4326",
    )


def test_percentile_calculation(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    area = profile.distributions["area_m2"]
    assert area["min"] == pytest.approx(100.0)
    assert area["p50"] == pytest.approx(550.0)
    assert area["max"] == pytest.approx(1000.0)
    assert set(area) == {
        "min",
        "p01",
        "p05",
        "p10",
        "p25",
        "p50",
        "p75",
        "p90",
        "p95",
        "p99",
        "max",
    }


def test_bucket_counts_sum_to_input_count(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert sum(profile.width_buckets.values()) == len(parcels)
    assert sum(profile.ratio_buckets.values()) == len(parcels)
    assert sum(profile.compactness_buckets.values()) == len(parcels)


def test_diagnostic_scenario_counts(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert profile.scenarios["A"].retained_count == 8
    assert profile.scenarios["B"].retained_count == 7
    assert profile.scenarios["C"].retained_count == 6
    assert profile.scenarios["D"].retained_count == 4
    assert profile.scenarios["E"].retained_count == 2
    assert profile.scenarios["F"].retained_count == 1


def test_input_is_not_mutated(parcels: gpd.GeoDataFrame) -> None:
    original = parcels.copy(deep=True)

    profile_shape_distribution(parcels)

    pd.testing.assert_frame_equal(parcels, original)


def test_missing_metric_fails(parcels: gpd.GeoDataFrame) -> None:
    without_width = parcels.drop(columns=["width_m"])

    with pytest.raises(ShapeProfileError, match="width_m"):
        profile_shape_distribution(without_width)


def test_null_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
    with_null = parcels.copy()
    with_null.loc[0, "parcel_id"] = None

    with pytest.raises(ShapeProfileError, match="null"):
        profile_shape_distribution(with_null)


def test_duplicate_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
    with_duplicate = parcels.copy()
    with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]

    with pytest.raises(ShapeProfileError, match="unique"):
        profile_shape_distribution(with_duplicate)


def test_missing_crs_fails(parcels: gpd.GeoDataFrame) -> None:
    without_crs = parcels.set_crs(None, allow_override=True)

    with pytest.raises(ShapeProfileError, match="CRS"):
        profile_shape_distribution(without_crs)


def test_null_metric_on_valid_shape_fails(parcels: gpd.GeoDataFrame) -> None:
    with_null_metric = parcels.copy()
    with_null_metric.loc[0, "compactness"] = None

    with pytest.raises(ShapeProfileError, match="complete"):
        profile_shape_distribution(with_null_metric)
