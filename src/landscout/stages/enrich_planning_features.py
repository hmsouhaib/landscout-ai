"""Normalize and intersect factual GPU prescription/information features."""

from __future__ import annotations

import json
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from math import isfinite
from numbers import Integral, Real
from typing import Literal, NamedTuple

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import (  # type: ignore[import-untyped]
    area as shapely_area,
)
from shapely import (
    contains,
    covers,
    force_2d,
    get_coordinate_dimension,
    get_parts,
    intersection,
    union_all,
)
from shapely import (
    length as shapely_length,
)

from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)
from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)
from landscout.common.planning_overlay import technical_overlay_tolerance
from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)

__all__ = [
    "ParcelPlanningFeaturesResult",
    "PlanningFeatureInputValidation",
    "PlanningFeaturesError",
    "intersect_parcels_with_gpu_planning_features",
    "validate_normalized_planning_feature_inputs",
]

CALCULATION_CRS = "EPSG:2154"
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})

FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
GeometryKind = Literal["SURFACE", "LINE", "POINT"]
SourceIdentityKind = Literal["CNIG_ATTRIBUTE", "ARCHIVE_SCOPED_OGR_FID"]

SOURCE_IDENTITY_KINDS = frozenset({"CNIG_ATTRIBUTE", "ARCHIVE_SCOPED_OGR_FID"})

SURFACE_TYPES = frozenset({"Polygon", "MultiPolygon"})
LINE_TYPES = frozenset({"LineString", "MultiLineString"})
POINT_TYPES = frozenset({"Point", "MultiPoint"})


class _LayerSpec(NamedTuple):
    logical_layer: str
    feature_family: FeatureFamily
    geometry_kind: GeometryKind
    identity_field: str
    type_field: str
    subtype_field: str
    allowed_geometry_types: frozenset[str]


LAYER_SPECS = {
    "prescription_surface": _LayerSpec(
        "prescription_surface",
        "PRESCRIPTION",
        "SURFACE",
        "LIB_IDPSC",
        "TYPEPSC",
        "STYPEPSC",
        SURFACE_TYPES,
    ),
    "prescription_line": _LayerSpec(
        "prescription_line",
        "PRESCRIPTION",
        "LINE",
        "LIB_IDPSC",
        "TYPEPSC",
        "STYPEPSC",
        LINE_TYPES,
    ),
    "prescription_point": _LayerSpec(
        "prescription_point",
        "PRESCRIPTION",
        "POINT",
        "LIB_IDPSC",
        "TYPEPSC",
        "STYPEPSC",
        POINT_TYPES,
    ),
    "information_surface": _LayerSpec(
        "information_surface",
        "INFORMATION",
        "SURFACE",
        "LIB_IDINFO",
        "TYPEINF",
        "STYPEINF",
        SURFACE_TYPES,
    ),
    "information_line": _LayerSpec(
        "information_line",
        "INFORMATION",
        "LINE",
        "LIB_IDINFO",
        "TYPEINF",
        "STYPEINF",
        LINE_TYPES,
    ),
    "information_point": _LayerSpec(
        "information_point",
        "INFORMATION",
        "POINT",
        "LIB_IDINFO",
        "TYPEINF",
        "STYPEINF",
        POINT_TYPES,
    ),
}

COMMON_SOURCE_FIELDS = {
    "label_raw": "LIBELLE",
    "text_raw": "TXT",
    "regulation_filename_raw": "NOMFIC",
    "regulation_url_raw": "URLFIC",
    "source_document_reference_raw": "IDURBA",
    "source_validity_date_raw": "DATVALID",
}
OPTIONAL_SOURCE_FIELDS = frozenset(
    {
        "LIBELLE",
        "TXT",
        "NOMFIC",
        "URLFIC",
        "DATVALID",
    }
)

_CATALOG_GEOMETRY_TYPES = {
    "SURFACE": SURFACE_TYPES,
    "LINE": LINE_TYPES,
    "POINT": POINT_TYPES,
}
_CATALOG_REQUIRED_EXACT_STRING_COLUMNS = (
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "source_document_reference_raw",
    "source_provider",
    "source_portal",
    "source_commune_code",
    "source_document_id",
    "source_document_type",
    "source_archive_name",
    "source_archive_sha256",
    "source_layer",
    "source_crs",
)
_CATALOG_OPTIONAL_EXACT_STRING_COLUMNS = (
    "label_raw",
    "text_raw",
    "regulation_filename_raw",
    "regulation_url_raw",
    "source_validity_date_raw",
    "source_standard_model",
)

PARCEL_OUTPUT_COLUMNS = frozenset(
    {
        "planning_surface_relation_count",
        "planning_surface_area_overlap_count",
        "planning_surface_touch_count",
        "planning_surface_intersection_area_sum_m2",
        "planning_surface_covered_union_area_m2",
        "planning_surface_covered_pct",
        "prescription_surface_relation_count",
        "prescription_surface_covered_union_area_m2",
        "prescription_surface_covered_pct",
        "information_surface_relation_count",
        "information_surface_covered_union_area_m2",
        "information_surface_covered_pct",
        "planning_line_relation_count",
        "planning_line_length_overlap_count",
        "planning_line_touch_count",
        "planning_line_intersection_length_sum_m",
        "planning_point_relation_count",
        "planning_point_inside_count",
        "planning_point_boundary_count",
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
    }
)

PARCEL_COUNT_COLUMNS = frozenset(
    {
        "planning_surface_relation_count",
        "planning_surface_area_overlap_count",
        "planning_surface_touch_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_line_length_overlap_count",
        "planning_line_touch_count",
        "planning_point_relation_count",
        "planning_point_inside_count",
        "planning_point_boundary_count",
    }
)


class PlanningFeaturesError(ValueError):
    """Raised when factual GPU feature measurement cannot be completed safely."""


@dataclass(frozen=True)
class ParcelPlanningFeaturesResult:
    """Normalized feature catalogs, parcel enrichment, and factual relations."""

    parcels: gpd.GeoDataFrame
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame


@dataclass(frozen=True)
class PlanningFeatureInputValidation:
    """Immutable source-completeness evidence for normalized planning facts."""

    gpu_related_source_files_sha256: str
    expected_relations_content_sha256: str
    related_source_layer_count: int
    related_source_file_count: int
    expected_relation_count: int


@dataclass(frozen=True)
class _PlanningContext:
    provider: str
    portal: str
    commune_code: str
    document_id: str
    document_type: str
    archive_name: str
    archive_sha256: str
    standard_model: str | None


def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningFeaturesError(f"{label} must be a non-empty exact string")
    return value


def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise PlanningFeaturesError(f"{label} must be an integer count")
    if value < 0:
        raise PlanningFeaturesError(f"{label} must be non-negative")
    return int(value)


def _validate_ids(values: pd.Series, label: str) -> None:
    _validate_exact_strings(values, label)
    if values.duplicated().any():
        raise PlanningFeaturesError(f"{label} values must be unique")


def _validate_exact_strings(values: pd.Series, label: str) -> None:
    if values.isna().any():
        raise PlanningFeaturesError(f"{label} values must not be null")
    for value in values.tolist():
        _strict_string(value, label)


def _validate_optional_exact_strings(values: pd.Series, label: str) -> None:
    for value in values.tolist():
        if pd.isna(value):
            continue
        _strict_string(value, label)


def _crs(value: object, label: str) -> CRS:
    if value is None:
        raise PlanningFeaturesError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise PlanningFeaturesError(f"{label} CRS is unreadable") from error


def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise PlanningFeaturesError(f"{label} geometry column is required")
    try:
        active = frame.active_geometry_name
    except AttributeError as error:
        raise PlanningFeaturesError(f"{label} geometry must be active") from error
    if active != "geometry":
        raise PlanningFeaturesError(f"{label} geometry must be active")


def _validate_geometries(
    frame: gpd.GeoDataFrame,
    allowed: frozenset[str],
    label: str,
) -> None:
    geometry = frame.geometry
    if geometry.isna().any():
        raise PlanningFeaturesError(f"{label} geometry must not be null")
    if geometry.is_empty.any():
        raise PlanningFeaturesError(f"{label} geometry must not be empty")
    if not geometry.is_valid.all():
        raise PlanningFeaturesError(f"{label} geometry must be valid")
    found = set(geometry.geom_type)
    if not found.issubset(allowed):
        raise PlanningFeaturesError(
            f"{label} has unsupported geometry types: "
            + ", ".join(sorted(found - allowed))
        )


