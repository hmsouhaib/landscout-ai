# `src/landscout/sources/inpn_protected_areas_fr.py`

## File identity

- Repository path: `src/landscout/sources/inpn_protected_areas_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: environment source
- Responsibility: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.
- Source SHA256: `2a5933085caf07a56f3afec34404e726fc9c34cff109e0a0697e34ab5d812c20`

## 1. Purpose

Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

## 2. Position in LandScout architecture

This file belongs to the **source adapter** layer and the **environment source** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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
- `from typing import Annotated, Any, Literal, Self`

### Third-party packages

- `import yaml`
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

## 4. Contract taxonomy

### A. Python constants

#### `DEFAULT_CONFIG_PATH`

```python
DEFAULT_CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `DOWNLOAD_CHUNK_SIZE`

```python
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/sources/gpu_fr.py::_sha256` (value argument/reference), `src/landscout/sources/gpu_fr.py::download_gpu_document` (value argument/reference), `src/landscout/sources/gpu_fr.py::extract_gpu_document` (value argument/reference), `src/landscout/sources/ign_bdtopo_fr.py::_calculate_checksums` (value argument/reference), `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` (value argument/reference), `src/landscout/sources/ign_bdtopo_fr.py::_geopackage_integrity` (value argument/reference), `src/landscout/sources/inpn_protected_areas_fr.py::_sha256_file` (value argument/reference), `src/landscout/sources/inpn_protected_areas_fr.py::_download_archive_bytes` (value argument/reference), `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` (value argument/reference), `src/landscout/sources/rte_odre_fr.py::_sha256` (value argument/reference), `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` (value argument/reference).

#### `DOWNLOAD_METADATA_SCHEMA_VERSION`

```python
DOWNLOAD_METADATA_SCHEMA_VERSION: Literal[1] = 1
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/sources/inpn_protected_areas_fr.py::_download_metadata` (value argument/reference).

#### `EXTRACTION_METADATA_SCHEMA_VERSION`

```python
EXTRACTION_METADATA_SCHEMA_VERSION: Literal[1] = 1
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/sources/inpn_protected_areas_fr.py::_extraction_metadata` (value argument/reference).

#### `EXTRACTION_METADATA_FILENAME`

```python
EXTRACTION_METADATA_FILENAME = ".landscout-extraction.json"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `OFFICIAL_REFERENCE_PAGE_URL`

```python
OFFICIAL_REFERENCE_PAGE_URL = (
    "https://www.patrinat.fr/fr/"
    "page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353"
)
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes.

#### `OFFICIAL_ARCHIVE_URL`

```python
OFFICIAL_ARCHIVE_URL = "https://assets.patrinat.fr/files/donnees/ep/EP.zip"
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes.

#### `OFFICIAL_DATASET_NAME`

```python
OFFICIAL_DATASET_NAME = "Base de référence des espaces protégés français"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_WINDOWS_RESERVED_BASENAMES`

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

Module-level technical/source/policy constant consumed by the exact references below.


### B. Type aliases and closed domains

#### `CanonicalSha256`

```python
CanonicalSha256 = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^[0-9a-f]{64}$"),
]
```

Strict lowercase 64-hex SHA256 string used by Pydantic/source-result validation. It is consumed by annotations or Pydantic validation in this module.

#### `DeclaredVersion`

```python
DeclaredVersion = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^(?:0[1-9]|1[0-2])/\d{4}$"),
]
```

Strict MM/YYYY protected-area snapshot version string. It is consumed by annotations or Pydantic validation in this module.

#### `StrictPositiveInt`

```python
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
```

Strict integer greater than zero; Boolean and numeric coercions are rejected by Pydantic Field(strict=True, gt=0). It is consumed by annotations or Pydantic validation in this module.

#### `StrictNonNegativeInt`

```python
StrictNonNegativeInt = Annotated[int, Field(strict=True, ge=0)]
```

Annotated validation alias whose strictness, regex/bounds, and callbacks are exactly those shown above. It is consumed by annotations or Pydantic validation in this module.


### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
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


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `InpnProtectedAreasSourceError`

**Purpose:** Raised when the pinned INPN source cannot be handled safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validated_config` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::load_inpn_protected_areas_source_config` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_windows_component_key` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_canonical_member_destination` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validated_zip_members` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_publish_cache_pair` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_download_archive_bytes` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_download` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_inventory` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_extraction_cache` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_publish_extraction_directory` via `InpnProtectedAreasSourceError`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `InpnProtectedAreasSourceError`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_config_rejects_noncanonical_values` via `pytest.raises(InpnProtectedAreasSourceError)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_wrong_download_config_type_has_controlled_error` via `pytest.raises(InpnProtectedAreasSourceError, match='config|type')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_download_timeout_is_strict_finite_positive` via `pytest.raises(InpnProtectedAreasSourceError, match='timeout')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_download_cache_setup_failure_is_controlled` via `pytest.raises(InpnProtectedAreasSourceError, match='download|cache')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_cold_download_must_match_configured_snapshot_before_publication` via `pytest.raises(InpnProtectedAreasSourceError, match='size|SHA|snapshot|integrity')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `pytest.raises(InpnProtectedAreasSourceError)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_http_and_payload_failures_are_controlled` via `pytest.raises(InpnProtectedAreasSourceError)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_unsupported_zip_compression_has_controlled_error` via `pytest.raises(InpnProtectedAreasSourceError, match='ZIP|archive')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_malformed_response_headers_have_controlled_error` via `pytest.raises(InpnProtectedAreasSourceError, match='response|download')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error` via `pytest.raises(InpnProtectedAreasSourceError, match='response|download')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair` via `pytest.raises(InpnProtectedAreasSourceError, match='publication|download')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `pytest.raises(InpnProtectedAreasSourceError, match='rollback')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_broken_download_recovery_symlink_is_rejected` via `pytest.raises(InpnProtectedAreasSourceError, match='backup|recovery|manual')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_existing_normal_download_recovery_backup_remains_unchanged` via `pytest.raises(InpnProtectedAreasSourceError, match='backup|recovery|manual')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `pytest.raises(InpnProtectedAreasSourceError, match='publication')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_unsafe_zip_member_paths_are_rejected` via `pytest.raises(InpnProtectedAreasSourceError, match='ZIP|archive|member|path')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_duplicate_or_colliding_zip_destinations_are_rejected` via `pytest.raises(InpnProtectedAreasSourceError, match='duplicate|collid|archive')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_zip_links_and_special_files_are_rejected` via `pytest.raises(InpnProtectedAreasSourceError, match=message)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy` via `pytest.raises(InpnProtectedAreasSourceError)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_validates_complete_inventory_before_copying` via `pytest.raises(InpnProtectedAreasSourceError)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_first_extraction_publication_failure_leaves_no_half_root` via `pytest.raises(InpnProtectedAreasSourceError, match='publication')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree` via `pytest.raises(InpnProtectedAreasSourceError, match='publication')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup` via `pytest.raises(InpnProtectedAreasSourceError, match='rollback')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `pytest.raises(InpnProtectedAreasSourceError, match='publication|stage')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_download_type` via `pytest.raises(InpnProtectedAreasSourceError, match='download|type')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_config_type` via `pytest.raises(InpnProtectedAreasSourceError, match='config|type')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_cache_setup_failure_is_controlled` via `pytest.raises(InpnProtectedAreasSourceError, match='extract|cache')`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_stale_download_bytes` via `pytest.raises(InpnProtectedAreasSourceError, match='SHA|size|archive|download')`.
- import/re-export: `tests/unit/test_inpn_protected_areas_fr.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.

**Exact class source**

```python
class InpnProtectedAreasSourceError(ValueError):
    """Raised when the pinned INPN source cannot be handled safely."""
