# `src/landscout/sources/cadastre_fr.py`

## File identity

- Repository path: `src/landscout/sources/cadastre_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: official source acquisition and physical authority
- Responsibility: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.
- Source SHA256: `8d99fb63b6815ef12acb5318bf0cbc8a4b3d87fffe54aa2205d9dd4b26304418`

## 1. STEP 7F.1A.4 contract delta

- Binds the Cadastre download envelope to canonical commune/official URL/filename and strict cache metadata, while preserving transactional recovery.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

The file belongs to the **source adapter** layer and **official source acquisition and physical authority** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import gzip`
- `import json`
- `import re`
- `import sys`
- `from dataclasses import dataclass`
- `from datetime import UTC, datetime`
- `from hashlib import sha256`
- `from math import isfinite`
- `from numbers import Real`
- `from pathlib import Path`
- `from shutil import copy2, copyfileobj`
- `from typing import Literal`
- `from urllib.error import HTTPError, URLError`

### Third-party packages

- `from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictStr,
    ValidationError,
    field_validator,
)`

### Internal LandScout imports

- `from landscout.common.safe_http import open_safe_https`
- `from landscout.common.strict_json import loads_strict_json_object`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `CADASTRE_BASE_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
CADASTRE_BASE_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DEFAULT_CACHE_DIR`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEFAULT_CACHE_DIR = Path("data/cache/cadastre")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `VALIDATION_CHUNK_SIZE`

- Category: module constant or closed domain.
- Exact declaration:

```python
VALIDATION_CHUNK_SIZE = 1024 * 1024
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `CadastreDownloadError`

**Source purpose:** Raised when a cadastre archive cannot be downloaded safely.

- Exact decorators: none.
- Exact bases: `RuntimeError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- constructor call: `landscout.sources.cadastre_fr::_require_no_cache_recovery_material` via `CadastreDownloadError`
- value/type reference: `landscout.sources.cadastre_fr::_require_no_cache_recovery_material` via `CadastreDownloadError`
- constructor call: `landscout.sources.cadastre_fr::_require_safe_cache_primary_paths` via `CadastreDownloadError`
- value/type reference: `landscout.sources.cadastre_fr::_require_safe_cache_primary_paths` via `CadastreDownloadError`
- constructor call: `landscout.sources.cadastre_fr::_prepare_temporary_cache_file` via `CadastreDownloadError`
- value/type reference: `landscout.sources.cadastre_fr::_prepare_temporary_cache_file` via `CadastreDownloadError`
- constructor call: `landscout.sources.cadastre_fr::_cleanup_temporary_cache_files` via `CadastreDownloadError`
- value/type reference: `landscout.sources.cadastre_fr::_cleanup_temporary_cache_files` via `CadastreDownloadError`
- constructor call: `landscout.sources.cadastre_fr::_publish_cache_pair` via `CadastreDownloadError`
- value/type reference: `landscout.sources.cadastre_fr::_publish_cache_pair` via `CadastreDownloadError`
- constructor call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `CadastreDownloadError`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `CadastreDownloadError`
- import: `tests.unit.test_cadastre_fr::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- value/type reference: `tests.unit.test_cadastre_fr::test_failed_refresh_preserves_cached_archive` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_failed_http_response` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_corrupted_new_download_preserves_existing_archive` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_first_metadata_publication_failure_leaves_no_half_pair` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_publication_and_rollback_failure_preserves_recovery_backup` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_next_run_after_double_failure_preserves_recovery_before_network` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_temporary_link_or_junction_cannot_modify_target_before_network` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_broken_recovery_symlink_is_rejected_before_network` via `CadastreDownloadError`
- value/type reference: `tests.unit.test_cadastre_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `CadastreDownloadError`

**Exact class source**

```python
class CadastreDownloadError(RuntimeError):
    """Raised when a cadastre archive cannot be downloaded safely."""
