"""Official IGN BD TOPO archive ingestion for spatial screening sources.

This adapter deliberately stops at source acquisition, archive/layer discovery,
and source-layer loading. IGN geometries are screening proxies and are not
claimed to prove exact current grid assets, connection points, or legal access.
"""

from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass
from datetime import UTC, date, datetime
from hashlib import md5, sha256
from pathlib import Path, PurePosixPath, PureWindowsPath
from shutil import copy2, copyfileobj
from typing import Annotated, Any, Literal, Self
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

import geopandas as gpd  # type: ignore[import-untyped]
import py7zr
import pyogrio  # type: ignore[import-untyped]
import yaml  # type: ignore[import-untyped]
from py7zr.exceptions import ArchiveError
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
    model_validator,
)
from pyproj import CRS

DEFAULT_CONFIG_PATH = Path("configs/sources/ign_bdtopo_fr.yaml")
DEFAULT_CACHE_DIR = Path("data/cache/ign_bdtopo")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
SPATIAL_ROLE = "PROXY_GEOMETRY"
COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"

SpatialRole = Literal["PROXY_GEOMETRY"]
CoverageSpatialRole = Literal["SOURCE_COVERAGE_BOUNDARY"]
LogicalLayerName = Literal[
    "electric_lines",
    "transformation_posts",
    "road_segments",
]
Projection = Literal["EPSG:2154"]
PackageFormat = Literal["GPKG"]
ArchiveFormat = Literal["7z"]
ChecksumAlgorithm = Literal["md5", "sha256"]

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
DepartmentCode = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=r"^(?:[0-9]{2}|2A|2B|97[1-6])$",
    ),
]
EditionString = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^\d{4}-\d{2}-\d{2}$"),
]
HexChecksum = Annotated[
    str,
    StringConstraints(strip_whitespace=True, to_lower=True, pattern=r"^[0-9a-fA-F]+$"),
]
CanonicalSha256 = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^[0-9a-f]{64}$"),
]
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]


