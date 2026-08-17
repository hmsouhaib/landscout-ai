# `src/landscout/sources/cadastre_fr.py`

## File identity

- Repository path: `src/landscout/sources/cadastre_fr.py`
- File type: Python source
- Primary responsibility: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.
- Layer / domain: `source adapter` / `cadastre`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `cd615e3db3acc3d4fb1a1dd44afe738fd8d58062972ac4d24c8c71a47f0255e6`

## 1. Purpose

Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

## 2. Position in LandScout architecture

This file is a `source adapter` artifact in the `cadastre` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `import gzip` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import sys` — required by the implementation paths and symbols documented below.
- `from dataclasses import asdict, dataclass` — required by the implementation paths and symbols documented below.
- `from datetime import UTC, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from shutil import copy2, copyfileobj` — required by the implementation paths and symbols documented below.
- `from urllib.error import HTTPError, URLError` — required by the implementation paths and symbols documented below.

### Third-party

- None.

### Internal LandScout

- `from landscout.common.safe_http import open_safe_https` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `CADASTRE_BASE_URL` | `"https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DEFAULT_CACHE_DIR` | `Path("data/cache/cadastre")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `VALIDATION_CHUNK_SIZE` | `1024 * 1024` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `CadastreDownloadError`

**Purpose:** Raised when a cadastre archive cannot be downloaded safely.

**Inheritance:** `RuntimeError`.

**Model form and mutability:** class inheriting from `RuntimeError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `CadastreDownload`

**Purpose:** Carries an immutable downloaded-source lineage envelope including byte identity and cache status.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `source_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `download_timestamp` | `str` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `filename` | `str` | `required` | `str` state used by `src/landscout/sources/cadastre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `file_size` | `int` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `path` | `Path` | `required` | `Path` state used by `src/landscout/sources/cadastre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache_hit` | `bool` | `required` | Boolean recording whether verified local bytes were reused instead of acquired during this call. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_department_code`

**Signature**

```python
def _department_code(commune_code: str) -> str:
```

**Purpose**

Implements department code according to the exact implementation and guards in this file.

**Inputs**

- `commune_code` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `commune_code[:3] if commune_code.startswith(('97', '98')) else commune_code[:2]`.

**Algorithm**

1. Returns `commune_code[:3] if commune_code.startswith(('97', '98')) else commune_code[:2]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `commune_code.startswith`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `build_cadastre_parcelles_url`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `build_cadastre_parcelles_url`

**Signature**

```python
def build_cadastre_parcelles_url(commune_code: str) -> str:
```

**Purpose**

Builds cadastre parcelles url according to the exact implementation and guards in this file.

**Inputs**

- `commune_code` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `f'{CADASTRE_BASE_URL}/{department}/{commune_code}/{filename}'`.

**Algorithm**

1. Checks `not isinstance(commune_code, str)`. When true: Raises `TypeError('Commune code must be an exact string')`.
2. Checks `re.fullmatch('(?:\\d{5}|2[AB]\\d{3})', commune_code) is None`. When true: Raises `ValueError('Commune code must be a canonical French INSEE code')`.
3. Computes `department` from `_department_code(commune_code)`.
4. Computes `filename` from `f'cadastre-{commune_code}-parcelles.json.gz'`.
5. Returns `f'{CADASTRE_BASE_URL}/{department}/{commune_code}/{filename}'`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(commune_code, str)` is true.
- Rejects or diverts the path when `re.fullmatch('(?:\\d{5}|2[AB]\\d{3})', commune_code) is None` is true.

**Exceptions**

- Explicitly raises: `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `TypeError`, `ValueError`, `_department_code`, `isinstance`, `re.fullmatch`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `download_cadastre_parcelles`
- `tests/unit/test_cadastre_fr.py` — `test_build_cadastre_parcelles_url`
- `tests/unit/test_cadastre_fr.py` — `test_corsica_cadastre_urls_are_canonical`
- `tests/unit/test_cadastre_fr.py` — `test_noncanonical_commune_code_is_controlled`

**Tests**

- `tests/unit/test_cadastre_fr.py::test_build_cadastre_parcelles_url`
- `tests/unit/test_cadastre_fr.py::test_corsica_cadastre_urls_are_canonical`
- `tests/unit/test_cadastre_fr.py::test_noncanonical_commune_code_is_controlled`

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_sha256`

**Signature**

```python
def _sha256(path: Path) -> str:
```

**Purpose**

