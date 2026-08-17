# `src/landscout/sources/cadastre_fr.py`

## File identity

- Repository path: `src/landscout/sources/cadastre_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: cadastre
- Responsibility: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.
- Source SHA256: `cd615e3db3acc3d4fb1a1dd44afe738fd8d58062972ac4d24c8c71a47f0255e6`

## 1. Purpose

Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

## 2. Position in LandScout architecture

This file belongs to the **source adapter** layer and the **cadastre** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import gzip`
- `import json`
- `import re`
- `import sys`
- `from dataclasses import asdict, dataclass`
- `from datetime import UTC, datetime`
- `from hashlib import sha256`
- `from math import isfinite`
- `from numbers import Real`
- `from pathlib import Path`
- `from shutil import copy2, copyfileobj`
- `from urllib.error import HTTPError, URLError`

### Third-party packages

- `None.`

### Internal LandScout imports

- `from landscout.common.safe_http import open_safe_https`

## 4. Contract taxonomy

### A. Python constants

#### `CADASTRE_BASE_URL`

```python
CADASTRE_BASE_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes"
)
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes. Consumers include `src/landscout/sources/cadastre_fr.py::build_cadastre_parcelles_url` (value reference).

#### `DEFAULT_CACHE_DIR`

```python
DEFAULT_CACHE_DIR = Path("data/cache/cadastre")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `VALIDATION_CHUNK_SIZE`

```python
VALIDATION_CHUNK_SIZE = 1024 * 1024
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/sources/cadastre_fr.py::_is_valid_gzip` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `CadastreDownloadError`

**Purpose:** Raised when a cadastre archive cannot be downloaded safely.

**Kind:** controlled exception.

**Inheritance:** `RuntimeError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`.
- import: `tests/unit/test_cadastre_fr.py::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`.
- constructor call: `src/landscout/sources/cadastre_fr.py::_require_no_cache_recovery_material` via `CadastreDownloadError`.
- constructor call: `src/landscout/sources/cadastre_fr.py::_prepare_temporary_cache_file` via `CadastreDownloadError`.
- constructor call: `src/landscout/sources/cadastre_fr.py::_cleanup_temporary_cache_files` via `CadastreDownloadError`.
- constructor call: `src/landscout/sources/cadastre_fr.py::_publish_cache_pair` via `CadastreDownloadError`.
- constructor call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `CadastreDownloadError`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_failed_refresh_preserves_cached_archive` via `pytest.raises(CadastreDownloadError)`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_failed_http_response` via `pytest.raises(CadastreDownloadError)`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_corrupted_new_download_preserves_existing_archive` via `pytest.raises(CadastreDownloadError)`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `pytest.raises(CadastreDownloadError, match='publication')`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_first_metadata_publication_failure_leaves_no_half_pair` via `pytest.raises(CadastreDownloadError, match='publication')`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` via `pytest.raises(CadastreDownloadError, match='rollback')`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes` via `pytest.raises(CadastreDownloadError, match='backup|recovery|manual')`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `pytest.raises(CadastreDownloadError, match='rollback')`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `pytest.raises(CadastreDownloadError, match='backup|recovery|manual')`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `pytest.raises(CadastreDownloadError, match='temporary|link|cache')`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `pytest.raises(CadastreDownloadError, match='backup|recovery|manual')`.
- expected exception type: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `pytest.raises(CadastreDownloadError, match='rollback')`.

**Exact class source**

```python
class CadastreDownloadError(RuntimeError):
    """Raised when a cadastre archive cannot be downloaded safely."""
```

### `CadastreDownload`

**Purpose:** Immutable envelope for one downloaded cadastral gzip: configured URL, physical path, filename, size, SHA256, timestamp, and cache status.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `source_url` | `source_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `download_timestamp` | `download_timestamp: str` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `filename` | `filename: str` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `file_size` | `file_size: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `path` | `path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `cache_hit` | `cache_hit: bool` | True only when already verified local cache state was reused. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`.
- import: `src/landscout/sources/cadastre_loader_fr.py::<module>` via `from landscout.sources.cadastre_fr import CadastreDownload`.
- import: `tests/unit/test_cadastre_loader_fr.py::<module>` via `from landscout.sources.cadastre_fr import CadastreDownload`.
- type annotation: `src/landscout/sources/cadastre_fr.py::_load_cached_download` via `CadastreDownload`.
- constructor call: `src/landscout/sources/cadastre_fr.py::_load_cached_download` via `CadastreDownload`.
- type annotation: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `CadastreDownload`.
- constructor call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `CadastreDownload`.
- type annotation: `src/landscout/sources/cadastre_loader_fr.py::_validate_download` via `CadastreDownload`.
- type annotation: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `CadastreDownload`.
- type annotation: `tests/unit/test_cadastre_loader_fr.py::_download` via `CadastreDownload`.
- constructor call: `tests/unit/test_cadastre_loader_fr.py::_download` via `CadastreDownload`.