```

### `InpnProtectedAreasSourceConfig`

**Purpose:** Strict identity of one reviewed PatriNat protected-areas snapshot.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `provider` | `provider: Literal["PatriNat"]` | Stores `InpnProtectedAreasSourceConfig`'s `provider` value under exact annotation `Literal['PatriNat']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `authority` | `authority: Literal["MNHN"]` | Stores `InpnProtectedAreasSourceConfig`'s `authority` value under exact annotation `Literal['MNHN']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `program` | `program: Literal["INPN"]` | Stores `InpnProtectedAreasSourceConfig`'s `program` value under exact annotation `Literal['INPN']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `dataset_id` | `dataset_id: Literal["EP"]` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `dataset_name` | `dataset_name: Literal["Base de référence des espaces protégés français"]` | Stores `InpnProtectedAreasSourceConfig`'s `dataset name` value under exact annotation `Literal['Base de référence des espaces protégés français']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `declared_version` | `declared_version: DeclaredVersion` | Stores `InpnProtectedAreasSourceConfig`'s `declared version` value under exact annotation `DeclaredVersion`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `reference_page_url` | `reference_page_url: HttpUrl` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `archive_url` | `archive_url: HttpUrl` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `archive_filename` | `archive_filename: Literal["EP.zip"]` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `expected_archive_size_bytes` | `expected_archive_size_bytes: StrictPositiveInt` | Stores `InpnProtectedAreasSourceConfig`'s `expected archive size bytes` value under exact annotation `StrictPositiveInt`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `expected_archive_sha256` | `expected_archive_sha256: CanonicalSha256` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cache_root` | `cache_root: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |

**Validators (exact source)**

`_pinned_official_urls`:

```python
def _pinned_official_urls(self) -> Self:
        if str(self.reference_page_url) != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("reference_page_url must be the reviewed PatriNat page")
        if str(self.archive_url) != OFFICIAL_ARCHIVE_URL:
            raise ValueError("archive_url must be the reviewed official EP archive")
        return self
```

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.
- import/re-export: `tests/unit/test_inpn_protected_areas_fr.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.

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

**Purpose:** Immutable result/value envelope carrying `provider`, `authority`, `program`, `dataset_id`, `dataset_name`, `declared_version`, `reference_page_url`, `archive_url`, `download_timestamp`, `filename`, `file_size`, `sha256`, `path`, `cache_hit`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `provider` | `provider: str` | Stores `InpnProtectedAreasDownload`'s `provider` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `authority` | `authority: str` | Stores `InpnProtectedAreasDownload`'s `authority` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `program` | `program: str` | Stores `InpnProtectedAreasDownload`'s `program` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `dataset_id` | `dataset_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `dataset_name` | `dataset_name: str` | Stores `InpnProtectedAreasDownload`'s `dataset name` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `declared_version` | `declared_version: str` | Stores `InpnProtectedAreasDownload`'s `declared version` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `reference_page_url` | `reference_page_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `archive_url` | `archive_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `download_timestamp` | `download_timestamp: str` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `filename` | `filename: str` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `file_size` | `file_size: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `path` | `path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `cache_hit` | `cache_hit: bool` | True only when already verified local cache state was reused. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_load_cached_download` via `InpnProtectedAreasDownload`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `InpnProtectedAreasDownload`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_result_schemas_are_factual_inventory_only` via `fields(InpnProtectedAreasDownload)`.
- import/re-export: `tests/unit/test_inpn_protected_areas_fr.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.

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

**Purpose:** Immutable result/value envelope carrying `relative_path`, `file_size`, `sha256`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `relative_path` | `relative_path: str` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `file_size` | `file_size: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_inventory` via `InpnProtectedAreasExtractedFile`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_extraction_cache` via `InpnProtectedAreasExtractedFile`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_result_schemas_are_factual_inventory_only` via `fields(InpnProtectedAreasExtractedFile)`.
- import/re-export: `tests/unit/test_inpn_protected_areas_fr.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.

**Exact class source**

```python
class InpnProtectedAreasExtractedFile:
    relative_path: str
    file_size: int
    sha256: str
```

### `InpnProtectedAreasExtraction`

**Purpose:** Immutable result/value envelope carrying `download`, `extraction_path`, `files`, `cache_hit`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `download` | `download: InpnProtectedAreasDownload` | Stores `InpnProtectedAreasExtraction`'s `download` value under exact annotation `InpnProtectedAreasDownload`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `extraction_path` | `extraction_path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `files` | `files: tuple[InpnProtectedAreasExtractedFile, ...]` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |
| `cache_hit` | `cache_hit: bool` | True only when already verified local cache state was reused. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `InpnProtectedAreasExtraction`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_result_schemas_are_factual_inventory_only` via `fields(InpnProtectedAreasExtraction)`.
- import/re-export: `tests/unit/test_inpn_protected_areas_fr.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.

**Exact class source**

```python
class InpnProtectedAreasExtraction:
    download: InpnProtectedAreasDownload
    extraction_path: Path
    files: tuple[InpnProtectedAreasExtractedFile, ...]
    cache_hit: bool
```

### `_DownloadMetadata`