Implements sha256 according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `digest.hexdigest()`.

**Algorithm**

1. Computes `digest` from `sha256()`.
2. Enters managed context(s) `path.open('rb')` and executes: Iterates `chunk` over `iter(lambda: stream.read(1024 * 1024), b'')`. For each value: Calls `digest.update(chunk)` for its validation or side effect.
3. Returns `digest.hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `digest.hexdigest`, `digest.update`, `iter`, `path.open`, `sha256`, `stream.read`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `_load_cached_download`
- `src/landscout/sources/cadastre_fr.py` — `download_cadastre_parcelles`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_is_valid_gzip`

**Signature**

```python
def _is_valid_gzip(path: Path) -> bool:
```

**Purpose**

Returns whether `valid gzip` satisfies the exact predicates and branches listed below.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `True`; `False`.

**Algorithm**

1. Runs guarded operation: Checks `not path.is_file() or path.stat().st_size == 0`. When true: Returns `False`. Enters managed context(s) `gzip.open(path, 'rb')` and executes: Repeats the guarded body while `stream.read(VALIDATION_CHUNK_SIZE)` remains true. Returns `True`. Handles `(EOFError, OSError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gzip.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `gzip.open`, `path.is_file`, `path.stat`, `stream.read`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `_load_cached_download`
- `src/landscout/sources/cadastre_fr.py` — `download_cadastre_parcelles`
- `tests/unit/test_cadastre_fr.py` — `test_truncated_gzip_is_rejected`
- `tests/unit/test_cadastre_fr.py` — `test_valid_gzip_is_accepted`

**Tests**

- `tests/unit/test_cadastre_fr.py::test_truncated_gzip_is_rejected`
- `tests/unit/test_cadastre_fr.py::test_valid_gzip_is_accepted`

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_load_cached_download`

**Signature**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    source_url: str,
    max_cache_age_hours: float,
) -> CadastreDownload | None:
```

**Purpose**

Loads cached download according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_url` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `max_cache_age_hours` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CadastreDownload | None`. Observed return expression(s): `None`; `CadastreDownload(source_url=source_url, download_timestamp=download_timestamp, filename=archive_path.name, file_size=file_size, sha256=checksum, path=archive_path, cache_hit=True)`.

**Algorithm**

1. Checks `not archive_path.is_file() or not metadata_path.is_file()`. When true: Returns `None`.
2. Runs guarded operation: Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`. Checks `not isinstance(metadata, dict)`. When true: Returns `None`. Computes `file_size` from `archive_path.stat().st_size`. Computes `checksum` from `_sha256(archive_path)`. Executes 8 additional source-ordered statement(s). Handles `(KeyError, OSError, TypeError, ValueError, json.JSONDecodeError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds`, `CadastreDownload`, `downloaded_at.astimezone`, `metadata_path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds`, `CadastreDownload`, `_is_valid_gzip`, `_sha256`, `archive_path.is_file`, `archive_path.stat`, `datetime.fromisoformat`, `datetime.now`, `downloaded_at.astimezone`, `isinstance`, `json.loads`, `metadata_path.is_file`, `metadata_path.read_text`, `re.fullmatch`, `type`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `download_cadastre_parcelles`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_replace_file`

**Signature**

```python
def _replace_file(source: Path, target: Path) -> None:
```

**Purpose**

Implements replace file according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `source.replace(target)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `source.replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `source.replace`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `_publish_cache_pair`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_is_link_or_junction`

**Signature**

```python
def _is_link_or_junction(path: Path) -> bool:
```

**Purpose**

Returns whether `link or junction` satisfies the exact predicates and branches listed below.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `path.is_symlink() or path.is_junction()`; `True`.

**Algorithm**

1. Runs guarded operation: Returns `path.is_symlink() or path.is_junction()`. Handles `OSError`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `path.is_junction`, `path.is_symlink`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `_prepare_temporary_cache_file`
- `src/landscout/sources/cadastre_fr.py` — `_require_no_cache_recovery_material`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_cache_recovery_paths`

**Signature**

```python
def _cache_recovery_paths(
    archive_path: Path,
    metadata_path: Path,
) -> tuple[Path, Path]:
```

**Purpose**

Implements cache recovery paths according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[Path, Path]`. Observed return expression(s): `(archive_path.with_suffix(f'{archive_path.suffix}.bak'), metadata_path.with_suffix(f'{metadata_path.suffix}.bak'))`.

**Algorithm**

