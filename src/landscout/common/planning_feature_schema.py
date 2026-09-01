"""Internal canonical schemas for normalized, coded, and applied planning facts."""

from __future__ import annotations

from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS

GeometryKind = Literal["SURFACE", "LINE", "POINT"]
IndexClass = Literal["Index", "RangeIndex"]

COMMON_FEATURE_COLUMNS = (
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
SURFACE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_area_m2")
LINE_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "feature_length_m")
POINT_FEATURE_COLUMNS = (*COMMON_FEATURE_COLUMNS, "geometry", "point_member_count")
NORMALIZED_FEATURE_COLUMNS = {
    "SURFACE": SURFACE_FEATURE_COLUMNS,
    "LINE": LINE_FEATURE_COLUMNS,
    "POINT": POINT_FEATURE_COLUMNS,
}

RELATION_COLUMNS = (
    "parcel_id",
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
RELATION_STRING_COLUMNS = (
    frozenset(RELATION_COLUMNS) - RELATION_FLOAT_COLUMNS - (RELATION_COUNT_COLUMNS)
)

OFFICIAL_CODE_COLUMNS = (
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)

_COMMON_STR_DTYPES = {
    column: "str"
    for column in COMMON_FEATURE_COLUMNS
    if column not in {"text_raw", "regulation_filename_raw", "regulation_url_raw"}
}
NORMALIZED_FEATURE_DTYPES: dict[GeometryKind, tuple[str, ...]] = {
    "SURFACE": tuple(
        {
            **_COMMON_STR_DTYPES,
            "text_raw": "str",
            "regulation_filename_raw": "str",
            "regulation_url_raw": "object",
            "geometry": "geometry",
            "feature_area_m2": "float64",
        }[column]
        for column in SURFACE_FEATURE_COLUMNS
    ),
    "LINE": tuple(
        {
            **_COMMON_STR_DTYPES,
            "text_raw": "object",
            "regulation_filename_raw": "object",
            "regulation_url_raw": "object",
            "geometry": "geometry",
            "feature_length_m": "float64",
        }[column]
        for column in LINE_FEATURE_COLUMNS
    ),
    "POINT": tuple(
        {
            **_COMMON_STR_DTYPES,
            "text_raw": "object",
            "regulation_filename_raw": "object",
            "regulation_url_raw": "object",
            "geometry": "geometry",
            "point_member_count": "int64",
        }[column]
        for column in POINT_FEATURE_COLUMNS
    ),
}
NORMALIZED_RELATION_DTYPES = tuple(
    "float64"
    if column in RELATION_FLOAT_COLUMNS
    else "Int64"
    if column in RELATION_COUNT_COLUMNS
    else "str"
    for column in RELATION_COLUMNS
)
OFFICIAL_CODE_DTYPES = tuple("str" for _ in OFFICIAL_CODE_COLUMNS)


def normalized_feature_dtypes(
    geometry_kind: GeometryKind,
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
    """Return exact factual dtypes, including deterministic all-null raw fields."""

    dtypes = list(NORMALIZED_FEATURE_DTYPES[geometry_kind])
    if frame is None or frame.empty:
        return tuple(dtypes)
    # Pandas/Parquet preserve an all-null optional raw source field as object. The
    # null pattern is factual input, so it is the sole deterministic variant.
    for column in ("text_raw", "regulation_filename_raw", "regulation_url_raw"):
        if column not in frame.columns:
            continue
        position = NORMALIZED_FEATURE_COLUMNS[geometry_kind].index(column)
        dtypes[position] = "object" if frame[column].isna().all() else "str"
    return tuple(dtypes)


def feature_columns(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
) -> tuple[str, ...]:
    """Return one exact ordered feature schema with deterministic suffixes."""

    return (*NORMALIZED_FEATURE_COLUMNS[geometry_kind], *OFFICIAL_CODE_COLUMNS, *suffix)


def feature_dtypes(
    geometry_kind: GeometryKind,
    suffix: tuple[str, ...] = (),
    frame: pd.DataFrame | None = None,
) -> tuple[str, ...]:
    """Return matching exact feature dtypes with deterministic suffixes."""

    return (
        *normalized_feature_dtypes(geometry_kind, frame),
        *OFFICIAL_CODE_DTYPES,
        *suffix,
    )


def relation_columns(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Return one exact ordered relation schema with deterministic suffixes."""

    return (*RELATION_COLUMNS, *OFFICIAL_CODE_COLUMNS, *suffix)


def relation_dtypes(suffix: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Return matching exact relation dtypes with deterministic suffixes."""

    return (*NORMALIZED_RELATION_DTYPES, *OFFICIAL_CODE_DTYPES, *suffix)


def validate_canonical_frame_schema(
    frame: pd.DataFrame,
    *,
    columns: tuple[str, ...],
    dtypes: tuple[str, ...],
    label: str,
    geospatial: bool,
    index_class: IndexClass = "Index",
) -> None:
    """Reject any deviation from one complete persisted frame-schema contract."""

    if not isinstance(frame, pd.DataFrame):
        raise TypeError(f"{label} must be a DataFrame")
    if frame.columns.duplicated().any():
        raise ValueError(f"{label} contains duplicate columns")
    if (
        tuple(frame.columns) != columns
        or tuple(str(dtype) for dtype in frame.dtypes) != dtypes
    ):
        raise ValueError(f"{label} canonical column, geometry, or dtype schema differs")
    index = frame.index
    expected_index_type = pd.Index if index_class == "Index" else pd.RangeIndex
    if (
        type(index) is not expected_index_type
        or list(index.names) != [None]
        or str(index.dtype) != "int64"
    ):
        raise ValueError(f"{label} canonical index schema differs")
    if index_class == "RangeIndex" and (
        index.start != 0 or index.stop != len(frame) or index.step != 1
    ):
        raise ValueError(f"{label} canonical range index differs")
    if geospatial:
        if not isinstance(frame, gpd.GeoDataFrame):
            raise TypeError(f"{label} must be a GeoDataFrame")
        if frame.geometry.name != "geometry" or frame.crs is None:
            raise ValueError(f"{label} canonical geometry or CRS metadata differs")
        try:
            canonical_crs = CRS.from_user_input(frame.crs).equals(CRS.from_epsg(2154))
        except Exception as error:
            raise ValueError(f"{label} canonical CRS is invalid") from error
        if not canonical_crs:
            raise ValueError(f"{label} canonical CRS differs from EPSG:2154")
    elif isinstance(frame, gpd.GeoDataFrame):
        raise TypeError(f"{label} must not be a GeoDataFrame")
