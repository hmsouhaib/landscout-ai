"""Normalize official GPU zoning and intersect it with LandScout parcels.

This module records source zoning facts only.  It deliberately contains no
urban-planning interpretation, BESS compatibility policy, rejection, or score.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from numbers import Real

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import (  # type: ignore[import-untyped]
    area as shapely_area,
)
from shapely import (
    force_2d,
    union_all,
)
from shapely import (
    intersection as shapely_intersection,
)

from landscout.sources.gpu_fr import GpuPlanningDocument

__all__ = ["intersect_parcels_with_gpu_zoning"]

CALCULATION_CRS = "EPSG:2154"

# Centralized CNIG/GPU source schema for the zoning layer currently supported by
# this factual normalization stage.  Raw values are copied without rewriting.
GPU_ZONING_SOURCE_FIELDS = {
    "source_zone_id": "LIB_IDZONE",
    "zone_label_raw": "LIBELLE",
    "zone_long_label_raw": "LIBELONG",
    "zone_type_raw": "TYPEZONE",
    "regulation_filename_raw": "NOMFIC",
    "regulation_url_raw": "URLFIC",
    "source_document_reference_raw": "IDURBA",
    "source_validity_date_raw": "DATVALID",
}
GPU_ZONING_REQUIRED_COLUMNS = frozenset(
    {*GPU_ZONING_SOURCE_FIELDS.values(), "geometry"}
)
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
POLYGON_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
RELATION_TYPES = frozenset({"AREA_OVERLAP", "TOUCH_ONLY"})

PARCEL_ZONING_OUTPUT_COLUMNS = frozenset(
    {
        "zoning_area_match_count",
        "zoning_touch_only_count",
        "zoning_intersection_area_sum_m2",
        "zoning_covered_union_area_m2",
        "zoning_coverage_pct",
        "zoning_gap_area_m2",
        "zoning_overlap_excess_area_m2",
        "dominant_planning_zone_id",
        "dominant_source_zone_id",
        "dominant_zone_type_raw",
        "dominant_zone_label_raw",
        "dominant_zone_long_label_raw",
        "dominant_zone_intersection_area_m2",
        "dominant_zone_share_pct",
        "dominant_zone_tie_count",
        "planning_document_id",
        "planning_document_type",
        "planning_archive_name",
        "planning_archive_sha256",
        "planning_source_layer",
        "planning_standard_model",
    }
)

# A one-square-millimetre technical guard for floating-point overlay noise.  It
# is used only to stabilize impossible tiny negative differences after overlay;
# it is not a planning or BESS threshold.
_AREA_ABSOLUTE_TOLERANCE_M2 = 1e-6
_AREA_RELATIVE_TOLERANCE = 1e-12

INTERSECTION_COLUMNS = (
    "parcel_id",
    "planning_zone_id",
    "source_zone_id",
    "zone_type_raw",
    "zone_label_raw",
    "zone_long_label_raw",
    "relation_type",
    "parcel_metric_area_m2",
    "zone_area_m2",
    "intersection_area_m2",
    "parcel_share_pct",
    "zone_share_pct",
    "source_document_id",
    "source_archive_sha256",
    "source_layer",
    "source_validity_date_raw",
    "regulation_filename_raw",
)

_INTERSECTION_FLOAT_COLUMNS = frozenset(
    {
        "parcel_metric_area_m2",
        "zone_area_m2",
        "intersection_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
    }
)


class PlanningZoningError(ValueError):
    """Raised when factual zoning normalization cannot be completed safely."""


@dataclass(frozen=True)
class ParcelZoningResult:
    """Normalized zones, parcel facts, and long-form parcel/zone relations."""

    parcels: gpd.GeoDataFrame
    zones: gpd.GeoDataFrame
    intersections: pd.DataFrame


@dataclass(frozen=True)
class _PlanningContext:
    provider: str
    portal: str
    commune_code: str
    document_id: str
    document_type: str
    archive_name: str
    archive_sha256: str
    source_layer: str
    standard_model: str | None
    source_crs: str


def _strict_nonempty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningZoningError(f"{label} must be a non-empty exact string")
    return value


def _validate_exact_string_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise PlanningZoningError(f"{label} values must not be null")
    for value in values.tolist():
        _strict_nonempty_string(value, label)
    if require_unique and values.duplicated().any():
        raise PlanningZoningError(f"{label} values must be unique")


def _readable_crs(value: object, label: str) -> CRS:
    if value is None:
        raise PlanningZoningError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise PlanningZoningError(f"{label} CRS is unreadable") from error


def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise PlanningZoningError(f"{label} geometry column is required")
    try:
        active_name = frame.active_geometry_name
    except AttributeError as error:
        raise PlanningZoningError(f"{label} geometry column must be active") from error
    if active_name != "geometry":
        raise PlanningZoningError(f"{label} geometry column must be active")


def _validate_polygon_geometries(frame: gpd.GeoDataFrame, label: str) -> None:
    geometry = frame.geometry
    if geometry.isna().any():
        raise PlanningZoningError(f"{label} geometry must not be null")
    if geometry.is_empty.any():
        raise PlanningZoningError(f"{label} geometry must not be empty")
    if not geometry.is_valid.all():
        raise PlanningZoningError(f"{label} geometry must be valid")
    unexpected = sorted(set(geometry.geom_type) - POLYGON_GEOMETRY_TYPES)
    if unexpected:
        raise PlanningZoningError(
            f"{label} geometry must be Polygon or MultiPolygon; found: "
            + ", ".join(unexpected)
        )


def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise PlanningZoningError("Parcels must be a GeoDataFrame")
    missing = sorted(PARCEL_REQUIRED_COLUMNS - set(parcels.columns))
    if missing:
        raise PlanningZoningError(
            "Parcels are missing required columns: " + ", ".join(missing)
        )
    collisions = sorted(PARCEL_ZONING_OUTPUT_COLUMNS & set(parcels.columns))
    if collisions:
        raise PlanningZoningError(
            "Parcels already contain zoning output columns: "
            + ", ".join(collisions)
        )
    _active_geometry(parcels, "Parcel")
    crs = _readable_crs(parcels.crs, "Parcel")
    _validate_exact_string_ids(
        parcels["parcel_id"], "parcel_id", require_unique=True
    )
    _validate_polygon_geometries(parcels, "Parcel")
    return crs


def _standard_model(planning_document: GpuPlanningDocument) -> str | None:
    document_value = planning_document.extraction.archive.document.standard_model
    values: list[str] = []
    if document_value is not None:
        values.append(_strict_nonempty_string(document_value, "GPU standard model"))
    for value in planning_document.extraction.standard_models:
        validated = _strict_nonempty_string(value, "GPU extracted standard model")
        if validated not in values:
            values.append(validated)
    if not values:
        return None
    if len(values) != 1:
        raise PlanningZoningError("GPU standard-model lineage is ambiguous")
    return values[0]


def _validate_planning_document(
    planning_document: GpuPlanningDocument,
) -> tuple[_PlanningContext, gpd.GeoDataFrame]:
    if not isinstance(planning_document, GpuPlanningDocument):
        raise PlanningZoningError("planning_document must be a GpuPlanningDocument")

    archive = planning_document.extraction.archive
    document = archive.document
    provider = _strict_nonempty_string(document.provider, "GPU provider")
    portal = _strict_nonempty_string(document.portal, "GPU portal")
    commune_code = _strict_nonempty_string(
        document.commune_code, "GPU commune code"
    )
    document_id = _strict_nonempty_string(document.document_id, "GPU document ID")
    document_type = _strict_nonempty_string(
        document.document_type, "GPU document type"
    )
    archive_name = _strict_nonempty_string(document.archive_name, "GPU archive name")
    archive_sha256 = _strict_nonempty_string(archive.sha256, "GPU archive SHA256")
    if len(archive_sha256) != 64 or any(
        character not in "0123456789abcdefABCDEF" for character in archive_sha256
    ):
        raise PlanningZoningError("GPU archive SHA256 must contain 64 hexadecimal chars")

    zoning = planning_document.zoning
    if zoning.logical_name != "zoning":
        raise PlanningZoningError("GPU planning bundle must contain its zoning layer")
    source_layer = _strict_nonempty_string(
        zoning.reference.source_layer, "GPU zoning source layer"
    )
    source = zoning.data
    if not isinstance(source, gpd.GeoDataFrame):
        raise PlanningZoningError("GPU zoning data must be a GeoDataFrame")
    missing = sorted(GPU_ZONING_REQUIRED_COLUMNS - set(source.columns))
    if missing:
        raise PlanningZoningError(
            "GPU zoning is missing required source columns: " + ", ".join(missing)
        )
    _active_geometry(source, "GPU zoning")
    source_crs = _readable_crs(source.crs, "GPU zoning")
    _validate_polygon_geometries(source, "GPU zoning")
    if source.empty:
        raise PlanningZoningError("GPU zoning must contain at least one source zone")

    source_zone_column = GPU_ZONING_SOURCE_FIELDS["source_zone_id"]
    _validate_exact_string_ids(
        source[source_zone_column], source_zone_column, require_unique=True
    )
    source_document_column = GPU_ZONING_SOURCE_FIELDS[
        "source_document_reference_raw"
    ]
    _validate_exact_string_ids(
        source[source_document_column], source_document_column, require_unique=False
    )
    expected_document_reference = (
        archive_name[:-4] if archive_name.casefold().endswith(".zip") else archive_name
    )
    if not source[source_document_column].eq(expected_document_reference).all():
        raise PlanningZoningError(
            "GPU zoning IDURBA does not match the loaded planning archive identity"
        )

    summary = zoning.summary
    if summary.source_document_id != document_id:
        raise PlanningZoningError("GPU zoning summary document lineage is inconsistent")
    if summary.source_archive_sha256 != archive_sha256:
        raise PlanningZoningError("GPU zoning summary archive lineage is inconsistent")
    if summary.source_layer != source_layer:
        raise PlanningZoningError("GPU zoning summary source layer is inconsistent")
    if summary.feature_count != len(source):
        raise PlanningZoningError("GPU zoning summary feature count is inconsistent")

    context = _PlanningContext(
        provider=provider,
        portal=portal,
        commune_code=commune_code,
        document_id=document_id,
        document_type=document_type,
        archive_name=archive_name,
        archive_sha256=archive_sha256,
        source_layer=source_layer,
        standard_model=_standard_model(planning_document),
        source_crs=source_crs.to_string(),
    )
    return context, source


def _project_geometries(
    frame: gpd.GeoDataFrame,
    label: str,
) -> gpd.GeoSeries:
    source_crs = _readable_crs(frame.crs, label)
    target_crs = CRS.from_epsg(2154)
    try:
        if source_crs.equals(target_crs):
            projected = frame.geometry.copy()
        else:
            projected = frame.geometry.to_crs(target_crs)
        projected = gpd.GeoSeries(
            force_2d(projected.array), index=frame.index, crs=CALCULATION_CRS
        )
    except Exception as error:
        raise PlanningZoningError(
            f"{label} CRS cannot be transformed safely to {CALCULATION_CRS}"
        ) from error
    return projected


def _normalize_zones(
    source: gpd.GeoDataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
    projected_geometry = _project_geometries(source, "GPU zoning")
    source_zone_ids = source[GPU_ZONING_SOURCE_FIELDS["source_zone_id"]].copy()
    planning_zone_ids = source_zone_ids.map(
        lambda value: f"GPU:{context.document_id}:ZONE:{value}"
    )
    if planning_zone_ids.duplicated().any():
        raise PlanningZoningError("Normalized planning_zone_id values must be unique")

    data: dict[str, object] = {
        "planning_zone_id": planning_zone_ids.to_numpy(copy=True),
        "source_zone_id": source_zone_ids.to_numpy(copy=True),
    }
    for normalized_name, source_name in GPU_ZONING_SOURCE_FIELDS.items():
        if normalized_name == "source_zone_id":
            continue
        data[normalized_name] = source[source_name].to_numpy(copy=True)
    count = len(source)
    data.update(
        {
            "source_provider": np.repeat(context.provider, count),
            "source_portal": np.repeat(context.portal, count),
            "source_commune_code": np.repeat(context.commune_code, count),
            "source_document_id": np.repeat(context.document_id, count),
            "source_document_type": np.repeat(context.document_type, count),
            "source_archive_name": np.repeat(context.archive_name, count),
            "source_archive_sha256": np.repeat(context.archive_sha256, count),
            "source_layer": np.repeat(context.source_layer, count),
            "source_standard_model": np.full(
                count, context.standard_model, dtype="object"
            ),
            "source_crs": np.repeat(context.source_crs, count),
        }
    )
    zones = gpd.GeoDataFrame(
        data,
        geometry=projected_geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    zone_areas = zones.geometry.area.to_numpy(dtype="float64", copy=True)
    if not np.isfinite(zone_areas).all() or (zone_areas <= 0).any():
        raise PlanningZoningError("GPU zone areas must be finite and positive")
    zones["zone_area_m2"] = zone_areas
    zones = zones.reset_index(drop=True)
    zones = zones.set_crs(CALCULATION_CRS, allow_override=True)
    return zones


def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    geometry = _project_geometries(parcels, "Parcel")
    metric = gpd.GeoDataFrame(
        {
            "_parcel_position": np.arange(len(parcels), dtype="int64"),
            "parcel_id": parcels["parcel_id"].to_numpy(copy=True),
        },
        geometry=geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    areas = metric.geometry.area.to_numpy(dtype="float64", copy=True)
    if not np.isfinite(areas).all() or (areas <= 0).any():
        raise PlanningZoningError("Parcel metric areas must be finite and positive")
    metric["_parcel_area_m2"] = areas
    return metric


def _empty_intersections() -> pd.DataFrame:
    return pd.DataFrame(
        {
            column: pd.Series(
                dtype="float64" if column in _INTERSECTION_FLOAT_COLUMNS else "object"
            )
            for column in INTERSECTION_COLUMNS
        }
    )


def _candidate_intersections(
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
) -> pd.DataFrame:
    parcel_candidates = gpd.GeoDataFrame(
        metric_parcels[["_parcel_position", "parcel_id"]].copy(),
        geometry=metric_parcels.geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    zone_candidates = gpd.GeoDataFrame(
        {"_zone_position": np.arange(len(zones), dtype="int64")},
        geometry=zones.geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    try:
        candidates = gpd.sjoin(
            parcel_candidates,
            zone_candidates,
            how="inner",
            predicate="intersects",
        )
    except Exception as error:
        raise PlanningZoningError("GPU zoning spatial-index query failed") from error
    if candidates.empty:
        return pd.DataFrame(
            columns=("_parcel_position", "_zone_position", "_intersection_geometry")
        )

    parcel_positions = candidates["_parcel_position"].to_numpy(
        dtype="int64", copy=True
    )
    zone_positions = candidates["_zone_position"].to_numpy(dtype="int64", copy=True)
    try:
        intersection_geometry = shapely_intersection(
            metric_parcels.geometry.iloc[parcel_positions].array,
            zones.geometry.iloc[zone_positions].array,
        )
        intersection_areas = np.asarray(
            shapely_area(intersection_geometry), dtype="float64"
        )
    except Exception as error:
        raise PlanningZoningError("GPU zoning geometry overlay failed") from error
    if not np.isfinite(intersection_areas).all() or (intersection_areas < 0).any():
        raise PlanningZoningError("Intersection areas must be finite and non-negative")

    parcel_areas = metric_parcels["_parcel_area_m2"].to_numpy(dtype="float64")[
        parcel_positions
    ]
    zone_areas = zones["zone_area_m2"].to_numpy(dtype="float64")[zone_positions]
    relation_types = np.where(intersection_areas > 0, "AREA_OVERLAP", "TOUCH_ONLY")
    selected_zones = zones.iloc[zone_positions]
    geometry_values = np.empty(len(intersection_geometry), dtype="object")
    geometry_values[:] = intersection_geometry

    work = pd.DataFrame(
        {
            "_parcel_position": parcel_positions,
            "_zone_position": zone_positions,
            "_intersection_geometry": geometry_values,
            "parcel_id": metric_parcels["parcel_id"].to_numpy(copy=False)[
                parcel_positions
            ],
            "planning_zone_id": selected_zones["planning_zone_id"].to_numpy(
                copy=True
            ),
            "source_zone_id": selected_zones["source_zone_id"].to_numpy(copy=True),
            "zone_type_raw": selected_zones["zone_type_raw"].to_numpy(copy=True),
            "zone_label_raw": selected_zones["zone_label_raw"].to_numpy(copy=True),
            "zone_long_label_raw": selected_zones["zone_long_label_raw"].to_numpy(
                copy=True
            ),
            "relation_type": relation_types,
            "parcel_metric_area_m2": parcel_areas,
            "zone_area_m2": zone_areas,
            "intersection_area_m2": intersection_areas,
            "parcel_share_pct": 100.0 * intersection_areas / parcel_areas,
            "zone_share_pct": 100.0 * intersection_areas / zone_areas,
            "source_document_id": selected_zones["source_document_id"].to_numpy(
                copy=True
            ),
            "source_archive_sha256": selected_zones[
                "source_archive_sha256"
            ].to_numpy(copy=True),
            "source_layer": selected_zones["source_layer"].to_numpy(copy=True),
            "source_validity_date_raw": selected_zones[
                "source_validity_date_raw"
            ].to_numpy(copy=True),
            "regulation_filename_raw": selected_zones[
                "regulation_filename_raw"
            ].to_numpy(copy=True),
        }
    )
    work = work.sort_values(
        ["_parcel_position", "planning_zone_id"], kind="stable"
    ).reset_index(drop=True)
    return work


def _technical_area_tolerance(parcel_area_m2: float) -> float:
    return max(
        _AREA_ABSOLUTE_TOLERANCE_M2,
        parcel_area_m2 * _AREA_RELATIVE_TOLERANCE,
    )


def _stabilize_area_relationships(
    parcel_area: float,
    raw_sum: float,
    covered_union: float,
) -> tuple[float, float, float]:
    tolerance = _technical_area_tolerance(parcel_area)
    if covered_union > parcel_area:
        if covered_union - parcel_area > tolerance:
            raise PlanningZoningError(
                "Zoning covered-union area materially exceeds parcel area"
            )
        covered_union = parcel_area
    if covered_union > raw_sum:
        if covered_union - raw_sum > tolerance:
            raise PlanningZoningError(
                "Zoning covered-union area materially exceeds raw intersection sum"
            )
        covered_union = raw_sum
    gap = parcel_area - covered_union
    overlap_excess = raw_sum - covered_union
    if gap < 0 or overlap_excess < 0:
        raise PlanningZoningError("Zoning area differences must not be negative")
    return covered_union, gap, overlap_excess


def _parcel_summary(
    parcels: gpd.GeoDataFrame,
    metric_parcels: gpd.GeoDataFrame,
    zones: gpd.GeoDataFrame,
    work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
    count = len(parcels)
    parcel_areas = metric_parcels["_parcel_area_m2"].to_numpy(
        dtype="float64", copy=True
    )
    area_match_count = np.zeros(count, dtype="int64")
    touch_count = np.zeros(count, dtype="int64")
    raw_sum = np.zeros(count, dtype="float64")
    covered_union = np.zeros(count, dtype="float64")
    gap = parcel_areas.copy()
    overlap_excess = np.zeros(count, dtype="float64")

    dominant_planning = np.full(count, None, dtype="object")
    dominant_source = np.full(count, None, dtype="object")
    dominant_type = np.full(count, None, dtype="object")
    dominant_label = np.full(count, None, dtype="object")
    dominant_long_label = np.full(count, None, dtype="object")
    dominant_area = np.full(count, np.nan, dtype="float64")
    dominant_share = np.full(count, np.nan, dtype="float64")
    dominant_ties = pd.array([pd.NA] * count, dtype="Int64")

    if not work.empty:
        touches = work.loc[work["relation_type"] == "TOUCH_ONLY"]
        for position, group in touches.groupby("_parcel_position", sort=False):
            touch_count[int(position)] = len(group)

        positive = work.loc[work["relation_type"] == "AREA_OVERLAP"]
        for position_value, group in positive.groupby("_parcel_position", sort=False):
            position = int(position_value)
            areas = group["intersection_area_m2"].to_numpy(dtype="float64")
            area_match_count[position] = len(group)
            raw_area = float(areas.sum())
            raw_sum[position] = raw_area
            try:
                union_area = float(
                    shapely_area(
                        union_all(group["_intersection_geometry"].to_numpy())
                    )
                )
            except Exception as error:
                raise PlanningZoningError(
                    "GPU zoning covered-union calculation failed"
                ) from error
            if not isfinite(union_area) or union_area < 0:
                raise PlanningZoningError(
                    "GPU zoning covered-union area must be finite and non-negative"
                )
            union_area, parcel_gap, excess = _stabilize_area_relationships(
                float(parcel_areas[position]), raw_area, union_area
            )
            covered_union[position] = union_area
            gap[position] = parcel_gap
            overlap_excess[position] = excess

            maximum = float(areas.max())
            tied = group.loc[group["intersection_area_m2"] == maximum]
            selected = tied.sort_values("planning_zone_id", kind="stable").iloc[0]
            dominant_planning[position] = selected["planning_zone_id"]
            dominant_source[position] = selected["source_zone_id"]
            dominant_type[position] = selected["zone_type_raw"]
            dominant_label[position] = selected["zone_label_raw"]
            dominant_long_label[position] = selected["zone_long_label_raw"]
            dominant_area[position] = maximum
            dominant_share[position] = 100.0 * maximum / parcel_areas[position]
            dominant_ties[position] = len(tied)

    output = parcels.copy(deep=True)
    output["zoning_area_match_count"] = area_match_count
    output["zoning_touch_only_count"] = touch_count
    output["zoning_intersection_area_sum_m2"] = raw_sum
    output["zoning_covered_union_area_m2"] = covered_union
    output["zoning_coverage_pct"] = np.where(
        gap == 0.0,
        100.0,
        100.0 * covered_union / parcel_areas,
    )
    output["zoning_gap_area_m2"] = gap
    output["zoning_overlap_excess_area_m2"] = overlap_excess
    output["dominant_planning_zone_id"] = dominant_planning
    output["dominant_source_zone_id"] = dominant_source
    output["dominant_zone_type_raw"] = dominant_type
    output["dominant_zone_label_raw"] = dominant_label
    output["dominant_zone_long_label_raw"] = dominant_long_label
    output["dominant_zone_intersection_area_m2"] = dominant_area
    output["dominant_zone_share_pct"] = dominant_share
    output["dominant_zone_tie_count"] = dominant_ties
    output["planning_document_id"] = context.document_id
    output["planning_document_type"] = context.document_type
    output["planning_archive_name"] = context.archive_name
    output["planning_archive_sha256"] = context.archive_sha256
    output["planning_source_layer"] = context.source_layer
    output["planning_standard_model"] = context.standard_model
    return output


def _validate_numeric_columns(
    frame: pd.DataFrame,
    columns: tuple[str, ...] | frozenset[str],
    label: str,
    *,
    allow_null: bool,
) -> None:
    for column in columns:
        if column not in frame.columns:
            raise PlanningZoningError(f"{label} is missing numeric column: {column}")
        for value in frame[column].tolist():
            if pd.isna(value):
                if allow_null:
                    continue
                raise PlanningZoningError(f"{label} {column} must not be null")
            if isinstance(value, bool) or not isinstance(value, Real):
                raise PlanningZoningError(f"{label} {column} must be numeric")
            try:
                numeric = float(value)
            except (TypeError, ValueError, OverflowError) as error:
                raise PlanningZoningError(
                    f"{label} {column} must be finite"
                ) from error
            if not isfinite(numeric) or numeric < 0:
                raise PlanningZoningError(
                    f"{label} {column} must be finite and non-negative"
                )


def _validate_result(
    input_parcels: gpd.GeoDataFrame,
    result: ParcelZoningResult,
) -> None:
    output = result.parcels
    if len(output) != len(input_parcels):
        raise PlanningZoningError("Parcel zoning output count changed")
    if output["parcel_id"].tolist() != input_parcels["parcel_id"].tolist():
        raise PlanningZoningError("Parcel zoning output IDs or order changed")
    if not output.index.equals(input_parcels.index):
        raise PlanningZoningError("Parcel zoning output index changed")
    if output.crs != input_parcels.crs:
        raise PlanningZoningError("Parcel zoning output CRS changed")
    if not np.array_equal(
        output.geometry.to_wkb(), input_parcels.geometry.to_wkb()
    ):
        raise PlanningZoningError("Parcel zoning output geometry changed")

    if not CRS.from_user_input(result.zones.crs).equals(CRS.from_epsg(2154)):
        raise PlanningZoningError("Normalized zones must use EPSG:2154")
    _validate_exact_string_ids(
        result.zones["planning_zone_id"],
        "planning_zone_id",
        require_unique=True,
    )
    _validate_numeric_columns(
        result.zones, ("zone_area_m2",), "Normalized zone", allow_null=False
    )

    intersections = result.intersections
    missing = sorted(set(INTERSECTION_COLUMNS) - set(intersections.columns))
    if missing:
        raise PlanningZoningError(
            "Intersection table is missing columns: " + ", ".join(missing)
        )
    if intersections.duplicated(["parcel_id", "planning_zone_id"]).any():
        raise PlanningZoningError("Parcel/zone intersection pairs must be unique")
    if not set(intersections["parcel_id"]).issubset(set(output["parcel_id"])):
        raise PlanningZoningError("Intersection table contains an unknown parcel ID")
    if not set(intersections["planning_zone_id"]).issubset(
        set(result.zones["planning_zone_id"])
    ):
        raise PlanningZoningError("Intersection table contains an unknown zone ID")
    if not set(intersections["relation_type"]).issubset(RELATION_TYPES):
        raise PlanningZoningError("Intersection table has an unknown relation type")
    _validate_numeric_columns(
        intersections,
        _INTERSECTION_FLOAT_COLUMNS,
        "Intersection table",
        allow_null=False,
    )

    required_summary = (
        "zoning_area_match_count",
        "zoning_touch_only_count",
        "zoning_intersection_area_sum_m2",
        "zoning_covered_union_area_m2",
        "zoning_coverage_pct",
        "zoning_gap_area_m2",
        "zoning_overlap_excess_area_m2",
    )
    _validate_numeric_columns(output, required_summary, "Parcel zoning", allow_null=False)
    coverage = output["zoning_coverage_pct"].to_numpy(dtype="float64")
    if (coverage > 100.0).any():
        raise PlanningZoningError("Parcel zoning coverage must not exceed 100 percent")


def intersect_parcels_with_gpu_zoning(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelZoningResult:
    """Return factual parcel/zoning intersections without policy interpretation.

    Parcel storage geometry and CRS are preserved.  Zoning normalization,
    overlay, area, and union calculations use planar XY geometry in EPSG:2154.
    """

    _validate_parcels(parcels)
    context, source_zones = _validate_planning_document(planning_document)
    zones = _normalize_zones(source_zones, context)
    metric_parcels = _metric_parcels(parcels)
    work = _candidate_intersections(metric_parcels, zones)
    parcel_output = _parcel_summary(
        parcels, metric_parcels, zones, work, context
    )
    intersections = (
        _empty_intersections()
        if work.empty
        else work.loc[:, INTERSECTION_COLUMNS].reset_index(drop=True)
    )
    result = ParcelZoningResult(
        parcels=parcel_output,
        zones=zones,
        intersections=intersections,
    )
    _validate_result(parcels, result)
    return result