class IgnBdTopoLogicalLayerConfig(BaseModel):
    """Catalogue class label and normalized tokens used for layer discovery."""

    model_config = ConfigDict(extra="forbid")

    class_label: NonEmptyString
    match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)

    @field_validator("match_tokens")
    @classmethod
    def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(token) for token in value)
        if any(not token for token in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(set(normalized)) != len(normalized):
            raise ValueError("Layer match tokens must be unique after normalization")
        return value


class IgnBdTopoLogicalLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    electric_lines: IgnBdTopoLogicalLayerConfig
    transformation_posts: IgnBdTopoLogicalLayerConfig

    @model_validator(mode="after")
    def _different_token_sets(self) -> Self:
        electric = {
            _normalize_words(token) for token in self.electric_lines.match_tokens
        }
        posts = {
            _normalize_words(token)
            for token in self.transformation_posts.match_tokens
        }
        if electric == posts:
            raise ValueError("Logical layers must use different match tokens")
        return self


class IgnBdTopoDepartmentLayerConfig(IgnBdTopoLogicalLayerConfig):
    """Configured department layer and its observed identity field."""

    department_code_field: NonEmptyString


class IgnBdTopoAccessConfig(BaseModel):
    """Configured factual transport layers loaded outside extraction metadata."""

    model_config = ConfigDict(extra="forbid")

    road_segments: IgnBdTopoLogicalLayerConfig


class IgnBdTopoCoverageConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    department_layer: IgnBdTopoDepartmentLayerConfig


class IgnBdTopoSourceConfig(BaseModel):
    """Strict, reproducible description of one official IGN package."""

    model_config = ConfigDict(extra="forbid")

    provider: NonEmptyString
    product: NonEmptyString
    department_code: DepartmentCode
    edition: EditionString
    product_version: NonEmptyString | None = None
    projection: Projection
    format: PackageFormat
    archive_format: ArchiveFormat
    source_url: HttpUrl
    checksum_url: HttpUrl | None = None
    official_checksum_algorithm: ChecksumAlgorithm | None = None
    official_checksum: HexChecksum | None = None
    expected_archive_size_bytes: int | None = Field(default=None, gt=0)
    cache_max_age_hours: float = Field(ge=0, allow_inf_nan=False)
    logical_layers: IgnBdTopoLogicalLayersConfig
    access: IgnBdTopoAccessConfig
    coverage: IgnBdTopoCoverageConfig

    @field_validator("edition")
    @classmethod
    def _valid_edition_date(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError as error:
            raise ValueError("edition must be a valid ISO calendar date") from error
        return value

    @model_validator(mode="after")
    def _consistent_package_and_checksum(self) -> Self:
        path = unquote(urlparse(str(self.source_url)).path)
        if Path(path).suffix.casefold() != f".{self.archive_format}":
            raise ValueError("source_url extension does not match archive_format")

        has_algorithm = self.official_checksum_algorithm is not None
        has_checksum = self.official_checksum is not None
        if has_algorithm != has_checksum:
            raise ValueError(
                "official_checksum_algorithm and official_checksum must be set together"
            )
        if self.official_checksum_algorithm == "md5" and len(
            self.official_checksum or ""
        ) != 32:
            raise ValueError("An official MD5 checksum must contain 32 hexadecimal digits")
        if self.official_checksum_algorithm == "sha256" and len(
            self.official_checksum or ""
        ) != 64:
            raise ValueError(
                "An official SHA256 checksum must contain 64 hexadecimal digits"
            )
        if self.checksum_url is not None and not has_checksum:
            raise ValueError(
                "checksum_url requires a pinned official checksum and algorithm"
            )
        return self


class IgnBdTopoError(RuntimeError):
    """Base error for controlled IGN BD TOPO source failures."""


class IgnBdTopoDownloadError(IgnBdTopoError):
    """Raised when an IGN archive cannot be downloaded or cached safely."""


class IgnBdTopoArchiveError(IgnBdTopoError):
    """Raised when an IGN archive or its extraction is unsafe or invalid."""


class IgnBdTopoLayerError(IgnBdTopoError):
    """Raised when required GeoPackage layers cannot be discovered or loaded."""


@dataclass(frozen=True)
class IgnBdTopoArchiveIntegrity:
    file_size: int
    sha256: str
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: bool


@dataclass(frozen=True)
class IgnBdTopoDownload:
    provider: str
    product: str
    department_code: str
    edition: str
    product_version: str | None
    projection: str
    package_format: str
    archive_format: str
    source_url: str
    checksum_url: str | None
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: bool
    path: Path
    cache_hit: bool
    spatial_role: SpatialRole = "PROXY_GEOMETRY"


@dataclass(frozen=True)
class IgnBdTopoLayerSelection:
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str


@dataclass(frozen=True)
class IgnBdTopoExtraction:
    archive: IgnBdTopoDownload
    extraction_path: Path
    geopackage_path: Path
    geopackage_filename: str
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    cache_hit: bool
    spatial_role: SpatialRole = "PROXY_GEOMETRY"


@dataclass(frozen=True)
class IgnBdTopoLayerSummary:
    logical_name: LogicalLayerName
    source_layer_name: str
    crs: str
    feature_count: int
    columns: tuple[str, ...]
    dtypes: tuple[tuple[str, str], ...]
    null_geometry_count: int
    empty_geometry_count: int
    invalid_geometry_count: int
    geometry_types: tuple[str, ...]
    spatial_role: SpatialRole = "PROXY_GEOMETRY"


@dataclass(frozen=True)
class IgnBdTopoLoadedLayer:
    data: gpd.GeoDataFrame
    summary: IgnBdTopoLayerSummary


@dataclass(frozen=True)
class IgnBdTopoElectricityData:
    extraction: IgnBdTopoExtraction
    electric_lines: gpd.GeoDataFrame
    transformation_posts: gpd.GeoDataFrame
    electric_lines_summary: IgnBdTopoLayerSummary
    transformation_posts_summary: IgnBdTopoLayerSummary
    spatial_role: SpatialRole = "PROXY_GEOMETRY"


@dataclass(frozen=True)
class IgnBdTopoRoadData:
    """Unfiltered factual road geometry from one verified IGN extraction."""

    extraction: IgnBdTopoExtraction
    road_segments: gpd.GeoDataFrame
    road_segments_summary: IgnBdTopoLayerSummary


@dataclass(frozen=True)
class IgnBdTopoCoverageLayerSummary:
    """Observed source-layer schema plus the authoritative selected feature."""

    source_layer_name: str
    crs: str
    source_feature_count: int
    selected_feature_count: int
    columns: tuple[str, ...]
    dtypes: tuple[tuple[str, str], ...]
    null_geometry_count: int
    empty_geometry_count: int
    invalid_geometry_count: int
    geometry_types: tuple[str, ...]
    department_code_field: str
    selected_department_code: str
    spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"


@dataclass(frozen=True)
class IgnBdTopoDepartmentCoverage:
    """Selected department coverage with package lineage and source schema."""

    coverage: gpd.GeoDataFrame
    summary: IgnBdTopoCoverageLayerSummary
    source_provider: str
    source_product: str
    source_department_code: str
    source_edition: str
    source_product_version: str | None
    source_archive_sha256: str
    source_layer: str
    spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"


class _CacheMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1]
    provider: str
    product: str
    department_code: str
    edition: str
    product_version: str | None
    projection: str
    package_format: str
    archive_format: str
    source_url: str
    checksum_url: str | None
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: bool
    spatial_role: SpatialRole


class _ExtractionMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[2]
    archive_sha256: CanonicalSha256
    geopackage_relative_path: str
    geopackage_size_bytes: StrictPositiveInt
    geopackage_sha256: CanonicalSha256
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    spatial_role: SpatialRole


def _normalize_words(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    ascii_like = "".join(char for char in decomposed if not unicodedata.combining(char))
    return " ".join(re.findall(r"[a-z0-9]+", ascii_like))


def load_ign_bdtopo_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> IgnBdTopoSourceConfig:
    """Load and strictly validate the pinned IGN source configuration."""

    try:
        with path.open(encoding="utf-8") as stream:
            content = yaml.safe_load(stream)
    except OSError as error:
        raise IgnBdTopoDownloadError(f"Cannot read IGN source config: {path}") from error
    if not isinstance(content, dict):
        raise TypeError(f"Expected a YAML mapping in {path}")
    return IgnBdTopoSourceConfig.model_validate(content)


def _archive_filename(config: IgnBdTopoSourceConfig) -> str:
    filename = Path(unquote(urlparse(str(config.source_url)).path)).name
    if not filename or Path(filename).suffix.casefold() != ".7z":
        raise IgnBdTopoDownloadError("IGN source URL does not identify a .7z archive")
    return filename


def _calculate_checksums(
    path: Path, official_algorithm: ChecksumAlgorithm | None
) -> tuple[str, str | None]:
    sha256_digest = sha256()
    official_digest = None
    if official_algorithm == "md5":
        official_digest = md5(usedforsecurity=False)
    elif official_algorithm == "sha256":
        official_digest = sha256()

    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
                sha256_digest.update(chunk)
                if official_digest is not None:
                    official_digest.update(chunk)
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot read IGN archive: {path}") from error
    return (
        sha256_digest.hexdigest(),
        official_digest.hexdigest() if official_digest is not None else None,
    )


def validate_ign_bdtopo_archive(
    path: Path, config: IgnBdTopoSourceConfig
) -> IgnBdTopoArchiveIntegrity:
    """Validate size, configured official checksum, and available 7z CRC data.

    Some official IGN archives omit container CRC metadata, for which py7zr
    returns ``None``.  Such archives still require exact official size/checksum
    validation here and a successful full extraction before they are usable.
    """

    if not path.is_file():
        raise IgnBdTopoArchiveError(f"IGN archive does not exist: {path}")
    try:
        file_size = path.stat().st_size
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot inspect IGN archive: {path}") from error
    if file_size <= 0:
        raise IgnBdTopoArchiveError(f"IGN archive is empty: {path}")
    if (
        config.expected_archive_size_bytes is not None
        and file_size != config.expected_archive_size_bytes
    ):
        raise IgnBdTopoArchiveError(
            "IGN archive size does not match the official catalogue: "
            f"{file_size} != {config.expected_archive_size_bytes}"
        )

    local_sha256, calculated_official = _calculate_checksums(
        path, config.official_checksum_algorithm
    )
    official_validated = config.official_checksum is not None
    if official_validated and calculated_official != config.official_checksum:
        raise IgnBdTopoArchiveError(
            "IGN archive does not match the pinned official "
            f"{config.official_checksum_algorithm} checksum"
        )

    try:
        with py7zr.SevenZipFile(path, mode="r") as archive:
            integrity_result = archive.test()
    except (ArchiveError, EOFError, OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"IGN archive is not a readable 7z file: {path}"
        ) from error
    if integrity_result is False:
        raise IgnBdTopoArchiveError(
            f"IGN archive failed its 7z CRC integrity check: {path}"
        )

    return IgnBdTopoArchiveIntegrity(
        file_size=file_size,
        sha256=local_sha256,
        official_checksum_algorithm=config.official_checksum_algorithm,
        official_checksum=config.official_checksum,
        official_checksum_validated=official_validated,
    )


def _cache_metadata_from_download(download: IgnBdTopoDownload) -> _CacheMetadata:
    return _CacheMetadata(
        schema_version=1,
        provider=download.provider,
        product=download.product,
        department_code=download.department_code,
        edition=download.edition,
        product_version=download.product_version,
        projection=download.projection,
        package_format=download.package_format,
        archive_format=download.archive_format,
        source_url=download.source_url,
        checksum_url=download.checksum_url,
        download_timestamp=download.download_timestamp,
        filename=download.filename,
        file_size=download.file_size,
        sha256=download.sha256,
        official_checksum_algorithm=download.official_checksum_algorithm,
        official_checksum=download.official_checksum,
        official_checksum_validated=download.official_checksum_validated,
        spatial_role=download.spatial_role,
    )


def _download_from_metadata(
    metadata: _CacheMetadata, archive_path: Path, *, cache_hit: bool
) -> IgnBdTopoDownload:
    return IgnBdTopoDownload(
        provider=metadata.provider,
        product=metadata.product,
        department_code=metadata.department_code,
        edition=metadata.edition,
        product_version=metadata.product_version,
        projection=metadata.projection,
        package_format=metadata.package_format,
        archive_format=metadata.archive_format,
        source_url=metadata.source_url,
        checksum_url=metadata.checksum_url,
        download_timestamp=metadata.download_timestamp,
        filename=metadata.filename,
        file_size=metadata.file_size,
        sha256=metadata.sha256,
        official_checksum_algorithm=metadata.official_checksum_algorithm,
        official_checksum=metadata.official_checksum,
        official_checksum_validated=metadata.official_checksum_validated,
        path=archive_path,
        cache_hit=cache_hit,
        spatial_role=metadata.spatial_role,
    )


def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        metadata = _CacheMetadata.model_validate_json(
            metadata_path.read_text(encoding="utf-8")
        )
        downloaded_at = datetime.fromisoformat(metadata.download_timestamp)
        if downloaded_at.tzinfo is None:
            return None
        age_seconds = (
            datetime.now(UTC) - downloaded_at.astimezone(UTC)
        ).total_seconds()
        if age_seconds < 0 or age_seconds > config.cache_max_age_hours * 3600:
            return None

        expected_values: tuple[tuple[Any, Any], ...] = (
            (metadata.provider, config.provider),
            (metadata.product, config.product),
            (metadata.department_code, config.department_code),
            (metadata.edition, config.edition),
            (metadata.product_version, config.product_version),
            (metadata.projection, config.projection),
            (metadata.package_format, config.format),
            (metadata.archive_format, config.archive_format),
            (metadata.source_url, str(config.source_url)),
            (
                metadata.checksum_url,
                str(config.checksum_url) if config.checksum_url is not None else None,
            ),
            (metadata.filename, archive_path.name),
            (
                metadata.official_checksum_algorithm,
                config.official_checksum_algorithm,
            ),
            (metadata.official_checksum, config.official_checksum),
            (metadata.spatial_role, SPATIAL_ROLE),
        )
        if any(actual != expected for actual, expected in expected_values):
            return None

        integrity = validate_ign_bdtopo_archive(archive_path, config)
        if (
            metadata.file_size != integrity.file_size
            or metadata.sha256 != integrity.sha256
            or metadata.official_checksum_validated
            != integrity.official_checksum_validated
        ):
            return None
        return _download_from_metadata(metadata, archive_path, cache_hit=True)
    except (
        IgnBdTopoArchiveError,
        OSError,
        TypeError,
        ValueError,
        ValidationError,
    ):
        return None


def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)


def _publish_cache_pair(
    temporary_archive: Path,
    temporary_metadata: Path,
    archive_path: Path,
    metadata_path: Path,
) -> None:
    archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    archive_existed = archive_path.is_file()
    metadata_existed = metadata_path.is_file()

    archive_backup.unlink(missing_ok=True)
    metadata_backup.unlink(missing_ok=True)
    try:
        if archive_existed:
            copy2(archive_path, archive_backup)
        if metadata_existed:
            copy2(metadata_path, metadata_backup)
    except OSError:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise

    archive_published = False
    try:
        _replace_file(temporary_archive, archive_path)
        archive_published = True
        _replace_file(temporary_metadata, metadata_path)
    except OSError:
        try:
            if archive_published:
                if archive_existed:
                    _replace_file(archive_backup, archive_path)
                else:
                    archive_path.unlink(missing_ok=True)
            if not metadata_existed:
                metadata_path.unlink(missing_ok=True)
        except OSError as rollback_error:
            raise IgnBdTopoDownloadError(
                "IGN cache publication and rollback both failed"
            ) from rollback_error
        raise
    finally:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)


