"""Diagnose road proximity against one verified IGN package boundary."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from math import isfinite
from numbers import Integral, Real
from pathlib import Path

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

from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)
from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)
from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)

__all__ = [
    "RoadProximityCoverageAssessmentResult",
    "RoadProximityCoverageError",
    "assess_road_proximity_coverage",
]

_CALCULATION_CRS = "EPSG:2154"
_PROXIMITY_SCOPE = "WITHIN_VERIFIED_SOURCE_PACKAGE"
_COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"
_SOURCE_SPATIAL_ROLE = "PROXY_GEOMETRY"
_POSITIONS = frozenset(
    {"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"}
)
_STATUSES = frozenset(
    {
        "NO_MATCH",
        "NOT_BOUNDARY_LIMITED",
        "BOUNDARY_LIMITED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
    }
)
_PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
_COVERAGE_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institutnationaldelinformationgeographiqueetforestiereign",
    }
)
_COVERAGE_LINEAGE_COLUMNS = (
    "road_source_coverage_provider",
    "road_source_coverage_product",
    "road_source_coverage_department_code",
    "road_source_coverage_edition",
    "road_source_coverage_product_version",
    "road_source_coverage_archive_sha256",
    "road_source_coverage_layer",
    "road_source_coverage_spatial_role",
)
_DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
    *_COVERAGE_LINEAGE_COLUMNS,
)
_COVERAGE_FRAME_LINEAGE = (
    "source_provider",
    "source_product",
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_archive_sha256",
    "source_layer",
    "spatial_role",
)
_SELECTED_ROAD_COLUMNS = (
    "nearest_road_feature_id",
    "nearest_source_feature_id",
    "nearest_road_tie_count",
    "nearest_road_primary_rule",
    "nearest_road_rule_trace_json",
    "nearest_road_unknown_fields_json",
    "nearest_road_toll_evidence",
    "nearest_nature_raw",
    "nearest_importance_raw",
    "nearest_asset_status_raw",
    "nearest_private_raw",
    "nearest_light_vehicle_access_raw",
    "nearest_carriageway_width_raw",
    "nearest_closure_period_raw",
    "nearest_restriction_nature_raw",
    "nearest_source_layer",
    "nearest_source_department_code",
    "nearest_source_edition",
    "nearest_source_archive_sha256",
)


class RoadProximityCoverageError(ValueError):
    """Raised when road source-boundary diagnostics cannot be proven safely."""


@dataclass(frozen=True)
class RoadProximityCoverageAssessmentResult:
    """Unchanged road proximity plus its source-package boundary diagnosis."""

    parcels: gpd.GeoDataFrame
    class_proximity: pd.DataFrame
    class_coverage: tuple[RoadProxyClassCoverage, ...]
    source_coverage: IgnBdTopoDepartmentCoverage


def _validated_crs(value: object, expected_epsg: int, label: str) -> CRS:
    if value is None:
        raise RoadProximityCoverageError(f"{label} CRS is required")
    try:
        actual = CRS.from_user_input(value)
    except Exception as error:
        raise RoadProximityCoverageError(f"{label} CRS is unreadable") from error
    expected = CRS.from_epsg(expected_epsg)
    if not actual.equals(expected):
        raise RoadProximityCoverageError(
            f"{label} must use EPSG:{expected_epsg}"
        )
    return actual


def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise RoadProximityCoverageError(
            f"{label} must be a non-empty exact string"
        )
    decomposed = unicodedata.normalize("NFKD", value)
    return "".join(
        character
        for character in decomposed.casefold()
        if character.isalnum()
    )


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise RoadProximityCoverageError(
            f"{label} must be a non-empty exact string"
        )
    return value


def _null_safe_scalar_equal(actual: object, expected: object) -> bool:
    if expected is None:
        return bool(pd.isna(actual))
    try:
        return bool(actual == expected)
    except (TypeError, ValueError):
        return False


def _exact_ids(values: pd.Series, label: str) -> None:
    if values.isna().any():
        raise RoadProximityCoverageError(f"{label} values must not be null")
    items = values.tolist()
    if any(not isinstance(item, str) for item in items):
        raise RoadProximityCoverageError(f"{label} values must be exact strings")
    if any(not item or item != item.strip() for item in items):
        raise RoadProximityCoverageError(
            f"{label} values must be non-empty without edge whitespace"
        )
    if values.duplicated().any():
        raise RoadProximityCoverageError(f"{label} values must be unique")


def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
    if not isinstance(frame, gpd.GeoDataFrame):
        raise RoadProximityCoverageError(f"{label} must be a GeoDataFrame")
    if frame.columns.duplicated().any():
        raise RoadProximityCoverageError(f"{label} columns must be unique")
    missing = {"parcel_id", "geometry"} - set(frame.columns)
    if missing:
        raise RoadProximityCoverageError(
            f"{label} is missing: " + ", ".join(sorted(missing))
        )
    if frame.active_geometry_name != "geometry":
        raise RoadProximityCoverageError(f"{label} geometry must be active")
    _validated_crs(frame.crs, 4326, label)
    _exact_ids(frame["parcel_id"], f"{label} parcel_id")
    geometry = frame.geometry
    if geometry.isna().any():
        raise RoadProximityCoverageError(f"{label} geometry must not be null")
    if geometry.is_empty.any():
        raise RoadProximityCoverageError(f"{label} geometry must not be empty")
    if not geometry.is_valid.all():
        raise RoadProximityCoverageError(f"{label} geometry must be valid")
    if not set(geometry.geom_type.dropna()) <= _PARCEL_GEOMETRY_TYPES:
        raise RoadProximityCoverageError(
            f"{label} geometry must be Polygon or MultiPolygon"
        )
    return frame


def _same_index(left: pd.Index, right: pd.Index) -> bool:
    return bool(
        type(left) is type(right)
        and left.names == right.names
        and str(left.dtype) == str(right.dtype)
        and left.equals(right)
    )


def _require_same_parcels(
    expected: gpd.GeoDataFrame,
    actual: gpd.GeoDataFrame,
    label: str,
) -> None:
    if list(actual.columns) != list(expected.columns):
        raise RoadProximityCoverageError(f"{label} parcel columns changed")
    if not actual.dtypes.equals(expected.dtypes):
        raise RoadProximityCoverageError(f"{label} parcel dtypes changed")
    if not _same_index(actual.index, expected.index):
        raise RoadProximityCoverageError(f"{label} parcel index changed")
    if not _validated_crs(actual.crs, 4326, label).equals(
        _validated_crs(expected.crs, 4326, label)
    ):
        raise RoadProximityCoverageError(f"{label} parcel CRS changed")
    if not actual.geometry.to_wkb().equals(expected.geometry.to_wkb()):
        raise RoadProximityCoverageError(f"{label} parcel geometry changed")
    if not actual.drop(columns="geometry").equals(
        expected.drop(columns="geometry")
    ):
        raise RoadProximityCoverageError(f"{label} parcel facts changed")


def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
    converted: list[float] = []
    for value in values.tolist():
        if not isinstance(value, Real) or isinstance(value, (bool, np.bool_)):
            raise RoadProximityCoverageError(f"{label} must be numeric")
        numeric = float(value)
        if not isfinite(numeric) or numeric < 0:
            raise RoadProximityCoverageError(
                f"{label} must be finite and non-negative"
            )
        converted.append(numeric)
    return np.asarray(converted, dtype="float64")


def _validate_class_coverage(
    coverage: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
    classes = policy.classes.values
    eligible = tuple(
        road_class
        for road_class in classes
        if road_class != policy.classes.not_distance_proxy
    )
    if type(coverage) is not tuple or len(coverage) != len(classes):
        raise RoadProximityCoverageError("Road class coverage is invalid")
    for position, item in enumerate(coverage):
        if type(item) is not RoadProxyClassCoverage:
            raise RoadProximityCoverageError("Road class coverage type is invalid")
        if item.road_proxy_class != classes[position]:
            raise RoadProximityCoverageError("Road class coverage order is invalid")
        if type(item.feature_count) is not int or item.feature_count < 0:
            raise RoadProximityCoverageError(
                "Road class coverage feature_count is invalid"
            )
        if type(item.distance_eligible) is not bool or (
            item.distance_eligible != (item.road_proxy_class in eligible)
        ):
            raise RoadProximityCoverageError(
                "Road class coverage distance eligibility is invalid"
            )
    return eligible


def _validate_match_rows(
    table: pd.DataFrame,
    coverage: tuple[RoadProxyClassCoverage, ...],
) -> None:
    by_class = {item.road_proxy_class: item for item in coverage}
    for road_class, item in by_class.items():
        if not item.distance_eligible:
            continue
        rows = table.loc[table["road_proxy_class"].eq(road_class)]
        matched = rows["nearest_road_proxy_distance_m"].notna()
        if item.feature_count == 0:
            if matched.any() or rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any().any():
                raise RoadProximityCoverageError(
                    "Empty road class contains selected road evidence"
                )
            continue
        if not matched.all():
            raise RoadProximityCoverageError(
                "Non-empty road class is missing a parcel match"
            )
        _finite_nonnegative(
            rows["nearest_road_proxy_distance_m"], "Nearest road distance"
        )
        required = (
            "nearest_road_feature_id",
            "nearest_source_feature_id",
            "nearest_road_tie_count",
            "nearest_road_primary_rule",
            "nearest_road_rule_trace_json",
            "nearest_road_unknown_fields_json",
            "nearest_road_toll_evidence",
            "nearest_source_layer",
            "nearest_source_department_code",
            "nearest_source_edition",
            "nearest_source_archive_sha256",
        )
        if rows.loc[:, list(required)].isna().any().any():
            raise RoadProximityCoverageError(
                "Matched road evidence is incomplete"
            )
        for value in rows["nearest_road_tie_count"].tolist():
            if (
                not isinstance(value, Integral)
                or isinstance(value, (bool, np.bool_))
                or int(value) < 1
            ):
                raise RoadProximityCoverageError(
                    "Nearest road tie count must be an integer >= 1"
                )


def _validate_upstream_result(
    input_parcels: gpd.GeoDataFrame,
    result: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> ParcelRoadProximityResult:
    if type(result) is not ParcelRoadProximityResult:
        raise RoadProximityCoverageError("Road proximity result type is invalid")
    parcels = _validate_parcel_frame(result.parcels, "Road proximity parcels")
    _require_same_parcels(input_parcels, parcels, "Road proximity")
    eligible = _validate_class_coverage(result.class_coverage, policy)
    table = result.class_proximity
    if type(table) is not pd.DataFrame:
        raise RoadProximityCoverageError("Class proximity must be a plain DataFrame")
    if table.columns.duplicated().any() or tuple(table.columns) != CLASS_PROXIMITY_COLUMNS:
        raise RoadProximityCoverageError("Class proximity schema is invalid")
    if not isinstance(table.index, pd.RangeIndex) or (
        table.index.start != 0
        or table.index.step != 1
        or table.index.name is not None
    ):
        raise RoadProximityCoverageError("Class proximity index is invalid")
    if len(table) != len(parcels) * len(eligible):
        raise RoadProximityCoverageError("Class proximity row count is invalid")
    expected_ids = [
        parcel_id
        for parcel_id in parcels["parcel_id"].tolist()
        for _ in eligible
    ]
    expected_classes = list(eligible) * len(parcels)
    if table["parcel_id"].tolist() != expected_ids:
        raise RoadProximityCoverageError("Class proximity parcel order is invalid")
    if table["road_proxy_class"].tolist() != expected_classes:
        raise RoadProximityCoverageError("Class proximity class order is invalid")
    if table.duplicated(["parcel_id", "road_proxy_class"]).any():
        raise RoadProximityCoverageError("Class proximity pairs are duplicated")
    expected_lineage = {
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
        "proximity_scope": _PROXIMITY_SCOPE,
    }
    for column, expected in expected_lineage.items():
        if table[column].isna().any() or not table[column].eq(expected).all():
            raise RoadProximityCoverageError(
                f"Class proximity policy lineage is invalid: {column}"
            )
    _validate_match_rows(table, result.class_coverage)
    return result


def _validate_coverage_summary(
    coverage: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
    config: IgnBdTopoSourceConfig,
) -> None:
    summary = coverage.summary
    if type(summary) is not IgnBdTopoCoverageLayerSummary:
        raise RoadProximityCoverageError("Coverage summary type is invalid")
    if summary.source_layer_name != coverage.source_layer:
        raise RoadProximityCoverageError("Coverage summary layer is invalid")
    _validated_crs(summary.crs, 2154, "Coverage summary")
    if type(summary.selected_feature_count) is not int or (
        summary.selected_feature_count != len(frame)
    ):
        raise RoadProximityCoverageError("Coverage selected feature count is invalid")
    if (
        type(summary.source_feature_count) is not int
        or summary.source_feature_count < summary.selected_feature_count
    ):
        raise RoadProximityCoverageError("Coverage source feature count is invalid")
    if (
        type(summary.columns) is not tuple
        or not summary.columns
        or len(set(summary.columns)) != len(summary.columns)
        or any(
            not isinstance(column, str)
            or not column
            or column != column.strip()
            for column in summary.columns
        )
    ):
        raise RoadProximityCoverageError("Coverage summary columns are invalid")
    if tuple(frame.columns) != (*summary.columns, *_COVERAGE_FRAME_LINEAGE):
        raise RoadProximityCoverageError("Coverage frame schema is invalid")
    expected_dtypes = tuple(
        (column, str(frame[column].dtype)) for column in summary.columns
    )
    if type(summary.dtypes) is not tuple or summary.dtypes != expected_dtypes:
        raise RoadProximityCoverageError("Coverage summary dtypes are invalid")
    expected_field = config.coverage.department_layer.department_code_field
    if summary.department_code_field != expected_field:
        raise RoadProximityCoverageError(
            "Coverage configured department field is invalid"
        )
    if summary.selected_department_code != coverage.source_department_code:
        raise RoadProximityCoverageError("Coverage selected department is invalid")
    if not frame[expected_field].eq(coverage.source_department_code).all():
        raise RoadProximityCoverageError("Coverage department identity is invalid")
    if summary.spatial_role != _COVERAGE_SPATIAL_ROLE:
        raise RoadProximityCoverageError("Coverage summary spatial role is invalid")


def _validate_source_coverage(
    source: object,
    road_source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> tuple[IgnBdTopoDepartmentCoverage, gpd.GeoDataFrame]:
    if type(source) is not IgnBdTopoDepartmentCoverage:
        raise RoadProximityCoverageError("Coverage source type is invalid")
    if source.extraction is not road_source.extraction:
        raise RoadProximityCoverageError(
            "Coverage must retain the exact road extraction identity"
        )
    archive = road_source.extraction.archive
    if road_source.extraction.spatial_role != _SOURCE_SPATIAL_ROLE or (
        archive.spatial_role != _SOURCE_SPATIAL_ROLE
    ):
        raise RoadProximityCoverageError("Road package spatial role is invalid")
    _validated_crs(archive.projection, 2154, "Road package")
    provider_identity = _normalized_identity(archive.provider, "Road provider")
    product_identity = _normalized_identity(archive.product, "Road product")
    if provider_identity not in _IGN_PROVIDER_IDENTITIES:
        raise RoadProximityCoverageError("Road package provider is not IGN")
    if product_identity != "bdtopo":
        raise RoadProximityCoverageError("Road package product is not BD TOPO")
    if provider_identity != _normalized_identity(config.provider, "Config provider"):
        raise RoadProximityCoverageError("Road package provider differs from config")
    if product_identity != _normalized_identity(config.product, "Config product"):
        raise RoadProximityCoverageError("Road package product differs from config")
    if archive.department_code != config.department_code:
        raise RoadProximityCoverageError("Road package department differs from config")
    if _SHA256_PATTERN.fullmatch(archive.sha256) is None:
        raise RoadProximityCoverageError("Road package archive SHA256 is invalid")
    expected_layer = _discover_department_coverage_layer(
        road_source.extraction.all_layer_names, config
    )
    if source.source_layer != expected_layer:
        raise RoadProximityCoverageError(
            "Coverage does not use the configured physical layer"
        )
    expected_scalars = {
        "source_provider": archive.provider,
        "source_product": archive.product,
        "source_department_code": archive.department_code,
        "source_edition": archive.edition,
        "source_product_version": archive.product_version,
        "source_archive_sha256": archive.sha256,
        "source_layer": expected_layer,
        "spatial_role": _COVERAGE_SPATIAL_ROLE,
    }
    for name, expected in expected_scalars.items():
        if not _null_safe_scalar_equal(getattr(source, name), expected):
            raise RoadProximityCoverageError(
                f"Coverage package lineage is invalid: {name}"
            )
    if _normalized_identity(source.source_provider, "Coverage provider") not in (
        _IGN_PROVIDER_IDENTITIES
    ):
        raise RoadProximityCoverageError("Coverage provider is not IGN")
    if _normalized_identity(source.source_product, "Coverage product") != "bdtopo":
        raise RoadProximityCoverageError("Coverage product is not BD TOPO")
    if _SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None:
        raise RoadProximityCoverageError("Coverage archive SHA256 is invalid")

    frame = source.coverage
    if not isinstance(frame, gpd.GeoDataFrame):
        raise RoadProximityCoverageError("Coverage must be a GeoDataFrame")
    if frame.columns.duplicated().any():
        raise RoadProximityCoverageError("Coverage columns must be unique")
    if "geometry" not in frame.columns or frame.active_geometry_name != "geometry":
        raise RoadProximityCoverageError("Coverage geometry must exist and be active")
    _validated_crs(frame.crs, 2154, "Coverage")
    if len(frame) != 1:
        raise RoadProximityCoverageError(
            "Coverage must contain exactly one selected feature"
        )
    geometry = frame.geometry
    if geometry.isna().any():
        raise RoadProximityCoverageError("Coverage geometry must not be null")
    if geometry.is_empty.any():
        raise RoadProximityCoverageError("Coverage geometry must not be empty")
    if not geometry.is_valid.all():
        raise RoadProximityCoverageError("Coverage geometry must be valid")
    if not set(geometry.geom_type.dropna()) <= _COVERAGE_GEOMETRY_TYPES:
        raise RoadProximityCoverageError(
            "Coverage geometry must be Polygon or MultiPolygon"
        )
    _validate_coverage_summary(source, frame, config)
    for column, expected in expected_scalars.items():
        actual = frame.iloc[0][column]
        if not _null_safe_scalar_equal(actual, expected):
            raise RoadProximityCoverageError(
                f"Coverage row lineage is invalid: {column}"
            )
    return source, frame


def _coverage_lineage(
    coverage: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
    return {
        "road_source_coverage_provider": coverage.source_provider,
        "road_source_coverage_product": coverage.source_product,
        "road_source_coverage_department_code": coverage.source_department_code,
        "road_source_coverage_edition": coverage.source_edition,
        "road_source_coverage_product_version": coverage.source_product_version,
        "road_source_coverage_archive_sha256": coverage.source_archive_sha256,
        "road_source_coverage_layer": coverage.source_layer,
        "road_source_coverage_spatial_role": coverage.spatial_role,
    }


def _parcel_coverage_diagnostics(
    parcels: gpd.GeoDataFrame,
    coverage_frame: gpd.GeoDataFrame,
) -> tuple[np.ndarray, np.ndarray]:
    calculation = parcels.to_crs(_CALCULATION_CRS)
    parcel_geometries = np.asarray(
        force_2d(np.asarray(calculation.geometry.array, dtype=object)),
        dtype=object,
    )
    coverage_geometry = force_2d(coverage_frame.geometry.iloc[0])
    coverage_boundary = boundary(coverage_geometry)
    covered = np.asarray(covers(coverage_geometry, parcel_geometries), dtype="bool")
    boundary_contact = np.asarray(
        intersects(parcel_geometries, coverage_boundary), dtype="bool"
    )
    fully_covered = covered & ~boundary_contact
    measured = np.asarray(
        distance(parcel_geometries, coverage_boundary), dtype="float64"
    )
    if not np.isfinite(measured).all() or (measured < 0).any():
        raise RoadProximityCoverageError(
            "Calculated boundary distances must be finite and non-negative"
        )
    boundary_distances = np.where(fully_covered, measured, 0.0)
    positions = np.where(
        fully_covered,
        "FULLY_COVERED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
    )
    return boundary_distances, positions


def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
) -> np.ndarray:
    numeric = distances.to_numpy(dtype="float64", na_value=np.nan)
    matched = ~np.isnan(numeric)
    fully_covered = positions == "FULLY_COVERED"
    statuses = np.full(len(distances), "NO_MATCH", dtype=object)
    outside = matched & ~fully_covered
    statuses[outside] = "OUTSIDE_OR_CROSSING_COVERAGE"
    internal = matched & fully_covered
    statuses[internal & (numeric < boundary_distances)] = "NOT_BOUNDARY_LIMITED"
    statuses[internal & (numeric >= boundary_distances)] = "BOUNDARY_LIMITED"
    return statuses


def _expected_diagnostics(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
    boundary_by_id = dict(
        zip(parcels["parcel_id"], boundary_distances, strict=True)
    )
    position_by_id = dict(zip(parcels["parcel_id"], positions, strict=True))
    row_boundary = table["parcel_id"].map(boundary_by_id).astype("float64")
    row_positions = table["parcel_id"].map(position_by_id)
    output = pd.DataFrame(index=table.index.copy())
    output["road_source_boundary_distance_m"] = row_boundary
    output["road_source_coverage_position"] = row_positions
    output["road_proximity_coverage_status"] = _coverage_statuses(
        table["nearest_road_proxy_distance_m"],
        row_boundary.to_numpy(dtype="float64"),
        row_positions.to_numpy(dtype=object),
    )
    for column, value in _coverage_lineage(coverage).items():
        output[column] = value
    return output.loc[:, list(_DIAGNOSTIC_COLUMNS)]


def _diagnosed_class_proximity(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
    output = table.copy(deep=True)
    diagnostics = _expected_diagnostics(
        table, parcels, boundary_distances, positions, coverage
    )
    for column in _DIAGNOSTIC_COLUMNS:
        output[column] = diagnostics[column]
    return output


def _validate_selected_road_package(
    table: pd.DataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> None:
    matched = table["nearest_road_proxy_distance_m"].notna()
    expected = {
        "nearest_source_department_code": coverage.source_department_code,
        "nearest_source_edition": coverage.source_edition,
        "nearest_source_archive_sha256": coverage.source_archive_sha256,
    }
    for column, value in expected.items():
        selected = table.loc[matched, column]
        if selected.isna().any() or not selected.eq(value).all():
            raise RoadProximityCoverageError(
                f"Selected road package lineage differs from coverage: {column}"
            )


def _validate_assessment_result(
    input_parcels: gpd.GeoDataFrame,
    proximity: ParcelRoadProximityResult,
    road_source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
    loaded_coverage: IgnBdTopoDepartmentCoverage,
    result: object,
) -> None:
    if type(result) is not RoadProximityCoverageAssessmentResult:
        raise RoadProximityCoverageError("Coverage assessment result type is invalid")
    if result.source_coverage is not loaded_coverage:
        raise RoadProximityCoverageError("Coverage assessment source was not preserved")
    coverage, coverage_frame = _validate_source_coverage(
        result.source_coverage, road_source, config
    )
    _validate_parcel_frame(result.parcels, "Coverage result parcels")
    _require_same_parcels(input_parcels, result.parcels, "Coverage result")
    _require_same_parcels(proximity.parcels, result.parcels, "Coverage result")
    if result.class_coverage is not proximity.class_coverage:
        raise RoadProximityCoverageError("Road class coverage was not preserved")
    output = result.class_proximity
    source = proximity.class_proximity
    if type(output) is not pd.DataFrame:
        raise RoadProximityCoverageError("Coverage class proximity is invalid")
    expected_columns = (*CLASS_PROXIMITY_COLUMNS, *_DIAGNOSTIC_COLUMNS)
    if output.columns.duplicated().any() or tuple(output.columns) != expected_columns:
        raise RoadProximityCoverageError(
            "Coverage class proximity schema is invalid"
        )
    if not _same_index(output.index, source.index):
        raise RoadProximityCoverageError("Coverage class proximity index changed")
    prefix = output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]
    if not prefix.dtypes.equals(source.dtypes) or not prefix.equals(source):
        raise RoadProximityCoverageError(
            "Coverage assessment changed original class proximity facts"
        )
    boundary_distances, positions = _parcel_coverage_diagnostics(
        proximity.parcels, coverage_frame
    )
    expected = _expected_diagnostics(
        source, proximity.parcels, boundary_distances, positions, coverage
    )
    actual = output.loc[:, list(_DIAGNOSTIC_COLUMNS)]
    if not actual.dtypes.equals(expected.dtypes) or not actual.equals(expected):
        raise RoadProximityCoverageError(
            "Coverage diagnostics differ from geometric reconstruction"
        )
    numeric = _finite_nonnegative(
        output["road_source_boundary_distance_m"],
        "Road source boundary distance",
    )
    position_values = output["road_source_coverage_position"]
    if position_values.isna().any() or not set(position_values.unique()) <= _POSITIONS:
        raise RoadProximityCoverageError("Coverage position is invalid")
    outside = position_values.eq("OUTSIDE_OR_CROSSING_COVERAGE").to_numpy(
        dtype="bool"
    )
    if (numeric[outside] != 0.0).any():
        raise RoadProximityCoverageError(
            "Outside or crossing rows require zero boundary distance"
        )
    statuses = output["road_proximity_coverage_status"]
    if statuses.isna().any() or not set(statuses.unique()) <= _STATUSES:
        raise RoadProximityCoverageError("Coverage status is invalid")
    _validate_selected_road_package(output, coverage)


def _assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> RoadProximityCoverageAssessmentResult:
    input_parcels = _validate_parcel_frame(parcels, "Input parcels")
    proximity = enrich_parcel_road_proximity(
        parcels, road_source, source_config, policy_path
    )
    policy = (
        load_ign_road_vehicle_proxy_policy()
        if policy_path is None
        else load_ign_road_vehicle_proxy_policy(policy_path)
    )
    validated_proximity = _validate_upstream_result(
        input_parcels, proximity, policy
    )
    coverage = load_ign_bdtopo_department_coverage(
        road_source.extraction, source_config
    )
    validated_coverage, coverage_frame = _validate_source_coverage(
        coverage, road_source, source_config
    )
    _validate_selected_road_package(
        validated_proximity.class_proximity, validated_coverage
    )
    boundary_distances, positions = _parcel_coverage_diagnostics(
        validated_proximity.parcels, coverage_frame
    )
    output_table = _diagnosed_class_proximity(
        validated_proximity.class_proximity,
        validated_proximity.parcels,
        boundary_distances,
        positions,
        validated_coverage,
    )
    result = RoadProximityCoverageAssessmentResult(
        parcels=validated_proximity.parcels.copy(deep=True),
        class_proximity=output_table,
        class_coverage=validated_proximity.class_coverage,
        source_coverage=validated_coverage,
    )
    _validate_assessment_result(
        input_parcels,
        validated_proximity,
        road_source,
        source_config,
        validated_coverage,
        result,
    )
    return result


def assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
    """Diagnose source-bound road proximity using the verified package boundary."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise RoadProximityCoverageError("parcels must be a GeoDataFrame")
        if type(road_source) is not IgnBdTopoRoadData:
            raise RoadProximityCoverageError(
                "road_source must be an IgnBdTopoRoadData"
            )
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise RoadProximityCoverageError(
                "source_config must be an IgnBdTopoSourceConfig"
            )
        if policy_path is not None and not isinstance(policy_path, Path):
            raise RoadProximityCoverageError(
                "policy_path must be a pathlib.Path or None"
            )
        return _assess_road_proximity_coverage(
            parcels, road_source, source_config, policy_path
        )
    except RoadProximityCoverageError:
        raise
    except Exception as error:
        raise RoadProximityCoverageError(
            "Road proximity coverage cannot be assessed safely"
        ) from error
