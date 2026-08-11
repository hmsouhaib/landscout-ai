import geopandas as gpd  # type: ignore[import-untyped]

from landscout.geo.crs import LAMBERT93, WGS84

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
REQUIRED_IDENTITY_COLUMNS = frozenset(
    {"id", "commune", "prefixe", "section", "numero"}
)


class CadastreNormalizationError(ValueError):
    """Raised when cadastral parcels cannot be normalized safely."""


def normalize_cadastre_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    if parcels.crs is None:
        raise CadastreNormalizationError("Cadastre input CRS is required")
    if parcels.crs != WGS84:
        raise CadastreNormalizationError("Cadastre source geometry must use EPSG:4326")

    missing_columns = REQUIRED_IDENTITY_COLUMNS - set(parcels.columns)
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise CadastreNormalizationError(
            f"Missing required cadastral identity columns: {formatted}"
        )
    if parcels["id"].isna().any():
        raise CadastreNormalizationError("parcel_id values must not be null")
    if parcels["id"].duplicated().any():
        raise CadastreNormalizationError("parcel_id values must be unique")

    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise CadastreNormalizationError("Cadastre geometry column is required")

    normalized = parcels.rename(columns=FIELD_MAPPING).copy()
    for output_column in FIELD_MAPPING.values():
        if output_column not in normalized.columns:
            normalized[output_column] = None

    valid_geometry = (
        normalized.geometry.notna()
        & ~normalized.geometry.is_empty
        & normalized.geometry.is_valid
    )
    normalized["geometry_status"] = "INVALID"
    normalized.loc[valid_geometry, "geometry_status"] = "VALID"
    normalized["area_m2"] = float("nan")
    projected = normalized.loc[valid_geometry].to_crs(LAMBERT93)
    normalized.loc[valid_geometry, "area_m2"] = projected.geometry.area

    output_columns = [
        *FIELD_MAPPING.values(),
        "geometry_status",
        "area_m2",
        geometry_column,
    ]
    return gpd.GeoDataFrame(
        normalized[output_columns], geometry=geometry_column, crs=parcels.crs
    )