def download_ign_bdtopo_archive(
    config: IgnBdTopoSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> IgnBdTopoDownload:
    """Download or reuse the pinned IGN package with atomic cache publication."""

    filename = _archive_filename(config)
    archive_path = cache_dir / filename
    metadata_path = cache_dir / f"{filename}.metadata.json"
    cached = _load_cached_download(archive_path, metadata_path, config)
    if cached is not None:
        return cached

    cache_dir.mkdir(parents=True, exist_ok=True)
    temporary_archive = archive_path.with_name(f"{archive_path.name}.part")
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    temporary_archive.unlink(missing_ok=True)
    temporary_metadata.unlink(missing_ok=True)
    source_url = str(config.source_url)
    try:
        request = Request(source_url, headers={"User-Agent": "LandScout-AI/0.1"})
        with (
            urlopen(request, timeout=timeout) as response,
            temporary_archive.open("wb") as output,
        ):
            copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)

        integrity = validate_ign_bdtopo_archive(temporary_archive, config)
        download_timestamp = datetime.now(UTC).isoformat()
        result = IgnBdTopoDownload(
            provider=config.provider,
            product=config.product,
            department_code=config.department_code,
            edition=config.edition,
            product_version=config.product_version,
            projection=config.projection,
            package_format=config.format,
            archive_format=config.archive_format,
            source_url=source_url,
            checksum_url=(
                str(config.checksum_url) if config.checksum_url is not None else None
            ),
            download_timestamp=download_timestamp,
            filename=filename,
            file_size=integrity.file_size,
            sha256=integrity.sha256,
            official_checksum_algorithm=integrity.official_checksum_algorithm,
            official_checksum=integrity.official_checksum,
            official_checksum_validated=integrity.official_checksum_validated,
            path=archive_path,
            cache_hit=False,
        )
        metadata = _cache_metadata_from_download(result)
        temporary_metadata.write_text(
            metadata.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        _publish_cache_pair(
            temporary_archive, temporary_metadata, archive_path, metadata_path
        )
        return result
    except IgnBdTopoArchiveError:
        raise
    except (HTTPError, URLError, OSError) as error:
        raise IgnBdTopoDownloadError(f"IGN download failed: {source_url}") from error
    finally:
        temporary_archive.unlink(missing_ok=True)
        temporary_metadata.unlink(missing_ok=True)


def _validate_archive_members(archive: py7zr.SevenZipFile) -> None:
    infos = archive.list()
    if not infos:
        raise IgnBdTopoArchiveError("IGN archive contains no members")
    for info in infos:
        name = info.filename
        if not name or "\x00" in name:
            raise IgnBdTopoArchiveError("IGN archive contains an invalid member name")
        normalized_name = name.replace("\\", "/")
        posix_path = PurePosixPath(normalized_name)
        windows_path = PureWindowsPath(name)
        if (
            posix_path.is_absolute()
            or windows_path.is_absolute()
            or bool(windows_path.drive)
            or ".." in posix_path.parts
        ):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsafe member path: {name}"
            )
        if info.is_symlink or not (
            info.is_file or info.is_directory
        ):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsupported link or special member: {name}"
            )