def _validate_two_dimensional_geometry(
    frame: gpd.GeoDataFrame,
    label: str,
) -> None:
    try:
        dimensions = np.asarray(
            get_coordinate_dimension(frame.geometry.array), dtype="int64"
        )
        if (dimensions != 2).any():
            raise PlanningFeaturesError(f"{label} geometry must be canonical 2D")
    except PlanningFeaturesError:
        raise
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} geometry dimensionality cannot be validated"
        ) from error


def _validate_parcels(
    parcels: gpd.GeoDataFrame,
    *,
    allow_output_columns: bool = False,
) -> CRS:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise PlanningFeaturesError("Parcels must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise PlanningFeaturesError("Parcels contain duplicate columns")
    missing = sorted(PARCEL_REQUIRED_COLUMNS - set(parcels.columns))
    if missing:
        raise PlanningFeaturesError(
            "Parcels are missing required columns: " + ", ".join(missing)
        )
    collisions = sorted(PARCEL_OUTPUT_COLUMNS & set(parcels.columns))
    if collisions and not allow_output_columns:
        raise PlanningFeaturesError(
            "Parcels already contain planning-feature output columns: "
            + ", ".join(collisions)
        )
    _active_geometry(parcels, "Parcel")
    source_crs = _crs(parcels.crs, "Parcel")
    _validate_ids(parcels["parcel_id"], "parcel_id")
    _validate_geometries(parcels, SURFACE_TYPES, "Parcel")
    return source_crs


def _standard_model(document: GpuPlanningDocument) -> str | None:
    values: list[str] = []
    model = document.extraction.archive.document.standard_model
    if model is not None:
        values.append(_strict_string(model, "GPU standard model"))
    for value in document.extraction.standard_models:
        validated = _strict_string(value, "GPU extracted standard model")
        if validated not in values:
            values.append(validated)
    if len(values) > 1:
        raise PlanningFeaturesError("GPU standard-model lineage is ambiguous")
    return values[0] if values else None


def _planning_context(document: GpuPlanningDocument) -> _PlanningContext:
    if not isinstance(document, GpuPlanningDocument):
        raise PlanningFeaturesError("planning_document must be a GpuPlanningDocument")
    archive = document.extraction.archive
    metadata = archive.document
    sha = _strict_string(archive.sha256, "GPU archive SHA256")
    if len(sha) != 64 or any(c not in "0123456789abcdefABCDEF" for c in sha):
        raise PlanningFeaturesError("GPU archive SHA256 must contain 64 hex chars")
    return _PlanningContext(
        provider=_strict_string(metadata.provider, "GPU provider"),
        portal=_strict_string(metadata.portal, "GPU portal"),
        commune_code=_strict_string(metadata.commune_code, "GPU commune code"),
        document_id=_strict_string(metadata.document_id, "GPU document ID"),
        document_type=_strict_string(metadata.document_type, "GPU document type"),
        archive_name=_strict_string(metadata.archive_name, "GPU archive name"),
        archive_sha256=sha,
        standard_model=_standard_model(document),
    )


def _summary_geometry_types(frame: gpd.GeoDataFrame) -> tuple[tuple[str, int], ...]:
    counts = frame.geometry.geom_type.value_counts().sort_index()
    return tuple((str(key), int(value)) for key, value in counts.items())


def _validate_layer_summary(
    layer: GpuInspectedLayer,
    context: _PlanningContext,
) -> None:
    frame = layer.data
    summary = layer.summary
    actual_crs = _crs(frame.crs, f"{layer.logical_name} source")
    summary_crs = _crs(summary.crs, f"{layer.logical_name} summary")
    expected_nulls = tuple(
        (str(column), int(frame[column].isna().sum())) for column in frame.columns
    )
    expected_dtypes = tuple(
        (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
    )
    geometry = frame.geometry
    non_null = geometry.notna()
    non_empty = non_null & ~geometry.is_empty
    _strict_nonnegative_integer(summary.feature_count, "summary feature_count")
    _strict_nonnegative_integer(
        summary.null_geometry_count, "summary null_geometry_count"
    )
    _strict_nonnegative_integer(
        summary.empty_geometry_count, "summary empty_geometry_count"
    )
    _strict_nonnegative_integer(
        summary.invalid_geometry_count, "summary invalid_geometry_count"
    )
    for column, value in summary.null_counts:
        _strict_nonnegative_integer(value, f"summary {column} null count")
    for geometry_type, value in summary.geometry_types:
        _strict_nonnegative_integer(value, f"summary {geometry_type} count")
    if (
        summary.source_document_id != context.document_id
        or summary.source_archive_sha256 != context.archive_sha256
        or summary.source_layer != layer.reference.source_layer
        or summary.feature_count != len(frame)
        or not actual_crs.equals(summary_crs)
        or summary.columns != tuple(str(column) for column in frame.columns)
        or summary.dtypes != expected_dtypes
        or summary.null_counts != expected_nulls
        or summary.geometry_types != _summary_geometry_types(frame)
        or summary.null_geometry_count != int((~non_null).sum())
        or summary.empty_geometry_count != int((non_null & geometry.is_empty).sum())
        or summary.invalid_geometry_count != int((non_empty & ~geometry.is_valid).sum())
    ):
        raise PlanningFeaturesError(
            f"{layer.logical_name} source summary is inconsistent with loaded data"
        )


def _project_geometry(frame: gpd.GeoDataFrame, label: str) -> gpd.GeoSeries:
    source = _crs(frame.crs, label)
    target = CRS.from_epsg(2154)
    try:
        projected = (
            frame.geometry.copy()
            if source.equals(target)
            else frame.to_crs(target).geometry
        )
        return gpd.GeoSeries(force_2d(projected.array), crs=target)
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} CRS cannot be transformed safely to EPSG:2154"
        ) from error


def _source_feature_ids(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    validated_source: GpuValidatedSpatialLayerSource,
) -> tuple[pd.Series, SourceIdentityKind, str]:
    if spec.identity_field in layer.data.columns:
        result = layer.data[spec.identity_field].reset_index(drop=True).copy()
        _validate_ids(result, spec.identity_field)
        return result, "CNIG_ATTRIBUTE", spec.identity_field
    if spec.logical_layer == "prescription_surface":
        if layer.data.empty:
            return (
                pd.Series(dtype="object"),
                "ARCHIVE_SCOPED_OGR_FID",
                "OGR_FID",
            )
        if len(validated_source.ogr_fids) != len(layer.data):
            raise PlanningFeaturesError(
                f"{layer.logical_name} verified source FIDs are unavailable"
            )
        values = pd.Series(
            [f"OGR_FID:{value}" for value in validated_source.ogr_fids],
            dtype="object",
        )
        _validate_ids(values, f"{layer.logical_name} OGR FID")
        return values, "ARCHIVE_SCOPED_OGR_FID", "OGR_FID"
    raise PlanningFeaturesError(
        f"{spec.logical_layer} is missing required identity field {spec.identity_field}"
    )


def _optional_values(frame: gpd.GeoDataFrame, source_field: str) -> np.ndarray:
    if source_field not in frame.columns:
        return np.full(len(frame), None, dtype="object")
    return frame[source_field].to_numpy(copy=True)


