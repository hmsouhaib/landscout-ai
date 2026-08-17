# `src/landscout/stages/index_planning_regulation.py`

## File identity

- Repository path: `src/landscout/stages/index_planning_regulation.py`
- File type: Python source
- Primary responsibility: Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.
- Layer / domain: `stage` / `planning`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `b9434ebeb1b3e05a0604bb56facde5f17183beb04cc2b6da667a438d11aa50d1`

## 1. Purpose

Selects the authoritative written regulation PDF, extracts text records, and builds a byte-bound searchable index.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from collections.abc import Sequence` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass, replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from numbers import Integral` — required by the implementation paths and symbols documented below.
- `from pathlib import Path, PurePosixPath` — required by the implementation paths and symbols documented below.
- `from re import escape, finditer, fullmatch, sub` — required by the implementation paths and symbols documented below.
- `from typing import Literal` — required by the implementation paths and symbols documented below.

### Third-party

- `from importlib.metadata import version` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pypdf import PdfReader` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common import planning_text` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import ( GpuArchiveDownload, GpuDocumentMetadata, GpuExtractedFile, GpuExtraction, GpuPlanningDocument, GpuSpatialInspectionError, GpuWrittenFile, revalidate_gpu_spatial_layer_source, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `SEARCH_NORMALIZATION_PROFILE` | `planning_text.SEARCH_NORMALIZATION_PROFILE` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PAGE_HASH_SCHEMA_VERSION` | `1` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `INDEX_HASH_SCHEMA_VERSION` | `1` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SEARCH_HASH_SCHEMA_VERSION` | `1` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PAGE_COLUMNS` | `( "page_number", "extraction_status", "raw_text", "normalized_search_text", "character_count", "extraction_error", "page_content_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SEARCH_HIT_COLUMNS` | `( "document_id", "archive_sha256", "pdf_sha256", "search_normalization_profile", "search_term", "normalized_search_term", "page_number", "occurrence_count", "raw_context", "normalized_context", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `PlanningRegulationIndexError`

**Purpose:** Raised when regulation indexing or search integrity cannot be proven.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `PlanningRegulationIndex`

**Purpose:** Immutable lineage envelope around a deterministic page text table.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `regulation_filename` | `str` | `required` | `str` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_selection_method` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `source_selection_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `pdf_relative_path` | `str` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `pdf_size_bytes` | `int` | `required` | `int` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `pdf_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `extraction_library` | `str` | `required` | `str` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `extraction_library_version` | `str` | `required` | `str` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `search_normalization_profile` | `str` | `required` | `str` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `page_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `index_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `total_page_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `pages_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `index_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `pages` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `PlanningRegulationSearchResult`

**Purpose:** Immutable lineage envelope around deterministic factual search hits.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `pdf_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `search_normalization_profile` | `str` | `required` | `str` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `search_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `index_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `requested_terms` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `context_characters` | `int` | `required` | `int` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `hit_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `hits_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `hits` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_ZoningSourceFileIntegrity`

**Purpose:** Groups the `ZoningSourceFileIntegrity` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `relative_path` | `str` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `size_bytes` | `int` | `required` | `int` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |

**Validators and methods:**

- None.

### `_ZoningSourceEvidence`

**Purpose:** Groups the `ZoningSourceEvidence` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `source_layer` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `driver` | `str` | `required` | `str` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `files` | `tuple[_ZoningSourceFileIntegrity, ...]` | `required` | `tuple[_ZoningSourceFileIntegrity, ...]` state used by `src/landscout/stages/index_planning_regulation.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_strict_string`

**Signature**

```python
def _strict_string(value: object, label: str) -> str:
```

**Purpose**

Implements strict string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `PlanningRegulationIndexError(f'{label} must be a non-empty exact string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_locate_regulation_pdf`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_document_lineage`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_index`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_search_result`
- `src/landscout/stages/index_planning_regulation.py` — `_validated_pdf_basename`
- `src/landscout/stages/index_planning_regulation.py` — `_validated_relative_path`
- `src/landscout/stages/index_planning_regulation.py` — `_validated_sha256`
- `src/landscout/stages/index_planning_regulation.py` — `_validated_terms`
- `src/landscout/stages/index_planning_regulation.py` — `_written_file_matches`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_nonnegative_integer`

**Signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

**Purpose**

Implements strict nonnegative integer according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `int(value)`.

**Algorithm**

1. Checks `isinstance(value, bool) or not isinstance(value, Integral)`. When true: Raises `PlanningRegulationIndexError(f'{label} must be an integer')`.
2. Checks `value < 0`. When true: Raises `PlanningRegulationIndexError(f'{label} must be non-negative')`.
3. Returns `int(value)`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Integral)` is true.
- Rejects or diverts the path when `value < 0` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `int`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_strict_positive_integer`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_pages`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_search_result`
- `src/landscout/stages/index_planning_regulation.py` — `search_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_positive_integer`

**Signature**

```python
def _strict_positive_integer(value: object, label: str) -> int:
```

**Purpose**

Implements strict positive integer according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `result` from `_strict_nonnegative_integer(value, label)`.
2. Checks `result == 0`. When true: Raises `PlanningRegulationIndexError(f'{label} must be positive')`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `result == 0` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_strict_nonnegative_integer`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_locate_regulation_pdf`
- `src/landscout/stages/index_planning_regulation.py` — `_supported_schema_version`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_pages`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_index`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_search_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_supported_schema_version`

**Signature**

```python
def _supported_schema_version(value: object, supported: int, label: str) -> int:
```

**Purpose**

Implements supported schema version according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `supported` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `result` from `_strict_positive_integer(value, label)`.
2. Checks `result != supported`. When true: Raises `PlanningRegulationIndexError(f'Unsupported {label}: {result}; expected {supported}')`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `result != supported` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_strict_positive_integer`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_index`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_search_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_sha256`

**Signature**

```python
def _validated_sha256(value: object, label: str) -> str:
```

**Purpose**

Validates and returns canonical sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `checksum`.

**Algorithm**

1. Computes `checksum` from `_strict_string(value, label)`.
2. Checks `fullmatch('[0-9a-f]{64}', checksum) is None`. When true: Raises `PlanningRegulationIndexError(f'{label} must contain exactly 64 lowercase hexadecimal characters')`.
3. Returns `checksum`.

**Validation and invariants**

- Rejects or diverts the path when `fullmatch('[0-9a-f]{64}', checksum) is None` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_strict_string`, `fullmatch`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_locate_regulation_pdf`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_document_lineage`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_pages`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_index`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_search_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_sha256`

**Signature**

```python
def _canonical_sha256(value: object) -> str:
```

**Purpose**

Implements canonical sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(payload).hexdigest()`.

**Algorithm**

1. Runs guarded operation: Computes `payload` from `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')`. Handles `Exception`.
2. Returns `sha256(payload).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `json.dumps`, `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(payload).hexdigest`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_hits_content_sha256`
- `src/landscout/stages/index_planning_regulation.py` — `_index_content_sha256`
- `src/landscout/stages/index_planning_regulation.py` — `_page_content_sha256`
- `src/landscout/stages/index_planning_regulation.py` — `_pages_content_sha256`
- `src/landscout/stages/index_planning_regulation.py` — `_source_selection_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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

- Declared return type: `bool`. Observed return expression(s): `path.is_symlink() or path.is_junction()`.

**Algorithm**

1. Runs guarded operation: Returns `path.is_symlink() or path.is_junction()`. Handles `OSError`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `path.is_junction`, `path.is_symlink`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_locate_regulation_pdf`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_relative_path`

**Signature**

```python
def _validated_relative_path(value: object) -> PurePosixPath:
```

**Purpose**

Validates and returns canonical relative path according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PurePosixPath`. Observed return expression(s): `relative`.

**Algorithm**

1. Computes `raw` from `_strict_string(value, 'GPU inventory relative path')`.
2. Checks `'\\' in raw or '\x00' in raw`. When true: Raises `PlanningRegulationIndexError('GPU inventory path is unsafe')`.
3. Computes `parts` from `raw.split('/')`.
4. Checks `any((part in {'', '.', '..'} for part in parts))`. When true: Raises `PlanningRegulationIndexError('GPU inventory path is unsafe')`.
5. Computes `relative` from `PurePosixPath(raw)`.
6. Checks `relative.is_absolute() or relative.as_posix() != raw`. When true: Raises `PlanningRegulationIndexError('GPU inventory path is unsafe')`.
7. Returns `relative`.

**Validation and invariants**

- Rejects or diverts the path when `'\\' in raw or '\x00' in raw` is true.
- Rejects or diverts the path when `any((part in {'', '.', '..'} for part in parts))` is true.
- Rejects or diverts the path when `relative.is_absolute() or relative.as_posix() != raw` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `PurePosixPath`, `_strict_string`, `any`, `raw.split`, `relative.as_posix`, `relative.is_absolute`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_locate_regulation_pdf`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_index`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_pdf_basename`

**Signature**

```python
def _validated_pdf_basename(value: object) -> str:
```

**Purpose**

Validates and returns canonical pdf basename according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `name`.

**Algorithm**

1. Computes `name` from `_strict_string(value, 'regulation PDF filename')`.
2. Checks `name in {'.', '..'} or '/' in name or '\\' in name or (Path(name).name != name) or (not name.casefold().endswith('.pdf')) or any((ord(character) < 32 or ord(character) == 127 for character in name))`. When true: Raises `PlanningRegulationIndexError('regulation PDF filename must be one safe PDF basename')`.
3. Returns `name`.

**Validation and invariants**

- Rejects or diverts the path when `name in {'.', '..'} or '/' in name or '\\' in name or (Path(name).name != name) or (not name.casefold().endswith('.pdf')) or any((ord(character) < 32 or ord(character) == 127 for character in name))` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Path`, `PlanningRegulationIndexError`, `_strict_string`, `any`, `name.casefold`, `name.casefold().endswith`, `ord`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_resolve_regulation_filename`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_index`
- `src/landscout/stages/index_planning_regulation.py` — `_zoning_regulation_filenames`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_file_sha256`

**Signature**

```python
def _file_sha256(path: Path) -> str:
```

**Purpose**

Implements file sha256 according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `digest.hexdigest()`.

**Algorithm**

1. Computes `digest` from `sha256()`.
2. Runs guarded operation: Enters managed context(s) `path.open('rb')` and executes: Repeats the guarded body while `(chunk := stream.read(1024 * 1024))` remains true. Handles `OSError`.
3. Returns `digest.hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningRegulationIndexError`, `digest.hexdigest`, `digest.update`, `path.open`, `sha256`, `stream.read`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`
- `src/landscout/stages/index_planning_regulation.py` — `_locate_regulation_pdf`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_revalidate_zoning_source`

**Signature**

```python
def _revalidate_zoning_source(
    planning_document: GpuPlanningDocument,
) -> tuple[gpd.GeoDataFrame, _ZoningSourceEvidence]:
```

**Purpose**

Re-read immutable zoning bytes before trusting source PDF references.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[gpd.GeoDataFrame, _ZoningSourceEvidence]`. Observed return expression(s): `(source.data, _ZoningSourceEvidence(source_layer=source.source_layer, driver=source.driver, files=tuple((_ZoningSourceFileIntegrity(relative_path=item.relative_path, size_bytes=item.size_bytes, sha256=item.sha256) for item in source.files))))`.

**Algorithm**

1. Runs guarded operation: Computes `source` from `revalidate_gpu_spatial_layer_source(planning_document, planning_document.zoning)`. Checks `'NOMFIC' not in source.data.columns`. When true: Raises `PlanningRegulationIndexError('GPU zoning is missing NOMFIC')`. Returns `(source.data, _ZoningSourceEvidence(source_layer=source.source_layer, driver=source.driver, files=tuple((_ZoningSourceFileIntegrity(relative_path=item.relative_path, size_bytes=item.size_bytes, sha256=item.sha256) for item in source.files))))`. Handles `PlanningRegulationIndexError`, `GpuSpatialInspectionError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `'NOMFIC' not in source.data.columns` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_ZoningSourceEvidence`, `_ZoningSourceFileIntegrity`, `revalidate_gpu_spatial_layer_source`, `tuple`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_resolve_regulation_filename`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_document_lineage`

**Signature**

```python
def _validate_document_lineage(planning_document: GpuPlanningDocument) -> tuple[str, str]:
```

**Purpose**

Validates and rejects malformed document lineage according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, str]`. Observed return expression(s): `(document_id, archive_sha)`.

**Algorithm**

1. Checks `not isinstance(planning_document, GpuPlanningDocument)`. When true: Raises `PlanningRegulationIndexError('planning_document must be a GpuPlanningDocument')`.
2. Computes `extraction` from `planning_document.extraction`.
3. Checks `not isinstance(extraction, GpuExtraction)`. When true: Raises `PlanningRegulationIndexError('GPU extraction lineage is invalid')`.
4. Computes `archive` from `extraction.archive`.
5. Checks `not isinstance(archive, GpuArchiveDownload) or not isinstance(archive.document, GpuDocumentMetadata)`. When true: Raises `PlanningRegulationIndexError('GPU archive lineage is invalid')`.
6. Computes `metadata` from `archive.document`.
7. Computes `document_id` from `_strict_string(metadata.document_id, 'GPU document ID')`.
8. Computes `archive_sha` from `_validated_sha256(archive.sha256, 'GPU archive SHA256')`.
9. Checks `not isinstance(archive.archive_format, str) or archive.archive_format.casefold() != 'zip'`. When true: Raises `PlanningRegulationIndexError('GPU archive format must be zip')`.
10. Checks `metadata.document_family != 'DU' or metadata.status != 'document.production' or metadata.legal_status != 'APPROVED' or (metadata.effective_status != 'EN_VIGUEUR')`. When true: Raises `PlanningRegulationIndexError('GPU planning document is not the current effective DU')`.
11. Checks `type(planning_document.related_layers) is not tuple or type(planning_document.all_spatial_layers) is not tuple`. When true: Raises `PlanningRegulationIndexError('GPU spatial-layer lineage is invalid')`.
12. Checks `planning_document.zoning.logical_name != 'zoning'`. When true: Raises `PlanningRegulationIndexError('GPU zoning logical layer is invalid')`.
13. Checks `planning_document.zoning.reference not in planning_document.all_spatial_layers`. When true: Raises `PlanningRegulationIndexError('GPU zoning reference is absent from discovered spatial layers')`.
14. Iterates `layer` over `(planning_document.zoning, *planning_document.related_layers)`. For each value: Checks `layer.summary.source_document_id != document_id or layer.summary.source_archive_sha256 != archive_sha or layer.summary.source_layer != layer.reference.source_layer or (layer.summary.feature_count != len(layer.data))`. When true: Raises `PlanningRegulationIndexError('GPU spatial-layer lineage is inconsistent with the archive')`.
15. Returns `(document_id, archive_sha)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(planning_document, GpuPlanningDocument)` is true.
- Rejects or diverts the path when `not isinstance(extraction, GpuExtraction)` is true.
- Rejects or diverts the path when `not isinstance(archive, GpuArchiveDownload) or not isinstance(archive.document, GpuDocumentMetadata)` is true.
- Rejects or diverts the path when `not isinstance(archive.archive_format, str) or archive.archive_format.casefold() != 'zip'` is true.
- Rejects or diverts the path when `metadata.document_family != 'DU' or metadata.status != 'document.production' or metadata.legal_status != 'APPROVED' or (metadata.effective_status != 'EN_VIGUEUR')` is true.
- Rejects or diverts the path when `type(planning_document.related_layers) is not tuple or type(planning_document.all_spatial_layers) is not tuple` is true.
- Rejects or diverts the path when `planning_document.zoning.logical_name != 'zoning'` is true.
- Rejects or diverts the path when `planning_document.zoning.reference not in planning_document.all_spatial_layers` is true.
- Rejects or diverts the path when `layer.summary.source_document_id != document_id or layer.summary.source_archive_sha256 != archive_sha or layer.summary.source_layer != layer.reference.source_layer or (layer.summary.feature_count != len(layer.data))` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_strict_string`, `_validated_sha256`, `archive.archive_format.casefold`, `isinstance`, `len`, `type`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_zoning_regulation_filenames`

**Signature**

```python
def _zoning_regulation_filenames(zoning: gpd.GeoDataFrame) -> tuple[str, ...]:
```

**Purpose**

Implements zoning regulation filenames according to the exact implementation and guards in this file.

**Inputs**

- `zoning` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `tuple(sorted(values, key=str.casefold))`.

**Algorithm**

1. Checks `'NOMFIC' not in zoning.columns`. When true: Raises `PlanningRegulationIndexError('GPU zoning is missing NOMFIC')`.
2. Defines `values` with annotation `set[str]` from `set()`.
3. Runs guarded operation: Computes `source_values` from `zoning['NOMFIC'].tolist()`. Iterates `value` over `source_values`. For each value: Checks `value is None or value is pd.NA or (isinstance(value, float) and pd.isna(value))`. When true: Executes `continue` control flow. Calls `values.add(_validated_pdf_basename(value))` for its validation or side effect. Handles `PlanningRegulationIndexError`, `Exception`.
4. Checks `not values`. When true: Raises `PlanningRegulationIndexError('GPU zoning NOMFIC contains no regulation filename')`.
5. Returns `tuple(sorted(values, key=str.casefold))`.

**Validation and invariants**

- Rejects or diverts the path when `'NOMFIC' not in zoning.columns` is true.
- Rejects or diverts the path when `not values` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_validated_pdf_basename`, `isinstance`, `pd.isna`, `set`, `sorted`, `tuple`, `values.add`, `zoning['NOMFIC'].tolist`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_resolve_regulation_filename`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_written_file_matches`