**Purpose:** Validates the environment source contract carried by `schema_version`, `provider`, `authority`, `program`, `dataset_id`, `dataset_name`, `declared_version`, `reference_page_url`, `archive_url`, `filename`, `download_timestamp`, `file_size`, `sha256`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: Literal[1]` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `provider` | `provider: Literal["PatriNat"]` | Stores `_DownloadMetadata`'s `provider` value under exact annotation `Literal['PatriNat']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `authority` | `authority: Literal["MNHN"]` | Stores `_DownloadMetadata`'s `authority` value under exact annotation `Literal['MNHN']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `program` | `program: Literal["INPN"]` | Stores `_DownloadMetadata`'s `program` value under exact annotation `Literal['INPN']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `dataset_id` | `dataset_id: Literal["EP"]` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `dataset_name` | `dataset_name: Literal["Base de référence des espaces protégés français"]` | Stores `_DownloadMetadata`'s `dataset name` value under exact annotation `Literal['Base de référence des espaces protégés français']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `declared_version` | `declared_version: DeclaredVersion` | Stores `_DownloadMetadata`'s `declared version` value under exact annotation `DeclaredVersion`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `reference_page_url` | `reference_page_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `archive_url` | `archive_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `filename` | `filename: Literal["EP.zip"]` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `download_timestamp` | `download_timestamp: str` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `file_size` | `file_size: StrictPositiveInt` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: CanonicalSha256` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |

**Validators (exact source)**

`_strict_schema_version`:

```python
def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int or value != DOWNLOAD_METADATA_SCHEMA_VERSION:
            raise ValueError("Download metadata schema_version must be exact integer 1")
        return value
```

`_exact_reference_page`:

```python
def _exact_reference_page(cls, value: str) -> str:
        if value != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("Cached reference page identity differs")
        return value
```

`_exact_archive_url`:

```python
def _exact_archive_url(cls, value: str) -> str:
        if value != OFFICIAL_ARCHIVE_URL:
            raise ValueError("Cached archive URL identity differs")
        return value
```

`_aware_utc_timestamp`:

```python
def _aware_utc_timestamp(cls, value: str) -> str:
        _validate_utc_timestamp(value)
        return value
```

**Interface consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_download_metadata` via `_DownloadMetadata`.

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

**Purpose:** Validates the environment source contract carried by `relative_path`, `file_size`, `sha256`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `relative_path` | `relative_path: str` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `file_size` | `file_size: StrictNonNegativeInt` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: CanonicalSha256` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |

**Validators (exact source)**

`_canonical_path`:

```python
def _canonical_path(cls, value: str) -> str:
        _validate_inventory_relative_path(value)
        return value
```

**Interface consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_extraction_metadata` via `_ExtractedFileMetadata`.

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

**Purpose:** Validates the environment source contract carried by `schema_version`, `archive_sha256`, `archive_size`, `files`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: Literal[1]` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `archive_sha256` | `archive_sha256: CanonicalSha256` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `archive_size` | `archive_size: StrictPositiveInt` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `files` | `files: tuple[_ExtractedFileMetadata, ...] = Field(min_length=1)` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |

**Validators (exact source)**

`_strict_schema_version`:

```python
def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int or value != EXTRACTION_METADATA_SCHEMA_VERSION:
            raise ValueError("Extraction metadata schema_version must be exact integer 1")
        return value
```

`_deterministic_files`:

```python
def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
        paths = tuple(item.relative_path for item in value)
        if paths != tuple(sorted(paths)) or len(set(paths)) != len(paths):
            raise ValueError("Extraction inventory must be unique and lexically ordered")
        return value
```

**Interface consumers**

- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_ExtractionMetadata`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_extraction_metadata` via `_ExtractionMetadata`.

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
```

### `_ValidatedZipMember`

**Purpose:** Immutable result/value envelope carrying `info`, `destination`, `is_directory`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `info` | `info: zipfile.ZipInfo` | Stores `_ValidatedZipMember`'s `info` value under exact annotation `zipfile.ZipInfo`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `destination` | `destination: PurePosixPath` | Stores `_ValidatedZipMember`'s `destination` value under exact annotation `PurePosixPath`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `is_directory` | `is_directory: bool` | Boolean `is directory` flag on `_ValidatedZipMember`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |

**Interface consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validated_zip_members` via `_ValidatedZipMember`.

**Exact class source**

```python
class _ValidatedZipMember:
    info: zipfile.ZipInfo
    destination: PurePosixPath
    is_directory: bool
```


## 6. Functions and methods

### `InpnProtectedAreasSourceConfig._pinned_official_urls`

**Exact signature**

```python
def _pinned_official_urls(self) -> Self:
```

**Purpose**

Private `environment source` helper for pinned official urls; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `str(self.reference_page_url) != OFFICIAL_REFERENCE_PAGE_URL`.
- Guard with a raise path: `str(self.archive_url) != OFFICIAL_ARCHIVE_URL`.
- Explicit raise expressions: `ValueError('archive_url must be the reviewed official EP archive')`, `ValueError('reference_page_url must be the reviewed PatriNat page')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_DownloadMetadata._strict_schema_version`

**Exact signature**

```python
def _strict_schema_version(cls, value: object) -> object:
```

**Purpose**

Private `environment source` helper for strict schema version; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `type(value) is not int or value != DOWNLOAD_METADATA_SCHEMA_VERSION`.
- Explicit raise expressions: `ValueError('Download metadata schema_version must be exact integer 1')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int or value != DOWNLOAD_METADATA_SCHEMA_VERSION:
            raise ValueError("Download metadata schema_version must be exact integer 1")
        return value
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_DownloadMetadata._exact_reference_page`

**Exact signature**

```python
def _exact_reference_page(cls, value: str) -> str:
```

**Purpose**

Private `environment source` helper for exact reference page; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `value != OFFICIAL_REFERENCE_PAGE_URL`.
- Explicit raise expressions: `ValueError('Cached reference page identity differs')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _exact_reference_page(cls, value: str) -> str:
        if value != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("Cached reference page identity differs")
        return value
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_DownloadMetadata._exact_archive_url`

**Exact signature**

```python
def _exact_archive_url(cls, value: str) -> str:
```

**Purpose**

Private `environment source` helper for exact archive url; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `value != OFFICIAL_ARCHIVE_URL`.
- Explicit raise expressions: `ValueError('Cached archive URL identity differs')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _exact_archive_url(cls, value: str) -> str:
        if value != OFFICIAL_ARCHIVE_URL:
            raise ValueError("Cached archive URL identity differs")
        return value
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_DownloadMetadata._aware_utc_timestamp`