def _normalize_layer(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    context: _PlanningContext,
    validated_source: GpuValidatedSpatialLayerSource,
) -> gpd.GeoDataFrame:
    frame = layer.data
    if not isinstance(frame, gpd.GeoDataFrame):
        raise PlanningFeaturesError(f"{spec.logical_layer} must be a GeoDataFrame")
    _active_geometry(frame, spec.logical_layer)
    required = {spec.type_field, spec.subtype_field, "IDURBA", "geometry"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise PlanningFeaturesError(
            f"{spec.logical_layer} is missing required source fields: "
            + ", ".join(missing)
        )
    # Raw classification codes may repeat; validate hygiene without uniqueness.
    for field in (spec.type_field, spec.subtype_field, "IDURBA"):
        if frame[field].isna().any():
            raise PlanningFeaturesError(
                f"{spec.logical_layer} {field} must not be null"
            )
        for value in frame[field].tolist():
            _strict_string(value, f"{spec.logical_layer} {field}")
    _validate_geometries(frame, spec.allowed_geometry_types, spec.logical_layer)
    _validate_layer_summary(layer, context)
    expected_reference = (
        context.archive_name[:-4]
        if context.archive_name.casefold().endswith(".zip")
        else context.archive_name
    )
    if not frame["IDURBA"].eq(expected_reference).all():
        raise PlanningFeaturesError(
            f"{spec.logical_layer} IDURBA does not match planning archive identity"
        )

    source_ids, identity_kind, identity_field = _source_feature_ids(
        layer, spec, validated_source
    )
    planning_ids = source_ids.map(
        lambda value: f"GPU:{context.document_id}:{spec.logical_layer}:{value}"
    )
    geometry = _project_geometry(frame, spec.logical_layer)
    projected = gpd.GeoDataFrame(
        {
            "planning_feature_id": planning_ids.to_numpy(copy=True),
            "source_feature_id": source_ids.to_numpy(copy=True),
            "source_identity_kind": np.repeat(identity_kind, len(frame)),
            "source_identity_field": np.repeat(identity_field, len(frame)),
            "logical_layer": np.repeat(spec.logical_layer, len(frame)),
            "feature_family": np.repeat(spec.feature_family, len(frame)),
            "geometry_kind": np.repeat(spec.geometry_kind, len(frame)),
            "type_code_raw": frame[spec.type_field].to_numpy(copy=True),
            "subtype_code_raw": frame[spec.subtype_field].to_numpy(copy=True),
            **{
                normalized: _optional_values(frame, source)
                for normalized, source in COMMON_SOURCE_FIELDS.items()
            },
            "source_provider": np.repeat(context.provider, len(frame)),
            "source_portal": np.repeat(context.portal, len(frame)),
            "source_commune_code": np.repeat(context.commune_code, len(frame)),
            "source_document_id": np.repeat(context.document_id, len(frame)),
            "source_document_type": np.repeat(context.document_type, len(frame)),
            "source_archive_name": np.repeat(context.archive_name, len(frame)),
            "source_archive_sha256": np.repeat(context.archive_sha256, len(frame)),
            "source_layer": np.repeat(layer.reference.source_layer, len(frame)),
            "source_standard_model": np.full(
                len(frame), context.standard_model, dtype="object"
            ),
            "source_crs": np.repeat(layer.summary.crs, len(frame)),
        },
        geometry=geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    ).reset_index(drop=True)
    _validate_geometries(projected, spec.allowed_geometry_types, spec.logical_layer)
    if spec.geometry_kind == "SURFACE":
        try:
            values = projected.geometry.area.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                f"{spec.logical_layer} area calculation failed"
            ) from error
        if not np.isfinite(values).all() or (values <= 0).any():
            raise PlanningFeaturesError(f"{spec.logical_layer} areas must be positive")
        projected["feature_area_m2"] = values
    elif spec.geometry_kind == "LINE":
        try:
            values = projected.geometry.length.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                f"{spec.logical_layer} length calculation failed"
            ) from error
        if not np.isfinite(values).all() or (values <= 0).any():
            raise PlanningFeaturesError(
                f"{spec.logical_layer} lengths must be positive"
            )
        projected["feature_length_m"] = values
    else:
        try:
            projected["point_member_count"] = [
                len(get_parts(value)) for value in projected.geometry.array
            ]
        except Exception as error:
            raise PlanningFeaturesError(
                f"{spec.logical_layer} point-member calculation failed"
            ) from error
    return projected


def _canonical_catalog_dtypes(
    catalog: gpd.GeoDataFrame,
    kind: GeometryKind,
) -> gpd.GeoDataFrame:
    for column, dtype in zip(
        NORMALIZED_FEATURE_COLUMNS[kind],
        normalized_feature_dtypes(kind, catalog),
        strict=True,
    ):
        if column == "geometry":
            continue
        catalog[column] = pd.Series(
            catalog[column].tolist(), index=catalog.index, dtype=dtype
        )
    catalog.index = pd.RangeIndex(len(catalog))
    return catalog


def _empty_catalog(kind: GeometryKind) -> gpd.GeoDataFrame:
    data: dict[str, object] = {}
    for column, dtype in zip(
        NORMALIZED_FEATURE_COLUMNS[kind],
        NORMALIZED_FEATURE_DTYPES[kind],
        strict=True,
    ):
        data[column] = (
            gpd.GeoSeries([], crs=CALCULATION_CRS)
            if column == "geometry"
            else pd.Series(dtype=dtype)
        )
    output = gpd.GeoDataFrame(data, geometry="geometry", crs=CALCULATION_CRS)
    return _canonical_catalog_dtypes(output, kind)


def _combine_catalogs(
    frames: list[gpd.GeoDataFrame], kind: GeometryKind
) -> gpd.GeoDataFrame:
    if not frames:
        return _empty_catalog(kind)
    combined = gpd.GeoDataFrame(
        pd.concat(frames, ignore_index=True), geometry="geometry", crs=CALCULATION_CRS
    )
    _validate_ids(combined["planning_feature_id"], "planning_feature_id")
    return _canonical_catalog_dtypes(combined, kind)


def _normalized_catalogs(
    planning_document: GpuPlanningDocument,
) -> tuple[
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    tuple[GpuValidatedSpatialLayerSource, ...],
]:
    """Rebuild canonical catalogs from the inspected GPU related layers only."""

    context = _planning_context(planning_document)
    spatial_inventory = tuple(planning_document.all_spatial_layers)
    inspected_layers = (planning_document.zoning, *planning_document.related_layers)
    for layer in inspected_layers:
        if sum(reference == layer.reference for reference in spatial_inventory) != 1:
            raise PlanningFeaturesError(
                f"{layer.logical_name} inspected reference must occur exactly once "
                "in the GPU spatial-layer inventory"
            )
    layer_map: dict[str, GpuInspectedLayer] = {}
    for inspected_layer in planning_document.related_layers:
        logical = str(inspected_layer.logical_name)
        if logical not in LAYER_SPECS:
            raise PlanningFeaturesError(f"Unsupported related layer: {logical}")
        if logical in layer_map:
            raise PlanningFeaturesError(f"Duplicate related layer: {logical}")
        layer_map[logical] = inspected_layer

    try:
        validated_sources = revalidate_gpu_spatial_layer_sources(
            planning_document,
            tuple(
                layer_map[logical] for logical in LAYER_SPECS if logical in layer_map
            ),
        )
    except GpuSpatialInspectionError as error:
        raise PlanningFeaturesError(
            "Related GPU spatial sources failed physical revalidation"
        ) from error
    source_by_logical: dict[str, GpuValidatedSpatialLayerSource] = {
        source.logical_name: source for source in validated_sources
    }
    normalized: dict[str, gpd.GeoDataFrame] = {}
    for logical, layer in layer_map.items():
        source = source_by_logical[logical]
        fresh_layer = replace(layer, data=source.data)
        normalized[logical] = _normalize_layer(
            fresh_layer, LAYER_SPECS[logical], context, source
        )

    def combined(kind: GeometryKind) -> gpd.GeoDataFrame:
        return _combine_catalogs(
            [
                normalized[logical]
                for logical, spec in LAYER_SPECS.items()
                if spec.geometry_kind == kind and logical in normalized
            ],
            kind,
        )

    return (
        combined("SURFACE"),
        combined("LINE"),
        combined("POINT"),
        validated_sources,
    )