1. Returns `(archive_path.with_suffix(f'{archive_path.suffix}.bak'), metadata_path.with_suffix(f'{metadata_path.suffix}.bak'))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `archive_path.with_suffix`, `metadata_path.with_suffix`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `_publish_cache_pair`
- `src/landscout/sources/cadastre_fr.py` — `_require_no_cache_recovery_material`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_require_no_cache_recovery_material`

**Signature**

```python
def _require_no_cache_recovery_material(
    archive_path: Path,
    metadata_path: Path,
) -> None:
```

**Purpose**

Implements require no cache recovery material according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `any((path.exists() or _is_link_or_junction(path) for path in _cache_recovery_paths(archive_path, metadata_path)))`. When true: Raises `CadastreDownloadError('Cadastre cache recovery backup already exists; manual recovery is required')`.

**Validation and invariants**

- Rejects or diverts the path when `any((path.exists() or _is_link_or_junction(path) for path in _cache_recovery_paths(archive_path, metadata_path)))` is true.

**Exceptions**

- Explicitly raises: `CadastreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `CadastreDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CadastreDownloadError`, `_cache_recovery_paths`, `_is_link_or_junction`, `any`, `path.exists`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `_publish_cache_pair`
- `src/landscout/sources/cadastre_fr.py` — `download_cadastre_parcelles`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_prepare_temporary_cache_file`

**Signature**

```python
def _prepare_temporary_cache_file(path: Path) -> None:
```

**Purpose**

Implements prepare temporary cache file according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Checks `_is_link_or_junction(path)`. When true: Raises `CadastreDownloadError('Cadastre cache temporary path is a link or junction')`. Checks `path.exists()`. When true: Checks `not path.is_file()`. When true: Raises `CadastreDownloadError('Cadastre cache temporary path is not a regular file')`. Calls `path.unlink()` for its validation or side effect. Handles `CadastreDownloadError`, `OSError`.

**Validation and invariants**

- Rejects or diverts the path when `_is_link_or_junction(path)` is true.
- Rejects or diverts the path when `path.exists()` is true.
- Rejects or diverts the path when `not path.is_file()` is true.

**Exceptions**

- Explicitly raises: `CadastreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `CadastreDownloadError`, `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CadastreDownloadError`, `_is_link_or_junction`, `path.exists`, `path.is_file`, `path.unlink`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `download_cadastre_parcelles`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_cleanup_temporary_cache_files`

**Signature**

```python
def _cleanup_temporary_cache_files(
    paths: tuple[Path, ...],
    primary_error: BaseException | None,
) -> None:
```

**Purpose**

Implements cleanup temporary cache files according to the exact implementation and guards in this file.

**Inputs**

