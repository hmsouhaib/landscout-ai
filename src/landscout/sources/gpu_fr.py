"""Official Géoportail de l'Urbanisme document ingestion for France.

This source adapter discovers one currently effective planning document, caches
its official archive, extracts it safely, and reports the source schema.  It
deliberately does not interpret planning rules or classify parcel suitability.
"""

from __future__ import annotations

import json
import math
import re
import shutil
import stat
import unicodedata
import zipfile
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path, PurePosixPath, PureWindowsPath
from shutil import copy2, copyfileobj
from typing import Annotated, Any, Literal
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urljoin, urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree

import geopandas as gpd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
import yaml  # type: ignore[import-untyped]
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
)
from pyproj import CRS

DEFAULT_CONFIG_PATH = Path("configs/sources/gpu_fr.yaml")
DEFAULT_CACHE_DIR = Path("data/cache/gpu")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
USER_AGENT = "LandScout-AI/0.1"

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
CommuneCode = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[0-9]{5}$"),
]
DownloadStrategy = Literal["partition"]
LogicalLayerName = Literal[
    "zoning",
    "prescription_surface",
    "prescription_line",
    "prescription_point",
    "information_surface",
    "information_line",
    "information_point",
]
FileCategory = Literal[
    "SPATIAL_DATA", "METADATA", "WRITTEN_REGULATION", "OTHER_ATTACHMENT"
]


class GpuApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    base_url: HttpUrl

    @field_validator("base_url")
    @classmethod
    def _official_api(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlparse(str(value))
        if parsed.scheme not in {"http", "https"}:
            raise ValueError("GPU API URL must use HTTP(S)")
        if parsed.hostname != "www.geoportail-urbanisme.gouv.fr":
            raise ValueError("GPU API URL must use the official GPU host")
        if parsed.path.rstrip("/") != "/api":
            raise ValueError("GPU API URL must identify the official /api base")
        return value


class GpuDownloadConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    strategy: DownloadStrategy
    partition_template: NonEmptyString

    @field_validator("partition_template")
    @classmethod
    def _valid_partition_template(cls, value: str) -> str:
        if value != value.strip() or value.count("{code_insee}") != 1:
            raise ValueError(
                "partition_template must contain exactly one {code_insee} placeholder"
            )
        try:
            rendered = value.format(code_insee="31395")
        except (KeyError, ValueError) as error:
            raise ValueError("partition_template is malformed") from error
        if not rendered or "/" in rendered or "\\" in rendered:
            raise ValueError("partition_template must render one safe path component")
        return value


class GpuCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    max_age_hours: float = Field(ge=0, allow_inf_nan=False)


class GpuPilotConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commune_code: CommuneCode


class GpuLogicalLayerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    class_label: NonEmptyString
    match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)

    @field_validator("match_tokens")
    @classmethod
    def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(value) for value in values)
        if any(not value for value in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(normalized) != len(set(normalized)):
            raise ValueError("Layer match tokens must be unique after normalization")
        return values


class GpuSpatialLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    zoning: GpuLogicalLayerConfig
    prescription_surface: GpuLogicalLayerConfig
    prescription_line: GpuLogicalLayerConfig
    prescription_point: GpuLogicalLayerConfig
    information_surface: GpuLogicalLayerConfig
    information_line: GpuLogicalLayerConfig
    information_point: GpuLogicalLayerConfig


class GpuSourceConfig(BaseModel):
    """Strict configuration for official French GPU ingestion."""

    model_config = ConfigDict(extra="forbid")

    provider: NonEmptyString
    portal: NonEmptyString
    country: Literal["FR"]
    api: GpuApiConfig
    download: GpuDownloadConfig
    cache: GpuCacheConfig
    pilot: GpuPilotConfig
    spatial_layers: GpuSpatialLayersConfig


class GpuError(RuntimeError):
    """Base class for controlled GPU source failures."""


class GpuConfigError(GpuError):
    """Raised when GPU source configuration is invalid."""


class GpuDiscoveryError(GpuError):
    """Raised when the current planning document cannot be resolved safely."""


class GpuDownloadError(GpuError):
    """Raised when the GPU archive cannot be downloaded or cached safely."""


class GpuArchiveError(GpuError):
    """Raised when a GPU archive or extraction is corrupt or unsafe."""


class GpuSpatialInspectionError(GpuError):
    """Raised when required GPU spatial layers cannot be inspected safely."""


@dataclass(frozen=True)
class GpuWrittenFile:
    filename: str
    title: str | None
    document_path: str | None
    source_url: str | None


@dataclass(frozen=True)
class GpuDocumentMetadata:
    provider: str
    portal: str
    commune_code: str
    partition: str
    document_id: str
    document_family: str
    document_type: str
    document_title: str | None
    status: str
    legal_status: str
    effective_status: str
    version: str | None
    archive_name: str
    publication_timestamp: str | None
    update_timestamp: str | None
    revision_date: str | None
    producer: str | None
    standard_model: str | None
    projection: str | None
    metadata_identifier: str | None
    source_url: str
    written_files: tuple[GpuWrittenFile, ...]


@dataclass(frozen=True)
class GpuArchiveDownload:
    document: GpuDocumentMetadata
    download_timestamp: str
    filename: str
    archive_format: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool


@dataclass(frozen=True)
class GpuExtractedFile:
    relative_path: str
    file_type: str
    size_bytes: int
    category: FileCategory


@dataclass(frozen=True)
class GpuExtraction:
    archive: GpuArchiveDownload
    extraction_root: Path
    files: tuple[GpuExtractedFile, ...]
    standard_models: tuple[str, ...]
    cache_hit: bool


@dataclass(frozen=True)
class GpuSpatialLayerReference:
    dataset_path: Path
    source_layer: str
    driver: str


@dataclass(frozen=True)
class GpuLayerSummary:
    source_document_id: str
    source_archive_sha256: str
    source_layer: str
    crs: str
    feature_count: int
    columns: tuple[str, ...]
    dtypes: tuple[tuple[str, str], ...]
    null_counts: tuple[tuple[str, int], ...]
    geometry_types: tuple[tuple[str, int], ...]
    null_geometry_count: int
    empty_geometry_count: int
    invalid_geometry_count: int


@dataclass(frozen=True)
class GpuInspectedLayer:
    logical_name: LogicalLayerName
    reference: GpuSpatialLayerReference
    data: gpd.GeoDataFrame
    summary: GpuLayerSummary


@dataclass(frozen=True)
class GpuPlanningDocument:
    extraction: GpuExtraction
    all_spatial_layers: tuple[GpuSpatialLayerReference, ...]
    zoning: GpuInspectedLayer
    related_layers: tuple[GpuInspectedLayer, ...]


def _normalize_words(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_value = "".join(char for char in decomposed if not unicodedata.combining(char))
    return "_".join(re.findall(r"[a-z0-9]+", ascii_value.casefold()))


def load_gpu_source_config(path: Path = DEFAULT_CONFIG_PATH) -> GpuSourceConfig:
    """Load and validate the strict GPU source configuration."""

    if not path.is_file():
        raise GpuConfigError(f"GPU source configuration does not exist: {path}")
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise TypeError("GPU source configuration must be a mapping")
        return GpuSourceConfig.model_validate(payload)
    except (OSError, TypeError, yaml.YAMLError, ValidationError) as error:
        raise GpuConfigError(f"Invalid GPU source configuration: {path}") from error


def build_gpu_partition(config: GpuSourceConfig, commune_code: str | None = None) -> str:
    code = commune_code or config.pilot.commune_code
    if not isinstance(code, str) or re.fullmatch(r"[0-9]{5}", code) is None:
        raise GpuConfigError("GPU commune code must contain exactly five digits")
    return config.download.partition_template.format(code_insee=code)


def _api_url(config: GpuSourceConfig, path: str) -> str:
    return urljoin(f"{str(config.api.base_url).rstrip('/')}/", path.lstrip("/"))


def build_gpu_document_list_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
    query = urlencode(
        {"partition": build_gpu_partition(config, commune_code), "page": 0, "limit": 100}
    )
    return f"{_api_url(config, 'document')}?{query}"


def build_gpu_partition_download_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
    partition = quote(build_gpu_partition(config, commune_code), safe="")
    return _api_url(config, f"document/download-by-partition/{partition}")


def _request_json(url: str, timeout: float) -> Any:
    request = Request(url, headers={"Accept": "application/json", "User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise GpuDiscoveryError(f"GPU metadata request failed: {url}") from error


def _required_string(payload: dict[str, Any], key: str, label: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise GpuDiscoveryError(f"GPU {label} is missing or invalid")
    return value


def _optional_string(payload: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = payload.get(key)
        if value is None:
            continue
        if not isinstance(value, (str, int, float)) or isinstance(value, bool):
            raise GpuDiscoveryError(f"GPU metadata field {key} has an invalid value")
        text = str(value)
        if text.strip():
            return text
    return None


def _written_files(
    details: dict[str, Any], payload: Any, document_id: str
) -> tuple[GpuWrittenFile, ...]:
    if not isinstance(payload, list):
        raise GpuDiscoveryError("GPU written-file metadata is not a list")
    materials = details.get("writingMaterials")
    material_urls = materials if isinstance(materials, dict) else {}
    result: list[GpuWrittenFile] = []
    seen: set[str] = set()
    for item in payload:
        if not isinstance(item, dict):
            raise GpuDiscoveryError("GPU written-file entry is invalid")
        filename = _required_string(item, "name", "written filename")
        if filename in seen:
            raise GpuDiscoveryError(f"Duplicate GPU written filename: {filename}")
        seen.add(filename)
        source_url = material_urls.get(filename)
        if source_url is None:
            source_url = _api_url_from_details(details, document_id, filename)
        if not isinstance(source_url, str):
            source_url = None
        result.append(
            GpuWrittenFile(
                filename=filename,
                title=_optional_string(item, "title"),
                document_path=_optional_string(item, "path"),
                source_url=source_url,
            )
        )
    return tuple(sorted(result, key=lambda item: item.filename.casefold()))


def _api_url_from_details(
    details: dict[str, Any], document_id: str, filename: str
) -> str | None:
    archive_url = details.get("archiveUrl")
    if not isinstance(archive_url, str):
        return None
    parsed = urlparse(archive_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None
    return f"{parsed.scheme}://{parsed.netloc}/api/document/{quote(document_id)}/files/{quote(filename)}"


def discover_current_gpu_document(
    config: GpuSourceConfig, commune_code: str | None = None, timeout: float = 60.0
) -> GpuDocumentMetadata:
    """Resolve exactly one official production, approved and in-force DU."""

    code = commune_code or config.pilot.commune_code
    partition = build_gpu_partition(config, code)
    listing = _request_json(build_gpu_document_list_url(config, code), timeout)
    if not isinstance(listing, list):
        raise GpuDiscoveryError("GPU document listing is not a list")
    current: list[dict[str, Any]] = []
    for item in listing:
        if not isinstance(item, dict):
            continue
        grid = item.get("grid")
        grid_code = grid.get("name") if isinstance(grid, dict) else None
        if (
            item.get("status") == "document.production"
            and item.get("legalStatus") == "APPROVED"
            and item.get("effectiveStatus") == "EN_VIGUEUR"
            and item.get("name") == partition
            and grid_code == code
        ):
            current.append(item)
    if not current:
        raise GpuDiscoveryError(
            f"No current approved and in-force GPU document for {partition}"
        )
    if len(current) != 1:
        raise GpuDiscoveryError(
            f"Ambiguous current GPU document selection for {partition}: {len(current)}"
        )

    selected = current[0]
    document_id = _required_string(selected, "id", "document ID")
    archive_name = _required_string(selected, "originalName", "archive name")
    details_url = _api_url(config, f"document/{quote(document_id)}/details")
    files_url = _api_url(config, f"document/{quote(document_id)}/files")
    details_payload = _request_json(details_url, timeout)
    files_payload = _request_json(files_url, timeout)
    if not isinstance(details_payload, dict):
        raise GpuDiscoveryError("GPU document details are not an object")
    details = details_payload
    if details.get("id") != document_id or details.get("originalName") != archive_name:
        raise GpuDiscoveryError("GPU document details do not match the selected document")
    detail_grid = details.get("grid")
    if not isinstance(detail_grid, dict) or detail_grid.get("name") != code:
        raise GpuDiscoveryError("GPU document details do not match the commune")
    document_type = _required_string(details, "type", "document type")
    source_url = build_gpu_partition_download_url(config, code)
    return GpuDocumentMetadata(
        provider=config.provider,
        portal=config.portal,
        commune_code=code,
        partition=partition,
        document_id=document_id,
        document_family="DU",
        document_type=document_type,
        document_title=_optional_string(details, "title"),
        status=_required_string(details, "status", "status"),
        legal_status=_required_string(details, "legalStatus", "legal status"),
        effective_status=_required_string(details, "effectiveStatus", "effective status"),
        version=_optional_string(details, "version"),
        archive_name=archive_name,
        publication_timestamp=_optional_string(details, "publicationDate"),
        update_timestamp=_optional_string(details, "updateDate"),
        revision_date=_optional_string(details, "revisionDate", "referenceDate"),
        producer=_optional_string(details, "producer"),
        standard_model=_optional_string(details, "standard", "model", "documentModel"),
        projection=_optional_string(details, "projectionCode"),
        metadata_identifier=_optional_string(details, "metadata", "fileIdentifier"),
        source_url=source_url,
        written_files=_written_files(details, files_payload, document_id),
    )


def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(DOWNLOAD_CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_archive_member(name: str) -> bool:
    if not name or "\x00" in name:
        return False
    posix = PurePosixPath(name.replace("\\", "/"))
    windows = PureWindowsPath(name)
    return not (
        posix.is_absolute()
        or windows.is_absolute()
        or windows.drive
        or any(part == ".." for part in posix.parts)
    )


def validate_gpu_archive(path: Path) -> tuple[str, ...]:
    """Fully validate a ZIP archive and return its deterministic member inventory."""

    if not path.is_file() or path.stat().st_size <= 0:
        raise GpuArchiveError(f"GPU archive is missing or empty: {path}")
    if not zipfile.is_zipfile(path):
        raise GpuArchiveError(f"GPU archive is not a readable ZIP: {path}")
    try:
        with zipfile.ZipFile(path) as archive:
            members = archive.infolist()
            if not members:
                raise GpuArchiveError("GPU ZIP contains no members")
            names: list[str] = []
            for member in members:
                if not _safe_archive_member(member.filename):
                    raise GpuArchiveError(
                        f"Unsafe path in GPU archive: {member.filename}"
                    )
                mode = member.external_attr >> 16
                if stat.S_ISLNK(mode):
                    raise GpuArchiveError(
                        f"Symbolic links are not allowed in GPU archive: {member.filename}"
                    )
                names.append(member.filename)
            bad_member = archive.testzip()
            if bad_member is not None:
                raise GpuArchiveError(f"Corrupt GPU ZIP member: {bad_member}")
    except GpuArchiveError:
        raise
    except (OSError, zipfile.BadZipFile, RuntimeError) as error:
        raise GpuArchiveError(f"Cannot validate GPU ZIP archive: {path}") from error
    return tuple(sorted(names, key=str.casefold))


def _document_identity(document: GpuDocumentMetadata) -> dict[str, Any]:
    result = asdict(document)
    result["written_files"] = [asdict(item) for item in document.written_files]
    return result


def _document_from_dict(payload: Any) -> GpuDocumentMetadata:
    if not isinstance(payload, dict):
        raise TypeError("Cached GPU document metadata is invalid")
    values = dict(payload)
    files = values.pop("written_files")
    if not isinstance(files, list):
        raise TypeError("Cached GPU written-file metadata is invalid")
    written: list[GpuWrittenFile] = []
    for item in files:
        if not isinstance(item, dict):
            raise TypeError("Cached GPU written-file entry is invalid")
        written.append(GpuWrittenFile(**item))
    return GpuDocumentMetadata(**values, written_files=tuple(written))


def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)


def _publish_cache_pair(
    temporary_archive: Path,
    temporary_metadata: Path,
    archive_path: Path,
    metadata_path: Path,
) -> None:
    archive_backup = archive_path.with_suffix(f"{archive_path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
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
    publication_started = False
    try:
        publication_started = True
        _replace_file(temporary_archive, archive_path)
        _replace_file(temporary_metadata, metadata_path)
    except OSError:
        try:
            if publication_started:
                if archive_existed:
                    _replace_file(archive_backup, archive_path)
                else:
                    archive_path.unlink(missing_ok=True)
                if metadata_existed:
                    _replace_file(metadata_backup, metadata_path)
                else:
                    metadata_path.unlink(missing_ok=True)
        except OSError as rollback_error:
            raise GpuDownloadError(
                "GPU cache publication and rollback both failed"
            ) from rollback_error
        raise
    finally:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)


def _load_cached_archive(
    archive_path: Path,
    metadata_path: Path,
    document: GpuDocumentMetadata,
    max_age_hours: float,
) -> GpuArchiveDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        payload = json.loads(metadata_path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            return None
        cached_document = _document_from_dict(payload["document"])
        timestamp = payload["download_timestamp"]
        if not isinstance(timestamp, str):
            return None
        downloaded_at = datetime.fromisoformat(timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() is None:
            return None
        age = (datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds()
        members = validate_gpu_archive(archive_path)
        checksum = _sha256(archive_path)
        size = archive_path.stat().st_size
        if not (
            0 <= age <= max_age_hours * 3600
            and cached_document == document
            and payload.get("filename") == archive_path.name
            and payload.get("archive_format") == "zip"
            and payload.get("file_size") == size
            and payload.get("sha256") == checksum
            and payload.get("member_count") == len(members)
        ):
            return None
        return GpuArchiveDownload(
            document=document,
            download_timestamp=timestamp,
            filename=archive_path.name,
            archive_format="zip",
            file_size=size,
            sha256=checksum,
            path=archive_path,
            cache_hit=True,
        )
    except (
        KeyError,
        OSError,
        TypeError,
        ValueError,
        json.JSONDecodeError,
        GpuArchiveError,
    ):
        return None


def download_gpu_document(
    document: GpuDocumentMetadata,
    config: GpuSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> GpuArchiveDownload:
    """Download and transactionally cache one discovered official GPU ZIP."""

    filename = f"{document.archive_name}.zip"
    archive_path = cache_dir / filename
    metadata_path = cache_dir / f"{filename}.metadata.json"
    cached = _load_cached_archive(
        archive_path, metadata_path, document, config.cache.max_age_hours
    )
    if cached is not None:
        return cached
    cache_dir.mkdir(parents=True, exist_ok=True)
    temporary_archive = archive_path.with_suffix(f"{archive_path.suffix}.part")
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    try:
        request = Request(document.source_url, headers={"User-Agent": USER_AGENT})
        with (
            urlopen(request, timeout=timeout) as response,
            temporary_archive.open("wb") as output,
        ):
            copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)
        members = validate_gpu_archive(temporary_archive)
        result = GpuArchiveDownload(
            document=document,
            download_timestamp=datetime.now(UTC).isoformat(),
            filename=filename,
            archive_format="zip",
            file_size=temporary_archive.stat().st_size,
            sha256=_sha256(temporary_archive),
            path=archive_path,
            cache_hit=False,
        )
        lineage = {
            "document": _document_identity(document),
            "download_timestamp": result.download_timestamp,
            "filename": filename,
            "archive_format": result.archive_format,
            "file_size": result.file_size,
            "sha256": result.sha256,
            "member_count": len(members),
        }
        temporary_metadata.write_text(
            json.dumps(lineage, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        _publish_cache_pair(
            temporary_archive, temporary_metadata, archive_path, metadata_path
        )
        return result
    except (HTTPError, URLError, OSError, GpuArchiveError) as error:
        raise GpuDownloadError(
            f"GPU document download failed: {document.source_url}"
        ) from error
    finally:
        temporary_archive.unlink(missing_ok=True)
        temporary_metadata.unlink(missing_ok=True)


def _classify_file(path: Path) -> FileCategory:
    suffix = path.suffix.casefold()
    if suffix in {
        ".gpkg",
        ".shp",
        ".shx",
        ".dbf",
        ".prj",
        ".cpg",
        ".qmd",
        ".qix",
        ".sbn",
        ".sbx",
    }:
        return "SPATIAL_DATA"
    if suffix in {".xml", ".json", ".yaml", ".yml", ".csv", ".txt"}:
        return "METADATA"
    if suffix in {".pdf", ".odt", ".doc", ".docx"}:
        return "WRITTEN_REGULATION"
    return "OTHER_ATTACHMENT"


def _inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    files: list[GpuExtractedFile] = []
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=str):
        resolved = path.resolve()
        try:
            relative = resolved.relative_to(root.resolve())
        except ValueError as error:
            raise GpuArchiveError(f"Extracted GPU file escapes cache: {path}") from error
        if path.is_symlink():
            raise GpuArchiveError(f"Extracted GPU symbolic link is forbidden: {path}")
        files.append(
            GpuExtractedFile(
                relative_path=relative.as_posix(),
                file_type=path.suffix.casefold().lstrip(".") or "none",
                size_bytes=path.stat().st_size,
                category=_classify_file(path),
            )
        )
    if not files:
        raise GpuArchiveError("Extracted GPU package contains no files")
    return tuple(files)


def _discover_standard_models(root: Path) -> tuple[str, ...]:
    models: set[str] = set()
    for path in sorted(root.rglob("*.xml"), key=str):
        try:
            parsed = ElementTree.parse(path)
        except (OSError, ElementTree.ParseError):
            continue
        for element in parsed.iter():
            text = element.text.strip() if element.text else ""
            if re.fullmatch(r"CNIG\s+[A-Za-z]+\s+v\d{4}", text, re.IGNORECASE):
                models.add(text)
    return tuple(sorted(models, key=str.casefold))


def extract_gpu_document(
    download: GpuArchiveDownload, cache_dir: Path = DEFAULT_CACHE_DIR
) -> GpuExtraction:
    """Safely extract a validated GPU ZIP into a content-addressed cache."""

    validate_gpu_archive(download.path)
    root = cache_dir / "x" / download.sha256[:16]
    marker = root / ".landscout-gpu-extraction.json"
    if root.is_dir() and marker.is_file():
        try:
            payload = json.loads(marker.read_text(encoding="utf-8"))
            files = _inventory(root)
            visible_count = sum(
                item.relative_path != marker.name for item in files
            )
            if (
                payload.get("archive_sha256") == download.sha256
                and payload.get("file_count") == visible_count
            ):
                return GpuExtraction(
                    archive=download,
                    extraction_root=root,
                    files=tuple(item for item in files if item.relative_path != marker.name),
                    standard_models=_discover_standard_models(root),
                    cache_hit=True,
                )
        except (OSError, ValueError, json.JSONDecodeError, GpuArchiveError):
            pass
    root.parent.mkdir(parents=True, exist_ok=True)
    temporary_root = root.with_name(f"{root.name}.part")
    if temporary_root.exists():
        shutil.rmtree(temporary_root)
    temporary_root.mkdir()
    try:
        with zipfile.ZipFile(download.path) as archive:
            for member in archive.infolist():
                target = (temporary_root / member.filename).resolve()
                try:
                    target.relative_to(temporary_root.resolve())
                except ValueError as error:
                    raise GpuArchiveError(
                        f"Unsafe extraction target: {member.filename}"
                    ) from error
            archive.extractall(temporary_root)
        files = _inventory(temporary_root)
        marker_payload = {
            "archive_sha256": download.sha256,
            "file_count": len(files),
        }
        (temporary_root / marker.name).write_text(
            json.dumps(marker_payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        if root.exists():
            shutil.rmtree(root)
        shutil.move(str(temporary_root), str(root))
        return GpuExtraction(
            archive=download,
            extraction_root=root,
            files=files,
            standard_models=_discover_standard_models(root),
            cache_hit=False,
        )
    except (OSError, zipfile.BadZipFile, GpuArchiveError) as error:
        if isinstance(error, GpuArchiveError):
            raise
        raise GpuArchiveError("Cannot safely extract GPU document") from error
    finally:
        if temporary_root.exists():
            shutil.rmtree(temporary_root)


def discover_gpu_spatial_layers(
    extraction: GpuExtraction,
) -> tuple[GpuSpatialLayerReference, ...]:
    """Discover every real GeoPackage or Shapefile layer in an extraction."""

    root = extraction.extraction_root
    references: list[GpuSpatialLayerReference] = []
    gpkg_paths = sorted(root.rglob("*.gpkg"), key=str)
    shp_paths = sorted(root.rglob("*.shp"), key=str)
    for path in gpkg_paths:
        try:
            layers = pyogrio.list_layers(path)
        except Exception as error:
            raise GpuSpatialInspectionError(
                f"Cannot list GPU GeoPackage layers: {path}"
            ) from error
        for raw_name in layers[:, 0].tolist():
            if isinstance(raw_name, str) and raw_name:
                references.append(
                    GpuSpatialLayerReference(path, raw_name, "GPKG")
                )
    for path in shp_paths:
        references.append(GpuSpatialLayerReference(path, path.stem, "ESRI Shapefile"))
    if not references:
        raise GpuSpatialInspectionError("GPU document contains no supported spatial data")
    unique = {(item.dataset_path.resolve(), item.source_layer) for item in references}
    if len(unique) != len(references):
        raise GpuSpatialInspectionError("GPU document exposes duplicate spatial layers")
    return tuple(
        sorted(references, key=lambda item: (str(item.dataset_path), item.source_layer))
    )


def _layer_config(
    config: GpuSourceConfig, logical_name: LogicalLayerName
) -> GpuLogicalLayerConfig:
    return getattr(config.spatial_layers, logical_name)


def _discover_logical_layer(
    references: tuple[GpuSpatialLayerReference, ...],
    config: GpuSourceConfig,
    logical_name: LogicalLayerName,
    *,
    required: bool,
) -> GpuSpatialLayerReference | None:
    configured = _layer_config(config, logical_name)
    tokens = {_normalize_words(value) for value in configured.match_tokens}
    matches = []
    for item in references:
        normalized_name = f"_{_normalize_words(item.source_layer)}_"
        if any(f"_{token}_" in normalized_name for token in tokens):
            matches.append(item)
    if not matches and not required:
        return None
    if len(matches) != 1:
        adjective = "exactly one" if required else "at most one"
        raise GpuSpatialInspectionError(
            f"Expected {adjective} {logical_name} layer, found {len(matches)}"
        )
    return matches[0]


def _load_reference(reference: GpuSpatialLayerReference) -> gpd.GeoDataFrame:
    try:
        if reference.driver == "GPKG":
            return gpd.read_file(
                reference.dataset_path, layer=reference.source_layer, engine="pyogrio"
            )
        return gpd.read_file(reference.dataset_path, engine="pyogrio")
    except Exception as error:
        raise GpuSpatialInspectionError(
            f"Cannot load GPU spatial layer: {reference.source_layer}"
        ) from error


def _crs_text(frame: gpd.GeoDataFrame) -> str:
    if frame.crs is None:
        return "UNKNOWN"
    authority = CRS.from_user_input(frame.crs).to_authority()
    return f"{authority[0]}:{authority[1]}" if authority else frame.crs.to_string()


def _summarize_layer(
    frame: gpd.GeoDataFrame,
    reference: GpuSpatialLayerReference,
    extraction: GpuExtraction,
) -> GpuLayerSummary:
    if frame.geometry.name not in frame.columns:
        raise GpuSpatialInspectionError(
            f"GPU layer has no active geometry: {reference.source_layer}"
        )
    geometry = frame.geometry
    non_null = geometry.notna()
    non_empty = non_null & ~geometry.is_empty
    invalid = non_empty & ~geometry.is_valid
    geometry_types = tuple(
        (str(key), int(value))
        for key, value in geometry[non_null].geom_type.value_counts().sort_index().items()
    )
    return GpuLayerSummary(
        source_document_id=extraction.archive.document.document_id,
        source_archive_sha256=extraction.archive.sha256,
        source_layer=reference.source_layer,
        crs=_crs_text(frame),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in frame.dtypes.items()),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=geometry_types,
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int(invalid.sum()),
    )


def inspect_gpu_planning_document(
    extraction: GpuExtraction, config: GpuSourceConfig
) -> GpuPlanningDocument:
    """Discover and inspect zoning/prescription layers without interpretation."""

    references = discover_gpu_spatial_layers(extraction)
    zoning_reference = _discover_logical_layer(
        references, config, "zoning", required=True
    )
    assert zoning_reference is not None
    zoning_data = _load_reference(zoning_reference)
    zoning = GpuInspectedLayer(
        logical_name="zoning",
        reference=zoning_reference,
        data=zoning_data,
        summary=_summarize_layer(zoning_data, zoning_reference, extraction),
    )
    related: list[GpuInspectedLayer] = []
    logical_names: tuple[LogicalLayerName, ...] = (
        "prescription_surface",
        "prescription_line",
        "prescription_point",
        "information_surface",
        "information_line",
        "information_point",
    )
    for logical_name in logical_names:
        reference = _discover_logical_layer(
            references, config, logical_name, required=False
        )
        if reference is None:
            continue
        data = _load_reference(reference)
        related.append(
            GpuInspectedLayer(
                logical_name=logical_name,
                reference=reference,
                data=data,
                summary=_summarize_layer(data, reference, extraction),
            )
        )
    return GpuPlanningDocument(
        extraction=extraction,
        all_spatial_layers=references,
        zoning=zoning,
        related_layers=tuple(related),
    )


def ingest_gpu_planning_document(
    config: GpuSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> GpuPlanningDocument:
    """High-level official GPU discovery, acquisition, extraction and inspection."""

    document = discover_current_gpu_document(config, timeout=timeout)
    download = download_gpu_document(document, config, cache_dir, timeout)
    extraction = extract_gpu_document(download, cache_dir)
    return inspect_gpu_planning_document(extraction, config)


def finite_numeric_vocabulary(
    frame: gpd.GeoDataFrame, column: str
) -> tuple[tuple[str, int], ...]:
    """Return deterministic raw value counts for inspection-only reporting."""

    if column not in frame.columns or column == frame.geometry.name:
        raise GpuSpatialInspectionError(f"Cannot inspect GPU attribute: {column}")
    counts = frame[column].value_counts(dropna=False)
    result: list[tuple[str, int]] = []
    for value, count in counts.items():
        if isinstance(value, float) and math.isnan(value) or value is None:
            label = "<NULL>"
        else:
            label = str(value)
        result.append((label, int(count)))
    return tuple(sorted(result, key=lambda item: item[0]))
