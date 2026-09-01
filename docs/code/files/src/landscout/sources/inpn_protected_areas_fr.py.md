# `src/landscout/sources/inpn_protected_areas_fr.py`

## File identity

- Repository path: `src/landscout/sources/inpn_protected_areas_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: official source acquisition and physical authority
- Responsibility: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.
- Source SHA256: `e3bde487e43bfb70fa0edc7ad39a0231cbac7163c167793984dc947ea35cf6b4`

## 1. STEP 7F.1A.4 contract delta

- Moves trust-bearing configuration/cache/extraction JSON/YAML to shared strict decoders and strict finite numeric models without changing the pinned EP snapshot.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

The file belongs to the **source adapter** layer and **official source acquisition and physical authority** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import re`
- `import shutil`
- `import stat`
- `import unicodedata`
- `import zipfile`
- `import zlib`
- `from dataclasses import dataclass`
- `from datetime import UTC, datetime`
- `from hashlib import sha256`
- `from math import isfinite`
- `from numbers import Real`
- `from pathlib import Path, PurePosixPath, PureWindowsPath`
- `from shutil import copy2, copyfileobj`
- `from typing import Annotated, Literal, Self`

### Third-party packages

- `from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
    model_validator,
)`

### Internal LandScout imports

- `from landscout.common.safe_http import SafeHttpsError, open_safe_https`
- `from landscout.common.strict_json import loads_strict_json_object`
- `from landscout.common.strict_yaml import loads_strict_yaml`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `DEFAULT_CONFIG_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEFAULT_CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DOWNLOAD_CHUNK_SIZE`

- Category: module constant or closed domain.
- Exact declaration:

```python
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DOWNLOAD_METADATA_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
DOWNLOAD_METADATA_SCHEMA_VERSION: Literal[1] = 1
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXTRACTION_METADATA_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
EXTRACTION_METADATA_SCHEMA_VERSION: Literal[1] = 1
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXTRACTION_METADATA_FILENAME`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXTRACTION_METADATA_FILENAME = ".landscout-extraction.json"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `OFFICIAL_REFERENCE_PAGE_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
OFFICIAL_REFERENCE_PAGE_URL = (
    "https://www.patrinat.fr/fr/"
    "page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `OFFICIAL_ARCHIVE_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
OFFICIAL_ARCHIVE_URL = "https://assets.patrinat.fr/files/donnees/ep/EP.zip"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `OFFICIAL_DATASET_NAME`

- Category: module constant or closed domain.
- Exact declaration:

```python
OFFICIAL_DATASET_NAME = "Base de référence des espaces protégés français"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CanonicalSha256`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
CanonicalSha256 = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^[0-9a-f]{64}$"),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DeclaredVersion`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
DeclaredVersion = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^(?:0[1-9]|1[0-2])/\d{4}$"),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `StrictPositiveInt`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `StrictNonNegativeInt`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
StrictNonNegativeInt = Annotated[int, Field(strict=True, ge=0)]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_WINDOWS_RESERVED_BASENAMES`

- Category: module constant or closed domain.
- Exact declaration:

```python
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
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
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
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `InpnProtectedAreasDownload`
  - `InpnProtectedAreasExtractedFile`
  - `InpnProtectedAreasExtraction`
  - `InpnProtectedAreasSourceConfig`
  - `InpnProtectedAreasSourceError`
  - `download_inpn_protected_areas_archive`
  - `extract_inpn_protected_areas_archive`
  - `load_inpn_protected_areas_source_config`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `InpnProtectedAreasSourceError`

**Source purpose:** Raised when the pinned INPN source cannot be handled safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_validated_config` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validated_config` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::load_inpn_protected_areas_source_config` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::load_inpn_protected_areas_source_config` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_windows_component_key` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_windows_component_key` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_canonical_member_destination` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_canonical_member_destination` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_validated_zip_members` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validated_zip_members` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_publish_cache_pair` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_publish_cache_pair` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_download_archive_bytes` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_download_archive_bytes` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_inventory` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_inventory` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_publish_extraction_directory` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_publish_extraction_directory` via `InpnProtectedAreasSourceError`
- constructor call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `InpnProtectedAreasSourceError`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `InpnProtectedAreasSourceError`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_source_config_yaml_rejects_duplicate_keys` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_noncanonical_values` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_wrong_download_config_type_has_controlled_error` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_timeout_is_strict_finite_positive` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_cache_setup_failure_is_controlled` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_cold_download_must_match_configured_snapshot_before_publication` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsupported_zip_compression_has_controlled_error` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_publication_failure_restores_old_pair` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_rollback_failure_preserves_recovery_material` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_broken_download_recovery_symlink_is_rejected` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_existing_normal_download_recovery_backup_remains_unchanged` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsafe_zip_member_paths_are_rejected` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_duplicate_or_colliding_zip_destinations_are_rejected` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_zip_links_and_special_files_are_rejected` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_complete_zip_inventory_is_validated_before_member_copy` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_validates_complete_inventory_before_copying` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_first_extraction_publication_failure_leaves_no_half_root` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_replacement_failure_restores_old_tree` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rollback_failure_preserves_backup` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_download_type` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_config_type` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_cache_setup_failure_is_controlled` via `InpnProtectedAreasSourceError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_stale_download_bytes` via `InpnProtectedAreasSourceError`

**Exact class source**

```python
class InpnProtectedAreasSourceError(ValueError):
    """Raised when the pinned INPN source cannot be handled safely."""
```

### `InpnProtectedAreasSourceConfig`

**Source purpose:** Strict identity of one reviewed PatriNat protected-areas snapshot.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `provider` | `Literal['PatriNat']` | `required` | `provider: Literal["PatriNat"]` |
| `authority` | `Literal['MNHN']` | `required` | `authority: Literal["MNHN"]` |
| `program` | `Literal['INPN']` | `required` | `program: Literal["INPN"]` |
| `dataset_id` | `Literal['EP']` | `required` | `dataset_id: Literal["EP"]` |
| `dataset_name` | `Literal['Base de référence des espaces protégés français']` | `required` | `dataset_name: Literal["Base de référence des espaces protégés français"]` |
| `declared_version` | `DeclaredVersion` | `required` | `declared_version: DeclaredVersion` |
| `reference_page_url` | `HttpUrl` | `required` | `reference_page_url: HttpUrl` |
| `archive_url` | `HttpUrl` | `required` | `archive_url: HttpUrl` |
| `archive_filename` | `Literal['EP.zip']` | `required` | `archive_filename: Literal["EP.zip"]` |
| `expected_archive_size_bytes` | `StrictPositiveInt` | `required` | `expected_archive_size_bytes: StrictPositiveInt` |
| `expected_archive_sha256` | `CanonicalSha256` | `required` | `expected_archive_sha256: CanonicalSha256` |
| `cache_root` | `Path` | `required` | `cache_root: Path` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validated_config` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::load_inpn_protected_areas_source_config` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_cache_directory` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_archive_path` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_download_metadata` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `InpnProtectedAreasSourceConfig`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_config` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_session` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download_with_session` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_checked_in_config_loads_with_exact_source_identity` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_invalid_expected_snapshot_integrity` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_cache_setup_failure_is_controlled` via `InpnProtectedAreasSourceConfig`

**Exact class source**

```python
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
    expected_archive_size_bytes: StrictPositiveInt
    expected_archive_sha256: CanonicalSha256
    cache_root: Path

    @model_validator(mode="after")
    def _pinned_official_urls(self) -> Self:
        if str(self.reference_page_url) != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("reference_page_url must be the reviewed PatriNat page")
        if str(self.archive_url) != OFFICIAL_ARCHIVE_URL:
            raise ValueError("archive_url must be the reviewed official EP archive")
        return self