**Signature**

```python
def _written_file_matches(
    planning_document: GpuPlanningDocument, filename: str
) -> tuple[GpuWrittenFile, ...]:
```

**Purpose**

Implements written file matches according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `filename` (`str`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuWrittenFile, ...]`. Observed return expression(s): `tuple(matches)`.

**Algorithm**

1. Defines `matches` with annotation `list[GpuWrittenFile]` from `[]`.
2. Computes `written_files` from `planning_document.extraction.archive.document.written_files`.
3. Checks `type(written_files) is not tuple`. When true: Raises `PlanningRegulationIndexError('GPU written-files metadata must be an immutable tuple')`.
4. Iterates `item` over `written_files`. For each value: Checks `not isinstance(item, GpuWrittenFile)`. When true: Raises `PlanningRegulationIndexError('GPU written-files metadata is invalid')`. Computes `written_filename` from `_strict_string(item.filename, 'GPU written filename')`. Checks `written_filename == filename`. When true: Calls `matches.append(item)` for its validation or side effect.
5. Checks `not matches`. When true: Raises `PlanningRegulationIndexError(f'Regulation PDF is absent from official written_files: {filename}')`.
6. Checks `len(matches) != 1`. When true: Raises `PlanningRegulationIndexError(f'Regulation PDF is duplicated in official written_files: {filename}')`.
7. Returns `tuple(matches)`.

**Validation and invariants**

- Rejects or diverts the path when `type(written_files) is not tuple` is true.
- Rejects or diverts the path when `not matches` is true.
- Rejects or diverts the path when `len(matches) != 1` is true.
- Rejects or diverts the path when `not isinstance(item, GpuWrittenFile)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_strict_string`, `isinstance`, `len`, `matches.append`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_resolve_regulation_filename`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolve_regulation_filename`

**Signature**

```python
def _resolve_regulation_filename(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None,
) -> tuple[str, str, _ZoningSourceEvidence, GpuWrittenFile]:
```

**Purpose**

Resolves regulation filename according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `regulation_filename` (`str | None`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, str, _ZoningSourceEvidence, GpuWrittenFile]`. Observed return expression(s): `(selected, method, zoning_evidence, written_file)`.