def discover_ign_bdtopo_geopackage(root: Path) -> Path:
    """Return the sole GeoPackage below an extracted package root."""

    if root.is_file():
        if root.suffix.casefold() == ".gpkg":
            return root
        raise IgnBdTopoArchiveError(f"Expected a GeoPackage, got: {root}")
    if not root.is_dir():
        raise IgnBdTopoArchiveError(f"Extraction directory does not exist: {root}")
    geopackages = sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix.casefold() == ".gpkg"
        ),
        key=lambda path: path.as_posix().casefold(),
    )
    if len(geopackages) != 1:
        raise IgnBdTopoArchiveError(
            "Expected exactly one GeoPackage in the IGN package, found "
            f"{len(geopackages)}"
        )
    return geopackages[0]


def list_ign_bdtopo_layers(geopackage_path: Path) -> tuple[str, ...]:
    """List every real layer name exposed by an IGN GeoPackage."""

    if not geopackage_path.is_file():
        raise IgnBdTopoLayerError(f"GeoPackage does not exist: {geopackage_path}")
    try:
        listed = pyogrio.list_layers(geopackage_path)
        names = tuple(str(row[0]) for row in listed)
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"Cannot list layers in GeoPackage: {geopackage_path}"
        ) from error
    if not names or any(not name.strip() for name in names):
        raise IgnBdTopoLayerError("GeoPackage exposes no valid layer names")
    if len(set(names)) != len(names):
        raise IgnBdTopoLayerError("GeoPackage exposes duplicate layer names")
    return names


