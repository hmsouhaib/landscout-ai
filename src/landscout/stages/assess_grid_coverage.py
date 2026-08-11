"""Diagnose IGN grid-proxy results against loaded package coverage boundaries."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from numbers import Real
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import (  # type: ignore[import-untyped]
    boundary,
    covers,
    distance,
    force_2d,
    intersects,
)

from landscout.sources.ign_bdtopo_fr import IgnBdTopoDepartmentCoverage
from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    profile_grid_proximity,
)

CALCULATION_CRS = "EPSG:2154"
COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"

CoverageStatus = Literal[
    "NOT_BOUNDARY_LIMITED",
    "BOUNDARY_LIMITED",
    "OUTSIDE_OR_CROSSING_COVERAGE",
    "NO_MATCH",
]
CoveragePosition = Literal["FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"]

COVERAGE_STATUSES = frozenset(
    {
        "NOT_BOUNDARY_LIMITED",
        "BOUNDARY_LIMITED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
        "NO_MATCH",
    }
)
COVERAGE_POSITIONS = frozenset(
    {"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"}
)
PARCEL_DIAGNOSTIC_COLUMNS = (
    "grid_source_boundary_distance_m",
    "grid_source_coverage_position",
    "nearest_line_coverage_status",
    "nearest_exact_line_coverage_status",
    "nearest_post_coverage_status",
)
VOLTAGE_DIAGNOSTIC_COLUMNS = (
    "source_boundary_distance_m",
    "coverage_status",
)
COVERAGE_LINEAGE_COLUMNS = (
    "grid_source_coverage_provider",
    "grid_source_coverage_product",
    "grid_source_coverage_department_code",
    "grid_source_coverage_edition",
    "grid_source_coverage_product_version",
    "grid_source_coverage_archive_sha256",
    "grid_source_coverage_layer",
    "grid_source_coverage_spatial_role",
)


class GridCoverageAssessmentError(ValueError):
    """Raised when coverage diagnostics cannot be calculated safely."""


@dataclass(frozen=True)
class GridCoverageAssessmentResult:
    """Coverage-annotated copies of both grid-proximity representations."""

    parcels: gpd.GeoDataFrame
    voltage_level_proximity: pd.DataFrame
    voltage_level_coverage: tuple[VoltageLevelCoverage, ...]
    source_coverage: IgnBdTopoDepartmentCoverage


@dataclass(frozen=True)
class BoundaryDistanceProfile:
    count: int
    minimum: float
    p01: float
    p05: float
    p10: float
    p25: float
    p50: float
    p75: float
    p90: float
    p95: float
    p99: float
    maximum: float


@dataclass(frozen=True)
class CoverageStatusCounts:
    not_boundary_limited: int
    boundary_limited: int
    outside_or_crossing_coverage: int
    no_match: int


@dataclass(frozen=True)
class VoltageCoverageStatusProfile:
    voltage_kv: float
    parcel_count: int
    statuses: CoverageStatusCounts


@dataclass(frozen=True)
class GridCoverageProfile:
    parcel_count: int
    fully_covered_count: int
    outside_or_crossing_count: int
    boundary_distance: BoundaryDistanceProfile
    nearest_line: CoverageStatusCounts
    nearest_exact_line: CoverageStatusCounts
    nearest_post: CoverageStatusCounts
    voltage_levels: tuple[VoltageCoverageStatusProfile, ...]


def _validated_lambert93(value: object, label: str) -> CRS:
    if value is None:
        raise GridCoverageAssessmentError(f"{label} CRS is required")
    try:
        crs = CRS.from_user_input(value)
    except Exception as error:
        raise GridCoverageAssessmentError(f"{label} CRS is unreadable") from error
    expected = CRS.from_epsg(2154)
    if not crs.is_projected or not crs.equals(expected):
        raise GridCoverageAssessmentError(f"{label} must use EPSG:2154")
    return crs


def _validate_source_coverage(
    source: IgnBdTopoDepartmentCoverage,
) -> gpd.GeoDataFrame:
    if source.spatial_role != COVERAGE_SPATIAL_ROLE:
        raise GridCoverageAssessmentError(
            "Department coverage spatial_role must be SOURCE_COVERAGE_BOUNDARY"
        )
    for label, value in (
        ("source_provider", source.source_provider),
        ("source_product", source.source_product),
        ("source_department_code", source.source_department_code),
        ("source_edition", source.source_edition),
        ("source_archive_sha256", source.source_archive_sha256),
        ("source_layer", source.source_layer),
    ):
        if not isinstance(value, str) or not value or value != value.strip():
            raise GridCoverageAssessmentError(
                f"Department coverage {label} must be a non-empty exact string"
            )
    frame = source.coverage
    if not isinstance(frame, gpd.GeoDataFrame):
        raise GridCoverageAssessmentError("Department coverage must be a GeoDataFrame")
    if "geometry" not in frame.columns or frame.active_geometry_name != "geometry":
        raise GridCoverageAssessmentError(
            "Department coverage geometry column must exist and be active"
        )
    _validated_lambert93(frame.crs, "Department coverage")
    if len(frame) != 1:
        raise GridCoverageAssessmentError(
            "Department coverage must contain exactly one selected feature"
        )
    geometry = frame.geometry
    if geometry.isna().any():
        raise GridCoverageAssessmentError("Department coverage geometry must not be null")
    if geometry.is_empty.any():
        raise GridCoverageAssessmentError("Department coverage geometry must not be empty")
    if not geometry.is_valid.all():
        raise GridCoverageAssessmentError("Department coverage geometry must be valid")
    if not set(geometry.geom_type.dropna()) <= {"Polygon", "MultiPolygon"}:
        raise GridCoverageAssessmentError(
            "Department coverage geometry must be Polygon or MultiPolygon"
        )
    expected_lineage: dict[str, object] = {
        "source_provider": source.source_provider,
        "source_product": source.source_product,
        "source_department_code": source.source_department_code,
        "source_edition": source.source_edition,
        "source_product_version": source.source_product_version,
        "source_archive_sha256": source.source_archive_sha256,
        "source_layer": source.source_layer,
        "spatial_role": source.spatial_role,
    }
    missing = set(expected_lineage) - set(frame.columns)
    if missing:
        raise GridCoverageAssessmentError(
            "Department coverage lineage columns are missing: "
            + ", ".join(sorted(missing))
        )
    for column, expected in expected_lineage.items():
        actual = frame.iloc[0][column]
        both_null = pd.isna(actual) and expected is None
        if not both_null and actual != expected:
            raise GridCoverageAssessmentError(
                f"Department coverage lineage is inconsistent: {column}"
            )
    return frame


def _coverage_lineage_values(
    source: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
    return {
        "grid_source_coverage_provider": source.source_provider,
        "grid_source_coverage_product": source.source_product,
        "grid_source_coverage_department_code": source.source_department_code,
        "grid_source_coverage_edition": source.source_edition,
        "grid_source_coverage_product_version": source.source_product_version,
        "grid_source_coverage_archive_sha256": source.source_archive_sha256,
        "grid_source_coverage_layer": source.source_layer,
        "grid_source_coverage_spatial_role": source.spatial_role,
    }


def _validate_proximity_source_identity(
    proximity: GridProximityResult,
    source: IgnBdTopoDepartmentCoverage,
) -> None:
    parcel_mappings = (
        (
            "nearest_line_source_department_code",
            source.source_department_code,
        ),
        ("nearest_line_source_edition", source.source_edition),
        ("nearest_line_source_archive_sha256", source.source_archive_sha256),
        (
            "nearest_exact_line_source_department_code",
            source.source_department_code,
        ),
        ("nearest_exact_line_source_edition", source.source_edition),
        (
            "nearest_exact_line_source_archive_sha256",
            source.source_archive_sha256,
        ),
        (
            "nearest_post_source_department_code",
            source.source_department_code,
        ),
        ("nearest_post_source_edition", source.source_edition),
        ("nearest_post_source_archive_sha256", source.source_archive_sha256),
    )
    for column, expected in parcel_mappings:
        values = proximity.parcels[column].dropna()
        if not values.eq(expected).all():
            raise GridCoverageAssessmentError(
                f"Proximity lineage does not match department coverage: {column}"
            )
    table_mappings = (
        ("source_department_code", source.source_department_code),
        ("source_edition", source.source_edition),
        ("source_archive_sha256", source.source_archive_sha256),
    )
    for column, expected in table_mappings:
        if not proximity.voltage_level_proximity[column].eq(expected).all():
            raise GridCoverageAssessmentError(
                f"Voltage proximity lineage does not match coverage: {column}"
            )


def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
    converted: list[float] = []
    for value in values.tolist():
        if not isinstance(value, Real) or isinstance(value, bool):
            raise GridCoverageAssessmentError(f"{label} must be numeric")
        try:
            numeric = float(value)
        except (OverflowError, TypeError, ValueError) as error:
            raise GridCoverageAssessmentError(f"{label} must be finite") from error
        if not isfinite(numeric) or numeric < 0:
            raise GridCoverageAssessmentError(
                f"{label} must be finite and non-negative"
            )
        converted.append(numeric)
    return np.asarray(converted, dtype="float64")


def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    fully_covered: np.ndarray,
) -> pd.Series:
    numeric = distances.to_numpy(dtype="float64", na_value=np.nan)
    matched = ~np.isnan(numeric)
    statuses = np.full(len(distances), "NO_MATCH", dtype=object)
    outside = matched & ~fully_covered
    statuses[outside] = "OUTSIDE_OR_CROSSING_COVERAGE"
    internal = matched & fully_covered
    statuses[internal & (numeric < boundary_distances)] = "NOT_BOUNDARY_LIMITED"
    statuses[internal & (numeric >= boundary_distances)] = "BOUNDARY_LIMITED"
    return pd.Series(statuses, index=distances.index, dtype="object")


def _preserves_original_frame(
    original: pd.DataFrame,
    output: pd.DataFrame,
    added_columns: set[str],
    label: str,
) -> None:
    original_columns = tuple(str(column) for column in original.columns)
    if set(output.columns) != set(original_columns) | added_columns:
        raise GridCoverageAssessmentError(f"{label} output schema is inconsistent")
    for column in original_columns:
        if column == "geometry":
            continue
        if not original[column].equals(output[column]):
            raise GridCoverageAssessmentError(
                f"{label} changed original proximity column: {column}"
            )


def _validate_assessment_result(result: GridCoverageAssessmentResult) -> None:
    profile_grid_proximity(
        GridProximityResult(
            parcels=result.parcels,
            voltage_level_proximity=result.voltage_level_proximity,
            voltage_level_coverage=result.voltage_level_coverage,
        )
    )
    _validate_source_coverage(result.source_coverage)
    parcels = result.parcels
    table = result.voltage_level_proximity
    parcel_missing = (
        set(PARCEL_DIAGNOSTIC_COLUMNS)
        | set(COVERAGE_LINEAGE_COLUMNS)
    ) - set(parcels.columns)
    table_missing = (
        set(VOLTAGE_DIAGNOSTIC_COLUMNS)
        | set(COVERAGE_LINEAGE_COLUMNS)
    ) - set(table.columns)
    if parcel_missing or table_missing:
        raise GridCoverageAssessmentError("Coverage diagnostic columns are missing")
    boundary_distances = _finite_nonnegative(
        parcels["grid_source_boundary_distance_m"],
        "Grid source boundary distance",
    )
    position = parcels["grid_source_coverage_position"]
    if position.isna().any() or not set(position.unique()) <= COVERAGE_POSITIONS:
        raise GridCoverageAssessmentError("Coverage position values are invalid")
    fully_covered = position.eq("FULLY_COVERED").to_numpy(dtype="bool")
    for distance_column, status_column in (
        ("nearest_line_proxy_distance_m", "nearest_line_coverage_status"),
        (
            "nearest_exact_line_proxy_distance_m",
            "nearest_exact_line_coverage_status",
        ),
        ("nearest_post_proxy_distance_m", "nearest_post_coverage_status"),
    ):
        expected = _coverage_statuses(
            parcels[distance_column], boundary_distances, fully_covered
        )
        actual_status = parcels[status_column].astype("object").reset_index(drop=True)
        expected_status = expected.astype("object").reset_index(drop=True)
        if not actual_status.equals(expected_status):
            raise GridCoverageAssessmentError(
                f"Coverage status is inconsistent: {status_column}"
            )
    boundary_by_id = dict(
        zip(parcels["parcel_id"], boundary_distances, strict=True)
    )
    fully_by_id = dict(zip(parcels["parcel_id"], fully_covered, strict=True))
    table_boundary = table["parcel_id"].map(boundary_by_id).astype("float64")
    if not table["source_boundary_distance_m"].equals(table_boundary):
        raise GridCoverageAssessmentError(
            "Voltage boundary distances do not match parcel diagnostics"
        )
    table_fully = table["parcel_id"].map(fully_by_id).to_numpy(dtype="bool")
    expected_table_status = _coverage_statuses(
        table["nearest_line_proxy_distance_m"],
        table_boundary.to_numpy(dtype="float64"),
        table_fully,
    )
    actual_table_status = table["coverage_status"].astype("object").reset_index(
        drop=True
    )
    expected_table_status = expected_table_status.astype("object").reset_index(
        drop=True
    )
    if not actual_table_status.equals(expected_table_status):
        raise GridCoverageAssessmentError(
            "Voltage coverage statuses are inconsistent"
        )
    lineage = _coverage_lineage_values(result.source_coverage)
    for column, expected in lineage.items():
        for frame in (parcels, table):
            values = frame[column]
            if expected is None:
                valid = values.isna().all()
            else:
                valid = values.eq(expected).all()
            if not valid:
                raise GridCoverageAssessmentError(
                    f"Coverage diagnostic lineage is inconsistent: {column}"
                )


def assess_grid_coverage(
    proximity_result: GridProximityResult,
    department_coverage: IgnBdTopoDepartmentCoverage,
) -> GridCoverageAssessmentResult:
    """Classify proximity results against one loaded department boundary.

    All geometry operations use planar XY copies in EPSG:2154. A parcel that
    touches or crosses the source boundary is handled conservatively as not
    fully covered. No parcel, proximity match, or source geometry is mutated.
    """

    profile_grid_proximity(proximity_result)
    coverage_frame = _validate_source_coverage(department_coverage)
    _validate_proximity_source_identity(proximity_result, department_coverage)

    source_parcels = proximity_result.parcels
    source_table = proximity_result.voltage_level_proximity
    output_parcels = source_parcels.copy()
    output_table = source_table.copy()

    calculation_parcels = source_parcels.to_crs(CALCULATION_CRS)
    parcel_geometries = np.asarray(
        force_2d(np.asarray(calculation_parcels.geometry.array, dtype=object)),
        dtype=object,
    )
    coverage_geometry = force_2d(coverage_frame.geometry.iloc[0])
    coverage_boundary = boundary(coverage_geometry)
    covered = np.asarray(covers(coverage_geometry, parcel_geometries), dtype="bool")
    touches_boundary = np.asarray(
        intersects(parcel_geometries, coverage_boundary), dtype="bool"
    )
    fully_covered = covered & ~touches_boundary
    measured_boundary = np.asarray(
        distance(parcel_geometries, coverage_boundary), dtype="float64"
    )
    if not np.isfinite(measured_boundary).all() or (measured_boundary < 0).any():
        raise GridCoverageAssessmentError(
            "Calculated coverage boundary distances must be finite and non-negative"
        )
    boundary_distances = np.where(fully_covered, measured_boundary, 0.0)

    output_parcels["grid_source_boundary_distance_m"] = boundary_distances
    output_parcels["grid_source_coverage_position"] = np.where(
        fully_covered,
        "FULLY_COVERED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
    )
    output_parcels["nearest_line_coverage_status"] = _coverage_statuses(
        output_parcels["nearest_line_proxy_distance_m"],
        boundary_distances,
        fully_covered,
    )
    output_parcels["nearest_exact_line_coverage_status"] = _coverage_statuses(
        output_parcels["nearest_exact_line_proxy_distance_m"],
        boundary_distances,
        fully_covered,
    )
    output_parcels["nearest_post_coverage_status"] = _coverage_statuses(
        output_parcels["nearest_post_proxy_distance_m"],
        boundary_distances,
        fully_covered,
    )

    boundary_by_id = dict(
        zip(output_parcels["parcel_id"], boundary_distances, strict=True)
    )
    covered_by_id = dict(
        zip(output_parcels["parcel_id"], fully_covered, strict=True)
    )
    output_table["source_boundary_distance_m"] = (
        output_table["parcel_id"].map(boundary_by_id).astype("float64")
    )
    table_fully_covered = output_table["parcel_id"].map(covered_by_id).to_numpy(
        dtype="bool"
    )
    output_table["coverage_status"] = _coverage_statuses(
        output_table["nearest_line_proxy_distance_m"],
        output_table["source_boundary_distance_m"].to_numpy(dtype="float64"),
        table_fully_covered,
    )
    lineage = _coverage_lineage_values(department_coverage)
    for column, value in lineage.items():
        output_parcels[column] = value
        output_table[column] = value

    _preserves_original_frame(
        source_parcels,
        output_parcels,
        set(PARCEL_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS),
        "Parcel proximity",
    )
    _preserves_original_frame(
        source_table,
        output_table,
        set(VOLTAGE_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS),
        "Voltage proximity",
    )
    if not output_parcels.geometry.geom_equals_exact(
        source_parcels.geometry, tolerance=0, align=False
    ).all():
        raise GridCoverageAssessmentError("Coverage assessment changed parcel geometry")
    if output_parcels.crs is None or source_parcels.crs is None:
        raise GridCoverageAssessmentError("Parcel CRS is required")
    if not CRS.from_user_input(output_parcels.crs).equals(
        CRS.from_user_input(source_parcels.crs)
    ):
        raise GridCoverageAssessmentError("Coverage assessment changed parcel CRS")

    result = GridCoverageAssessmentResult(
        parcels=output_parcels,
        voltage_level_proximity=output_table,
        voltage_level_coverage=proximity_result.voltage_level_coverage,
        source_coverage=department_coverage,
    )
    _validate_assessment_result(result)
    return result


def _status_counts(values: pd.Series) -> CoverageStatusCounts:
    counts = values.value_counts()
    return CoverageStatusCounts(
        not_boundary_limited=int(counts.get("NOT_BOUNDARY_LIMITED", 0)),
        boundary_limited=int(counts.get("BOUNDARY_LIMITED", 0)),
        outside_or_crossing_coverage=int(
            counts.get("OUTSIDE_OR_CROSSING_COVERAGE", 0)
        ),
        no_match=int(counts.get("NO_MATCH", 0)),
    )


def _boundary_profile(values: pd.Series) -> BoundaryDistanceProfile:
    numeric = _finite_nonnegative(values, "Grid source boundary distance")
    if len(numeric) == 0:
        raise GridCoverageAssessmentError(
            "Cannot profile an empty parcel coverage assessment"
        )
    series = pd.Series(numeric, dtype="float64")
    return BoundaryDistanceProfile(
        count=len(series),
        minimum=float(series.min()),
        p01=float(series.quantile(0.01)),
        p05=float(series.quantile(0.05)),
        p10=float(series.quantile(0.10)),
        p25=float(series.quantile(0.25)),
        p50=float(series.quantile(0.50)),
        p75=float(series.quantile(0.75)),
        p90=float(series.quantile(0.90)),
        p95=float(series.quantile(0.95)),
        p99=float(series.quantile(0.99)),
        maximum=float(series.max()),
    )


def profile_grid_coverage(
    result: GridCoverageAssessmentResult,
) -> GridCoverageProfile:
    """Summarize boundary diagnostics without suitability thresholds."""

    _validate_assessment_result(result)
    parcels = result.parcels
    position_counts = parcels["grid_source_coverage_position"].value_counts()
    voltage_profiles: list[VoltageCoverageStatusProfile] = []
    for item in result.voltage_level_coverage:
        rows = result.voltage_level_proximity.loc[
            result.voltage_level_proximity["voltage_kv"] == item.voltage_kv
        ]
        voltage_profiles.append(
            VoltageCoverageStatusProfile(
                voltage_kv=float(item.voltage_kv),
                parcel_count=len(rows),
                statuses=_status_counts(rows["coverage_status"]),
            )
        )
    return GridCoverageProfile(
        parcel_count=len(parcels),
        fully_covered_count=int(position_counts.get("FULLY_COVERED", 0)),
        outside_or_crossing_count=int(
            position_counts.get("OUTSIDE_OR_CROSSING_COVERAGE", 0)
        ),
        boundary_distance=_boundary_profile(
            parcels["grid_source_boundary_distance_m"]
        ),
        nearest_line=_status_counts(parcels["nearest_line_coverage_status"]),
        nearest_exact_line=_status_counts(
            parcels["nearest_exact_line_coverage_status"]
        ),
        nearest_post=_status_counts(parcels["nearest_post_coverage_status"]),
        voltage_levels=tuple(voltage_profiles),
    )