def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    geometry = _project_geometry(parcels, "Parcel")
    result = gpd.GeoDataFrame(
        {
            "_parcel_position": np.arange(len(parcels), dtype="int64"),
            "parcel_id": parcels["parcel_id"].to_numpy(copy=True),
        },
        geometry=geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    try:
        areas = result.geometry.area.to_numpy(dtype="float64")
    except Exception as error:
        raise PlanningFeaturesError("Parcel metric-area calculation failed") from error
    if not np.isfinite(areas).all() or (areas <= 0).any():
        raise PlanningFeaturesError("Parcel metric areas must be finite and positive")
    result["_parcel_area_m2"] = areas
    return result


def _relation_base(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    if catalog.empty or metric.empty:
        return pd.DataFrame(), np.array([], dtype="int64"), np.array([], dtype="int64")
    try:
        candidates = gpd.sjoin(
            metric[["_parcel_position", "parcel_id", "geometry"]],
            gpd.GeoDataFrame(
                {"_feature_position": np.arange(len(catalog), dtype="int64")},
                geometry=catalog.geometry.to_numpy(copy=True),
                crs=CALCULATION_CRS,
            ),
            how="inner",
            predicate="intersects",
        )
    except Exception as error:
        raise PlanningFeaturesError("Planning-feature spatial join failed") from error
    if candidates.empty:
        return pd.DataFrame(), np.array([], dtype="int64"), np.array([], dtype="int64")
    parcel_positions = candidates["_parcel_position"].to_numpy(dtype="int64")
    feature_positions = candidates["_feature_position"].to_numpy(dtype="int64")
    selected = catalog.iloc[feature_positions]
    base = pd.DataFrame(
        {
            "_parcel_position": parcel_positions,
            "_feature_position": feature_positions,
            "parcel_id": metric["parcel_id"].to_numpy()[parcel_positions],
            **{
                column: selected[column].to_numpy(copy=True)
                for column in (
                    "planning_feature_id",
                    "source_feature_id",
                    "source_identity_kind",
                    "source_identity_field",
                    "logical_layer",
                    "feature_family",
                    "geometry_kind",
                    "type_code_raw",
                    "subtype_code_raw",
                    "label_raw",
                    "text_raw",
                )
            },
            "parcel_metric_area_m2": metric["_parcel_area_m2"].to_numpy()[
                parcel_positions
            ],
            "source_document_id": selected["source_document_id"].to_numpy(copy=True),
            "source_archive_sha256": selected["source_archive_sha256"].to_numpy(
                copy=True
            ),
            "source_layer": selected["source_layer"].to_numpy(copy=True),
            "source_validity_date_raw": selected["source_validity_date_raw"].to_numpy(
                copy=True
            ),
            "regulation_filename_raw": selected["regulation_filename_raw"].to_numpy(
                copy=True
            ),
        }
    )
    return base, parcel_positions, feature_positions


def _surface_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
    base, parcel_positions, feature_positions = _relation_base(metric, catalog)
    if base.empty:
        return base
    try:
        geometries = intersection(
            metric.geometry.iloc[parcel_positions].array,
            catalog.geometry.iloc[feature_positions].array,
        )
        areas = np.asarray(shapely_area(geometries), dtype="float64")
    except Exception as error:
        raise PlanningFeaturesError(
            "Surface intersection calculation failed"
        ) from error
    feature_areas = catalog["feature_area_m2"].to_numpy(dtype="float64")[
        feature_positions
    ]
    base["_intersection_geometry"] = list(geometries)
    base["relation_type"] = np.where(areas > 0, "AREA_OVERLAP", "TOUCH_ONLY")
    base["feature_area_m2"] = feature_areas
    base["source_line_length_m"] = np.nan
    base["intersection_area_m2"] = areas
    base["intersection_length_m"] = np.nan
    base["parcel_share_pct"] = 100.0 * areas / base["parcel_metric_area_m2"]
    base["feature_share_pct"] = 100.0 * areas / feature_areas
    for column in RELATION_COUNT_COLUMNS:
        base[column] = pd.array([pd.NA] * len(base), dtype="Int64")
    return base


def _line_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
    base, parcel_positions, feature_positions = _relation_base(metric, catalog)
    if base.empty:
        return base
    try:
        geometries = intersection(
            metric.geometry.iloc[parcel_positions].array,
            catalog.geometry.iloc[feature_positions].array,
        )
        lengths = np.asarray(shapely_length(geometries), dtype="float64")
    except Exception as error:
        raise PlanningFeaturesError("Line intersection calculation failed") from error
    source_lengths = catalog["feature_length_m"].to_numpy(dtype="float64")[
        feature_positions
    ]
    base["relation_type"] = np.where(lengths > 0, "LENGTH_OVERLAP", "TOUCH_ONLY")
    base["feature_area_m2"] = np.nan
    base["source_line_length_m"] = source_lengths
    base["intersection_area_m2"] = np.nan
    base["intersection_length_m"] = lengths
    base["parcel_share_pct"] = np.nan
    base["feature_share_pct"] = np.nan
    for column in RELATION_COUNT_COLUMNS:
        base[column] = pd.array([pd.NA] * len(base), dtype="Int64")
    return base


def _point_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
    base, parcel_positions, feature_positions = _relation_base(metric, catalog)
    if base.empty:
        return base
    try:
        members, relation_positions = get_parts(
            catalog.geometry.iloc[feature_positions].array,
            return_index=True,
        )
        relation_positions = np.asarray(relation_positions, dtype="int64")
        member_parcels = metric.geometry.iloc[
            parcel_positions[relation_positions]
        ].array
        inside_mask = np.asarray(contains(member_parcels, members), dtype="bool")
        covered_mask = np.asarray(covers(member_parcels, members), dtype="bool")
    except Exception as error:
        raise PlanningFeaturesError("Point intersection calculation failed") from error
    member_counts = np.bincount(relation_positions, minlength=len(base))
    inside_counts = np.bincount(
        relation_positions, weights=inside_mask, minlength=len(base)
    ).astype("int64")
    covered_counts = np.bincount(
        relation_positions, weights=covered_mask, minlength=len(base)
    ).astype("int64")
    boundary_counts = covered_counts - inside_counts
    if ((inside_counts + boundary_counts) <= 0).any():
        raise PlanningFeaturesError("Point candidate has no covered source member")
    base["relation_type"] = np.where(inside_counts > 0, "INSIDE", "BOUNDARY_TOUCH")
    for column in RELATION_FLOAT_COLUMNS - {"parcel_metric_area_m2"}:
        base[column] = np.nan
    base["point_member_count"] = pd.array(member_counts, dtype="Int64")
    base["point_members_inside_count"] = pd.array(inside_counts, dtype="Int64")
    base["point_members_boundary_count"] = pd.array(boundary_counts, dtype="Int64")
    return base


def _empty_relations() -> pd.DataFrame:
    output = pd.DataFrame(
        {
            column: pd.Series(
                dtype=(
                    "float64"
                    if column in RELATION_FLOAT_COLUMNS
                    else "Int64"
                    if column in RELATION_COUNT_COLUMNS
                    else "str"
                )
            )
            for column in RELATION_COLUMNS
        }
    )
    output.index = pd.RangeIndex(0)
    return output


def _build_relation_tables(
    metric: gpd.GeoDataFrame,
    surfaces: gpd.GeoDataFrame,
    lines: gpd.GeoDataFrame,
    points: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    surface_work = _surface_relations(metric, surfaces)
    line_work = _line_relations(metric, lines)
    point_work = _point_relations(metric, points)
    work_frames = [
        frame for frame in (surface_work, line_work, point_work) if not frame.empty
    ]
    if not work_frames:
        return surface_work, line_work, point_work, _empty_relations()
    combined = pd.concat(work_frames, ignore_index=True)
    combined = combined.sort_values(
        ["_parcel_position", "planning_feature_id"], kind="stable"
    ).reset_index(drop=True)
    relations = combined.loc[:, RELATION_COLUMNS].copy()
    for column in RELATION_STRING_COLUMNS:
        relations[column] = relations[column].astype("str")
    for column in RELATION_COUNT_COLUMNS:
        relations[column] = pd.array(relations[column], dtype="Int64")
    relations.index = pd.RangeIndex(len(relations))
    return surface_work, line_work, point_work, relations


def _canonical_integrity_value(value: object) -> object:
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_integrity_value(value.item())
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not isfinite(number):
            raise PlanningFeaturesError(
                "Integrity payload contains non-finite numeric data"
            )
        return number
    if isinstance(value, str):
        return value
    raise PlanningFeaturesError(
        f"Integrity payload contains unsupported value {type(value).__name__}"
    )


def _canonical_integrity_sha256(payload: object) -> str:
    try:
        encoded = json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except Exception as error:
        raise PlanningFeaturesError(
            "Planning-feature integrity payload cannot be serialized"
        ) from error
    return sha256(encoded).hexdigest()


def _gpu_related_source_files_sha256(
    planning_document: GpuPlanningDocument,
    sources: tuple[GpuValidatedSpatialLayerSource, ...],
) -> str:
    return _canonical_integrity_sha256(
        {
            "domain": "landscout.planning_features.verified_gpu_sources.v1",
            "source_archive_sha256": planning_document.extraction.archive.sha256,
            "layers": [
                {
                    "logical_layer": source.logical_name,
                    "driver": source.driver,
                    "source_layer": source.source_layer,
                    "dataset_relative_path": source.dataset_relative_path,
                    "source_feature_count": source.feature_count,
                    "source_crs": source.source_crs,
                    "ogr_fids": list(source.ogr_fids),
                    "files": [
                        {
                            "relative_path": item.relative_path,
                            "file_type": item.file_type,
                            "size_bytes": item.size_bytes,
                            "sha256": item.sha256,
                            "category": item.category,
                        }
                        for item in sorted(
                            source.files, key=lambda value: value.relative_path
                        )
                    ],
                }
                for source in sorted(sources, key=lambda value: value.logical_name)
            ],
        }
    )


def _expected_relations_content_sha256(relations: pd.DataFrame) -> str:
    return _canonical_integrity_sha256(
        {
            "domain": "landscout.planning_features.expected_relations.v2",
            "schema": deterministic_frame_schema_signature(relations),
            "index": [
                _canonical_integrity_value(value) for value in relations.index.tolist()
            ],
            "rows": [
                [_canonical_integrity_value(value) for value in row]
                for row in relations.itertuples(index=False, name=None)
            ],
        }
    )


def _technical_tolerance(parcel_area: float) -> float:
    return technical_overlay_tolerance(parcel_area)


def _surface_union_summary(
    positive: pd.DataFrame,
    parcel_areas: np.ndarray,
    count: int,
) -> np.ndarray:
    output = np.zeros(count, dtype="float64")
    if positive.empty:
        return output
    for position_value, group in positive.groupby("_parcel_position", sort=False):
        position = int(position_value)
        try:
            value = float(
                shapely_area(union_all(group["_intersection_geometry"].to_numpy()))
            )
        except Exception as error:
            raise PlanningFeaturesError(
                "Surface covered-union calculation failed"
            ) from error
        if not isfinite(value) or value < 0:
            raise PlanningFeaturesError("Surface covered-union area is invalid")
        area = float(parcel_areas[position])
        if value > area:
            if value - area > _technical_tolerance(area):
                raise PlanningFeaturesError(
                    "Surface covered-union area exceeds parcel area"
                )
            value = area
        output[position] = value
    return output


def _attach_parcel_summaries(
    parcels: gpd.GeoDataFrame,
    metric: gpd.GeoDataFrame,
    surface_work: pd.DataFrame,
    line_work: pd.DataFrame,
    point_work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
    count = len(parcels)
    areas = metric["_parcel_area_m2"].to_numpy(dtype="float64")
    output = parcels.copy(deep=True)

    def relation_counts(
        frame: pd.DataFrame, mask: pd.Series | None = None
    ) -> np.ndarray:
        result = np.zeros(count, dtype="int64")
        selected = frame if mask is None else frame.loc[mask]
        if not selected.empty:
            counts = selected.groupby("_parcel_position", sort=False).size()
            result[counts.index.to_numpy(dtype="int64")] = counts.to_numpy(
                dtype="int64"
            )
        return result

    surface_positive = (
        surface_work.loc[surface_work["relation_type"] == "AREA_OVERLAP"]
        if not surface_work.empty
        else surface_work
    )
    surface_union = _surface_union_summary(surface_positive, areas, count)
    output["planning_surface_relation_count"] = relation_counts(surface_work)
    output["planning_surface_area_overlap_count"] = relation_counts(
        surface_work,
        surface_work["relation_type"].eq("AREA_OVERLAP")
        if not surface_work.empty
        else None,
    )
    output["planning_surface_touch_count"] = relation_counts(
        surface_work,
        surface_work["relation_type"].eq("TOUCH_ONLY")
        if not surface_work.empty
        else None,
    )
    raw_sum = np.zeros(count, dtype="float64")
    if not surface_positive.empty:
        sums = surface_positive.groupby("_parcel_position", sort=False)[
            "intersection_area_m2"
        ].sum()
        raw_sum[sums.index.to_numpy(dtype="int64")] = sums.to_numpy(dtype="float64")
    output["planning_surface_intersection_area_sum_m2"] = raw_sum
    output["planning_surface_covered_union_area_m2"] = surface_union
    output["planning_surface_covered_pct"] = np.where(
        surface_union == areas, 100.0, 100.0 * surface_union / areas
    )

    for family, prefix in (
        ("PRESCRIPTION", "prescription"),
        ("INFORMATION", "information"),
    ):
        family_work = (
            surface_work.loc[surface_work["feature_family"] == family]
            if not surface_work.empty
            else surface_work
        )
        family_positive = (
            family_work.loc[family_work["relation_type"] == "AREA_OVERLAP"]
            if not family_work.empty
            else family_work
        )
        union = _surface_union_summary(family_positive, areas, count)
        output[f"{prefix}_surface_relation_count"] = relation_counts(family_work)
        output[f"{prefix}_surface_covered_union_area_m2"] = union
        output[f"{prefix}_surface_covered_pct"] = np.where(
            union == areas, 100.0, 100.0 * union / areas
        )

    output["planning_line_relation_count"] = relation_counts(line_work)
    output["planning_line_length_overlap_count"] = relation_counts(
        line_work,
        line_work["relation_type"].eq("LENGTH_OVERLAP")
        if not line_work.empty
        else None,
    )
    output["planning_line_touch_count"] = relation_counts(
        line_work,
        line_work["relation_type"].eq("TOUCH_ONLY") if not line_work.empty else None,
    )
    line_sum = np.zeros(count, dtype="float64")
    if not line_work.empty:
        values = line_work.groupby("_parcel_position", sort=False)[
            "intersection_length_m"
        ].sum()
        line_sum[values.index.to_numpy(dtype="int64")] = values.to_numpy(
            dtype="float64"
        )
    output["planning_line_intersection_length_sum_m"] = line_sum

    output["planning_point_relation_count"] = relation_counts(point_work)
    for source, target in (
        ("point_members_inside_count", "planning_point_inside_count"),
        ("point_members_boundary_count", "planning_point_boundary_count"),
    ):
        values = np.zeros(count, dtype="int64")
        if not point_work.empty:
            grouped = point_work.groupby("_parcel_position", sort=False)[source].sum()
            values[grouped.index.to_numpy(dtype="int64")] = grouped.to_numpy(
                dtype="int64"
            )
        output[target] = values
    output["planning_feature_document_id"] = context.document_id
    output["planning_feature_archive_sha256"] = context.archive_sha256
    return output


def _numeric_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
    for column in columns:
        for value in frame[column].tolist():
            if pd.isna(value):
                if allow_null:
                    continue
                raise PlanningFeaturesError(f"{label} {column} must not be null")
            if isinstance(value, bool) or not isinstance(value, Real):
                raise PlanningFeaturesError(f"{label} {column} must be numeric")
            try:
                number = float(value)
            except (TypeError, ValueError, OverflowError) as error:
                raise PlanningFeaturesError(
                    f"{label} {column} must be finite"
                ) from error
            if not isfinite(number) or number < 0:
                raise PlanningFeaturesError(
                    f"{label} {column} must be finite and non-negative"
                )


def _integer_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
    for column in columns:
        for value in frame[column].tolist():
            if pd.isna(value):
                if allow_null:
                    continue
                raise PlanningFeaturesError(f"{label} {column} must not be null")
            _strict_nonnegative_integer(value, f"{label} {column}")


def _null_safe_equal(left: object, right: object) -> bool:
    try:
        left_missing = pd.isna(left)
        right_missing = pd.isna(right)
    except (TypeError, ValueError):
        return False
    if not isinstance(left_missing, (bool, np.bool_)) or not isinstance(
        right_missing, (bool, np.bool_)
    ):
        return False
    left_null = bool(left_missing)
    right_null = bool(right_missing)
    if left_null or right_null:
        return left_null and right_null
    try:
        return bool(left == right)
    except (TypeError, ValueError):
        return False


def _require_close(actual: object, expected: float, label: str) -> None:
    if isinstance(actual, bool) or not isinstance(actual, Real):
        raise PlanningFeaturesError(f"{label} must be numeric")
    try:
        number = float(actual)
    except (TypeError, ValueError, OverflowError) as error:
        raise PlanningFeaturesError(f"{label} must be finite") from error
    if not isfinite(number):
        raise PlanningFeaturesError(f"{label} must be finite")
    reference = max(abs(number), abs(expected))
    if abs(number - expected) > technical_overlay_tolerance(reference):
        raise PlanningFeaturesError(f"{label} is inconsistent")


def _validate_catalog_identity(catalog: gpd.GeoDataFrame) -> None:
    for column in _CATALOG_REQUIRED_EXACT_STRING_COLUMNS:
        _validate_exact_strings(
            catalog[column], f"Feature catalog {column.replace('_', ' ')}"
        )
    for column in _CATALOG_OPTIONAL_EXACT_STRING_COLUMNS:
        _validate_optional_exact_strings(
            catalog[column], f"Feature catalog {column.replace('_', ' ')}"
        )
    _validate_ids(catalog["planning_feature_id"], "planning_feature_id")
    for logical_layer, group in catalog.groupby("logical_layer", sort=False):
        _validate_ids(group["source_feature_id"], f"{logical_layer} source_feature_id")
    for _, row in catalog.iterrows():
        logical = _strict_string(row["logical_layer"], "logical_layer")
        if logical not in LAYER_SPECS:
            raise PlanningFeaturesError("Feature catalog logical layer is invalid")
        spec = LAYER_SPECS[logical]
        if row["feature_family"] != spec.feature_family:
            raise PlanningFeaturesError("Feature catalog family is inconsistent")
        if row["geometry_kind"] != spec.geometry_kind:
            raise PlanningFeaturesError(
                "Feature catalog logical layer and geometry kind are inconsistent"
            )
        expected_planning_id = (
            f"GPU:{row['source_document_id']}:{logical}:{row['source_feature_id']}"
        )
        if row["planning_feature_id"] != expected_planning_id:
            raise PlanningFeaturesError(
                "planning_feature_id differs from deterministic GPU identity"
            )
        kind = row["source_identity_kind"]
        field = row["source_identity_field"]
        if kind not in SOURCE_IDENTITY_KINDS:
            raise PlanningFeaturesError("Feature source identity kind is invalid")
        if kind == "CNIG_ATTRIBUTE":
            if field != spec.identity_field:
                raise PlanningFeaturesError(
                    "CNIG source identity field is inconsistent"
                )
        elif (
            logical != "prescription_surface"
            or field != "OGR_FID"
            or not str(row["source_feature_id"]).startswith("OGR_FID:")
        ):
            raise PlanningFeaturesError(
                "Archive-scoped OGR FID provenance is inconsistent"
            )


def _validate_catalog_contract(
    catalog: object,
    geometry_kind: GeometryKind,
) -> gpd.GeoDataFrame:
    label = f"{geometry_kind} feature catalog"
    if not isinstance(catalog, gpd.GeoDataFrame):
        raise PlanningFeaturesError(f"{label} must be a GeoDataFrame")
    try:
        validate_canonical_frame_schema(
            catalog,
            columns=NORMALIZED_FEATURE_COLUMNS[geometry_kind],
            dtypes=normalized_feature_dtypes(geometry_kind, catalog),
            label=label,
            geospatial=True,
            index_class="RangeIndex",
        )
    except (TypeError, ValueError) as error:
        raise PlanningFeaturesError(str(error)) from error
    _active_geometry(catalog, label)
    _validate_catalog_identity(catalog)
    if not catalog.empty and not catalog["geometry_kind"].eq(geometry_kind).all():
        raise PlanningFeaturesError(f"{label} geometry kind is invalid")
    _validate_geometries(catalog, _CATALOG_GEOMETRY_TYPES[geometry_kind], label)
    _validate_two_dimensional_geometry(catalog, label)
    if geometry_kind == "SURFACE":
        _numeric_values(
            catalog,
            ("feature_area_m2",),
            "Surface feature",
            allow_null=False,
        )
        if (catalog["feature_area_m2"] <= 0).any():
            raise PlanningFeaturesError("Surface feature areas must be positive")
        try:
            measured = catalog.geometry.area.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                "Surface feature metric validation failed"
            ) from error
        for actual, expected in zip(
            catalog["feature_area_m2"].tolist(), measured, strict=True
        ):
            _require_close(actual, float(expected), "feature_area_m2")
    elif geometry_kind == "LINE":
        _numeric_values(
            catalog,
            ("feature_length_m",),
            "Line feature",
            allow_null=False,
        )
        if (catalog["feature_length_m"] <= 0).any():
            raise PlanningFeaturesError("Line feature lengths must be positive")
        try:
            measured = catalog.geometry.length.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                "Line feature metric validation failed"
            ) from error
        for actual, expected in zip(
            catalog["feature_length_m"].tolist(), measured, strict=True
        ):
            _require_close(actual, float(expected), "feature_length_m")
    else:
        _integer_values(
            catalog,
            ("point_member_count",),
            "Point feature",
            allow_null=False,
        )
        if (catalog["point_member_count"] < 1).any():
            raise PlanningFeaturesError("Point features must contain a member")
        try:
            member_counts = [len(get_parts(value)) for value in catalog.geometry.array]
        except Exception as error:
            raise PlanningFeaturesError(
                "Point feature member validation failed"
            ) from error
        if catalog["point_member_count"].tolist() != member_counts:
            raise PlanningFeaturesError(
                "Point feature member count is inconsistent with geometry"
            )
    return catalog


def _compare_normalized_catalog(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
    if deterministic_frame_schema_signature(
        supplied
    ) != deterministic_frame_schema_signature(expected):
        raise PlanningFeaturesError(
            f"{label} schema differs from normalized GPU source"
        )
    try:
        supplied_crs = _crs(supplied.crs, label)
        expected_crs = _crs(expected.crs, f"expected {label}")
        geometry_equal = np.array_equal(
            supplied.geometry.to_wkb(), expected.geometry.to_wkb()
        )
        attributes_equal = supplied.drop(columns="geometry").equals(
            expected.drop(columns="geometry")
        )
    except PlanningFeaturesError:
        raise
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} cannot be compared with normalized GPU source"
        ) from error
    if (
        not supplied_crs.equals(expected_crs)
        or not geometry_equal
        or not attributes_equal
    ):
        raise PlanningFeaturesError(f"{label} differs from normalized GPU source")


_RELATION_CATALOG_FIELDS = (
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "label_raw",
    "text_raw",
    "source_document_id",
    "source_archive_sha256",
    "source_layer",
    "source_validity_date_raw",
    "regulation_filename_raw",
)


def _validate_relation_catalog_consistency(
    relations: pd.DataFrame,
    catalogs: tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame],
) -> None:
    feature_rows = pd.concat(
        [catalog.drop(columns="geometry") for catalog in catalogs],
        ignore_index=True,
    )
    if feature_rows["planning_feature_id"].duplicated().any():
        raise PlanningFeaturesError(
            "planning_feature_id values must be globally unique"
        )
    indexed = feature_rows.set_index("planning_feature_id", drop=False)
    for _, relation in relations.iterrows():
        identifier = relation["planning_feature_id"]
        if identifier not in indexed.index:
            raise PlanningFeaturesError(
                "Planning relation references an unknown feature"
            )
        feature = indexed.loc[identifier]
        for column in _RELATION_CATALOG_FIELDS:
            if not _null_safe_equal(relation[column], feature[column]):
                raise PlanningFeaturesError(
                    f"Relation {column} is inconsistent with feature catalog"
                )
        kind = relation["geometry_kind"]
        metric_column = {
            "SURFACE": "feature_area_m2",
            "LINE": "source_line_length_m",
            "POINT": "point_member_count",
        }.get(kind)
        catalog_column = {
            "SURFACE": "feature_area_m2",
            "LINE": "feature_length_m",
            "POINT": "point_member_count",
        }.get(kind)
        if (
            metric_column is None
            or catalog_column is None
            or not _null_safe_equal(relation[metric_column], feature[catalog_column])
        ):
            raise PlanningFeaturesError(
                "Relation feature metric is inconsistent with feature catalog"
            )