**Exact class source**

```python
class CadastreDownload:
    source_url: str
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool
```


## 6. Functions and methods

### `_department_code`

**Exact signature**

```python
def _department_code(commune_code: str) -> str:
```

**Purpose**

Private `cadastre` helper for department code; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
commune_code[:3] if commune_code.startswith(('97', '98')) else commune_code[:2]
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::build_cadastre_parcelles_url` via `_department_code`.

**Complete source-ordered implementation**

```python
def _department_code(commune_code: str) -> str:
    return commune_code[:3] if commune_code.startswith(("97", "98")) else commune_code[:2]
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `build_cadastre_parcelles_url`

**Exact signature**

```python
def build_cadastre_parcelles_url(commune_code: str) -> str:
```

**Purpose**

Constructs cadastre parcelles url; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
f'{CADASTRE_BASE_URL}/{department}/{commune_code}/{filename}'
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(commune_code, str)`.
- Guard with a raise path: `re.fullmatch('(?:\\d{5}|2[AB]\\d{3})', commune_code) is None`.
- Explicit raise expressions: `TypeError('Commune code must be an exact string')`, `ValueError('Commune code must be a canonical French INSEE code')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`.
- import: `tests/unit/test_cadastre_fr.py::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`.
- direct call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `build_cadastre_parcelles_url`.
- direct call: `tests/unit/test_cadastre_fr.py::test_build_cadastre_parcelles_url` via `build_cadastre_parcelles_url`.
- direct call: `tests/unit/test_cadastre_fr.py::test_corsica_cadastre_urls_are_canonical` via `build_cadastre_parcelles_url`.
- direct call: `tests/unit/test_cadastre_fr.py::test_noncanonical_commune_code_is_controlled` via `build_cadastre_parcelles_url`.

**Complete source-ordered implementation**

```python
def build_cadastre_parcelles_url(commune_code: str) -> str:
    if not isinstance(commune_code, str):
        raise TypeError("Commune code must be an exact string")
    if re.fullmatch(r"(?:\d{5}|2[AB]\d{3})", commune_code) is None:
        raise ValueError("Commune code must be a canonical French INSEE code")
    department = _department_code(commune_code)
    filename = f"cadastre-{commune_code}-parcelles.json.gz"
    return f"{CADASTRE_BASE_URL}/{department}/{commune_code}/{filename}"
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_sha256`

**Exact signature**

```python
def _sha256(path: Path) -> str:
```

**Purpose**

Private `cadastre` helper for sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
digest.hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.open`, `stream.read`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `digest.hexdigest`, `sha256`.
- Environment/process effects: none.
- In-memory mutation: `digest`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::_load_cached_download` via `_sha256`.
- direct call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_sha256`.

**Complete source-ordered implementation**

```python
def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_is_valid_gzip`

**Exact signature**

```python
def _is_valid_gzip(path: Path) -> bool:
```

**Purpose**

Tests whether valid gzip; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
True

False

False
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `gzip.open`, `path.is_file`, `path.stat`, `stream.read`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `tests/unit/test_cadastre_fr.py::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`.
- direct call: `src/landscout/sources/cadastre_fr.py::_load_cached_download` via `_is_valid_gzip`.
- direct call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_is_valid_gzip`.
- direct call: `tests/unit/test_cadastre_fr.py::test_valid_gzip_is_accepted` via `_is_valid_gzip`.
- direct call: `tests/unit/test_cadastre_fr.py::test_truncated_gzip_is_rejected` via `_is_valid_gzip`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_load_cached_download`