def _matching_layers(
    layer_names: tuple[str, ...], logical_config: IgnBdTopoLogicalLayerConfig
) -> tuple[str, ...]:
    token_words: set[str] = set()
    for token in logical_config.match_tokens:
        token_words.update(_normalize_words(token).split())
    matches = []
    for layer_name in layer_names:
        layer_words = set(_normalize_words(layer_name).split())
        if token_words.issubset(layer_words):
            matches.append(layer_name)
    return tuple(matches)


def discover_ign_bdtopo_layers(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoLayerSelection:
    """Resolve both configured logical classes without assuming exact casing."""

    layer_names = list_ign_bdtopo_layers(geopackage_path)
    electric_matches = _matching_layers(
        layer_names, config.logical_layers.electric_lines
    )
    post_matches = _matching_layers(
        layer_names, config.logical_layers.transformation_posts
    )
    if len(electric_matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous electric-line layer for "
            f"'{config.logical_layers.electric_lines.class_label}', found "
            f"{len(electric_matches)}: {electric_matches}"
        )
    if len(post_matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous transformation-post layer for "
            f"'{config.logical_layers.transformation_posts.class_label}', found "
            f"{len(post_matches)}: {post_matches}"
        )
    if electric_matches[0] == post_matches[0]:
        raise IgnBdTopoLayerError(
            "Electric-line and transformation-post discovery selected the same layer"
        )
    return IgnBdTopoLayerSelection(
        all_layer_names=layer_names,
        electric_lines_layer=electric_matches[0],
        transformation_posts_layer=post_matches[0],
    )


def _discover_department_coverage_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
    matches = _matching_layers(layer_names, config.coverage.department_layer)
    if len(matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous department coverage layer for "
            f"'{config.coverage.department_layer.class_label}', found "
            f"{len(matches)}: {matches}"
        )
    return matches[0]


def _discover_road_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
    matches = _matching_layers(layer_names, config.access.road_segments)
    if len(matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous road-segment layer for "
            f"'{config.access.road_segments.class_label}', found "
            f"{len(matches)}: {matches}"
        )
    return matches[0]


def _safe_relative_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except (OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"Extracted GeoPackage escapes its extraction root: {path}"
        ) from error


def _resolve_relative_path(root: Path, relative_path: str) -> Path:
    posix_path = PurePosixPath(relative_path)
    windows_path = PureWindowsPath(relative_path)
    if (
        not relative_path
        or posix_path.is_absolute()
        or windows_path.is_absolute()
        or bool(windows_path.drive)
        or ".." in posix_path.parts
    ):
        raise IgnBdTopoArchiveError(
            "Cached extraction metadata contains an unsafe GeoPackage path"
        )
    candidate = root.joinpath(*posix_path.parts)
    try:
        candidate.resolve().relative_to(root.resolve())
    except (OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            "Cached GeoPackage path escapes its extraction root"
        ) from error
    return candidate


def _geopackage_integrity(path: Path) -> tuple[int, str]:
    if not path.is_file():
        raise IgnBdTopoArchiveError(f"IGN GeoPackage does not exist: {path}")
    try:
        size_bytes = path.stat().st_size
    except OSError as error:
        raise IgnBdTopoArchiveError(
            f"Cannot inspect IGN GeoPackage: {path}"
        ) from error
    if size_bytes <= 0:
        raise IgnBdTopoArchiveError(f"IGN GeoPackage is empty: {path}")
    digest = sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
                digest.update(chunk)
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot read IGN GeoPackage: {path}") from error
    return size_bytes, digest.hexdigest()


def _load_cached_extraction(
    extraction_path: Path,
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoExtraction | None:
    metadata_path = extraction_path / ".landscout-extraction.json"
    if not extraction_path.is_dir() or not metadata_path.is_file():
        return None
    try:
        metadata = _ExtractionMetadata.model_validate_json(
            metadata_path.read_text(encoding="utf-8")
        )
        if (
            metadata.archive_sha256 != download.sha256
            or metadata.spatial_role != SPATIAL_ROLE
        ):
            return None
        geopackage_path = _resolve_relative_path(
            extraction_path, metadata.geopackage_relative_path
        )
        discovered_path = discover_ign_bdtopo_geopackage(extraction_path)
        if geopackage_path.resolve() != discovered_path.resolve():
            return None
        geopackage_size, geopackage_sha256 = _geopackage_integrity(
            geopackage_path
        )
        if (
            geopackage_size != metadata.geopackage_size_bytes
            or geopackage_sha256 != metadata.geopackage_sha256
        ):
            return None
        selection = discover_ign_bdtopo_layers(geopackage_path, config)
        if (
            selection.all_layer_names != metadata.all_layer_names
            or selection.electric_lines_layer != metadata.electric_lines_layer
            or selection.transformation_posts_layer
            != metadata.transformation_posts_layer
        ):
            return None
        return IgnBdTopoExtraction(
            archive=download,
            extraction_path=extraction_path,
            geopackage_path=geopackage_path,
            geopackage_filename=geopackage_path.name,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            cache_hit=True,
        )
    except (
        IgnBdTopoArchiveError,
        IgnBdTopoLayerError,
        OSError,
        ValidationError,
        ValueError,
    ):
        return None


def _replace_directory(source: Path, target: Path) -> None:
    source.replace(target)


def _remove_tree(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def _publish_extraction_directory(
    temporary_path: Path, extraction_path: Path
) -> None:
    backup_path = extraction_path.with_name(f"{extraction_path.name}.bak")
    _remove_tree(backup_path)
    extraction_existed = extraction_path.exists()
    if extraction_existed:
        _replace_directory(extraction_path, backup_path)
    try:
        _replace_directory(temporary_path, extraction_path)
    except OSError:
        try:
            if extraction_existed:
                _replace_directory(backup_path, extraction_path)
        except OSError as rollback_error:
            raise IgnBdTopoArchiveError(
                "IGN extraction publication and rollback both failed"
            ) from rollback_error
        raise
    else:
        _remove_tree(backup_path)


def extract_ign_bdtopo_archive(
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
    extraction_dir: Path | None = None,
) -> IgnBdTopoExtraction:
    """Safely extract the package and resolve its required electricity layers."""

    integrity = validate_ign_bdtopo_archive(download.path, config)
    if integrity.sha256 != download.sha256:
        raise IgnBdTopoArchiveError(
            "Downloaded IGN archive checksum changed before extraction"
        )
    extraction_path = extraction_dir or (
        download.path.parent / "x" / download.sha256[:16]
    )
    if extraction_path.exists() and not extraction_path.is_dir():
        raise IgnBdTopoArchiveError(
            f"IGN extraction target exists and is not a directory: {extraction_path}"
        )
    cached = _load_cached_extraction(extraction_path, download, config)
    if cached is not None:
        return cached

    extraction_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = extraction_path.with_name(f"{extraction_path.name}.part")
    _remove_tree(temporary_path)
    temporary_path.mkdir(parents=True)
    try:
        with py7zr.SevenZipFile(download.path, mode="r") as archive:
            _validate_archive_members(archive)
            archive.extractall(path=temporary_path)

        geopackage_path = discover_ign_bdtopo_geopackage(temporary_path)
        selection = discover_ign_bdtopo_layers(geopackage_path, config)
        relative_path = _safe_relative_path(geopackage_path, temporary_path)
        geopackage_size, geopackage_sha256 = _geopackage_integrity(
            geopackage_path
        )
        metadata = _ExtractionMetadata(
            schema_version=2,
            archive_sha256=download.sha256,
            geopackage_relative_path=relative_path,
            geopackage_size_bytes=geopackage_size,
            geopackage_sha256=geopackage_sha256,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            spatial_role="PROXY_GEOMETRY",
        )
        (temporary_path / ".landscout-extraction.json").write_text(
            metadata.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        _publish_extraction_directory(temporary_path, extraction_path)
        published_geopackage = _resolve_relative_path(extraction_path, relative_path)
        return IgnBdTopoExtraction(
            archive=download,
            extraction_path=extraction_path,
            geopackage_path=published_geopackage,
            geopackage_filename=published_geopackage.name,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            cache_hit=False,
        )
    except (ArchiveError, EOFError, OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"IGN archive extraction failed: {download.path}"
        ) from error
    finally:
        _remove_tree(temporary_path)


def _validate_lambert93(crs_value: Any, layer_name: str) -> CRS:
    if crs_value is None:
        raise IgnBdTopoLayerError(f"IGN layer has no CRS: {layer_name}")
    try:
        crs = CRS.from_user_input(crs_value)
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"IGN layer has an unreadable CRS: {layer_name}"
        ) from error
    if not crs.is_projected:
        raise IgnBdTopoLayerError(
            f"IGN layer CRS must be projected: {layer_name} ({crs.to_string()})"
        )
    expected = CRS.from_epsg(2154)
    if not crs.equals(expected):
        raise IgnBdTopoLayerError(
            "IGN layer CRS is not Lambert-93 / EPSG:2154 compatible: "
            f"{layer_name} ({crs.to_string()})"
        )
    return crs


def load_ign_bdtopo_layer(
    geopackage_path: Path,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
    """Load and validate one selected IGN layer without repairing geometry."""

    if not geopackage_path.is_file():
        raise IgnBdTopoLayerError(f"GeoPackage does not exist: {geopackage_path}")
    if not layer_name.strip():
        raise IgnBdTopoLayerError("IGN source layer name must not be empty")
    try:
        frame = gpd.read_file(
            geopackage_path,
            layer=layer_name,
            engine="pyogrio",
        )
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"Cannot load IGN GeoPackage layer: {layer_name}"
        ) from error

    if not isinstance(frame, gpd.GeoDataFrame):
        raise IgnBdTopoLayerError(f"IGN layer is not spatial: {layer_name}")
    try:
        geometry_name = frame.geometry.name
    except (AttributeError, ValueError) as error:
        raise IgnBdTopoLayerError(
            f"IGN layer has no active geometry column: {layer_name}"
        ) from error
    if geometry_name not in frame.columns:
        raise IgnBdTopoLayerError(
            f"IGN layer geometry column is missing: {layer_name}"
        )
    crs = _validate_lambert93(frame.crs, layer_name)
    if frame.empty:
        raise IgnBdTopoLayerError(f"IGN layer contains no features: {layer_name}")

    geometry = frame.geometry
    null_mask = geometry.isna()
    non_null_mask = ~null_mask
    empty_mask = non_null_mask & geometry.is_empty
    measurable_mask = non_null_mask & ~geometry.is_empty
    invalid_mask = measurable_mask & ~geometry.is_valid
    geometry_types = tuple(
        sorted(str(value) for value in geometry[non_null_mask].geom_type.dropna().unique())
    )
    summary = IgnBdTopoLayerSummary(
        logical_name=logical_name,
        source_layer_name=layer_name,
        crs=crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype))
            for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
    )
    return IgnBdTopoLoadedLayer(data=frame, summary=summary)


def load_ign_bdtopo_electricity(
    extraction: IgnBdTopoExtraction,
) -> IgnBdTopoElectricityData:
    """Load only the two electricity layers selected during extraction."""

    electric_lines = load_ign_bdtopo_layer(
        extraction.geopackage_path,
        extraction.electric_lines_layer,
        "electric_lines",
    )
    transformation_posts = load_ign_bdtopo_layer(
        extraction.geopackage_path,
        extraction.transformation_posts_layer,
        "transformation_posts",
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=electric_lines.data,
        transformation_posts=transformation_posts.data,
        electric_lines_summary=electric_lines.summary,
        transformation_posts_summary=transformation_posts.summary,
    )


def load_ign_bdtopo_roads(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
    """Load the configured factual road layer without filtering or repair."""

    if config.department_code != extraction.archive.department_code:
        raise IgnBdTopoLayerError(
            "IGN road config department does not match archive lineage"
        )
    actual_layers = list_ign_bdtopo_layers(extraction.geopackage_path)
    if actual_layers != extraction.all_layer_names:
        raise IgnBdTopoLayerError(
            "IGN extraction layer inventory changed before road loading"
        )
    layer_name = _discover_road_layer(actual_layers, config)
    if layer_name in {
        extraction.electric_lines_layer,
        extraction.transformation_posts_layer,
    }:
        raise IgnBdTopoLayerError(
            "Road, electric-line, and transformation-post roles must use distinct layers"
        )
    loaded = load_ign_bdtopo_layer(
        extraction.geopackage_path,
        layer_name,
        "road_segments",
    )
    return IgnBdTopoRoadData(
        extraction=extraction,
        road_segments=loaded.data,
        road_segments_summary=loaded.summary,
    )


def load_ign_bdtopo_department_coverage(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
    """Load the one authoritative configured department coverage feature."""

    archive = extraction.archive
    if config.department_code != archive.department_code:
        raise IgnBdTopoLayerError(
            "IGN coverage config department does not match archive lineage"
        )
    actual_layers = list_ign_bdtopo_layers(extraction.geopackage_path)
    if actual_layers != extraction.all_layer_names:
        raise IgnBdTopoLayerError(
            "IGN extraction layer inventory changed before coverage loading"
        )
    layer_name = _discover_department_coverage_layer(actual_layers, config)
    try:
        frame = gpd.read_file(
            extraction.geopackage_path,
            layer=layer_name,
            engine="pyogrio",
        )
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"Cannot load IGN department coverage layer: {layer_name}"
        ) from error
    if not isinstance(frame, gpd.GeoDataFrame):
        raise IgnBdTopoLayerError(
            f"IGN department coverage layer is not spatial: {layer_name}"
        )
    try:
        geometry_name = frame.geometry.name
    except (AttributeError, ValueError) as error:
        raise IgnBdTopoLayerError(
            f"IGN department coverage layer has no active geometry: {layer_name}"
        ) from error
    if geometry_name not in frame.columns:
        raise IgnBdTopoLayerError(
            f"IGN department coverage geometry column is missing: {layer_name}"
        )
    crs = _validate_lambert93(frame.crs, layer_name)
    if frame.empty:
        raise IgnBdTopoLayerError(
            f"IGN department coverage layer contains no features: {layer_name}"
        )

    geometry = frame.geometry
    null_mask = geometry.isna()
    non_null_mask = ~null_mask
    empty_mask = non_null_mask & geometry.is_empty
    measurable_mask = non_null_mask & ~geometry.is_empty
    invalid_mask = measurable_mask & ~geometry.is_valid
    geometry_types = tuple(
        sorted(
            str(value)
            for value in geometry[non_null_mask].geom_type.dropna().unique()
        )
    )

    department_field = config.coverage.department_layer.department_code_field
    if department_field not in frame.columns:
        raise IgnBdTopoLayerError(
            "Configured department identity field is missing from IGN coverage "
            f"layer: {department_field}"
        )
    selected_mask = frame[department_field].eq(archive.department_code)
    selected_count = int(selected_mask.sum())
    if selected_count != 1:
        raise IgnBdTopoLayerError(
            "Expected exactly one authoritative department coverage feature for "
            f"{archive.department_code}, found {selected_count}"
        )
    selected = frame.loc[selected_mask].reset_index(drop=True).copy()
    selected_geometry = selected.geometry
    if selected_geometry.isna().any():
        raise IgnBdTopoLayerError("Selected department coverage geometry is null")
    if selected_geometry.is_empty.any():
        raise IgnBdTopoLayerError("Selected department coverage geometry is empty")
    if not selected_geometry.is_valid.all():
        raise IgnBdTopoLayerError("Selected department coverage geometry is invalid")
    selected_types = set(selected_geometry.geom_type.dropna())
    if not selected_types <= {"Polygon", "MultiPolygon"}:
        raise IgnBdTopoLayerError(
            "Selected department coverage geometry must be Polygon or MultiPolygon"
        )

    lineage = {
        "source_provider": archive.provider,
        "source_product": archive.product,
        "source_department_code": archive.department_code,
        "source_edition": archive.edition,
        "source_product_version": archive.product_version,
        "source_archive_sha256": archive.sha256,
        "source_layer": layer_name,
        "spatial_role": COVERAGE_SPATIAL_ROLE,
    }
    collisions = set(lineage) & set(selected.columns)
    if collisions:
        raise IgnBdTopoLayerError(
            "IGN department coverage attributes collide with lineage columns: "
            + ", ".join(sorted(collisions))
        )
    for column, value in lineage.items():
        selected[column] = value

    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name=layer_name,
        crs=crs.to_string(),
        source_feature_count=len(frame),
        selected_feature_count=selected_count,
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype))
            for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
        department_code_field=department_field,
        selected_department_code=archive.department_code,
    )
    return IgnBdTopoDepartmentCoverage(
        coverage=selected,
        summary=summary,
        source_provider=archive.provider,
        source_product=archive.product,
        source_department_code=archive.department_code,
        source_edition=archive.edition,
        source_product_version=archive.product_version,
        source_archive_sha256=archive.sha256,
        source_layer=layer_name,
    )
