import geopandas as gpd
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import Polygon

from landscout.config import ShapeCalibrationConfig, ShapeScreeningConfig
from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_shape,
)


def _shape_config(
    *,
    min_width_m: float = 15,
    max_length_width_ratio: float = 10,
    policy_version: str = "test_policy_v1",
) -> ShapeScreeningConfig:
    return ShapeScreeningConfig(
        enabled=True,
        min_width_m=min_width_m,
        max_length_width_ratio=max_length_width_ratio,
        calibration=ShapeCalibrationConfig(
            policy_version=policy_version,
            method="unit_test",
            calibration_scope="test fixture",
            sample_size=10,
            calibrated_at="2026-08-11",
            target_retention_pct=90,
            observed_retention_pct=90,
        ),
    )


@pytest.fixture
def shape_config() -> ShapeScreeningConfig:
    return _shape_config()


@pytest.fixture
def parcels() -> gpd.GeoDataFrame:
    geometry = Polygon(
        [(2.0, 43.0), (2.01, 43.0), (2.01, 43.01), (2.0, 43.0)]
    )
    return gpd.GeoDataFrame(
        {
            "parcel_id": [
                "at-boundaries",
                "passing",
                "width-below",
                "ratio-above",
                "shape-error",
                "width-unknown",
                "ratio-unknown",
                "both-unknown",
                "ratio-unknown-width-below",
                "both-thresholds-fail",
            ],
            "shape_status": [
                "VALID",
                "VALID",
                "VALID",
                "VALID",
                "ERROR",
                "VALID",
                "VALID",
                "VALID",
                "VALID",
                "VALID",
            ],
            "width_m": [15.0, 20.0, 14.9, 16.0, None, None, 20.0, None, 14.0, 14.0],
            "length_width_ratio": [
                10.0,
                5.0,
                8.0,
                10.1,
                None,
                2.0,
                None,
                None,
                None,
                11.0,
            ],
            "compactness": [0.5] * 10,
        },
        geometry=[geometry] * 10,
        crs="EPSG:4326",
    )


