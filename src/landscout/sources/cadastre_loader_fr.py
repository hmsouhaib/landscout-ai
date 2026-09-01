"""Source-bound loading and physical revalidation for Cadastre parcels."""

import gzip
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pyogrio.errors import DataSourceError  # type: ignore[import-untyped]

from landscout.sources.cadastre_fr import (
    CadastreDownload,
    build_cadastre_parcelles_url,
)

__all__ = [
    "CadastreLoadError",
    "CadastreParcelSource",
    "EmptyCadastreDatasetError",
    "MissingGeometryColumnError",
    "UnsupportedGeometryTypeError",
    "load_cadastre_parcels",
    "revalidate_cadastre_parcel_source",
]

SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})


class CadastreLoadError(RuntimeError):
    """Base error for controlled cadastre loading failures."""


class EmptyCadastreDatasetError(CadastreLoadError):
    """Raised when a cadastre dataset contains no parcel records."""


class MissingGeometryColumnError(CadastreLoadError):
    """Raised when a cadastre dataset has no active geometry column."""


class UnsupportedGeometryTypeError(CadastreLoadError):
    """Raised when a cadastre dataset contains non-parcel geometry types."""


@dataclass(frozen=True)
class CadastreParcelSource:
    """One physical Cadastre download bound to its parsed parcel frame."""

    download: CadastreDownload
    parcels: gpd.GeoDataFrame


def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True


def _physical_integrity(path: Path) -> tuple[int, str]:
    try:
        size = path.stat().st_size
        digest = sha256(path.read_bytes()).hexdigest()
    except OSError as error:
        raise CadastreLoadError(f"Cannot inspect cadastre dataset: {path}") from error
    return size, digest


