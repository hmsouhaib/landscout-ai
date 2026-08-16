"""Verified acquisition and factual inventory of the official INPN EP archive.

This source adapter deliberately stops at byte acquisition, safe extraction,
and exact file inventory.  It does not interpret protected-area categories,
open spatial files, intersect parcels, or produce environmental decisions.
"""

from __future__ import annotations

import ipaddress
import json
import re
import shutil
import socket
import stat
import unicodedata
import zipfile
import zlib
from contextlib import suppress
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from math import isfinite
from numbers import Real
from pathlib import Path, PurePosixPath, PureWindowsPath
from shutil import copy2, copyfileobj
from typing import Annotated, Any, Literal, Self
from urllib.parse import urljoin, urlsplit

import requests  # type: ignore[import-untyped]
import yaml  # type: ignore[import-untyped]
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

DEFAULT_CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
DOWNLOAD_METADATA_SCHEMA_VERSION: Literal[1] = 1
EXTRACTION_METADATA_SCHEMA_VERSION: Literal[1] = 1
EXTRACTION_METADATA_FILENAME = ".landscout-extraction.json"
MAX_REDIRECTS = 10

OFFICIAL_REFERENCE_PAGE_URL = (
    "https://www.patrinat.fr/fr/"
    "page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353"
)
OFFICIAL_ARCHIVE_URL = "https://assets.patrinat.fr/files/donnees/ep/EP.zip"
OFFICIAL_DATASET_NAME = "Base de référence des espaces protégés français"

CanonicalSha256 = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^[0-9a-f]{64}$"),
]
DeclaredVersion = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^(?:0[1-9]|1[0-2])/\d{4}$"),
]
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
StrictNonNegativeInt = Annotated[int, Field(strict=True, ge=0)]

_WINDOWS_RESERVED_BASENAMES = frozenset(
    {
        "con",
        "prn",
        "aux",
        "nul",
        "clock$",
        *(f"com{index}" for index in range(1, 10)),
        *(f"lpt{index}" for index in range(1, 10)),
    }
)
_REDIRECT_STATUSES = frozenset({301, 302, 303, 307, 308})


class InpnProtectedAreasSourceError(ValueError):
    """Raised when the pinned INPN source cannot be handled safely."""