def test_exact_width_and_ratio_boundaries_are_retained(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, _ = filter_parcels_by_shape(parcels, shape_config)

    assert "at-boundaries" in set(retained["parcel_id"])


@pytest.mark.parametrize(
    ("parcel_id", "expected_reason"),
    [
        ("width-below", "WIDTH_BELOW_MIN"),
        ("ratio-above", "RATIO_ABOVE_MAX"),
        ("shape-error", "SHAPE_ERROR"),
        ("width-unknown", "WIDTH_UNKNOWN"),
        ("ratio-unknown", "RATIO_UNKNOWN"),
    ],
)
def test_rejected_parcel_has_expected_primary_reason(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_shape(parcels, shape_config)

    row = rejected.loc[rejected["parcel_id"] == parcel_id].iloc[0]
    assert row["shape_rejection_reason"] == expected_reason


@pytest.mark.parametrize(
    ("parcel_id", "expected_reason"),
    [
        ("shape-error", "SHAPE_ERROR"),
        ("both-unknown", "WIDTH_UNKNOWN"),
        ("ratio-unknown-width-below", "RATIO_UNKNOWN"),
        ("both-thresholds-fail", "WIDTH_BELOW_MIN"),
    ],
)
def test_rejection_reason_precedence_is_deterministic(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_shape(parcels, shape_config)

    reason = rejected.set_index("parcel_id").loc[parcel_id, "shape_rejection_reason"]
    assert reason == expected_reason


def test_shape_error_precedence_does_not_inspect_metrics(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    with_error_payload = parcels.copy()
    with_error_payload["width_m"] = with_error_payload["width_m"].astype(object)
    with_error_payload["length_width_ratio"] = with_error_payload[
        "length_width_ratio"
    ].astype(object)
    error_row = with_error_payload["parcel_id"] == "shape-error"
    with_error_payload.loc[error_row, "width_m"] = "unavailable"
    with_error_payload.loc[error_row, "length_width_ratio"] = "unavailable"

    _, rejected = filter_parcels_by_shape(with_error_payload, shape_config)

    reason = rejected.set_index("parcel_id").loc[
        "shape-error", "shape_rejection_reason"
    ]
    assert reason == "SHAPE_ERROR"


def test_enabled_outputs_record_active_policy_metadata(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, rejected = filter_parcels_by_shape(parcels, shape_config)

    for output in (retained, rejected):
        assert set(output["shape_policy_version"]) == {"test_policy_v1"}
        assert set(output["shape_policy_min_width_m"]) == {15.0}
        assert set(output["shape_policy_max_ratio"]) == {10.0}
    assert "shape_rejection_reason" not in retained.columns


def test_enabled_partition_preserves_exact_ids_and_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, rejected = filter_parcels_by_shape(parcels, shape_config)

    retained_ids = set(retained["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    assert len(parcels) == len(retained) + len(rejected)
    assert retained_ids.isdisjoint(rejected_ids)
    assert retained_ids | rejected_ids == set(parcels["parcel_id"])
    assert not retained["parcel_id"].duplicated().any()
    assert not rejected["parcel_id"].duplicated().any()
    assert retained.crs == parcels.crs
    assert rejected.crs == parcels.crs
    assert "compactness" in retained.columns
    assert "compactness" in rejected.columns


def test_filter_does_not_mutate_input(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    original = parcels.copy(deep=True)

    filter_parcels_by_shape(parcels, shape_config)

    assert_geodataframe_equal(parcels, original)


@pytest.mark.parametrize(
    "column",
    ["parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"],
)
def test_missing_required_column_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
    missing_column = parcels.drop(columns=[column])

    with pytest.raises(ParcelFilterError, match="Missing required shape columns"):
        filter_parcels_by_shape(missing_column, shape_config)


def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "parcel_id"] = None

    with pytest.raises(ParcelFilterError, match="must not be null"):
        filter_parcels_by_shape(invalid, shape_config)


def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.loc[1, "parcel_id"] = invalid.loc[0, "parcel_id"]

    with pytest.raises(ParcelFilterError, match="must be unique"):
        filter_parcels_by_shape(invalid, shape_config)


def test_unknown_crs_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.set_crs(None, allow_override=True)

    with pytest.raises(ParcelFilterError, match="known CRS"):
        filter_parcels_by_shape(invalid, shape_config)


@pytest.mark.parametrize("status", [None, "UNKNOWN"])
def test_unexpected_or_null_shape_status_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    status: str | None,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "shape_status"] = status

    with pytest.raises(ParcelFilterError, match="Unexpected shape_status"):
        filter_parcels_by_shape(invalid, shape_config)


@pytest.mark.parametrize("column", ["width_m", "length_width_ratio"])
def test_non_finite_known_metric_on_valid_row_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, column] = float("inf")

    with pytest.raises(ParcelFilterError, match="numeric and finite"):
        filter_parcels_by_shape(invalid, shape_config)


@pytest.mark.parametrize("width", [-1, 0, float("inf"), "20", True])
def test_valid_shape_requires_strict_positive_width(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: object,
) -> None:
    invalid = parcels.copy()
    invalid["width_m"] = invalid["width_m"].astype(object)
    invalid.loc[0, "width_m"] = width

    with pytest.raises(
        ParcelFilterError,
        match="width_m must be (numeric and finite|greater than zero)",
    ):
        filter_parcels_by_shape(invalid, shape_config)


@pytest.mark.parametrize("ratio", [-1, 0, 0.999, float("inf"), "2", True])
def test_valid_shape_requires_ratio_at_least_one(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    ratio: object,
) -> None:
    invalid = parcels.copy()
    invalid["length_width_ratio"] = invalid["length_width_ratio"].astype(object)
    invalid.loc[0, "length_width_ratio"] = ratio

    with pytest.raises(
        ParcelFilterError,
        match="length_width_ratio must be (numeric and finite|at least one)",
    ):
        filter_parcels_by_shape(invalid, shape_config)


def test_negative_ratio_cannot_pass_permissive_thresholds(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "width_m"] = 20
    invalid.loc[0, "length_width_ratio"] = -1

    with pytest.raises(ParcelFilterError, match="length_width_ratio must be at least one"):
        filter_parcels_by_shape(invalid, shape_config)


def test_disabled_policy_is_an_exact_passthrough(parcels: gpd.GeoDataFrame) -> None:
    disabled = ShapeScreeningConfig(enabled=False)

    retained, rejected = filter_parcels_by_shape(parcels, disabled)

    assert_geodataframe_equal(retained, parcels)
    assert_geodataframe_equal(rejected, parcels.iloc[0:0])
    for column in (
        "shape_rejection_reason",
        "shape_policy_version",
        "shape_policy_min_width_m",
        "shape_policy_max_ratio",
    ):
        assert column not in retained.columns
        assert column not in rejected.columns


def test_different_configs_change_results_for_same_parcels(
    parcels: gpd.GeoDataFrame,
) -> None:
    permissive = _shape_config(
        min_width_m=10,
        max_length_width_ratio=12,
        policy_version="permissive",
    )
    restrictive = _shape_config(
        min_width_m=18,
        max_length_width_ratio=6,
        policy_version="restrictive",
    )

    permissive_retained, _ = filter_parcels_by_shape(parcels, permissive)
    restrictive_retained, _ = filter_parcels_by_shape(parcels, restrictive)

    assert set(permissive_retained["parcel_id"]) == {
        "at-boundaries",
        "passing",
        "width-below",
        "ratio-above",
        "both-thresholds-fail",
    }
    assert set(restrictive_retained["parcel_id"]) == {"passing"}
