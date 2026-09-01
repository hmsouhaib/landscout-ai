import re

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
from pyproj import CRS

from landscout.common.cadastre_contract import (
    CADASTRE_NORMALIZED_PREFIX,
    validate_normalized_cadastre_parcels,
)
from landscout.geo.crs import LAMBERT93, WGS84
from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    revalidate_cadastre_parcel_source,
)

FIELD_MAPPING = {
    "id": "parcel_id",
    "commune": "commune_code",
    "prefixe": "section_prefix",
    "section": "section",
    "numero": "parcel_number",
    "contenance": "source_contenance",
    "arpente": "source_arpente",
    "created": "source_created_at",
    "updated": "source_updated_at",
}
REQUIRED_IDENTITY_COLUMNS = frozenset({"id", "commune", "prefixe", "section", "numero"})
CANONICAL_COMMUNE_PATTERN = re.compile(r"^(?:\d{5}|2[AB]\d{3})$")


class CadastreNormalizationError(ValueError):
    """Raised when cadastral parcels cannot be normalized safely."""


def normalize_cadastre_parcels(source: CadastreParcelSource) -> gpd.GeoDataFrame:
    if type(source) is not CadastreParcelSource:
        raise CadastreNormalizationError(
            "Cadastre input must be an exact CadastreParcelSource"
        )
    try:
        parcels = revalidate_cadastre_parcel_source(source)
    except CadastreLoadError as error:
        raise CadastreNormalizationError(
            "Cadastre physical source revalidation failed"
        ) from error
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise CadastreNormalizationError(
            "Fresh Cadastre parcels must be a GeoDataFrame"
        )
    if parcels.columns.duplicated().any():
        raise CadastreNormalizationError("Cadastre input columns must be unique")
    if parcels.crs is None:
        raise CadastreNormalizationError("Cadastre input CRS is required")
    try:
        source_crs = CRS.from_user_input(parcels.crs)
    except Exception as error:
        raise CadastreNormalizationError("Cadastre input CRS is unreadable") from error
    if not source_crs.equals(CRS.from_user_input(WGS84)):
        raise CadastreNormalizationError("Cadastre source geometry must use EPSG:4326")

    missing_columns = REQUIRED_IDENTITY_COLUMNS - set(parcels.columns)
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise CadastreNormalizationError(
            f"Missing required cadastral identity columns: {formatted}"
        )
    target_collisions = (
        set(CADASTRE_NORMALIZED_PREFIX) - {"section", "geometry"}
    ) & set(parcels.columns)
    if target_collisions:
        raise CadastreNormalizationError(
            "Cadastre source attributes collide with normalized columns: "
            + ", ".join(sorted(target_collisions))
        )
    for column in ("id", "commune", "prefixe", "section", "numero"):
        values = parcels[column].tolist()
        if any(
            not isinstance(value, str) or not value or value != value.strip()
            for value in values
        ):
            label = "parcel_id" if column == "id" else column
            raise CadastreNormalizationError(
                f"{label} values must be non-empty exact strings"
            )
    if parcels["id"].duplicated().any():
        raise CadastreNormalizationError("parcel_id values must be unique")
    if any(
        CANONICAL_COMMUNE_PATTERN.fullmatch(value) is None
        for value in parcels["commune"].tolist()
    ):
        raise CadastreNormalizationError(
            "commune values must be canonical French INSEE strings"
        )
    if any(
        value != source.download.commune_code for value in parcels["commune"].tolist()
    ):
        raise CadastreNormalizationError(
            "Cadastre parcel commune differs from its physical download identity"
        )

    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise CadastreNormalizationError("Cadastre geometry column is required")
    if geometry_column != "geometry":
        raise CadastreNormalizationError(
            "Cadastre active geometry must use the canonical geometry name"
        )
    non_null_geometry = parcels.geometry.dropna()
    unsupported = sorted(
        set(non_null_geometry.geom_type.dropna()) - {"Polygon", "MultiPolygon"}
    )
    if unsupported:
        raise CadastreNormalizationError(
            "Cadastre geometry must be Polygon or MultiPolygon; found: "
            + ", ".join(unsupported)
        )
    if any(bool(value) for value in non_null_geometry.has_z):
        raise CadastreNormalizationError("Cadastre geometry must be exactly 2D")

    normalized = parcels.rename(columns=FIELD_MAPPING).reset_index(drop=True).copy()
    for output_column in FIELD_MAPPING.values():
        if output_column not in normalized.columns:
            normalized[output_column] = None

    valid_geometry = (
        ~normalized.geometry.isna()
        & ~normalized.geometry.is_empty
        & normalized.geometry.is_valid
    )
    normalized["geometry_status"] = "INVALID"
    normalized.loc[valid_geometry, "geometry_status"] = "VALID"
    normalized["area_m2"] = float("nan")
    projected = normalized.loc[valid_geometry].to_crs(LAMBERT93)
    normalized.loc[valid_geometry, "area_m2"] = projected.geometry.area
    valid_areas = normalized.loc[valid_geometry, "area_m2"].to_numpy(dtype="float64")
    if not np.isfinite(valid_areas).all() or (valid_areas <= 0).any():
        raise CadastreNormalizationError(
            "VALID cadastre parcel areas must be finite and positive"
        )

    output = gpd.GeoDataFrame(
        normalized[list(CADASTRE_NORMALIZED_PREFIX)],
        geometry="geometry",
        crs=parcels.crs,
    )
    try:
        validate_normalized_cadastre_parcels(output)
    except ValueError as error:
        raise CadastreNormalizationError(str(error)) from error
    return output
