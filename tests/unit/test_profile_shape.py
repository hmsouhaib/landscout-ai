import geopandas as gpd
import pandas as pd
import pytest
from shapely.geometry import Point

from landscout.stages.profile_shape import (
    PROFILE_METRICS,
    ShapeProfileError,
    profile_shape_distribution,
)


def _with_error_row(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    mixed = parcels.copy()
    mixed.loc[9, "shape_status"] = "ERROR"
    for column in (*PROFILE_METRICS, "centroid_lat", "centroid_lon"):
        mixed.loc[9, column] = None
    return mixed


@pytest.fixture
def parcels() -> gpd.GeoDataFrame:
    count = 10
    return gpd.GeoDataFrame(
        {
            "parcel_id": [f"parcel-{index}" for index in range(count)],
            "shape_status": ["VALID"] * count,
            "area_m2": [100.0 * (index + 1) for index in range(count)],
            "length_m": [4.0, 17.5, 42.0, 76.5, 132.0, 216.0, 420.0, 900.0, 1650.0, 300.0],
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


def test_existing_all_valid_behavior_is_unchanged(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert profile.input_count == 10
    assert profile.valid_count == 10
    assert profile.error_count == 0
    assert profile.distributions["area_m2"]["max"] == pytest.approx(1000.0)


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


def test_mixed_valid_and_error_rows_are_counted(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.input_count == 10
    assert profile.valid_count == 9
    assert profile.error_count == 1
    assert profile.input_count == profile.valid_count + profile.error_count


def test_error_rows_are_excluded_from_percentiles(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.distributions["area_m2"]["max"] == pytest.approx(900.0)


def test_error_rows_are_excluded_from_buckets(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert sum(profile.width_buckets.values()) == profile.valid_count == 9
    assert sum(profile.ratio_buckets.values()) == profile.valid_count
    assert sum(profile.compactness_buckets.values()) == profile.valid_count


def test_scenario_percentages_use_valid_count(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.scenarios["A"].retained_count == 7
    assert profile.scenarios["A"].retained_percentage == pytest.approx(7 / 9 * 100)


def test_unexpected_shape_status_fails(parcels: gpd.GeoDataFrame) -> None:
    unexpected = parcels.copy()
    unexpected.loc[0, "shape_status"] = "UNKNOWN"

    with pytest.raises(ShapeProfileError, match="Unexpected"):
        profile_shape_distribution(unexpected)


def test_non_finite_metric_on_valid_row_fails(parcels: gpd.GeoDataFrame) -> None:
    non_finite = parcels.copy()
    non_finite.loc[0, "length_m"] = float("inf")

    with pytest.raises(ShapeProfileError, match="finite"):
        profile_shape_distribution(non_finite)


def test_zero_valid_rows_fails_clearly(parcels: gpd.GeoDataFrame) -> None:
    errors_only = parcels.copy()
    errors_only["shape_status"] = "ERROR"

    with pytest.raises(ShapeProfileError, match="At least one VALID"):
        profile_shape_distribution(errors_only)


@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("area_m2", 0, "area_m2 must be greater than zero"),
        ("length_m", 0, "length_m must be greater than zero"),
        ("width_m", -1, "width_m must be greater than zero"),
        ("length_width_ratio", 0.99, "length_width_ratio must be at least one"),
        ("compactness", 0, "compactness must be greater than zero and at most one"),
        ("compactness", 1.01, "compactness must be greater than zero and at most one"),
        ("centroid_lat", 90.1, "centroid_lat must be between -90 and 90"),
        ("centroid_lon", 180.1, "centroid_lon must be between -180 and 180"),
    ],
)
def test_valid_shape_metrics_require_physical_domains(
    parcels: gpd.GeoDataFrame,
    column: str,
    value: float,
    message: str,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, column] = value

    with pytest.raises(ShapeProfileError, match=message):
        profile_shape_distribution(invalid)


def test_valid_shape_length_must_not_be_less_than_width(
    parcels: gpd.GeoDataFrame,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "length_m"] = 3

    with pytest.raises(ShapeProfileError, match="length_m must be at least width_m"):
        profile_shape_distribution(invalid)


def test_valid_shape_ratio_must_match_length_divided_by_width(
    parcels: gpd.GeoDataFrame,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "length_width_ratio"] = 2

    with pytest.raises(ShapeProfileError, match="must equal length_m / width_m"):
        profile_shape_distribution(invalid)


@pytest.mark.parametrize("value", [True, "100"])
def test_valid_shape_metrics_reject_bool_and_numeric_strings(
    parcels: gpd.GeoDataFrame,
    value: object,
) -> None:
    invalid = parcels.copy()
    invalid["area_m2"] = invalid["area_m2"].astype(object)
    invalid.loc[0, "area_m2"] = value

    with pytest.raises(ShapeProfileError, match="numeric and finite"):
        profile_shape_distribution(invalid)