```

### `CadastreDownload`

**Source purpose:** Defines `CadastreDownload`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `commune_code` | `str` | `required` | `commune_code: str` |
| `source_url` | `str` | `required` | `source_url: str` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `filename` | `str` | `required` | `filename: str` |
| `file_size` | `int` | `required` | `file_size: int` |
| `sha256` | `str` | `required` | `sha256: str` |
| `path` | `Path` | `required` | `path: Path` |
| `cache_hit` | `bool` | `required` | `cache_hit: bool` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- constructor call: `landscout.sources.cadastre_fr::_load_cached_download` via `CadastreDownload`
- value/type reference: `landscout.sources.cadastre_fr::_load_cached_download` via `CadastreDownload`
- constructor call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `CadastreDownload`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `CadastreDownload`
- import: `landscout.sources.cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    build_cadastre_parcelles_url,
)`
- value/type reference: `landscout.sources.cadastre_loader_fr::_validate_download` via `CadastreDownload`
- value/type reference: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `CadastreDownload`
- value/type reference: `landscout.sources.cadastre_loader_fr::load_cadastre_parcels` via `CadastreDownload`
- import: `tests.unit.test_cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_fr import CadastreDownload`
- constructor call: `tests.unit.test_cadastre_loader_fr::_download` via `CadastreDownload`
- value/type reference: `tests.unit.test_cadastre_loader_fr::_download` via `CadastreDownload`
- import: `tests.unit.test_normalize_cadastre::<module>` via `from landscout.sources.cadastre_fr import CadastreDownload`
- constructor call: `tests.unit.test_normalize_cadastre::_bound_source` via `CadastreDownload`
- value/type reference: `tests.unit.test_normalize_cadastre::_bound_source` via `CadastreDownload`

**Exact class source**

```python
class CadastreDownload:
    commune_code: str
    source_url: str
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool
```

### `_CadastreCacheMetadata`

**Source purpose:** Defines `_CadastreCacheMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `schema_version` | `Literal[1]` | `required` | `schema_version: Literal[1]` |
| `commune_code` | `StrictStr` | `required` | `commune_code: StrictStr` |
| `source_url` | `StrictStr` | `required` | `source_url: StrictStr` |
| `download_timestamp` | `StrictStr` | `required` | `download_timestamp: StrictStr` |
| `filename` | `StrictStr` | `required` | `filename: StrictStr` |
| `file_size` | `int` | `Field(strict=True, gt=0)` | `file_size: int = Field(strict=True, gt=0)` |
| `sha256` | `StrictStr` | `required` | `sha256: StrictStr` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.sources.cadastre_fr::_load_cached_download` via `_CadastreCacheMetadata`
- constructor call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_CadastreCacheMetadata`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_CadastreCacheMetadata`

**Exact class source**

```python
class _CadastreCacheMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    commune_code: StrictStr
    source_url: StrictStr
    download_timestamp: StrictStr
    filename: StrictStr
    file_size: int = Field(strict=True, gt=0)
    sha256: StrictStr

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("Cadastre cache schema version must be an exact integer")
        return value
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_CadastreCacheMetadata._strict_schema_version`

**Purpose:** Implements `strict schema version` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _strict_schema_version(cls, value: object) -> object:
```

- Exact decorators: `field_validator("schema_version", mode="before")`, `classmethod`.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cls` | positional-or-keyword | `None` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError("Cadastre cache schema version must be an exact integer")` under lexical guard `type(value) is not int`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `field_validator` | `pydantic.field_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("Cadastre cache schema version must be an exact integer")
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_department_code`

