"""Normalize IGN BD TOPO electricity layers into stable LandScout proxies."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS

from landscout.sources.ign_bdtopo_fr import IgnBdTopoElectricityData

SOURCE_PROVIDER = "IGN"
SOURCE_PRODUCT = "BD_TOPO"
SPATIAL_ROLE = "PROXY_GEOMETRY"
ELECTRIC_LINE_SOURCE_LAYER = "ligne_electrique"
TRANSFORMATION_POST_SOURCE_LAYER = "poste_de_transformation"

VoltageStatus = Literal["EXACT", "BELOW", "UNKNOWN", "DEENERGIZED", "UNPARSED"]
GeometryStatus = Literal["VALID", "NULL", "EMPTY", "INVALID"]

LINE_OUTPUT_COLUMNS = (
    "grid_feature_id",
    "grid_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
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


class IgnGridNormalizationError(ValueError):
    """Raised when IGN electricity data cannot be normalized safely."""


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
    return value if value > 0 else None


def parse_ign_voltage(value: object) -> IgnVoltageNormalization:
    """Parse IGN voltage vocabulary without inventing numeric precision."""

    if value is None or pd.isna(value):
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
    if frame.crs is None:
        raise IgnGridNormalizationError(f"IGN {source_layer} CRS is required")
    try:
        source_crs = CRS.from_user_input(frame.crs)
    except Exception as error:
        raise IgnGridNormalizationError(
            f"IGN {source_layer} CRS is unreadable"
        ) from error
    expected_crs = CRS.from_epsg(2154)
    if not source_crs.is_projected or not source_crs.equals(expected_crs):
        raise IgnGridNormalizationError(
            f"IGN {source_layer} must use EPSG:2154"
        )

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


def _base_output(
    frame: gpd.GeoDataFrame,
    *,
    feature_type: str,
    source_layer: str,
) -> pd.DataFrame:
    source_ids = frame["cleabs"].copy()
    output = pd.DataFrame(index=frame.index.copy())
    output["grid_feature_id"] = source_ids.map(
        lambda identifier: f"IGN_BDTOPO:{feature_type}:{identifier}"
    )
    output["grid_feature_type"] = feature_type
    output["source_provider"] = SOURCE_PROVIDER
    output["source_product"] = SOURCE_PRODUCT
    output["source_layer"] = source_layer
    output["source_feature_id"] = source_ids
    return output


def _validated_geodataframe(
    output: pd.DataFrame,
    frame: gpd.GeoDataFrame,
    columns: tuple[str, ...],
) -> gpd.GeoDataFrame:
    output["spatial_role"] = SPATIAL_ROLE
    output["geometry_status"] = _geometry_status(frame.geometry)
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
    return normalized


def normalize_ign_electric_lines(
    lines: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    """Normalize the IGN electric-line source layer without changing geometry."""

    _validate_input(lines, LINE_SOURCE_FIELDS, ELECTRIC_LINE_SOURCE_LAYER)
    output = _base_output(
        lines,
        feature_type="ELECTRIC_LINE",
        source_layer=ELECTRIC_LINE_SOURCE_LAYER,
    )
    parsed = [parse_ign_voltage(value) for value in lines["voltage"].tolist()]
    output["voltage_raw"] = [result.raw for result in parsed]
    output["voltage_status"] = [result.status for result in parsed]
    output["voltage_kv"] = [result.voltage_kv for result in parsed]
    output["voltage_upper_bound_kv"] = [
        result.voltage_upper_bound_kv for result in parsed
    ]
    output["manager_name"] = lines["gestionnaire"].copy()
    output["manager_siren"] = lines["siren_gestionnaire"].copy()
    output["asset_status_raw"] = lines["etat_de_l_objet"].copy()
    output["source_name_raw"] = lines["sources"].copy()
    output["source_identifiers_raw"] = lines["identifiants_sources"].copy()
    output["source_created_at"] = lines["date_creation"].copy()
    output["source_modified_at"] = lines["date_modification"].copy()
    output["source_confirmed_at"] = lines["date_de_confirmation"].copy()
    output["planimetric_acquisition_method"] = lines[
        "methode_d_acquisition_planimetrique"
    ].copy()
    output["planimetric_precision_m"] = lines["precision_planimetrique"].copy()
    return _validated_geodataframe(output, lines, LINE_OUTPUT_COLUMNS)


def normalize_ign_transformation_posts(
    posts: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    """Normalize IGN transformation-post proxies without inferring voltage."""

    _validate_input(
        posts,
        TRANSFORMATION_POST_SOURCE_FIELDS,
        TRANSFORMATION_POST_SOURCE_LAYER,
    )
    output = _base_output(
        posts,
        feature_type="TRANSFORMATION_POST",
        source_layer=TRANSFORMATION_POST_SOURCE_LAYER,
    )
    output["name"] = posts["toponyme"].copy()
    output["name_status_raw"] = posts["statut_du_toponyme"].copy()
    output["importance_raw"] = posts["importance"].copy()
    output["asset_status_raw"] = posts["etat_de_l_objet"].copy()
    output["source_name_raw"] = posts["sources"].copy()
    output["source_identifiers_raw"] = posts["identifiants_sources"].copy()
    output["source_created_at"] = posts["date_creation"].copy()
    output["source_modified_at"] = posts["date_modification"].copy()
    output["source_confirmed_at"] = posts["date_de_confirmation"].copy()
    output["planimetric_acquisition_method"] = posts[
        "methode_d_acquisition_planimetrique"
    ].copy()
    output["planimetric_precision_m"] = posts["precision_planimetrique"].copy()
    output["voltage_status"] = "UNKNOWN"
    output["voltage_kv"] = float("nan")
    return _validated_geodataframe(
        output,
        posts,
        TRANSFORMATION_POST_OUTPUT_COLUMNS,
    )


def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
) -> NormalizedIgnElectricityData:
    """Normalize both already-loaded IGN electricity layers independently."""

    return NormalizedIgnElectricityData(
        electric_lines=normalize_ign_electric_lines(source.electric_lines),
        transformation_posts=normalize_ign_transformation_posts(
            source.transformation_posts
        ),
    )