- `paths` (`tuple[Path, ...]`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `primary_error` (`BaseException | None`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Defines `cleanup_error` with annotation `OSError | None` from `None`.
2. Iterates `path` over `paths`. For each value: Runs guarded operation: Calls `path.unlink(missing_ok=True)` for its validation or side effect. Handles `OSError`.
3. Checks `cleanup_error is not None and primary_error is None`. When true: Raises `CadastreDownloadError('Cadastre cache temporary files could not be cleaned safely')`.

**Validation and invariants**

- Rejects or diverts the path when `cleanup_error is not None and primary_error is None` is true.

**Exceptions**

- Explicitly raises: `CadastreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `CadastreDownloadError`, `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CadastreDownloadError`, `path.unlink`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `download_cadastre_parcelles`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_publish_cache_pair`

**Signature**

```python
def _publish_cache_pair(
    temporary_archive: Path,
    temporary_metadata: Path,
    archive_path: Path,
    metadata_path: Path,
) -> None:
```

**Purpose**

Implements publish cache pair according to the exact implementation and guards in this file.

**Inputs**

- `temporary_archive` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `temporary_metadata` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `(archive_backup, metadata_backup)` from `_cache_recovery_paths(archive_path, metadata_path)`.
2. Computes `archive_existed` from `archive_path.is_file()`.
3. Computes `metadata_existed` from `metadata_path.is_file()`.
4. Calls `_require_no_cache_recovery_material(archive_path, metadata_path)` for its validation or side effect.
5. Runs guarded operation: Checks `archive_existed`. When true: Calls `copy2(archive_path, archive_backup)` for its validation or side effect. Checks `metadata_existed`. When true: Calls `copy2(metadata_path, metadata_backup)` for its validation or side effect. Handles `OSError`.
6. Runs guarded operation: Calls `_replace_file(temporary_archive, archive_path)` for its validation or side effect. Calls `_replace_file(temporary_metadata, metadata_path)` for its validation or side effect. Handles `OSError`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `CadastreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `CadastreDownloadError`, `_replace_file`, `archive_backup.unlink`, `archive_path.unlink`, `copy2`, `metadata_backup.unlink`, `metadata_path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CadastreDownloadError`, `_cache_recovery_paths`, `_replace_file`, `_require_no_cache_recovery_material`, `archive_backup.unlink`, `archive_path.is_file`, `archive_path.unlink`, `copy2`, `metadata_backup.unlink`, `metadata_path.is_file`, `metadata_path.unlink`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `download_cadastre_parcelles`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `download_cadastre_parcelles`

**Signature**

```python
def download_cadastre_parcelles(
    commune_code: str,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
    max_cache_age_hours: float = 168.0,
) -> CadastreDownload:
```

**Purpose**

Downloads and validates cadastre parcelles according to the exact implementation and guards in this file.

**Inputs**

- `commune_code` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cache_dir` (`Path`; optional/default `DEFAULT_CACHE_DIR`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; optional/default `60.0`) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.
- `max_cache_age_hours` (`float`; optional/default `168.0`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CadastreDownload`. Observed return expression(s): `cached`; `result`.

**Algorithm**

1. Checks `isinstance(timeout, bool) or not isinstance(timeout, Real) or (not isfinite(float(timeout))) or (timeout <= 0)`. When true: Raises `ValueError('timeout must be a strict finite positive number')`.
2. Checks `isinstance(max_cache_age_hours, bool) or not isinstance(max_cache_age_hours, Real) or (not isfinite(float(max_cache_age_hours))) or (max_cache_age_hours < 0)`. When true: Raises `ValueError('max_cache_age_hours must be non-negative')`.
3. Computes `source_url` from `build_cadastre_parcelles_url(commune_code)`.
4. Computes `filename` from `source_url.rsplit('/', maxsplit=1)[-1]`.
5. Computes `archive_path` from `cache_dir / filename`.
6. Computes `metadata_path` from `cache_dir / f'{filename}.metadata.json'`.
7. Calls `_require_no_cache_recovery_material(archive_path, metadata_path)` for its validation or side effect.
8. Computes `cached` from `_load_cached_download(archive_path, metadata_path, source_url, max_cache_age_hours)`.
9. Checks `cached is not None`. When true: Returns `cached`.
10. Computes `temporary_archive` from `archive_path.with_suffix(f'{archive_path.suffix}.part')`.
11. Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
12. Runs guarded operation: Calls `cache_dir.mkdir(parents=True, exist_ok=True)` for its validation or side effect. Calls `_prepare_temporary_cache_file(temporary_archive)` for its validation or side effect. Calls `_prepare_temporary_cache_file(temporary_metadata)` for its validation or side effect. Handles `CadastreDownloadError`, `OSError`.
13. Runs guarded operation: Enters managed context(s) `open_safe_https(source_url, timeout=timeout, headers={'User-Agent': 'LandScout-AI/0.1'}), temporary_archive.open('xb')` and executes: Calls `copyfileobj(response, output)` for its validation or side effect. Checks `not _is_valid_gzip(temporary_archive)`. When true: Raises `CadastreDownloadError('Downloaded cadastre archive is not valid gzip')`. Computes `result` from `CadastreDownload(source_url=source_url, download_timestamp=datetime.now(UTC).isoformat(), filename=filename, file_size=temporary_archive.stat().st_size, sha256=_sha256(temporary_archive), path=archive_path, cache_hit=False)`. Computes `metadata` from `asdict(result)`. Executes 4 additional source-ordered statement(s). Handles `CadastreDownloadError`, `(HTTPError, URLError, OSError)`. Finally: Calls `_cleanup_temporary_cache_files((temporary_archive, temporary_metadata), sys.exception())` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(timeout, bool) or not isinstance(timeout, Real) or (not isfinite(float(timeout))) or (timeout <= 0)` is true.
- Rejects or diverts the path when `isinstance(max_cache_age_hours, bool) or not isinstance(max_cache_age_hours, Real) or (not isfinite(float(max_cache_age_hours))) or (max_cache_age_hours < 0)` is true.
- Rejects or diverts the path when `not _is_valid_gzip(temporary_archive)` is true.

**Exceptions**

- Explicitly raises: `CadastreDownloadError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `CadastreDownload`, `CadastreDownloadError`, `_load_cached_download`, `cache_dir.mkdir`, `copyfileobj`, `open_safe_https`, `output.write`, `temporary_archive.open`, `temporary_metadata.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CadastreDownload`, `CadastreDownloadError`, `ValueError`, `_cleanup_temporary_cache_files`, `_is_valid_gzip`, `_load_cached_download`, `_prepare_temporary_cache_file`, `_publish_cache_pair`, `_require_no_cache_recovery_material`, `_sha256`, `archive_path.with_suffix`, `asdict`, `build_cadastre_parcelles_url`, `cache_dir.mkdir`, `copyfileobj`, `datetime.now`, `datetime.now(UTC).isoformat`, `float`, `isfinite`, `isinstance`, `json.dumps`, `metadata.pop`, `metadata_path.with_suffix`, `open_safe_https`, `output.write`, `source_url.rsplit`, `sys.exception`, `temporary_archive.open`, `temporary_archive.stat`, `temporary_metadata.open`.

**Known repository callers**

- `tests/unit/test_cadastre_fr.py` — `test_broken_recovery_symlink_is_rejected_before_network`
- `tests/unit/test_cadastre_fr.py` — `test_cache_age_is_strict_finite_nonnegative`
- `tests/unit/test_cadastre_fr.py` — `test_checksum_generation`
- `tests/unit/test_cadastre_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_cadastre_fr.py` — `test_corrupted_cached_archive_triggers_fresh_download`
- `tests/unit/test_cadastre_fr.py` — `test_corrupted_new_download_preserves_existing_archive`
- `tests/unit/test_cadastre_fr.py` — `test_download_timeout_is_strict_finite_positive`
- `tests/unit/test_cadastre_fr.py` — `test_expired_cache_is_downloaded_again`
- `tests/unit/test_cadastre_fr.py` — `test_failed_http_response`
- `tests/unit/test_cadastre_fr.py` — `test_failed_refresh_preserves_cached_archive`
- `tests/unit/test_cadastre_fr.py` — `test_first_metadata_publication_failure_leaves_no_half_pair`
- `tests/unit/test_cadastre_fr.py` — `test_fresh_cache_is_reused`
- `tests/unit/test_cadastre_fr.py` — `test_future_cached_timestamp_triggers_refresh`
- `tests/unit/test_cadastre_fr.py` — `test_malformed_cached_metadata_triggers_refresh`
- `tests/unit/test_cadastre_fr.py` — `test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_cadastre_fr.py` — `test_next_run_after_double_failure_preserves_recovery_before_network`
- `tests/unit/test_cadastre_fr.py` — `test_publication_and_rollback_failure_preserves_recovery_backup`
- `tests/unit/test_cadastre_fr.py` — `test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes`
- `tests/unit/test_cadastre_fr.py` — `test_successful_download`
- `tests/unit/test_cadastre_fr.py` — `test_temporary_link_or_junction_cannot_modify_target_before_network`

**Tests**

- `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network`
- `tests/unit/test_cadastre_fr.py::test_cache_age_is_strict_finite_nonnegative`
- `tests/unit/test_cadastre_fr.py::test_checksum_generation`
- `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_cadastre_fr.py::test_corrupted_cached_archive_triggers_fresh_download`
- `tests/unit/test_cadastre_fr.py::test_corrupted_new_download_preserves_existing_archive`
- `tests/unit/test_cadastre_fr.py::test_download_timeout_is_strict_finite_positive`
- `tests/unit/test_cadastre_fr.py::test_expired_cache_is_downloaded_again`
- `tests/unit/test_cadastre_fr.py::test_failed_http_response`
- `tests/unit/test_cadastre_fr.py::test_failed_refresh_preserves_cached_archive`
- `tests/unit/test_cadastre_fr.py::test_first_metadata_publication_failure_leaves_no_half_pair`
- `tests/unit/test_cadastre_fr.py::test_fresh_cache_is_reused`
- `tests/unit/test_cadastre_fr.py::test_future_cached_timestamp_triggers_refresh`
- `tests/unit/test_cadastre_fr.py::test_malformed_cached_metadata_triggers_refresh`
- `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network`
- `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup`
- `tests/unit/test_cadastre_fr.py::test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes`
- `tests/unit/test_cadastre_fr.py::test_successful_download`
- `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network`

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `file_size` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `filename` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sha256` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `cadastre` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
