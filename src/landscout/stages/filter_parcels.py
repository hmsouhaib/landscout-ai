import geopandas as gpd  # type: ignore[import-untyped]

from landscout.config import ParcelConfig

REQUIRED_COLUMNS = frozenset({"geometry_status", "area_m2"})


class ParcelFilterError(ValueError):
    """Raised when normalized parcels cannot be partitioned safely."""


def filter_parcels_by_area(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    missing_columns = REQUIRED_COLUMNS - set(parcels.columns)
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ParcelFilterError(f"Missing required normalized columns: {formatted}")

    valid_geometry = parcels["geometry_status"] == "VALID"
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
    return candidates, rejected
