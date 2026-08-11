from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
from pyogrio.errors import DataSourceError  # type: ignore[import-untyped]

SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})


class CadastreLoadError(RuntimeError):
    """Base error for controlled cadastre loading failures."""


class EmptyCadastreDatasetError(CadastreLoadError):
    """Raised when a cadastre dataset contains no parcel records."""


class MissingGeometryColumnError(CadastreLoadError):
    """Raised when a cadastre dataset has no active geometry column."""


class UnsupportedGeometryTypeError(CadastreLoadError):
    """Raised when a cadastre dataset contains non-parcel geometry types."""


def load_cadastre_parcels(path: Path) -> gpd.GeoDataFrame:
    if not path.is_file():
        raise FileNotFoundError(f"Cadastre dataset does not exist: {path}")

    source: Path | str = path
    if path.suffix.lower() == ".gz":
        source = f"/vsigzip/{path.resolve().as_posix()}"
    try:
        parcels = gpd.read_file(source, engine="pyogrio")
    except (DataSourceError, OSError, ValueError) as error:
        raise CadastreLoadError(f"Unable to read cadastre dataset: {path}") from error

    if parcels.empty:
        raise EmptyCadastreDatasetError(f"Cadastre dataset is empty: {path}")
    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise MissingGeometryColumnError("Cadastre dataset has no geometry column")

    geometry_types = set(parcels.geometry.geom_type.dropna().unique())
    unsupported_types = geometry_types - SUPPORTED_GEOMETRY_TYPES
    if unsupported_types:
        formatted_types = ", ".join(sorted(unsupported_types))
        raise UnsupportedGeometryTypeError(
            f"Unsupported cadastre geometry types: {formatted_types}"
        )
    return parcels