```

### `InpnProtectedAreasDownload`

**Source purpose:** Defines `InpnProtectedAreasDownload`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `provider` | `str` | `required` | `provider: str` |
| `authority` | `str` | `required` | `authority: str` |
| `program` | `str` | `required` | `program: str` |
| `dataset_id` | `str` | `required` | `dataset_id: str` |
| `dataset_name` | `str` | `required` | `dataset_name: str` |
| `declared_version` | `str` | `required` | `declared_version: str` |
| `reference_page_url` | `str` | `required` | `reference_page_url: str` |
| `archive_url` | `str` | `required` | `archive_url: str` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `filename` | `str` | `required` | `filename: str` |
| `file_size` | `int` | `required` | `file_size: int` |
| `sha256` | `str` | `required` | `sha256: str` |
| `path` | `Path` | `required` | `path: Path` |
| `cache_hit` | `bool` | `required` | `cache_hit: bool` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_download_metadata` via `InpnProtectedAreasDownload`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `InpnProtectedAreasDownload`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `InpnProtectedAreasDownload`
- constructor call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `InpnProtectedAreasDownload`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `InpnProtectedAreasDownload`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `InpnProtectedAreasDownload`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `InpnProtectedAreasDownload`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `InpnProtectedAreasDownload`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `InpnProtectedAreasDownload`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download` via `InpnProtectedAreasDownload`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download_with_session` via `InpnProtectedAreasDownload`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download_metadata_path` via `InpnProtectedAreasDownload`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_force_cache_miss` via `InpnProtectedAreasDownload`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_result_schemas_are_factual_inventory_only` via `InpnProtectedAreasDownload`

**Exact class source**

```python
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
```

### `InpnProtectedAreasExtractedFile`

**Source purpose:** Defines `InpnProtectedAreasExtractedFile`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `relative_path` | `str` | `required` | `relative_path: str` |
| `file_size` | `int` | `required` | `file_size: int` |
| `sha256` | `str` | `required` | `sha256: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_inventory` via `InpnProtectedAreasExtractedFile`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_inventory` via `InpnProtectedAreasExtractedFile`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `InpnProtectedAreasExtractedFile`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `InpnProtectedAreasExtractedFile`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `InpnProtectedAreasExtractedFile`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_result_schemas_are_factual_inventory_only` via `InpnProtectedAreasExtractedFile`

**Exact class source**

```python
class InpnProtectedAreasExtractedFile:
    relative_path: str
    file_size: int
    sha256: str
```

### `InpnProtectedAreasExtraction`

**Source purpose:** Defines `InpnProtectedAreasExtraction`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `download` | `InpnProtectedAreasDownload` | `required` | `download: InpnProtectedAreasDownload` |
| `extraction_path` | `Path` | `required` | `extraction_path: Path` |
| `files` | `tuple[InpnProtectedAreasExtractedFile, ...]` | `required` | `files: tuple[InpnProtectedAreasExtractedFile, ...]` |
| `cache_hit` | `bool` | `required` | `cache_hit: bool` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- constructor call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `InpnProtectedAreasExtraction`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `InpnProtectedAreasExtraction`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_extraction_metadata_path` via `InpnProtectedAreasExtraction`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_result_schemas_are_factual_inventory_only` via `InpnProtectedAreasExtraction`

**Exact class source**

```python
class InpnProtectedAreasExtraction:
    download: InpnProtectedAreasDownload
    extraction_path: Path
    files: tuple[InpnProtectedAreasExtractedFile, ...]
    cache_hit: bool
```

### `_DownloadMetadata`

**Source purpose:** Defines `_DownloadMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `schema_version` | `Literal[1]` | `required` | `schema_version: Literal[1]` |
| `provider` | `Literal['PatriNat']` | `required` | `provider: Literal["PatriNat"]` |
| `authority` | `Literal['MNHN']` | `required` | `authority: Literal["MNHN"]` |
| `program` | `Literal['INPN']` | `required` | `program: Literal["INPN"]` |
| `dataset_id` | `Literal['EP']` | `required` | `dataset_id: Literal["EP"]` |
| `dataset_name` | `Literal['Base de référence des espaces protégés français']` | `required` | `dataset_name: Literal["Base de référence des espaces protégés français"]` |
| `declared_version` | `DeclaredVersion` | `required` | `declared_version: DeclaredVersion` |
| `reference_page_url` | `str` | `required` | `reference_page_url: str` |
| `archive_url` | `str` | `required` | `archive_url: str` |
| `filename` | `Literal['EP.zip']` | `required` | `filename: Literal["EP.zip"]` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `file_size` | `StrictPositiveInt` | `required` | `file_size: StrictPositiveInt` |
| `sha256` | `CanonicalSha256` | `required` | `sha256: CanonicalSha256` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.inpn_protected_areas_fr::_download_metadata` via `_DownloadMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_download_metadata` via `_DownloadMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_DownloadMetadata`

**Exact class source**

```python
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
```

### `_ExtractedFileMetadata`

**Source purpose:** Defines `_ExtractedFileMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `relative_path` | `str` | `required` | `relative_path: str` |
| `file_size` | `StrictNonNegativeInt` | `required` | `file_size: StrictNonNegativeInt` |
| `sha256` | `CanonicalSha256` | `required` | `sha256: CanonicalSha256` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.sources.inpn_protected_areas_fr::_ExtractionMetadata._deterministic_files` via `_ExtractedFileMetadata`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `_ExtractedFileMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `_ExtractedFileMetadata`

**Exact class source**

```python
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
```

### `_ExtractionMetadata`

**Source purpose:** Defines `_ExtractionMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `schema_version` | `Literal[1]` | `required` | `schema_version: Literal[1]` |
| `archive_sha256` | `CanonicalSha256` | `required` | `archive_sha256: CanonicalSha256` |
| `archive_size` | `StrictPositiveInt` | `required` | `archive_size: StrictPositiveInt` |
| `files` | `tuple[_ExtractedFileMetadata, ...]` | `Field(min_length=1)` | `files: tuple[_ExtractedFileMetadata, ...] = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `_ExtractionMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `_ExtractionMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `_ExtractionMetadata`

**Exact class source**

```python
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
            raise ValueError(
                "Extraction metadata schema_version must be exact integer 1"
            )
        return value

    @field_validator("files")
    @classmethod
    def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
        paths = tuple(item.relative_path for item in value)
        if paths != tuple(sorted(paths)) or len(set(paths)) != len(paths):
            raise ValueError(
                "Extraction inventory must be unique and lexically ordered"
            )
        return value
```

### `_ValidatedZipMember`

**Source purpose:** Defines `_ValidatedZipMember`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `info` | `zipfile.ZipInfo` | `required` | `info: zipfile.ZipInfo` |
| `destination` | `PurePosixPath` | `required` | `destination: PurePosixPath` |
| `is_directory` | `bool` | `required` | `is_directory: bool` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.inpn_protected_areas_fr::_validated_zip_members` via `_ValidatedZipMember`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validated_zip_members` via `_ValidatedZipMember`

**Exact class source**

```python
class _ValidatedZipMember:
    info: zipfile.ZipInfo
    destination: PurePosixPath
    is_directory: bool
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `InpnProtectedAreasSourceConfig._pinned_official_urls`

**Purpose:** Implements `pinned official urls` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _pinned_official_urls(self) -> Self:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("reference_page_url must be the reviewed PatriNat page")` under lexical guard `str(self.reference_page_url) != OFFICIAL_REFERENCE_PAGE_URL`.
  - `ValueError("archive_url must be the reviewed official EP archive")` under lexical guard `str(self.archive_url) != OFFICIAL_ARCHIVE_URL`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
def _pinned_official_urls(self) -> Self:
        if str(self.reference_page_url) != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("reference_page_url must be the reviewed PatriNat page")
        if str(self.archive_url) != OFFICIAL_ARCHIVE_URL:
            raise ValueError("archive_url must be the reviewed official EP archive")
        return self
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_DownloadMetadata._strict_schema_version`

**Purpose:** Implements `strict schema version` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

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
  - `ValueError("Download metadata schema_version must be exact integer 1")` under lexical guard `type(value) is not int or value != DOWNLOAD_METADATA_SCHEMA_VERSION`.

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
        if type(value) is not int or value != DOWNLOAD_METADATA_SCHEMA_VERSION:
            raise ValueError("Download metadata schema_version must be exact integer 1")
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_DownloadMetadata._exact_reference_page`

**Purpose:** Implements `exact reference page` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _exact_reference_page(cls, value: str) -> str:
```

- Exact decorators: `field_validator("reference_page_url")`, `classmethod`.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cls` | positional-or-keyword | `None` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError("Cached reference page identity differs")` under lexical guard `value != OFFICIAL_REFERENCE_PAGE_URL`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
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
def _exact_reference_page(cls, value: str) -> str:
        if value != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("Cached reference page identity differs")
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_DownloadMetadata._exact_archive_url`