**Exact signature**

```python
def _aware_utc_timestamp(cls, value: str) -> str:
```

**Purpose**

Private `environment source` helper for aware utc timestamp; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _aware_utc_timestamp(cls, value: str) -> str:
        _validate_utc_timestamp(value)
        return value
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_ExtractedFileMetadata._canonical_path`

**Exact signature**

```python
def _canonical_path(cls, value: str) -> str:
```

**Purpose**

Private `environment source` helper for canonical path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _canonical_path(cls, value: str) -> str:
        _validate_inventory_relative_path(value)
        return value
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_ExtractionMetadata._strict_schema_version`

**Exact signature**

```python
def _strict_schema_version(cls, value: object) -> object:
```

**Purpose**

Private `environment source` helper for strict schema version; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `type(value) is not int or value != EXTRACTION_METADATA_SCHEMA_VERSION`.
- Explicit raise expressions: `ValueError('Extraction metadata schema_version must be exact integer 1')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int or value != EXTRACTION_METADATA_SCHEMA_VERSION:
            raise ValueError("Extraction metadata schema_version must be exact integer 1")
        return value
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_ExtractionMetadata._deterministic_files`

**Exact signature**

```python
def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
```

**Purpose**

Private `environment source` helper for deterministic files; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[_ExtractedFileMetadata, ...]`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `paths != tuple(sorted(paths)) or len(set(paths)) != len(paths)`.
- Explicit raise expressions: `ValueError('Extraction inventory must be unique and lexically ordered')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
        paths = tuple(item.relative_path for item in value)
        if paths != tuple(sorted(paths)) or len(set(paths)) != len(paths):
            raise ValueError("Extraction inventory must be unique and lexically ordered")
        return value
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validate_utc_timestamp`

**Exact signature**

```python
def _validate_utc_timestamp(value: object) -> None:
```

**Purpose**

Rejects malformed or inconsistent utc timestamp; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(value) is not str or not value or value != value.strip()`.
- Guard with a raise path: `parsed.tzinfo is None or offset is None`.
- Guard with a raise path: `offset.total_seconds() != 0`.
- Explicit raise expressions: `ValueError('download_timestamp must be an exact non-empty string')`, `ValueError('download_timestamp must be timezone-aware')`, `ValueError('download_timestamp must use UTC')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_DownloadMetadata._aware_utc_timestamp` via `_validate_utc_timestamp`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_download` via `_validate_utc_timestamp`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validated_config`

**Exact signature**

```python
def _validated_config(config: object) -> InpnProtectedAreasSourceConfig:
```

**Purpose**

Checks and returns canonical config; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `InpnProtectedAreasSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
InpnProtectedAreasSourceConfig.model_validate(config.model_dump(mode='python'))
```

**Validation and exceptions**

- Guard with a raise path: `type(config) is not InpnProtectedAreasSourceConfig`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('INPN protected-areas config is invalid')`, `InpnProtectedAreasSourceError('config must be an exact InpnProtectedAreasSourceConfig')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasSourceConfig.model_validate`, `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_validated_config`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_validated_config`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected` via `_validated_config`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback` via `_validated_config`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate` via `_validated_config`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected` via `_validated_config`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `load_inpn_protected_areas_source_config`

**Exact signature**

```python
def load_inpn_protected_areas_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> InpnProtectedAreasSourceConfig:
```

**Purpose**

Load the explicit, version-pinned PatriNat EP source configuration.

**Return contract**

- Declared return annotation: `InpnProtectedAreasSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
InpnProtectedAreasSourceConfig.model_validate(payload)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(path, Path)`.
- Guard with a raise path: `type(payload) is not dict`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('Config path must be a pathlib Path')`, `InpnProtectedAreasSourceError(f'Cannot load INPN protected-areas source config: {path}')`, `ValueError('Expected a YAML mapping')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasSourceConfig.model_validate`, `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_checked_in_config_loads_with_exact_source_identity` via `load_inpn_protected_areas_source_config`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_config_rejects_noncanonical_values` via `load_inpn_protected_areas_source_config`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_download_timeout_is_strict_finite_positive` via `load_inpn_protected_areas_source_config`.
- import/re-export: `tests/unit/test_inpn_protected_areas_fr.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_cache_directory`

**Exact signature**

```python
def _cache_directory(config: InpnProtectedAreasSourceConfig) -> Path:
```

**Purpose**

Private `environment source` helper for cache directory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
config.cache_root / config.dataset_id / version
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_archive_path` via `_cache_directory`.

**Complete source-ordered implementation**

```python
def _cache_directory(config: InpnProtectedAreasSourceConfig) -> Path:
    version = config.declared_version.replace("/", "-")
    return config.cache_root / config.dataset_id / version
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_archive_path`

**Exact signature**

```python
def _archive_path(config: InpnProtectedAreasSourceConfig) -> Path:
```

**Purpose**

Private `environment source` helper for archive path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
_cache_directory(config) / config.archive_filename
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_archive_path`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_download` via `_archive_path`.

**Complete source-ordered implementation**

```python
def _archive_path(config: InpnProtectedAreasSourceConfig) -> Path:
    return _cache_directory(config) / config.archive_filename
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_metadata_path`

**Exact signature**

```python
def _metadata_path(archive_path: Path) -> Path:
```

**Purpose**

Private `environment source` helper for metadata path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
archive_path.with_name(f'{archive_path.name}.metadata.json')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_metadata_path`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `_metadata_path`.
- direct call or construction: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_path`.

**Complete source-ordered implementation**

```python
def _metadata_path(archive_path: Path) -> Path:
    return archive_path.with_name(f"{archive_path.name}.metadata.json")
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_sha256_file`

**Exact signature**

```python
def _sha256_file(path: Path) -> str:
```

**Purpose**

