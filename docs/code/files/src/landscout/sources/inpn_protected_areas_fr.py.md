# `src/landscout/sources/inpn_protected_areas_fr.py`

## File identity

- Repository path: `src/landscout/sources/inpn_protected_areas_fr.py`
- File type: Python source
- Primary responsibility: Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.
- Layer / domain: `source adapter` / `environment`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `2a5933085caf07a56f3afec34404e726fc9c34cff109e0a0697e34ab5d812c20`

## 1. Purpose

Acquires the pinned PatriNat/INPN EP archive and safely caches, validates, extracts, and inventories its files.

## 2. Position in LandScout architecture

This file is a `source adapter` artifact in the `environment` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import shutil` — required by the implementation paths and symbols documented below.
- `import unicodedata` — required by the implementation paths and symbols documented below.
- `import zipfile` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from datetime import UTC, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path, PurePosixPath, PureWindowsPath` — required by the implementation paths and symbols documented below.
- `from shutil import copy2, copyfileobj` — required by the implementation paths and symbols documented below.
- `from typing import Annotated, Any, Literal, Self` — required by the implementation paths and symbols documented below.

### Third-party

- `import stat` — required by the implementation paths and symbols documented below.
- `import zlib` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import ( BaseModel, ConfigDict, Field, HttpUrl, StringConstraints, ValidationError, field_validator, model_validator, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.safe_http import SafeHttpsError, open_safe_https` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `DEFAULT_CONFIG_PATH` | `Path("configs/sources/inpn_protected_areas_fr.yaml")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DOWNLOAD_CHUNK_SIZE` | `1024 * 1024` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DOWNLOAD_METADATA_SCHEMA_VERSION` | `1` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXTRACTION_METADATA_SCHEMA_VERSION` | `1` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXTRACTION_METADATA_FILENAME` | `".landscout-extraction.json"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OFFICIAL_REFERENCE_PAGE_URL` | `"https://www.patrinat.fr/fr/" "page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OFFICIAL_ARCHIVE_URL` | `"https://assets.patrinat.fr/files/donnees/ep/EP.zip"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OFFICIAL_DATASET_NAME` | `"Base de référence des espaces protégés français"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_WINDOWS_RESERVED_BASENAMES` | `frozenset( { "con", "prn", "aux", "nul", "clock$", *(f"com{index}" for index in range(1, 10)), *(f"lpt{index}" for index in range(1, 10)), } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `InpnProtectedAreasSourceError`

**Purpose:** Raised when the pinned INPN source cannot be handled safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `InpnProtectedAreasSourceConfig`

**Purpose:** Strict identity of one reviewed PatriNat protected-areas snapshot.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid", frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `provider` | `Literal['PatriNat']` | `required` | `Literal['PatriNat']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `authority` | `Literal['MNHN']` | `required` | `Literal['MNHN']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `program` | `Literal['INPN']` | `required` | `Literal['INPN']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `dataset_id` | `Literal['EP']` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `dataset_name` | `Literal['Base de référence des espaces protégés français']` | `required` | `Literal['Base de référence des espaces protégés français']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `declared_version` | `DeclaredVersion` | `required` | `DeclaredVersion` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `reference_page_url` | `HttpUrl` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `archive_url` | `HttpUrl` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `archive_filename` | `Literal['EP.zip']` | `required` | `Literal['EP.zip']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `expected_archive_size_bytes` | `StrictPositiveInt` | `required` | `StrictPositiveInt` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `expected_archive_sha256` | `CanonicalSha256` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cache_root` | `Path` | `required` | `Path` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_pinned_official_urls` — `def _pinned_official_urls(self) -> Self:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `InpnProtectedAreasDownload`

**Purpose:** Carries an immutable downloaded-source lineage envelope including byte identity and cache status.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `provider` | `str` | `required` | `str` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `authority` | `str` | `required` | `str` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `program` | `str` | `required` | `str` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `dataset_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `dataset_name` | `str` | `required` | `str` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `declared_version` | `str` | `required` | `str` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `reference_page_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `archive_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `download_timestamp` | `str` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `filename` | `str` | `required` | `str` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `file_size` | `int` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `path` | `Path` | `required` | `Path` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache_hit` | `bool` | `required` | Boolean recording whether verified local bytes were reused instead of acquired during this call. |

**Validators and methods:**

- None.

### `InpnProtectedAreasExtractedFile`

**Purpose:** Groups the `InpnProtectedAreasExtractedFile` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `relative_path` | `str` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `file_size` | `int` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |

**Validators and methods:**

- None.

### `InpnProtectedAreasExtraction`

**Purpose:** Carries an immutable extraction envelope binding extracted files to their source archive.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `download` | `InpnProtectedAreasDownload` | `required` | `InpnProtectedAreasDownload` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `extraction_path` | `Path` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `files` | `tuple[InpnProtectedAreasExtractedFile, ...]` | `required` | `tuple[InpnProtectedAreasExtractedFile, ...]` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache_hit` | `bool` | `required` | Boolean recording whether verified local bytes were reused instead of acquired during this call. |

**Validators and methods:**

- None.

### `_DownloadMetadata`

**Purpose:** Carries an immutable downloaded-source lineage envelope including byte identity and cache status.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid", frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `Literal[1]` | `required` | `Literal[1]` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `provider` | `Literal['PatriNat']` | `required` | `Literal['PatriNat']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `authority` | `Literal['MNHN']` | `required` | `Literal['MNHN']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `program` | `Literal['INPN']` | `required` | `Literal['INPN']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `dataset_id` | `Literal['EP']` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `dataset_name` | `Literal['Base de référence des espaces protégés français']` | `required` | `Literal['Base de référence des espaces protégés français']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `declared_version` | `DeclaredVersion` | `required` | `DeclaredVersion` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `reference_page_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `archive_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `filename` | `Literal['EP.zip']` | `required` | `Literal['EP.zip']` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `download_timestamp` | `str` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `file_size` | `StrictPositiveInt` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `CanonicalSha256` | `required` | Lowercase SHA256 binding the exact relevant bytes. |

**Validators and methods:**

- `_strict_schema_version` — `def _strict_schema_version(cls, value: object) -> object:`; decorators `field_validator('schema_version', mode='before'), classmethod`. The complete method algorithm appears in the function/method section.
- `_exact_reference_page` — `def _exact_reference_page(cls, value: str) -> str:`; decorators `field_validator('reference_page_url'), classmethod`. The complete method algorithm appears in the function/method section.
- `_exact_archive_url` — `def _exact_archive_url(cls, value: str) -> str:`; decorators `field_validator('archive_url'), classmethod`. The complete method algorithm appears in the function/method section.
- `_aware_utc_timestamp` — `def _aware_utc_timestamp(cls, value: str) -> str:`; decorators `field_validator('download_timestamp'), classmethod`. The complete method algorithm appears in the function/method section.

### `_ExtractedFileMetadata`

**Purpose:** Represents strict metadata used to reconstruct or validate a byte-bound cache/source object.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid", frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `relative_path` | `str` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `file_size` | `StrictNonNegativeInt` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `CanonicalSha256` | `required` | Lowercase SHA256 binding the exact relevant bytes. |

**Validators and methods:**

- `_canonical_path` — `def _canonical_path(cls, value: str) -> str:`; decorators `field_validator('relative_path'), classmethod`. The complete method algorithm appears in the function/method section.

### `_ExtractionMetadata`

**Purpose:** Carries an immutable extraction envelope binding extracted files to their source archive.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid", frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `Literal[1]` | `required` | `Literal[1]` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `archive_sha256` | `CanonicalSha256` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `archive_size` | `StrictPositiveInt` | `required` | `StrictPositiveInt` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `files` | `tuple[_ExtractedFileMetadata, ...]` | `Field(min_length=1)` | `tuple[_ExtractedFileMetadata, ...]` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_strict_schema_version` — `def _strict_schema_version(cls, value: object) -> object:`; decorators `field_validator('schema_version', mode='before'), classmethod`. The complete method algorithm appears in the function/method section.
- `_deterministic_files` — `def _deterministic_files(         cls, value: tuple[_ExtractedFileMetadata, ...]     ) -> tuple[_ExtractedFileMetadata, ...]:`; decorators `field_validator('files'), classmethod`. The complete method algorithm appears in the function/method section.

### `_ValidatedZipMember`

**Purpose:** Groups the `ValidatedZipMember` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `info` | `zipfile.ZipInfo` | `required` | `zipfile.ZipInfo` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `destination` | `PurePosixPath` | `required` | `PurePosixPath` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `is_directory` | `bool` | `required` | `bool` state used by `src/landscout/sources/inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `InpnProtectedAreasSourceConfig._pinned_official_urls`

**Signature**

```python
def _pinned_official_urls(self) -> Self:
```

**Purpose**

Implements pinned official urls according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `str(self.reference_page_url) != OFFICIAL_REFERENCE_PAGE_URL`. When true: Raises `ValueError('reference_page_url must be the reviewed PatriNat page')`.
2. Checks `str(self.archive_url) != OFFICIAL_ARCHIVE_URL`. When true: Raises `ValueError('archive_url must be the reviewed official EP archive')`.
3. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `str(self.reference_page_url) != OFFICIAL_REFERENCE_PAGE_URL` is true.
- Rejects or diverts the path when `str(self.archive_url) != OFFICIAL_ARCHIVE_URL` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `model_validator`, `str`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_DownloadMetadata._strict_schema_version`

**Signature**

```python
def _strict_schema_version(cls, value: object) -> object:
```

**Purpose**

Implements strict schema version according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `type(value) is not int or value != DOWNLOAD_METADATA_SCHEMA_VERSION`. When true: Raises `ValueError('Download metadata schema_version must be exact integer 1')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `type(value) is not int or value != DOWNLOAD_METADATA_SCHEMA_VERSION` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `field_validator`, `type`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_DownloadMetadata._exact_reference_page`

**Signature**

```python
def _exact_reference_page(cls, value: str) -> str:
```

**Purpose**

Implements exact reference page according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `value != OFFICIAL_REFERENCE_PAGE_URL`. When true: Raises `ValueError('Cached reference page identity differs')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `value != OFFICIAL_REFERENCE_PAGE_URL` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `field_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_DownloadMetadata._exact_archive_url`

**Signature**

```python
def _exact_archive_url(cls, value: str) -> str:
```

**Purpose**

Implements exact archive url according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `value != OFFICIAL_ARCHIVE_URL`. When true: Raises `ValueError('Cached archive URL identity differs')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `value != OFFICIAL_ARCHIVE_URL` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `field_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_DownloadMetadata._aware_utc_timestamp`

**Signature**

```python
def _aware_utc_timestamp(cls, value: str) -> str:
```

**Purpose**

Implements aware utc timestamp according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Calls `_validate_utc_timestamp(value)` for its validation or side effect.
2. Returns `value`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_validate_utc_timestamp`, `field_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_ExtractedFileMetadata._canonical_path`

**Signature**

```python
def _canonical_path(cls, value: str) -> str:
```

**Purpose**

Implements canonical path according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Calls `_validate_inventory_relative_path(value)` for its validation or side effect.
2. Returns `value`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_validate_inventory_relative_path`, `field_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_ExtractionMetadata._strict_schema_version`

**Signature**

```python
def _strict_schema_version(cls, value: object) -> object:
```

**Purpose**

Implements strict schema version according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `type(value) is not int or value != EXTRACTION_METADATA_SCHEMA_VERSION`. When true: Raises `ValueError('Extraction metadata schema_version must be exact integer 1')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `type(value) is not int or value != EXTRACTION_METADATA_SCHEMA_VERSION` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `field_validator`, `type`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_ExtractionMetadata._deterministic_files`

**Signature**

```python
def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
```

**Purpose**

Implements deterministic files according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`tuple[_ExtractedFileMetadata, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[_ExtractedFileMetadata, ...]`. Observed return expression(s): `value`.

**Algorithm**

1. Computes `paths` from `tuple((item.relative_path for item in value))`.
2. Checks `paths != tuple(sorted(paths)) or len(set(paths)) != len(paths)`. When true: Raises `ValueError('Extraction inventory must be unique and lexically ordered')`.
3. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `paths != tuple(sorted(paths)) or len(set(paths)) != len(paths)` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `field_validator`, `len`, `set`, `sorted`, `tuple`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validate_utc_timestamp`

**Signature**

```python
def _validate_utc_timestamp(value: object) -> None:
```

**Purpose**

Validates and rejects malformed utc timestamp according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `type(value) is not str or not value or value != value.strip()`. When true: Raises `ValueError('download_timestamp must be an exact non-empty string')`.
2. Computes `parsed` from `datetime.fromisoformat(value)`.
3. Computes `offset` from `parsed.utcoffset()`.
4. Checks `parsed.tzinfo is None or offset is None`. When true: Raises `ValueError('download_timestamp must be timezone-aware')`.
5. Checks `offset.total_seconds() != 0`. When true: Raises `ValueError('download_timestamp must use UTC')`.

**Validation and invariants**

- Rejects or diverts the path when `type(value) is not str or not value or value != value.strip()` is true.
- Rejects or diverts the path when `parsed.tzinfo is None or offset is None` is true.
- Rejects or diverts the path when `offset.total_seconds() != 0` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `datetime.fromisoformat`, `offset.total_seconds`, `parsed.utcoffset`, `type`, `value.strip`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_DownloadMetadata._aware_utc_timestamp`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validate_download`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validated_config`

**Signature**

```python
def _validated_config(config: object) -> InpnProtectedAreasSourceConfig:
```

**Purpose**

Validates and returns canonical config according to the exact implementation and guards in this file.

**Inputs**

- `config` (`object`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `InpnProtectedAreasSourceConfig`. Observed return expression(s): `InpnProtectedAreasSourceConfig.model_validate(config.model_dump(mode='python'))`.

**Algorithm**

1. Checks `type(config) is not InpnProtectedAreasSourceConfig`. When true: Raises `InpnProtectedAreasSourceError('config must be an exact InpnProtectedAreasSourceConfig')`.
2. Runs guarded operation: Returns `InpnProtectedAreasSourceConfig.model_validate(config.model_dump(mode='python'))`. Handles `(AttributeError, TypeError, ValueError, ValidationError)`.

**Validation and invariants**

- Rejects or diverts the path when `type(config) is not InpnProtectedAreasSourceConfig` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `InpnProtectedAreasSourceConfig.model_validate`, `InpnProtectedAreasSourceError`, `config.model_dump`, `type`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `download_inpn_protected_areas_archive`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `extract_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `load_inpn_protected_areas_source_config`

**Signature**

```python
def load_inpn_protected_areas_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> InpnProtectedAreasSourceConfig:
```

**Purpose**

Load the explicit, version-pinned PatriNat EP source configuration.

**Inputs**

- `path` (`Path`; optional/default `DEFAULT_CONFIG_PATH`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `InpnProtectedAreasSourceConfig`. Observed return expression(s): `InpnProtectedAreasSourceConfig.model_validate(payload)`.

**Algorithm**

1. Checks `not isinstance(path, Path)`. When true: Raises `InpnProtectedAreasSourceError('Config path must be a pathlib Path')`.
2. Runs guarded operation: Enters managed context(s) `path.open(encoding='utf-8')` and executes: Computes `payload` from `yaml.safe_load(stream)`. Checks `type(payload) is not dict`. When true: Raises `ValueError('Expected a YAML mapping')`. Returns `InpnProtectedAreasSourceConfig.model_validate(payload)`. Handles `(OSError, TypeError, ValueError, ValidationError, yaml.YAMLError)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(path, Path)` is true.
- Rejects or diverts the path when `type(payload) is not dict` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `InpnProtectedAreasSourceConfig.model_validate`, `InpnProtectedAreasSourceError`, `ValueError`, `isinstance`, `path.open`, `type`, `yaml.safe_load`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `test_checked_in_config_loads_with_exact_source_identity`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_config_rejects_noncanonical_values`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_download_timeout_is_strict_finite_positive`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_checked_in_config_loads_with_exact_source_identity`
- `tests/unit/test_inpn_protected_areas_fr.py::test_config_rejects_noncanonical_values`
- `tests/unit/test_inpn_protected_areas_fr.py::test_download_timeout_is_strict_finite_positive`

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_cache_directory`

**Signature**

```python
def _cache_directory(config: InpnProtectedAreasSourceConfig) -> Path:
```

**Purpose**

Implements cache directory according to the exact implementation and guards in this file.

**Inputs**

- `config` (`InpnProtectedAreasSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `config.cache_root / config.dataset_id / version`.

**Algorithm**

1. Computes `version` from `config.declared_version.replace('/', '-')`.
2. Returns `config.cache_root / config.dataset_id / version`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `config.declared_version.replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `config.declared_version.replace`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_archive_path`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_archive_path`

**Signature**

```python
def _archive_path(config: InpnProtectedAreasSourceConfig) -> Path:
```

**Purpose**

Implements archive path according to the exact implementation and guards in this file.

**Inputs**

- `config` (`InpnProtectedAreasSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `_cache_directory(config) / config.archive_filename`.

**Algorithm**

1. Returns `_cache_directory(config) / config.archive_filename`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_cache_directory`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validate_download`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `download_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_metadata_path`

**Signature**

```python
def _metadata_path(archive_path: Path) -> Path:
```

**Purpose**

Implements metadata path according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `archive_path.with_name(f'{archive_path.name}.metadata.json')`.

**Algorithm**

1. Returns `archive_path.with_name(f'{archive_path.name}.metadata.json')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `archive_path.with_name`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `download_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_sha256_file`

**Signature**

```python
def _sha256_file(path: Path) -> str:
```

**Purpose**

Implements sha256 file according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `digest.hexdigest()`.

**Algorithm**

1. Computes `digest` from `sha256()`.
2. Enters managed context(s) `path.open('rb')` and executes: Iterates `chunk` over `iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b'')`. For each value: Calls `digest.update(chunk)` for its validation or side effect.
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

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_inventory`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_load_cached_download`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validate_download`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `download_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

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

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_inventory`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_is_regular_file`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_path_exists`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_publish_cache_pair`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `extract_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_is_regular_file`

**Signature**

```python
def _is_regular_file(path: Path) -> bool:
```

**Purpose**

Returns whether `regular file` satisfies the exact predicates and branches listed below.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `not _is_link_or_junction(path) and path.is_file()`.

**Algorithm**

1. Returns `not _is_link_or_junction(path) and path.is_file()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_is_link_or_junction`, `path.is_file`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_load_cached_download`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validate_download`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validate_extraction_cache`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validated_zip_members`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_duplicate_rejecting_object`

**Signature**

```python
def _duplicate_rejecting_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
```

**Purpose**

Implements duplicate rejecting object according to the exact implementation and guards in this file.

**Inputs**

- `pairs` (`list[tuple[str, Any]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, Any]`. Observed return expression(s): `result`.

**Algorithm**

1. Defines `result` with annotation `dict[str, Any]` from `{}`.
2. Iterates `(key, value)` over `pairs`. For each value: Checks `key in result`. When true: Raises `ValueError(f'Duplicate JSON key: {key}')`. Computes `result[key]` from `value`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `key in result` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_read_strict_json`

**Signature**

```python
def _read_strict_json(path: Path) -> Any:
```

**Purpose**

Reads and validates strict json according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Any`. Observed return expression(s): `json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_duplicate_rejecting_object)`.

**Algorithm**

1. Returns `json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_duplicate_rejecting_object)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `json.loads`, `path.read_text`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_load_cached_download`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validate_extraction_cache`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_windows_component_key`

**Signature**

```python
def _windows_component_key(component: str) -> str:
```

**Purpose**

Implements windows component key according to the exact implementation and guards in this file.

**Inputs**

- `component` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `normalized.casefold()`.

**Algorithm**

1. Computes `normalized` from `unicodedata.normalize('NFKC', component)`.
2. Checks `not normalized or normalized in {'.', '..'} or normalized != normalized.strip() or normalized.endswith((' ', '.')) or any((ord(character) < 32 or ord(character) == 127 for character in normalized)) or any((character in '<>:"/\\|?*' for character in normalized))`. When true: Raises `InpnProtectedAreasSourceError(f'Unsafe Windows-compatible ZIP component: {component}')`.
3. Computes `stem` from `normalized.split('.', 1)[0].casefold()`.
4. Checks `stem in _WINDOWS_RESERVED_BASENAMES`. When true: Raises `InpnProtectedAreasSourceError(f'Reserved Windows device name in ZIP member: {component}')`.
5. Returns `normalized.casefold()`.

**Validation and invariants**

- Rejects or diverts the path when `not normalized or normalized in {'.', '..'} or normalized != normalized.strip() or normalized.endswith((' ', '.')) or any((ord(character) < 32 or ord(character) == 127 for character in normalized)) or any((character in '<>:"/\\|?*' for character in normalized))` is true.
- Rejects or diverts the path when `stem in _WINDOWS_RESERVED_BASENAMES` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `InpnProtectedAreasSourceError`, `any`, `normalized.casefold`, `normalized.endswith`, `normalized.split`, `normalized.split('.', 1)[0].casefold`, `normalized.strip`, `ord`, `unicodedata.normalize`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_canonical_member_destination`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_canonical_member_destination`

**Signature**

```python
def _canonical_member_destination(name: str) -> tuple[PurePosixPath, tuple[str, ...]]:
```

**Purpose**

Implements canonical member destination according to the exact implementation and guards in this file.

**Inputs**

- `name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[PurePosixPath, tuple[str, ...]]`. Observed return expression(s): `(PurePosixPath(*parts), canonical)`.

**Algorithm**

1. Checks `type(name) is not str or not name or '\x00' in name`. When true: Raises `InpnProtectedAreasSourceError('ZIP member name is empty or invalid')`.
2. Checks `any((ord(character) < 32 or ord(character) == 127 for character in name))`. When true: Raises `InpnProtectedAreasSourceError('ZIP member name contains control characters')`.
3. Computes `posix` from `PurePosixPath(name.replace('\\', '/'))`.
4. Computes `windows` from `PureWindowsPath(name)`.
5. Checks `posix.is_absolute() or windows.is_absolute() or bool(windows.drive)`. When true: Raises `InpnProtectedAreasSourceError(f'Absolute ZIP member path is unsafe: {name}')`.
6. Checks `'..' in posix.parts`. When true: Raises `InpnProtectedAreasSourceError(f'ZIP member traversal is unsafe: {name}')`.
7. Computes `parts` from `tuple((part for part in posix.parts if part not in {'', '.'}))`.
8. Checks `not parts`. When true: Raises `InpnProtectedAreasSourceError('ZIP member has no normalized destination')`.
9. Computes `canonical` from `tuple((_windows_component_key(part) for part in parts))`.
10. Checks `canonical[0] == EXTRACTION_METADATA_FILENAME.casefold()`. When true: Raises `InpnProtectedAreasSourceError('ZIP member collides with the extraction metadata path')`.
11. Returns `(PurePosixPath(*parts), canonical)`.

**Validation and invariants**

- Rejects or diverts the path when `type(name) is not str or not name or '\x00' in name` is true.
- Rejects or diverts the path when `any((ord(character) < 32 or ord(character) == 127 for character in name))` is true.
- Rejects or diverts the path when `posix.is_absolute() or windows.is_absolute() or bool(windows.drive)` is true.
- Rejects or diverts the path when `'..' in posix.parts` is true.
- Rejects or diverts the path when `not parts` is true.
- Rejects or diverts the path when `canonical[0] == EXTRACTION_METADATA_FILENAME.casefold()` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `name.replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `EXTRACTION_METADATA_FILENAME.casefold`, `InpnProtectedAreasSourceError`, `PurePosixPath`, `PureWindowsPath`, `_windows_component_key`, `any`, `bool`, `name.replace`, `ord`, `posix.is_absolute`, `tuple`, `type`, `windows.is_absolute`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validate_inventory_relative_path`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validated_zip_members`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validated_zip_members`

**Signature**

```python
def _validated_zip_members(path: Path) -> tuple[_ValidatedZipMember, ...]:
```

**Purpose**

Validates and returns canonical zip members according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[_ValidatedZipMember, ...]`. Observed return expression(s): `tuple(validated)`.

**Algorithm**

1. Checks `not _is_regular_file(path)`. When true: Raises `InpnProtectedAreasSourceError(f'Archive is missing or unsafe: {path}')`.
2. Runs guarded operation: Checks `path.stat().st_size <= 0 or not zipfile.is_zipfile(path)`. When true: Raises `InpnProtectedAreasSourceError('Archive is empty or is not a ZIP')`. Enters managed context(s) `zipfile.ZipFile(path)` and executes: Computes `infos` from `archive.infolist()`. Checks `not infos`. When true: Raises `InpnProtectedAreasSourceError('ZIP archive contains no members')`. Defines `raw_names` with annotation `set[str]` from `set()`. Defines `explicit` with annotation `dict[tuple[str, ...], str]` from `{}`. Executes 9 additional source-ordered statement(s). Handles `InpnProtectedAreasSourceError`, `(NotImplementedError, OSError, RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error)`.

**Validation and invariants**

- Rejects or diverts the path when `not _is_regular_file(path)` is true.
- Rejects or diverts the path when `path.stat().st_size <= 0 or not zipfile.is_zipfile(path)` is true.
- Rejects or diverts the path when `not infos` is true.
- Rejects or diverts the path when `regular_count == 0` is true.
- Rejects or diverts the path when `bad_member is not None` is true.
- Rejects or diverts the path when `name in raw_names` is true.
- Rejects or diverts the path when `info.flag_bits & 1` is true.
- Rejects or diverts the path when `stat.S_ISLNK(mode)` is true.
- Rejects or diverts the path when `file_type not in {0, stat.S_IFREG, stat.S_IFDIR}` is true.
- Rejects or diverts the path when `canonical in explicit` is true.
- Rejects or diverts the path when `any((parent in files for parent in parents))` is true.
- Rejects or diverts the path when `is_directory` is true.
- Rejects or diverts the path when `canonical in files` is true.
- Rejects or diverts the path when `canonical in directories` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `InpnProtectedAreasSourceError`, `_ValidatedZipMember`, `_canonical_member_destination`, `_is_regular_file`, `any`, `archive.infolist`, `archive.testzip`, `directories.add`, `directories.update`, `files.add`, `info.is_dir`, `len`, `name.endswith`, `path.stat`, `range`, `raw_names.add`, `set`, `stat.S_IFMT`, `stat.S_ISDIR`, `stat.S_ISLNK`, `tuple`, `validated.append`, `zipfile.ZipFile`, `zipfile.is_zipfile`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_load_cached_download`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validate_download`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `download_inpn_protected_areas_archive`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `extract_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_download_metadata`

**Signature**

```python
def _download_metadata(
    config: InpnProtectedAreasSourceConfig,
    result: InpnProtectedAreasDownload,
) -> _DownloadMetadata:
```

**Purpose**

Downloads and validates metadata according to the exact implementation and guards in this file.

**Inputs**

- `config` (`InpnProtectedAreasSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`InpnProtectedAreasDownload`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_DownloadMetadata`. Observed return expression(s): `_DownloadMetadata(schema_version=DOWNLOAD_METADATA_SCHEMA_VERSION, provider=config.provider, authority=config.authority, program=config.program, dataset_id=config.dataset_id, dataset_name=config.dataset_name, declared_version=config.declared_version, reference_page_url=str(config.reference_page_url), archive_url=str(config.archive_url), filename=config.archive_filename, download_timestamp=result.…`.

**Algorithm**

1. Returns `_DownloadMetadata(schema_version=DOWNLOAD_METADATA_SCHEMA_VERSION, provider=config.provider, authority=config.authority, program=config.program, dataset_id=config.dataset_id, dataset_name=config.dataset_name, declared_version=config.declared_version, reference_page_url=str(config.reference_page_url), archive_url=str(config.archive_url), filename=config.arch…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_DownloadMetadata`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_DownloadMetadata`, `str`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `download_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_load_cached_download`

**Signature**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload | None:
```

**Purpose**

Loads cached download according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`InpnProtectedAreasSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `InpnProtectedAreasDownload | None`. Observed return expression(s): `None`; `InpnProtectedAreasDownload(provider=metadata.provider, authority=metadata.authority, program=metadata.program, dataset_id=metadata.dataset_id, dataset_name=metadata.dataset_name, declared_version=metadata.declared_version, reference_page_url=metadata.reference_page_url, archive_url=metadata.archive_url, download_timestamp=metadata.download_timestamp, filename=metadata.filename, file_size=metadata…`.

**Algorithm**

1. Checks `not _is_regular_file(archive_path) or not _is_regular_file(metadata_path)`. When true: Returns `None`.
2. Runs guarded operation: Computes `metadata` from `_DownloadMetadata.model_validate(_read_strict_json(metadata_path))`. Computes `expected` from `{'provider': config.provider, 'authority': config.authority, 'program': config.program, 'dataset_id': config.dataset_id, 'dataset_name': config.dataset_name, 'declared_version': config.declared_version, 'reference_page_url': str(config.reference_page_url), 'archive_url': str(config.archive_url), 'filename': config.arc…`. Checks `any((getattr(metadata, key) != value for key, value in expected.items()))`. When true: Returns `None`. Computes `size` from `archive_path.stat().st_size`. Executes 4 additional source-ordered statement(s). Handles `(InpnProtectedAreasSourceError, OSError, TypeError, ValueError, ValidationError, json.JSONDecodeError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `InpnProtectedAreasDownload`, `_DownloadMetadata.model_validate`, `_read_strict_json`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `InpnProtectedAreasDownload`, `_DownloadMetadata.model_validate`, `_is_regular_file`, `_read_strict_json`, `_sha256_file`, `_validated_zip_members`, `any`, `archive_path.stat`, `expected.items`, `getattr`, `str`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `download_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

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

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_publish_cache_pair`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

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

1. Computes `archive_backup` from `archive_path.with_name(f'{archive_path.name}.bak')`.
2. Computes `metadata_backup` from `metadata_path.with_name(f'{metadata_path.name}.bak')`.
3. Checks `any((path.exists() or _is_link_or_junction(path) for path in (archive_backup, metadata_backup)))`. When true: Raises `InpnProtectedAreasSourceError('Cache recovery backup already exists; manual recovery is required')`.
4. Computes `archive_existed` from `archive_path.is_file()`.
5. Computes `metadata_existed` from `metadata_path.is_file()`.
6. Runs guarded operation: Checks `archive_existed`. When true: Calls `copy2(archive_path, archive_backup)` for its validation or side effect. Checks `metadata_existed`. When true: Calls `copy2(metadata_path, metadata_backup)` for its validation or side effect. Handles `OSError`.
7. Runs guarded operation: Calls `_replace_file(temporary_archive, archive_path)` for its validation or side effect. Calls `_replace_file(temporary_metadata, metadata_path)` for its validation or side effect. Handles `OSError`.

**Validation and invariants**

- Rejects or diverts the path when `any((path.exists() or _is_link_or_junction(path) for path in (archive_backup, metadata_backup)))` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_replace_file`, `archive_backup.unlink`, `archive_path.unlink`, `copy2`, `metadata_backup.unlink`, `metadata_path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `InpnProtectedAreasSourceError`, `_is_link_or_junction`, `_replace_file`, `any`, `archive_backup.unlink`, `archive_path.is_file`, `archive_path.unlink`, `archive_path.with_name`, `copy2`, `metadata_backup.unlink`, `metadata_path.is_file`, `metadata_path.unlink`, `metadata_path.with_name`, `path.exists`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `download_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_download_archive_bytes`

**Signature**

```python
def _download_archive_bytes(
    configured_url: str,
    timeout_seconds: float,
    destination: Path,
) -> None:
```

**Purpose**

Downloads and validates archive bytes according to the exact implementation and guards in this file.

**Inputs**

- `configured_url` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout_seconds` (`float`; required) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.
- `destination` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Enters managed context(s) `open_safe_https(configured_url, timeout=timeout_seconds, headers={'User-Agent': 'LandScout-AI/0.1'})` and executes: Computes `response_headers` from `getattr(response, 'headers', None)`. Computes `header_get` from `getattr(response_headers, 'get', None)`. Checks `not callable(header_get)`. When true: Raises `InpnProtectedAreasSourceError('HTTP response headers are invalid')`. Computes `content_type` from `str(header_get('Content-Type', ''))`. Executes 2 additional source-ordered statement(s). Handles `InpnProtectedAreasSourceError`, `(SafeHttpsError, OSError, TypeError, ValueError)`.

**Validation and invariants**

- Rejects or diverts the path when `not callable(header_get)` is true.
- Rejects or diverts the path when `'text/html' in content_type.casefold()` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `copyfileobj`, `destination.open`, `open_safe_https`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `InpnProtectedAreasSourceError`, `callable`, `content_type.casefold`, `copyfileobj`, `destination.open`, `getattr`, `header_get`, `open_safe_https`, `str`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `download_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `download_inpn_protected_areas_archive`

**Signature**

```python
def download_inpn_protected_areas_archive(
    config: InpnProtectedAreasSourceConfig,
    *,
    timeout_seconds: float = 120.0,
) -> InpnProtectedAreasDownload:
```

**Purpose**

Download or reuse the exact configured official EP ZIP bytes.

**Inputs**

- `config` (`InpnProtectedAreasSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout_seconds` (`float`; optional/default `120.0`) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `InpnProtectedAreasDownload`. Observed return expression(s): `cached`; `result`.

**Algorithm**

1. Computes `validated_config` from `_validated_config(config)`.
2. Checks `isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, Real)`. When true: Raises `InpnProtectedAreasSourceError('timeout_seconds must be a strict finite positive number')`.
3. Runs guarded operation: Computes `validated_timeout` from `float(timeout_seconds)`. Handles `(OverflowError, TypeError, ValueError)`.
4. Checks `not isfinite(validated_timeout) or validated_timeout <= 0`. When true: Raises `InpnProtectedAreasSourceError('timeout_seconds must be a strict finite positive number')`.
5. Computes `archive_path` from `_archive_path(validated_config)`.
6. Computes `metadata_path` from `_metadata_path(archive_path)`.
7. Computes `cached` from `_load_cached_download(archive_path, metadata_path, validated_config)`.
8. Checks `cached is not None`. When true: Returns `cached`.
9. Computes `temporary_archive` from `archive_path.with_name(f'{archive_path.name}.part')`.
10. Computes `temporary_metadata` from `metadata_path.with_name(f'{metadata_path.name}.part')`.
11. Runs guarded operation: Calls `archive_path.parent.mkdir(parents=True, exist_ok=True)` for its validation or side effect. Calls `temporary_archive.unlink(missing_ok=True)` for its validation or side effect. Calls `temporary_metadata.unlink(missing_ok=True)` for its validation or side effect. Calls `_download_archive_bytes(str(validated_config.archive_url), validated_timeout, temporary_archive)` for its validation or side effect. Executes 9 additional source-ordered statement(s). Handles `InpnProtectedAreasSourceError`, `(OSError, TypeError, ValueError, ValidationError)`. Finally: Iterates `temporary_path` over `(temporary_archive, temporary_metadata)`. For each value: Runs guarded operation: Calls `temporary_path.unlink(missing_ok=True)` for its validation or side effect. Handles `OSError`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, Real)` is true.
- Rejects or diverts the path when `not isfinite(validated_timeout) or validated_timeout <= 0` is true.
- Rejects or diverts the path when `file_size != validated_config.expected_archive_size_bytes or checksum != validated_config.expected_archive_sha256` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `InpnProtectedAreasDownload`, `_download_archive_bytes`, `_download_metadata`, `_load_cached_download`, `archive_path.parent.mkdir`, `temporary_archive.unlink`, `temporary_metadata.unlink`, `temporary_metadata.write_text`, `temporary_path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `InpnProtectedAreasDownload`, `InpnProtectedAreasSourceError`, `_archive_path`, `_download_archive_bytes`, `_download_metadata`, `_load_cached_download`, `_metadata_path`, `_publish_cache_pair`, `_sha256_file`, `_validated_config`, `_validated_zip_members`, `archive_path.parent.mkdir`, `archive_path.with_name`, `datetime.now`, `datetime.now(UTC).isoformat`, `float`, `isfinite`, `isinstance`, `metadata.model_dump_json`, `metadata_path.with_name`, `str`, `temporary_archive.stat`, `temporary_archive.unlink`, `temporary_metadata.unlink`, `temporary_metadata.write_text`, `temporary_path.unlink`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `_download_with_session`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_download_timeout_is_strict_finite_positive`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_physical_and_metadata_cache_is_reused`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_wrong_download_config_type_has_controlled_error`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_download_timeout_is_strict_finite_positive`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_physical_and_metadata_cache_is_reused`
- `tests/unit/test_inpn_protected_areas_fr.py::test_wrong_download_config_type_has_controlled_error`

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validate_download`

**Signature**

```python
def _validate_download(
    download: object,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload:
```

**Purpose**

Validates and rejects malformed download according to the exact implementation and guards in this file.

**Inputs**

- `download` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`InpnProtectedAreasSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `InpnProtectedAreasDownload`. Observed return expression(s): `download`.

**Algorithm**

1. Checks `type(download) is not InpnProtectedAreasDownload`. When true: Raises `InpnProtectedAreasSourceError('download must be an exact InpnProtectedAreasDownload')`.
2. Computes `expected` from `{'provider': config.provider, 'authority': config.authority, 'program': config.program, 'dataset_id': config.dataset_id, 'dataset_name': config.dataset_name, 'declared_version': config.declared_version, 'reference_page_url': str(config.reference_page_url), 'archive_url': str(config.archive_url), 'filename': config.arc…`.
3. Runs guarded operation: Checks `any((getattr(download, key) != value for key, value in expected.items()))`. When true: Raises `ValueError('Download lineage differs from config')`. Checks `not isinstance(download.path, Path) or download.path != _archive_path(config)`. When true: Raises `ValueError('Download path differs from configured cache identity')`. Checks `type(download.cache_hit) is not bool`. When true: Raises `ValueError('Download cache_hit must be boolean')`. Checks `type(download.file_size) is not int or download.file_size <= 0 or download.file_size != config.expected_archive_size_bytes or (type(download.sha256) is not str) or (re.fullmatch('[0-9a-f]{64}', download.sha256) is None) or (download.sha256 != config.expected_archive_sha256)`. When true: Raises `ValueError('Download integrity scalars are invalid')`. Executes 6 additional source-ordered statement(s). Handles `InpnProtectedAreasSourceError`, `(AttributeError, OSError, TypeError, ValueError)`.

**Validation and invariants**

- Rejects or diverts the path when `type(download) is not InpnProtectedAreasDownload` is true.
- Rejects or diverts the path when `any((getattr(download, key) != value for key, value in expected.items()))` is true.
- Rejects or diverts the path when `not isinstance(download.path, Path) or download.path != _archive_path(config)` is true.
- Rejects or diverts the path when `type(download.cache_hit) is not bool` is true.
- Rejects or diverts the path when `type(download.file_size) is not int or download.file_size <= 0 or download.file_size != config.expected_archive_size_bytes or (type(download.sha256) is not str) or (re.fullmatch('[0-9a-f]{64}', download.sha256) is None) or (download.sha256 != config.expected_archive_sha256)` is true.
- Rejects or diverts the path when `not _is_regular_file(download.path)` is true.
- Rejects or diverts the path when `download.path.stat().st_size != download.file_size` is true.
- Rejects or diverts the path when `_sha256_file(download.path) != download.sha256` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `download.path.stat`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `InpnProtectedAreasSourceError`, `ValueError`, `_archive_path`, `_is_regular_file`, `_sha256_file`, `_validate_utc_timestamp`, `_validated_zip_members`, `any`, `download.path.stat`, `expected.items`, `getattr`, `isinstance`, `re.fullmatch`, `str`, `type`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `extract_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validate_inventory_relative_path`

**Signature**

```python
def _validate_inventory_relative_path(value: object) -> None:
```

**Purpose**

Validates and rejects malformed inventory relative path according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `type(value) is not str or not value or value != value.strip()`. When true: Raises `ValueError('Inventory relative_path must be an exact non-empty string')`.
2. Computes `(destination, _)` from `_canonical_member_destination(value)`.
3. Checks `destination.as_posix() != value or value == EXTRACTION_METADATA_FILENAME`. When true: Raises `ValueError('Inventory relative_path is not canonical POSIX form')`.

**Validation and invariants**

- Rejects or diverts the path when `type(value) is not str or not value or value != value.strip()` is true.
- Rejects or diverts the path when `destination.as_posix() != value or value == EXTRACTION_METADATA_FILENAME` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_canonical_member_destination`, `destination.as_posix`, `type`, `value.strip`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_ExtractedFileMetadata._canonical_path`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_inventory`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_inventory`

**Signature**

```python
def _inventory(root: Path) -> tuple[InpnProtectedAreasExtractedFile, ...]:
```

**Purpose**

Implements inventory according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[InpnProtectedAreasExtractedFile, ...]`. Observed return expression(s): `tuple(files)`.

**Algorithm**

1. Checks `_is_link_or_junction(root) or not root.is_dir()`. When true: Raises `InpnProtectedAreasSourceError('Extraction root must be a regular directory')`.
2. Defines `files` with annotation `list[InpnProtectedAreasExtractedFile]` from `[]`.
3. Iterates `path` over `root.rglob('*')`. For each value: Checks `_is_link_or_junction(path)`. When true: Raises `InpnProtectedAreasSourceError(f'Extracted link or junction is forbidden: {path}')`. Checks `path.is_dir()`. When true: Executes `continue` control flow. Checks `not path.is_file()`. When true: Raises `InpnProtectedAreasSourceError(f'Extracted special filesystem entry is forbidden: {path}')`. Executes 4 additional source-ordered statement(s).
4. Calls `files.sort(key=lambda item: item.relative_path)` for its validation or side effect.
5. Checks `not files`. When true: Raises `InpnProtectedAreasSourceError('Extracted INPN archive contains no regular files')`.
6. Returns `tuple(files)`.

**Validation and invariants**

- Rejects or diverts the path when `_is_link_or_junction(root) or not root.is_dir()` is true.
- Rejects or diverts the path when `not files` is true.
- Rejects or diverts the path when `_is_link_or_junction(path)` is true.
- Rejects or diverts the path when `not path.is_file()` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `InpnProtectedAreasExtractedFile`, `InpnProtectedAreasSourceError`, `_is_link_or_junction`, `_sha256_file`, `_validate_inventory_relative_path`, `files.append`, `files.sort`, `path.is_dir`, `path.is_file`, `path.relative_to`, `path.relative_to(root).as_posix`, `path.stat`, `root.is_dir`, `root.rglob`, `tuple`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_validate_extraction_cache`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `extract_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_extraction_metadata`

**Signature**

```python
def _extraction_metadata(
    download: InpnProtectedAreasDownload,
    files: tuple[InpnProtectedAreasExtractedFile, ...],
) -> _ExtractionMetadata:
```

**Purpose**

Implements extraction metadata according to the exact implementation and guards in this file.

**Inputs**

- `download` (`InpnProtectedAreasDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `files` (`tuple[InpnProtectedAreasExtractedFile, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_ExtractionMetadata`. Observed return expression(s): `_ExtractionMetadata(schema_version=EXTRACTION_METADATA_SCHEMA_VERSION, archive_sha256=download.sha256, archive_size=download.file_size, files=tuple((_ExtractedFileMetadata(relative_path=item.relative_path, file_size=item.file_size, sha256=item.sha256) for item in files)))`.

**Algorithm**

1. Returns `_ExtractionMetadata(schema_version=EXTRACTION_METADATA_SCHEMA_VERSION, archive_sha256=download.sha256, archive_size=download.file_size, files=tuple((_ExtractedFileMetadata(relative_path=item.relative_path, file_size=item.file_size, sha256=item.sha256) for item in files)))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_ExtractedFileMetadata`, `_ExtractionMetadata`, `tuple`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `extract_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_validate_extraction_cache`

**Signature**

```python
def _validate_extraction_cache(
    root: Path,
    download: InpnProtectedAreasDownload,
) -> tuple[InpnProtectedAreasExtractedFile, ...]:
```

**Purpose**

Validates and rejects malformed extraction cache according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `download` (`InpnProtectedAreasDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[InpnProtectedAreasExtractedFile, ...]`. Observed return expression(s): `actual`.

**Algorithm**

1. Computes `marker` from `root / EXTRACTION_METADATA_FILENAME`.
2. Checks `not _is_regular_file(marker)`. When true: Raises `InpnProtectedAreasSourceError('Extraction integrity metadata is missing or unsafe')`.
3. Runs guarded operation: Computes `metadata` from `_ExtractionMetadata.model_validate(_read_strict_json(marker))`. Checks `metadata.archive_sha256 != download.sha256 or metadata.archive_size != download.file_size`. When true: Raises `ValueError('Extraction metadata archive lineage differs')`. Computes `expected` from `tuple((InpnProtectedAreasExtractedFile(relative_path=item.relative_path, file_size=item.file_size, sha256=item.sha256) for item in metadata.files))`. Computes `actual` from `_inventory(root)`. Executes 2 additional source-ordered statement(s). Handles `InpnProtectedAreasSourceError`, `(OSError, TypeError, ValueError, ValidationError, json.JSONDecodeError)`.

**Validation and invariants**

- Rejects or diverts the path when `not _is_regular_file(marker)` is true.
- Rejects or diverts the path when `metadata.archive_sha256 != download.sha256 or metadata.archive_size != download.file_size` is true.
- Rejects or diverts the path when `actual != expected` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_read_strict_json`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `InpnProtectedAreasExtractedFile`, `InpnProtectedAreasSourceError`, `ValueError`, `_ExtractionMetadata.model_validate`, `_inventory`, `_is_regular_file`, `_read_strict_json`, `tuple`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `extract_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_path_exists`

**Signature**

```python
def _path_exists(path: Path) -> bool:
```

**Purpose**

Implements path exists according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `path.exists() or path.is_symlink() or _is_link_or_junction(path)`.

**Algorithm**

1. Returns `path.exists() or path.is_symlink() or _is_link_or_junction(path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_is_link_or_junction`, `path.exists`, `path.is_symlink`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_publish_extraction_directory`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_remove_path`

**Signature**

```python
def _remove_path(path: Path) -> None:
```

**Purpose**

Implements remove path according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `path.is_junction()`. When true: Calls `path.rmdir()` for its validation or side effect. Otherwise: Checks `path.is_symlink() or path.is_file()`. When true: Calls `path.unlink(missing_ok=True)` for its validation or side effect. Otherwise: Checks `path.exists()`. When true: Calls `shutil.rmtree(path)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `path.exists`, `path.is_file`, `path.is_junction`, `path.is_symlink`, `path.rmdir`, `path.unlink`, `shutil.rmtree`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_publish_extraction_directory`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `extract_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_replace_directory`

**Signature**

```python
def _replace_directory(source: Path, target: Path) -> None:
```

**Purpose**

Implements replace directory according to the exact implementation and guards in this file.

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

- `src/landscout/sources/inpn_protected_areas_fr.py` — `_publish_extraction_directory`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `_publish_extraction_directory`

**Signature**

```python
def _publish_extraction_directory(temporary_root: Path, root: Path) -> None:
```

**Purpose**

Implements publish extraction directory according to the exact implementation and guards in this file.

**Inputs**

- `temporary_root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `backup` from `root.with_name(f'{root.name}.bak')`.
2. Checks `_path_exists(backup)`. When true: Raises `InpnProtectedAreasSourceError('Extraction recovery backup already exists; manual recovery is required')`.
3. Computes `old_moved` from `False`.
4. Checks `_path_exists(root)`. When true: Runs guarded operation: Calls `_replace_directory(root, backup)` for its validation or side effect. Handles `OSError`. Computes `old_moved` from `True`.
5. Runs guarded operation: Calls `_replace_directory(temporary_root, root)` for its validation or side effect. Handles `OSError`.

**Validation and invariants**

- Rejects or diverts the path when `_path_exists(backup)` is true.
- Rejects or diverts the path when `_path_exists(root)` is true.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_replace_directory`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `InpnProtectedAreasSourceError`, `_path_exists`, `_remove_path`, `_replace_directory`, `root.with_name`.

**Known repository callers**

- `src/landscout/sources/inpn_protected_areas_fr.py` — `extract_inpn_protected_areas_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

### `extract_inpn_protected_areas_archive`

**Signature**

```python
def extract_inpn_protected_areas_archive(
    download: InpnProtectedAreasDownload,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasExtraction:
```

**Purpose**

Safely extract all regular files and bind an exact factual inventory.

**Inputs**

- `download` (`InpnProtectedAreasDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`InpnProtectedAreasSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `InpnProtectedAreasExtraction`. Observed return expression(s): `InpnProtectedAreasExtraction(download=validated_download, extraction_path=root, files=files, cache_hit=False)`; `InpnProtectedAreasExtraction(download=validated_download, extraction_path=root, files=files, cache_hit=True)`.

**Algorithm**

1. Computes `validated_config` from `_validated_config(config)`.
2. Computes `validated_download` from `_validate_download(download, validated_config)`.
3. Computes `root` from `validated_download.path.parent / 'x' / validated_download.sha256`.
4. Checks `root.is_dir() and (not _is_link_or_junction(root))`. When true: Runs guarded operation: Computes `files` from `_validate_extraction_cache(root, validated_download)`. Returns `InpnProtectedAreasExtraction(download=validated_download, extraction_path=root, files=files, cache_hit=True)`. Handles `(InpnProtectedAreasSourceError, OSError)`.
5. Computes `temporary_root` from `root.with_name(f'{root.name}.part')`.
6. Runs guarded operation: Calls `root.parent.mkdir(parents=True, exist_ok=True)` for its validation or side effect. Calls `_remove_path(temporary_root)` for its validation or side effect. Calls `temporary_root.mkdir(parents=True)` for its validation or side effect. Enters managed context(s) `zipfile.ZipFile(validated_download.path)` and executes: Computes `members` from `_validated_zip_members(validated_download.path)`. Iterates `member` over `members`. For each value: Computes `target` from `temporary_root.joinpath(*member.destination.parts)`. Checks `member.is_directory`. When true: Calls `target.mkdir(parents=True, exist_ok=True)` for its validation or side effect. Executes `continue` control flow. Calls `target.parent.mkdir(parents=True, exist_ok=True)` for its validation or side effect. Executes 1 additional source-ordered statement(s). Executes 7 additional source-ordered statement(s). Handles `InpnProtectedAreasSourceError`, `(NotImplementedError, OSError, RuntimeError, ValueError, zipfile.BadZipFile, zlib.error)`. Finally: Runs guarded operation: Calls `_remove_path(temporary_root)` for its validation or side effect. Handles `OSError`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `InpnProtectedAreasSourceError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(temporary_root / EXTRACTION_METADATA_FILENAME).write_text`, `_validate_download`, `archive.open`, `copyfileobj`, `root.parent.mkdir`, `target.mkdir`, `target.open`, `target.parent.mkdir`, `temporary_root.mkdir`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(temporary_root / EXTRACTION_METADATA_FILENAME).write_text`, `InpnProtectedAreasExtraction`, `InpnProtectedAreasSourceError`, `_extraction_metadata`, `_inventory`, `_is_link_or_junction`, `_publish_extraction_directory`, `_remove_path`, `_validate_download`, `_validate_extraction_cache`, `_validated_config`, `_validated_zip_members`, `archive.open`, `copyfileobj`, `metadata.model_dump_json`, `root.is_dir`, `root.parent.mkdir`, `root.with_name`, `target.mkdir`, `target.open`, `target.parent.mkdir`, `temporary_root.joinpath`, `temporary_root.mkdir`, `zipfile.ZipFile`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `test_archive_and_extraction_cache_reuse_are_independent`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_exact_file_inventory_does_not_omit_unknown_suffixes`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_backup_move_failure_leaves_old_tree_untouched`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_cache_setup_failure_is_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rejects_stale_download_bytes`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rejects_wrong_config_type`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rejects_wrong_download_type`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_replacement_failure_restores_old_tree`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rollback_failure_preserves_backup`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_validates_complete_inventory_before_copying`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_first_extraction_publication_failure_leaves_no_half_root`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_no_stale_parts_after_download_or_extraction_success`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_result_dataclasses_are_frozen`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_extraction_cache_is_reused`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_archive_and_extraction_cache_reuse_are_independent`
- `tests/unit/test_inpn_protected_areas_fr.py::test_exact_file_inventory_does_not_omit_unknown_suffixes`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_cache_setup_failure_is_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_stale_download_bytes`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_config_type`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_download_type`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_validates_complete_inventory_before_copying`
- `tests/unit/test_inpn_protected_areas_fr.py::test_first_extraction_publication_failure_leaves_no_half_root`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py::test_no_stale_parts_after_download_or_extraction_success`
- `tests/unit/test_inpn_protected_areas_fr.py::test_result_dataclasses_are_frozen`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_extraction_cache_is_reused`

**Business interpretation**

This symbol contributes to the `environment` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `Base de référence des espaces protégés français` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `EP` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `EP.zip` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `INPN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `MNHN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `PatriNat` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `environment` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