def _validate_relation_semantics(relations: pd.DataFrame) -> None:
    try:
        validate_intrinsic_planning_feature_relations(relations)
    except (TypeError, ValueError) as error:
        raise PlanningFeaturesError(str(error)) from error


def _compare_rebuilt_relations(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
) -> None:
    if deterministic_frame_schema_signature(
        supplied
    ) != deterministic_frame_schema_signature(expected):
        raise PlanningFeaturesError(
            "Planning relation schema differs from the spatial reconstruction"
        )
    if not supplied.index.equals(expected.index):
        raise PlanningFeaturesError(
            "Planning relation index or row order differs from the spatial reconstruction"
        )
    if len(supplied) != len(expected):
        raise PlanningFeaturesError(
            "Planning relation count differs from the spatial reconstruction"
        )
    for column in RELATION_COLUMNS:
        actual_values = supplied[column].tolist()
        expected_values = expected[column].tolist()
        for position, (actual, rebuilt) in enumerate(
            zip(actual_values, expected_values, strict=True)
        ):
            label = f"Planning relation {column} at row {position}"
            if column in RELATION_FLOAT_COLUMNS:
                actual_missing = bool(pd.isna(actual))
                expected_missing = bool(pd.isna(rebuilt))
                if actual_missing or expected_missing:
                    if actual_missing != expected_missing:
                        raise PlanningFeaturesError(
                            f"{label} null pattern differs from spatial reconstruction"
                        )
                    continue
                _require_close(actual, float(rebuilt), label)
            elif not _null_safe_equal(actual, rebuilt):
                raise PlanningFeaturesError(
                    f"{label} differs from the spatial reconstruction"
                )