**Purpose:** Implements `exact archive url` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _exact_archive_url(cls, value: str) -> str:
```

- Exact decorators: `field_validator("archive_url")`, `classmethod`.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cls` | positional-or-keyword | `None` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError("Cached archive URL identity differs")` under lexical guard `value != OFFICIAL_ARCHIVE_URL`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
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
def _exact_archive_url(cls, value: str) -> str:
        if value != OFFICIAL_ARCHIVE_URL:
            raise ValueError("Cached archive URL identity differs")
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_DownloadMetadata._aware_utc_timestamp`

**Purpose:** Implements `aware utc timestamp` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _aware_utc_timestamp(cls, value: str) -> str:
```

- Exact decorators: `field_validator("download_timestamp")`, `classmethod`.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cls` | positional-or-keyword | `None` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_utc_timestamp` | `landscout.sources.inpn_protected_areas_fr._validate_utc_timestamp` |
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
def _aware_utc_timestamp(cls, value: str) -> str:
        _validate_utc_timestamp(value)
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_ExtractedFileMetadata._canonical_path`

**Purpose:** Implements `canonical path` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _canonical_path(cls, value: str) -> str:
```

- Exact decorators: `field_validator("relative_path")`, `classmethod`.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cls` | positional-or-keyword | `None` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_inventory_relative_path` | `landscout.sources.inpn_protected_areas_fr._validate_inventory_relative_path` |
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
def _canonical_path(cls, value: str) -> str:
        _validate_inventory_relative_path(value)
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_ExtractionMetadata._strict_schema_version`

**Purpose:** Implements `strict schema version` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

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
  - `ValueError(<br>                "Extraction metadata schema_version must be exact integer 1"<br>            )` under lexical guard `type(value) is not int or value != EXTRACTION_METADATA_SCHEMA_VERSION`.

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
        if type(value) is not int or value != EXTRACTION_METADATA_SCHEMA_VERSION:
            raise ValueError(
                "Extraction metadata schema_version must be exact integer 1"
            )
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_ExtractionMetadata._deterministic_files`

**Purpose:** Implements `deterministic files` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
```

- Exact decorators: `field_validator("files")`, `classmethod`.
- Declared return annotation: `tuple[_ExtractedFileMetadata, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cls` | positional-or-keyword | `None` | `required` |
| `value` | positional-or-keyword | `tuple[_ExtractedFileMetadata, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError(<br>                "Extraction inventory must be unique and lexically ordered"<br>            )` under lexical guard `paths != tuple(sorted(paths)) or len(set(paths)) != len(paths)`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
        paths = tuple(item.relative_path for item in value)
        if paths != tuple(sorted(paths)) or len(set(paths)) != len(paths):
            raise ValueError(
                "Extraction inventory must be unique and lexically ordered"
            )
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_utc_timestamp`

**Purpose:** Implements `validate utc timestamp` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _validate_utc_timestamp(value: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError("download_timestamp must be an exact non-empty string")` under lexical guard `type(value) is not str or not value or value != value.strip()`.
  - `ValueError("download_timestamp must be timezone-aware")` under lexical guard `parsed.tzinfo is None or offset is None`.
  - `ValueError("download_timestamp must use UTC")` under lexical guard `offset.total_seconds() != 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_DownloadMetadata._aware_utc_timestamp` via `_validate_utc_timestamp`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_DownloadMetadata._aware_utc_timestamp` via `_validate_utc_timestamp`
- direct call: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_validate_utc_timestamp`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_validate_utc_timestamp`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `parsed.utcoffset` | `unresolved local/third-party receiver; no ownership inferred` |
| `offset.total_seconds` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_utc_timestamp(value: object) -> None:
    if type(value) is not str or not value or value != value.strip():
        raise ValueError("download_timestamp must be an exact non-empty string")
    parsed = datetime.fromisoformat(value)
    offset = parsed.utcoffset()
    if parsed.tzinfo is None or offset is None:
        raise ValueError("download_timestamp must be timezone-aware")
    if offset.total_seconds() != 0:
        raise ValueError("download_timestamp must use UTC")
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validated_config`