**Exact signature**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    source_url: str,
    max_cache_age_hours: float,
) -> CadastreDownload | None:
```

**Purpose**

Reads and validates cached download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CadastreDownload | None`.
- Every observed return expression is reproduced without truncation:
```python
None

CadastreDownload(source_url=source_url, download_timestamp=download_timestamp, filename=archive_path.name, file_size=file_size, sha256=checksum, path=archive_path, cache_hit=True)

None

None

None

None

None
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `archive_path.is_file`, `archive_path.stat`, `metadata_path.is_file`, `metadata_path.read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_load_cached_download`.

**Complete source-ordered implementation**

```python
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
        if not isinstance(metadata, dict):
            return None
        file_size = archive_path.stat().st_size
        checksum = _sha256(archive_path)
        download_timestamp = metadata["download_timestamp"]
        if not isinstance(download_timestamp, str):
            return None
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
            and type(metadata["source_url"]) is str
            and metadata["source_url"] == source_url
            and type(metadata["filename"]) is str
            and metadata["filename"] == archive_path.name
            and type(metadata["file_size"]) is int
            and metadata["file_size"] > 0
            and metadata["file_size"] == file_size
            and type(metadata["sha256"]) is str
            and re.fullmatch(r"[0-9a-f]{64}", metadata["sha256"]) is not None
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
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_replace_file`

**Exact signature**

```python
def _replace_file(source: Path, target: Path) -> None:
```

**Purpose**

Private `cadastre` helper for replace file; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::_publish_cache_pair` via `_replace_file`.

**Complete source-ordered implementation**

```python
def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_is_link_or_junction`

**Exact signature**

```python
def _is_link_or_junction(path: Path) -> bool:
```

**Purpose**

Tests whether link or junction; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
path.is_symlink() or path.is_junction()

True
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::_require_no_cache_recovery_material` via `_is_link_or_junction`.
- direct call: `src/landscout/sources/cadastre_fr.py::_prepare_temporary_cache_file` via `_is_link_or_junction`.

**Complete source-ordered implementation**

```python
def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_cache_recovery_paths`

**Exact signature**

```python
def _cache_recovery_paths(
    archive_path: Path,
    metadata_path: Path,
) -> tuple[Path, Path]:
```

**Purpose**

Private `cadastre` helper for cache recovery paths; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[Path, Path]`.
- Every observed return expression is reproduced without truncation:
```python
(archive_path.with_suffix(f'{archive_path.suffix}.bak'), metadata_path.with_suffix(f'{metadata_path.suffix}.bak'))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::_require_no_cache_recovery_material` via `_cache_recovery_paths`.
- direct call: `src/landscout/sources/cadastre_fr.py::_publish_cache_pair` via `_cache_recovery_paths`.

**Complete source-ordered implementation**

```python
def _cache_recovery_paths(
    archive_path: Path,
    metadata_path: Path,
) -> tuple[Path, Path]:
    return (
        archive_path.with_suffix(f"{archive_path.suffix}.bak"),
        metadata_path.with_suffix(f"{metadata_path.suffix}.bak"),
    )
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_require_no_cache_recovery_material`

**Exact signature**

```python
def _require_no_cache_recovery_material(
    archive_path: Path,
    metadata_path: Path,
) -> None:
```

**Purpose**

Private `cadastre` helper for require no cache recovery material; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `any((path.exists() or _is_link_or_junction(path) for path in _cache_recovery_paths(archive_path, metadata_path)))`.
- Explicit raise expressions: `CadastreDownloadError('Cadastre cache recovery backup already exists; manual recovery is required')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.exists`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::_publish_cache_pair` via `_require_no_cache_recovery_material`.
- direct call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_require_no_cache_recovery_material`.

**Complete source-ordered implementation**

```python
def _require_no_cache_recovery_material(
    archive_path: Path,
    metadata_path: Path,
) -> None:
    if any(
        path.exists() or _is_link_or_junction(path)
        for path in _cache_recovery_paths(archive_path, metadata_path)
    ):
        raise CadastreDownloadError(
            "Cadastre cache recovery backup already exists; manual recovery is required"
        )
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_prepare_temporary_cache_file`

**Exact signature**

```python
def _prepare_temporary_cache_file(path: Path) -> None:
```

**Purpose**