Private `environment source` helper for sha256 file; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `digest.hexdigest`, `digest.update`, `sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_load_cached_download` via `_sha256_file`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_sha256_file`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_download` via `_sha256_file`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_inventory` via `_sha256_file`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::_require_no_cache_recovery_material` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/cadastre_fr.py::_prepare_temporary_cache_file` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_archive_download` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_require_no_cache_recovery_material` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_prepare_temporary_cache_file` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_inventory` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_extraction_manifest` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_publish_extraction_directory` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validated_spatial_root` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_contained_spatial_path` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_dataset_relative_path` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_is_regular_file` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_publish_cache_pair` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_inventory` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_path_exists` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_require_no_cache_recovery_material` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_prepare_temporary_cache_file` via `_is_link_or_junction`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `_is_link_or_junction`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_linked_spatial_dataset` via `gpu_source_module._is_link_or_junction`.

**Complete source-ordered implementation**

```python
def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_is_regular_file`

**Exact signature**

```python
def _is_regular_file(path: Path) -> bool:
```

**Purpose**

Tests whether regular file; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
not _is_link_or_junction(path) and path.is_file()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validated_zip_members` via `_is_regular_file`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_load_cached_download` via `_is_regular_file`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_download` via `_is_regular_file`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_extraction_cache` via `_is_regular_file`.

**Complete source-ordered implementation**

```python
def _is_regular_file(path: Path) -> bool:
    return not _is_link_or_junction(path) and path.is_file()
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_duplicate_rejecting_object`

**Exact signature**

```python
def _duplicate_rejecting_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
```

**Purpose**

Private `environment source` helper for duplicate rejecting object; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, Any]`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `key in result`.
- Explicit raise expressions: `ValueError(f'Duplicate JSON key: {key}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `result[key]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `src/landscout/sources/inpn_protected_areas_fr.py::_read_strict_json` via `json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_duplicate_rejecting_object)`.

**Complete source-ordered implementation**

```python
def _duplicate_rejecting_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_read_strict_json`

**Exact signature**

```python
def _read_strict_json(path: Path) -> Any:
```

**Purpose**

Reads strict json; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `Any`.
- Every observed return expression is reproduced without truncation:
```python
json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_duplicate_rejecting_object)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.read_text`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_load_cached_download` via `_read_strict_json`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_extraction_cache` via `_read_strict_json`.

**Complete source-ordered implementation**

```python
def _read_strict_json(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_duplicate_rejecting_object,
    )
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_windows_component_key`

**Exact signature**

```python
def _windows_component_key(component: str) -> str:
```

**Purpose**