class InpnProtectedAreasSourceConfig(BaseModel):
    """Strict identity of one reviewed PatriNat protected-areas snapshot."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: Literal["PatriNat"]
    authority: Literal["MNHN"]
    program: Literal["INPN"]
    dataset_id: Literal["EP"]
    dataset_name: Literal["Base de référence des espaces protégés français"]
    declared_version: DeclaredVersion
    reference_page_url: HttpUrl
    archive_url: HttpUrl
    archive_filename: Literal["EP.zip"]
    cache_root: Path

    @model_validator(mode="after")
    def _pinned_official_urls(self) -> Self:
        if str(self.reference_page_url) != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("reference_page_url must be the reviewed PatriNat page")
        if str(self.archive_url) != OFFICIAL_ARCHIVE_URL:
            raise ValueError("archive_url must be the reviewed official EP archive")
        return self


@dataclass(frozen=True)
class InpnProtectedAreasDownload:
    provider: str
    authority: str
    program: str
    dataset_id: str
    dataset_name: str
    declared_version: str
    reference_page_url: str
    archive_url: str
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool


@dataclass(frozen=True)
class InpnProtectedAreasExtractedFile:
    relative_path: str
    file_size: int
    sha256: str


@dataclass(frozen=True)
class InpnProtectedAreasExtraction:
    download: InpnProtectedAreasDownload
    extraction_path: Path
    files: tuple[InpnProtectedAreasExtractedFile, ...]
    cache_hit: bool


class _DownloadMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    provider: Literal["PatriNat"]
    authority: Literal["MNHN"]
    program: Literal["INPN"]
    dataset_id: Literal["EP"]
    dataset_name: Literal["Base de référence des espaces protégés français"]
    declared_version: DeclaredVersion
    reference_page_url: str
    archive_url: str
    filename: Literal["EP.zip"]
    download_timestamp: str
    file_size: StrictPositiveInt
    sha256: CanonicalSha256

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int or value != DOWNLOAD_METADATA_SCHEMA_VERSION:
            raise ValueError("Download metadata schema_version must be exact integer 1")
        return value

    @field_validator("reference_page_url")
    @classmethod
    def _exact_reference_page(cls, value: str) -> str:
        if value != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("Cached reference page identity differs")
        return value

    @field_validator("archive_url")
    @classmethod
    def _exact_archive_url(cls, value: str) -> str:
        if value != OFFICIAL_ARCHIVE_URL:
            raise ValueError("Cached archive URL identity differs")
        return value

    @field_validator("download_timestamp")
    @classmethod
    def _aware_utc_timestamp(cls, value: str) -> str:
        _validate_utc_timestamp(value)
        return value


class _ExtractedFileMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    relative_path: str
    file_size: StrictNonNegativeInt
    sha256: CanonicalSha256

    @field_validator("relative_path")
    @classmethod
    def _canonical_path(cls, value: str) -> str:
        _validate_inventory_relative_path(value)
        return value


class _ExtractionMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    archive_sha256: CanonicalSha256
    archive_size: StrictPositiveInt
    files: tuple[_ExtractedFileMetadata, ...] = Field(min_length=1)

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int or value != EXTRACTION_METADATA_SCHEMA_VERSION:
            raise ValueError("Extraction metadata schema_version must be exact integer 1")
        return value

    @field_validator("files")
    @classmethod
    def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
        paths = tuple(item.relative_path for item in value)
        if paths != tuple(sorted(paths)) or len(set(paths)) != len(paths):
            raise ValueError("Extraction inventory must be unique and lexically ordered")
        return value


@dataclass(frozen=True)
class _ValidatedZipMember:
    info: zipfile.ZipInfo
    destination: PurePosixPath
    is_directory: bool


def _validate_utc_timestamp(value: object) -> None:
    if type(value) is not str or not value or value != value.strip():
        raise ValueError("download_timestamp must be an exact non-empty string")
    parsed = datetime.fromisoformat(value)
    offset = parsed.utcoffset()
    if parsed.tzinfo is None or offset is None:
        raise ValueError("download_timestamp must be timezone-aware")
    if offset.total_seconds() != 0:
        raise ValueError("download_timestamp must use UTC")


def _validated_config(config: object) -> InpnProtectedAreasSourceConfig:
    if type(config) is not InpnProtectedAreasSourceConfig:
        raise InpnProtectedAreasSourceError(
            "config must be an exact InpnProtectedAreasSourceConfig"
        )
    try:
        return InpnProtectedAreasSourceConfig.model_validate(
            config.model_dump(mode="python")
        )
    except (AttributeError, TypeError, ValueError, ValidationError) as error:
        raise InpnProtectedAreasSourceError(
            "INPN protected-areas config is invalid"
        ) from error


def load_inpn_protected_areas_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> InpnProtectedAreasSourceConfig:
    """Load the explicit, version-pinned PatriNat EP source configuration."""

    if not isinstance(path, Path):
        raise InpnProtectedAreasSourceError("Config path must be a pathlib Path")
    try:
        with path.open(encoding="utf-8") as stream:
            payload = yaml.safe_load(stream)
        if type(payload) is not dict:
            raise ValueError("Expected a YAML mapping")
        return InpnProtectedAreasSourceConfig.model_validate(payload)
    except (OSError, TypeError, ValueError, ValidationError, yaml.YAMLError) as error:
        raise InpnProtectedAreasSourceError(
            f"Cannot load INPN protected-areas source config: {path}"
        ) from error


def _cache_directory(config: InpnProtectedAreasSourceConfig) -> Path:
    version = config.declared_version.replace("/", "-")
    return config.cache_root / config.dataset_id / version


def _archive_path(config: InpnProtectedAreasSourceConfig) -> Path:
    return _cache_directory(config) / config.archive_filename


def _metadata_path(archive_path: Path) -> Path:
    return archive_path.with_name(f"{archive_path.name}.metadata.json")


def _sha256_file(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True


def _is_regular_file(path: Path) -> bool:
    return not _is_link_or_junction(path) and path.is_file()


def _duplicate_rejecting_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _read_strict_json(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_duplicate_rejecting_object,
    )


def _windows_component_key(component: str) -> str:
    normalized = unicodedata.normalize("NFKC", component)
    if (
        not normalized
        or normalized in {".", ".."}
        or normalized != normalized.strip()
        or normalized.endswith((" ", "."))
        or any(ord(character) < 32 or ord(character) == 127 for character in normalized)
        or any(character in '<>:"/\\|?*' for character in normalized)
    ):
        raise InpnProtectedAreasSourceError(
            f"Unsafe Windows-compatible ZIP component: {component}"
        )
    stem = normalized.split(".", 1)[0].casefold()
    if stem in _WINDOWS_RESERVED_BASENAMES:
        raise InpnProtectedAreasSourceError(
            f"Reserved Windows device name in ZIP member: {component}"
        )
    return normalized.casefold()


def _canonical_member_destination(name: str) -> tuple[PurePosixPath, tuple[str, ...]]:
    if type(name) is not str or not name or "\x00" in name:
        raise InpnProtectedAreasSourceError("ZIP member name is empty or invalid")
    if any(ord(character) < 32 or ord(character) == 127 for character in name):
        raise InpnProtectedAreasSourceError("ZIP member name contains control characters")
    posix = PurePosixPath(name.replace("\\", "/"))
    windows = PureWindowsPath(name)
    if posix.is_absolute() or windows.is_absolute() or bool(windows.drive):
        raise InpnProtectedAreasSourceError(f"Absolute ZIP member path is unsafe: {name}")
    if ".." in posix.parts:
        raise InpnProtectedAreasSourceError(f"ZIP member traversal is unsafe: {name}")
    parts = tuple(part for part in posix.parts if part not in {"", "."})
    if not parts:
        raise InpnProtectedAreasSourceError("ZIP member has no normalized destination")
    canonical = tuple(_windows_component_key(part) for part in parts)
    if canonical[0] == EXTRACTION_METADATA_FILENAME.casefold():
        raise InpnProtectedAreasSourceError(
            "ZIP member collides with the extraction metadata path"
        )
    return PurePosixPath(*parts), canonical


def _validated_zip_members(path: Path) -> tuple[_ValidatedZipMember, ...]:
    if not _is_regular_file(path):
        raise InpnProtectedAreasSourceError(f"Archive is missing or unsafe: {path}")
    try:
        if path.stat().st_size <= 0 or not zipfile.is_zipfile(path):
            raise InpnProtectedAreasSourceError("Archive is empty or is not a ZIP")
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
            if not infos:
                raise InpnProtectedAreasSourceError("ZIP archive contains no members")
            raw_names: set[str] = set()
            explicit: dict[tuple[str, ...], str] = {}
            files: set[tuple[str, ...]] = set()
            directories: set[tuple[str, ...]] = set()
            validated: list[_ValidatedZipMember] = []
            regular_count = 0
            for info in infos:
                name = info.filename
                if name in raw_names:
                    raise InpnProtectedAreasSourceError(
                        f"duplicate ZIP member name: {name}"
                    )
                raw_names.add(name)
                if info.flag_bits & 0x1:
                    raise InpnProtectedAreasSourceError(
                        f"Encrypted ZIP members are unsupported: {name}"
                    )
                destination, canonical = _canonical_member_destination(name)
                mode = info.external_attr >> 16
                if stat.S_ISLNK(mode):
                    raise InpnProtectedAreasSourceError(
                        f"ZIP symbolic links are forbidden: {name}"
                    )
                file_type = stat.S_IFMT(mode)
                if file_type not in {0, stat.S_IFREG, stat.S_IFDIR}:
                    raise InpnProtectedAreasSourceError(
                        f"ZIP special files are forbidden: {name}"
                    )
                is_directory = (
                    info.is_dir()
                    or name.endswith(("/", "\\"))
                    or stat.S_ISDIR(mode)
                )
                if canonical in explicit:
                    raise InpnProtectedAreasSourceError(
                        "ZIP members collide at one normalized destination: "
                        f"{explicit[canonical]} / {name}"
                    )
                explicit[canonical] = name
                parents = tuple(canonical[:index] for index in range(1, len(canonical)))
                if any(parent in files for parent in parents):
                    raise InpnProtectedAreasSourceError(
                        f"colliding ZIP file/directory destination: {name}"
                    )
                if is_directory:
                    if canonical in files:
                        raise InpnProtectedAreasSourceError(
                            f"colliding ZIP file/directory destination: {name}"
                        )
                    directories.add(canonical)
                else:
                    if canonical in directories:
                        raise InpnProtectedAreasSourceError(
                            f"colliding ZIP file/directory destination: {name}"
                        )
                    files.add(canonical)
                    regular_count += 1
                directories.update(parents)
                validated.append(
                    _ValidatedZipMember(info, destination, is_directory)
                )
            if regular_count == 0:
                raise InpnProtectedAreasSourceError(
                    "ZIP archive contains no regular files"
                )
            bad_member = archive.testzip()
            if bad_member is not None:
                raise InpnProtectedAreasSourceError(
                    f"Corrupt ZIP member: {bad_member}"
                )
            return tuple(validated)
    except InpnProtectedAreasSourceError:
        raise
    except (
        NotImplementedError,
        OSError,
        RuntimeError,
        zipfile.BadZipFile,
        zipfile.LargeZipFile,
        zlib.error,
    ) as error:
        raise InpnProtectedAreasSourceError("Cannot validate ZIP archive") from error


def _download_metadata(
    config: InpnProtectedAreasSourceConfig,
    result: InpnProtectedAreasDownload,
) -> _DownloadMetadata:
    return _DownloadMetadata(
        schema_version=DOWNLOAD_METADATA_SCHEMA_VERSION,
        provider=config.provider,
        authority=config.authority,
        program=config.program,
        dataset_id=config.dataset_id,
        dataset_name=config.dataset_name,
        declared_version=config.declared_version,
        reference_page_url=str(config.reference_page_url),
        archive_url=str(config.archive_url),
        filename=config.archive_filename,
        download_timestamp=result.download_timestamp,
        file_size=result.file_size,
        sha256=result.sha256,
    )


def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload | None:
    if not _is_regular_file(archive_path) or not _is_regular_file(metadata_path):
        return None
    try:
        metadata = _DownloadMetadata.model_validate(_read_strict_json(metadata_path))
        expected = {
            "provider": config.provider,
            "authority": config.authority,
            "program": config.program,
            "dataset_id": config.dataset_id,
            "dataset_name": config.dataset_name,
            "declared_version": config.declared_version,
            "reference_page_url": str(config.reference_page_url),
            "archive_url": str(config.archive_url),
            "filename": config.archive_filename,
        }
        if any(getattr(metadata, key) != value for key, value in expected.items()):
            return None
        size = archive_path.stat().st_size
        checksum = _sha256_file(archive_path)
        if size != metadata.file_size or checksum != metadata.sha256:
            return None
        _validated_zip_members(archive_path)
        return InpnProtectedAreasDownload(
            provider=metadata.provider,
            authority=metadata.authority,
            program=metadata.program,
            dataset_id=metadata.dataset_id,
            dataset_name=metadata.dataset_name,
            declared_version=metadata.declared_version,
            reference_page_url=metadata.reference_page_url,
            archive_url=metadata.archive_url,
            download_timestamp=metadata.download_timestamp,
            filename=metadata.filename,
            file_size=metadata.file_size,
            sha256=metadata.sha256,
            path=archive_path,
            cache_hit=True,
        )
    except (
        InpnProtectedAreasSourceError,
        OSError,
        TypeError,
        ValueError,
        ValidationError,
        json.JSONDecodeError,
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
    if archive_backup.exists() or metadata_backup.exists():
        raise InpnProtectedAreasSourceError(
            "Cache recovery backup already exists; manual recovery is required"
        )
    archive_existed = archive_path.is_file()
    metadata_existed = metadata_path.is_file()
    try:
        if archive_existed:
            copy2(archive_path, archive_backup)
        if metadata_existed:
            copy2(metadata_path, metadata_backup)
    except OSError:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise

    try:
        _replace_file(temporary_archive, archive_path)
        _replace_file(temporary_metadata, metadata_path)
    except OSError as publication_error:
        try:
            if archive_existed:
                _replace_file(archive_backup, archive_path)
            else:
                archive_path.unlink(missing_ok=True)
            if metadata_existed:
                _replace_file(metadata_backup, metadata_path)
            else:
                metadata_path.unlink(missing_ok=True)
        except OSError as rollback_error:
            raise InpnProtectedAreasSourceError(
                "INPN cache publication and rollback both failed"
            ) from rollback_error
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise InpnProtectedAreasSourceError(
            "INPN cache publication failed"
        ) from publication_error
    else:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)


def _validate_destination_url(value: str) -> str:
    try:
        parsed = urlsplit(value)
        if parsed.scheme.casefold() != "https" or not parsed.hostname:
            raise ValueError("Remote URL must use HTTPS and have a hostname")
        if parsed.username is not None or parsed.password is not None:
            raise ValueError("Remote URL credentials are forbidden")
        hostname = parsed.hostname.rstrip(".").casefold()
        if hostname == "localhost" or hostname.endswith(".localhost"):
            raise ValueError("Localhost destinations are forbidden")
        address: ipaddress.IPv4Address | ipaddress.IPv6Address | None = None
        try:
            address = ipaddress.ip_address(hostname)
        except ValueError:
            try:
                address = ipaddress.ip_address(socket.inet_aton(hostname))
            except OSError:
                if hostname.isdecimal() or hostname.startswith("0x"):
                    base = 16 if hostname.startswith("0x") else 10
                    try:
                        numeric_address = int(hostname, base)
                        address = ipaddress.IPv4Address(numeric_address)
                    except (ValueError, ipaddress.AddressValueError):
                        address = None
        if address is not None and not address.is_global:
            raise ValueError("Private or local IP destinations are forbidden")
        return value
    except (AttributeError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            f"Unsafe download or redirect URL: {value}"
        ) from error


def _copy_response_bytes(response: Any, destination: Path) -> None:
    try:
        headers = getattr(response, "headers", None)
        header_get = getattr(headers, "get", None)
        if not callable(header_get):
            raise InpnProtectedAreasSourceError("HTTP response headers are invalid")
        content_type = str(header_get("Content-Type", ""))
        if "text/html" in content_type.casefold():
            raise InpnProtectedAreasSourceError("HTML response cannot be used as a ZIP")
        raw = getattr(response, "raw", None)
        with destination.open("xb") as output:
            if raw is not None and callable(getattr(raw, "read", None)):
                if hasattr(raw, "decode_content"):
                    raw.decode_content = False
                copyfileobj(raw, output, length=DOWNLOAD_CHUNK_SIZE)
                return
            iterator = getattr(response, "iter_content", None)
            if not callable(iterator):
                raise InpnProtectedAreasSourceError(
                    "HTTP response does not expose streaming bytes"
                )
            for chunk in iterator(chunk_size=DOWNLOAD_CHUNK_SIZE):
                if chunk:
                    output.write(chunk)
    except InpnProtectedAreasSourceError:
        raise
    except Exception as error:
        raise InpnProtectedAreasSourceError(
            "Official INPN archive response stream failed"
        ) from error


def _download_archive_bytes(
    session: Any,
    configured_url: str,
    timeout_seconds: float,
    destination: Path,
) -> None:
    current_url = _validate_destination_url(configured_url)
    seen = {current_url}
    for _ in range(MAX_REDIRECTS + 1):
        response: Any | None = None
        try:
            response = session.get(
                current_url,
                allow_redirects=False,
                stream=True,
                timeout=timeout_seconds,
            )
            history = getattr(response, "history", ())
            for prior in history:
                _validate_destination_url(str(getattr(prior, "url", "")))
            response_url = str(getattr(response, "url", current_url))
            _validate_destination_url(response_url)
            status_code = getattr(response, "status_code", None)
            if status_code in _REDIRECT_STATUSES:
                headers = getattr(response, "headers", {})
                location = headers.get("Location") if hasattr(headers, "get") else None
                if type(location) is not str or not location:
                    raise InpnProtectedAreasSourceError(
                        "HTTP redirect is missing a Location header"
                    )
                next_url = _validate_destination_url(urljoin(current_url, location))
                if next_url in seen:
                    raise InpnProtectedAreasSourceError("HTTP redirect loop detected")
                seen.add(next_url)
                current_url = next_url
                continue
            if type(status_code) is not int or not 200 <= status_code < 300:
                raise InpnProtectedAreasSourceError(
                    "Official INPN archive response was not HTTP success"
                )
            raise_for_status = getattr(response, "raise_for_status", None)
            if not callable(raise_for_status):
                raise InpnProtectedAreasSourceError(
                    "HTTP response cannot prove status success"
                )
            raise_for_status()
            _copy_response_bytes(response, destination)
            return
        except InpnProtectedAreasSourceError:
            raise
        except (
            AttributeError,
            OSError,
            TypeError,
            ValueError,
            requests.RequestException,
        ) as error:
            raise InpnProtectedAreasSourceError(
                "Official INPN archive download failed"
            ) from error
        finally:
            if response is not None:
                close = getattr(response, "close", None)
                if callable(close):
                    with suppress(Exception):
                        close()
    raise InpnProtectedAreasSourceError("Too many HTTP redirects")


def download_inpn_protected_areas_archive(
    config: InpnProtectedAreasSourceConfig,
    *,
    session: requests.Session | None = None,
    timeout_seconds: float = 120.0,
) -> InpnProtectedAreasDownload:
    """Download or reuse the exact configured official EP ZIP bytes."""

    validated_config = _validated_config(config)
    if isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, Real):
        raise InpnProtectedAreasSourceError(
            "timeout_seconds must be a strict finite positive number"
        )
    try:
        validated_timeout = float(timeout_seconds)
    except (OverflowError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            "timeout_seconds must be a strict finite positive number"
        ) from error
    if not isfinite(validated_timeout) or validated_timeout <= 0:
        raise InpnProtectedAreasSourceError(
            "timeout_seconds must be a strict finite positive number"
        )
    if session is not None and not callable(getattr(session, "get", None)):
        raise InpnProtectedAreasSourceError("session must provide an HTTP get method")

    archive_path = _archive_path(validated_config)
    metadata_path = _metadata_path(archive_path)
    cached = _load_cached_download(
        archive_path, metadata_path, validated_config
    )
    if cached is not None:
        return cached

    temporary_archive = archive_path.with_name(f"{archive_path.name}.part")
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    owned_session = session is None
    http_session: Any | None = session
    try:
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_archive.unlink(missing_ok=True)
        temporary_metadata.unlink(missing_ok=True)
        if http_session is None:
            http_session = requests.Session()
        _download_archive_bytes(
            http_session,
            str(validated_config.archive_url),
            validated_timeout,
            temporary_archive,
        )
        _validated_zip_members(temporary_archive)
        file_size = temporary_archive.stat().st_size
        checksum = _sha256_file(temporary_archive)
        result = InpnProtectedAreasDownload(
            provider=validated_config.provider,
            authority=validated_config.authority,
            program=validated_config.program,
            dataset_id=validated_config.dataset_id,
            dataset_name=validated_config.dataset_name,
            declared_version=validated_config.declared_version,
            reference_page_url=str(validated_config.reference_page_url),
            archive_url=str(validated_config.archive_url),
            download_timestamp=datetime.now(UTC).isoformat(),
            filename=validated_config.archive_filename,
            file_size=file_size,
            sha256=checksum,
            path=archive_path,
            cache_hit=False,
        )
        metadata = _download_metadata(validated_config, result)
        temporary_metadata.write_text(
            metadata.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        _publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )
        return result
    except InpnProtectedAreasSourceError:
        raise
    except (OSError, TypeError, ValueError, ValidationError) as error:
        raise InpnProtectedAreasSourceError(
            "Official INPN archive download or cache publication failed"
        ) from error
    finally:
        for temporary_path in (temporary_archive, temporary_metadata):
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass
        if owned_session and http_session is not None:
            close = getattr(http_session, "close", None)
            if callable(close):
                with suppress(Exception):
                    close()


def _validate_download(
    download: object,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload:
    if type(download) is not InpnProtectedAreasDownload:
        raise InpnProtectedAreasSourceError(
            "download must be an exact InpnProtectedAreasDownload"
        )
    expected = {
        "provider": config.provider,
        "authority": config.authority,
        "program": config.program,
        "dataset_id": config.dataset_id,
        "dataset_name": config.dataset_name,
        "declared_version": config.declared_version,
        "reference_page_url": str(config.reference_page_url),
        "archive_url": str(config.archive_url),
        "filename": config.archive_filename,
    }
    try:
        if any(getattr(download, key) != value for key, value in expected.items()):
            raise ValueError("Download lineage differs from config")
        if not isinstance(download.path, Path) or download.path != _archive_path(config):
            raise ValueError("Download path differs from configured cache identity")
        if type(download.cache_hit) is not bool:
            raise ValueError("Download cache_hit must be boolean")
        if (
            type(download.file_size) is not int
            or download.file_size <= 0
            or type(download.sha256) is not str
            or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
        ):
            raise ValueError("Download integrity scalars are invalid")
        _validate_utc_timestamp(download.download_timestamp)
        if not _is_regular_file(download.path):
            raise ValueError("Downloaded archive path is missing or unsafe")
        if download.path.stat().st_size != download.file_size:
            raise ValueError("Downloaded archive size changed")
        if _sha256_file(download.path) != download.sha256:
            raise ValueError("Downloaded archive SHA256 changed")
        _validated_zip_members(download.path)
        return download
    except InpnProtectedAreasSourceError:
        raise
    except (AttributeError, OSError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            "INPN protected-areas download is stale or invalid"
        ) from error


def _validate_inventory_relative_path(value: object) -> None:
    if type(value) is not str or not value or value != value.strip():
        raise ValueError("Inventory relative_path must be an exact non-empty string")
    destination, _ = _canonical_member_destination(value)
    if destination.as_posix() != value or value == EXTRACTION_METADATA_FILENAME:
        raise ValueError("Inventory relative_path is not canonical POSIX form")


def _inventory(root: Path) -> tuple[InpnProtectedAreasExtractedFile, ...]:
    if _is_link_or_junction(root) or not root.is_dir():
        raise InpnProtectedAreasSourceError(
            "Extraction root must be a regular directory"
        )
    files: list[InpnProtectedAreasExtractedFile] = []
    for path in root.rglob("*"):
        if _is_link_or_junction(path):
            raise InpnProtectedAreasSourceError(
                f"Extracted link or junction is forbidden: {path}"
            )
        if path.is_dir():
            continue
        if not path.is_file():
            raise InpnProtectedAreasSourceError(
                f"Extracted special filesystem entry is forbidden: {path}"
            )
        relative_path = path.relative_to(root).as_posix()
        if relative_path == EXTRACTION_METADATA_FILENAME:
            continue
        try:
            _validate_inventory_relative_path(relative_path)
            file_size = path.stat().st_size
            checksum = _sha256_file(path)
        except (OSError, ValueError) as error:
            raise InpnProtectedAreasSourceError(
                f"Cannot inventory extracted file: {relative_path}"
            ) from error
        files.append(
            InpnProtectedAreasExtractedFile(
                relative_path=relative_path,
                file_size=file_size,
                sha256=checksum,
            )
        )
    files.sort(key=lambda item: item.relative_path)
    if not files:
        raise InpnProtectedAreasSourceError(
            "Extracted INPN archive contains no regular files"
        )
    return tuple(files)


def _extraction_metadata(
    download: InpnProtectedAreasDownload,
    files: tuple[InpnProtectedAreasExtractedFile, ...],
) -> _ExtractionMetadata:
    return _ExtractionMetadata(
        schema_version=EXTRACTION_METADATA_SCHEMA_VERSION,
        archive_sha256=download.sha256,
        archive_size=download.file_size,
        files=tuple(
            _ExtractedFileMetadata(
                relative_path=item.relative_path,
                file_size=item.file_size,
                sha256=item.sha256,
            )
            for item in files
        ),
    )


def _validate_extraction_cache(
    root: Path,
    download: InpnProtectedAreasDownload,
) -> tuple[InpnProtectedAreasExtractedFile, ...]:
    marker = root / EXTRACTION_METADATA_FILENAME
    if not _is_regular_file(marker):
        raise InpnProtectedAreasSourceError(
            "Extraction integrity metadata is missing or unsafe"
        )
    try:
        metadata = _ExtractionMetadata.model_validate(_read_strict_json(marker))
        if (
            metadata.archive_sha256 != download.sha256
            or metadata.archive_size != download.file_size
        ):
            raise ValueError("Extraction metadata archive lineage differs")
        expected = tuple(
            InpnProtectedAreasExtractedFile(
                relative_path=item.relative_path,
                file_size=item.file_size,
                sha256=item.sha256,
            )
            for item in metadata.files
        )
        actual = _inventory(root)
        if actual != expected:
            raise ValueError("Extraction files differ from integrity metadata")
        return actual
    except InpnProtectedAreasSourceError:
        raise
    except (
        OSError,
        TypeError,
        ValueError,
        ValidationError,
        json.JSONDecodeError,
    ) as error:
        raise InpnProtectedAreasSourceError(
            "Extraction cache failed physical integrity validation"
        ) from error


def _path_exists(path: Path) -> bool:
    return path.exists() or path.is_symlink() or _is_link_or_junction(path)


def _remove_path(path: Path) -> None:
    if path.is_junction():
        path.rmdir()
    elif path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.exists():
        shutil.rmtree(path)


def _replace_directory(source: Path, target: Path) -> None:
    source.replace(target)


def _publish_extraction_directory(temporary_root: Path, root: Path) -> None:
    backup = root.with_name(f"{root.name}.bak")
    if _path_exists(backup):
        raise InpnProtectedAreasSourceError(
            "Extraction recovery backup already exists; manual recovery is required"
        )
    old_moved = False
    if _path_exists(root):
        try:
            _replace_directory(root, backup)
        except OSError as staging_error:
            raise InpnProtectedAreasSourceError(
                "Cannot stage existing INPN extraction for publication"
            ) from staging_error
        old_moved = True
    try:
        _replace_directory(temporary_root, root)
    except OSError as publication_error:
        try:
            _remove_path(root)
            if old_moved:
                _replace_directory(backup, root)
        except OSError as rollback_error:
            raise InpnProtectedAreasSourceError(
                "INPN extraction publication and rollback both failed"
            ) from rollback_error
        raise InpnProtectedAreasSourceError(
            "INPN extraction publication failed"
        ) from publication_error
    else:
        _remove_path(backup)


def extract_inpn_protected_areas_archive(
    download: InpnProtectedAreasDownload,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasExtraction:
    """Safely extract all regular files and bind an exact factual inventory."""

    validated_config = _validated_config(config)
    validated_download = _validate_download(download, validated_config)
    root = validated_download.path.parent / "x" / validated_download.sha256
    if root.is_dir() and not _is_link_or_junction(root):
        try:
            files = _validate_extraction_cache(root, validated_download)
            return InpnProtectedAreasExtraction(
                download=validated_download,
                extraction_path=root,
                files=files,
                cache_hit=True,
            )
        except (InpnProtectedAreasSourceError, OSError):
            pass

    temporary_root = root.with_name(f"{root.name}.part")
    try:
        root.parent.mkdir(parents=True, exist_ok=True)
        _remove_path(temporary_root)
        temporary_root.mkdir(parents=True)
        with zipfile.ZipFile(validated_download.path) as archive:
            members = _validated_zip_members(validated_download.path)
            for member in members:
                target = temporary_root.joinpath(*member.destination.parts)
                if member.is_directory:
                    target.mkdir(parents=True, exist_ok=True)
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(member.info) as source, target.open("xb") as output:
                    copyfileobj(source, output, length=DOWNLOAD_CHUNK_SIZE)
        files = _inventory(temporary_root)
        _validate_download(validated_download, validated_config)
        metadata = _extraction_metadata(validated_download, files)
        (temporary_root / EXTRACTION_METADATA_FILENAME).write_text(
            metadata.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        files = _validate_extraction_cache(temporary_root, validated_download)
        _publish_extraction_directory(temporary_root, root)
        return InpnProtectedAreasExtraction(
            download=validated_download,
            extraction_path=root,
            files=files,
            cache_hit=False,
        )
    except InpnProtectedAreasSourceError:
        raise
    except (
        NotImplementedError,
        OSError,
        RuntimeError,
        ValueError,
        zipfile.BadZipFile,
        zlib.error,
    ) as error:
        raise InpnProtectedAreasSourceError(
            "Cannot safely extract the INPN protected-areas archive"
        ) from error
    finally:
        try:
            _remove_path(temporary_root)
        except OSError:
            pass


__all__ = [
    "InpnProtectedAreasDownload",
    "InpnProtectedAreasExtractedFile",
    "InpnProtectedAreasExtraction",
    "InpnProtectedAreasSourceConfig",
    "InpnProtectedAreasSourceError",
    "download_inpn_protected_areas_archive",
    "extract_inpn_protected_areas_archive",
    "load_inpn_protected_areas_source_config",
]