def _validate_download(download: object) -> CadastreDownload:
    try:
        if type(download) is not CadastreDownload:
            raise TypeError("Cadastre source must be an exact CadastreDownload")
        if type(download.commune_code) is not str:
            raise TypeError("Cadastre commune code is invalid")
        official_url = build_cadastre_parcelles_url(download.commune_code)
        official_filename = official_url.rsplit("/", maxsplit=1)[-1]
        if download.source_url != official_url:
            raise ValueError("Cadastre download source URL is not the official URL")
        if download.filename != official_filename:
            raise ValueError("Cadastre download filename is not official")
        path = download.path
        if not isinstance(path, Path):
            raise TypeError("Cadastre download path must be a pathlib.Path")
        if _is_link_or_junction(path) or not path.is_file():
            raise ValueError("Cadastre dataset must exist as a regular non-linked file")
        if path.name != official_filename:
            raise ValueError("Cadastre download filename does not match its path")
        if type(download.file_size) is not int or download.file_size <= 0:
            raise TypeError("Cadastre download size must be a strict positive integer")
        if (
            type(download.sha256) is not str
            or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
        ):
            raise ValueError("Cadastre download SHA256 must be lowercase hexadecimal")
        if type(download.download_timestamp) is not str:
            raise TypeError("Cadastre download timestamp must be an exact string")
        downloaded_at = datetime.fromisoformat(download.download_timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(
            None
        ):
            raise ValueError("Cadastre download timestamp must be timezone-aware UTC")
        if type(download.cache_hit) is not bool:
            raise TypeError("Cadastre cache-hit state must be an exact Boolean")
        size, digest = _physical_integrity(path)
        if size != download.file_size:
            raise ValueError("Cadastre physical size differs from verified download")
        if digest != download.sha256:
            raise ValueError("Cadastre physical SHA256 differs from verified download")
        try:
            with gzip.open(path, "rb") as stream:
                while stream.read(1024 * 1024):
                    pass
        except (EOFError, OSError) as error:
            raise ValueError("Cadastre verified source is not valid gzip") from error
        return download
    except CadastreLoadError:
        raise
    except Exception as error:
        detail = str(error) or "Cadastre download envelope is invalid"
        raise CadastreLoadError(detail) from error


def _read_physical_parcels(download: CadastreDownload) -> gpd.GeoDataFrame:
    path = download.path
    source_path = f"/vsigzip/{path.resolve().as_posix()}"
    try:
        parcels = gpd.read_file(source_path, engine="pyogrio")
    except (DataSourceError, OSError, ValueError) as error:
        raise CadastreLoadError(f"Unable to read cadastre dataset: {path}") from error

    size_after, digest_after = _physical_integrity(path)
    if size_after != download.file_size or digest_after != download.sha256:
        raise CadastreLoadError("Cadastre physical source changed during parsing")
    if parcels.empty:
        raise EmptyCadastreDatasetError(f"Cadastre dataset is empty: {path}")
    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise MissingGeometryColumnError("Cadastre dataset has no geometry column")
    if geometry_column != "geometry":
        raise MissingGeometryColumnError(
            "Cadastre dataset active geometry must use the canonical geometry name"
        )
    non_null = parcels.geometry.dropna()
    unsupported_types = set(non_null.geom_type.dropna()) - SUPPORTED_GEOMETRY_TYPES
    if unsupported_types:
        formatted_types = ", ".join(sorted(unsupported_types))
        raise UnsupportedGeometryTypeError(
            f"Unsupported cadastre geometry types: {formatted_types}"
        )
    if any(bool(value) for value in non_null.has_z):
        raise UnsupportedGeometryTypeError(
            "Cadastre parcel geometry must be exactly 2D"
        )
    return parcels


def _compare_parcel_frames(
    supplied: object,
    expected: gpd.GeoDataFrame,
) -> None:
    try:
        if not isinstance(supplied, gpd.GeoDataFrame):
            raise TypeError("supplied parcels are not a GeoDataFrame")
        if tuple(supplied.columns) != tuple(expected.columns):
            raise AssertionError("columns differ")
        if tuple(str(dtype) for dtype in supplied.dtypes) != tuple(
            str(dtype) for dtype in expected.dtypes
        ):
            raise AssertionError("dtypes differ")
        if type(supplied.index) is not type(expected.index):
            raise AssertionError("index type differs")
        if supplied.index.names != expected.index.names or not supplied.index.equals(
            expected.index
        ):
            raise AssertionError("index differs")
        if supplied.active_geometry_name != expected.active_geometry_name:
            raise AssertionError("active geometry differs")
        if supplied.crs != expected.crs:
            raise AssertionError("CRS differs")
        geometry_name = expected.active_geometry_name
        if geometry_name is None:
            raise AssertionError("geometry is missing")
        pd.testing.assert_frame_equal(
            pd.DataFrame(supplied.drop(columns=geometry_name)),
            pd.DataFrame(expected.drop(columns=geometry_name)),
            check_dtype=True,
            check_index_type=True,
            check_column_type=True,
            check_names=True,
            check_exact=True,
        )
        if (
            supplied.geometry.to_wkb(hex=True).tolist()
            != expected.geometry.to_wkb(hex=True).tolist()
        ):
            raise AssertionError("geometry WKB differs")
        if supplied.attrs != expected.attrs:
            raise AssertionError("frame attributes differ")
    except Exception as error:
        raise CadastreLoadError(
            "Supplied Cadastre parcels differ from freshly read physical source"
        ) from error


def load_cadastre_parcels(download: CadastreDownload) -> CadastreParcelSource:
    """Load parcels while retaining the verified physical source authority."""

    verified = _validate_download(download)
    return CadastreParcelSource(
        download=verified,
        parcels=_read_physical_parcels(verified),
    )


def revalidate_cadastre_parcel_source(
    source: object,
) -> gpd.GeoDataFrame:
    """Fresh-read and exact-compare one supplied Cadastre parcel source."""

    try:
        if type(source) is not CadastreParcelSource:
            raise TypeError("Cadastre parcel source type is invalid")
        verified = _validate_download(source.download)
        fresh = _read_physical_parcels(verified)
        _compare_parcel_frames(source.parcels, fresh)
        return fresh
    except CadastreLoadError:
        raise
    except Exception as error:
        raise CadastreLoadError(
            "Cadastre source-complete revalidation failed"
        ) from error