Private `cadastre` helper for prepare temporary cache file; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `_is_link_or_junction(path)`.
- Guard with a raise path: `path.exists()`.
- Guard with a raise path: `not path.is_file()`.
- Explicit raise expressions: `CadastreDownloadError('Cadastre cache temporary path cannot be prepared safely')`, `CadastreDownloadError('Cadastre cache temporary path is a link or junction')`, `CadastreDownloadError('Cadastre cache temporary path is not a regular file')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.exists`, `path.is_file`.
- Filesystem write: `path.unlink`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_prepare_temporary_cache_file`.

**Complete source-ordered implementation**

```python
def _prepare_temporary_cache_file(path: Path) -> None:
    try:
        if _is_link_or_junction(path):
            raise CadastreDownloadError(
                "Cadastre cache temporary path is a link or junction"
            )
        if path.exists():
            if not path.is_file():
                raise CadastreDownloadError(
                    "Cadastre cache temporary path is not a regular file"
                )
            path.unlink()
    except CadastreDownloadError:
        raise
    except OSError as error:
        raise CadastreDownloadError(
            "Cadastre cache temporary path cannot be prepared safely"
        ) from error
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_cleanup_temporary_cache_files`

**Exact signature**

```python
def _cleanup_temporary_cache_files(
    paths: tuple[Path, ...],
    primary_error: BaseException | None,
) -> None:
```

**Purpose**

Private `cadastre` helper for cleanup temporary cache files; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `cleanup_error is not None and primary_error is None`.
- Explicit raise expressions: `CadastreDownloadError('Cadastre cache temporary files could not be cleaned safely')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.unlink`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_cleanup_temporary_cache_files`.

**Complete source-ordered implementation**

```python
def _cleanup_temporary_cache_files(
    paths: tuple[Path, ...],
    primary_error: BaseException | None,
) -> None:
    cleanup_error: OSError | None = None
    for path in paths:
        try:
            path.unlink(missing_ok=True)
        except OSError as error:
            cleanup_error = cleanup_error or error
    if cleanup_error is not None and primary_error is None:
        raise CadastreDownloadError(
            "Cadastre cache temporary files could not be cleaned safely"
        ) from cleanup_error
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_publish_cache_pair`

**Exact signature**

```python
def _publish_cache_pair(
    temporary_archive: Path,
    temporary_metadata: Path,
    archive_path: Path,
    metadata_path: Path,
) -> None:
```

**Purpose**

Private `cadastre` helper for publish cache pair; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `CadastreDownloadError('Cadastre cache publication and rollback both failed')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `archive_path.is_file`, `metadata_path.is_file`.
- Filesystem write: `archive_backup.unlink`, `archive_path.unlink`, `metadata_backup.unlink`, `metadata_path.unlink`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_publish_cache_pair`.

**Complete source-ordered implementation**

```python
def _publish_cache_pair(
    temporary_archive: Path,
    temporary_metadata: Path,
    archive_path: Path,
    metadata_path: Path,
) -> None:
    archive_backup, metadata_backup = _cache_recovery_paths(
        archive_path,
        metadata_path,
    )
    archive_existed = archive_path.is_file()
    metadata_existed = metadata_path.is_file()
    _require_no_cache_recovery_material(archive_path, metadata_path)
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
    except OSError:
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
            # Do not remove remaining backups: they are recovery material.
            raise CadastreDownloadError(
                "Cadastre cache publication and rollback both failed"
            ) from rollback_error
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise
    else:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `download_cadastre_parcelles`

**Exact signature**

```python
def download_cadastre_parcelles(
    commune_code: str,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
    max_cache_age_hours: float = 168.0,
) -> CadastreDownload:
```

**Purpose**

Acquires, verifies, and records cadastre parcelles; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CadastreDownload`.
- Every observed return expression is reproduced without truncation:
```python
cached

result
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(timeout, bool) or not isinstance(timeout, Real) or (not isfinite(float(timeout))) or (timeout <= 0)`.
- Guard with a raise path: `isinstance(max_cache_age_hours, bool) or not isinstance(max_cache_age_hours, Real) or (not isfinite(float(max_cache_age_hours))) or (max_cache_age_hours < 0)`.
- Guard with a raise path: `not _is_valid_gzip(temporary_archive)`.
- Explicit raise expressions: `CadastreDownloadError('Cadastre cache paths cannot be prepared safely')`, `CadastreDownloadError('Downloaded cadastre archive is not valid gzip')`, `CadastreDownloadError(f'Cadastre cache publication failed: {source_url}')`, `CadastreDownloadError(f'Cadastre download failed: {source_url}')`, `ValueError('max_cache_age_hours must be non-negative')`, `ValueError('timeout must be a strict finite positive number')`, `re-raise`.

**Side effects**