def _compare_rebuilt_parcel_output(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
) -> None:
    if deterministic_frame_schema_signature(
        supplied
    ) != deterministic_frame_schema_signature(expected):
        raise PlanningFeaturesError(
            "Planning-feature parcel output schema differs from reconstruction"
        )
    if not supplied.index.equals(expected.index):
        raise PlanningFeaturesError(
            "Planning-feature parcel output index differs from reconstruction"
        )
    if not _crs(supplied.crs, "Parcel output").equals(
        _crs(expected.crs, "Expected parcel output")
    ) or not np.array_equal(supplied.geometry.to_wkb(), expected.geometry.to_wkb()):
        raise PlanningFeaturesError(
            "Planning-feature parcel geometry or CRS differs from reconstruction"
        )
    summary_float_columns = (
        PARCEL_OUTPUT_COLUMNS
        - PARCEL_COUNT_COLUMNS
        - {"planning_feature_document_id", "planning_feature_archive_sha256"}
    )
    for column in supplied.columns:
        if column == "geometry":
            continue
        if column in summary_float_columns:
            for position, (actual, rebuilt) in enumerate(
                zip(
                    supplied[column].tolist(),
                    expected[column].tolist(),
                    strict=True,
                )
            ):
                _require_close(
                    actual,
                    float(rebuilt),
                    f"Parcel summary {column} at row {position}",
                )
        elif not supplied[column].equals(expected[column]):
            raise PlanningFeaturesError(
                f"Planning-feature parcel column {column} differs from reconstruction"
            )


