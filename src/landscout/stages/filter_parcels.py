from math import isfinite
from numbers import Real

import geopandas as gpd  # type: ignore[import-untyped]
from pyproj import CRS

from landscout.common.cadastre_contract import validate_cadastre_geometry_statuses
from landscout.config import ParcelConfig, ShapeScreeningConfig

AREA_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "geometry_status", "area_m2", "geometry"}
)
SHAPE_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"}
)
ALLOWED_SHAPE_STATUSES = frozenset({"VALID", "ERROR"})


class ParcelFilterError(ValueError):
    """Raised when normalized parcels cannot be partitioned safely."""


def _validate_spatial_frame(parcels: object, label: str) -> gpd.GeoDataFrame:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise ParcelFilterError(f"{label} input must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise ParcelFilterError(f"{label} input columns must be unique")
    try:
        geometry_name = parcels.active_geometry_name
    except (AttributeError, ValueError) as error:
        raise ParcelFilterError(f"{label} input geometry is invalid") from error
    if geometry_name is None or geometry_name not in parcels.columns:
        raise ParcelFilterError(f"{label} input requires an active geometry column")
    if parcels.crs is None:
        raise ParcelFilterError(f"{label} input must have a known CRS")
    try:
        CRS.from_user_input(parcels.crs)
    except Exception as error:
        raise ParcelFilterError(f"{label} input CRS must be readable") from error
    return parcels


def _missing_columns(
    parcels: object,
    required: frozenset[str],
    label: str,
) -> frozenset[str]:
    try:
        return required - set(parcels.columns)  # type: ignore[attr-defined]
    except Exception as error:
        raise ParcelFilterError(f"{label} input must be a GeoDataFrame") from error


def _validate_exact_parcel_ids(parcels: gpd.GeoDataFrame) -> None:
    identifiers = parcels["parcel_id"]
    if identifiers.isna().any():
        raise ParcelFilterError("parcel_id values must not be null")
    if any(
        not isinstance(identifier, str)
        or not identifier
        or identifier != identifier.strip()
        for identifier in identifiers
    ):
        raise ParcelFilterError("parcel_id values must be exact non-empty strings")
    if identifiers.duplicated().any():
        raise ParcelFilterError("parcel_id values must be unique")


def _is_strict_finite_number(value: object) -> bool:
    return (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and isfinite(float(value))
    )


def filter_parcels_by_area(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    missing_columns = _missing_columns(parcels, AREA_REQUIRED_COLUMNS, "Area-filter")
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ParcelFilterError(f"Missing required normalized columns: {formatted}")
    parcels = _validate_spatial_frame(parcels, "Area-filter")
    _validate_exact_parcel_ids(parcels)
    try:
        validate_cadastre_geometry_statuses(parcels["geometry_status"].tolist())
    except ValueError as error:
        raise ParcelFilterError(str(error)) from error

    valid_geometry = parcels["geometry_status"] == "VALID"
    if any(
        not _is_strict_finite_number(value) or float(value) <= 0
        for value in parcels.loc[valid_geometry, "area_m2"]
    ):
        raise ParcelFilterError(
            "area_m2 must be a strict positive finite numeric value when "
            "geometry_status is VALID"
        )

    known_area = parcels["area_m2"].notna()
    within_area_range = parcels["area_m2"].between(
        area_config.min_area_m2, area_config.max_area_m2, inclusive="both"
    )
    candidate_mask = valid_geometry & known_area & within_area_range

    candidates = parcels.loc[candidate_mask].copy()
    rejected = parcels.loc[~candidate_mask].copy()
    rejected["rejection_reason"] = "AREA_UNKNOWN"

    rejected_valid_geometry = rejected["geometry_status"] == "VALID"
    rejected_known_area = rejected["area_m2"].notna()
    rejected.loc[~rejected_valid_geometry, "rejection_reason"] = "INVALID_GEOMETRY"
    rejected.loc[
        rejected_valid_geometry
        & rejected_known_area
        & (rejected["area_m2"] < area_config.min_area_m2),
        "rejection_reason",
    ] = "AREA_BELOW_MIN"
    rejected.loc[
        rejected_valid_geometry
        & rejected_known_area
        & (rejected["area_m2"] > area_config.max_area_m2),
        "rejection_reason",
    ] = "AREA_ABOVE_MAX"

    if len(parcels) != len(candidates) + len(rejected):
        raise ParcelFilterError("Parcel partition did not preserve every input row")
    input_ids = set(parcels["parcel_id"])
    candidate_ids = set(candidates["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    if candidates["parcel_id"].duplicated().any() or rejected[
        "parcel_id"
    ].duplicated().any():
        raise ParcelFilterError("Parcel partition contains duplicate parcel IDs")
    if candidate_ids & rejected_ids:
        raise ParcelFilterError("Candidate and rejected parcel IDs overlap")
    if candidate_ids | rejected_ids != input_ids:
        raise ParcelFilterError("Parcel partition did not preserve exact parcel IDs")
    return candidates, rejected


def _validate_shape_filter_input(parcels: gpd.GeoDataFrame) -> None:
    missing_columns = _missing_columns(parcels, SHAPE_REQUIRED_COLUMNS, "Shape-filter")
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ParcelFilterError(f"Missing required shape columns: {formatted}")
    parcels = _validate_spatial_frame(parcels, "Shape-filter")
    _validate_exact_parcel_ids(parcels)

    statuses = parcels["shape_status"]
    unexpected_statuses = set(statuses.dropna().unique()) - ALLOWED_SHAPE_STATUSES
    if statuses.isna().any() or unexpected_statuses:
        formatted = ", ".join(sorted(str(value) for value in unexpected_statuses))
        detail = formatted or "null"
        raise ParcelFilterError(f"Unexpected shape_status value(s): {detail}")

    valid_rows = statuses == "VALID"
    if parcels.loc[valid_rows, ["width_m", "length_width_ratio"]].isna().any().any():
        raise ParcelFilterError(
            "VALID shape rows must have complete width_m and length_width_ratio metrics"
        )
    for column in ("width_m", "length_width_ratio"):
        if any(
            not _is_strict_finite_number(value)
            for value in parcels.loc[valid_rows, column]
        ):
            raise ParcelFilterError(
                f"{column} must be numeric and finite when shape_status is VALID"
            )
    valid_width = parcels.loc[valid_rows, "width_m"]
    if any(float(value) <= 0 for value in valid_width):
        raise ParcelFilterError(
            "width_m must be greater than zero when shape_status is VALID"
        )
    valid_ratio = parcels.loc[valid_rows, "length_width_ratio"]
    if any(float(value) < 1 for value in valid_ratio):
        raise ParcelFilterError(
            "length_width_ratio must be at least one when shape_status is VALID"
        )


def _validate_shape_partition(
    parcels: gpd.GeoDataFrame,
    retained: gpd.GeoDataFrame,
    rejected: gpd.GeoDataFrame,
) -> None:
    if len(parcels) != len(retained) + len(rejected):
        raise ParcelFilterError("Shape partition did not preserve every input row")
    if retained["parcel_id"].duplicated().any() or rejected[
        "parcel_id"
    ].duplicated().any():
        raise ParcelFilterError("Shape partition contains duplicate parcel IDs")

    input_ids = set(parcels["parcel_id"])
    retained_ids = set(retained["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    if retained_ids & rejected_ids:
        raise ParcelFilterError("Retained and rejected parcel IDs overlap")
    if retained_ids | rejected_ids != input_ids:
        raise ParcelFilterError("Shape partition did not preserve exact parcel IDs")


def filter_parcels_by_shape(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """Partition shape-enriched parcels using an explicit screening policy."""
    _validate_shape_filter_input(parcels)

    if not shape_config.enabled:
        retained = parcels.copy()
        rejected = parcels.iloc[0:0].copy()
        _validate_shape_partition(parcels, retained, rejected)
        return retained, rejected

    min_width_m = shape_config.min_width_m
    max_ratio = shape_config.max_length_width_ratio
    calibration = shape_config.calibration
    if min_width_m is None or max_ratio is None or calibration is None:
        raise ParcelFilterError("Enabled shape screening policy is incomplete")

    valid_shape = parcels["shape_status"] == "VALID"
    screening_width = parcels["width_m"].where(valid_shape)
    screening_ratio = parcels["length_width_ratio"].where(valid_shape)
    known_width = screening_width.notna()
    known_ratio = screening_ratio.notna()
    retained_mask = (
        valid_shape
        & known_width
        & known_ratio
        & (screening_width >= min_width_m)
        & (screening_ratio <= max_ratio)
    )

    retained = parcels.loc[retained_mask].copy()
    rejected = parcels.loc[~retained_mask].copy()

    rejected["shape_rejection_reason"] = "RATIO_ABOVE_MAX"
    rejected_valid = rejected["shape_status"] == "VALID"
    rejected_width = rejected["width_m"].where(rejected_valid)
    rejected.loc[
        rejected_valid
        & (rejected_width < min_width_m),
        "shape_rejection_reason",
    ] = "WIDTH_BELOW_MIN"
    rejected.loc[~rejected_valid, "shape_rejection_reason"] = "SHAPE_ERROR"

    for output in (retained, rejected):
        output["shape_policy_version"] = calibration.policy_version
        output["shape_policy_min_width_m"] = min_width_m
        output["shape_policy_max_ratio"] = max_ratio

    _validate_shape_partition(parcels, retained, rejected)
    return retained, rejected
