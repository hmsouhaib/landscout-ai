"""Compute diagnostic parcel proximity to normalized IGN electricity proxies."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from numbers import Integral, Real

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pandas.api.types import is_scalar  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import STRtree, force_2d  # type: ignore[import-untyped]

CALCULATION_CRS = "EPSG:2154"
SPATIAL_ROLE = "PROXY_GEOMETRY"

PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
LINE_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "voltage_raw",
        "voltage_status",
        "voltage_kv",
        "voltage_upper_bound_kv",
        "manager_name",
        "asset_status_raw",
        "geometry",
    }
)
POST_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "name",
        "importance_raw",
        "asset_status_raw",
        "geometry",
    }
)
GRID_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
LINE_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
POST_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})

VOLTAGE_PROXIMITY_COLUMNS = (
    "parcel_id",
    "voltage_kv",
    "nearest_line_proxy_distance_m",
    "nearest_line_grid_feature_id",
    "nearest_line_source_feature_id",
    "tie_count",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)

_LINE_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "voltage_raw",
    "voltage_status",
    "voltage_kv",
    "voltage_upper_bound_kv",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
_POST_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "name",
    "importance_raw",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)

_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_line_proxy_distance_m",
    "grid_feature_id": "nearest_line_grid_feature_id",
    "source_feature_id": "nearest_line_source_feature_id",
    "tie_count": "nearest_line_tie_count",
    "voltage_raw": "nearest_line_voltage_raw",
    "voltage_status": "nearest_line_voltage_status",
    "voltage_kv": "nearest_line_voltage_kv",
    "voltage_upper_bound_kv": "nearest_line_voltage_upper_bound_kv",
    "manager_name": "nearest_line_manager_name",
    "asset_status_raw": "nearest_line_asset_status_raw",
    "source_department_code": "nearest_line_source_department_code",
    "source_edition": "nearest_line_source_edition",
    "source_archive_sha256": "nearest_line_source_archive_sha256",
}
_EXACT_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_exact_line_proxy_distance_m",
    "grid_feature_id": "nearest_exact_line_grid_feature_id",
    "source_feature_id": "nearest_exact_line_source_feature_id",
    "tie_count": "nearest_exact_line_tie_count",
    "voltage_kv": "nearest_exact_line_voltage_kv",
    "manager_name": "nearest_exact_line_manager_name",
    "asset_status_raw": "nearest_exact_line_asset_status_raw",
    "source_department_code": "nearest_exact_line_source_department_code",
    "source_edition": "nearest_exact_line_source_edition",
    "source_archive_sha256": "nearest_exact_line_source_archive_sha256",
}
_POST_OUTPUT_MAPPING = {
    "distance_m": "nearest_post_proxy_distance_m",
    "grid_feature_id": "nearest_post_grid_feature_id",
    "source_feature_id": "nearest_post_source_feature_id",
    "tie_count": "nearest_post_tie_count",
    "name": "nearest_post_name",
    "importance_raw": "nearest_post_importance_raw",
    "asset_status_raw": "nearest_post_asset_status_raw",
    "source_department_code": "nearest_post_source_department_code",
    "source_edition": "nearest_post_source_edition",
    "source_archive_sha256": "nearest_post_source_archive_sha256",
}


class GridProximityError(ValueError):
    """Raised when grid-proximity inputs or results are unsafe."""


@dataclass(frozen=True)
class VoltageLevelCoverage:
    """Source-line coverage for one dynamically observed exact voltage."""

    voltage_kv: float
    line_feature_count: int


@dataclass(frozen=True)
class GridProximityResult:
    """Parcel enrichment and dynamic exact-voltage proximity output."""

    parcels: gpd.GeoDataFrame
    voltage_level_proximity: pd.DataFrame
    voltage_level_coverage: tuple[VoltageLevelCoverage, ...]


@dataclass(frozen=True)
class DistanceProfile:
    """Threshold-free distribution summary for one distance field."""

    count: int
    missing_count: int
    minimum: float | None
    p01: float | None
    p05: float | None
    p10: float | None
    p25: float | None
    p50: float | None
    p75: float | None
    p90: float | None
    p95: float | None
    p99: float | None
    maximum: float | None
    zero_distance_count: int
    tie_count: int


@dataclass(frozen=True)
class VoltageLevelDistanceProfile:
    """Distance distribution and source coverage for one exact voltage."""

    voltage_kv: float
    line_feature_count: int
    parcel_proximity_count: int
    distance: DistanceProfile


@dataclass(frozen=True)
class GridProximityProfile:
    """Threshold-free parcel and voltage-level proximity profiles."""

    parcel_count: int
    nearest_line: DistanceProfile
    nearest_exact_line: DistanceProfile
    nearest_post: DistanceProfile
    voltage_levels: tuple[VoltageLevelDistanceProfile, ...]


def _validated_crs(value: object, label: str) -> CRS:
    if value is None:
        raise GridProximityError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise GridProximityError(f"{label} CRS is unreadable") from error


def _require_lambert93(value: object, label: str) -> None:
    actual = _validated_crs(value, label)
    expected = CRS.from_epsg(2154)
    if not actual.is_projected or not actual.equals(expected):
        raise GridProximityError(f"{label} must use EPSG:2154")


def _validate_active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise GridProximityError(f"{label} geometry column is required")
    if frame.active_geometry_name != "geometry":
        raise GridProximityError(f"{label} geometry column must be active")


def _validate_id_values(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise GridProximityError(f"{label} values must not be null")
    raw_values = values.tolist()
    if any(not isinstance(value, str) for value in raw_values):
        raise GridProximityError(f"{label} values must be strings")
    if any(not value.strip() for value in raw_values):
        raise GridProximityError(f"{label} values must not be empty")
    if any(value != value.strip() for value in raw_values):
        raise GridProximityError(
            f"{label} values must not contain leading or trailing whitespace"
        )
    if require_unique and values.duplicated().any():
        raise GridProximityError(f"{label} values must be unique")


def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
    missing = PARCEL_REQUIRED_COLUMNS - set(parcels.columns)
    if missing:
        raise GridProximityError(
            "Missing required parcel columns: " + ", ".join(sorted(missing))
        )
    _validate_active_geometry(parcels, "Parcel")
    source_crs = _validated_crs(parcels.crs, "Parcel")
    _validate_id_values(parcels["parcel_id"], "parcel_id", require_unique=True)
    if parcels.geometry.isna().any():
        raise GridProximityError("Parcel geometries must not be null")
    if parcels.geometry.is_empty.any():
        raise GridProximityError("Parcel geometries must not be empty")
    if not parcels.geometry.is_valid.all():
        raise GridProximityError("Parcel geometries must be valid")
    geometry_types = set(parcels.geometry.geom_type.dropna())
    unsupported = sorted(
        str(value) for value in geometry_types - PARCEL_GEOMETRY_TYPES
    )
    if unsupported:
        raise GridProximityError(
            "Parcel geometries must be Polygon or MultiPolygon; found: "
            + ", ".join(unsupported)
        )
    return source_crs


def _observed_geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
    status = pd.Series("VALID", index=geometry.index, dtype="object")
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    status.loc[null_mask] = "NULL"
    status.loc[empty_mask] = "EMPTY"
    status.loc[invalid_mask] = "INVALID"
    return status


def _validate_grid(
    frame: gpd.GeoDataFrame,
    *,
    label: str,
    required_columns: frozenset[str],
    feature_type: str,
    allowed_geometry_types: frozenset[str],
) -> gpd.GeoDataFrame:
    missing = required_columns - set(frame.columns)
    if missing:
        raise GridProximityError(
            f"Missing required {label} columns: " + ", ".join(sorted(missing))
        )
    _validate_active_geometry(frame, label)
    _require_lambert93(frame.crs, label)

    identifiers = frame["grid_feature_id"]
    if identifiers.isna().any():
        raise GridProximityError(f"{label} grid_feature_id values must not be null")
    if any(not isinstance(value, str) or not value for value in identifiers.tolist()):
        raise GridProximityError(
            f"{label} grid_feature_id values must be non-empty strings"
        )
    if identifiers.duplicated().any():
        raise GridProximityError(f"{label} grid_feature_id values must be unique")
    if frame["grid_feature_type"].isna().any() or not frame[
        "grid_feature_type"
    ].eq(feature_type).all():
        raise GridProximityError(
            f"{label} grid_feature_type must be {feature_type}"
        )
    if frame["spatial_role"].isna().any() or not frame["spatial_role"].eq(
        SPATIAL_ROLE
    ).all():
        raise GridProximityError(f"{label} spatial_role must be PROXY_GEOMETRY")

    declared_status = frame["geometry_status"]
    observed_status = _observed_geometry_status(frame.geometry)
    declared_values = set(declared_status.dropna().unique())
    if declared_status.isna().any() or not declared_values <= GRID_GEOMETRY_STATUSES:
        raise GridProximityError(f"{label} has unexpected geometry_status values")
    if not declared_status.astype("object").equals(observed_status):
        raise GridProximityError(
            f"{label} geometry_status does not match the source geometry"
        )

    valid_mask = declared_status == "VALID"
    valid_types = set(frame.loc[valid_mask, "geometry"].geom_type.dropna())
    unsupported = sorted(str(value) for value in valid_types - allowed_geometry_types)
    if unsupported:
        raise GridProximityError(
            f"{label} has unsupported VALID geometry types: "
            + ", ".join(unsupported)
        )
    return frame.loc[valid_mask].reset_index(drop=True).copy()


def _finite_real_as_float(value: object) -> float | None:
    if not isinstance(value, Real) or isinstance(value, bool):
        return None
    try:
        numeric = float(value)
    except (OverflowError, TypeError, ValueError):
        return None
    return numeric if isfinite(numeric) else None


def _is_positive_finite_number(value: object) -> bool:
    numeric = _finite_real_as_float(value)
    return numeric is not None and numeric > 0


def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
    values = np.asarray(frame.geometry.array, dtype=object)
    return np.asarray(force_2d(values), dtype=object)


def _empty_nearest_result(
    parcel_count: int,
    attribute_columns: tuple[str, ...],
) -> pd.DataFrame:
    output = pd.DataFrame(index=pd.RangeIndex(parcel_count))
    output["distance_m"] = pd.Series(np.nan, index=output.index, dtype="float64")
    output["tie_count"] = pd.Series(pd.NA, index=output.index, dtype="Int64")
    for column in attribute_columns:
        if column in {"voltage_kv", "voltage_upper_bound_kv"}:
            output[column] = pd.Series(np.nan, index=output.index, dtype="float64")
        else:
            output[column] = pd.Series(pd.NA, index=output.index, dtype="object")
    return output


def _nearest_feature_rows(
    parcel_geometries: np.ndarray,
    features: gpd.GeoDataFrame,
    attribute_columns: tuple[str, ...],
    *,
    allow_empty: bool = False,
) -> pd.DataFrame:
    parcel_count = len(parcel_geometries)
    if features.empty:
        if allow_empty:
            return _empty_nearest_result(parcel_count, attribute_columns)
        raise GridProximityError("No VALID grid proxy feature is available")

    feature_geometries = _calculation_geometries(features)
    tree = STRtree(feature_geometries)
    indices, distances = tree.query_nearest(
        parcel_geometries,
        all_matches=True,
        return_distance=True,
    )
    matches = pd.DataFrame(
        {
            "parcel_position": indices[0],
            "feature_position": indices[1],
            "distance_m": distances,
        }
    )
    matches["grid_feature_id"] = features.iloc[
        matches["feature_position"].to_numpy()
    ]["grid_feature_id"].to_numpy()
    matches = matches.sort_values(
        ["parcel_position", "distance_m", "grid_feature_id"],
        kind="mergesort",
    )
    ties = matches.groupby("parcel_position", sort=False).size()
    selected = matches.drop_duplicates("parcel_position", keep="first").sort_values(
        "parcel_position"
    )
    if selected["parcel_position"].tolist() != list(range(parcel_count)):
        raise GridProximityError("Nearest-neighbour matching did not cover every parcel")

    feature_positions = selected["feature_position"].to_numpy()
    output = features.iloc[feature_positions].loc[:, list(attribute_columns)].copy()
    output = output.reset_index(drop=True)
    output.insert(0, "tie_count", ties.reindex(range(parcel_count)).to_numpy())
    output.insert(0, "distance_m", selected["distance_m"].to_numpy(dtype="float64"))
    return output


def _attach_matches(
    parcels: gpd.GeoDataFrame,
    matches: pd.DataFrame,
    mapping: dict[str, str],
) -> None:
    for source_column, output_column in mapping.items():
        parcels[output_column] = matches[source_column].reset_index(drop=True)


def _validate_distance_values(values: pd.Series, label: str) -> None:
    non_null = values.dropna()
    numeric_values = [
        _finite_real_as_float(value) for value in non_null.tolist()
    ]
    if any(value is None for value in numeric_values):
        raise GridProximityError(f"{label} distances must be numeric and finite")
    numeric = np.asarray(numeric_values, dtype="float64")
    if (numeric < 0).any():
        raise GridProximityError(f"{label} distances must be finite and >= 0")


def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    if not is_scalar(value):
        return False
    return bool(pd.isna(value))


def _validate_tie_counts(
    values: pd.Series,
    matched: pd.Series,
    label: str,
) -> None:
    if len(values) != len(matched):
        raise GridProximityError(f"{label} tie-count state is inconsistent")
    for value, row_is_matched in zip(
        values.tolist(), matched.to_numpy(dtype="bool"), strict=True
    ):
        missing = _is_missing_scalar(value)
        if not row_is_matched:
            if not missing:
                raise GridProximityError(
                    f"{label} unmatched rows must have null tie_count"
                )
            continue
        if missing:
            raise GridProximityError(f"{label} matched rows require tie_count")
        numeric = _finite_real_as_float(value)
        if numeric is None or not numeric.is_integer() or numeric < 1:
            raise GridProximityError(
                f"{label} tie_count must be a finite integer >= 1"
            )


def _validate_match_integrity(
    frame: pd.DataFrame,
    *,
    label: str,
    distance_column: str,
    grid_id_column: str,
    source_id_column: str,
    tie_column: str,
    expect_matches: bool,
    voltage_column: str | None = None,
    unmatched_null_columns: tuple[str, ...] = (),
) -> None:
    required = {distance_column, grid_id_column, source_id_column, tie_column}
    if voltage_column is not None:
        required.add(voltage_column)
    missing = required - set(frame.columns)
    if missing:
        raise GridProximityError(
            f"Missing {label} match columns: " + ", ".join(sorted(missing))
        )

    distance = frame[distance_column]
    matched = distance.notna()
    if expect_matches and not matched.all():
        raise GridProximityError(f"{label} requires a match for every parcel")
    if not expect_matches and matched.any():
        raise GridProximityError(f"{label} must be entirely unmatched")
    _validate_distance_values(distance, label)
    _validate_tie_counts(frame[tie_column], matched, label)

    id_columns = (grid_id_column, source_id_column)
    if expect_matches:
        for column in id_columns:
            if frame[column].isna().any():
                raise GridProximityError(f"{label} matched rows require {column}")
        if voltage_column is not None and not frame[voltage_column].map(
            _is_positive_finite_number
        ).all():
            raise GridProximityError(
                f"{label} voltage must be numeric, finite, and > 0"
            )
        return

    null_columns = set(unmatched_null_columns) | set(id_columns)
    if voltage_column is not None:
        null_columns.add(voltage_column)
    for column in null_columns:
        if column not in frame.columns:
            raise GridProximityError(f"Missing {label} match column: {column}")
        if frame[column].notna().any():
            raise GridProximityError(
                f"{label} unmatched rows must have null {column}"
            )


def _validate_voltage_coverage(
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
    levels: list[float] = []
    for item in coverage:
        if not isinstance(item, VoltageLevelCoverage):
            raise GridProximityError("Voltage coverage entries are invalid")
        if not _is_positive_finite_number(item.voltage_kv):
            raise GridProximityError(
                "Voltage coverage levels must be numeric, finite, and > 0"
            )
        if (
            not isinstance(item.line_feature_count, Integral)
            or isinstance(item.line_feature_count, bool)
            or item.line_feature_count <= 0
        ):
            raise GridProximityError(
                "Voltage coverage line_feature_count must be an integer > 0"
            )
        levels.append(float(item.voltage_kv))
    if len(set(levels)) != len(levels):
        raise GridProximityError("Voltage coverage levels must be unique")
    if levels != sorted(levels):
        raise GridProximityError("Voltage coverage levels must be ascending")
    return tuple(levels)


def _validate_voltage_table(
    table: pd.DataFrame,
    parcel_ids: pd.Series,
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
    missing = set(VOLTAGE_PROXIMITY_COLUMNS) - set(table.columns)
    if missing:
        raise GridProximityError(
            "Missing voltage proximity columns: " + ", ".join(sorted(missing))
        )
    levels = _validate_voltage_coverage(coverage)
    expected_rows = len(parcel_ids) * len(levels)
    if len(table) != expected_rows:
        raise GridProximityError("Voltage proximity row count is inconsistent")
    if table.empty:
        return levels

    _validate_id_values(table["parcel_id"], "parcel_id", require_unique=False)
    raw_voltage_values = table["voltage_kv"]
    if not raw_voltage_values.map(_is_positive_finite_number).all():
        raise GridProximityError(
            "Voltage proximity levels must be numeric, finite, and > 0"
        )
    if table.duplicated(["parcel_id", "voltage_kv"]).any():
        raise GridProximityError("Voltage proximity parcel/voltage pairs must be unique")
    table_levels = tuple(
        sorted({float(value) for value in raw_voltage_values.tolist()})
    )
    if table_levels != levels:
        raise GridProximityError(
            "Voltage proximity levels do not match source coverage"
        )

    expected_ids = parcel_ids.tolist()
    for voltage_kv in levels:
        rows = table.loc[raw_voltage_values.map(float) == voltage_kv]
        if len(rows) != len(expected_ids) or rows["parcel_id"].tolist() != expected_ids:
            raise GridProximityError(
                f"Voltage proximity does not contain the exact parcel set for {voltage_kv:g} kV"
            )

    _validate_match_integrity(
        table,
        label="Voltage-level line proximity",
        distance_column="nearest_line_proxy_distance_m",
        grid_id_column="nearest_line_grid_feature_id",
        source_id_column="nearest_line_source_feature_id",
        tie_column="tie_count",
        expect_matches=True,
    )
    for column in (
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    ):
        if table[column].isna().any():
            raise GridProximityError(
                f"Voltage-level matched rows require {column}"
            )
    return levels


def _validate_result_contract(result: GridProximityResult) -> tuple[float, ...]:
    parcels = result.parcels
    _validate_parcels(parcels)
    required_proximity_columns = (
        set(_LINE_OUTPUT_MAPPING.values())
        | set(_EXACT_LINE_OUTPUT_MAPPING.values())
        | set(_POST_OUTPUT_MAPPING.values())
    )
    missing = required_proximity_columns - set(parcels.columns)
    if missing:
        raise GridProximityError(
            "Missing proximity result columns: " + ", ".join(sorted(missing))
        )
    levels = _validate_voltage_coverage(result.voltage_level_coverage)
    _validate_match_integrity(
        parcels,
        label="Nearest line proximity",
        distance_column="nearest_line_proxy_distance_m",
        grid_id_column="nearest_line_grid_feature_id",
        source_id_column="nearest_line_source_feature_id",
        tie_column="nearest_line_tie_count",
        expect_matches=True,
    )
    _validate_match_integrity(
        parcels,
        label="Nearest post proximity",
        distance_column="nearest_post_proxy_distance_m",
        grid_id_column="nearest_post_grid_feature_id",
        source_id_column="nearest_post_source_feature_id",
        tie_column="nearest_post_tie_count",
        expect_matches=True,
    )
    _validate_match_integrity(
        parcels,
        label="Nearest exact-line proximity",
        distance_column="nearest_exact_line_proxy_distance_m",
        grid_id_column="nearest_exact_line_grid_feature_id",
        source_id_column="nearest_exact_line_source_feature_id",
        tie_column="nearest_exact_line_tie_count",
        expect_matches=bool(levels),
        voltage_column="nearest_exact_line_voltage_kv",
        unmatched_null_columns=tuple(_EXACT_LINE_OUTPUT_MAPPING.values()),
    )
    if levels and not parcels["nearest_exact_line_voltage_kv"].map(float).isin(
        levels
    ).all():
        raise GridProximityError(
            "Nearest exact-line voltage does not match source coverage"
        )
    _validate_voltage_table(
        result.voltage_level_proximity,
        parcels["parcel_id"],
        result.voltage_level_coverage,
    )
    return levels


def _validate_output_integrity(
    source_parcels: gpd.GeoDataFrame,
    result: GridProximityResult,
) -> None:
    _validate_result_contract(result)
    output = result.parcels
    if len(output) != len(source_parcels):
        raise GridProximityError("Grid proximity enrichment changed parcel count")
    source_ids = source_parcels["parcel_id"].reset_index(drop=True)
    output_ids = output["parcel_id"].reset_index(drop=True)
    if not source_ids.equals(output_ids):
        raise GridProximityError("Grid proximity enrichment changed parcel IDs or order")
    source_crs = _validated_crs(source_parcels.crs, "Input parcel")
    output_crs = _validated_crs(output.crs, "Output parcel")
    if not source_crs.equals(output_crs):
        raise GridProximityError("Enriched parcel CRS changed")
    if not output.geometry.geom_equals_exact(
        source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False
    ).all():
        raise GridProximityError("Enriched parcel geometry changed")


def _voltage_level_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    exact_lines: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]:
    levels = tuple(sorted(float(value) for value in exact_lines["voltage_kv"].unique()))
    tables: list[pd.DataFrame] = []
    coverage: list[VoltageLevelCoverage] = []
    for voltage_kv in levels:
        level_lines = exact_lines.loc[exact_lines["voltage_kv"] == voltage_kv].copy()
        coverage.append(
            VoltageLevelCoverage(
                voltage_kv=voltage_kv,
                line_feature_count=len(level_lines),
            )
        )
        nearest = _nearest_feature_rows(
            parcel_geometries,
            level_lines,
            (
                "grid_feature_id",
                "source_feature_id",
                "manager_name",
                "asset_status_raw",
                "source_department_code",
                "source_edition",
                "source_archive_sha256",
            ),
        )
        table = pd.DataFrame(
            {
                "parcel_id": parcel_ids.reset_index(drop=True),
                "voltage_kv": voltage_kv,
                "nearest_line_proxy_distance_m": nearest["distance_m"],
                "nearest_line_grid_feature_id": nearest["grid_feature_id"],
                "nearest_line_source_feature_id": nearest["source_feature_id"],
                "tie_count": nearest["tie_count"],
                "manager_name": nearest["manager_name"],
                "asset_status_raw": nearest["asset_status_raw"],
                "source_department_code": nearest["source_department_code"],
                "source_edition": nearest["source_edition"],
                "source_archive_sha256": nearest["source_archive_sha256"],
            }
        )
        tables.append(table.loc[:, list(VOLTAGE_PROXIMITY_COLUMNS)])

    if not tables:
        empty = pd.DataFrame(columns=list(VOLTAGE_PROXIMITY_COLUMNS))
        empty["voltage_kv"] = empty["voltage_kv"].astype("float64")
        empty["nearest_line_proxy_distance_m"] = empty[
            "nearest_line_proxy_distance_m"
        ].astype("float64")
        empty["tie_count"] = empty["tie_count"].astype("Int64")
        return empty, ()
    return pd.concat(tables, ignore_index=True), tuple(coverage)


def enrich_parcel_grid_proximity(
    parcels: gpd.GeoDataFrame,
    electric_lines: gpd.GeoDataFrame,
    transformation_posts: gpd.GeoDataFrame,
) -> GridProximityResult:
    """Attach nearest IGN proxy matches using planar XY distance in EPSG:2154.

    IGN Z values are removed from calculation-only copies and do not affect
    horizontal proximity. Source parcel and normalized IGN geometries are not
    mutated. Distances describe only the nearest feature inside loaded proxy
    coverage and do not establish connection feasibility.
    """

    _validate_parcels(parcels)
    valid_lines = _validate_grid(
        electric_lines,
        label="Electric-line grid",
        required_columns=LINE_REQUIRED_COLUMNS,
        feature_type="ELECTRIC_LINE",
        allowed_geometry_types=LINE_GEOMETRY_TYPES,
    )
    valid_posts = _validate_grid(
        transformation_posts,
        label="Transformation-post grid",
        required_columns=POST_REQUIRED_COLUMNS,
        feature_type="TRANSFORMATION_POST",
        allowed_geometry_types=POST_GEOMETRY_TYPES,
    )
    if valid_lines.empty:
        raise GridProximityError("No VALID electric-line proxy is available")
    if valid_posts.empty:
        raise GridProximityError("No VALID transformation-post proxy is available")

    output = parcels.reset_index(drop=True).copy()
    calculation_parcels = output.to_crs(CALCULATION_CRS)
    parcel_geometries = _calculation_geometries(calculation_parcels)

    nearest_line = _nearest_feature_rows(
        parcel_geometries,
        valid_lines,
        _LINE_MATCH_COLUMNS,
    )
    _attach_matches(output, nearest_line, _LINE_OUTPUT_MAPPING)

    exact_mask = (valid_lines["voltage_status"] == "EXACT") & valid_lines[
        "voltage_kv"
    ].map(_is_positive_finite_number)
    exact_lines = valid_lines.loc[exact_mask].reset_index(drop=True).copy()
    exact_lines["voltage_kv"] = exact_lines["voltage_kv"].map(float).astype("float64")
    nearest_exact = _nearest_feature_rows(
        parcel_geometries,
        exact_lines,
        _LINE_MATCH_COLUMNS,
        allow_empty=True,
    )
    _attach_matches(output, nearest_exact, _EXACT_LINE_OUTPUT_MAPPING)

    nearest_post = _nearest_feature_rows(
        parcel_geometries,
        valid_posts,
        _POST_MATCH_COLUMNS,
    )
    _attach_matches(output, nearest_post, _POST_OUTPUT_MAPPING)

    voltage_table, voltage_coverage = _voltage_level_table(
        output["parcel_id"], parcel_geometries, exact_lines
    )
    result = GridProximityResult(
        parcels=output,
        voltage_level_proximity=voltage_table,
        voltage_level_coverage=voltage_coverage,
    )
    _validate_output_integrity(parcels, result)
    return result


def _distance_profile(distances: pd.Series, ties: pd.Series) -> DistanceProfile:
    _validate_distance_values(distances, "Profile")
    values = distances.dropna().astype("float64")
    missing_count = int(distances.isna().sum())
    if values.empty:
        return DistanceProfile(
            count=0,
            missing_count=missing_count,
            minimum=None,
            p01=None,
            p05=None,
            p10=None,
            p25=None,
            p50=None,
            p75=None,
            p90=None,
            p95=None,
            p99=None,
            maximum=None,
            zero_distance_count=0,
            tie_count=0,
        )
    matched_ties = ties.loc[distances.notna()]
    if matched_ties.isna().any():
        raise GridProximityError("Matched distance rows require tie counts")
    return DistanceProfile(
        count=len(values),
        missing_count=missing_count,
        minimum=float(values.min()),
        p01=float(values.quantile(0.01)),
        p05=float(values.quantile(0.05)),
        p10=float(values.quantile(0.10)),
        p25=float(values.quantile(0.25)),
        p50=float(values.quantile(0.50)),
        p75=float(values.quantile(0.75)),
        p90=float(values.quantile(0.90)),
        p95=float(values.quantile(0.95)),
        p99=float(values.quantile(0.99)),
        maximum=float(values.max()),
        zero_distance_count=int(values.eq(0).sum()),
        tie_count=sum(value > 1 for value in matched_ties.tolist()),
    )


def profile_grid_proximity(result: GridProximityResult) -> GridProximityProfile:
    """Profile proximity distances without thresholds or suitability labels."""

    _validate_result_contract(result)
    parcels = result.parcels
    coverage = {
        float(item.voltage_kv): item.line_feature_count
        for item in result.voltage_level_coverage
    }
    voltage_profiles: list[VoltageLevelDistanceProfile] = []
    table = result.voltage_level_proximity
    observed_levels = tuple(coverage)
    for voltage_kv in observed_levels:
        rows = table.loc[table["voltage_kv"] == voltage_kv]
        distance = _distance_profile(
            rows["nearest_line_proxy_distance_m"], rows["tie_count"]
        )
        voltage_profiles.append(
            VoltageLevelDistanceProfile(
                voltage_kv=voltage_kv,
                line_feature_count=coverage[voltage_kv],
                parcel_proximity_count=len(rows),
                distance=distance,
            )
        )

    return GridProximityProfile(
        parcel_count=len(parcels),
        nearest_line=_distance_profile(
            parcels["nearest_line_proxy_distance_m"],
            parcels["nearest_line_tie_count"],
        ),
        nearest_exact_line=_distance_profile(
            parcels["nearest_exact_line_proxy_distance_m"],
            parcels["nearest_exact_line_tie_count"],
        ),
        nearest_post=_distance_profile(
            parcels["nearest_post_proxy_distance_m"],
            parcels["nearest_post_tie_count"],
        ),
        voltage_levels=tuple(voltage_profiles),
    )