**Purpose:** Implements `validated config` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _validated_config(config: object) -> InpnProtectedAreasSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `InpnProtectedAreasSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `InpnProtectedAreasSourceConfig.model_validate(<br>            config.model_dump(mode="python")<br>        )`
- Explicit raise paths:
  - `InpnProtectedAreasSourceError(<br>            "config must be an exact InpnProtectedAreasSourceConfig"<br>        )` under lexical guard `type(config) is not InpnProtectedAreasSourceConfig`.
  - `InpnProtectedAreasSourceError(<br>            "INPN protected-areas config is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_validated_config`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_validated_config`
- direct call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_validated_config`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_validated_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `InpnProtectedAreasSourceConfig.model_validate` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig.model_validate` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `load_inpn_protected_areas_source_config`

**Purpose:** Load the explicit, version-pinned PatriNat EP source configuration.

**Exact signature**

```python
def load_inpn_protected_areas_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> InpnProtectedAreasSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `InpnProtectedAreasSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `DEFAULT_CONFIG_PATH` |

**Return and exception contract**

- Exact observed return expressions:
  - `InpnProtectedAreasSourceConfig.model_validate(payload)`
- Explicit raise paths:
  - `InpnProtectedAreasSourceError("Config path must be a pathlib Path")` under lexical guard `not isinstance(path, Path)`.
  - `ValueError("Expected a YAML mapping")` under lexical guard `type(payload) is not dict`.
  - `InpnProtectedAreasSourceError(<br>            f"Cannot load INPN protected-areas source config: {path}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_checked_in_config_loads_with_exact_source_identity` via `load_inpn_protected_areas_source_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_checked_in_config_loads_with_exact_source_identity` via `load_inpn_protected_areas_source_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_source_config_yaml_rejects_duplicate_keys` via `load_inpn_protected_areas_source_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_source_config_yaml_rejects_duplicate_keys` via `load_inpn_protected_areas_source_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_loaded_source_config_is_immutable` via `load_inpn_protected_areas_source_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_loaded_source_config_is_immutable` via `load_inpn_protected_areas_source_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_noncanonical_values` via `load_inpn_protected_areas_source_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_noncanonical_values` via `load_inpn_protected_areas_source_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_download_timeout_is_strict_finite_positive` via `load_inpn_protected_areas_source_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_timeout_is_strict_finite_positive` via `load_inpn_protected_areas_source_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceConfig.model_validate` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig.model_validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def load_inpn_protected_areas_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> InpnProtectedAreasSourceConfig:
    """Load the explicit, version-pinned PatriNat EP source configuration."""

    if not isinstance(path, Path):
        raise InpnProtectedAreasSourceError("Config path must be a pathlib Path")
    try:
        payload = loads_strict_yaml(path.read_bytes())
        if type(payload) is not dict:
            raise ValueError("Expected a YAML mapping")
        return InpnProtectedAreasSourceConfig.model_validate(payload)
    except (OSError, TypeError, ValueError, ValidationError) as error:
        raise InpnProtectedAreasSourceError(
            f"Cannot load INPN protected-areas source config: {path}"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_cache_directory`

**Purpose:** Implements `cache directory` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _cache_directory(config: InpnProtectedAreasSourceConfig) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `InpnProtectedAreasSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `config.cache_root / config.dataset_id / version`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_archive_path` via `_cache_directory`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_archive_path` via `_cache_directory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `config.declared_version.replace` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `config.declared_version.replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _cache_directory(config: InpnProtectedAreasSourceConfig) -> Path:
    version = config.declared_version.replace("/", "-")
    return config.cache_root / config.dataset_id / version
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_archive_path`

**Purpose:** Implements `archive path` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _archive_path(config: InpnProtectedAreasSourceConfig) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `InpnProtectedAreasSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_cache_directory(config) / config.archive_filename`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_archive_path`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_archive_path`
- direct call: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_archive_path`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_archive_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_cache_directory` | `landscout.sources.inpn_protected_areas_fr._cache_directory` |

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
def _archive_path(config: InpnProtectedAreasSourceConfig) -> Path:
    return _cache_directory(config) / config.archive_filename
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_metadata_path`

**Purpose:** Implements `metadata path` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _metadata_path(archive_path: Path) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `archive_path.with_name(f"{archive_path.name}.metadata.json")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_metadata_path`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_metadata_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _metadata_path(archive_path: Path) -> Path:
    return archive_path.with_name(f"{archive_path.name}.metadata.json")
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_sha256_file`

**Purpose:** Implements `sha256 file` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _sha256_file(path: Path) -> str:
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
- direct call: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_sha256_file`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_sha256_file`
- direct call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_sha256_file`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_sha256_file`
- direct call: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_sha256_file`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_sha256_file`
- direct call: `landscout.sources.inpn_protected_areas_fr::_inventory` via `_sha256_file`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_inventory` via `_sha256_file`

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
def _sha256_file(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_is_link_or_junction`

**Purpose:** Implements `is link or junction` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

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
- direct call: `landscout.sources.inpn_protected_areas_fr::_is_regular_file` via `_is_link_or_junction`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_is_regular_file` via `_is_link_or_junction`
- direct call: `landscout.sources.inpn_protected_areas_fr::_publish_cache_pair` via `_is_link_or_junction`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_publish_cache_pair` via `_is_link_or_junction`
- direct call: `landscout.sources.inpn_protected_areas_fr::_inventory` via `_is_link_or_junction`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_inventory` via `_is_link_or_junction`
- direct call: `landscout.sources.inpn_protected_areas_fr::_path_exists` via `_is_link_or_junction`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_path_exists` via `_is_link_or_junction`
- direct call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_is_link_or_junction`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_is_link_or_junction`

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

### `_is_regular_file`

**Purpose:** Implements `is regular file` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _is_regular_file(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `not _is_link_or_junction(path) and path.is_file()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_validated_zip_members` via `_is_regular_file`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validated_zip_members` via `_is_regular_file`
- direct call: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_is_regular_file`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_is_regular_file`
- direct call: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_is_regular_file`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_is_regular_file`
- direct call: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `_is_regular_file`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `_is_regular_file`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_link_or_junction` | `landscout.sources.inpn_protected_areas_fr._is_link_or_junction` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _is_regular_file(path: Path) -> bool:
    return not _is_link_or_junction(path) and path.is_file()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_read_strict_json`

**Purpose:** Implements `read strict json` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _read_strict_json(path: Path) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `loads_strict_json_object(path.read_bytes())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_read_strict_json`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_read_strict_json`
- direct call: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `_read_strict_json`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `_read_strict_json`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _read_strict_json(path: Path) -> dict[str, object]:
    return loads_strict_json_object(path.read_bytes())
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_windows_component_key`

**Purpose:** Implements `windows component key` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _windows_component_key(component: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `component` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `normalized.casefold()`
- Explicit raise paths:
  - `InpnProtectedAreasSourceError(<br>            f"Unsafe Windows-compatible ZIP component: {component}"<br>        )` under lexical guard `not normalized<br>        or normalized in {".", ".."}<br>        or normalized != normalized.strip()<br>        or normalized.endswith((" ", "."))<br>        or any(ord(character) < 32 or ord(character) == 127 for character in normalized)<br>        or any(character in '<>:"/\\\|?*' for character in normalized)`.
  - `InpnProtectedAreasSourceError(<br>            f"Reserved Windows device name in ZIP member: {component}"<br>        )` under lexical guard `stem in _WINDOWS_RESERVED_BASENAMES`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_canonical_member_destination` via `_windows_component_key`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_canonical_member_destination` via `_windows_component_key`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `unicodedata.normalize` | `unicodedata.normalize` |
| `normalized.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ord` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `normalized.split(".", 1)[0].casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.split` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.casefold` | `unresolved local/third-party receiver; no ownership inferred` |

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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_canonical_member_destination`

**Purpose:** Implements `canonical member destination` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _canonical_member_destination(name: str) -> tuple[PurePosixPath, tuple[str, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[PurePosixPath, tuple[str, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `PurePosixPath(*parts), canonical`
- Explicit raise paths:
  - `InpnProtectedAreasSourceError("ZIP member name is empty or invalid")` under lexical guard `type(name) is not str or not name or "\x00" in name`.
  - `InpnProtectedAreasSourceError(<br>            "ZIP member name contains control characters"<br>        )` under lexical guard `any(ord(character) < 32 or ord(character) == 127 for character in name)`.
  - `InpnProtectedAreasSourceError(<br>            f"Absolute ZIP member path is unsafe: {name}"<br>        )` under lexical guard `posix.is_absolute() or windows.is_absolute() or bool(windows.drive)`.
  - `InpnProtectedAreasSourceError(f"ZIP member traversal is unsafe: {name}")` under lexical guard `".." in posix.parts`.
  - `InpnProtectedAreasSourceError("ZIP member has no normalized destination")` under lexical guard `not parts`.
  - `InpnProtectedAreasSourceError(<br>            "ZIP member collides with the extraction metadata path"<br>        )` under lexical guard `canonical[0] == EXTRACTION_METADATA_FILENAME.casefold()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_validated_zip_members` via `_canonical_member_destination`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validated_zip_members` via `_canonical_member_destination`
- direct call: `landscout.sources.inpn_protected_areas_fr::_validate_inventory_relative_path` via `_canonical_member_destination`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_inventory_relative_path` via `_canonical_member_destination`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ord` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `name.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `PureWindowsPath` | `pathlib.PureWindowsPath` |
| `posix.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `windows.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_windows_component_key` | `landscout.sources.inpn_protected_areas_fr._windows_component_key` |
| `EXTRACTION_METADATA_FILENAME.casefold` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `name.replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_member_destination(name: str) -> tuple[PurePosixPath, tuple[str, ...]]:
    if type(name) is not str or not name or "\x00" in name:
        raise InpnProtectedAreasSourceError("ZIP member name is empty or invalid")
    if any(ord(character) < 32 or ord(character) == 127 for character in name):
        raise InpnProtectedAreasSourceError(
            "ZIP member name contains control characters"
        )
    posix = PurePosixPath(name.replace("\\", "/"))
    windows = PureWindowsPath(name)
    if posix.is_absolute() or windows.is_absolute() or bool(windows.drive):
        raise InpnProtectedAreasSourceError(
            f"Absolute ZIP member path is unsafe: {name}"
        )
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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validated_zip_members`

**Purpose:** Implements `validated zip members` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _validated_zip_members(path: Path) -> tuple[_ValidatedZipMember, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[_ValidatedZipMember, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(validated)`
- Explicit raise paths:
  - `InpnProtectedAreasSourceError(f"Archive is missing or unsafe: {path}")` under lexical guard `not _is_regular_file(path)`.
  - `InpnProtectedAreasSourceError("Archive is empty or is not a ZIP")` under lexical guard `path.stat().st_size <= 0 or not zipfile.is_zipfile(path)`.
  - `InpnProtectedAreasSourceError("ZIP archive contains no members")` under lexical guard `not infos`.
  - `InpnProtectedAreasSourceError(<br>                        f"duplicate ZIP member name: {name}"<br>                    )` under lexical guard `name in raw_names`.
  - `InpnProtectedAreasSourceError(<br>                        f"Encrypted ZIP members are unsupported: {name}"<br>                    )` under lexical guard `info.flag_bits & 0x1`.
  - `InpnProtectedAreasSourceError(<br>                        f"ZIP symbolic links are forbidden: {name}"<br>                    )` under lexical guard `stat.S_ISLNK(mode)`.
  - `InpnProtectedAreasSourceError(<br>                        f"ZIP special files are forbidden: {name}"<br>                    )` under lexical guard `file_type not in {0, stat.S_IFREG, stat.S_IFDIR}`.
  - `InpnProtectedAreasSourceError(<br>                        "ZIP members collide at one normalized destination: "<br>                        f"{explicit[canonical]} / {name}"<br>                    )` under lexical guard `canonical in explicit`.
  - `InpnProtectedAreasSourceError(<br>                        f"colliding ZIP file/directory destination: {name}"<br>                    )` under lexical guard `any(parent in files for parent in parents)`.
  - `InpnProtectedAreasSourceError(<br>                            f"colliding ZIP file/directory destination: {name}"<br>                        )` under lexical guard `is_directory`.
  - `InpnProtectedAreasSourceError(<br>                            f"colliding ZIP file/directory destination: {name}"<br>                        )` under lexical guard `is_directory`.
  - `InpnProtectedAreasSourceError(<br>                    "ZIP archive contains no regular files"<br>                )` under lexical guard `regular_count == 0`.
  - `InpnProtectedAreasSourceError(f"Corrupt ZIP member: {bad_member}")` under lexical guard `bad_member is not None`.
  - `re-raise`.
  - `InpnProtectedAreasSourceError("Cannot validate ZIP archive")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_validated_zip_members`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_validated_zip_members`
- direct call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_validated_zip_members`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_validated_zip_members`
- direct call: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_validated_zip_members`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `_validated_zip_members`
- direct call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_validated_zip_members`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_validated_zip_members`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_regular_file` | `landscout.sources.inpn_protected_areas_fr._is_regular_file` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `zipfile.is_zipfile` | `zipfile.is_zipfile` |
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `archive.infolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_names.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_member_destination` | `landscout.sources.inpn_protected_areas_fr._canonical_member_destination` |
| `stat.S_ISLNK` | `stat.S_ISLNK` |
| `stat.S_IFMT` | `stat.S_IFMT` |
| `info.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `stat.S_ISDIR` | `stat.S_ISDIR` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `directories.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `files.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `directories.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `validated.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_ValidatedZipMember` | `landscout.sources.inpn_protected_areas_fr._ValidatedZipMember` |
| `archive.testzip` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.stat`<br>`zipfile.is_zipfile`<br>`zipfile.ZipFile`<br>`info.is_dir` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `raw_names.add(name)`<br>`explicit[canonical] = name`<br>`directories.add(canonical)`<br>`files.add(canonical)`<br>`directories.update(parents)`<br>`validated.append(_ValidatedZipMember(info, destination, is_directory))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
                    info.is_dir() or name.endswith(("/", "\\")) or stat.S_ISDIR(mode)
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
                validated.append(_ValidatedZipMember(info, destination, is_directory))
            if regular_count == 0:
                raise InpnProtectedAreasSourceError(
                    "ZIP archive contains no regular files"
                )
            bad_member = archive.testzip()
            if bad_member is not None:
                raise InpnProtectedAreasSourceError(f"Corrupt ZIP member: {bad_member}")
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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_download_metadata`

**Purpose:** Implements `download metadata` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _download_metadata(
    config: InpnProtectedAreasSourceConfig,
    result: InpnProtectedAreasDownload,
) -> _DownloadMetadata:
```

- Exact decorators: none.
- Declared return annotation: `_DownloadMetadata`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `InpnProtectedAreasSourceConfig` | `required` |
| `result` | positional-or-keyword | `InpnProtectedAreasDownload` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_DownloadMetadata(<br>        schema_version=DOWNLOAD_METADATA_SCHEMA_VERSION,<br>        provider=config.provider,<br>        authority=config.authority,<br>        program=config.program,<br>        dataset_id=config.dataset_id,<br>        dataset_name=config.dataset_name,<br>        declared_version=config.declared_version,<br>        reference_page_url=str(config.reference_page_url),<br>        archive_url=str(config.archive_url),<br>        filename=config.archive_filename,<br>        download_timestamp=result.download_timestamp,<br>        file_size=result.file_size,<br>        sha256=result.sha256,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_download_metadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_download_metadata`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_DownloadMetadata` | `landscout.sources.inpn_protected_areas_fr._DownloadMetadata` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_load_cached_download`

**Purpose:** Implements `load cached download` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload | None:
```

- Exact decorators: none.
- Declared return annotation: `InpnProtectedAreasDownload | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `metadata_path` | positional-or-keyword | `Path` | `required` |
| `config` | positional-or-keyword | `InpnProtectedAreasSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `InpnProtectedAreasDownload(<br>            provider=metadata.provider,<br>            authority=metadata.authority,<br>            program=metadata.program,<br>            dataset_id=metadata.dataset_id,<br>            dataset_name=metadata.dataset_name,<br>            declared_version=metadata.declared_version,<br>            reference_page_url=metadata.reference_page_url,<br>            archive_url=metadata.archive_url,<br>            download_timestamp=metadata.download_timestamp,<br>            filename=metadata.filename,<br>            file_size=metadata.file_size,<br>            sha256=metadata.sha256,<br>            path=archive_path,<br>            cache_hit=True,<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_load_cached_download`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_load_cached_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_regular_file` | `landscout.sources.inpn_protected_areas_fr._is_regular_file` |
| `_DownloadMetadata.model_validate` | `landscout.sources.inpn_protected_areas_fr._DownloadMetadata.model_validate` |
| `_read_strict_json` | `landscout.sources.inpn_protected_areas_fr._read_strict_json` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_file` | `landscout.sources.inpn_protected_areas_fr._sha256_file` |
| `_validated_zip_members` | `landscout.sources.inpn_protected_areas_fr._validated_zip_members` |
| `InpnProtectedAreasDownload` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasDownload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256_file` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
        if (
            size != metadata.file_size
            or size != config.expected_archive_size_bytes
            or checksum != metadata.sha256
            or checksum != config.expected_archive_sha256
        ):
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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_replace_file`

**Purpose:** Implements `replace file` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

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
- direct call: `landscout.sources.inpn_protected_areas_fr::_publish_cache_pair` via `_replace_file`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_publish_cache_pair` via `_replace_file`

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

### `_publish_cache_pair`

**Purpose:** Implements `publish cache pair` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

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
  - `InpnProtectedAreasSourceError(<br>            "Cache recovery backup already exists; manual recovery is required"<br>        )` under lexical guard `any(<br>        path.exists() or _is_link_or_junction(path)<br>        for path in (archive_backup, metadata_backup)<br>    )`.
  - `re-raise`.
  - `InpnProtectedAreasSourceError(<br>                "INPN cache publication and rollback both failed"<br>            )`.
  - `InpnProtectedAreasSourceError(<br>            "INPN cache publication failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_publish_cache_pair`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_publish_cache_pair`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_broken_download_recovery_symlink_is_rejected` via `inpn._publish_cache_pair`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_existing_normal_download_recovery_backup_remains_unchanged` via `inpn._publish_cache_pair`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.inpn_protected_areas_fr._is_link_or_junction` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `archive_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `copy2` | `shutil.copy2` |
| `archive_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_file` | `landscout.sources.inpn_protected_areas_fr._replace_file` |
| `archive_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.exists`<br>`archive_path.is_file`<br>`metadata_path.is_file` |
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
    archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    if any(
        path.exists() or _is_link_or_junction(path)
        for path in (archive_backup, metadata_backup)
    ):
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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_download_archive_bytes`

**Purpose:** Implements `download archive bytes` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _download_archive_bytes(
    configured_url: str,
    timeout_seconds: float,
    destination: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `configured_url` | positional-or-keyword | `str` | `required` |
| `timeout_seconds` | positional-or-keyword | `float` | `required` |
| `destination` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `InpnProtectedAreasSourceError("HTTP response headers are invalid")` under lexical guard `not callable(header_get)`.
  - `InpnProtectedAreasSourceError(<br>                    "HTML response cannot be used as a ZIP"<br>                )` under lexical guard `"text/html" in content_type.casefold()`.
  - `re-raise`.
  - `InpnProtectedAreasSourceError(<br>            "Official INPN archive download failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_download_archive_bytes`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `_download_archive_bytes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `callable` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `header_get` | `unresolved local/third-party receiver; no ownership inferred` |
| `content_type.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `destination.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `copyfileobj` | `shutil.copyfileobj` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | `destination.open` |
| Filesystem/archive write or publication | `copyfileobj` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _download_archive_bytes(
    configured_url: str,
    timeout_seconds: float,
    destination: Path,
) -> None:
    try:
        with open_safe_https(
            configured_url,
            timeout=timeout_seconds,
            headers={"User-Agent": "LandScout-AI/0.1"},
        ) as response:
            response_headers = getattr(response, "headers", None)
            header_get = getattr(response_headers, "get", None)
            if not callable(header_get):
                raise InpnProtectedAreasSourceError("HTTP response headers are invalid")
            content_type = str(header_get("Content-Type", ""))
            if "text/html" in content_type.casefold():
                raise InpnProtectedAreasSourceError(
                    "HTML response cannot be used as a ZIP"
                )
            with destination.open("xb") as output:
                copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)
    except InpnProtectedAreasSourceError:
        raise
    except (SafeHttpsError, OSError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            "Official INPN archive download failed"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `download_inpn_protected_areas_archive`

**Purpose:** Download or reuse the exact configured official EP ZIP bytes.

**Exact signature**

```python
def download_inpn_protected_areas_archive(
    config: InpnProtectedAreasSourceConfig,
    *,
    timeout_seconds: float = 120.0,
) -> InpnProtectedAreasDownload:
```

- Exact decorators: none.
- Declared return annotation: `InpnProtectedAreasDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `InpnProtectedAreasSourceConfig` | `required` |
| `timeout_seconds` | keyword-only | `float` | `120.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `cached`
  - `result`
- Explicit raise paths:
  - `InpnProtectedAreasSourceError(<br>            "timeout_seconds must be a strict finite positive number"<br>        )` under lexical guard `isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, Real)`.
  - `InpnProtectedAreasSourceError(<br>            "timeout_seconds must be a strict finite positive number"<br>        )`.
  - `InpnProtectedAreasSourceError(<br>            "timeout_seconds must be a strict finite positive number"<br>        )` under lexical guard `not isfinite(validated_timeout) or validated_timeout <= 0`.
  - `InpnProtectedAreasSourceError(<br>                "Downloaded INPN archive differs from the configured snapshot"<br>            )` under lexical guard `file_size != validated_config.expected_archive_size_bytes<br>            or checksum != validated_config.expected_archive_sha256`.
  - `re-raise`.
  - `InpnProtectedAreasSourceError(<br>            "Official INPN archive download or cache publication failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- direct call: `tests.unit.test_inpn_protected_areas_fr::_download_with_session` via `download_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download_with_session` via `download_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_wrong_download_config_type_has_controlled_error` via `download_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_wrong_download_config_type_has_controlled_error` via `download_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_download_timeout_is_strict_finite_positive` via `download_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_timeout_is_strict_finite_positive` via `download_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_api_has_no_arbitrary_http_session_injection` via `download_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_physical_and_metadata_cache_is_reused` via `download_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_physical_and_metadata_cache_is_reused` via `download_inpn_protected_areas_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_config` | `landscout.sources.inpn_protected_areas_fr._validated_config` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |
| `_archive_path` | `landscout.sources.inpn_protected_areas_fr._archive_path` |
| `_metadata_path` | `landscout.sources.inpn_protected_areas_fr._metadata_path` |
| `_load_cached_download` | `landscout.sources.inpn_protected_areas_fr._load_cached_download` |
| `archive_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_path.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_archive.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_metadata.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `_download_archive_bytes` | `landscout.sources.inpn_protected_areas_fr._download_archive_bytes` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_archive.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_file` | `landscout.sources.inpn_protected_areas_fr._sha256_file` |
| `_validated_zip_members` | `landscout.sources.inpn_protected_areas_fr._validated_zip_members` |
| `InpnProtectedAreasDownload` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasDownload` |
| `datetime.now(UTC).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `_download_metadata` | `landscout.sources.inpn_protected_areas_fr._download_metadata` |
| `temporary_metadata.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata.model_dump_json` | `unresolved local/third-party receiver; no ownership inferred` |
| `_publish_cache_pair` | `landscout.sources.inpn_protected_areas_fr._publish_cache_pair` |
| `temporary_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `temporary_archive.stat` |
| Filesystem/archive write or publication | `archive_path.parent.mkdir`<br>`temporary_archive.unlink`<br>`temporary_metadata.unlink`<br>`temporary_metadata.write_text`<br>`temporary_path.unlink` |
| Hashing/byte identity | `_sha256_file` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def download_inpn_protected_areas_archive(
    config: InpnProtectedAreasSourceConfig,
    *,
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
    archive_path = _archive_path(validated_config)
    metadata_path = _metadata_path(archive_path)
    cached = _load_cached_download(archive_path, metadata_path, validated_config)
    if cached is not None:
        return cached

    temporary_archive = archive_path.with_name(f"{archive_path.name}.part")
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    try:
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_archive.unlink(missing_ok=True)
        temporary_metadata.unlink(missing_ok=True)
        _download_archive_bytes(
            str(validated_config.archive_url),
            validated_timeout,
            temporary_archive,
        )
        file_size = temporary_archive.stat().st_size
        checksum = _sha256_file(temporary_archive)
        if (
            file_size != validated_config.expected_archive_size_bytes
            or checksum != validated_config.expected_archive_sha256
        ):
            raise InpnProtectedAreasSourceError(
                "Downloaded INPN archive differs from the configured snapshot"
            )
        _validated_zip_members(temporary_archive)
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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_download`

**Purpose:** Implements `validate download` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _validate_download(
    download: object,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload:
```

- Exact decorators: none.
- Declared return annotation: `InpnProtectedAreasDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `object` | `required` |
| `config` | positional-or-keyword | `InpnProtectedAreasSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `download`
- Explicit raise paths:
  - `InpnProtectedAreasSourceError(<br>            "download must be an exact InpnProtectedAreasDownload"<br>        )` under lexical guard `type(download) is not InpnProtectedAreasDownload`.
  - `ValueError("Download lineage differs from config")` under lexical guard `any(getattr(download, key) != value for key, value in expected.items())`.
  - `ValueError("Download path differs from configured cache identity")` under lexical guard `not isinstance(download.path, Path) or download.path != _archive_path(<br>            config<br>        )`.
  - `ValueError("Download cache_hit must be boolean")` under lexical guard `type(download.cache_hit) is not bool`.
  - `ValueError("Download integrity scalars are invalid")` under lexical guard `type(download.file_size) is not int<br>            or download.file_size <= 0<br>            or download.file_size != config.expected_archive_size_bytes<br>            or type(download.sha256) is not str<br>            or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None<br>            or download.sha256 != config.expected_archive_sha256`.
  - `ValueError("Downloaded archive path is missing or unsafe")` under lexical guard `not _is_regular_file(download.path)`.
  - `ValueError("Downloaded archive size changed")` under lexical guard `download.path.stat().st_size != download.file_size`.
  - `ValueError("Downloaded archive SHA256 changed")` under lexical guard `_sha256_file(download.path) != download.sha256`.
  - `re-raise`.
  - `InpnProtectedAreasSourceError(<br>            "INPN protected-areas download is stale or invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_validate_download`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_validate_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_archive_path` | `landscout.sources.inpn_protected_areas_fr._archive_path` |
| `re.fullmatch` | `re.fullmatch` |
| `_validate_utc_timestamp` | `landscout.sources.inpn_protected_areas_fr._validate_utc_timestamp` |
| `_is_regular_file` | `landscout.sources.inpn_protected_areas_fr._is_regular_file` |
| `download.path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_file` | `landscout.sources.inpn_protected_areas_fr._sha256_file` |
| `_validated_zip_members` | `landscout.sources.inpn_protected_areas_fr._validated_zip_members` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `download.path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256_file` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
        if not isinstance(download.path, Path) or download.path != _archive_path(
            config
        ):
            raise ValueError("Download path differs from configured cache identity")
        if type(download.cache_hit) is not bool:
            raise ValueError("Download cache_hit must be boolean")
        if (
            type(download.file_size) is not int
            or download.file_size <= 0
            or download.file_size != config.expected_archive_size_bytes
            or type(download.sha256) is not str
            or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
            or download.sha256 != config.expected_archive_sha256
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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_inventory_relative_path`

**Purpose:** Implements `validate inventory relative path` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _validate_inventory_relative_path(value: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError("Inventory relative_path must be an exact non-empty string")` under lexical guard `type(value) is not str or not value or value != value.strip()`.
  - `ValueError("Inventory relative_path is not canonical POSIX form")` under lexical guard `destination.as_posix() != value or value == EXTRACTION_METADATA_FILENAME`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_ExtractedFileMetadata._canonical_path` via `_validate_inventory_relative_path`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_ExtractedFileMetadata._canonical_path` via `_validate_inventory_relative_path`
- direct call: `landscout.sources.inpn_protected_areas_fr::_inventory` via `_validate_inventory_relative_path`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_inventory` via `_validate_inventory_relative_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_member_destination` | `landscout.sources.inpn_protected_areas_fr._canonical_member_destination` |
| `destination.as_posix` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_inventory_relative_path(value: object) -> None:
    if type(value) is not str or not value or value != value.strip():
        raise ValueError("Inventory relative_path must be an exact non-empty string")
    destination, _ = _canonical_member_destination(value)
    if destination.as_posix() != value or value == EXTRACTION_METADATA_FILENAME:
        raise ValueError("Inventory relative_path is not canonical POSIX form")
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_inventory`

**Purpose:** Implements `inventory` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _inventory(root: Path) -> tuple[InpnProtectedAreasExtractedFile, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[InpnProtectedAreasExtractedFile, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(files)`
- Explicit raise paths:
  - `InpnProtectedAreasSourceError(<br>            "Extraction root must be a regular directory"<br>        )` under lexical guard `_is_link_or_junction(root) or not root.is_dir()`.
  - `InpnProtectedAreasSourceError(<br>                f"Extracted link or junction is forbidden: {path}"<br>            )` under lexical guard `_is_link_or_junction(path)`.
  - `InpnProtectedAreasSourceError(<br>                f"Extracted special filesystem entry is forbidden: {path}"<br>            )` under lexical guard `not path.is_file()`.
  - `InpnProtectedAreasSourceError(<br>                f"Cannot inventory extracted file: {relative_path}"<br>            )`.
  - `InpnProtectedAreasSourceError(<br>            "Extracted INPN archive contains no regular files"<br>        )` under lexical guard `not files`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `_inventory`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `_inventory`
- direct call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_inventory`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_inventory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_link_or_junction` | `landscout.sources.inpn_protected_areas_fr._is_link_or_junction` |
| `root.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `root.rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to(root).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_inventory_relative_path` | `landscout.sources.inpn_protected_areas_fr._validate_inventory_relative_path` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_file` | `landscout.sources.inpn_protected_areas_fr._sha256_file` |
| `files.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasExtractedFile` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtractedFile` |
| `files.sort` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.is_dir`<br>`path.is_dir`<br>`path.is_file`<br>`path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256_file` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `files.append(<br>            InpnProtectedAreasExtractedFile(<br>                relative_path=relative_path,<br>                file_size=file_size,<br>                sha256=checksum,<br>            )<br>        )`<br>`files.sort(key=lambda item: item.relative_path)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_extraction_metadata`

**Purpose:** Implements `extraction metadata` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _extraction_metadata(
    download: InpnProtectedAreasDownload,
    files: tuple[InpnProtectedAreasExtractedFile, ...],
) -> _ExtractionMetadata:
```

- Exact decorators: none.
- Declared return annotation: `_ExtractionMetadata`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `InpnProtectedAreasDownload` | `required` |
| `files` | positional-or-keyword | `tuple[InpnProtectedAreasExtractedFile, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_ExtractionMetadata(<br>        schema_version=EXTRACTION_METADATA_SCHEMA_VERSION,<br>        archive_sha256=download.sha256,<br>        archive_size=download.file_size,<br>        files=tuple(<br>            _ExtractedFileMetadata(<br>                relative_path=item.relative_path,<br>                file_size=item.file_size,<br>                sha256=item.sha256,<br>            )<br>            for item in files<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_extraction_metadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_extraction_metadata`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_ExtractionMetadata` | `landscout.sources.inpn_protected_areas_fr._ExtractionMetadata` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_ExtractedFileMetadata` | `landscout.sources.inpn_protected_areas_fr._ExtractedFileMetadata` |

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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_extraction_cache`

**Purpose:** Implements `validate extraction cache` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _validate_extraction_cache(
    root: Path,
    download: InpnProtectedAreasDownload,
) -> tuple[InpnProtectedAreasExtractedFile, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[InpnProtectedAreasExtractedFile, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `download` | positional-or-keyword | `InpnProtectedAreasDownload` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `actual`
- Explicit raise paths:
  - `InpnProtectedAreasSourceError(<br>            "Extraction integrity metadata is missing or unsafe"<br>        )` under lexical guard `not _is_regular_file(marker)`.
  - `ValueError("Extraction metadata archive lineage differs")` under lexical guard `metadata.archive_sha256 != download.sha256<br>            or metadata.archive_size != download.file_size`.
  - `ValueError("Extraction files differ from integrity metadata")` under lexical guard `actual != expected`.
  - `re-raise`.
  - `InpnProtectedAreasSourceError(<br>            "Extraction cache failed physical integrity validation"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_validate_extraction_cache`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_validate_extraction_cache`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_regular_file` | `landscout.sources.inpn_protected_areas_fr._is_regular_file` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `_ExtractionMetadata.model_validate` | `landscout.sources.inpn_protected_areas_fr._ExtractionMetadata.model_validate` |
| `_read_strict_json` | `landscout.sources.inpn_protected_areas_fr._read_strict_json` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasExtractedFile` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtractedFile` |
| `_inventory` | `landscout.sources.inpn_protected_areas_fr._inventory` |

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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_path_exists`

**Purpose:** Implements `path exists` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _path_exists(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path.exists() or path.is_symlink() or _is_link_or_junction(path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_publish_extraction_directory` via `_path_exists`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_publish_extraction_directory` via `_path_exists`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.inpn_protected_areas_fr._is_link_or_junction` |

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
def _path_exists(path: Path) -> bool:
    return path.exists() or path.is_symlink() or _is_link_or_junction(path)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_remove_path`

**Purpose:** Implements `remove path` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _remove_path(path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::_publish_extraction_directory` via `_remove_path`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_publish_extraction_directory` via `_remove_path`
- direct call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_remove_path`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_remove_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.rmdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `shutil.rmtree` | `shutil.rmtree` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file`<br>`path.exists` |
| Filesystem/archive write or publication | `path.rmdir`<br>`path.unlink` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _remove_path(path: Path) -> None:
    if path.is_junction():
        path.rmdir()
    elif path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.exists():
        shutil.rmtree(path)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_replace_directory`

**Purpose:** Implements `replace directory` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _replace_directory(source: Path, target: Path) -> None:
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
- direct call: `landscout.sources.inpn_protected_areas_fr::_publish_extraction_directory` via `_replace_directory`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_publish_extraction_directory` via `_replace_directory`

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
def _replace_directory(source: Path, target: Path) -> None:
    source.replace(target)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_publish_extraction_directory`

**Purpose:** Implements `publish extraction directory` within the file role: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

**Exact signature**

```python
def _publish_extraction_directory(temporary_root: Path, root: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `temporary_root` | positional-or-keyword | `Path` | `required` |
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `InpnProtectedAreasSourceError(<br>            "Extraction recovery backup already exists; manual recovery is required"<br>        )` under lexical guard `_path_exists(backup)`.
  - `InpnProtectedAreasSourceError(<br>                "Cannot stage existing INPN extraction for publication"<br>            )` under lexical guard `_path_exists(root)`.
  - `InpnProtectedAreasSourceError(<br>                "INPN extraction publication and rollback both failed"<br>            )`.
  - `InpnProtectedAreasSourceError(<br>            "INPN extraction publication failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_publish_extraction_directory`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `_publish_extraction_directory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `_path_exists` | `landscout.sources.inpn_protected_areas_fr._path_exists` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `_replace_directory` | `landscout.sources.inpn_protected_areas_fr._replace_directory` |
| `_remove_path` | `landscout.sources.inpn_protected_areas_fr._remove_path` |

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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `extract_inpn_protected_areas_archive`

**Purpose:** Safely extract all regular files and bind an exact factual inventory.

**Exact signature**

```python
def extract_inpn_protected_areas_archive(
    download: InpnProtectedAreasDownload,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasExtraction:
```

- Exact decorators: none.
- Declared return annotation: `InpnProtectedAreasExtraction`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `InpnProtectedAreasDownload` | `required` |
| `config` | positional-or-keyword | `InpnProtectedAreasSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `InpnProtectedAreasExtraction(<br>                download=validated_download,<br>                extraction_path=root,<br>                files=files,<br>                cache_hit=True,<br>            )`
  - `InpnProtectedAreasExtraction(<br>            download=validated_download,<br>            extraction_path=root,<br>            files=files,<br>            cache_hit=False,<br>        )`
- Explicit raise paths:
  - `re-raise`.
  - `InpnProtectedAreasSourceError(<br>            "Cannot safely extract the INPN protected-areas archive"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_validates_complete_inventory_before_copying` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_validates_complete_inventory_before_copying` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_extraction_cache_is_reused` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_extraction_cache_is_reused` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_first_extraction_publication_failure_leaves_no_half_root` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_first_extraction_publication_failure_leaves_no_half_root` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_replacement_failure_restores_old_tree` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_replacement_failure_restores_old_tree` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rollback_failure_preserves_backup` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rollback_failure_preserves_backup` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_download_type` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_download_type` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_config_type` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_config_type` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_cache_setup_failure_is_controlled` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_cache_setup_failure_is_controlled` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_stale_download_bytes` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_stale_download_bytes` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_result_dataclasses_are_frozen` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_result_dataclasses_are_frozen` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_archive_and_extraction_cache_reuse_are_independent` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_archive_and_extraction_cache_reuse_are_independent` via `extract_inpn_protected_areas_archive`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_no_stale_parts_after_download_or_extraction_success` via `extract_inpn_protected_areas_archive`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_no_stale_parts_after_download_or_extraction_success` via `extract_inpn_protected_areas_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_config` | `landscout.sources.inpn_protected_areas_fr._validated_config` |
| `_validate_download` | `landscout.sources.inpn_protected_areas_fr._validate_download` |
| `root.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.inpn_protected_areas_fr._is_link_or_junction` |
| `_validate_extraction_cache` | `landscout.sources.inpn_protected_areas_fr._validate_extraction_cache` |
| `InpnProtectedAreasExtraction` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtraction` |
| `root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `_remove_path` | `landscout.sources.inpn_protected_areas_fr._remove_path` |
| `temporary_root.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `_validated_zip_members` | `landscout.sources.inpn_protected_areas_fr._validated_zip_members` |
| `temporary_root.joinpath` | `unresolved local/third-party receiver; no ownership inferred` |
| `target.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `target.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `target.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `copyfileobj` | `shutil.copyfileobj` |
| `_inventory` | `landscout.sources.inpn_protected_areas_fr._inventory` |
| `_extraction_metadata` | `landscout.sources.inpn_protected_areas_fr._extraction_metadata` |
| `(temporary_root / EXTRACTION_METADATA_FILENAME).write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata.model_dump_json` | `unresolved local/third-party receiver; no ownership inferred` |
| `_publish_extraction_directory` | `landscout.sources.inpn_protected_areas_fr._publish_extraction_directory` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.is_dir`<br>`zipfile.ZipFile`<br>`archive.open`<br>`target.open` |
| Filesystem/archive write or publication | `root.parent.mkdir`<br>`temporary_root.mkdir`<br>`target.mkdir`<br>`target.parent.mkdir`<br>`copyfileobj`<br>`(temporary_root / EXTRACTION_METADATA_FILENAME).write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `DOWNLOAD_METADATA_SCHEMA_VERSION`, `EXTRACTION_METADATA_SCHEMA_VERSION`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `InpnProtectedAreasDownload` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasDownload` |
| `InpnProtectedAreasExtractedFile` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtractedFile` |
| `InpnProtectedAreasExtraction` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasExtraction` |
| `InpnProtectedAreasSourceConfig` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig` |
| `InpnProtectedAreasSourceError` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceError` |
| `download_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.download_inpn_protected_areas_archive` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `load_inpn_protected_areas_source_config` | `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config` |

## 9. Trust, provenance, side effects, and business boundary

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Verified acquisition and factual inventory of the official INPN EP archive.

This source adapter deliberately stops at byte acquisition, safe extraction,
and exact file inventory.  It does not interpret protected-area categories,
open spatial files, intersect parcels, or produce environmental decisions.
"""

from __future__ import annotations

import json
import re
import shutil
import stat
import unicodedata
import zipfile
import zlib
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from math import isfinite
from numbers import Real
from pathlib import Path, PurePosixPath, PureWindowsPath
from shutil import copy2, copyfileobj
from typing import Annotated, Literal, Self

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

from landscout.common.safe_http import SafeHttpsError, open_safe_https
from landscout.common.strict_json import loads_strict_json_object
from landscout.common.strict_yaml import loads_strict_yaml

DEFAULT_CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
DOWNLOAD_METADATA_SCHEMA_VERSION: Literal[1] = 1
EXTRACTION_METADATA_SCHEMA_VERSION: Literal[1] = 1
EXTRACTION_METADATA_FILENAME = ".landscout-extraction.json"

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
    expected_archive_size_bytes: StrictPositiveInt
    expected_archive_sha256: CanonicalSha256
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
            raise ValueError(
                "Extraction metadata schema_version must be exact integer 1"
            )
        return value

    @field_validator("files")
    @classmethod
    def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
        paths = tuple(item.relative_path for item in value)
        if paths != tuple(sorted(paths)) or len(set(paths)) != len(paths):
            raise ValueError(
                "Extraction inventory must be unique and lexically ordered"
            )
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
        payload = loads_strict_yaml(path.read_bytes())
        if type(payload) is not dict:
            raise ValueError("Expected a YAML mapping")
        return InpnProtectedAreasSourceConfig.model_validate(payload)
    except (OSError, TypeError, ValueError, ValidationError) as error:
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


def _read_strict_json(path: Path) -> dict[str, object]:
    return loads_strict_json_object(path.read_bytes())


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
        raise InpnProtectedAreasSourceError(
            "ZIP member name contains control characters"
        )
    posix = PurePosixPath(name.replace("\\", "/"))
    windows = PureWindowsPath(name)
    if posix.is_absolute() or windows.is_absolute() or bool(windows.drive):
        raise InpnProtectedAreasSourceError(
            f"Absolute ZIP member path is unsafe: {name}"
        )
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
                    info.is_dir() or name.endswith(("/", "\\")) or stat.S_ISDIR(mode)
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
                validated.append(_ValidatedZipMember(info, destination, is_directory))
            if regular_count == 0:
                raise InpnProtectedAreasSourceError(
                    "ZIP archive contains no regular files"
                )
            bad_member = archive.testzip()
            if bad_member is not None:
                raise InpnProtectedAreasSourceError(f"Corrupt ZIP member: {bad_member}")
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
        if (
            size != metadata.file_size
            or size != config.expected_archive_size_bytes
            or checksum != metadata.sha256
            or checksum != config.expected_archive_sha256
        ):
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
    if any(
        path.exists() or _is_link_or_junction(path)
        for path in (archive_backup, metadata_backup)
    ):
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


def _download_archive_bytes(
    configured_url: str,
    timeout_seconds: float,
    destination: Path,
) -> None:
    try:
        with open_safe_https(
            configured_url,
            timeout=timeout_seconds,
            headers={"User-Agent": "LandScout-AI/0.1"},
        ) as response:
            response_headers = getattr(response, "headers", None)
            header_get = getattr(response_headers, "get", None)
            if not callable(header_get):
                raise InpnProtectedAreasSourceError("HTTP response headers are invalid")
            content_type = str(header_get("Content-Type", ""))
            if "text/html" in content_type.casefold():
                raise InpnProtectedAreasSourceError(
                    "HTML response cannot be used as a ZIP"
                )
            with destination.open("xb") as output:
                copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)
    except InpnProtectedAreasSourceError:
        raise
    except (SafeHttpsError, OSError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            "Official INPN archive download failed"
        ) from error


def download_inpn_protected_areas_archive(
    config: InpnProtectedAreasSourceConfig,
    *,
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
    archive_path = _archive_path(validated_config)
    metadata_path = _metadata_path(archive_path)
    cached = _load_cached_download(archive_path, metadata_path, validated_config)
    if cached is not None:
        return cached

    temporary_archive = archive_path.with_name(f"{archive_path.name}.part")
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    try:
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_archive.unlink(missing_ok=True)
        temporary_metadata.unlink(missing_ok=True)
        _download_archive_bytes(
            str(validated_config.archive_url),
            validated_timeout,
            temporary_archive,
        )
        file_size = temporary_archive.stat().st_size
        checksum = _sha256_file(temporary_archive)
        if (
            file_size != validated_config.expected_archive_size_bytes
            or checksum != validated_config.expected_archive_sha256
        ):
            raise InpnProtectedAreasSourceError(
                "Downloaded INPN archive differs from the configured snapshot"
            )
        _validated_zip_members(temporary_archive)
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
        if not isinstance(download.path, Path) or download.path != _archive_path(
            config
        ):
            raise ValueError("Download path differs from configured cache identity")
        if type(download.cache_hit) is not bool:
            raise ValueError("Download cache_hit must be boolean")
        if (
            type(download.file_size) is not int
            or download.file_size <= 0
            or download.file_size != config.expected_archive_size_bytes
            or type(download.sha256) is not str
            or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
            or download.sha256 != config.expected_archive_sha256
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
```