**Purpose:** Implements `department code` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _department_code(commune_code: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `commune_code` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `commune_code[:3] if commune_code.startswith(("97", "98")) else commune_code[:2]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::build_cadastre_parcelles_url` via `_department_code`
- value/type reference: `landscout.sources.cadastre_fr::build_cadastre_parcelles_url` via `_department_code`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `commune_code.startswith` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _department_code(commune_code: str) -> str:
    return (
        commune_code[:3] if commune_code.startswith(("97", "98")) else commune_code[:2]
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `build_cadastre_parcelles_url`

**Purpose:** Implements `build cadastre parcelles url` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def build_cadastre_parcelles_url(commune_code: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `commune_code` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `f"{CADASTRE_BASE_URL}/{department}/{commune_code}/{filename}"`
- Explicit raise paths:
  - `TypeError("Commune code must be an exact string")` under lexical guard `not isinstance(commune_code, str)`.
  - `ValueError("Commune code must be a canonical French INSEE code")` under lexical guard `re.fullmatch(r"(?:\d{5}\|2[AB]\d{3})", commune_code) is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `build_cadastre_parcelles_url`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `build_cadastre_parcelles_url`
- import: `landscout.sources.cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    build_cadastre_parcelles_url,
)`
- direct call: `landscout.sources.cadastre_loader_fr::_validate_download` via `build_cadastre_parcelles_url`
- value/type reference: `landscout.sources.cadastre_loader_fr::_validate_download` via `build_cadastre_parcelles_url`
- import: `tests.unit.test_cadastre_fr::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- direct call: `tests.unit.test_cadastre_fr::test_build_cadastre_parcelles_url` via `build_cadastre_parcelles_url`
- value/type reference: `tests.unit.test_cadastre_fr::test_build_cadastre_parcelles_url` via `build_cadastre_parcelles_url`
- direct call: `tests.unit.test_cadastre_fr::test_corsica_cadastre_urls_are_canonical` via `build_cadastre_parcelles_url`
- value/type reference: `tests.unit.test_cadastre_fr::test_corsica_cadastre_urls_are_canonical` via `build_cadastre_parcelles_url`
- direct call: `tests.unit.test_cadastre_fr::test_noncanonical_commune_code_is_controlled` via `build_cadastre_parcelles_url`
- value/type reference: `tests.unit.test_cadastre_fr::test_noncanonical_commune_code_is_controlled` via `build_cadastre_parcelles_url`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.fullmatch` | `re.fullmatch` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_department_code` | `landscout.sources.cadastre_fr._department_code` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_sha256`

**Purpose:** Implements `sha256` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _sha256(path: Path) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `digest.hexdigest()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::_load_cached_download` via `_sha256`
- value/type reference: `landscout.sources.cadastre_fr::_load_cached_download` via `_sha256`
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_sha256`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sha256` | `hashlib.sha256` |
| `path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `iter` | `unresolved local/third-party receiver; no ownership inferred` |
| `digest.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `digest.hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `digest.update(chunk)` |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_is_valid_gzip`

**Purpose:** Implements `is valid gzip` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _is_valid_gzip(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `False`
  - `True`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::_load_cached_download` via `_is_valid_gzip`
- value/type reference: `landscout.sources.cadastre_fr::_load_cached_download` via `_is_valid_gzip`
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_is_valid_gzip`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_is_valid_gzip`
- import: `tests.unit.test_cadastre_fr::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- direct call: `tests.unit.test_cadastre_fr::test_valid_gzip_is_accepted` via `_is_valid_gzip`
- value/type reference: `tests.unit.test_cadastre_fr::test_valid_gzip_is_accepted` via `_is_valid_gzip`
- direct call: `tests.unit.test_cadastre_fr::test_truncated_gzip_is_rejected` via `_is_valid_gzip`
- value/type reference: `tests.unit.test_cadastre_fr::test_truncated_gzip_is_rejected` via `_is_valid_gzip`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `gzip.open` | `gzip.open` |
| `stream.read` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file`<br>`path.stat`<br>`gzip.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_load_cached_download`

**Purpose:** Implements `load cached download` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    commune_code: str,
    source_url: str,
    max_cache_age_hours: float,
) -> CadastreDownload | None:
```

- Exact decorators: none.
- Declared return annotation: `CadastreDownload | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `metadata_path` | positional-or-keyword | `Path` | `required` |
| `commune_code` | positional-or-keyword | `str` | `required` |
| `source_url` | positional-or-keyword | `str` | `required` |
| `max_cache_age_hours` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `CadastreDownload(<br>            commune_code=commune_code,<br>            source_url=source_url,<br>            download_timestamp=download_timestamp,<br>            filename=archive_path.name,<br>            file_size=file_size,<br>            sha256=checksum,<br>            path=archive_path,<br>            cache_hit=True,<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_load_cached_download`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_load_cached_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.cadastre_fr._is_link_or_junction` |
| `_CadastreCacheMetadata.model_validate` | `landscout.sources.cadastre_fr._CadastreCacheMetadata.model_validate` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `landscout.sources.cadastre_fr._sha256` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `download_timestamp.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `downloaded_at.utcoffset` | `unresolved local/third-party receiver; no ownership inferred` |
| `UTC.utcoffset` | `datetime.UTC.utcoffset` |
| `(<br>            datetime.now(UTC) - downloaded_at.astimezone(UTC)<br>        ).total_seconds` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `downloaded_at.astimezone` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_valid_gzip` | `landscout.sources.cadastre_fr._is_valid_gzip` |
| `re.fullmatch` | `re.fullmatch` |
| `CadastreDownload` | `landscout.sources.cadastre_fr.CadastreDownload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_path.is_file`<br>`metadata_path.is_file`<br>`metadata_path.read_bytes`<br>`archive_path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    commune_code: str,
    source_url: str,
    max_cache_age_hours: float,
) -> CadastreDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        if _is_link_or_junction(archive_path) or _is_link_or_junction(metadata_path):
            return None
        metadata = _CadastreCacheMetadata.model_validate(
            loads_strict_json_object(metadata_path.read_bytes())
        )
        if metadata.schema_version != 1:
            return None
        file_size = archive_path.stat().st_size
        checksum = _sha256(archive_path)
        download_timestamp = metadata.download_timestamp
        if (
            type(download_timestamp) is not str
            or not download_timestamp
            or download_timestamp != download_timestamp.strip()
        ):
            return None
        downloaded_at = datetime.fromisoformat(download_timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(
            None
        ):
            return None
        age_seconds = (
            datetime.now(UTC) - downloaded_at.astimezone(UTC)
        ).total_seconds()
        valid = (
            file_size > 0
            and 0 <= age_seconds <= max_cache_age_hours * 3600
            and _is_valid_gzip(archive_path)
            and metadata.commune_code == commune_code
            and metadata.source_url == source_url
            and metadata.filename == archive_path.name
            and metadata.file_size == file_size
            and re.fullmatch(r"[0-9a-f]{64}", metadata.sha256) is not None
            and metadata.sha256 == checksum
        )
        if not valid:
            return None
        return CadastreDownload(
            commune_code=commune_code,
            source_url=source_url,
            download_timestamp=download_timestamp,
            filename=archive_path.name,
            file_size=file_size,
            sha256=checksum,
            path=archive_path,
            cache_hit=True,
        )
    except (OSError, TypeError, ValueError, ValidationError):
        return None
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_replace_file`

**Purpose:** Implements `replace file` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _replace_file(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::_publish_cache_pair` via `_replace_file`
- value/type reference: `landscout.sources.cadastre_fr::_publish_cache_pair` via `_replace_file`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source.replace` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `source.replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_is_link_or_junction`

**Purpose:** Implements `is link or junction` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _is_link_or_junction(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path.is_symlink() or path.is_junction()`
  - `True`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::_load_cached_download` via `_is_link_or_junction`
- value/type reference: `landscout.sources.cadastre_fr::_load_cached_download` via `_is_link_or_junction`
- direct call: `landscout.sources.cadastre_fr::_require_no_cache_recovery_material` via `_is_link_or_junction`
- value/type reference: `landscout.sources.cadastre_fr::_require_no_cache_recovery_material` via `_is_link_or_junction`
- direct call: `landscout.sources.cadastre_fr::_require_safe_cache_primary_paths` via `_is_link_or_junction`
- value/type reference: `landscout.sources.cadastre_fr::_require_safe_cache_primary_paths` via `_is_link_or_junction`
- direct call: `landscout.sources.cadastre_fr::_prepare_temporary_cache_file` via `_is_link_or_junction`
- value/type reference: `landscout.sources.cadastre_fr::_prepare_temporary_cache_file` via `_is_link_or_junction`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_cache_recovery_paths`

**Purpose:** Implements `cache recovery paths` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _cache_recovery_paths(
    archive_path: Path,
    metadata_path: Path,
) -> tuple[Path, Path]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[Path, Path]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `metadata_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>        archive_path.with_suffix(f"{archive_path.suffix}.bak"),<br>        metadata_path.with_suffix(f"{metadata_path.suffix}.bak"),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::_require_no_cache_recovery_material` via `_cache_recovery_paths`
- value/type reference: `landscout.sources.cadastre_fr::_require_no_cache_recovery_material` via `_cache_recovery_paths`
- direct call: `landscout.sources.cadastre_fr::_publish_cache_pair` via `_cache_recovery_paths`
- value/type reference: `landscout.sources.cadastre_fr::_publish_cache_pair` via `_cache_recovery_paths`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_require_no_cache_recovery_material`

**Purpose:** Implements `require no cache recovery material` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _require_no_cache_recovery_material(
    archive_path: Path,
    metadata_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `metadata_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `CadastreDownloadError(<br>            "Cadastre cache recovery backup already exists; manual recovery is required"<br>        )` under lexical guard `any(<br>        path.exists() or _is_link_or_junction(path)<br>        for path in _cache_recovery_paths(archive_path, metadata_path)<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::_publish_cache_pair` via `_require_no_cache_recovery_material`
- value/type reference: `landscout.sources.cadastre_fr::_publish_cache_pair` via `_require_no_cache_recovery_material`
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_require_no_cache_recovery_material`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_require_no_cache_recovery_material`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.cadastre_fr._is_link_or_junction` |
| `_cache_recovery_paths` | `landscout.sources.cadastre_fr._cache_recovery_paths` |
| `CadastreDownloadError` | `landscout.sources.cadastre_fr.CadastreDownloadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.exists` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_require_safe_cache_primary_paths`

**Purpose:** Implements `require safe cache primary paths` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _require_safe_cache_primary_paths(
    archive_path: Path,
    metadata_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `metadata_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `CadastreDownloadError(<br>                    "Cadastre cache path must not be a link or junction"<br>                )` under lexical guard `_is_link_or_junction(path)`.
  - `CadastreDownloadError(<br>                    "Cadastre cache path must be a regular file"<br>                )` under lexical guard `path.exists() and not path.is_file()`.
  - `re-raise`.
  - `CadastreDownloadError(<br>                "Cadastre cache path cannot be inspected safely"<br>            )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_require_safe_cache_primary_paths`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_require_safe_cache_primary_paths`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_link_or_junction` | `landscout.sources.cadastre_fr._is_link_or_junction` |
| `CadastreDownloadError` | `landscout.sources.cadastre_fr.CadastreDownloadError` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.exists`<br>`path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _require_safe_cache_primary_paths(
    archive_path: Path,
    metadata_path: Path,
) -> None:
    for path in (archive_path, metadata_path):
        try:
            if _is_link_or_junction(path):
                raise CadastreDownloadError(
                    "Cadastre cache path must not be a link or junction"
                )
            if path.exists() and not path.is_file():
                raise CadastreDownloadError(
                    "Cadastre cache path must be a regular file"
                )
        except CadastreDownloadError:
            raise
        except OSError as error:
            raise CadastreDownloadError(
                "Cadastre cache path cannot be inspected safely"
            ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_prepare_temporary_cache_file`

**Purpose:** Implements `prepare temporary cache file` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _prepare_temporary_cache_file(path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `CadastreDownloadError(<br>                "Cadastre cache temporary path is a link or junction"<br>            )` under lexical guard `_is_link_or_junction(path)`.
  - `CadastreDownloadError(<br>                    "Cadastre cache temporary path is not a regular file"<br>                )` under lexical guard `path.exists()`.
  - `re-raise`.
  - `CadastreDownloadError(<br>            "Cadastre cache temporary path cannot be prepared safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_prepare_temporary_cache_file`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_prepare_temporary_cache_file`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_link_or_junction` | `landscout.sources.cadastre_fr._is_link_or_junction` |
| `CadastreDownloadError` | `landscout.sources.cadastre_fr.CadastreDownloadError` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.exists`<br>`path.is_file` |
| Filesystem/archive write or publication | `path.unlink` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_cleanup_temporary_cache_files`

**Purpose:** Implements `cleanup temporary cache files` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _cleanup_temporary_cache_files(
    paths: tuple[Path, ...],
    primary_error: BaseException | None,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `paths` | positional-or-keyword | `tuple[Path, ...]` | `required` |
| `primary_error` | positional-or-keyword | `BaseException \| None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `CadastreDownloadError(<br>            "Cadastre cache temporary files could not be cleaned safely"<br>        )` under lexical guard `cleanup_error is not None and primary_error is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_cleanup_temporary_cache_files`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_cleanup_temporary_cache_files`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `CadastreDownloadError` | `landscout.sources.cadastre_fr.CadastreDownloadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.unlink` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_publish_cache_pair`

**Purpose:** Implements `publish cache pair` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def _publish_cache_pair(
    temporary_archive: Path,
    temporary_metadata: Path,
    archive_path: Path,
    metadata_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `temporary_archive` | positional-or-keyword | `Path` | `required` |
| `temporary_metadata` | positional-or-keyword | `Path` | `required` |
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `metadata_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `re-raise`.
  - `CadastreDownloadError(<br>                "Cadastre cache publication and rollback both failed"<br>            )`.
  - `re-raise`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_publish_cache_pair`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `_publish_cache_pair`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_cache_recovery_paths` | `landscout.sources.cadastre_fr._cache_recovery_paths` |
| `archive_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_no_cache_recovery_material` | `landscout.sources.cadastre_fr._require_no_cache_recovery_material` |
| `copy2` | `shutil.copy2` |
| `archive_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_file` | `landscout.sources.cadastre_fr._replace_file` |
| `archive_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `CadastreDownloadError` | `landscout.sources.cadastre_fr.CadastreDownloadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_path.is_file`<br>`metadata_path.is_file` |
| Filesystem/archive write or publication | `archive_backup.unlink`<br>`metadata_backup.unlink`<br>`archive_path.unlink`<br>`metadata_path.unlink` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `download_cadastre_parcelles`

**Purpose:** Implements `download cadastre parcelles` within the file role: Acquires the official French cadastral parcel archive with gzip, cache-integrity, and transactional recovery checks.

**Exact signature**

```python
def download_cadastre_parcelles(
    commune_code: str,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
    max_cache_age_hours: float = 168.0,
) -> CadastreDownload:
```

- Exact decorators: none.
- Declared return annotation: `CadastreDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `commune_code` | positional-or-keyword | `str` | `required` |
| `cache_dir` | positional-or-keyword | `Path` | `DEFAULT_CACHE_DIR` |
| `timeout` | positional-or-keyword | `float` | `60.0` |
| `max_cache_age_hours` | positional-or-keyword | `float` | `168.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `cached`
  - `result`
- Explicit raise paths:
  - `ValueError("timeout must be a strict finite positive number")` under lexical guard `isinstance(timeout, bool)<br>        or not isinstance(timeout, Real)<br>        or not isfinite(float(timeout))<br>        or timeout <= 0`.
  - `ValueError("max_cache_age_hours must be non-negative")` under lexical guard `isinstance(max_cache_age_hours, bool)<br>        or not isinstance(max_cache_age_hours, Real)<br>        or not isfinite(float(max_cache_age_hours))<br>        or max_cache_age_hours < 0`.
  - `re-raise`.
  - `CadastreDownloadError(<br>            "Cadastre cache paths cannot be prepared safely"<br>        )`.
  - `CadastreDownloadError("Downloaded cadastre archive is not valid gzip")` under lexical guard `not _is_valid_gzip(temporary_archive)`.
  - `CadastreDownloadError(<br>                f"Cadastre cache publication failed: {source_url}"<br>            )`.
  - `re-raise`.
  - `CadastreDownloadError(<br>            f"Cadastre download failed: {source_url}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- import: `tests.unit.test_cadastre_fr::<module>` via `from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`
- direct call: `tests.unit.test_cadastre_fr::test_successful_download` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_successful_download` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_fresh_cache_is_reused` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_fresh_cache_is_reused` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_expired_cache_is_downloaded_again` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_expired_cache_is_downloaded_again` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_failed_refresh_preserves_cached_archive` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_failed_refresh_preserves_cached_archive` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_failed_http_response` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_failed_http_response` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_checksum_generation` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_checksum_generation` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_corrupted_cached_archive_triggers_fresh_download` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_corrupted_cached_archive_triggers_fresh_download` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_corrupted_new_download_preserves_existing_archive` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_corrupted_new_download_preserves_existing_archive` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_download_timeout_is_strict_finite_positive` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_download_timeout_is_strict_finite_positive` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_cache_age_is_strict_finite_nonnegative` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_cache_age_is_strict_finite_nonnegative` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_malformed_cached_metadata_triggers_refresh` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_malformed_cached_metadata_triggers_refresh` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_cache_metadata_schema_and_size_are_strict_integers` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_cache_metadata_schema_and_size_are_strict_integers` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_future_cached_timestamp_triggers_refresh` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_future_cached_timestamp_triggers_refresh` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_strict_cadastre_cache_json_never_returns_a_cache_hit` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_strict_cadastre_cache_json_never_returns_a_cache_hit` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_first_metadata_publication_failure_leaves_no_half_pair` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_first_metadata_publication_failure_leaves_no_half_pair` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_publication_and_rollback_failure_preserves_recovery_backup` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_publication_and_rollback_failure_preserves_recovery_backup` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_next_run_after_double_failure_preserves_recovery_before_network` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_next_run_after_double_failure_preserves_recovery_before_network` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_temporary_link_or_junction_cannot_modify_target_before_network` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_temporary_link_or_junction_cannot_modify_target_before_network` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_broken_recovery_symlink_is_rejected_before_network` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_broken_recovery_symlink_is_rejected_before_network` via `download_cadastre_parcelles`
- direct call: `tests.unit.test_cadastre_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_cadastre_parcelles`
- value/type reference: `tests.unit.test_cadastre_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_cadastre_parcelles`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `build_cadastre_parcelles_url` | `landscout.sources.cadastre_fr.build_cadastre_parcelles_url` |
| `source_url.rsplit` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_safe_cache_primary_paths` | `landscout.sources.cadastre_fr._require_safe_cache_primary_paths` |
| `_require_no_cache_recovery_material` | `landscout.sources.cadastre_fr._require_no_cache_recovery_material` |
| `_load_cached_download` | `landscout.sources.cadastre_fr._load_cached_download` |
| `archive_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `cache_dir.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `_prepare_temporary_cache_file` | `landscout.sources.cadastre_fr._prepare_temporary_cache_file` |
| `CadastreDownloadError` | `landscout.sources.cadastre_fr.CadastreDownloadError` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `temporary_archive.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `copyfileobj` | `shutil.copyfileobj` |
| `_is_valid_gzip` | `landscout.sources.cadastre_fr._is_valid_gzip` |
| `CadastreDownload` | `landscout.sources.cadastre_fr.CadastreDownload` |
| `datetime.now(UTC).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `temporary_archive.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `landscout.sources.cadastre_fr._sha256` |
| `_CadastreCacheMetadata` | `landscout.sources.cadastre_fr._CadastreCacheMetadata` |
| `temporary_metadata.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `metadata.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_publish_cache_pair` | `landscout.sources.cadastre_fr._publish_cache_pair` |
| `_cleanup_temporary_cache_files` | `landscout.sources.cadastre_fr._cleanup_temporary_cache_files` |
| `sys.exception` | `sys.exception` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | `temporary_archive.open`<br>`temporary_archive.stat`<br>`temporary_metadata.open` |
| Filesystem/archive write or publication | `cache_dir.mkdir`<br>`copyfileobj` |
| Hashing/byte identity | `_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
    _require_safe_cache_primary_paths(archive_path, metadata_path)
    _require_no_cache_recovery_material(archive_path, metadata_path)
    cached = _load_cached_download(
        archive_path,
        metadata_path,
        commune_code,
        source_url,
        max_cache_age_hours,
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
            commune_code=commune_code,
            source_url=source_url,
            download_timestamp=datetime.now(UTC).isoformat(),
            filename=filename,
            file_size=temporary_archive.stat().st_size,
            sha256=_sha256(temporary_archive),
            path=archive_path,
            cache_hit=False,
        )
        metadata = _CadastreCacheMetadata(
            schema_version=1,
            commune_code=result.commune_code,
            source_url=result.source_url,
            download_timestamp=result.download_timestamp,
            filename=result.filename,
            file_size=result.file_size,
            sha256=result.sha256,
        )
        try:
            with temporary_metadata.open("x", encoding="utf-8") as output:
                output.write(
                    json.dumps(
                        metadata.model_dump(mode="json"), indent=2, sort_keys=True
                    )
                    + "\n"
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
        raise CadastreDownloadError(
            f"Cadastre download failed: {source_url}"
        ) from error
    finally:
        _cleanup_temporary_cache_files(
            (temporary_archive, temporary_metadata),
            sys.exception(),
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: none at module scope.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
import gzip
import json
import re
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from math import isfinite
from numbers import Real
from pathlib import Path
from shutil import copy2, copyfileobj
from typing import Literal
from urllib.error import HTTPError, URLError

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictStr,
    ValidationError,
    field_validator,
)

from landscout.common.safe_http import open_safe_https
from landscout.common.strict_json import loads_strict_json_object

CADASTRE_BASE_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes"
)
DEFAULT_CACHE_DIR = Path("data/cache/cadastre")
VALIDATION_CHUNK_SIZE = 1024 * 1024


class CadastreDownloadError(RuntimeError):
    """Raised when a cadastre archive cannot be downloaded safely."""


@dataclass(frozen=True)
class CadastreDownload:
    commune_code: str
    source_url: str
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool


class _CadastreCacheMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    commune_code: StrictStr
    source_url: StrictStr
    download_timestamp: StrictStr
    filename: StrictStr
    file_size: int = Field(strict=True, gt=0)
    sha256: StrictStr

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("Cadastre cache schema version must be an exact integer")
        return value


def _department_code(commune_code: str) -> str:
    return (
        commune_code[:3] if commune_code.startswith(("97", "98")) else commune_code[:2]
    )


def build_cadastre_parcelles_url(commune_code: str) -> str:
    if not isinstance(commune_code, str):
        raise TypeError("Commune code must be an exact string")
    if re.fullmatch(r"(?:\d{5}|2[AB]\d{3})", commune_code) is None:
        raise ValueError("Commune code must be a canonical French INSEE code")
    department = _department_code(commune_code)
    filename = f"cadastre-{commune_code}-parcelles.json.gz"
    return f"{CADASTRE_BASE_URL}/{department}/{commune_code}/{filename}"


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
    commune_code: str,
    source_url: str,
    max_cache_age_hours: float,
) -> CadastreDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        if _is_link_or_junction(archive_path) or _is_link_or_junction(metadata_path):
            return None
        metadata = _CadastreCacheMetadata.model_validate(
            loads_strict_json_object(metadata_path.read_bytes())
        )
        if metadata.schema_version != 1:
            return None
        file_size = archive_path.stat().st_size
        checksum = _sha256(archive_path)
        download_timestamp = metadata.download_timestamp
        if (
            type(download_timestamp) is not str
            or not download_timestamp
            or download_timestamp != download_timestamp.strip()
        ):
            return None
        downloaded_at = datetime.fromisoformat(download_timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(
            None
        ):
            return None
        age_seconds = (
            datetime.now(UTC) - downloaded_at.astimezone(UTC)
        ).total_seconds()
        valid = (
            file_size > 0
            and 0 <= age_seconds <= max_cache_age_hours * 3600
            and _is_valid_gzip(archive_path)
            and metadata.commune_code == commune_code
            and metadata.source_url == source_url
            and metadata.filename == archive_path.name
            and metadata.file_size == file_size
            and re.fullmatch(r"[0-9a-f]{64}", metadata.sha256) is not None
            and metadata.sha256 == checksum
        )
        if not valid:
            return None
        return CadastreDownload(
            commune_code=commune_code,
            source_url=source_url,
            download_timestamp=download_timestamp,
            filename=archive_path.name,
            file_size=file_size,
            sha256=checksum,
            path=archive_path,
            cache_hit=True,
        )
    except (OSError, TypeError, ValueError, ValidationError):
        return None


def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)


def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True


def _cache_recovery_paths(
    archive_path: Path,
    metadata_path: Path,
) -> tuple[Path, Path]:
    return (
        archive_path.with_suffix(f"{archive_path.suffix}.bak"),
        metadata_path.with_suffix(f"{metadata_path.suffix}.bak"),
    )


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


def _require_safe_cache_primary_paths(
    archive_path: Path,
    metadata_path: Path,
) -> None:
    for path in (archive_path, metadata_path):
        try:
            if _is_link_or_junction(path):
                raise CadastreDownloadError(
                    "Cadastre cache path must not be a link or junction"
                )
            if path.exists() and not path.is_file():
                raise CadastreDownloadError(
                    "Cadastre cache path must be a regular file"
                )
        except CadastreDownloadError:
            raise
        except OSError as error:
            raise CadastreDownloadError(
                "Cadastre cache path cannot be inspected safely"
            ) from error


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
    _require_safe_cache_primary_paths(archive_path, metadata_path)
    _require_no_cache_recovery_material(archive_path, metadata_path)
    cached = _load_cached_download(
        archive_path,
        metadata_path,
        commune_code,
        source_url,
        max_cache_age_hours,
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
            commune_code=commune_code,
            source_url=source_url,
            download_timestamp=datetime.now(UTC).isoformat(),
            filename=filename,
            file_size=temporary_archive.stat().st_size,
            sha256=_sha256(temporary_archive),
            path=archive_path,
            cache_hit=False,
        )
        metadata = _CadastreCacheMetadata(
            schema_version=1,
            commune_code=result.commune_code,
            source_url=result.source_url,
            download_timestamp=result.download_timestamp,
            filename=result.filename,
            file_size=result.file_size,
            sha256=result.sha256,
        )
        try:
            with temporary_metadata.open("x", encoding="utf-8") as output:
                output.write(
                    json.dumps(
                        metadata.model_dump(mode="json"), indent=2, sort_keys=True
                    )
                    + "\n"
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
        raise CadastreDownloadError(
            f"Cadastre download failed: {source_url}"
        ) from error
    finally:
        _cleanup_temporary_cache_files(
            (temporary_archive, temporary_metadata),
            sys.exception(),
        )
```
