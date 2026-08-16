"""Normalize IGN BD TOPO electricity layers into stable LandScout proxies."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime
from math import isfinite
from numbers import Real
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pandas.api.types import is_scalar  # type: ignore[import-untyped]
from pydantic import HttpUrl, TypeAdapter, ValidationError
from pyproj import CRS

from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)

SOURCE_PROVIDER = "IGN"
SOURCE_PRODUCT = "BD_TOPO"
SPATIAL_ROLE = "PROXY_GEOMETRY"

VoltageStatus = Literal["EXACT", "BELOW", "UNKNOWN", "DEENERGIZED", "UNPARSED"]
GeometryStatus = Literal["VALID", "NULL", "EMPTY", "INVALID"]

PACKAGE_LINEAGE_COLUMNS = (
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
)

LINE_OUTPUT_COLUMNS = (
    "grid_feature_id",
    "grid_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    *PACKAGE_LINEAGE_COLUMNS,
    "voltage_raw",
    "voltage_status",
    "voltage_kv",
    "voltage_upper_bound_kv",
    "manager_name",
    "manager_siren",
    "asset_status_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_m",
    "spatial_role",
    "geometry_status",
    "geometry",
)

TRANSFORMATION_POST_OUTPUT_COLUMNS = (
    "grid_feature_id",
    "grid_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    *PACKAGE_LINEAGE_COLUMNS,
    "name",
    "name_status_raw",
    "importance_raw",
    "asset_status_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_m",
    "voltage_status",
    "voltage_kv",
    "spatial_role",
    "geometry_status",
    "geometry",
)

LINE_SOURCE_FIELDS = frozenset(
    {
        "cleabs",
        "voltage",
        "gestionnaire",
        "siren_gestionnaire",
        "etat_de_l_objet",
        "sources",
        "identifiants_sources",
        "date_creation",
        "date_modification",
        "date_de_confirmation",
        "methode_d_acquisition_planimetrique",
        "precision_planimetrique",
        "geometry",
    }
)

TRANSFORMATION_POST_SOURCE_FIELDS = frozenset(
    {
        "cleabs",
        "toponyme",
        "statut_du_toponyme",
        "importance",
        "etat_de_l_objet",
        "sources",
        "identifiants_sources",
        "date_creation",
        "date_modification",
        "date_de_confirmation",
        "methode_d_acquisition_planimetrique",
        "precision_planimetrique",
        "geometry",
    }
)

LINE_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
TRANSFORMATION_POST_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})

_EXACT_VOLTAGE_PATTERN = re.compile(
    r"^(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE
)
_BELOW_VOLTAGE_PATTERN = re.compile(
    r"^<\s*(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE
)
_UNKNOWN_VOLTAGE_TERMS = frozenset(
    {"inconnu", "inconnue", "unknown", "non renseigne", "non renseignee"}
)
_DEENERGIZED_VOLTAGE_TERMS = frozenset({"hors tension"})
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


class IgnGridNormalizationError(ValueError):
    """Raised when IGN electricity data cannot be normalized safely."""


@dataclass(frozen=True)
class _IgnGridSourceContext:
    """Immutable source-package context persisted on every normalized row."""

    source_layer: str
    department_code: str
    edition: str
    product_version: str | None
    download_timestamp: str
    archive_sha256: str
    source_url: str


@dataclass(frozen=True)
class IgnVoltageNormalization:
    """One source voltage value and its explicit normalized semantics."""

    raw: str | None
    status: VoltageStatus
    voltage_kv: float | None
    voltage_upper_bound_kv: float | None


@dataclass(frozen=True)
class NormalizedIgnElectricityData:
    electric_lines: gpd.GeoDataFrame
    transformation_posts: gpd.GeoDataFrame


def _normalized_term(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.strip().casefold())
    without_accents = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    return " ".join(without_accents.split())


def _positive_voltage(match: re.Match[str]) -> float | None:
    value = float(match.group("value").replace(",", "."))
    return value if value > 0 and isfinite(value) else None


def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    if not is_scalar(value):
        return False
    return bool(pd.isna(value))


def parse_ign_voltage(value: object) -> IgnVoltageNormalization:
    """Parse scalar IGN voltage vocabulary without inventing precision.

    Unsupported list-like or array-like inputs are preserved as text and
    classified ``UNPARSED`` rather than reaching Pandas' ambiguous truth-value
    handling.
    """

    if not is_scalar(value):
        return IgnVoltageNormalization(str(value), "UNPARSED", None, None)
    if _is_missing_scalar(value):
        return IgnVoltageNormalization(None, "UNKNOWN", None, None)

    raw = value if isinstance(value, str) else str(value)
    normalized = _normalized_term(raw)
    if normalized in _UNKNOWN_VOLTAGE_TERMS:
        return IgnVoltageNormalization(raw, "UNKNOWN", None, None)
    if normalized in _DEENERGIZED_VOLTAGE_TERMS:
        return IgnVoltageNormalization(raw, "DEENERGIZED", None, None)

    below_match = _BELOW_VOLTAGE_PATTERN.fullmatch(normalized)
    if below_match is not None:
        upper_bound = _positive_voltage(below_match)
        if upper_bound is not None:
            return IgnVoltageNormalization(raw, "BELOW", None, upper_bound)

    exact_match = _EXACT_VOLTAGE_PATTERN.fullmatch(normalized)
    if exact_match is not None:
        exact = _positive_voltage(exact_match)
        if exact is not None:
            return IgnVoltageNormalization(raw, "EXACT", exact, None)

    return IgnVoltageNormalization(raw, "UNPARSED", None, None)


def _validated_lambert93(crs_value: object, label: str) -> CRS:
    if crs_value is None:
        raise IgnGridNormalizationError(f"{label} CRS is required")
    try:
        source_crs = CRS.from_user_input(crs_value)
    except Exception as error:
        raise IgnGridNormalizationError(f"{label} CRS is unreadable") from error
    expected_crs = CRS.from_epsg(2154)
    if not source_crs.is_projected or not source_crs.equals(expected_crs):
        raise IgnGridNormalizationError(f"{label} must use EPSG:2154")
    return source_crs


def _required_exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnGridNormalizationError(f"IGN source context {label} must be a string")
    if value != value.strip():
        raise IgnGridNormalizationError(
            f"IGN source context {label} must not contain edge whitespace"
        )
    return value


def _validate_source_context(context: _IgnGridSourceContext) -> None:
    _required_exact_string(context.source_layer, "source_layer")
    department_code = _required_exact_string(
        context.department_code, "department_code"
    )
    edition = _required_exact_string(context.edition, "edition")
    download_timestamp = _required_exact_string(
        context.download_timestamp, "download_timestamp"
    )
    archive_sha256 = _required_exact_string(
        context.archive_sha256, "archive_sha256"
    )
    source_url = _required_exact_string(context.source_url, "source_url")

    try:
        validated_department = _DEPARTMENT_CODE_VALIDATOR.validate_python(
            department_code
        )
    except ValidationError as error:
        raise IgnGridNormalizationError(
            "IGN source context department_code is invalid"
        ) from error
    if validated_department != department_code:
        raise IgnGridNormalizationError(
            "IGN source context department_code must not be rewritten"
        )

    try:
        validated_edition = _EDITION_VALIDATOR.validate_python(edition)
        date.fromisoformat(validated_edition)
    except (ValidationError, ValueError) as error:
        raise IgnGridNormalizationError(
            "IGN source context edition must be a valid ISO calendar date"
        ) from error
    if validated_edition != edition:
        raise IgnGridNormalizationError(
            "IGN source context edition must not be rewritten"
        )

    try:
        timestamp = datetime.fromisoformat(download_timestamp)
    except ValueError as error:
        raise IgnGridNormalizationError(
            "IGN source context download_timestamp must be a valid ISO datetime"
        ) from error
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise IgnGridNormalizationError(
            "IGN source context download_timestamp must be timezone-aware"
        )

    if _SHA256_PATTERN.fullmatch(archive_sha256) is None:
        raise IgnGridNormalizationError(
            "IGN source context archive_sha256 must contain 64 hexadecimal characters"
        )

    try:
        _HTTP_URL_VALIDATOR.validate_python(source_url)
    except ValidationError as error:
        raise IgnGridNormalizationError(
            "IGN source context source_url must be a valid HTTP(S) URL"
        ) from error

    if context.product_version is not None:
        _required_exact_string(context.product_version, "product_version")


def _validate_input(
    frame: gpd.GeoDataFrame,
    required_columns: frozenset[str],
    source_layer: str,
) -> None:
    missing = required_columns - set(frame.columns)
    if missing:
        formatted = ", ".join(sorted(missing))
        raise IgnGridNormalizationError(
            f"Missing required IGN {source_layer} columns: {formatted}"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnGridNormalizationError(
            f"IGN {source_layer} requires an active geometry column"
        )
    _validated_lambert93(frame.crs, f"IGN {source_layer}")

    identifiers = frame["cleabs"]
    if identifiers.isna().any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not be null"
        )
    if any(not isinstance(identifier, str) for identifier in identifiers.tolist()):
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must be strings"
        )
    if identifiers.str.strip().eq("").any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not be empty"
        )
    if identifiers.map(lambda value: value != value.strip()).any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not contain edge whitespace"
        )
    if identifiers.str.contains(":", regex=False).any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not contain ':'"
        )
    if identifiers.map(
        lambda value: any(unicodedata.category(character) == "Cc" for character in value)
    ).any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not contain control characters"
        )
    if identifiers.duplicated().any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must be unique"
        )


def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
    status = pd.Series("VALID", index=geometry.index, dtype="object")
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    status.loc[null_mask] = "NULL"
    status.loc[empty_mask] = "EMPTY"
    status.loc[invalid_mask] = "INVALID"
    return status


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


def _validate_valid_geometry_types(
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    allowed_types: frozenset[str],
    source_layer: str,
) -> None:
    valid_types = frame.loc[status == "VALID", "geometry"].geom_type
    unsupported = sorted(set(valid_types.dropna()) - allowed_types)
    if unsupported:
        raise IgnGridNormalizationError(
            f"IGN {source_layer} has unsupported VALID geometry types: "
            + ", ".join(unsupported)
        )


def _normalized_precision(
    source: pd.Series,
    source_layer: str,
) -> pd.Series:
    normalized: list[float] = []
    for value in source.tolist():
        if _is_missing_scalar(value):
            normalized.append(float("nan"))
            continue
        if isinstance(value, bool) or not isinstance(value, Real):
            raise IgnGridNormalizationError(
                f"IGN {source_layer} precision_planimetrique must be numeric or null"
            )
        numeric = float(value)
        if not isfinite(numeric) or numeric < 0:
            raise IgnGridNormalizationError(
                f"IGN {source_layer} precision_planimetrique must be finite and >= 0"
            )
        normalized.append(numeric)
    return pd.Series(normalized, index=source.index, dtype="float64")


def _base_output(
    frame: gpd.GeoDataFrame,
    *,
    feature_type: str,
    context: _IgnGridSourceContext,
) -> pd.DataFrame:
    source_ids = frame["cleabs"].copy()
    output = pd.DataFrame(index=frame.index.copy())
    output["grid_feature_id"] = source_ids.map(
        lambda identifier: f"IGN_BDTOPO:{feature_type}:{identifier}"
    )
    output["grid_feature_type"] = feature_type
    output["source_provider"] = SOURCE_PROVIDER
    output["source_product"] = SOURCE_PRODUCT
    output["source_layer"] = context.source_layer
    output["source_feature_id"] = source_ids
    output["source_department_code"] = context.department_code
    output["source_edition"] = context.edition
    output["source_product_version"] = context.product_version
    output["source_download_timestamp"] = context.download_timestamp
    output["source_archive_sha256"] = context.archive_sha256
    output["source_url"] = context.source_url
    return output


def _validated_geodataframe(
    output: pd.DataFrame,
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    columns: tuple[str, ...],
) -> gpd.GeoDataFrame:
    output["spatial_role"] = SPATIAL_ROLE
    output["geometry_status"] = status
    output["geometry"] = frame.geometry.copy()
    normalized = gpd.GeoDataFrame(
        output.loc[:, list(columns)], geometry="geometry", crs=frame.crs
    )
    normalized_ids = normalized["grid_feature_id"]
    if normalized_ids.isna().any() or normalized_ids.duplicated().any():
        raise IgnGridNormalizationError(
            "Normalized IGN grid_feature_id values must be non-null and unique"
        )
    if len(normalized) != len(frame):
        raise IgnGridNormalizationError("IGN normalization changed the row count")
    if not isinstance(normalized.index, pd.RangeIndex):
        raise IgnGridNormalizationError("IGN normalized output must use a RangeIndex")
    return normalized


def _normalize_ign_electric_lines(
    lines: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
    """Normalize one discovered IGN electric-line layer."""

    _validate_source_context(context)
    _validate_input(lines, LINE_SOURCE_FIELDS, context.source_layer)
    working = lines.reset_index(drop=True).copy()
    status = _geometry_status(working.geometry)
    _validate_valid_geometry_types(
        working, status, LINE_GEOMETRY_TYPES, context.source_layer
    )
    precision = _normalized_precision(
        working["precision_planimetrique"], context.source_layer
    )
    output = _base_output(
        working,
        feature_type="ELECTRIC_LINE",
        context=context,
    )
    parsed = [parse_ign_voltage(value) for value in working["voltage"].tolist()]
    output["voltage_raw"] = [result.raw for result in parsed]
    output["voltage_status"] = [result.status for result in parsed]
    output["voltage_kv"] = [result.voltage_kv for result in parsed]
    output["voltage_upper_bound_kv"] = [
        result.voltage_upper_bound_kv for result in parsed
    ]
    output["manager_name"] = working["gestionnaire"].copy()
    output["manager_siren"] = working["siren_gestionnaire"].copy()
    output["asset_status_raw"] = working["etat_de_l_objet"].copy()
    output["source_name_raw"] = working["sources"].copy()
    output["source_identifiers_raw"] = working["identifiants_sources"].copy()
    output["source_created_at"] = working["date_creation"].copy()
    output["source_modified_at"] = working["date_modification"].copy()
    output["source_confirmed_at"] = working["date_de_confirmation"].copy()
    output["planimetric_acquisition_method"] = working[
        "methode_d_acquisition_planimetrique"
    ].copy()
    output["planimetric_precision_m"] = precision
    return _validated_geodataframe(
        output, working, status, LINE_OUTPUT_COLUMNS
    )


def _normalize_ign_transformation_posts(
    posts: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
    """Normalize one discovered IGN transformation-post proxy layer."""

    _validate_source_context(context)
    _validate_input(posts, TRANSFORMATION_POST_SOURCE_FIELDS, context.source_layer)
    working = posts.reset_index(drop=True).copy()
    status = _geometry_status(working.geometry)
    _validate_valid_geometry_types(
        working,
        status,
        TRANSFORMATION_POST_GEOMETRY_TYPES,
        context.source_layer,
    )
    precision = _normalized_precision(
        working["precision_planimetrique"], context.source_layer
    )
    output = _base_output(
        working,
        feature_type="TRANSFORMATION_POST",
        context=context,
    )
    output["name"] = working["toponyme"].copy()
    output["name_status_raw"] = working["statut_du_toponyme"].copy()
    output["importance_raw"] = working["importance"].copy()
    output["asset_status_raw"] = working["etat_de_l_objet"].copy()
    output["source_name_raw"] = working["sources"].copy()
    output["source_identifiers_raw"] = working["identifiants_sources"].copy()
    output["source_created_at"] = working["date_creation"].copy()
    output["source_modified_at"] = working["date_modification"].copy()
    output["source_confirmed_at"] = working["date_de_confirmation"].copy()
    output["planimetric_acquisition_method"] = working[
        "methode_d_acquisition_planimetrique"
    ].copy()
    output["planimetric_precision_m"] = precision
    output["voltage_status"] = "UNKNOWN"
    output["voltage_kv"] = float("nan")
    return _validated_geodataframe(
        output,
        working,
        status,
        TRANSFORMATION_POST_OUTPUT_COLUMNS,
    )


def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    *,
    expected_layer: str,
    expected_logical_name: str,
) -> None:
    try:
        _validate_layer_summary_contract(summary)
    except Exception as error:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary schema contract is invalid"
        ) from error
    if summary.source_layer_name != expected_layer:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary layer does not match extraction"
        )
    if summary.logical_name != expected_logical_name:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary has the wrong logical name"
        )
    if summary.feature_count != len(frame):
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary row count does not match frame"
        )
    observed_columns = tuple(str(column) for column in frame.columns)
    observed_dtypes = tuple(
        (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
    )
    if summary.columns != observed_columns or summary.dtypes != observed_dtypes:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary schema columns or dtypes "
            "do not match frame"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} requires an active geometry column"
        )
    frame_crs = _validated_lambert93(frame.crs, f"IGN {expected_logical_name}")
    summary_crs = _validated_lambert93(
        summary.crs, f"IGN {expected_logical_name} summary"
    )
    if not frame_crs.equals(summary_crs):
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary CRS does not match frame"
        )
    observed_geometry = _geometry_summary(frame)
    expected_geometry = (
        summary.null_geometry_count,
        summary.empty_geometry_count,
        summary.invalid_geometry_count,
        summary.geometry_types,
    )
    if observed_geometry != expected_geometry:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} geometry summary does not match frame"
        )


def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnGridNormalizationError(f"IGN archive {label} must be a string")
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    without_accents = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    return " ".join(re.findall(r"[a-z0-9]+", without_accents))


def _validate_archive_identity(source: IgnBdTopoElectricityData) -> None:
    archive = source.extraction.archive
    provider = _normalized_identity(archive.provider, "provider")
    product = _normalized_identity(archive.product, "product")
    if provider not in _IGN_PROVIDER_IDENTITIES:
        raise IgnGridNormalizationError(
            "IGN archive provider is incompatible with the IGN normalizer"
        )
    if product.replace(" ", "") != "bdtopo":
        raise IgnGridNormalizationError(
            "IGN archive product is incompatible with the BD TOPO normalizer"
        )
    _validated_lambert93(archive.projection, "IGN archive projection")


def _validate_source_bundle(source: IgnBdTopoElectricityData) -> None:
    if type(source) is not IgnBdTopoElectricityData:
        raise IgnGridNormalizationError(
            "IGN electricity source must be IgnBdTopoElectricityData"
        )
    if type(source.extraction) is not IgnBdTopoExtraction:
        raise IgnGridNormalizationError("IGN electricity extraction type is invalid")
    if type(source.extraction.archive) is not IgnBdTopoDownload:
        raise IgnGridNormalizationError("IGN electricity archive type is invalid")
    if type(source.electric_lines_summary) is not IgnBdTopoLayerSummary or type(
        source.transformation_posts_summary
    ) is not IgnBdTopoLayerSummary:
        raise IgnGridNormalizationError("IGN electricity summary type is invalid")
    if not isinstance(source.electric_lines, gpd.GeoDataFrame) or not isinstance(
        source.transformation_posts, gpd.GeoDataFrame
    ):
        raise IgnGridNormalizationError(
            "IGN electricity layers must be GeoDataFrames"
        )
    extraction = source.extraction
    layer_names = extraction.all_layer_names
    if (
        type(layer_names) is not tuple
        or not layer_names
        or any(
            not isinstance(name, str) or not name or name != name.strip()
            for name in layer_names
        )
        or len(set(layer_names)) != len(layer_names)
    ):
        raise IgnGridNormalizationError(
            "IGN electricity layer inventory must be a unique non-empty tuple"
        )
    selected_layers = (
        extraction.electric_lines_layer,
        extraction.transformation_posts_layer,
    )
    if any(layer not in layer_names for layer in selected_layers):
        raise IgnGridNormalizationError(
            "IGN electricity selected layer is absent from the layer inventory"
        )
    if selected_layers[0] == selected_layers[1]:
        raise IgnGridNormalizationError(
            "IGN electricity roles must use distinct layers, not the same layer"
        )
    _validate_archive_identity(source)
    roles = (
        source.spatial_role,
        source.extraction.spatial_role,
        source.extraction.archive.spatial_role,
        source.electric_lines_summary.spatial_role,
        source.transformation_posts_summary.spatial_role,
    )
    if any(role != SPATIAL_ROLE for role in roles):
        raise IgnGridNormalizationError(
            "IGN source bundle spatial roles must all be PROXY_GEOMETRY"
        )
    _validate_layer_summary(
        source.electric_lines,
        source.electric_lines_summary,
        expected_layer=source.extraction.electric_lines_layer,
        expected_logical_name="electric_lines",
    )
    _validate_layer_summary(
        source.transformation_posts,
        source.transformation_posts_summary,
        expected_layer=source.extraction.transformation_posts_layer,
        expected_logical_name="transformation_posts",
    )


def _source_context(
    source: IgnBdTopoElectricityData,
    source_layer: str,
) -> _IgnGridSourceContext:
    archive = source.extraction.archive
    return _IgnGridSourceContext(
        source_layer=source_layer,
        department_code=archive.department_code,
        edition=archive.edition,
        product_version=archive.product_version,
        download_timestamp=archive.download_timestamp,
        archive_sha256=archive.sha256,
        source_url=archive.source_url,
    )


def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnElectricityData:
    """Validate and normalize a complete already-loaded IGN source bundle."""

    try:
        if type(config) is not IgnBdTopoSourceConfig:
            raise IgnGridNormalizationError(
                "IGN electricity source config type is invalid"
            )
        _validate_source_bundle(source)
        _revalidate_ign_bdtopo_electricity_data(source, config)
        line_context = _source_context(
            source, source.extraction.electric_lines_layer
        )
        post_context = _source_context(
            source, source.extraction.transformation_posts_layer
        )
        return NormalizedIgnElectricityData(
            electric_lines=_normalize_ign_electric_lines(
                source.electric_lines, line_context
            ),
            transformation_posts=_normalize_ign_transformation_posts(
                source.transformation_posts, post_context
            ),
        )
    except IgnGridNormalizationError:
        raise
    except Exception as error:
        raise IgnGridNormalizationError(
            "IGN electricity source cannot be normalized safely"
        ) from error