Private `environment source` helper for windows component key; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
normalized.casefold()
```

**Validation and exceptions**

- Guard with a raise path: `not normalized or normalized in {'.', '..'} or normalized != normalized.strip() or normalized.endswith((' ', '.')) or any((ord(character) < 32 or ord(character) == 127 for character in normalized)) or any((character in '<>:"/\\|?*' for character in normalized))`.
- Guard with a raise path: `stem in _WINDOWS_RESERVED_BASENAMES`.
- Explicit raise expressions: `InpnProtectedAreasSourceError(f'Reserved Windows device name in ZIP member: {component}')`, `InpnProtectedAreasSourceError(f'Unsafe Windows-compatible ZIP component: {component}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_canonical_member_destination` via `_windows_component_key`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_canonical_member_destination`

**Exact signature**

```python
def _canonical_member_destination(name: str) -> tuple[PurePosixPath, tuple[str, ...]]:
```

**Purpose**

Private `environment source` helper for canonical member destination; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[PurePosixPath, tuple[str, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(PurePosixPath(*parts), canonical)
```

**Validation and exceptions**

- Guard with a raise path: `type(name) is not str or not name or '\x00' in name`.
- Guard with a raise path: `any((ord(character) < 32 or ord(character) == 127 for character in name))`.
- Guard with a raise path: `posix.is_absolute() or windows.is_absolute() or bool(windows.drive)`.
- Guard with a raise path: `'..' in posix.parts`.
- Guard with a raise path: `not parts`.
- Guard with a raise path: `canonical[0] == EXTRACTION_METADATA_FILENAME.casefold()`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('ZIP member collides with the extraction metadata path')`, `InpnProtectedAreasSourceError('ZIP member has no normalized destination')`, `InpnProtectedAreasSourceError('ZIP member name contains control characters')`, `InpnProtectedAreasSourceError('ZIP member name is empty or invalid')`, `InpnProtectedAreasSourceError(f'Absolute ZIP member path is unsafe: {name}')`, `InpnProtectedAreasSourceError(f'ZIP member traversal is unsafe: {name}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validated_zip_members` via `_canonical_member_destination`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_inventory_relative_path` via `_canonical_member_destination`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validated_zip_members`

**Exact signature**

```python
def _validated_zip_members(path: Path) -> tuple[_ValidatedZipMember, ...]:
```

**Purpose**

Checks and returns canonical zip members; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[_ValidatedZipMember, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(validated)
```

**Validation and exceptions**

- Guard with a raise path: `not _is_regular_file(path)`.
- Guard with a raise path: `path.stat().st_size <= 0 or not zipfile.is_zipfile(path)`.
- Guard with a raise path: `not infos`.
- Guard with a raise path: `regular_count == 0`.
- Guard with a raise path: `bad_member is not None`.
- Guard with a raise path: `name in raw_names`.
- Guard with a raise path: `info.flag_bits & 1`.
- Guard with a raise path: `stat.S_ISLNK(mode)`.
- Guard with a raise path: `file_type not in {0, stat.S_IFREG, stat.S_IFDIR}`.
- Guard with a raise path: `canonical in explicit`.
- Guard with a raise path: `any((parent in files for parent in parents))`.
- Guard with a raise path: `is_directory`.
- Guard with a raise path: `canonical in files`.
- Guard with a raise path: `canonical in directories`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('Archive is empty or is not a ZIP')`, `InpnProtectedAreasSourceError('Cannot validate ZIP archive')`, `InpnProtectedAreasSourceError('ZIP archive contains no members')`, `InpnProtectedAreasSourceError('ZIP archive contains no regular files')`, `InpnProtectedAreasSourceError(f'Archive is missing or unsafe: {path}')`, `InpnProtectedAreasSourceError(f'Corrupt ZIP member: {bad_member}')`, `InpnProtectedAreasSourceError(f'Encrypted ZIP members are unsupported: {name}')`, `InpnProtectedAreasSourceError(f'ZIP members collide at one normalized destination: {explicit[canonical]} / {name}')`, `InpnProtectedAreasSourceError(f'ZIP special files are forbidden: {name}')`, `InpnProtectedAreasSourceError(f'ZIP symbolic links are forbidden: {name}')`, `InpnProtectedAreasSourceError(f'colliding ZIP file/directory destination: {name}')`, `InpnProtectedAreasSourceError(f'duplicate ZIP member name: {name}')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.stat`, `zipfile.ZipFile`, `zipfile.is_zipfile`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `explicit[canonical]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_load_cached_download` via `_validated_zip_members`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_validated_zip_members`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_download` via `_validated_zip_members`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_validated_zip_members`.

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
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_download_metadata`

**Exact signature**

```python
def _download_metadata(
    config: InpnProtectedAreasSourceConfig,
    result: InpnProtectedAreasDownload,
) -> _DownloadMetadata:
```

**Purpose**

Acquires, verifies, and records metadata; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `_DownloadMetadata`.
- Every observed return expression is reproduced without truncation:
```python
_DownloadMetadata(schema_version=DOWNLOAD_METADATA_SCHEMA_VERSION, provider=config.provider, authority=config.authority, program=config.program, dataset_id=config.dataset_id, dataset_name=config.dataset_name, declared_version=config.declared_version, reference_page_url=str(config.reference_page_url), archive_url=str(config.archive_url), filename=config.archive_filename, download_timestamp=result.download_timestamp, file_size=result.file_size, sha256=result.sha256)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `_DownloadMetadata`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_download_metadata`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_load_cached_download`

**Exact signature**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload | None:
```

**Purpose**

Reads and validates cached download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `InpnProtectedAreasDownload | None`.
- Every observed return expression is reproduced without truncation:
```python
None

InpnProtectedAreasDownload(provider=metadata.provider, authority=metadata.authority, program=metadata.program, dataset_id=metadata.dataset_id, dataset_name=metadata.dataset_name, declared_version=metadata.declared_version, reference_page_url=metadata.reference_page_url, archive_url=metadata.archive_url, download_timestamp=metadata.download_timestamp, filename=metadata.filename, file_size=metadata.file_size, sha256=metadata.sha256, path=archive_path, cache_hit=True)

None

None

None
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `InpnProtectedAreasDownload`, `_DownloadMetadata.model_validate`.
- Filesystem read: `archive_path.stat`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasDownload`.
- Hashing: `_sha256_file`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_load_cached_download`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_load_cached_download`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_load_cached_download`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_load_cached_download`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `inpn._load_cached_download`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_replace_file`

**Exact signature**

```python
def _replace_file(source: Path, target: Path) -> None:
```

**Purpose**

Private `environment source` helper for replace file; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::_publish_cache_pair` via `_replace_file`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_publish_cache_pair` via `_replace_file`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_publish_cache_pair` via `_replace_file`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_publish_cache_pair` via `_replace_file`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_publish_cache_pair` via `_replace_file`.
- property/attribute access: `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `__import__('landscout.sources.cadastre_fr', fromlist=['_replace_file'])._replace_file`.
- property/attribute access: `tests/unit/test_cadastre_fr.py::test_first_metadata_publication_failure_leaves_no_half_pair` via `__import__('landscout.sources.cadastre_fr', fromlist=['_replace_file'])._replace_file`.
- property/attribute access: `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` via `cadastre_fr._replace_file`.
- property/attribute access: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `cadastre_fr._replace_file`.
- property/attribute access: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `cadastre_fr._replace_file`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files` via `gpu._replace_file`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `gpu._replace_file`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `gpu._replace_file`.
- property/attribute access: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `ign_bdtopo_fr._replace_file`.
- property/attribute access: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `ign_bdtopo_fr._replace_file`.
- property/attribute access: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `ign_bdtopo_fr._replace_file`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair` via `inpn._replace_file`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `inpn._replace_file`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `inpn._replace_file`.
- property/attribute access: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `rte_odre_fr._replace_file`.
- property/attribute access: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `rte_odre_fr._replace_file`.
- property/attribute access: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `rte_odre_fr._replace_file`.

**Complete source-ordered implementation**

```python
def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

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

Private `environment source` helper for publish cache pair; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `any((path.exists() or _is_link_or_junction(path) for path in (archive_backup, metadata_backup)))`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('Cache recovery backup already exists; manual recovery is required')`, `InpnProtectedAreasSourceError('INPN cache publication and rollback both failed')`, `InpnProtectedAreasSourceError('INPN cache publication failed')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: `archive_backup.unlink`, `archive_path.unlink`, `metadata_backup.unlink`, `metadata_path.unlink`.
- CRS/geometry calculation: `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_publish_cache_pair`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `_publish_cache_pair`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_publish_cache_pair`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_publish_cache_pair`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_publish_cache_pair`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `gpu._publish_cache_pair`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `gpu._publish_cache_pair`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `gpu._publish_cache_pair`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `gpu._publish_cache_pair`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `ign_bdtopo_fr._publish_cache_pair`.
- property/attribute access: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `ign_bdtopo_fr._publish_cache_pair`.
- direct call or construction: `tests/unit/test_ign_bdtopo_fr.py::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `ign_bdtopo_fr._publish_cache_pair`.
- property/attribute access: `tests/unit/test_ign_bdtopo_fr.py::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `ign_bdtopo_fr._publish_cache_pair`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_broken_download_recovery_symlink_is_rejected` via `inpn._publish_cache_pair`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_broken_download_recovery_symlink_is_rejected` via `inpn._publish_cache_pair`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_existing_normal_download_recovery_backup_remains_unchanged` via `inpn._publish_cache_pair`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_existing_normal_download_recovery_backup_remains_unchanged` via `inpn._publish_cache_pair`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_download_archive_bytes`

**Exact signature**

```python
def _download_archive_bytes(
    configured_url: str,
    timeout_seconds: float,
    destination: Path,
) -> None:
```

**Purpose**

Acquires, verifies, and records archive bytes; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not callable(header_get)`.
- Guard with a raise path: `'text/html' in content_type.casefold()`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('HTML response cannot be used as a ZIP')`, `InpnProtectedAreasSourceError('HTTP response headers are invalid')`, `InpnProtectedAreasSourceError('Official INPN archive download failed')`, `re-raise`.

**Side effects**

- Network I/O: `open_safe_https`.
- Filesystem read: none directly visible.
- Filesystem write: `copyfileobj`.
- CRS/geometry calculation: `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_download_archive_bytes`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `download_inpn_protected_areas_archive`

**Exact signature**

```python
def download_inpn_protected_areas_archive(
    config: InpnProtectedAreasSourceConfig,
    *,
    timeout_seconds: float = 120.0,
) -> InpnProtectedAreasDownload:
```

**Purpose**

Download or reuse the exact configured official EP ZIP bytes.

**Return contract**

- Declared return annotation: `InpnProtectedAreasDownload`.
- Every observed return expression is reproduced without truncation:
```python
cached

result
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, Real)`.
- Guard with a raise path: `not isfinite(validated_timeout) or validated_timeout <= 0`.
- Guard with a raise path: `file_size != validated_config.expected_archive_size_bytes or checksum != validated_config.expected_archive_sha256`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('Downloaded INPN archive differs from the configured snapshot')`, `InpnProtectedAreasSourceError('Official INPN archive download or cache publication failed')`, `InpnProtectedAreasSourceError('timeout_seconds must be a strict finite positive number')`, `re-raise`.

**Side effects**

- Network I/O: `InpnProtectedAreasDownload`, `_download_archive_bytes`, `_download_metadata`, `_load_cached_download`.
- Filesystem read: `temporary_archive.stat`.
- Filesystem write: `archive_path.parent.mkdir`, `temporary_archive.unlink`, `temporary_metadata.unlink`, `temporary_metadata.write_text`, `temporary_path.unlink`.
- CRS/geometry calculation: `InpnProtectedAreasDownload`, `InpnProtectedAreasSourceError`.
- Hashing: `_sha256_file`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::_download_with_session` via `download_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_wrong_download_config_type_has_controlled_error` via `download_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_download_timeout_is_strict_finite_positive` via `download_inpn_protected_areas_archive`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_download_api_has_no_arbitrary_http_session_injection` via `inspect.signature(download_inpn_protected_areas_archive)`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_physical_and_metadata_cache_is_reused` via `download_inpn_protected_areas_archive`.
- import/re-export: `tests/unit/test_inpn_protected_areas_fr.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.

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
    cached = _load_cached_download(
        archive_path, metadata_path, validated_config
    )
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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validate_download`

**Exact signature**

```python
def _validate_download(
    download: object,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload:
```

**Purpose**

Rejects malformed or inconsistent download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `InpnProtectedAreasDownload`.
- Every observed return expression is reproduced without truncation:
```python
download
```

**Validation and exceptions**

- Guard with a raise path: `type(download) is not InpnProtectedAreasDownload`.
- Guard with a raise path: `any((getattr(download, key) != value for key, value in expected.items()))`.
- Guard with a raise path: `not isinstance(download.path, Path) or download.path != _archive_path(config)`.
- Guard with a raise path: `type(download.cache_hit) is not bool`.
- Guard with a raise path: `type(download.file_size) is not int or download.file_size <= 0 or download.file_size != config.expected_archive_size_bytes or (type(download.sha256) is not str) or (re.fullmatch('[0-9a-f]{64}', download.sha256) is None) or (download.sha256 != config.expected_archive_sha256)`.
- Guard with a raise path: `not _is_regular_file(download.path)`.
- Guard with a raise path: `download.path.stat().st_size != download.file_size`.
- Guard with a raise path: `_sha256_file(download.path) != download.sha256`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('INPN protected-areas download is stale or invalid')`, `InpnProtectedAreasSourceError('download must be an exact InpnProtectedAreasDownload')`, `ValueError('Download cache_hit must be boolean')`, `ValueError('Download integrity scalars are invalid')`, `ValueError('Download lineage differs from config')`, `ValueError('Download path differs from configured cache identity')`, `ValueError('Downloaded archive SHA256 changed')`, `ValueError('Downloaded archive path is missing or unsafe')`, `ValueError('Downloaded archive size changed')`, `re-raise`.

**Side effects**

- Network I/O: `download.path.stat`.
- Filesystem read: `download.path.stat`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasSourceError`.
- Hashing: `_sha256_file`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `_validate_download`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_validate_download`.

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
        if not isinstance(download.path, Path) or download.path != _archive_path(config):
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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validate_inventory_relative_path`

**Exact signature**

```python
def _validate_inventory_relative_path(value: object) -> None:
```

**Purpose**

Rejects malformed or inconsistent inventory relative path; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(value) is not str or not value or value != value.strip()`.
- Guard with a raise path: `destination.as_posix() != value or value == EXTRACTION_METADATA_FILENAME`.
- Explicit raise expressions: `ValueError('Inventory relative_path is not canonical POSIX form')`, `ValueError('Inventory relative_path must be an exact non-empty string')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_ExtractedFileMetadata._canonical_path` via `_validate_inventory_relative_path`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_inventory` via `_validate_inventory_relative_path`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_inventory`

**Exact signature**

```python
def _inventory(root: Path) -> tuple[InpnProtectedAreasExtractedFile, ...]:
```

**Purpose**

Private `environment source` helper for inventory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[InpnProtectedAreasExtractedFile, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(files)
```

**Validation and exceptions**

- Guard with a raise path: `_is_link_or_junction(root) or not root.is_dir()`.
- Guard with a raise path: `not files`.
- Guard with a raise path: `_is_link_or_junction(path)`.
- Guard with a raise path: `not path.is_file()`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('Extracted INPN archive contains no regular files')`, `InpnProtectedAreasSourceError('Extraction root must be a regular directory')`, `InpnProtectedAreasSourceError(f'Cannot inventory extracted file: {relative_path}')`, `InpnProtectedAreasSourceError(f'Extracted link or junction is forbidden: {path}')`, `InpnProtectedAreasSourceError(f'Extracted special filesystem entry is forbidden: {path}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.stat`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasExtractedFile`, `InpnProtectedAreasSourceError`.
- Hashing: `_sha256_file`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_extraction_manifest` via `_inventory`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `_inventory`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_validate_extraction_cache` via `_inventory`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_inventory`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_extraction_metadata`

**Exact signature**

```python
def _extraction_metadata(
    download: InpnProtectedAreasDownload,
    files: tuple[InpnProtectedAreasExtractedFile, ...],
) -> _ExtractionMetadata:
```

**Purpose**

Private `environment source` helper for extraction metadata; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_ExtractionMetadata`.
- Every observed return expression is reproduced without truncation:
```python
_ExtractionMetadata(schema_version=EXTRACTION_METADATA_SCHEMA_VERSION, archive_sha256=download.sha256, archive_size=download.file_size, files=tuple((_ExtractedFileMetadata(relative_path=item.relative_path, file_size=item.file_size, sha256=item.sha256) for item in files)))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_extraction_metadata`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validate_extraction_cache`

**Exact signature**

```python
def _validate_extraction_cache(
    root: Path,
    download: InpnProtectedAreasDownload,
) -> tuple[InpnProtectedAreasExtractedFile, ...]:
```

**Purpose**

Rejects malformed or inconsistent extraction cache; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[InpnProtectedAreasExtractedFile, ...]`.
- Every observed return expression is reproduced without truncation:
```python
actual
```

**Validation and exceptions**

- Guard with a raise path: `not _is_regular_file(marker)`.
- Guard with a raise path: `metadata.archive_sha256 != download.sha256 or metadata.archive_size != download.file_size`.
- Guard with a raise path: `actual != expected`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('Extraction cache failed physical integrity validation')`, `InpnProtectedAreasSourceError('Extraction integrity metadata is missing or unsafe')`, `ValueError('Extraction files differ from integrity metadata')`, `ValueError('Extraction metadata archive lineage differs')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasExtractedFile`, `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_validate_extraction_cache`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_path_exists`

**Exact signature**

```python
def _path_exists(path: Path) -> bool:
```

**Purpose**

Private `environment source` helper for path exists; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
path.exists() or path.is_symlink() or _is_link_or_junction(path)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_publish_extraction_directory` via `_path_exists`.

**Complete source-ordered implementation**

```python
def _path_exists(path: Path) -> bool:
    return path.exists() or path.is_symlink() or _is_link_or_junction(path)
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_remove_path`

**Exact signature**

```python
def _remove_path(path: Path) -> None:
```

**Purpose**

Private `environment source` helper for remove path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: `path.rmdir`, `path.unlink`, `shutil.rmtree`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_publish_extraction_directory` via `_remove_path`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_remove_path`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_replace_directory`

**Exact signature**

```python
def _replace_directory(source: Path, target: Path) -> None:
```

**Purpose**

Private `environment source` helper for replace directory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_publish_extraction_directory` via `_replace_directory`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_publish_extraction_directory` via `_replace_directory`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_first_extraction_publication_failure_leaves_no_half_root` via `inpn._replace_directory`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree` via `inpn._replace_directory`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup` via `inpn._replace_directory`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `inpn._replace_directory`.

**Complete source-ordered implementation**

```python
def _replace_directory(source: Path, target: Path) -> None:
    source.replace(target)
```

**Business boundary**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_publish_extraction_directory`

**Exact signature**

```python
def _publish_extraction_directory(temporary_root: Path, root: Path) -> None:
```

**Purpose**

Private `environment source` helper for publish extraction directory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `_path_exists(backup)`.
- Guard with a raise path: `_path_exists(root)`.
- Explicit raise expressions: `InpnProtectedAreasSourceError('Cannot stage existing INPN extraction for publication')`, `InpnProtectedAreasSourceError('Extraction recovery backup already exists; manual recovery is required')`, `InpnProtectedAreasSourceError('INPN extraction publication and rollback both failed')`, `InpnProtectedAreasSourceError('INPN extraction publication failed')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `_publish_extraction_directory`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_publish_extraction_directory`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_publish_extraction_directory`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `extract_inpn_protected_areas_archive`

**Exact signature**

```python
def extract_inpn_protected_areas_archive(
    download: InpnProtectedAreasDownload,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasExtraction:
```

**Purpose**

Safely extract all regular files and bind an exact factual inventory.

**Return contract**

- Declared return annotation: `InpnProtectedAreasExtraction`.
- Every observed return expression is reproduced without truncation:
```python
InpnProtectedAreasExtraction(download=validated_download, extraction_path=root, files=files, cache_hit=False)

InpnProtectedAreasExtraction(download=validated_download, extraction_path=root, files=files, cache_hit=True)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `InpnProtectedAreasSourceError('Cannot safely extract the INPN protected-areas archive')`, `re-raise`.

**Side effects**

- Network I/O: `_validate_download`.
- Filesystem read: `zipfile.ZipFile`.
- Filesystem write: `(temporary_root / EXTRACTION_METADATA_FILENAME).write_text`, `copyfileobj`, `root.parent.mkdir`, `target.mkdir`, `target.parent.mkdir`, `temporary_root.mkdir`.
- CRS/geometry calculation: `InpnProtectedAreasExtraction`, `InpnProtectedAreasSourceError`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_validates_complete_inventory_before_copying` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_extraction_cache_is_reused` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_first_extraction_publication_failure_leaves_no_half_root` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_download_type` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_config_type` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_cache_setup_failure_is_controlled` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_stale_download_bytes` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_result_dataclasses_are_frozen` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_archive_and_extraction_cache_reuse_are_independent` via `extract_inpn_protected_areas_archive`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_no_stale_parts_after_download_or_extraction_success` via `extract_inpn_protected_areas_archive`.
- import/re-export: `tests/unit/test_inpn_protected_areas_fr.py::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `InpnProtectedAreasDownload` | re-exported/defined Python symbol | `defined in `src/landscout/sources/inpn_protected_areas_fr.py`` | yes |
| `InpnProtectedAreasExtractedFile` | re-exported/defined Python symbol | `defined in `src/landscout/sources/inpn_protected_areas_fr.py`` | yes |
| `InpnProtectedAreasExtraction` | re-exported/defined Python symbol | `defined in `src/landscout/sources/inpn_protected_areas_fr.py`` | yes |
| `InpnProtectedAreasSourceConfig` | re-exported/defined Python symbol | `defined in `src/landscout/sources/inpn_protected_areas_fr.py`` | yes |
| `InpnProtectedAreasSourceError` | re-exported/defined Python symbol | `defined in `src/landscout/sources/inpn_protected_areas_fr.py`` | yes |
| `download_inpn_protected_areas_archive` | re-exported/defined Python symbol | `defined in `src/landscout/sources/inpn_protected_areas_fr.py`` | yes |
| `extract_inpn_protected_areas_archive` | re-exported/defined Python symbol | `defined in `src/landscout/sources/inpn_protected_areas_fr.py`` | yes |
| `load_inpn_protected_areas_source_config` | re-exported/defined Python symbol | `defined in `src/landscout/sources/inpn_protected_areas_fr.py`` | yes |

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.

- Configured source identity: exact PatriNat/MNHN/INPN EP 07/2026 metadata, official HTTPS paths, filename, 99,835,011-byte size pin, SHA256 pin, and cache root.
- URL/safe transport: the revalidated configured archive URL uses open_safe_https.
- Physical bytes/cache/archive: current bytes must agree with config pins and strict schema-v1 sidecar; every ZIP member is validated before publication/extraction.
- Extraction: manual exclusive extraction plus schema-v1 marker rescans every regular file/path/size/SHA and rejects links/special/extra/missing/changed files.
- Layer/result/later revalidation: no environmental GIS layer is selected or opened; immutable download/extraction envelopes stop at complete factual file inventory.

## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the environment source flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
