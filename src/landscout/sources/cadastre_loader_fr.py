import gzip
import re
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlparse

import geopandas as gpd  # type: ignore[import-untyped]
from pyogrio.errors import DataSourceError  # type: ignore[import-untyped]

from landscout.sources.cadastre_fr import CadastreDownload

SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})


class CadastreLoadError(RuntimeError):
    """Base error for controlled cadastre loading failures."""


class EmptyCadastreDatasetError(CadastreLoadError):
    """Raised when a cadastre dataset contains no parcel records."""


class MissingGeometryColumnError(CadastreLoadError):
    """Raised when a cadastre dataset has no active geometry column."""


class UnsupportedGeometryTypeError(CadastreLoadError):
    """Raised when a cadastre dataset contains non-parcel geometry types."""


def _physical_integrity(path: Path) -> tuple[int, str]:
    try:
        size = path.stat().st_size
        digest = sha256(path.read_bytes()).hexdigest()
    except OSError as error:
        raise CadastreLoadError(f"Cannot inspect cadastre dataset: {path}") from error
    return size, digest


def _validate_download(download: object) -> CadastreDownload:
    if type(download) is not CadastreDownload:
        raise CadastreLoadError("Cadastre source must be an exact CadastreDownload")
    path = download.path
    if not isinstance(path, Path):
        raise CadastreLoadError("Cadastre download path must be a Path")
    if not path.is_file():
        raise CadastreLoadError(f"Cadastre dataset does not exist: {path}")
    if (
        not isinstance(download.source_url, str)
        or not download.source_url
        or download.source_url != download.source_url.strip()
        or urlparse(download.source_url).scheme not in {"http", "https"}
    ):
        raise CadastreLoadError("Cadastre download source URL is invalid")
    if (
        not isinstance(download.filename, str)
        or not download.filename
        or download.filename != download.filename.strip()
        or download.filename != path.name
    ):
        raise CadastreLoadError("Cadastre download filename does not match its path")
    if type(download.file_size) is not int or download.file_size <= 0:
        raise CadastreLoadError("Cadastre download size must be a strict positive integer")
    if (
        not isinstance(download.sha256, str)
        or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
    ):
        raise CadastreLoadError("Cadastre download SHA256 must be lowercase hexadecimal")
    size, digest = _physical_integrity(path)
    if size != download.file_size:
        raise CadastreLoadError("Cadastre physical size differs from verified download")
    if digest != download.sha256:
        raise CadastreLoadError("Cadastre physical SHA256 differs from verified download")
    try:
        with gzip.open(path, "rb") as stream:
            while stream.read(1024 * 1024):
                pass
    except (EOFError, OSError) as error:
        raise CadastreLoadError("Cadastre verified source is not valid gzip") from error
    return download


def load_cadastre_parcels(download: CadastreDownload) -> gpd.GeoDataFrame:
    """Load parcels from one byte-verified cadastral download envelope."""

    verified = _validate_download(download)
    path = verified.path

    source = f"/vsigzip/{path.resolve().as_posix()}"
    try:
        parcels = gpd.read_file(source, engine="pyogrio")
    except (DataSourceError, OSError, ValueError) as error:
        raise CadastreLoadError(f"Unable to read cadastre dataset: {path}") from error

    size_after, digest_after = _physical_integrity(path)
    if size_after != verified.file_size or digest_after != verified.sha256:
        raise CadastreLoadError("Cadastre physical source changed during parsing")

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
