import gzip
import json
import re
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path
from shutil import copyfileobj
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

CADASTRE_BASE_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes"
)
DEFAULT_CACHE_DIR = Path("data/cache/cadastre")
VALIDATION_CHUNK_SIZE = 1024 * 1024


class CadastreDownloadError(RuntimeError):
    """Raised when a cadastre archive cannot be downloaded safely."""


@dataclass(frozen=True)
class CadastreDownload:
    source_url: str
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool


def _department_code(commune_code: str) -> str:
    return commune_code[:3] if commune_code.startswith(("97", "98")) else commune_code[:2]


def build_cadastre_parcelles_url(commune_code: str) -> str:
    normalized = commune_code.strip().upper()
    if re.fullmatch(r"[0-9A-Z]{5}", normalized) is None:
        raise ValueError("Commune code must contain exactly 5 letters or digits")
    department = _department_code(normalized)
    filename = f"cadastre-{normalized}-parcelles.json.gz"
    return f"{CADASTRE_BASE_URL}/{department}/{normalized}/{filename}"


def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _is_valid_gzip(path: Path) -> bool:
    try:
        if not path.is_file() or path.stat().st_size == 0:
            return False
        with gzip.open(path, "rb") as stream:
            while stream.read(VALIDATION_CHUNK_SIZE):
                pass
        return True
    except (EOFError, OSError):
        return False


def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    source_url: str,
    max_cache_age_hours: float,
) -> CadastreDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        file_size = archive_path.stat().st_size
        checksum = _sha256(archive_path)
        download_timestamp = str(metadata["download_timestamp"])
        downloaded_at = datetime.fromisoformat(download_timestamp)
        if downloaded_at.tzinfo is None:
            return None
        age_seconds = (
            datetime.now(UTC) - downloaded_at.astimezone(UTC)
        ).total_seconds()
        valid = (
            file_size > 0
            and 0 <= age_seconds <= max_cache_age_hours * 3600
            and _is_valid_gzip(archive_path)
            and metadata["source_url"] == source_url
            and metadata["filename"] == archive_path.name
            and metadata["file_size"] == file_size
            and metadata["sha256"] == checksum
        )
        if not valid:
            return None
        return CadastreDownload(
            source_url=source_url,
            download_timestamp=download_timestamp,
            filename=archive_path.name,
            file_size=file_size,
            sha256=checksum,
            path=archive_path,
            cache_hit=True,
        )
    except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
        return None


def download_cadastre_parcelles(
    commune_code: str,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
    max_cache_age_hours: float = 168.0,
) -> CadastreDownload:
    if max_cache_age_hours < 0:
        raise ValueError("max_cache_age_hours must be non-negative")
    source_url = build_cadastre_parcelles_url(commune_code)
    filename = source_url.rsplit("/", maxsplit=1)[-1]
    archive_path = cache_dir / filename
    metadata_path = cache_dir / f"{filename}.metadata.json"
    cached = _load_cached_download(
        archive_path, metadata_path, source_url, max_cache_age_hours
    )
    if cached is not None:
        return cached

    cache_dir.mkdir(parents=True, exist_ok=True)
    temporary_archive = archive_path.with_suffix(f"{archive_path.suffix}.part")
    request = Request(source_url, headers={"User-Agent": "LandScout-AI/0.1"})
    try:
        with (
            urlopen(request, timeout=timeout) as response,
            temporary_archive.open("wb") as output,
        ):
            copyfileobj(response, output)
        if not _is_valid_gzip(temporary_archive):
            raise CadastreDownloadError("Downloaded cadastre archive is not valid gzip")
        temporary_archive.replace(archive_path)
    except (HTTPError, URLError, OSError) as error:
        temporary_archive.unlink(missing_ok=True)
        raise CadastreDownloadError(f"Cadastre download failed: {source_url}") from error
    except CadastreDownloadError:
        temporary_archive.unlink(missing_ok=True)
        raise

    result = CadastreDownload(
        source_url=source_url,
        download_timestamp=datetime.now(UTC).isoformat(),
        filename=filename,
        file_size=archive_path.stat().st_size,
        sha256=_sha256(archive_path),
        path=archive_path,
        cache_hit=False,
    )
    metadata = asdict(result)
    metadata.pop("path")
    metadata.pop("cache_hit")
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    temporary_metadata.write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary_metadata.replace(metadata_path)
    return result