**Algorithm**

1. Computes `(reread_zoning, zoning_evidence)` from `_revalidate_zoning_source(planning_document)`.
2. Computes `referenced` from `_zoning_regulation_filenames(reread_zoning)`.
3. Checks `regulation_filename is None`. When true: Checks `len(referenced) != 1`. When true: Raises `PlanningRegulationIndexError('GPU zoning NOMFIC regulation selection is ambiguous')`. Computes `selected` from `referenced[0]`. Computes `method` from `'ZONING_NOMFIC'`. Otherwise: Computes `selected` from `_validated_pdf_basename(regulation_filename)`. Checks `selected not in referenced`. When true: Raises `PlanningRegulationIndexError('Explicit regulation filename is not referenced by zoning NOMFIC')`. Executes 1 additional source-ordered statement(s).
4. Computes `written_file` from `_written_file_matches(planning_document, selected)[0]`.
5. Returns `(selected, method, zoning_evidence, written_file)`.

**Validation and invariants**

- Rejects or diverts the path when `regulation_filename is None` is true.
- Rejects or diverts the path when `len(referenced) != 1` is true.
- Rejects or diverts the path when `selected not in referenced` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_revalidate_zoning_source`, `_validated_pdf_basename`, `_written_file_matches`, `_zoning_regulation_filenames`, `len`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_locate_regulation_pdf`

**Signature**

```python
def _locate_regulation_pdf(
    planning_document: GpuPlanningDocument,
    pdf_basename: str,
) -> tuple[Path, GpuExtractedFile]:
```

**Purpose**

Implements locate regulation pdf according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `pdf_basename` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[Path, GpuExtractedFile]`. Observed return expression(s): `(path, item)`.

**Algorithm**

1. Computes `extraction` from `planning_document.extraction`.
2. Computes `root` from `extraction.extraction_root`.
3. Checks `not isinstance(root, Path) or _is_link_or_junction(root) or (not root.is_dir())`. When true: Raises `PlanningRegulationIndexError('GPU extraction root must be a regular directory')`.
4. Defines `inventory_paths` with annotation `set[str]` from `set()`.
5. Defines `matches` with annotation `list[tuple[PurePosixPath, GpuExtractedFile]]` from `[]`.
6. Iterates `item` over `extraction.files`. For each value: Checks `not isinstance(item, GpuExtractedFile)`. When true: Raises `PlanningRegulationIndexError('GPU extraction inventory is invalid')`. Computes `relative` from `_validated_relative_path(item.relative_path)`. Checks `item.relative_path in inventory_paths`. When true: Raises `PlanningRegulationIndexError('GPU extraction inventory contains duplicate paths')`. Executes 2 additional source-ordered statement(s).
7. Checks `not matches`. When true: Raises `PlanningRegulationIndexError(f'Regulation PDF is missing from GPU inventory: {pdf_basename}')`.
8. Checks `len(matches) != 1`. When true: Raises `PlanningRegulationIndexError(f'Regulation PDF is ambiguous in GPU inventory: {pdf_basename}')`.
9. Computes `(relative, item)` from `matches[0]`.
10. Computes `file_type` from `_strict_string(item.file_type, 'PDF inventory file type')`.
11. Checks `file_type.casefold() != 'pdf' or item.category != 'WRITTEN_REGULATION'`. When true: Raises `PlanningRegulationIndexError('Regulation PDF inventory classification is inconsistent')`.
12. Runs guarded operation: Computes `root_resolved` from `root.resolve(strict=True)`. Handles `OSError`.
13. Computes `path` from `root.joinpath(*relative.parts)`.
14. Runs guarded operation: Computes `resolved` from `path.resolve(strict=True)`. Calls `resolved.relative_to(root_resolved)` for its validation or side effect. Handles `(OSError, ValueError)`.
15. Computes `current` from `root`.
16. Iterates `part` over `relative.parts`. For each value: Updates `current` using `` and `part`. Checks `_is_link_or_junction(current)`. When true: Raises `PlanningRegulationIndexError('Regulation PDF path contains a symbolic link or junction')`.
17. Checks `not path.is_file()`. When true: Raises `PlanningRegulationIndexError('Regulation PDF must be an extracted regular file')`.
18. Computes `expected_size` from `_strict_positive_integer(item.size_bytes, 'PDF inventory size')`.
19. Runs guarded operation: Computes `actual_size` from `path.stat().st_size`. Handles `OSError`.
20. Checks `actual_size != expected_size`. When true: Raises `PlanningRegulationIndexError('Regulation PDF size differs from extraction inventory')`.
21. Computes `expected_sha` from `_validated_sha256(item.sha256, 'PDF inventory SHA256')`.
22. Checks `_file_sha256(path) != expected_sha`. When true: Raises `PlanningRegulationIndexError('Regulation PDF SHA256 differs from extraction inventory')`.
23. Returns `(path, item)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(root, Path) or _is_link_or_junction(root) or (not root.is_dir())` is true.
- Rejects or diverts the path when `not matches` is true.
- Rejects or diverts the path when `len(matches) != 1` is true.
- Rejects or diverts the path when `file_type.casefold() != 'pdf' or item.category != 'WRITTEN_REGULATION'` is true.
- Rejects or diverts the path when `not path.is_file()` is true.
- Rejects or diverts the path when `actual_size != expected_size` is true.
- Rejects or diverts the path when `_file_sha256(path) != expected_sha` is true.
- Rejects or diverts the path when `not isinstance(item, GpuExtractedFile)` is true.
- Rejects or diverts the path when `item.relative_path in inventory_paths` is true.
- Rejects or diverts the path when `_is_link_or_junction(current)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_file_sha256`, `_is_link_or_junction`, `_strict_positive_integer`, `_strict_string`, `_validated_relative_path`, `_validated_sha256`, `file_type.casefold`, `inventory_paths.add`, `isinstance`, `len`, `matches.append`, `path.is_file`, `path.resolve`, `path.stat`, `resolved.relative_to`, `root.is_dir`, `root.joinpath`, `root.resolve`, `set`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_error`