def _validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
    """Validate exact STEP 7D.3.1 facts against their document and parcels."""

    present_outputs = PARCEL_OUTPUT_COLUMNS & set(parcels.columns)
    if present_outputs and present_outputs != PARCEL_OUTPUT_COLUMNS:
        missing = sorted(PARCEL_OUTPUT_COLUMNS - present_outputs)
        raise PlanningFeaturesError(
            "Parcel planning-feature summaries are incomplete: " + ", ".join(missing)
        )
    _validate_parcels(parcels, allow_output_columns=True)
    source_parcels = (
        parcels.drop(columns=list(PARCEL_OUTPUT_COLUMNS))
        if present_outputs
        else parcels
    )
    _validate_parcels(source_parcels)
    metric_parcels = _metric_parcels(source_parcels)
    surfaces, lines, points, validated_sources = _normalized_catalogs(planning_document)
    expected_catalogs = (surfaces, lines, points)

    catalogs = (
        _validate_catalog_contract(surface_features, "SURFACE"),
        _validate_catalog_contract(line_features, "LINE"),
        _validate_catalog_contract(point_features, "POINT"),
    )
    for supplied, expected, label in zip(
        catalogs,
        expected_catalogs,
        ("SURFACE feature catalog", "LINE feature catalog", "POINT feature catalog"),
        strict=True,
    ):
        _compare_normalized_catalog(supplied, expected, label)
    all_feature_ids = [
        identifier
        for catalog in catalogs
        for identifier in catalog["planning_feature_id"].tolist()
    ]
    if len(all_feature_ids) != len(set(all_feature_ids)):
        raise PlanningFeaturesError(
            "planning_feature_id values must be globally unique"
        )

    if not isinstance(relations, pd.DataFrame) or isinstance(
        relations, gpd.GeoDataFrame
    ):
        raise PlanningFeaturesError("Planning relations must be a DataFrame")
    try:
        validate_canonical_frame_schema(
            relations,
            columns=RELATION_COLUMNS,
            dtypes=NORMALIZED_RELATION_DTYPES,
            label="Planning relations",
            geospatial=False,
            index_class="RangeIndex",
        )
    except (TypeError, ValueError) as error:
        raise PlanningFeaturesError(str(error)) from error
    _validate_exact_strings(relations["parcel_id"], "planning relation parcel_id")
    _validate_exact_strings(
        relations["planning_feature_id"], "planning relation planning_feature_id"
    )
    if relations.duplicated(["parcel_id", "planning_feature_id"]).any():
        raise PlanningFeaturesError("Parcel/planning-feature relations must be unique")
    if not set(relations["planning_feature_id"]).issubset(set(all_feature_ids)):
        raise PlanningFeaturesError("Planning relation references an unknown feature")
    parcel_areas = dict(
        zip(
            metric_parcels["parcel_id"].tolist(),
            metric_parcels["_parcel_area_m2"].tolist(),
            strict=True,
        )
    )
    for parcel_id, actual_area in relations[
        ["parcel_id", "parcel_metric_area_m2"]
    ].itertuples(index=False, name=None):
        if parcel_id not in parcel_areas:
            raise PlanningFeaturesError(
                "Planning relation references an unknown source parcel"
            )
        _require_close(
            actual_area,
            float(parcel_areas[parcel_id]),
            "Relation parcel metric area",
        )
    _validate_relation_semantics(relations)
    _validate_relation_catalog_consistency(relations, catalogs)
    surface_work, line_work, point_work, expected_relations = _build_relation_tables(
        metric_parcels, *expected_catalogs
    )
    _compare_rebuilt_relations(relations, expected_relations)

    if present_outputs:
        context = _planning_context(planning_document)
        expected_output = _attach_parcel_summaries(
            source_parcels,
            metric_parcels,
            surface_work,
            line_work,
            point_work,
            context,
        )
        _compare_rebuilt_parcel_output(parcels, expected_output)
        _validate_parcel_summaries(
            source_parcels, parcels, expected_relations, surface_work
        )
        if not parcels["planning_feature_document_id"].eq(context.document_id).all():
            raise PlanningFeaturesError(
                "Parcel planning-feature document lineage differs"
            )
        if (
            not parcels["planning_feature_archive_sha256"]
            .eq(context.archive_sha256)
            .all()
        ):
            raise PlanningFeaturesError(
                "Parcel planning-feature archive lineage differs"
            )

    unique_files = {
        item.relative_path for source in validated_sources for item in source.files
    }
    return PlanningFeatureInputValidation(
        gpu_related_source_files_sha256=_gpu_related_source_files_sha256(
            planning_document, validated_sources
        ),
        expected_relations_content_sha256=(
            _expected_relations_content_sha256(expected_relations)
        ),
        related_source_layer_count=len(validated_sources),
        related_source_file_count=len(unique_files),
        expected_relation_count=len(expected_relations),
    )


def validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
    """Validate exact STEP 7D.3.1 facts against their document and parcels."""

    try:
        return _validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
        )
    except PlanningFeaturesError:
        raise
    except Exception as error:
        raise PlanningFeaturesError(
            "Normalized planning-feature input validation failed safely"
        ) from error