- Network I/O: `open_safe_https`.
- Filesystem read: `temporary_archive.open`, `temporary_archive.stat`, `temporary_metadata.open`.
- Filesystem write: `cache_dir.mkdir`, `copyfileobj`.
- CRS/geometry calculation: none.
- Hashing: `_sha256`.
- Environment/process effects: none.
- In-memory mutation: `metadata`.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`.
- import: `tests/unit/test_cadastre_fr.py::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`.
- direct call: `tests/unit/test_cadastre_fr.py::test_successful_download` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_fresh_cache_is_reused` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_expired_cache_is_downloaded_again` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_failed_refresh_preserves_cached_archive` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_failed_http_response` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_checksum_generation` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_corrupted_cached_archive_triggers_fresh_download` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_corrupted_new_download_preserves_existing_archive` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_download_timeout_is_strict_finite_positive` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_cache_age_is_strict_finite_nonnegative` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_malformed_cached_metadata_triggers_refresh` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_future_cached_timestamp_triggers_refresh` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_first_metadata_publication_failure_leaves_no_half_pair` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `download_cadastre_parcelles`.
- direct call: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_cadastre_parcelles`.

**Complete source-ordered implementation**

```python
def download_cadastre_parcelles(
    commune_code: str,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
    max_cache_age_hours: float = 168.0,
) -> CadastreDownload:
    if (
        isinstance(timeout, bool)
        or not isinstance(timeout, Real)
        or not isfinite(float(timeout))
        or timeout <= 0
    ):
        raise ValueError("timeout must be a strict finite positive number")
    if (
        isinstance(max_cache_age_hours, bool)
        or not isinstance(max_cache_age_hours, Real)
        or not isfinite(float(max_cache_age_hours))
        or max_cache_age_hours < 0
    ):
        raise ValueError("max_cache_age_hours must be non-negative")
    source_url = build_cadastre_parcelles_url(commune_code)
    filename = source_url.rsplit("/", maxsplit=1)[-1]
    archive_path = cache_dir / filename
    metadata_path = cache_dir / f"{filename}.metadata.json"
    _require_no_cache_recovery_material(archive_path, metadata_path)
    cached = _load_cached_download(
        archive_path, metadata_path, source_url, max_cache_age_hours
    )
    if cached is not None:
        return cached

    temporary_archive = archive_path.with_suffix(f"{archive_path.suffix}.part")
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        _prepare_temporary_cache_file(temporary_archive)
        _prepare_temporary_cache_file(temporary_metadata)
    except CadastreDownloadError:
        raise
    except OSError as error:
        raise CadastreDownloadError(
            "Cadastre cache paths cannot be prepared safely"
        ) from error
    try:
        with (
            open_safe_https(
                source_url,
                timeout=timeout,
                headers={"User-Agent": "LandScout-AI/0.1"},
            ) as response,
            temporary_archive.open("xb") as output,
        ):
            copyfileobj(response, output)
        if not _is_valid_gzip(temporary_archive):
            raise CadastreDownloadError("Downloaded cadastre archive is not valid gzip")
        result = CadastreDownload(
            source_url=source_url,
            download_timestamp=datetime.now(UTC).isoformat(),
            filename=filename,
            file_size=temporary_archive.stat().st_size,
            sha256=_sha256(temporary_archive),
            path=archive_path,
            cache_hit=False,
        )
        metadata = asdict(result)
        metadata.pop("path")
        metadata.pop("cache_hit")
        try:
            with temporary_metadata.open("x", encoding="utf-8") as output:
                output.write(
                    json.dumps(metadata, indent=2, sort_keys=True) + "\n"
                )
            _publish_cache_pair(
                temporary_archive,
                temporary_metadata,
                archive_path,
                metadata_path,
            )
        except OSError as error:
            raise CadastreDownloadError(
                f"Cadastre cache publication failed: {source_url}"
            ) from error
        return result
    except CadastreDownloadError:
        raise
    except (HTTPError, URLError, OSError) as error:
        raise CadastreDownloadError(f"Cadastre download failed: {source_url}") from error
    finally:
        _cleanup_temporary_cache_files(
            (temporary_archive, temporary_metadata),
            sys.exception(),
        )
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.

- Configured source identity: canonical commune code and the adapter's official URL builder; no checked-in Cadastre YAML model.
- URL/safe transport: the constructed HTTPS URL is passed through open_safe_https.
- Physical bytes: streamed gzip is fully validated and hashed; cache sidecar binds URL/timestamp/name/size/SHA and freshness.
- Archive/extraction/layer: gzip GeoJSON is validated but not extracted to a directory and has no physical-layer selector.
- Result/later revalidation: CadastreDownload carries byte identity; cadastre_loader_fr later rechecks type, current bytes, gzip, parse-time stability, and geometry.

## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the cadastre flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
