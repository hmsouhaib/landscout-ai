"""Normalize and intersect factual GPU prescription/information features."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from numbers import Real
from pathlib import Path
from typing import Literal, NamedTuple

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import (  # type: ignore[import-untyped]
    area as shapely_area,
)
from shapely import (
    contains,
    covers,
    force_2d,
    get_parts,
    intersection,
    union_all,
)
from shapely import (
    length as shapely_length,
)

from landscout.sources.gpu_fr import GpuInspectedLayer, GpuPlanningDocument
from landscout.stages.enrich_planning_zoning import (
    _AREA_ABSOLUTE_TOLERANCE_M2,
    _AREA_RELATIVE_TOLERANCE,
)

__all__ = ["intersect_parcels_with_gpu_planning_features"]

CALCULATION_CRS = "EPSG:2154"
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})

FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
GeometryKind = Literal["SURFACE", "LINE", "POINT"]

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

COMMON_FEATURE_COLUMNS = (
    "planning_feature_id",
    "source_feature_id",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "label_raw",
    "text_raw",
    "regulation_filename_raw",
    "regulation_url_raw",
    "source_document_reference_raw",
    "source_validity_date_raw",
    "source_provider",
    "source_portal",
    "source_commune_code",
    "source_document_id",
    "source_document_type",
    "source_archive_name",
    "source_archive_sha256",
    "source_layer",
    "source_standard_model",
    "source_crs",
)

RELATION_COLUMNS = (
    "parcel_id",
    "planning_feature_id",
    "source_feature_id",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "label_raw",
    "text_raw",
    "relation_type",
    "parcel_metric_area_m2",
    "feature_area_m2",
    "source_line_length_m",
    "intersection_area_m2",
    "intersection_length_m",
    "parcel_share_pct",
    "feature_share_pct",
    "point_member_count",
    "point_members_inside_count",
    "point_members_boundary_count",
    "source_document_id",
    "source_archive_sha256",
    "source_layer",
    "source_validity_date_raw",
    "regulation_filename_raw",
)

RELATION_FLOAT_COLUMNS = frozenset(
    {
        "parcel_metric_area_m2",
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
    }
)
RELATION_COUNT_COLUMNS = frozenset(
    {
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    }
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


def _validate_ids(values: pd.Series, label: str) -> None:
    if values.isna().any():
        raise PlanningFeaturesError(f"{label} values must not be null")
    for value in values.tolist():
        _strict_string(value, label)
    if values.duplicated().any():
        raise PlanningFeaturesError(f"{label} values must be unique")


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


def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise PlanningFeaturesError("Parcels must be a GeoDataFrame")
    missing = sorted(PARCEL_REQUIRED_COLUMNS - set(parcels.columns))
    if missing:
        raise PlanningFeaturesError(
            "Parcels are missing required columns: " + ", ".join(missing)
        )
    collisions = sorted(PARCEL_OUTPUT_COLUMNS & set(parcels.columns))
    if collisions:
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
        or summary.invalid_geometry_count
        != int((non_empty & ~geometry.is_valid).sum())
    ):
        raise PlanningFeaturesError(
            f"{layer.logical_name} source summary is inconsistent with loaded data"
        )


def _project_geometry(frame: gpd.GeoDataFrame, label: str) -> gpd.GeoSeries:
    source = _crs(frame.crs, label)
    target = CRS.from_epsg(2154)
    try:
        projected = frame.geometry.copy() if source.equals(target) else frame.to_crs(target).geometry
        return gpd.GeoSeries(force_2d(projected.array), crs=target)
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} CRS cannot be transformed safely to EPSG:2154"
        ) from error


def _read_ogr_fids(layer: GpuInspectedLayer) -> pd.Series:
    """Read source-driver FIDs, not mutable GeoDataFrame index labels.

    The current official prescription-surface Shapefile omits `LIB_IDPSC`.
    Its OGR feature identifier is therefore the only source-record identity.
    It is tied to the immutable archive/layer lineage and validated against a
    fresh read of every source row before use.
    """

    path = layer.reference.dataset_path
    if not isinstance(path, Path) or not path.is_file():
        raise PlanningFeaturesError(
            f"{layer.logical_name} has no identity field and source FIDs are unavailable"
        )
    try:
        reread = pyogrio.read_dataframe(
            path,
            layer=layer.reference.source_layer,
            fid_as_index=True,
        )
    except Exception as error:
        raise PlanningFeaturesError(
            f"{layer.logical_name} source FIDs cannot be read"
        ) from error
    if len(reread) != len(layer.data) or not np.array_equal(
        reread.geometry.to_wkb(), layer.data.geometry.to_wkb()
    ):
        raise PlanningFeaturesError(
            f"{layer.logical_name} source FID order does not match loaded data"
        )
    common = [column for column in layer.data.columns if column != "geometry"]
    if common and not reread[common].reset_index(drop=True).equals(
        layer.data[common].reset_index(drop=True)
    ):
        raise PlanningFeaturesError(
            f"{layer.logical_name} source attributes changed since inspection"
        )
    values = pd.Series(
        [f"OGR_FID:{value}" for value in reread.index.tolist()], dtype="object"
    )
    _validate_ids(values, f"{layer.logical_name} OGR FID")
    return values


def _source_feature_ids(layer: GpuInspectedLayer, spec: _LayerSpec) -> pd.Series:
    if spec.identity_field in layer.data.columns:
        result = layer.data[spec.identity_field].reset_index(drop=True).copy()
        _validate_ids(result, spec.identity_field)
        return result
    if spec.logical_layer == "prescription_surface":
        return _read_ogr_fids(layer)
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
) -> gpd.GeoDataFrame:
    frame = layer.data
    if not isinstance(frame, gpd.GeoDataFrame) or frame.empty:
        raise PlanningFeaturesError(f"{spec.logical_layer} must be a non-empty GeoDataFrame")
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
            raise PlanningFeaturesError(f"{spec.logical_layer} {field} must not be null")
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

    source_ids = _source_feature_ids(layer, spec)
    planning_ids = source_ids.map(
        lambda value: (
            f"GPU:{context.document_id}:{spec.logical_layer}:{value}"
        )
    )
    geometry = _project_geometry(frame, spec.logical_layer)
    projected = gpd.GeoDataFrame(
        {
            "planning_feature_id": planning_ids.to_numpy(copy=True),
            "source_feature_id": source_ids.to_numpy(copy=True),
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
        values = projected.geometry.area.to_numpy(dtype="float64")
        if not np.isfinite(values).all() or (values <= 0).any():
            raise PlanningFeaturesError(f"{spec.logical_layer} areas must be positive")
        projected["feature_area_m2"] = values
    elif spec.geometry_kind == "LINE":
        values = projected.geometry.length.to_numpy(dtype="float64")
        if not np.isfinite(values).all() or (values <= 0).any():
            raise PlanningFeaturesError(f"{spec.logical_layer} lengths must be positive")
        projected["feature_length_m"] = values
    else:
        projected["point_member_count"] = [
            len(get_parts(value)) for value in projected.geometry.array
        ]
    return projected


def _empty_catalog(kind: GeometryKind) -> gpd.GeoDataFrame:
    data = {column: pd.Series(dtype="object") for column in COMMON_FEATURE_COLUMNS}
    if kind == "SURFACE":
        data["feature_area_m2"] = pd.Series(dtype="float64")
    elif kind == "LINE":
        data["feature_length_m"] = pd.Series(dtype="float64")
    else:
        data["point_member_count"] = pd.Series(dtype="int64")
    return gpd.GeoDataFrame(data, geometry=gpd.GeoSeries([], crs=CALCULATION_CRS))


def _combine_catalogs(
    frames: list[gpd.GeoDataFrame], kind: GeometryKind
) -> gpd.GeoDataFrame:
    if not frames:
        return _empty_catalog(kind)
    combined = gpd.GeoDataFrame(
        pd.concat(frames, ignore_index=True), geometry="geometry", crs=CALCULATION_CRS
    )
    _validate_ids(combined["planning_feature_id"], "planning_feature_id")
    return combined


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
    areas = result.geometry.area.to_numpy(dtype="float64")
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
            "source_validity_date_raw": selected[
                "source_validity_date_raw"
            ].to_numpy(copy=True),
            "regulation_filename_raw": selected[
                "regulation_filename_raw"
            ].to_numpy(copy=True),
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
    geometries = intersection(
        metric.geometry.iloc[parcel_positions].array,
        catalog.geometry.iloc[feature_positions].array,
    )
    areas = np.asarray(shapely_area(geometries), dtype="float64")
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
    geometries = intersection(
        metric.geometry.iloc[parcel_positions].array,
        catalog.geometry.iloc[feature_positions].array,
    )
    lengths = np.asarray(shapely_length(geometries), dtype="float64")
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
    base["relation_type"] = np.where(
        inside_counts > 0, "INSIDE", "BOUNDARY_TOUCH"
    )
    for column in RELATION_FLOAT_COLUMNS - {"parcel_metric_area_m2"}:
        base[column] = np.nan
    base["point_member_count"] = pd.array(member_counts, dtype="Int64")
    base["point_members_inside_count"] = pd.array(inside_counts, dtype="Int64")
    base["point_members_boundary_count"] = pd.array(boundary_counts, dtype="Int64")
    return base


def _empty_relations() -> pd.DataFrame:
    return pd.DataFrame(
        {
            column: pd.Series(
                dtype=(
                    "float64"
                    if column in RELATION_FLOAT_COLUMNS
                    else "Int64"
                    if column in RELATION_COUNT_COLUMNS
                    else "object"
                )
            )
            for column in RELATION_COLUMNS
        }
    )


def _technical_tolerance(parcel_area: float) -> float:
    return max(
        _AREA_ABSOLUTE_TOLERANCE_M2,
        parcel_area * _AREA_RELATIVE_TOLERANCE,
    )


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
        value = float(shapely_area(union_all(group["_intersection_geometry"].to_numpy())))
        if not isfinite(value) or value < 0:
            raise PlanningFeaturesError("Surface covered-union area is invalid")
        area = float(parcel_areas[position])
        if value > area:
            if value - area > _technical_tolerance(area):
                raise PlanningFeaturesError("Surface covered-union area exceeds parcel area")
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

    def relation_counts(frame: pd.DataFrame, mask: pd.Series | None = None) -> np.ndarray:
        result = np.zeros(count, dtype="int64")
        selected = frame if mask is None else frame.loc[mask]
        if not selected.empty:
            counts = selected.groupby("_parcel_position", sort=False).size()
            result[counts.index.to_numpy(dtype="int64")] = counts.to_numpy(dtype="int64")
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
        surface_work["relation_type"].eq("AREA_OVERLAP") if not surface_work.empty else None,
    )
    output["planning_surface_touch_count"] = relation_counts(
        surface_work,
        surface_work["relation_type"].eq("TOUCH_ONLY") if not surface_work.empty else None,
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
        line_work["relation_type"].eq("LENGTH_OVERLAP") if not line_work.empty else None,
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
        line_sum[values.index.to_numpy(dtype="int64")] = values.to_numpy(dtype="float64")
    output["planning_line_intersection_length_sum_m"] = line_sum

    output["planning_point_relation_count"] = relation_counts(point_work)
    for source, target in (
        ("point_members_inside_count", "planning_point_inside_count"),
        ("point_members_boundary_count", "planning_point_boundary_count"),
    ):
        values = np.zeros(count, dtype="int64")
        if not point_work.empty:
            grouped = point_work.groupby("_parcel_position", sort=False)[source].sum()
            values[grouped.index.to_numpy(dtype="int64")] = grouped.to_numpy(dtype="int64")
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
                raise PlanningFeaturesError(f"{label} {column} must be finite") from error
            if not isfinite(number) or number < 0:
                raise PlanningFeaturesError(
                    f"{label} {column} must be finite and non-negative"
                )


def _validate_result(
    source: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
) -> None:
    output = result.parcels
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
    known_features: set[str] = set()
    for catalog in catalogs:
        if not _crs(catalog.crs, "Feature catalog").equals(CRS.from_epsg(2154)):
            raise PlanningFeaturesError("Feature catalog must use EPSG:2154")
        _validate_ids(catalog["planning_feature_id"], "planning_feature_id")
        known_features.update(catalog["planning_feature_id"].tolist())

    relations = result.relations
    if tuple(relations.columns) != RELATION_COLUMNS:
        raise PlanningFeaturesError("Planning relation schema is not deterministic")
    if relations.duplicated(["parcel_id", "planning_feature_id"]).any():
        raise PlanningFeaturesError("Parcel/planning-feature relations must be unique")
    if not set(relations["parcel_id"]).issubset(set(output["parcel_id"])):
        raise PlanningFeaturesError("Planning relation references an unknown parcel")
    if not set(relations["planning_feature_id"]).issubset(known_features):
        raise PlanningFeaturesError("Planning relation references an unknown feature")
    _numeric_values(relations, RELATION_FLOAT_COLUMNS, "Relation", allow_null=True)
    _numeric_values(relations, RELATION_COUNT_COLUMNS, "Relation", allow_null=True)
    for _, row in relations.iterrows():
        kind = row["geometry_kind"]
        relation_type = row["relation_type"]
        required: tuple[str, ...]
        null_only: tuple[str, ...]
        if kind == "SURFACE":
            if relation_type not in {"AREA_OVERLAP", "TOUCH_ONLY"}:
                raise PlanningFeaturesError("Surface relation type is invalid")
            required = (
                "feature_area_m2",
                "intersection_area_m2",
                "parcel_share_pct",
                "feature_share_pct",
            )
            null_only = (
                "source_line_length_m",
                "intersection_length_m",
                *RELATION_COUNT_COLUMNS,
            )
            parcel_area = float(row["parcel_metric_area_m2"])
            feature_area = float(row["feature_area_m2"])
            intersection_area = float(row["intersection_area_m2"])
            if intersection_area - parcel_area > _technical_tolerance(parcel_area):
                raise PlanningFeaturesError("Surface parcel share exceeds 100 percent")
            if intersection_area - feature_area > _technical_tolerance(feature_area):
                raise PlanningFeaturesError("Surface feature share exceeds 100 percent")
        elif kind == "LINE":
            if relation_type not in {"LENGTH_OVERLAP", "TOUCH_ONLY"}:
                raise PlanningFeaturesError("Line relation type is invalid")
            required = ("source_line_length_m", "intersection_length_m")
            null_only = (
                "feature_area_m2",
                "intersection_area_m2",
                "parcel_share_pct",
                "feature_share_pct",
                *RELATION_COUNT_COLUMNS,
            )
        elif kind == "POINT":
            if relation_type not in {"INSIDE", "BOUNDARY_TOUCH"}:
                raise PlanningFeaturesError("Point relation type is invalid")
            required = tuple(RELATION_COUNT_COLUMNS)
            null_only = (
                "feature_area_m2",
                "source_line_length_m",
                "intersection_area_m2",
                "intersection_length_m",
                "parcel_share_pct",
                "feature_share_pct",
            )
            member_count = int(row["point_member_count"])
            inside = int(row["point_members_inside_count"])
            boundary_count = int(row["point_members_boundary_count"])
            if member_count < 1 or inside + boundary_count < 1:
                raise PlanningFeaturesError("Point relation member counts are invalid")
            if inside + boundary_count > member_count:
                raise PlanningFeaturesError("Point covered members exceed source members")
        else:
            raise PlanningFeaturesError("Planning relation geometry kind is invalid")
        if any(pd.isna(row[column]) for column in required):
            raise PlanningFeaturesError(f"{kind} relation has a missing required metric")
        if any(not pd.isna(row[column]) for column in null_only):
            raise PlanningFeaturesError(f"{kind} relation populated an unrelated metric")
    summary_numeric = tuple(PARCEL_OUTPUT_COLUMNS - {
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
    })
    _numeric_values(output, summary_numeric, "Parcel summary", allow_null=False)


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
    layer_map: dict[str, GpuInspectedLayer] = {}
    for inspected_layer in planning_document.related_layers:
        logical = str(inspected_layer.logical_name)
        if logical not in LAYER_SPECS:
            raise PlanningFeaturesError(f"Unsupported related layer: {logical}")
        if logical in layer_map:
            raise PlanningFeaturesError(f"Duplicate related layer: {logical}")
        layer_map[logical] = inspected_layer

    normalized: list[gpd.GeoDataFrame] = []
    for logical, spec in LAYER_SPECS.items():
        layer = layer_map.get(logical)
        if layer is not None:
            normalized.append(_normalize_layer(layer, spec, context))

    surfaces = _combine_catalogs(
        [frame for frame in normalized if frame["geometry_kind"].iloc[0] == "SURFACE"],
        "SURFACE",
    )
    lines = _combine_catalogs(
        [frame for frame in normalized if frame["geometry_kind"].iloc[0] == "LINE"],
        "LINE",
    )
    points = _combine_catalogs(
        [frame for frame in normalized if frame["geometry_kind"].iloc[0] == "POINT"],
        "POINT",
    )
    metric = _metric_parcels(parcels)
    surface_work = _surface_relations(metric, surfaces)
    line_work = _line_relations(metric, lines)
    point_work = _point_relations(metric, points)
    work_frames = [frame for frame in (surface_work, line_work, point_work) if not frame.empty]
    if work_frames:
        combined = pd.concat(work_frames, ignore_index=True)
        combined = combined.sort_values(
            ["_parcel_position", "planning_feature_id"], kind="stable"
        ).reset_index(drop=True)
        relations = combined.loc[:, RELATION_COLUMNS].copy()
        for column in RELATION_COUNT_COLUMNS:
            relations[column] = pd.array(relations[column], dtype="Int64")
    else:
        relations = _empty_relations()
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
    _validate_result(parcels, result)
    return result