def _validate_parcel_summaries(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    surface_work: pd.DataFrame | None,
) -> None:
    metric = _metric_parcels(source)
    metric_areas = dict(
        zip(
            metric["parcel_id"].tolist(),
            metric["_parcel_area_m2"].tolist(),
            strict=True,
        )
    )
    _integer_values(output, PARCEL_COUNT_COLUMNS, "Parcel summary", allow_null=False)
    float_columns = tuple(
        PARCEL_OUTPUT_COLUMNS
        - PARCEL_COUNT_COLUMNS
        - {"planning_feature_document_id", "planning_feature_archive_sha256"}
    )
    _numeric_values(output, float_columns, "Parcel summary", allow_null=False)

    for _, parcel in output.iterrows():
        parcel_id = parcel["parcel_id"]
        rows = relations.loc[relations["parcel_id"] == parcel_id]
        surfaces = rows.loc[rows["geometry_kind"] == "SURFACE"]
        positive_surfaces = surfaces.loc[surfaces["relation_type"] == "AREA_OVERLAP"]
        lines = rows.loc[rows["geometry_kind"] == "LINE"]
        points = rows.loc[rows["geometry_kind"] == "POINT"]
        exact_counts = {
            "planning_surface_relation_count": len(surfaces),
            "planning_surface_area_overlap_count": len(positive_surfaces),
            "planning_surface_touch_count": int(
                surfaces["relation_type"].eq("TOUCH_ONLY").sum()
            ),
            "prescription_surface_relation_count": int(
                surfaces["feature_family"].eq("PRESCRIPTION").sum()
            ),
            "information_surface_relation_count": int(
                surfaces["feature_family"].eq("INFORMATION").sum()
            ),
            "planning_line_relation_count": len(lines),
            "planning_line_length_overlap_count": int(
                lines["relation_type"].eq("LENGTH_OVERLAP").sum()
            ),
            "planning_line_touch_count": int(
                lines["relation_type"].eq("TOUCH_ONLY").sum()
            ),
            "planning_point_relation_count": len(points),
            "planning_point_inside_count": int(
                points["point_members_inside_count"].sum()
            ),
            "planning_point_boundary_count": int(
                points["point_members_boundary_count"].sum()
            ),
        }
        for column, expected in exact_counts.items():
            if parcel[column] != expected:
                raise PlanningFeaturesError(
                    f"Parcel summary {column} is inconsistent with relations"
                )
        raw_sum = float(positive_surfaces["intersection_area_m2"].sum())
        line_sum = float(lines["intersection_length_m"].sum())
        _require_close(
            parcel["planning_surface_intersection_area_sum_m2"],
            raw_sum,
            "planning_surface_intersection_area_sum_m2",
        )
        _require_close(
            parcel["planning_line_intersection_length_sum_m"],
            line_sum,
            "planning_line_intersection_length_sum_m",
        )
        parcel_area = float(metric_areas[parcel_id])
        planning_union = float(parcel["planning_surface_covered_union_area_m2"])
        if planning_union - raw_sum > technical_overlay_tolerance(raw_sum):
            raise PlanningFeaturesError("Surface union exceeds raw intersection sum")
        if planning_union - parcel_area > technical_overlay_tolerance(parcel_area):
            raise PlanningFeaturesError("Surface union exceeds parcel area")
        for prefix in ("planning", "prescription", "information"):
            union = float(parcel[f"{prefix}_surface_covered_union_area_m2"])
            pct = float(parcel[f"{prefix}_surface_covered_pct"])
            if union - planning_union > technical_overlay_tolerance(planning_union):
                raise PlanningFeaturesError("Family surface union exceeds total union")
            expected_pct = (
                100.0 if union == parcel_area else 100.0 * union / parcel_area
            )
            pct_tolerance = (
                100.0 * technical_overlay_tolerance(parcel_area) / parcel_area
            )
            if abs(pct - expected_pct) > pct_tolerance:
                raise PlanningFeaturesError(
                    f"{prefix} surface percentage is inconsistent"
                )

    if surface_work is not None:
        areas = metric["_parcel_area_m2"].to_numpy(dtype="float64")
        positive = (
            surface_work.loc[surface_work["relation_type"] == "AREA_OVERLAP"]
            if not surface_work.empty
            else surface_work
        )
        expected_total = _surface_union_summary(positive, areas, len(output))
        for family, column in (
            (None, "planning_surface_covered_union_area_m2"),
            ("PRESCRIPTION", "prescription_surface_covered_union_area_m2"),
            ("INFORMATION", "information_surface_covered_union_area_m2"),
        ):
            expected_union = expected_total
            if family is not None:
                family_rows = (
                    positive.loc[positive["feature_family"] == family]
                    if not positive.empty
                    else positive
                )
                expected_union = _surface_union_summary(family_rows, areas, len(output))
            for actual, value in zip(
                output[column].tolist(), expected_union, strict=True
            ):
                _require_close(actual, float(value), column)


def _validate_result(
    source: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
    surface_work: pd.DataFrame | None = None,
    *,
    planning_document: GpuPlanningDocument,
    source_inputs_already_rebuilt: bool = False,
) -> None:
    output = result.parcels
    missing_output = sorted(PARCEL_OUTPUT_COLUMNS - set(output.columns))
    if missing_output:
        raise PlanningFeaturesError(
            "Planning-feature parcel output is missing columns: "
            + ", ".join(missing_output)
        )
    if len(output) != len(source):
        raise PlanningFeaturesError("Planning-feature parcel count changed")
    if output["parcel_id"].tolist() != source["parcel_id"].tolist():
        raise PlanningFeaturesError("Planning-feature parcel IDs or order changed")
    if not output.index.equals(source.index):
        raise PlanningFeaturesError("Planning-feature parcel index changed")
    if output.crs != source.crs or not np.array_equal(
        output.geometry.to_wkb(), source.geometry.to_wkb()
    ):
        raise PlanningFeaturesError("Planning-feature parcel geometry or CRS changed")
    for column in source.columns:
        if column == "geometry":
            continue
        if not output[column].equals(source[column]):
            raise PlanningFeaturesError(f"Existing parcel column changed: {column}")

    catalogs = (
        result.surface_features,
        result.line_features,
        result.point_features,
    )
    if not source_inputs_already_rebuilt:
        validate_normalized_planning_feature_inputs(
            planning_document,
            source,
            *catalogs,
            result.relations,
        )
    all_feature_ids = [
        identifier
        for catalog in catalogs
        for identifier in catalog["planning_feature_id"].tolist()
    ]
    known_features = set(all_feature_ids)

    relations = result.relations
    if not set(relations["parcel_id"]).issubset(set(output["parcel_id"])):
        raise PlanningFeaturesError("Planning relation references an unknown parcel")
    if not set(relations["planning_feature_id"]).issubset(known_features):
        raise PlanningFeaturesError("Planning relation references an unknown feature")
    _validate_parcel_summaries(source, output, relations, surface_work)
    for column in (
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
    ):
        _validate_exact_strings(output[column], column)
    nonempty_catalogs = [catalog for catalog in catalogs if not catalog.empty]
    if nonempty_catalogs:
        expected_document_ids = {
            value
            for catalog in nonempty_catalogs
            for value in catalog["source_document_id"].tolist()
        }
        expected_archive_hashes = {
            value
            for catalog in nonempty_catalogs
            for value in catalog["source_archive_sha256"].tolist()
        }
        if (
            len(expected_document_ids) != 1
            or len(expected_archive_hashes) != 1
            or set(output["planning_feature_document_id"]) != expected_document_ids
            or set(output["planning_feature_archive_sha256"]) != expected_archive_hashes
        ):
            raise PlanningFeaturesError(
                "Parcel planning-feature lineage is inconsistent with catalogs"
            )


def intersect_parcels_with_gpu_planning_features(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelPlanningFeaturesResult:
    """Measure factual GPU prescription/information relations to full parcels.

    All metric work is planar XY in EPSG:2154.  Raw codes are preserved without
    interpretation, and every pre-existing parcel field and geometry is copied.
    """

    _validate_parcels(parcels)
    context = _planning_context(planning_document)
    surfaces, lines, points, _ = _normalized_catalogs(planning_document)
    metric = _metric_parcels(parcels)
    surface_work, line_work, point_work, relations = _build_relation_tables(
        metric, surfaces, lines, points
    )
    parcel_output = _attach_parcel_summaries(
        parcels, metric, surface_work, line_work, point_work, context
    )
    result = ParcelPlanningFeaturesResult(
        parcels=parcel_output,
        surface_features=surfaces,
        line_features=lines,
        point_features=points,
        relations=relations,
    )
    _validate_result(
        parcels,
        result,
        surface_work,
        planning_document=planning_document,
        source_inputs_already_rebuilt=True,
    )
    return result