**Signature**

```python
def _page_error(error: Exception) -> str:
```

**Purpose**

Implements page error according to the exact implementation and guards in this file.

**Inputs**

- `error` (`Exception`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `f'{type(error).__name__}: {message}' if message else type(error).__name__`.

**Algorithm**

1. Computes `message` from `sub('\\s+', ' ', str(error)).strip()`.
2. Returns `f'{type(error).__name__}: {message}' if message else type(error).__name__`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `str`, `sub`, `sub('\\s+', ' ', str(error)).strip`, `type`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_page_record`

**Signature**

```python
def _canonical_page_record(row: dict[str, object]) -> dict[str, object]:
```

**Purpose**

Implements canonical page record according to the exact implementation and guards in this file.

**Inputs**

- `row` (`dict[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `record`.

**Algorithm**

1. Computes `record` from `{key: row[key] for key in PAGE_COLUMNS if key != 'page_content_sha256'}`.
2. Checks `bool(pd.isna(record['extraction_error']))`. When true: Computes `record['extraction_error']` from `None`.
3. Returns `record`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_page_hash_payload`
- `src/landscout/stages/index_planning_regulation.py` — `_pages_content_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_hash_payload`

**Signature**

```python
def _page_hash_payload(
    row: dict[str, object],
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> dict[str, object]:
```

**Purpose**

Implements page hash payload according to the exact implementation and guards in this file.

**Inputs**

- `row` (`dict[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `page_hash_schema_version` (`int`; optional/default `PAGE_HASH_SCHEMA_VERSION`) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.
- `search_normalization_profile` (`str`; optional/default `SEARCH_NORMALIZATION_PROFILE`) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'schema_version': page_hash_schema_version, 'search_normalization_profile': search_normalization_profile, 'page': _canonical_page_record(row)}`.

**Algorithm**

1. Returns `{'schema_version': page_hash_schema_version, 'search_normalization_profile': search_normalization_profile, 'page': _canonical_page_record(row)}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_page_record`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_page_content_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_page_content_sha256`

**Signature**

```python
def _page_content_sha256(
    row: dict[str, object],
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> str:
```

**Purpose**

Implements page content sha256 according to the exact implementation and guards in this file.

**Inputs**

- `row` (`dict[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `page_hash_schema_version` (`int`; optional/default `PAGE_HASH_SCHEMA_VERSION`) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.
- `search_normalization_profile` (`str`; optional/default `SEARCH_NORMALIZATION_PROFILE`) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256(_page_hash_payload(row, page_hash_schema_version, search_normalization_profile))`.

**Algorithm**

1. Returns `_canonical_sha256(_page_hash_payload(row, page_hash_schema_version, search_normalization_profile))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `_page_hash_payload`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_pages`
- `tests/unit/test_interpret_bess_zoning.py` — `_index`
- `tests/unit/test_structure_planning_regulation.py` — `_index`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_pages_content_sha256`

**Signature**

```python
def _pages_content_sha256(
    frame: pd.DataFrame,
    page_hash_schema_version: int = PAGE_HASH_SCHEMA_VERSION,
    search_normalization_profile: str = SEARCH_NORMALIZATION_PROFILE,
) -> str:
```

**Purpose**

Implements pages content sha256 according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `page_hash_schema_version` (`int`; optional/default `PAGE_HASH_SCHEMA_VERSION`) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.
- `search_normalization_profile` (`str`; optional/default `SEARCH_NORMALIZATION_PROFILE`) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'schema_version': page_hash_schema_version, 'search_normalization_profile': search_normalization_profile, 'pages': pages})`.

**Algorithm**

1. Computes `pages` from `[]`.
2. Iterates `row` over `frame.loc[:, PAGE_COLUMNS].to_dict('records')`. For each value: Computes `canonical` from `_canonical_page_record(row)`. Computes `canonical['page_content_sha256']` from `row['page_content_sha256']`. Calls `pages.append(canonical)` for its validation or side effect.
3. Returns `_canonical_sha256({'schema_version': page_hash_schema_version, 'search_normalization_profile': search_normalization_profile, 'pages': pages})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_page_record`, `_canonical_sha256`, `frame.loc[:, PAGE_COLUMNS].to_dict`, `pages.append`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_index`
- `tests/unit/test_interpret_bess_zoning.py` — `_index`
- `tests/unit/test_structure_planning_regulation.py` — `_index`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_pages_frame`

**Signature**

```python
def _pages_frame(rows: list[dict[str, object]]) -> pd.DataFrame:
```

**Purpose**

Implements pages frame according to the exact implementation and guards in this file.

**Inputs**

- `rows` (`list[dict[str, object]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `frame` from `pd.DataFrame(rows, columns=PAGE_COLUMNS)`.
2. Computes `frame['page_number']` from `frame['page_number'].astype('int64')`.
3. Computes `frame['character_count']` from `frame['character_count'].astype('int64')`.
4. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `frame['character_count'].astype`, `frame['page_number'].astype`, `pd.DataFrame`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_index_hash_payload`

**Signature**

```python
def _index_hash_payload(index: PlanningRegulationIndex) -> dict[str, object]:
```

**Purpose**

Implements index hash payload according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'domain': 'landscout.planning_regulation.index', 'index_hash_schema_version': index.index_hash_schema_version, 'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'regulation_filename': index.regulation_filename, 'source_selection_method': index.source_selection_method, 'source_selection_sha256': index.source_selection_sha256, 'pdf_relative_path': index.pdf_relative_path, '…`.

**Algorithm**

1. Returns `{'domain': 'landscout.planning_regulation.index', 'index_hash_schema_version': index.index_hash_schema_version, 'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'regulation_filename': index.regulation_filename, 'source_selection_method': index.source_selection_method, 'source_selection_sha256': index.source_selection_sha256, 'pdf_re…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_content_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_index_content_sha256`

**Signature**

```python
def _index_content_sha256(index: PlanningRegulationIndex) -> str:
```

**Purpose**

Implements index content sha256 according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256(_index_hash_payload(index))`.

**Algorithm**

1. Returns `_canonical_sha256(_index_hash_payload(index))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `_index_hash_payload`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_index`
- `tests/unit/test_interpret_bess_zoning.py` — `_index`
- `tests/unit/test_structure_planning_regulation.py` — `_index`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_selection_sha256`

**Signature**

```python
def _source_selection_sha256(
    filename: str,
    method: str,
    zoning_evidence: _ZoningSourceEvidence,
    written_file: GpuWrittenFile,
    pdf_inventory: GpuExtractedFile,
) -> str:
```

**Purpose**

Implements source selection sha256 according to the exact implementation and guards in this file.

**Inputs**

- `filename` (`str`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `method` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_evidence` (`_ZoningSourceEvidence`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `written_file` (`GpuWrittenFile`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `pdf_inventory` (`GpuExtractedFile`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.planning_regulation.source_selection', 'regulation_filename': filename, 'source_selection_method': method, 'zoning': {'source_layer': zoning_evidence.source_layer, 'driver': zoning_evidence.driver, 'source_files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in zoning_evidence.files]}, 'written_file':…`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': 'landscout.planning_regulation.source_selection', 'regulation_filename': filename, 'source_selection_method': method, 'zoning': {'source_layer': zoning_evidence.source_layer, 'driver': zoning_evidence.driver, 'source_files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in …`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_pages`

**Signature**

```python
def _validate_pages(
    frame: pd.DataFrame,
    total_page_count: int,
    page_hash_schema_version: int,
    search_normalization_profile: str,
) -> None:
```

**Purpose**

Validates and rejects malformed pages according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `total_page_count` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `page_hash_schema_version` (`int`; required) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.
- `search_normalization_profile` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `not isinstance(frame, pd.DataFrame)`. When true: Raises `PlanningRegulationIndexError('Regulation pages must be a DataFrame')`.
2. Checks `tuple(frame.columns) != PAGE_COLUMNS`. When true: Raises `PlanningRegulationIndexError('Regulation page schema is not deterministic')`.
3. Checks `len(frame) != total_page_count`. When true: Raises `PlanningRegulationIndexError('Regulation page count is inconsistent')`.
4. Checks `frame['page_number'].tolist() != list(range(1, total_page_count + 1))`. When true: Raises `PlanningRegulationIndexError('Regulation page numbers must be unique and ordered from 1')`.
5. Checks `not frame['extraction_status'].isin({'TEXT', 'EMPTY', 'ERROR'}).all()`. When true: Raises `PlanningRegulationIndexError('Regulation extraction status is invalid')`.
6. Iterates `row` over `frame.to_dict('records')`. For each value: Calls `_strict_positive_integer(row['page_number'], 'page number')` for its validation or side effect. Computes `character_count` from `_strict_nonnegative_integer(row['character_count'], 'character count')`. Computes `raw_text` from `row['raw_text']`. Executes 12 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, pd.DataFrame)` is true.
- Rejects or diverts the path when `tuple(frame.columns) != PAGE_COLUMNS` is true.
- Rejects or diverts the path when `len(frame) != total_page_count` is true.
- Rejects or diverts the path when `frame['page_number'].tolist() != list(range(1, total_page_count + 1))` is true.
- Rejects or diverts the path when `not frame['extraction_status'].isin({'TEXT', 'EMPTY', 'ERROR'}).all()` is true.
- Rejects or diverts the path when `not isinstance(raw_text, str) or not isinstance(normalized, str)` is true.
- Rejects or diverts the path when `character_count != len(raw_text)` is true.
- Rejects or diverts the path when `normalized != _normalize_search_text(raw_text)` is true.
- Rejects or diverts the path when `status == 'TEXT' and (not normalized or not error_is_null)` is true.
- Rejects or diverts the path when `status == 'EMPTY' and (normalized or not error_is_null)` is true.
- Rejects or diverts the path when `status == 'ERROR' and (raw_text or normalized or (not isinstance(extraction_error, str)) or (not extraction_error))` is true.
- Rejects or diverts the path when `checksum != _page_content_sha256(row, page_hash_schema_version, search_normalization_profile)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_normalize_search_text`, `_page_content_sha256`, `_strict_nonnegative_integer`, `_strict_positive_integer`, `_validated_sha256`, `bool`, `frame.to_dict`, `frame['extraction_status'].isin`, `frame['extraction_status'].isin({'TEXT', 'EMPTY', 'ERROR'}).all`, `frame['page_number'].tolist`, `isinstance`, `len`, `list`, `pd.isna`, `range`, `tuple`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_index`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_pypdf_version`

**Signature**

```python
def _pypdf_version() -> str:
```

**Purpose**

Implements pypdf version according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `str`. Observed return expression(s): `version('pypdf')`.

**Algorithm**

1. Runs guarded operation: Returns `version('pypdf')`. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `version`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_index_planning_regulation`

**Signature**

```python
def _index_planning_regulation(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None = None,
) -> PlanningRegulationIndex:
```

**Purpose**

Index the source-validated primary written regulation page by page.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `regulation_filename` (`str | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationIndex`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `(document_id, archive_sha)` from `_validate_document_lineage(planning_document)`.
2. Computes `(filename, selection_method, zoning_evidence, written_file)` from `_resolve_regulation_filename(planning_document, regulation_filename)`.
3. Computes `(path, inventory)` from `_locate_regulation_pdf(planning_document, filename)`.
4. Computes `selection_sha` from `_source_selection_sha256(filename, selection_method, zoning_evidence, written_file, inventory)`.
5. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
6. Runs guarded operation: Enters managed context(s) `path.open('rb')` and executes: Computes `reader` from `PdfReader(stream, strict=False)`. Checks `reader.is_encrypted`. When true: Raises `PlanningRegulationIndexError('Encrypted regulation PDFs are not supported')`. Computes `total_page_count` from `len(reader.pages)`. Checks `total_page_count == 0`. When true: Raises `PlanningRegulationIndexError('Regulation PDF must contain at least one page')`. Executes 1 additional source-ordered statement(s). Handles `PlanningRegulationIndexError`, `Exception`.
7. Runs guarded operation: Computes `final_size` from `path.stat().st_size`. Handles `OSError`.
8. Computes `final_sha` from `_file_sha256(path)`.
9. Checks `final_size != inventory.size_bytes or final_sha != inventory.sha256`. When true: Raises `PlanningRegulationIndexError('Regulation PDF changed during text extraction')`.
10. Computes `pages` from `_pages_frame(rows)`.
11. Computes `result` from `PlanningRegulationIndex(document_id=document_id, archive_sha256=archive_sha, regulation_filename=filename, source_selection_method=selection_method, source_selection_sha256=selection_sha, pdf_relative_path=inventory.relative_path, pdf_size_bytes=inventory.size_bytes, pdf_sha256=final_sha, extraction_library='pypdf', e…`.
12. Computes `result` from `replace(result, index_content_sha256=_index_content_sha256(result))`.
13. Calls `validate_planning_regulation_index(result)` for its validation or side effect.
14. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `final_size != inventory.size_bytes or final_sha != inventory.sha256` is true.
- Rejects or diverts the path when `reader.is_encrypted` is true.
- Rejects or diverts the path when `total_page_count == 0` is true.
- Rejects or diverts the path when `not isinstance(raw_text, str)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PdfReader`, `PlanningRegulationIndex`, `PlanningRegulationIndexError`, `TypeError`, `_file_sha256`, `_index_content_sha256`, `_locate_regulation_pdf`, `_normalize_search_text`, `_page_content_sha256`, `_page_error`, `_pages_content_sha256`, `_pages_frame`, `_pypdf_version`, `_resolve_regulation_filename`, `_source_selection_sha256`, `_validate_document_lineage`, `isinstance`, `len`, `path.open`, `path.stat`, `range`, `reader.pages[page_index].extract_text`, `replace`, `rows.append`, `validate_planning_regulation_index`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `index_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `index_planning_regulation`

**Signature**

```python
def index_planning_regulation(
    planning_document: GpuPlanningDocument,
    regulation_filename: str | None = None,
) -> PlanningRegulationIndex:
```

**Purpose**

Index one source-validated written regulation with controlled failures.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `regulation_filename` (`str | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationIndex`. Observed return expression(s): `_index_planning_regulation(planning_document, regulation_filename)`.

**Algorithm**

1. Runs guarded operation: Returns `_index_planning_regulation(planning_document, regulation_filename)`. Handles `PlanningRegulationIndexError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_index_planning_regulation`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_one_page_index`
- `tests/unit/test_index_planning_regulation.py` — `test_duplicate_inventory_basename_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_explicit_filename_not_referenced_by_zoning_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_explicit_source_validated_selection_succeeds`
- `tests/unit/test_index_planning_regulation.py` — `test_extraction_and_search_do_not_mutate_inputs`
- `tests/unit/test_index_planning_regulation.py` — `test_filename_absent_from_inventory_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_filename_absent_from_written_files_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_index_integrity_mutations_fail`
- `tests/unit/test_index_planning_regulation.py` — `test_malformed_source_metadata_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py` — `test_missing_nomfic_field_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_multiple_nomfic_values_are_ambiguous`
- `tests/unit/test_index_planning_regulation.py` — `test_mutated_loaded_nomfic_is_rejected_before_selection`
- `tests/unit/test_index_planning_regulation.py` — `test_mutated_loaded_zoning_geometry_or_order_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_null_nomfic_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_page_states_numbering_and_hashes`
- `tests/unit/test_index_planning_regulation.py` — `test_path_outside_root_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_pdf_inventory_integrity_mismatch_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_pdf_reader_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py` — `test_source_nomfic_resolves_generic_filename`
- `tests/unit/test_index_planning_regulation.py` — `test_unchanged_zoning_source_is_revalidated_before_selection`
- `tests/unit/test_index_planning_regulation.py` — `test_unrelated_non_pdf_written_file_does_not_block_selection`
- `tests/unit/test_index_planning_regulation.py` — `test_unsafe_explicit_filename_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_version_discovery_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py` — `test_zero_page_pdf_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_zoning_source_bytes_changed_after_ingestion_are_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_zoning_source_inventory_integrity_mismatch_is_rejected`

**Tests**

- `tests/unit/test_index_planning_regulation.py::test_duplicate_inventory_basename_fails`
- `tests/unit/test_index_planning_regulation.py::test_explicit_filename_not_referenced_by_zoning_fails`
- `tests/unit/test_index_planning_regulation.py::test_explicit_source_validated_selection_succeeds`
- `tests/unit/test_index_planning_regulation.py::test_extraction_and_search_do_not_mutate_inputs`
- `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_inventory_fails`
- `tests/unit/test_index_planning_regulation.py::test_filename_absent_from_written_files_fails`
- `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail`
- `tests/unit/test_index_planning_regulation.py::test_malformed_source_metadata_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py::test_missing_nomfic_field_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_multiple_nomfic_values_are_ambiguous`
- `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_nomfic_is_rejected_before_selection`
- `tests/unit/test_index_planning_regulation.py::test_mutated_loaded_zoning_geometry_or_order_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_null_nomfic_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_page_states_numbering_and_hashes`
- `tests/unit/test_index_planning_regulation.py::test_path_outside_root_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_pdf_inventory_integrity_mismatch_fails`
- `tests/unit/test_index_planning_regulation.py::test_pdf_reader_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py::test_source_nomfic_resolves_generic_filename`
- `tests/unit/test_index_planning_regulation.py::test_unchanged_zoning_source_is_revalidated_before_selection`
- `tests/unit/test_index_planning_regulation.py::test_unrelated_non_pdf_written_file_does_not_block_selection`
- `tests/unit/test_index_planning_regulation.py::test_unsafe_explicit_filename_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_version_discovery_failure_is_controlled_and_chained`
- `tests/unit/test_index_planning_regulation.py::test_zero_page_pdf_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_zoning_source_bytes_changed_after_ingestion_are_rejected`
- `tests/unit/test_index_planning_regulation.py::test_zoning_source_inventory_integrity_mismatch_is_rejected`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_planning_regulation_index`

**Signature**

```python
def _validate_planning_regulation_index(index: PlanningRegulationIndex) -> None:
```

**Purpose**

Validates and rejects malformed planning regulation index according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `not isinstance(index, PlanningRegulationIndex)`. When true: Raises `PlanningRegulationIndexError('index must be a PlanningRegulationIndex')`.
2. Calls `_strict_string(index.document_id, 'regulation document ID')` for its validation or side effect.
3. Calls `_validated_sha256(index.archive_sha256, 'regulation archive SHA256')` for its validation or side effect.
4. Computes `filename` from `_validated_pdf_basename(index.regulation_filename)`.
5. Checks `index.source_selection_method not in {'ZONING_NOMFIC', 'EXPLICIT_ZONING_NOMFIC'}`. When true: Raises `PlanningRegulationIndexError('Regulation source-selection method is unsupported')`.
6. Calls `_validated_sha256(index.source_selection_sha256, 'source selection SHA256')` for its validation or side effect.
7. Computes `relative_pdf` from `_validated_relative_path(index.pdf_relative_path)`.
8. Checks `relative_pdf.name != filename`. When true: Raises `PlanningRegulationIndexError('Regulation filename differs from PDF relative path')`.
9. Calls `_strict_positive_integer(index.pdf_size_bytes, 'regulation PDF size')` for its validation or side effect.
10. Calls `_validated_sha256(index.pdf_sha256, 'regulation PDF SHA256')` for its validation or side effect.
11. Checks `index.extraction_library != 'pypdf'`. When true: Raises `PlanningRegulationIndexError('Regulation extraction library differs')`.
12. Calls `_strict_string(index.extraction_library_version, 'extraction library version')` for its validation or side effect.
13. Checks `index.search_normalization_profile != SEARCH_NORMALIZATION_PROFILE`. When true: Raises `PlanningRegulationIndexError('Regulation search normalization profile is unsupported')`.
14. Computes `page_schema` from `_supported_schema_version(index.page_hash_schema_version, PAGE_HASH_SCHEMA_VERSION, 'page hash schema version')`.
15. Calls `_supported_schema_version(index.index_hash_schema_version, INDEX_HASH_SCHEMA_VERSION, 'index hash schema version')` for its validation or side effect.
16. Computes `total` from `_strict_positive_integer(index.total_page_count, 'total page count')`.
17. Calls `_validate_pages(index.pages, total, page_schema, index.search_normalization_profile)` for its validation or side effect.
18. Computes `checksum` from `_validated_sha256(index.pages_content_sha256, 'pages content SHA256')`.
19. Checks `checksum != _pages_content_sha256(index.pages, page_schema, index.search_normalization_profile)`. When true: Raises `PlanningRegulationIndexError('Regulation pages envelope hash differs')`.
20. Computes `index_checksum` from `_validated_sha256(index.index_content_sha256, 'index content SHA256')`.
21. Checks `index_checksum != _index_content_sha256(index)`. When true: Raises `PlanningRegulationIndexError('Regulation index envelope hash differs')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(index, PlanningRegulationIndex)` is true.
- Rejects or diverts the path when `index.source_selection_method not in {'ZONING_NOMFIC', 'EXPLICIT_ZONING_NOMFIC'}` is true.
- Rejects or diverts the path when `relative_pdf.name != filename` is true.
- Rejects or diverts the path when `index.extraction_library != 'pypdf'` is true.
- Rejects or diverts the path when `index.search_normalization_profile != SEARCH_NORMALIZATION_PROFILE` is true.
- Rejects or diverts the path when `checksum != _pages_content_sha256(index.pages, page_schema, index.search_normalization_profile)` is true.
- Rejects or diverts the path when `index_checksum != _index_content_sha256(index)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_index_content_sha256`, `_pages_content_sha256`, `_strict_positive_integer`, `_strict_string`, `_supported_schema_version`, `_validate_pages`, `_validated_pdf_basename`, `_validated_relative_path`, `_validated_sha256`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `validate_planning_regulation_index`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_regulation_index`

**Signature**

```python
def validate_planning_regulation_index(index: PlanningRegulationIndex) -> None:
```

**Purpose**

Validate all page, metadata, and complete index integrity contracts.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_planning_regulation_index(index)` for its validation or side effect. Handles `PlanningRegulationIndexError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_validate_planning_regulation_index`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_index_planning_regulation`
- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_search_result`
- `src/landscout/stages/index_planning_regulation.py` — `search_planning_regulation`
- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_document_lock`
- `src/landscout/stages/structure_planning_regulation.py` — `_validate_result_self`
- `tests/unit/test_index_planning_regulation.py` — `test_complete_index_envelope_mutation_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_coordinated_page_mutation_fails_envelope_hash`
- `tests/unit/test_index_planning_regulation.py` — `test_index_integrity_mutations_fail`
- `tests/unit/test_index_planning_regulation.py` — `test_malformed_page_hash_schema_is_rejected_as_controlled_error`
- `tests/unit/test_index_planning_regulation.py` — `test_malformed_page_value_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py` — `test_page_states_numbering_and_hashes`
- `tests/unit/test_index_planning_regulation.py` — `test_unsupported_or_malformed_index_hash_schema_is_rejected`

**Tests**

- `tests/unit/test_index_planning_regulation.py::test_complete_index_envelope_mutation_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_coordinated_page_mutation_fails_envelope_hash`
- `tests/unit/test_index_planning_regulation.py::test_index_integrity_mutations_fail`
- `tests/unit/test_index_planning_regulation.py::test_malformed_page_hash_schema_is_rejected_as_controlled_error`
- `tests/unit/test_index_planning_regulation.py::test_malformed_page_value_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py::test_page_states_numbering_and_hashes`
- `tests/unit/test_index_planning_regulation.py::test_unsupported_or_malformed_index_hash_schema_is_rejected`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_terms`

**Signature**

```python
def _validated_terms(terms: Sequence[str]) -> tuple[tuple[str, str], ...]:
```

**Purpose**

Validates and returns canonical terms according to the exact implementation and guards in this file.

**Inputs**

- `terms` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[tuple[str, str], ...]`. Observed return expression(s): `tuple(result)`.

**Algorithm**

1. Checks `isinstance(terms, (str, bytes)) or not isinstance(terms, Sequence)`. When true: Raises `PlanningRegulationIndexError('Search terms must be a sequence of terms')`.
2. Defines `result` with annotation `list[tuple[str, str]]` from `[]`.
3. Defines `normalized_seen` with annotation `set[str]` from `set()`.
4. Iterates `term` over `terms`. For each value: Computes `raw_term` from `_strict_string(term, 'search term')`. Computes `normalized_term` from `_normalize_search_text(raw_term)`. Checks `not normalized_term or normalized_term in normalized_seen`. When true: Raises `PlanningRegulationIndexError('Search terms must be unique after normalization')`. Executes 2 additional source-ordered statement(s).
5. Returns `tuple(result)`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(terms, (str, bytes)) or not isinstance(terms, Sequence)` is true.
- Rejects or diverts the path when `not normalized_term or normalized_term in normalized_seen` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_normalize_search_text`, `_strict_string`, `isinstance`, `normalized_seen.add`, `result.append`, `set`, `tuple`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_search_result`
- `src/landscout/stages/index_planning_regulation.py` — `search_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_empty_hits`

**Signature**

```python
def _empty_hits() -> pd.DataFrame:
```

**Purpose**

Implements empty hits according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `pd.DataFrame({column: pd.Series(dtype='int64' if column in {'page_number', 'occurrence_count'} else 'object') for column in SEARCH_HIT_COLUMNS})`.

**Algorithm**

1. Returns `pd.DataFrame({column: pd.Series(dtype='int64' if column in {'page_number', 'occurrence_count'} else 'object') for column in SEARCH_HIT_COLUMNS})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.DataFrame`, `pd.Series`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_build_hits`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_hits`

**Signature**

```python
def _build_hits(
    index: PlanningRegulationIndex,
    terms: tuple[tuple[str, str], ...],
    context_characters: int,
) -> pd.DataFrame:
```

**Purpose**

Builds hits according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `terms` (`tuple[tuple[str, str], ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context_characters` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`; `_empty_hits()`.

**Algorithm**

1. Defines `hits` with annotation `list[dict[str, object]]` from `[]`.
2. Iterates `(raw_term, normalized_term)` over `terms`. For each value: Computes `pattern` from `escape(normalized_term)`. Iterates `page` over `index.pages.to_dict('records')`. For each value: Computes `raw_text` from `page['raw_text']`. Computes `(normalized_text, raw_spans)` from `_normalize_search_text_with_mapping(raw_text)`. Computes `matches` from `list(finditer(pattern, normalized_text))`. Executes 5 additional source-ordered statement(s).
3. Checks `not hits`. When true: Returns `_empty_hits()`.
4. Computes `frame` from `pd.DataFrame(hits, columns=SEARCH_HIT_COLUMNS)`.
5. Computes `frame['page_number']` from `frame['page_number'].astype('int64')`.
6. Computes `frame['occurrence_count']` from `frame['occurrence_count'].astype('int64')`.
7. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_empty_hits`, `_normalize_search_text_with_mapping`, `_raw_context`, `escape`, `finditer`, `first.end`, `first.start`, `frame['occurrence_count'].astype`, `frame['page_number'].astype`, `hits.append`, `index.pages.to_dict`, `len`, `list`, `max`, `min`, `pd.DataFrame`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_search_result`
- `src/landscout/stages/index_planning_regulation.py` — `search_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_hits_content_sha256`

**Signature**

```python
def _hits_content_sha256(
    index: PlanningRegulationIndex,
    requested_terms: tuple[str, ...],
    context_characters: int,
    hits: pd.DataFrame,
    search_hash_schema_version: int = SEARCH_HASH_SCHEMA_VERSION,
) -> str:
```

**Purpose**

Implements hits content sha256 according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `requested_terms` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context_characters` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `hits` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `search_hash_schema_version` (`int`; optional/default `SEARCH_HASH_SCHEMA_VERSION`) — integrity digest used to bind exact bytes or canonical content. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.planning_regulation.search', 'search_hash_schema_version': search_hash_schema_version, 'index_content_sha256': index.index_content_sha256, 'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'pdf_sha256': index.pdf_sha256, 'search_normalization_profile': index.search_normalization_profile, 'requested_terms': list(requested_terms), 'con…`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': 'landscout.planning_regulation.search', 'search_hash_schema_version': search_hash_schema_version, 'index_content_sha256': index.index_content_sha256, 'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'pdf_sha256': index.pdf_sha256, 'search_normalization_profile': index.search_normalization_profile, 'reque…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `hits.loc[:, SEARCH_HIT_COLUMNS].to_dict`, `len`, `list`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_validate_planning_regulation_search_result`
- `src/landscout/stages/index_planning_regulation.py` — `search_planning_regulation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `search_planning_regulation`

**Signature**

```python
def search_planning_regulation(
    index: PlanningRegulationIndex,
    terms: Sequence[str],
    *,
    context_characters: int = 80,
) -> PlanningRegulationSearchResult:
```

**Purpose**

Return sealed literal search hits with raw and normalized contexts.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `terms` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context_characters` (`int`; optional/default `80`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningRegulationSearchResult`. Observed return expression(s): `result`.

**Algorithm**

1. Calls `validate_planning_regulation_index(index)` for its validation or side effect.
2. Computes `validated_terms` from `_validated_terms(terms)`.
3. Computes `context` from `_strict_nonnegative_integer(context_characters, 'context_characters')`.
4. Computes `requested` from `tuple((raw for raw, _ in validated_terms))`.
5. Computes `hits` from `_build_hits(index, validated_terms, context)`.
6. Computes `result` from `PlanningRegulationSearchResult(document_id=index.document_id, archive_sha256=index.archive_sha256, pdf_sha256=index.pdf_sha256, search_normalization_profile=index.search_normalization_profile, search_hash_schema_version=SEARCH_HASH_SCHEMA_VERSION, index_content_sha256=index.index_content_sha256, requested_terms=reques…`.
7. Calls `validate_planning_regulation_search_result(index, result)` for its validation or side effect.
8. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationSearchResult`, `_build_hits`, `_hits_content_sha256`, `_strict_nonnegative_integer`, `_validated_terms`, `len`, `tuple`, `validate_planning_regulation_index`, `validate_planning_regulation_search_result`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `_valid_search_result`
- `tests/unit/test_index_planning_regulation.py` — `test_duplicate_normalized_search_terms_are_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_empty_search_result_has_stable_schema_and_lineage`
- `tests/unit/test_index_planning_regulation.py` — `test_extraction_and_search_do_not_mutate_inputs`
- `tests/unit/test_index_planning_regulation.py` — `test_invalid_search_term_is_rejected`
- `tests/unit/test_index_planning_regulation.py` — `test_literal_search_does_not_add_semantic_synonyms`
- `tests/unit/test_index_planning_regulation.py` — `test_raw_context_preserves_source_typography`
- `tests/unit/test_index_planning_regulation.py` — `test_search_result_envelope_is_valid_and_deterministic`
- `tests/unit/test_index_planning_regulation.py` — `test_zero_context_preserves_complete_raw_unicode_span`

**Tests**

- `tests/unit/test_index_planning_regulation.py::test_duplicate_normalized_search_terms_are_rejected`
- `tests/unit/test_index_planning_regulation.py::test_empty_search_result_has_stable_schema_and_lineage`
- `tests/unit/test_index_planning_regulation.py::test_extraction_and_search_do_not_mutate_inputs`
- `tests/unit/test_index_planning_regulation.py::test_invalid_search_term_is_rejected`
- `tests/unit/test_index_planning_regulation.py::test_literal_search_does_not_add_semantic_synonyms`
- `tests/unit/test_index_planning_regulation.py::test_raw_context_preserves_source_typography`
- `tests/unit/test_index_planning_regulation.py::test_search_result_envelope_is_valid_and_deterministic`
- `tests/unit/test_index_planning_regulation.py::test_zero_context_preserves_complete_raw_unicode_span`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_planning_regulation_search_result`

**Signature**

```python
def _validate_planning_regulation_search_result(
    index: PlanningRegulationIndex,
    result: PlanningRegulationSearchResult,
) -> None:
```

**Purpose**

Validates and rejects malformed planning regulation search result according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningRegulationSearchResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `validate_planning_regulation_index(index)` for its validation or side effect.
2. Checks `not isinstance(result, PlanningRegulationSearchResult)`. When true: Raises `PlanningRegulationIndexError('result must be a PlanningRegulationSearchResult')`.
3. Checks `result.document_id != index.document_id or result.archive_sha256 != index.archive_sha256 or result.pdf_sha256 != index.pdf_sha256 or (result.search_normalization_profile != index.search_normalization_profile) or (result.index_content_sha256 != index.index_content_sha256)`. When true: Raises `PlanningRegulationIndexError('Search-result lineage differs from index')`.
4. Computes `search_schema` from `_supported_schema_version(result.search_hash_schema_version, SEARCH_HASH_SCHEMA_VERSION, 'search hash schema version')`.
5. Checks `type(result.requested_terms) is not tuple`. When true: Raises `PlanningRegulationIndexError('Search-result requested_terms must be tuple[str, ...]')`.
6. Computes `validated_terms` from `_validated_terms(result.requested_terms)`.
7. Computes `context` from `_strict_nonnegative_integer(result.context_characters, 'context_characters')`.
8. Checks `not isinstance(result.hits, pd.DataFrame) or tuple(result.hits.columns) != SEARCH_HIT_COLUMNS`. When true: Raises `PlanningRegulationIndexError('Search-hit schema is not deterministic')`.
9. Computes `hit_count` from `_strict_nonnegative_integer(result.hit_count, 'hit count')`.
10. Checks `hit_count != len(result.hits)`. When true: Raises `PlanningRegulationIndexError('Search-result hit count differs')`.
11. Computes `allowed_pages` from `set(index.pages['page_number'].tolist())`.
12. Computes `allowed_terms` from `{normalized for _, normalized in validated_terms}`.
13. Defines `seen` with annotation `set[tuple[str, int]]` from `set()`.
14. Iterates `row` over `result.hits.to_dict('records')`. For each value: Checks `row['document_id'] != index.document_id or row['archive_sha256'] != index.archive_sha256 or row['pdf_sha256'] != index.pdf_sha256 or (row['search_normalization_profile'] != index.search_normalization_profile)`. When true: Raises `PlanningRegulationIndexError('Search-hit lineage differs from index')`. Computes `normalized_term` from `_strict_string(row['normalized_search_term'], 'normalized search term')`. Checks `normalized_term not in allowed_terms`. When true: Raises `PlanningRegulationIndexError('Search hit has an unrequested term')`. Executes 7 additional source-ordered statement(s).
15. Computes `requested` from `tuple((raw for raw, _ in validated_terms))`.
16. Computes `checksum` from `_validated_sha256(result.hits_content_sha256, 'hits content SHA256')`.
17. Checks `checksum != _hits_content_sha256(index, requested, context, result.hits, search_schema)`. When true: Raises `PlanningRegulationIndexError('Search-result content hash differs')`.
18. Computes `expected` from `_build_hits(index, validated_terms, context)`.
19. Checks `not result.hits.reset_index(drop=True).equals(expected)`. When true: Raises `PlanningRegulationIndexError('Search-result rows differ from deterministic source search')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(result, PlanningRegulationSearchResult)` is true.
- Rejects or diverts the path when `result.document_id != index.document_id or result.archive_sha256 != index.archive_sha256 or result.pdf_sha256 != index.pdf_sha256 or (result.search_normalization_profile != index.search_normalization_profile) or (result.index_content_sha256 != index.index_content_sha256)` is true.
- Rejects or diverts the path when `type(result.requested_terms) is not tuple` is true.
- Rejects or diverts the path when `not isinstance(result.hits, pd.DataFrame) or tuple(result.hits.columns) != SEARCH_HIT_COLUMNS` is true.
- Rejects or diverts the path when `hit_count != len(result.hits)` is true.
- Rejects or diverts the path when `checksum != _hits_content_sha256(index, requested, context, result.hits, search_schema)` is true.
- Rejects or diverts the path when `not result.hits.reset_index(drop=True).equals(expected)` is true.
- Rejects or diverts the path when `row['document_id'] != index.document_id or row['archive_sha256'] != index.archive_sha256 or row['pdf_sha256'] != index.pdf_sha256 or (row['search_normalization_profile'] != index.search_normalization_profile)` is true.
- Rejects or diverts the path when `normalized_term not in allowed_terms` is true.
- Rejects or diverts the path when `page_number not in allowed_pages` is true.
- Rejects or diverts the path when `pair in seen` is true.
- Rejects or diverts the path when `not isinstance(row['raw_context'], str) or not isinstance(row['normalized_context'], str)` is true.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_build_hits`, `_hits_content_sha256`, `_strict_nonnegative_integer`, `_strict_positive_integer`, `_strict_string`, `_supported_schema_version`, `_validated_sha256`, `_validated_terms`, `index.pages['page_number'].tolist`, `isinstance`, `len`, `result.hits.reset_index`, `result.hits.reset_index(drop=True).equals`, `result.hits.to_dict`, `seen.add`, `set`, `tuple`, `type`, `validate_planning_regulation_index`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `validate_planning_regulation_search_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_regulation_search_result`

**Signature**

```python
def validate_planning_regulation_search_result(
    index: PlanningRegulationIndex,
    result: PlanningRegulationSearchResult,
) -> None:
```

**Purpose**

Validate search lineage, schema, rows, hash, and source-derived contexts.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningRegulationSearchResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_planning_regulation_search_result(index, result)` for its validation or side effect. Handles `PlanningRegulationIndexError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningRegulationIndexError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningRegulationIndexError`, `_validate_planning_regulation_search_result`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `search_planning_regulation`
- `tests/unit/test_index_planning_regulation.py` — `test_empty_search_result_has_stable_schema_and_lineage`
- `tests/unit/test_index_planning_regulation.py` — `test_malformed_hit_value_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py` — `test_search_hit_lineage_mutation_fails`
- `tests/unit/test_index_planning_regulation.py` — `test_search_index_identity_schema_and_terms_are_sealed`
- `tests/unit/test_index_planning_regulation.py` — `test_search_requested_terms_must_be_an_immutable_exact_tuple`
- `tests/unit/test_index_planning_regulation.py` — `test_search_result_envelope_is_valid_and_deterministic`
- `tests/unit/test_index_planning_regulation.py` — `test_search_result_integrity_mutations_fail`

**Tests**

- `tests/unit/test_index_planning_regulation.py::test_empty_search_result_has_stable_schema_and_lineage`
- `tests/unit/test_index_planning_regulation.py::test_malformed_hit_value_raises_controlled_index_error`
- `tests/unit/test_index_planning_regulation.py::test_search_hit_lineage_mutation_fails`
- `tests/unit/test_index_planning_regulation.py::test_search_index_identity_schema_and_terms_are_sealed`
- `tests/unit/test_index_planning_regulation.py::test_search_requested_terms_must_be_an_immutable_exact_tuple`
- `tests/unit/test_index_planning_regulation.py::test_search_result_envelope_is_valid_and_deterministic`
- `tests/unit/test_index_planning_regulation.py::test_search_result_integrity_mutations_fail`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `EMPTY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `ERROR` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `NOMFIC` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `TEXT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `character_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `extraction_error` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `extraction_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `normalized_context` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `normalized_search_term` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `normalized_search_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `occurrence_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `page_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `page_number` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `pdf_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `raw_context` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `raw_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `search_normalization_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `search_term` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `planning` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
