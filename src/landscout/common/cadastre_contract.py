"""Internal contracts shared by normalized cadastral stages."""

import re
from collections.abc import Iterable
from math import isfinite
from numbers import Real

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS

from landscout.geo.crs import LAMBERT93, WGS84

CADASTRE_GEOMETRY_STATUSES = frozenset({"VALID", "INVALID"})
CADASTRE_NORMALIZED_PREFIX = (
    "parcel_id",
    "commune_code",
    "section_prefix",
    "section",
    "parcel_number",
    "source_contenance",
    "source_arpente",
    "source_created_at",
    "source_updated_at",
    "geometry_status",
    "area_m2",
    "geometry",
)
CADASTRE_AREA_ABSOLUTE_TOLERANCE_M2 = 1e-6
CADASTRE_AREA_RELATIVE_TOLERANCE = 1e-12
_CANONICAL_COMMUNE = re.compile(r"^(?:\d{5}|2[AB]\d{3})$")


def validate_cadastre_geometry_statuses(values: Iterable[object]) -> None:
    """Require the exact geometry-status vocabulary emitted by normalization."""

    if any(
        type(value) is not str or value not in CADASTRE_GEOMETRY_STATUSES
        for value in values
    ):
        raise ValueError(
            "geometry_status must contain only exact VALID or INVALID strings"
        )


def _require_exact_strings(values: Iterable[object], label: str) -> None:
    items = tuple(values)
    if any(bool(pd.isna(value)) for value in items):
        raise ValueError(f"{label} values must not be null")
    if any(
        type(value) is not str or not value or value != value.strip() for value in items
    ):
        raise ValueError(f"{label} values must be exact non-empty strings")


def validate_normalized_cadastre_parcels(
    parcels: object,
) -> gpd.GeoDataFrame:
    """Validate the canonical normalized Cadastre prefix and cross-field facts."""

    if not isinstance(parcels, gpd.GeoDataFrame):
        raise ValueError(  # noqa: TRY004 - one stable validation-error contract
            "Normalized Cadastre parcels must be a GeoDataFrame"
        )
    if parcels.columns.duplicated().any():
        raise ValueError("Normalized Cadastre parcel columns must be unique")
    if tuple(str(column) for column in parcels.columns[:12]) != (
        CADASTRE_NORMALIZED_PREFIX
    ):
        raise ValueError(
            "Normalized Cadastre parcels must retain the exact canonical column prefix "
            "including parcel_id"
        )
    if parcels.active_geometry_name != "geometry":
        raise ValueError("Normalized Cadastre parcels require active geometry")
    if parcels.crs is None:
        raise ValueError("Normalized Cadastre parcel CRS is required")
    try:
        crs = CRS.from_user_input(parcels.crs)
    except Exception as error:
        raise ValueError("Normalized Cadastre parcel CRS is unreadable") from error
    if not crs.equals(CRS.from_user_input(WGS84)):
        raise ValueError("Normalized Cadastre parcels must use EPSG:4326")

    _require_exact_strings(parcels["parcel_id"].tolist(), "parcel_id")
    if parcels["parcel_id"].duplicated().any():
        raise ValueError("parcel_id values must be unique")
    _require_exact_strings(parcels["commune_code"].tolist(), "commune_code")
    if any(
        _CANONICAL_COMMUNE.fullmatch(value) is None
        for value in parcels["commune_code"].tolist()
    ):
        raise ValueError("commune_code values must be canonical French INSEE strings")
    for column in ("section_prefix", "section", "parcel_number"):
        _require_exact_strings(parcels[column].tolist(), column)
    expected_ids = (
        parcels["commune_code"]
        + parcels["section_prefix"]
        + parcels["section"].str.zfill(2)
        + parcels["parcel_number"].str.zfill(4)
    )
    if not parcels["parcel_id"].equals(expected_ids):
        raise ValueError(
            "parcel_id must equal commune, prefix, section, and parcel number identity"
        )

    validate_cadastre_geometry_statuses(parcels["geometry_status"].tolist())
    geometry = parcels.geometry
    non_null = ~geometry.isna()
    if any(bool(value) for value in geometry.loc[non_null].has_z):
        raise ValueError("Normalized Cadastre parcel geometry must be exactly 2D")
    unsupported = set(geometry.loc[non_null].geom_type.dropna()) - {
        "Polygon",
        "MultiPolygon",
    }
    if unsupported:
        raise ValueError("Normalized Cadastre geometry must be Polygon or MultiPolygon")
    factually_valid = non_null & ~geometry.is_empty & geometry.is_valid
    recorded_valid = parcels["geometry_status"] == "VALID"
    if not recorded_valid.equals(factually_valid):
        raise ValueError("geometry_status differs from the actual parcel geometry")

    valid_areas = parcels.loc[recorded_valid, "area_m2"]
    if any(
        isinstance(value, bool)
        or not isinstance(value, Real)
        or not isfinite(float(value))
        for value in valid_areas
    ):
        raise ValueError(
            "area_m2 must be numeric and finite and must be a strict positive "
            "finite numeric value when geometry_status is VALID"
        )
    if any(float(value) <= 0 for value in valid_areas):
        raise ValueError(
            "area_m2 must be greater than zero and must be a strict positive "
            "finite numeric value when geometry_status is VALID"
        )
    invalid_areas = parcels.loc[~recorded_valid, "area_m2"]
    if invalid_areas.notna().any():
        raise ValueError("INVALID parcel area_m2 must be null")

    if recorded_valid.any():
        measured = parcels.loc[recorded_valid].to_crs(LAMBERT93).geometry.area
        for stored, actual in zip(valid_areas, measured, strict=True):
            tolerance = max(
                CADASTRE_AREA_ABSOLUTE_TOLERANCE_M2,
                abs(float(actual)) * CADASTRE_AREA_RELATIVE_TOLERANCE,
            )
            if abs(float(stored) - float(actual)) > tolerance:
                raise ValueError(
                    "VALID parcel area_m2 differs from measured EPSG:2154 geometry area"
                )
    return parcels
