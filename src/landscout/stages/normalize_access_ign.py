"""Normalize factual IGN BD TOPO roads into a stable access-domain catalog."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pydantic import HttpUrl, TypeAdapter, ValidationError
from pyproj import CRS

from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)

__all__ = [
    "IgnRoadNormalizationError",
    "NormalizedIgnRoadData",
    "normalize_ign_roads",
]

_SOURCE_PROVIDER = "IGN"
_SOURCE_PRODUCT = "BD_TOPO"
_SPATIAL_ROLE = "PROXY_GEOMETRY"
_ROAD_FEATURE_TYPE = "ROAD_SEGMENT"

_OUTPUT_COLUMNS = (
    "road_feature_id",
    "road_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
    "nature_raw",
    "importance_raw",
    "fictitious_raw",
    "position_relative_to_ground_raw",
    "asset_status_raw",
    "lane_count_raw",
    "carriageway_width_raw",
    "private_raw",
    "traffic_direction_raw",
    "urban_raw",
    "mean_light_vehicle_speed_raw",
    "light_vehicle_access_raw",
    "closure_period_raw",
    "restriction_nature_raw",
    "restriction_height_raw",
    "restriction_total_weight_raw",
    "restriction_axle_weight_raw",
    "restriction_width_raw",
    "restriction_length_raw",
    "dangerous_goods_forbidden_raw",
    "administrative_classification_raw",
    "manager_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_raw",
    "spatial_role",
    "geometry_status",
    "geometry",
)

_RAW_FIELD_MAPPING = (
    ("nature", "nature_raw"),
    ("importance", "importance_raw"),
    ("fictif", "fictitious_raw"),
    ("position_par_rapport_au_sol", "position_relative_to_ground_raw"),
    ("etat_de_l_objet", "asset_status_raw"),
    ("nombre_de_voies", "lane_count_raw"),
    ("largeur_de_chaussee", "carriageway_width_raw"),
    ("prive", "private_raw"),
    ("sens_de_circulation", "traffic_direction_raw"),
    ("urbain", "urban_raw"),
    ("vitesse_moyenne_vl", "mean_light_vehicle_speed_raw"),
    ("acces_vehicule_leger", "light_vehicle_access_raw"),
    ("periode_de_fermeture", "closure_period_raw"),
    ("nature_de_la_restriction", "restriction_nature_raw"),
    ("restriction_de_hauteur", "restriction_height_raw"),
    ("restriction_de_poids_total", "restriction_total_weight_raw"),
    ("restriction_de_poids_par_essieu", "restriction_axle_weight_raw"),
    ("restriction_de_largeur", "restriction_width_raw"),
    ("restriction_de_longueur", "restriction_length_raw"),
    ("matieres_dangereuses_interdites", "dangerous_goods_forbidden_raw"),
    ("cpx_classement_administratif", "administrative_classification_raw"),
    ("cpx_gestionnaire", "manager_raw"),
    ("sources", "source_name_raw"),
    ("identifiants_sources", "source_identifiers_raw"),
    ("date_creation", "source_created_at"),
    ("date_modification", "source_modified_at"),
    ("date_de_confirmation", "source_confirmed_at"),
    ("methode_d_acquisition_planimetrique", "planimetric_acquisition_method"),
    ("precision_planimetrique", "planimetric_precision_raw"),
)
_REQUIRED_SOURCE_FIELDS = frozenset(
    {"cleabs", "geometry", *(source for source, _ in _RAW_FIELD_MAPPING)}
)
_ROAD_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
_DEPARTMENT_CODE_VALIDATOR = TypeAdapter(DepartmentCode)
_EDITION_VALIDATOR = TypeAdapter(EditionString)
_HTTP_URL_VALIDATOR = TypeAdapter(HttpUrl)
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institut national de l information geographique et forestiere",
        "institut national de l information geographique et forestiere ign",
    }
)


class IgnRoadNormalizationError(ValueError):
    """Raised when factual IGN road data cannot be normalized safely."""


@dataclass(frozen=True)
class _IgnRoadSourceContext:
    source_layer: str
    department_code: str
    edition: str
    product_version: str | None
    download_timestamp: str
    archive_sha256: str
    source_url: str


@dataclass(frozen=True)
class NormalizedIgnRoadData:
    """Stable factual IGN road catalog with no access-policy interpretation."""

    road_segments: gpd.GeoDataFrame


def _validated_lambert93(crs_value: object, label: str) -> CRS:
    if crs_value is None:
        raise IgnRoadNormalizationError(f"{label} CRS is required")
    try:
        source_crs = CRS.from_user_input(crs_value)
    except Exception as error:
        raise IgnRoadNormalizationError(f"{label} CRS is unreadable") from error
    expected_crs = CRS.from_epsg(2154)
    if not source_crs.is_projected or not source_crs.equals(expected_crs):
        raise IgnRoadNormalizationError(f"{label} must use EPSG:2154")
    return source_crs


def _required_exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnRoadNormalizationError(f"IGN road {label} must be a string")
    if value != value.strip():
        raise IgnRoadNormalizationError(
            f"IGN road {label} must not contain edge whitespace"
        )
    return value


def _validate_source_context(context: _IgnRoadSourceContext) -> None:
    _required_exact_string(context.source_layer, "source_layer")
    department_code = _required_exact_string(context.department_code, "department_code")
    edition = _required_exact_string(context.edition, "edition")
    timestamp_raw = _required_exact_string(
        context.download_timestamp, "download_timestamp"
    )
    archive_sha256 = _required_exact_string(context.archive_sha256, "archive_sha256")
    source_url = _required_exact_string(context.source_url, "source_url")

    try:
        validated_department = _DEPARTMENT_CODE_VALIDATOR.validate_python(
            department_code
        )
    except ValidationError as error:
        raise IgnRoadNormalizationError(
            "IGN road department_code is invalid"
        ) from error
    if validated_department != department_code:
        raise IgnRoadNormalizationError(
            "IGN road department_code must not be rewritten"
        )

    try:
        validated_edition = _EDITION_VALIDATOR.validate_python(edition)
        date.fromisoformat(validated_edition)
    except (ValidationError, ValueError) as error:
        raise IgnRoadNormalizationError(
            "IGN road edition must be a valid ISO calendar date"
        ) from error
    if validated_edition != edition:
        raise IgnRoadNormalizationError("IGN road edition must not be rewritten")

    try:
        timestamp = datetime.fromisoformat(timestamp_raw)
    except ValueError as error:
        raise IgnRoadNormalizationError(
            "IGN road download_timestamp must be a valid ISO datetime"
        ) from error
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise IgnRoadNormalizationError(
            "IGN road download_timestamp must be timezone-aware"
        )

    if _SHA256_PATTERN.fullmatch(archive_sha256) is None:
        raise IgnRoadNormalizationError(
            "IGN road archive_sha256 must contain 64 hexadecimal characters"
        )
    try:
        _HTTP_URL_VALIDATOR.validate_python(source_url)
    except ValidationError as error:
        raise IgnRoadNormalizationError(
            "IGN road source_url must be a valid HTTP(S) URL"
        ) from error

    if context.product_version is not None:
        _required_exact_string(context.product_version, "product_version")


def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnRoadNormalizationError(f"IGN archive {label} must be a string")
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    without_accents = "".join(
        character for character in decomposed if not unicodedata.combining(character)
    )
    return " ".join(re.findall(r"[a-z0-9]+", without_accents))


def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    geometry_types = tuple(
        sorted(str(value) for value in geometry[~null_mask].geom_type.dropna().unique())
    )
    return (
        int(null_mask.sum()),
        int(empty_mask.sum()),
        int(invalid_mask.sum()),
        geometry_types,
    )


def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    all_layer_names: tuple[str, ...],
) -> None:
    try:
        _validate_layer_summary_contract(summary)
    except Exception as error:
        raise IgnRoadNormalizationError(
            "IGN road summary schema contract is invalid"
        ) from error
    if summary.logical_name != "road_segments":
        raise IgnRoadNormalizationError("IGN road summary has the wrong logical name")
    source_layer = _required_exact_string(
        summary.source_layer_name, "summary physical layer"
    )
    if source_layer not in all_layer_names:
        raise IgnRoadNormalizationError(
            "IGN road summary physical layer is absent from the extraction layer inventory"
        )
    if summary.feature_count != len(frame):
        raise IgnRoadNormalizationError(
            "IGN road summary row count does not match the source frame"
        )
    observed_columns = tuple(str(column) for column in frame.columns)
    observed_dtypes = tuple(
        (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
    )
    if summary.columns != observed_columns or summary.dtypes != observed_dtypes:
        raise IgnRoadNormalizationError(
            "IGN road summary schema columns or dtypes do not match the source frame"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnRoadNormalizationError(
            "IGN road source requires an active geometry column"
        )
    frame_crs = _validated_lambert93(frame.crs, "IGN road source")
    summary_crs = _validated_lambert93(summary.crs, "IGN road summary")
    if not frame_crs.equals(summary_crs):
        raise IgnRoadNormalizationError(
            "IGN road summary CRS does not match the source frame"
        )
    expected_geometry = (
        summary.null_geometry_count,
        summary.empty_geometry_count,
        summary.invalid_geometry_count,
        summary.geometry_types,
    )
    if _geometry_summary(frame) != expected_geometry:
        raise IgnRoadNormalizationError(
            "IGN road geometry summary does not match the source frame"
        )


def _validate_source_bundle(source: IgnBdTopoRoadData) -> _IgnRoadSourceContext:
    if type(source.extraction) is not IgnBdTopoExtraction:
        raise IgnRoadNormalizationError("IGN road extraction type is invalid")
    if type(source.extraction.archive) is not IgnBdTopoDownload:
        raise IgnRoadNormalizationError("IGN road archive type is invalid")
    if type(source.road_segments_summary) is not IgnBdTopoLayerSummary:
        raise IgnRoadNormalizationError("IGN road summary type is invalid")
    archive = source.extraction.archive
    provider = _normalized_identity(archive.provider, "provider")
    product = _normalized_identity(archive.product, "product")
    if provider not in _IGN_PROVIDER_IDENTITIES:
        raise IgnRoadNormalizationError(
            "IGN archive provider is incompatible with the IGN road normalizer"
        )
    if product.replace(" ", "") != "bdtopo":
        raise IgnRoadNormalizationError(
            "IGN archive product is incompatible with the BD TOPO road normalizer"
        )
    _validated_lambert93(archive.projection, "IGN archive projection")
    roles = (
        archive.spatial_role,
        source.extraction.spatial_role,
        source.road_segments_summary.spatial_role,
    )
    if any(role != _SPATIAL_ROLE for role in roles):
        raise IgnRoadNormalizationError(
            "IGN road source spatial roles must all be PROXY_GEOMETRY"
        )
    layer_names = source.extraction.all_layer_names
    if (
        type(layer_names) is not tuple
        or not layer_names
        or any(
            not isinstance(name, str) or not name or name != name.strip()
            for name in layer_names
        )
        or len(set(layer_names)) != len(layer_names)
    ):
        raise IgnRoadNormalizationError(
            "IGN road layer inventory must be a unique non-empty tuple"
        )
    selected_layers = (
        source.extraction.electric_lines_layer,
        source.extraction.transformation_posts_layer,
    )
    if any(layer not in layer_names for layer in selected_layers):
        raise IgnRoadNormalizationError(
            "IGN road extraction selected layer is absent from the layer inventory"
        )
    if selected_layers[0] == selected_layers[1]:
        raise IgnRoadNormalizationError(
            "IGN electricity roles must use distinct layers, not the same layer"
        )
    road_layer = source.road_segments_summary.source_layer_name
    if road_layer in selected_layers:
        raise IgnRoadNormalizationError(
            "IGN road and electricity roles must use distinct layers, not the same layer"
        )
    if not isinstance(source.road_segments, gpd.GeoDataFrame):
        raise IgnRoadNormalizationError(
            "IGN road_segments must be a GeoDataFrame with an active geometry column"
        )
    _validate_source_frame(source.road_segments)
    _validate_layer_summary(
        source.road_segments,
        source.road_segments_summary,
        source.extraction.all_layer_names,
    )
    return _IgnRoadSourceContext(
        source_layer=source.road_segments_summary.source_layer_name,
        department_code=archive.department_code,
        edition=archive.edition,
        product_version=archive.product_version,
        download_timestamp=archive.download_timestamp,
        archive_sha256=archive.sha256,
        source_url=archive.source_url,
    )


def _validate_identifiers(frame: gpd.GeoDataFrame) -> None:
    identifiers = frame["cleabs"]
    if identifiers.isna().any():
        raise IgnRoadNormalizationError("IGN road cleabs values must not be null")
    values = identifiers.tolist()
    if any(not isinstance(identifier, str) for identifier in values):
        raise IgnRoadNormalizationError("IGN road cleabs values must be strings")
    if any(not identifier.strip() for identifier in values):
        raise IgnRoadNormalizationError("IGN road cleabs values must not be empty")
    if any(identifier != identifier.strip() for identifier in values):
        raise IgnRoadNormalizationError(
            "IGN road cleabs values must not contain edge whitespace"
        )
    if any(":" in identifier for identifier in values):
        raise IgnRoadNormalizationError("IGN road cleabs values must not contain ':'")
    if any(
        unicodedata.category(character) == "Cc"
        for identifier in values
        for character in identifier
    ):
        raise IgnRoadNormalizationError(
            "IGN road cleabs values must not contain control characters"
        )
    if identifiers.duplicated().any():
        raise IgnRoadNormalizationError("IGN road cleabs values must be unique")


def _validate_source_frame(frame: gpd.GeoDataFrame) -> None:
    if frame.columns.duplicated().any():
        raise IgnRoadNormalizationError(
            "IGN road source columns must not contain duplicates"
        )
    missing = _REQUIRED_SOURCE_FIELDS - set(frame.columns)
    if missing:
        formatted = ", ".join(sorted(missing))
        raise IgnRoadNormalizationError(
            f"Missing required IGN road source columns: {formatted}"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnRoadNormalizationError(
            "IGN road source requires an active geometry column"
        )
    _validated_lambert93(frame.crs, "IGN road source")
    _validate_identifiers(frame)


def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
    status = pd.Series("VALID", index=geometry.index, dtype="object")
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    status.loc[null_mask] = "NULL"
    status.loc[empty_mask] = "EMPTY"
    status.loc[invalid_mask] = "INVALID"
    return status


def _normalize_road_frame(
    frame: gpd.GeoDataFrame,
    context: _IgnRoadSourceContext,
) -> gpd.GeoDataFrame:
    _validate_source_context(context)
    _validate_source_frame(frame)
    working = frame.reset_index(drop=True).copy()
    status = _geometry_status(working.geometry)
    valid_types = working.loc[status == "VALID", "geometry"].geom_type
    unsupported = sorted(set(valid_types.dropna()) - _ROAD_GEOMETRY_TYPES)
    if unsupported:
        raise IgnRoadNormalizationError(
            "IGN road source has unsupported VALID geometry types: "
            + ", ".join(unsupported)
        )

    source_ids = working["cleabs"].copy()
    output = pd.DataFrame(index=working.index.copy())
    output["road_feature_id"] = source_ids.map(
        lambda identifier: f"IGN_BDTOPO:{_ROAD_FEATURE_TYPE}:{identifier}"
    )
    output["road_feature_type"] = _ROAD_FEATURE_TYPE
    output["source_provider"] = _SOURCE_PROVIDER
    output["source_product"] = _SOURCE_PRODUCT
    output["source_layer"] = context.source_layer
    output["source_feature_id"] = source_ids
    output["source_department_code"] = context.department_code
    output["source_edition"] = context.edition
    output["source_product_version"] = context.product_version
    output["source_download_timestamp"] = context.download_timestamp
    output["source_archive_sha256"] = context.archive_sha256
    output["source_url"] = context.source_url
    for source_column, output_column in _RAW_FIELD_MAPPING:
        output[output_column] = working[source_column].copy()
    output["spatial_role"] = _SPATIAL_ROLE
    output["geometry_status"] = status
    output["geometry"] = working.geometry.copy()

    normalized = gpd.GeoDataFrame(
        output.loc[:, list(_OUTPUT_COLUMNS)],
        geometry="geometry",
        crs=working.crs,
    )
    if len(normalized) != len(frame):
        raise IgnRoadNormalizationError("IGN road normalization changed the row count")
    if not isinstance(normalized.index, pd.RangeIndex):
        raise IgnRoadNormalizationError(
            "IGN normalized road output must use a RangeIndex"
        )
    if (
        normalized["road_feature_id"].isna().any()
        or normalized["road_feature_id"].duplicated().any()
    ):
        raise IgnRoadNormalizationError(
            "Normalized IGN road_feature_id values must be non-null and unique"
        )
    return normalized


def _normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
    fresh = _revalidate_ign_bdtopo_road_data(source, config)
    context = _validate_source_bundle(fresh)
    return NormalizedIgnRoadData(
        road_segments=_normalize_road_frame(fresh.road_segments, context)
    )


def normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
    """Validate and project one already-loaded IGN road source without interpretation."""

    try:
        if type(source) is not IgnBdTopoRoadData:
            raise TypeError("source must be an IgnBdTopoRoadData")
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("config must be an IgnBdTopoSourceConfig")
        return _normalize_ign_roads(source, config)
    except IgnRoadNormalizationError:
        raise
    except Exception as error:
        raise IgnRoadNormalizationError(
            f"IGN road source cannot be normalized safely: {error}"
        ) from error
