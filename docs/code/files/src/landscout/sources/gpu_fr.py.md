# `src/landscout/sources/gpu_fr.py`

## File identity

- Repository path: `src/landscout/sources/gpu_fr.py`
- File type: Python source
- Primary responsibility: Discovers and verifies the authoritative GPU planning document, archive, spatial layers, written files, and provenance.
- Layer / domain: `source adapter` / `planning`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `ae581db5e8719611b98d3d57e2de9016b688bece5e7d1375f498660442d1ce06`

## 1. Purpose

Discovers and verifies the authoritative GPU planning document, archive, spatial layers, written files, and provenance.

## 2. Position in LandScout architecture

This file is a `source adapter` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import math` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import shutil` — required by the implementation paths and symbols documented below.
- `import sys` — required by the implementation paths and symbols documented below.
- `import unicodedata` — required by the implementation paths and symbols documented below.
- `import zipfile` — required by the implementation paths and symbols documented below.
- `from dataclasses import asdict, dataclass` — required by the implementation paths and symbols documented below.
- `from datetime import UTC, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from numbers import Integral` — required by the implementation paths and symbols documented below.
- `from pathlib import Path, PurePosixPath, PureWindowsPath` — required by the implementation paths and symbols documented below.
- `from shutil import copy2, copyfileobj` — required by the implementation paths and symbols documented below.
- `from typing import Annotated, Any, Literal` — required by the implementation paths and symbols documented below.
- `from urllib.error import HTTPError, URLError` — required by the implementation paths and symbols documented below.
- `from urllib.parse import quote, urlencode, urljoin, urlparse` — required by the implementation paths and symbols documented below.

### Third-party

- `import stat` — required by the implementation paths and symbols documented below.
- `from xml.etree import ElementTree` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pyogrio` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import ( BaseModel, ConfigDict, Field, HttpUrl, StringConstraints, ValidationError, field_validator, )` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.safe_http import open_safe_https` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `DEFAULT_CONFIG_PATH` | `Path("configs/sources/gpu_fr.yaml")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DEFAULT_CACHE_DIR` | `Path("data/cache/gpu")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DOWNLOAD_CHUNK_SIZE` | `1024 * 1024` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `USER_AGENT` | `"LandScout-AI/0.1"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXTRACTION_MANIFEST_NAME` | `".landscout-gpu-extraction.json"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXTRACTION_MANIFEST_SCHEMA_VERSION` | `2` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_WINDOWS_RESERVED_BASENAMES` | `{ "con", "prn", "aux", "nul", *(f"com{index}" for index in range(1, 10)), *(f"lpt{index}" for index in range(1, 10)), }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `GpuApiConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `base_url` | `HttpUrl` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |

**Validators and methods:**

- `_official_api` — `def _official_api(cls, value: HttpUrl) -> HttpUrl:`; decorators `field_validator('base_url'), classmethod`. The complete method algorithm appears in the function/method section.

### `GpuDownloadConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `strategy` | `DownloadStrategy` | `required` | `DownloadStrategy` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `partition_template` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_valid_partition_template` — `def _valid_partition_template(cls, value: str) -> str:`; decorators `field_validator('partition_template'), classmethod`. The complete method algorithm appears in the function/method section.

### `GpuCacheConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `max_age_hours` | `float` | `Field(ge=0, allow_inf_nan=False)` | `float` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GpuPilotConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `commune_code` | `CommuneCode` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |

**Validators and methods:**

- None.

### `GpuLogicalLayerConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `class_label` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `match_tokens` | `tuple[NonEmptyString, ...]` | `Field(min_length=1)` | `tuple[NonEmptyString, ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_unique_tokens` — `def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:`; decorators `field_validator('match_tokens'), classmethod`. The complete method algorithm appears in the function/method section.

### `GpuSpatialLayersConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `zoning` | `GpuLogicalLayerConfig` | `required` | `GpuLogicalLayerConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `prescription_surface` | `GpuLogicalLayerConfig` | `required` | `GpuLogicalLayerConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `prescription_line` | `GpuLogicalLayerConfig` | `required` | `GpuLogicalLayerConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `prescription_point` | `GpuLogicalLayerConfig` | `required` | `GpuLogicalLayerConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `information_surface` | `GpuLogicalLayerConfig` | `required` | `GpuLogicalLayerConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `information_line` | `GpuLogicalLayerConfig` | `required` | `GpuLogicalLayerConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `information_point` | `GpuLogicalLayerConfig` | `required` | `GpuLogicalLayerConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GpuSourceConfig`

**Purpose:** Strict configuration for official French GPU ingestion.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `provider` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `portal` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `country` | `Literal['FR']` | `required` | `Literal['FR']` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `api` | `GpuApiConfig` | `required` | `GpuApiConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `download` | `GpuDownloadConfig` | `required` | `GpuDownloadConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache` | `GpuCacheConfig` | `required` | `GpuCacheConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `pilot` | `GpuPilotConfig` | `required` | `GpuPilotConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `spatial_layers` | `GpuSpatialLayersConfig` | `required` | `GpuSpatialLayersConfig` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GpuError`

**Purpose:** Base class for controlled GPU source failures.

**Inheritance:** `RuntimeError`.

**Model form and mutability:** class inheriting from `RuntimeError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `GpuConfigError`

**Purpose:** Raised when GPU source configuration is invalid.

**Inheritance:** `GpuError`.

**Model form and mutability:** class inheriting from `GpuError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `GpuDiscoveryError`

**Purpose:** Raised when the current planning document cannot be resolved safely.

**Inheritance:** `GpuError`.

**Model form and mutability:** class inheriting from `GpuError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `GpuDownloadError`

**Purpose:** Raised when the GPU archive cannot be downloaded or cached safely.

**Inheritance:** `GpuError`.

**Model form and mutability:** class inheriting from `GpuError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `GpuArchiveError`

**Purpose:** Raised when a GPU archive or extraction is corrupt or unsafe.

**Inheritance:** `GpuError`.

**Model form and mutability:** class inheriting from `GpuError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `GpuSpatialInspectionError`

**Purpose:** Raised when required GPU spatial layers cannot be inspected safely.

**Inheritance:** `GpuError`.

**Model form and mutability:** class inheriting from `GpuError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `GpuWrittenFile`

**Purpose:** Groups the `GpuWrittenFile` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `filename` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `title` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `document_path` | `str | None` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `source_url` | `str | None` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |

**Validators and methods:**

- None.

### `GpuDocumentMetadata`

**Purpose:** Represents strict metadata used to reconstruct or validate a byte-bound cache/source object.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `provider` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `portal` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `commune_code` | `str` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `partition` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `document_family` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `document_type` | `str` | `required` | Categorical source, feature, or relation type constrained by the owning model or validator. |
| `document_title` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `status` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `legal_status` | `str` | `required` | Categorical factual, technical, policy, or diagnostic status; the owning constants/validators define the closed vocabulary. |
| `effective_status` | `str` | `required` | Categorical factual, technical, policy, or diagnostic status; the owning constants/validators define the closed vocabulary. |
| `version` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `archive_name` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `publication_timestamp` | `str | None` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `update_timestamp` | `str | None` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `revision_date` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `producer` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `standard_model` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `projection` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `metadata_identifier` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `written_files` | `tuple[GpuWrittenFile, ...]` | `required` | `tuple[GpuWrittenFile, ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GpuArchiveDownload`

**Purpose:** Carries an immutable downloaded-source lineage envelope including byte identity and cache status.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `document` | `GpuDocumentMetadata` | `required` | `GpuDocumentMetadata` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `download_timestamp` | `str` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `filename` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `archive_format` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `file_size` | `int` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `path` | `Path` | `required` | `Path` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache_hit` | `bool` | `required` | Boolean recording whether verified local bytes were reused instead of acquired during this call. |

**Validators and methods:**

- None.

### `GpuExtractedFile`

**Purpose:** Groups the `GpuExtractedFile` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `relative_path` | `str` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `file_type` | `str` | `required` | Categorical source, feature, or relation type constrained by the owning model or validator. |
| `size_bytes` | `int` | `required` | `int` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `category` | `FileCategory` | `required` | `FileCategory` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GpuExtraction`

**Purpose:** Carries an immutable extraction envelope binding extracted files to their source archive.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `archive` | `GpuArchiveDownload` | `required` | `GpuArchiveDownload` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `extraction_root` | `Path` | `required` | `Path` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `files` | `tuple[GpuExtractedFile, ...]` | `required` | `tuple[GpuExtractedFile, ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `standard_models` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache_hit` | `bool` | `required` | Boolean recording whether verified local bytes were reused instead of acquired during this call. |

**Validators and methods:**

- None.

### `GpuSpatialLayerReference`

**Purpose:** Groups the `GpuSpatialLayerReference` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `dataset_path` | `Path` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `source_layer` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `driver` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GpuLayerSummary`

**Purpose:** Carries deterministic factual counts, schema, or geometry summary data used to validate a frame or source.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `source_document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_layer` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `crs` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `feature_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `columns` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `dtypes` | `tuple[tuple[str, str], ...]` | `required` | `tuple[tuple[str, str], ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `null_counts` | `tuple[tuple[str, int], ...]` | `required` | `tuple[tuple[str, int], ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `geometry_types` | `tuple[tuple[str, int], ...]` | `required` | `tuple[tuple[str, int], ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `null_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `empty_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `invalid_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |

**Validators and methods:**

- None.

### `GpuInspectedLayer`

**Purpose:** Groups the `GpuInspectedLayer` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `logical_name` | `LogicalLayerName` | `required` | `LogicalLayerName` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `reference` | `GpuSpatialLayerReference` | `required` | `GpuSpatialLayerReference` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `data` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `summary` | `GpuLayerSummary` | `required` | `GpuLayerSummary` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GpuSpatialSourceFileIntegrity`

**Purpose:** One verified physical member of an extracted GPU spatial dataset.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `relative_path` | `str` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `file_type` | `str` | `required` | Categorical source, feature, or relation type constrained by the owning model or validator. |
| `size_bytes` | `int` | `required` | `int` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `category` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GpuValidatedSpatialLayerSource`

**Purpose:** Freshly reloaded GPU layer plus its extraction-inventory evidence.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `logical_name` | `LogicalLayerName` | `required` | `LogicalLayerName` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_layer` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `driver` | `str` | `required` | `str` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `dataset_relative_path` | `str` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `source_crs` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `feature_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `files` | `tuple[GpuSpatialSourceFileIntegrity, ...]` | `required` | `tuple[GpuSpatialSourceFileIntegrity, ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `ogr_fids` | `tuple[int, ...]` | `required` | `tuple[int, ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `data` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GpuPlanningDocument`

**Purpose:** Groups the `GpuPlanningDocument` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `extraction` | `GpuExtraction` | `required` | `GpuExtraction` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `all_spatial_layers` | `tuple[GpuSpatialLayerReference, ...]` | `required` | `tuple[GpuSpatialLayerReference, ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `zoning` | `GpuInspectedLayer` | `required` | `GpuInspectedLayer` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `related_layers` | `tuple[GpuInspectedLayer, ...]` | `required` | `tuple[GpuInspectedLayer, ...]` state used by `src/landscout/sources/gpu_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `GpuApiConfig._official_api`

**Signature**

```python
def _official_api(cls, value: HttpUrl) -> HttpUrl:
```

**Purpose**

Implements official api according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`HttpUrl`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `HttpUrl`. Observed return expression(s): `value`.

**Algorithm**

1. Computes `parsed` from `urlparse(str(value))`.
2. Checks `parsed.scheme != 'https' or parsed.hostname != 'www.geoportail-urbanisme.gouv.fr' or parsed.port not in {None, 443} or (parsed.username is not None) or (parsed.password is not None) or (parsed.path.rstrip('/') != '/api') or parsed.params or parsed.query or parsed.fragment`. When true: Raises `ValueError('GPU API URL must use the exact official HTTPS /api base')`.
3. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `parsed.scheme != 'https' or parsed.hostname != 'www.geoportail-urbanisme.gouv.fr' or parsed.port not in {None, 443} or (parsed.username is not None) or (parsed.password is not None) or (parsed.path.rstrip('/') != '/api') or parsed.params or parsed.query or parsed.fragment` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `field_validator`, `parsed.path.rstrip`, `str`, `urlparse`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `GpuDownloadConfig._valid_partition_template`

**Signature**

```python
def _valid_partition_template(cls, value: str) -> str:
```

**Purpose**

Implements valid partition template according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `value != value.strip() or value.count('{code_insee}') != 1`. When true: Raises `ValueError('partition_template must contain exactly one {code_insee} placeholder')`.
2. Runs guarded operation: Computes `rendered` from `value.format(code_insee='31395')`. Handles `(KeyError, ValueError)`.
3. Checks `not rendered or '/' in rendered or '\\' in rendered`. When true: Raises `ValueError('partition_template must render one safe path component')`.
4. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `value != value.strip() or value.count('{code_insee}') != 1` is true.
- Rejects or diverts the path when `not rendered or '/' in rendered or '\\' in rendered` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `field_validator`, `value.count`, `value.format`, `value.strip`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `GpuLogicalLayerConfig._unique_tokens`

**Signature**

```python
def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:
```

**Purpose**

Implements unique tokens according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `values` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `values`.

**Algorithm**

1. Computes `normalized` from `tuple((_normalize_words(value) for value in values))`.
2. Checks `any((not value for value in normalized))`. When true: Raises `ValueError('Layer match tokens must contain letters or digits')`.
3. Checks `len(normalized) != len(set(normalized))`. When true: Raises `ValueError('Layer match tokens must be unique after normalization')`.
4. Returns `values`.

**Validation and invariants**

- Rejects or diverts the path when `any((not value for value in normalized))` is true.
- Rejects or diverts the path when `len(normalized) != len(set(normalized))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_normalize_words`, `any`, `field_validator`, `len`, `set`, `tuple`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalize_words`

**Signature**

```python
def _normalize_words(value: str) -> str:
```

**Purpose**

Normalizes words according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `'_'.join(re.findall('[a-z0-9]+', ascii_value.casefold()))`.

**Algorithm**

1. Computes `decomposed` from `unicodedata.normalize('NFKD', value)`.
2. Computes `ascii_value` from `''.join((char for char in decomposed if not unicodedata.combining(char)))`.
3. Returns `'_'.join(re.findall('[a-z0-9]+', ascii_value.casefold()))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `''.join`, `'_'.join`, `ascii_value.casefold`, `re.findall`, `unicodedata.combining`, `unicodedata.normalize`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `GpuLogicalLayerConfig._unique_tokens`
- `src/landscout/sources/gpu_fr.py` — `_discover_logical_layer`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_gpu_source_config`

**Signature**

```python
def load_gpu_source_config(path: Path = DEFAULT_CONFIG_PATH) -> GpuSourceConfig:
```

**Purpose**

Load and validate the strict GPU source configuration.

**Inputs**

- `path` (`Path`; optional/default `DEFAULT_CONFIG_PATH`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuSourceConfig`. Observed return expression(s): `GpuSourceConfig.model_validate(payload)`.

**Algorithm**

1. Checks `not path.is_file()`. When true: Raises `GpuConfigError(f'GPU source configuration does not exist: {path}')`.
2. Runs guarded operation: Computes `payload` from `yaml.safe_load(path.read_text(encoding='utf-8'))`. Checks `not isinstance(payload, dict)`. When true: Raises `TypeError('GPU source configuration must be a mapping')`. Returns `GpuSourceConfig.model_validate(payload)`. Handles `(OSError, TypeError, yaml.YAMLError, ValidationError)`.

**Validation and invariants**

- Rejects or diverts the path when `not path.is_file()` is true.
- Rejects or diverts the path when `not isinstance(payload, dict)` is true.

**Exceptions**

- Explicitly raises: `GpuConfigError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuConfigError`, `GpuSourceConfig.model_validate`, `TypeError`, `isinstance`, `path.is_file`, `path.read_text`, `yaml.safe_load`.

**Known repository callers**

- `tests/unit/test_gpu_fr.py` — `_config`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_source_config`

**Signature**

```python
def _validated_source_config(config: object) -> GpuSourceConfig:
```

**Purpose**

Validates and returns canonical source config according to the exact implementation and guards in this file.

**Inputs**

- `config` (`object`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuSourceConfig`. Observed return expression(s): `GpuSourceConfig.model_validate(config.model_dump(mode='python'))`.

**Algorithm**

1. Runs guarded operation: Checks `type(config) is not GpuSourceConfig`. When true: Raises `TypeError('GPU source config type is invalid')`. Returns `GpuSourceConfig.model_validate(config.model_dump(mode='python'))`. Handles `(AttributeError, TypeError, ValidationError, ValueError)`.

**Validation and invariants**

- Rejects or diverts the path when `type(config) is not GpuSourceConfig` is true.

**Exceptions**

- Explicitly raises: `GpuConfigError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuConfigError`, `GpuSourceConfig.model_validate`, `TypeError`, `config.model_dump`, `type`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `build_gpu_document_list_url`
- `src/landscout/sources/gpu_fr.py` — `build_gpu_partition_download_url`
- `src/landscout/sources/gpu_fr.py` — `build_gpu_partition`
- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`
- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `build_gpu_partition`

**Signature**

```python
def build_gpu_partition(config: GpuSourceConfig, commune_code: str | None = None) -> str:
```

**Purpose**

Builds gpu partition according to the exact implementation and guards in this file.

**Inputs**

- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `commune_code` (`str | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `validated_config.download.partition_template.format(code_insee=code)`.

**Algorithm**

1. Computes `validated_config` from `_validated_source_config(config)`.
2. Computes `code` from `commune_code or validated_config.pilot.commune_code`.
3. Checks `not isinstance(code, str) or re.fullmatch('[0-9]{5}', code) is None`. When true: Raises `GpuConfigError('GPU commune code must contain exactly five digits')`.
4. Returns `validated_config.download.partition_template.format(code_insee=code)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(code, str) or re.fullmatch('[0-9]{5}', code) is None` is true.

**Exceptions**

- Explicitly raises: `GpuConfigError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `validated_config.download.partition_template.format`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuConfigError`, `_validated_source_config`, `isinstance`, `re.fullmatch`, `validated_config.download.partition_template.format`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_validate_gpu_document_for_config`
- `src/landscout/sources/gpu_fr.py` — `build_gpu_document_list_url`
- `src/landscout/sources/gpu_fr.py` — `build_gpu_partition_download_url`
- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`
- `tests/unit/test_gpu_fr.py` — `test_valid_config_and_urls`

**Tests**

- `tests/unit/test_gpu_fr.py::test_valid_config_and_urls`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_api_url`

**Signature**

```python
def _api_url(config: GpuSourceConfig, path: str) -> str:
```

**Purpose**

Implements api url according to the exact implementation and guards in this file.

**Inputs**

- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `path` (`str`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `urljoin(f"{str(config.api.base_url).rstrip('/')}/", path.lstrip('/'))`.

**Algorithm**

1. Returns `urljoin(f"{str(config.api.base_url).rstrip('/')}/", path.lstrip('/'))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `path.lstrip`, `str`, `str(config.api.base_url).rstrip`, `urljoin`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_validate_gpu_document_for_config`
- `src/landscout/sources/gpu_fr.py` — `_written_files`
- `src/landscout/sources/gpu_fr.py` — `build_gpu_document_list_url`
- `src/landscout/sources/gpu_fr.py` — `build_gpu_partition_download_url`
- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `build_gpu_document_list_url`

**Signature**

```python
def build_gpu_document_list_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
```

**Purpose**

Builds gpu document list url according to the exact implementation and guards in this file.

**Inputs**

- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `commune_code` (`str | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `f"{_api_url(validated_config, 'document')}?{query}"`.

**Algorithm**

1. Computes `validated_config` from `_validated_source_config(config)`.
2. Computes `query` from `urlencode({'partition': build_gpu_partition(validated_config, commune_code), 'page': 0, 'limit': 100})`.
3. Returns `f"{_api_url(validated_config, 'document')}?{query}"`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_api_url`, `_validated_source_config`, `build_gpu_partition`, `urlencode`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`
- `tests/unit/test_gpu_fr.py` — `test_valid_config_and_urls`

**Tests**

- `tests/unit/test_gpu_fr.py::test_valid_config_and_urls`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `build_gpu_partition_download_url`

**Signature**

```python
def build_gpu_partition_download_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
```

**Purpose**

Builds gpu partition download url according to the exact implementation and guards in this file.

**Inputs**

- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `commune_code` (`str | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_api_url(validated_config, f'document/download-by-partition/{partition}')`.

**Algorithm**

1. Computes `validated_config` from `_validated_source_config(config)`.
2. Computes `partition` from `quote(build_gpu_partition(validated_config, commune_code), safe='')`.
3. Returns `_api_url(validated_config, f'document/download-by-partition/{partition}')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_api_url`, `_validated_source_config`, `build_gpu_partition`, `quote`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_validate_gpu_document_for_config`
- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`
- `tests/unit/test_gpu_fr.py` — `test_valid_config_and_urls`

**Tests**

- `tests/unit/test_gpu_fr.py::test_valid_config_and_urls`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_request_json`

**Signature**

```python
def _request_json(url: str, timeout: float) -> Any:
```

**Purpose**

Implements request json according to the exact implementation and guards in this file.

**Inputs**

- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; required) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Any`. Observed return expression(s): `json.loads(response.read().decode('utf-8'))`.

**Algorithm**

1. Runs guarded operation: Enters managed context(s) `open_safe_https(url, timeout=timeout, headers={'Accept': 'application/json', 'User-Agent': USER_AGENT})` and executes: Returns `json.loads(response.read().decode('utf-8'))`. Handles `(HTTPError, URLError, OSError, UnicodeDecodeError, json.JSONDecodeError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `GpuDiscoveryError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `open_safe_https`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuDiscoveryError`, `json.loads`, `open_safe_https`, `response.read`, `response.read().decode`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_required_string`

**Signature**

```python
def _required_string(payload: dict[str, Any], key: str, label: str) -> str:
```

**Purpose**

Implements required string according to the exact implementation and guards in this file.

**Inputs**

- `payload` (`dict[str, Any]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `key` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Computes `value` from `payload.get(key)`.
2. Checks `not isinstance(value, str) or not value.strip()`. When true: Raises `GpuDiscoveryError(f'GPU {label} is missing or invalid')`.
3. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value.strip()` is true.

**Exceptions**

- Explicitly raises: `GpuDiscoveryError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuDiscoveryError`, `isinstance`, `payload.get`, `value.strip`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_written_files`
- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_optional_string`

**Signature**

```python
def _optional_string(payload: dict[str, Any], *keys: str) -> str | None:
```

**Purpose**

Implements optional string according to the exact implementation and guards in this file.

**Inputs**

- `payload` (`dict[str, Any]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*keys` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str | None`. Observed return expression(s): `None`; `text`.

**Algorithm**

1. Iterates `key` over `keys`. For each value: Computes `value` from `payload.get(key)`. Checks `value is None`. When true: Executes `continue` control flow. Checks `not isinstance(value, (str, int, float)) or isinstance(value, bool)`. When true: Raises `GpuDiscoveryError(f'GPU metadata field {key} has an invalid value')`. Executes 2 additional source-ordered statement(s).
2. Returns `None`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, (str, int, float)) or isinstance(value, bool)` is true.

**Exceptions**

- Explicitly raises: `GpuDiscoveryError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuDiscoveryError`, `isinstance`, `payload.get`, `str`, `text.strip`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_written_files`
- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_written_files`

**Signature**

```python
def _written_files(
    details: dict[str, Any],
    payload: Any,
    document_id: str,
    config: GpuSourceConfig,
) -> tuple[GpuWrittenFile, ...]:
```

**Purpose**

Implements written files according to the exact implementation and guards in this file.

**Inputs**

- `details` (`dict[str, Any]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `payload` (`Any`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `document_id` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuWrittenFile, ...]`. Observed return expression(s): `tuple(sorted(result, key=lambda item: item.filename.casefold()))`.

**Algorithm**

1. Checks `not isinstance(payload, list)`. When true: Raises `GpuDiscoveryError('GPU written-file metadata is not a list')`.
2. Computes `materials` from `details.get('writingMaterials')`.
3. Computes `material_urls` from `materials if isinstance(materials, dict) else {}`.
4. Defines `result` with annotation `list[GpuWrittenFile]` from `[]`.
5. Defines `seen` with annotation `set[str]` from `set()`.
6. Iterates `item` over `payload`. For each value: Checks `not isinstance(item, dict)`. When true: Raises `GpuDiscoveryError('GPU written-file entry is invalid')`. Computes `filename` from `_required_string(item, 'name', 'written filename')`. Checks `filename in seen`. When true: Raises `GpuDiscoveryError(f'Duplicate GPU written filename: {filename}')`. Executes 5 additional source-ordered statement(s).
7. Returns `tuple(sorted(result, key=lambda item: item.filename.casefold()))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, list)` is true.
- Rejects or diverts the path when `not isinstance(item, dict)` is true.
- Rejects or diverts the path when `filename in seen` is true.
- Rejects or diverts the path when `source_url is not None and source_url != expected_source_url` is true.

**Exceptions**

- Explicitly raises: `GpuDiscoveryError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuDiscoveryError`, `GpuWrittenFile`, `_api_url`, `_optional_string`, `_required_string`, `details.get`, `isinstance`, `item.filename.casefold`, `material_urls.get`, `quote`, `result.append`, `seen.add`, `set`, `sorted`, `tuple`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `discover_current_gpu_document`

**Signature**

```python
def discover_current_gpu_document(
    config: GpuSourceConfig, commune_code: str | None = None, timeout: float = 60.0
) -> GpuDocumentMetadata:
```

**Purpose**

Resolve exactly one official production, approved and in-force DU.

**Inputs**

- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `commune_code` (`str | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; optional/default `60.0`) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuDocumentMetadata`. Observed return expression(s): `GpuDocumentMetadata(provider=validated_config.provider, portal=validated_config.portal, commune_code=code, partition=partition, document_id=document_id, document_family='DU', document_type=document_type, document_title=_optional_string(details, 'title'), status=_required_string(details, 'status', 'status'), legal_status=_required_string(details, 'legalStatus', 'legal status'), effective_status=_r…`.

**Algorithm**

1. Runs guarded operation: Computes `validated_config` from `_validated_source_config(config)`. Handles `GpuConfigError`.
2. Computes `code` from `commune_code or validated_config.pilot.commune_code`.
3. Computes `partition` from `build_gpu_partition(validated_config, code)`.
4. Computes `listing` from `_request_json(build_gpu_document_list_url(validated_config, code), timeout)`.
5. Checks `not isinstance(listing, list)`. When true: Raises `GpuDiscoveryError('GPU document listing is not a list')`.
6. Defines `current` with annotation `list[dict[str, Any]]` from `[]`.
7. Iterates `item` over `listing`. For each value: Checks `not isinstance(item, dict)`. When true: Executes `continue` control flow. Computes `grid` from `item.get('grid')`. Computes `grid_code` from `grid.get('name') if isinstance(grid, dict) else None`. Executes 1 additional source-ordered statement(s).
8. Checks `not current`. When true: Raises `GpuDiscoveryError(f'No current approved and in-force GPU document for {partition}')`.
9. Checks `len(current) != 1`. When true: Raises `GpuDiscoveryError(f'Ambiguous current GPU document selection for {partition}: {len(current)}')`.
10. Computes `selected` from `current[0]`.
11. Computes `document_id` from `_required_string(selected, 'id', 'document ID')`.
12. Computes `archive_name` from `_required_string(selected, 'originalName', 'archive name')`.
13. Computes `listing_type` from `_required_string(selected, 'type', 'listing document type')`.
14. Runs guarded operation: Computes `archive_filename` from `_safe_gpu_archive_filename(archive_name)`. Handles `GpuDownloadError`.
15. Computes `details_url` from `_api_url(validated_config, f"document/{quote(document_id, safe='')}/details")`.
16. Computes `files_url` from `_api_url(validated_config, f"document/{quote(document_id, safe='')}/files")`.
17. Computes `details_payload` from `_request_json(details_url, timeout)`.
18. Checks `not isinstance(details_payload, dict)`. When true: Raises `GpuDiscoveryError('GPU document details are not an object')`.
19. Computes `details` from `details_payload`.
20. Checks `details.get('id') != document_id or details.get('originalName') != archive_name`. When true: Raises `GpuDiscoveryError('GPU document details do not match the selected document')`.
21. Computes `expected_state` from `{'status': 'document.production', 'legalStatus': 'APPROVED', 'effectiveStatus': 'EN_VIGUEUR'}`.
22. Checks `any((details.get(key) != value for key, value in expected_state.items()))`. When true: Raises `GpuDiscoveryError('GPU document details no longer describe a current approved and in-force document')`.
23. Computes `detail_grid` from `details.get('grid')`.
24. Checks `not isinstance(detail_grid, dict) or detail_grid.get('name') != code`. When true: Raises `GpuDiscoveryError('GPU document details do not match the commune')`.
25. Checks `details.get('name') != partition`. When true: Raises `GpuDiscoveryError('GPU document details do not match the partition')`.
26. Computes `expected_details_archive_url` from `_api_url(validated_config, f"document/{quote(document_id, safe='')}/download/{quote(archive_filename, safe='')}")`.
27. Checks `details.get('archiveUrl') != expected_details_archive_url`. When true: Raises `GpuDiscoveryError('GPU document archive URL is not the exact official HTTPS API URL')`.
28. Computes `document_type` from `_required_string(details, 'type', 'document type')`.
29. Checks `listing_type != document_type`. When true: Raises `GpuDiscoveryError('GPU document type changed between listing and details')`.
30. Computes `files_payload` from `_request_json(files_url, timeout)`.
31. Computes `source_url` from `build_gpu_partition_download_url(validated_config, code)`.
32. Returns `GpuDocumentMetadata(provider=validated_config.provider, portal=validated_config.portal, commune_code=code, partition=partition, document_id=document_id, document_family='DU', document_type=document_type, document_title=_optional_string(details, 'title'), status=_required_string(details, 'status', 'status'), legal_status=_required_string(details, 'legalStatu…`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(listing, list)` is true.
- Rejects or diverts the path when `not current` is true.
- Rejects or diverts the path when `len(current) != 1` is true.
- Rejects or diverts the path when `not isinstance(details_payload, dict)` is true.
- Rejects or diverts the path when `details.get('id') != document_id or details.get('originalName') != archive_name` is true.
- Rejects or diverts the path when `any((details.get(key) != value for key, value in expected_state.items()))` is true.
- Rejects or diverts the path when `not isinstance(detail_grid, dict) or detail_grid.get('name') != code` is true.
- Rejects or diverts the path when `details.get('name') != partition` is true.
- Rejects or diverts the path when `details.get('archiveUrl') != expected_details_archive_url` is true.
- Rejects or diverts the path when `listing_type != document_type` is true.

**Exceptions**

- Explicitly raises: `GpuDiscoveryError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_request_json`, `build_gpu_partition_download_url`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuDiscoveryError`, `GpuDocumentMetadata`, `_api_url`, `_optional_string`, `_request_json`, `_required_string`, `_safe_gpu_archive_filename`, `_validated_source_config`, `_written_files`, `any`, `build_gpu_document_list_url`, `build_gpu_partition`, `build_gpu_partition_download_url`, `current.append`, `detail_grid.get`, `details.get`, `expected_state.items`, `grid.get`, `isinstance`, `item.get`, `len`, `quote`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `ingest_gpu_planning_document`
- `tests/unit/test_gpu_fr.py` — `_document`
- `tests/unit/test_gpu_fr.py` — `test_ambiguous_current_documents_are_rejected`
- `tests/unit/test_gpu_fr.py` — `test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py` — `test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py` — `test_missing_document_identity_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_mutated_loaded_api_origin_is_rejected_before_discovery_network`
- `tests/unit/test_gpu_fr.py` — `test_no_current_document_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py` — `test_written_material_url_must_be_exact_official_https_api_url`

**Tests**

- `tests/unit/test_gpu_fr.py::test_ambiguous_current_documents_are_rejected`
- `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name`
- `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing`
- `tests/unit/test_gpu_fr.py::test_missing_document_identity_is_rejected`
- `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network`
- `tests/unit/test_gpu_fr.py::test_no_current_document_is_rejected`
- `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance`
- `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_safe_gpu_archive_filename`

**Signature**

```python
def _safe_gpu_archive_filename(archive_name: object) -> str:
```

**Purpose**

Implements safe gpu archive filename according to the exact implementation and guards in this file.

**Inputs**

- `archive_name` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `filename`.

**Algorithm**

1. Checks `not isinstance(archive_name, str)`. When true: Raises `GpuDownloadError('GPU archive name must be a string')`.
2. Checks `not archive_name or archive_name != archive_name.strip()`. When true: Raises `GpuDownloadError('GPU archive name is empty or has edge whitespace')`.
3. Checks `any((ord(character) < 32 or ord(character) == 127 for character in archive_name))`. When true: Raises `GpuDownloadError('GPU archive name contains control characters')`.
4. Computes `normalized` from `unicodedata.normalize('NFKC', archive_name)`.
5. Checks `normalized in {'.', '..'} or '/' in normalized or '\\' in normalized or PurePosixPath(normalized).is_absolute() or PureWindowsPath(normalized).is_absolute() or bool(PureWindowsPath(normalized).drive) or normalized.endswith((' ', '.')) or any((character in '<>:"/\\|?*' for character in normalized))`. When true: Raises `GpuDownloadError('GPU archive name is not a safe local basename')`.
6. Checks `normalized.casefold().endswith('.zip')`. When true: Computes `basename` from `archive_name[:-4]`. Computes `normalized_basename` from `normalized[:-4]`. Checks `normalized_basename.casefold().endswith('.zip')`. When true: Raises `GpuDownloadError('GPU archive name contains repeated .zip suffixes')`. Otherwise: Computes `basename` from `archive_name`. Computes `normalized_basename` from `normalized`.
7. Checks `not basename or normalized_basename in {'.', '..'} or normalized_basename.endswith((' ', '.'))`. When true: Raises `GpuDownloadError('GPU archive name has no safe logical basename')`.
8. Computes `windows_stem` from `normalized_basename.split('.', 1)[0].casefold()`.
9. Checks `windows_stem in _WINDOWS_RESERVED_BASENAMES`. When true: Raises `GpuDownloadError('GPU archive name is reserved on Windows')`.
10. Computes `filename` from `f'{basename}.zip'`.
11. Checks `len(unicodedata.normalize('NFKC', filename).encode('utf-16-le')) // 2 > 255`. When true: Raises `GpuDownloadError('GPU archive filename exceeds Windows component limits')`.
12. Returns `filename`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(archive_name, str)` is true.
- Rejects or diverts the path when `not archive_name or archive_name != archive_name.strip()` is true.
- Rejects or diverts the path when `any((ord(character) < 32 or ord(character) == 127 for character in archive_name))` is true.
- Rejects or diverts the path when `normalized in {'.', '..'} or '/' in normalized or '\\' in normalized or PurePosixPath(normalized).is_absolute() or PureWindowsPath(normalized).is_absolute() or bool(PureWindowsPath(normalized).drive) or normalized.endswith((' ', '.')) or any((character in '<>:"/\\|?*' for character in normalized))` is true.
- Rejects or diverts the path when `normalized.casefold().endswith('.zip')` is true.
- Rejects or diverts the path when `not basename or normalized_basename in {'.', '..'} or normalized_basename.endswith((' ', '.'))` is true.
- Rejects or diverts the path when `windows_stem in _WINDOWS_RESERVED_BASENAMES` is true.
- Rejects or diverts the path when `len(unicodedata.normalize('NFKC', filename).encode('utf-16-le')) // 2 > 255` is true.
- Rejects or diverts the path when `normalized_basename.casefold().endswith('.zip')` is true.

**Exceptions**

- Explicitly raises: `GpuDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuDownloadError`, `PurePosixPath`, `PurePosixPath(normalized).is_absolute`, `PureWindowsPath`, `PureWindowsPath(normalized).is_absolute`, `any`, `archive_name.strip`, `bool`, `isinstance`, `len`, `normalized.casefold`, `normalized.casefold().endswith`, `normalized.endswith`, `normalized_basename.casefold`, `normalized_basename.casefold().endswith`, `normalized_basename.endswith`, `normalized_basename.split`, `normalized_basename.split('.', 1)[0].casefold`, `ord`, `unicodedata.normalize`, `unicodedata.normalize('NFKC', filename).encode`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_validate_gpu_archive_download`
- `src/landscout/sources/gpu_fr.py` — `_validate_gpu_document_for_config`
- `src/landscout/sources/gpu_fr.py` — `discover_current_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_gpu_document_for_config`

**Signature**

```python
def _validate_gpu_document_for_config(
    document: GpuDocumentMetadata, config: GpuSourceConfig
) -> str:
```

**Purpose**

Validates and rejects malformed gpu document for config according to the exact implementation and guards in this file.

**Inputs**

- `document` (`GpuDocumentMetadata`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_safe_gpu_archive_filename(document.archive_name)`.

**Algorithm**

1. Checks `not isinstance(document, GpuDocumentMetadata)`. When true: Raises `GpuDownloadError('GPU document metadata object is invalid')`.
2. Checks `document.provider != config.provider or document.portal != config.portal`. When true: Raises `GpuDownloadError('GPU document provider/portal does not match configuration')`.
3. Checks `type(document.document_id) is not str or not document.document_id or document.document_id != document.document_id.strip() or any((ord(character) < 32 or ord(character) == 127 for character in document.document_id))`. When true: Raises `GpuDownloadError('GPU document ID is invalid')`.
4. Checks `type(document.written_files) is not tuple`. When true: Raises `GpuDownloadError('GPU document written-file provenance is invalid')`.
5. Defines `written_filenames` with annotation `set[str]` from `set()`.
6. Iterates `written_file` over `document.written_files`. For each value: Checks `type(written_file) is not GpuWrittenFile`. When true: Raises `GpuDownloadError('GPU document written-file type is invalid')`. Computes `filename` from `written_file.filename`. Checks `type(filename) is not str or not filename or filename != filename.strip() or any((ord(character) < 32 or ord(character) == 127 for character in filename)) or (filename in written_filenames)`. When true: Raises `GpuDownloadError('GPU document written filename is invalid')`. Executes 3 additional source-ordered statement(s).
7. Computes `code` from `document.commune_code`.
8. Checks `not isinstance(code, str) or re.fullmatch('[0-9]{5}', code) is None`. When true: Raises `GpuDownloadError('GPU document commune code is invalid')`.
9. Checks `code != config.pilot.commune_code`. When true: Raises `GpuDownloadError('GPU document commune does not match configured pilot')`.
10. Runs guarded operation: Computes `expected_partition` from `build_gpu_partition(config, code)`. Computes `expected_url` from `build_gpu_partition_download_url(config, code)`. Handles `GpuConfigError`.
11. Checks `document.partition != expected_partition`. When true: Raises `GpuDownloadError('GPU document partition does not match configuration')`.
12. Checks `document.document_family != 'DU'`. When true: Raises `GpuDownloadError('GPU document family is not a planning document')`.
13. Checks `document.status != 'document.production' or document.legal_status != 'APPROVED' or document.effective_status != 'EN_VIGUEUR'`. When true: Raises `GpuDownloadError('GPU document is not current, approved, and in force')`.
14. Checks `not isinstance(document.source_url, str) or document.source_url != expected_url`. When true: Raises `GpuDownloadError('GPU document source URL is not the official partition URL')`.
15. Computes `parsed` from `urlparse(document.source_url)`.
16. Computes `expected_parsed` from `urlparse(expected_url)`.
17. Checks `parsed.scheme != 'https' or parsed.hostname != 'www.geoportail-urbanisme.gouv.fr' or parsed.path != expected_parsed.path or parsed.params or parsed.query or parsed.fragment or (parsed.username is not None) or (parsed.password is not None)`. When true: Raises `GpuDownloadError('GPU document source URL has an unsafe identity')`.
18. Returns `_safe_gpu_archive_filename(document.archive_name)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(document, GpuDocumentMetadata)` is true.
- Rejects or diverts the path when `document.provider != config.provider or document.portal != config.portal` is true.
- Rejects or diverts the path when `type(document.document_id) is not str or not document.document_id or document.document_id != document.document_id.strip() or any((ord(character) < 32 or ord(character) == 127 for character in document.document_id))` is true.
- Rejects or diverts the path when `type(document.written_files) is not tuple` is true.
- Rejects or diverts the path when `not isinstance(code, str) or re.fullmatch('[0-9]{5}', code) is None` is true.
- Rejects or diverts the path when `code != config.pilot.commune_code` is true.
- Rejects or diverts the path when `document.partition != expected_partition` is true.
- Rejects or diverts the path when `document.document_family != 'DU'` is true.
- Rejects or diverts the path when `document.status != 'document.production' or document.legal_status != 'APPROVED' or document.effective_status != 'EN_VIGUEUR'` is true.
- Rejects or diverts the path when `not isinstance(document.source_url, str) or document.source_url != expected_url` is true.
- Rejects or diverts the path when `parsed.scheme != 'https' or parsed.hostname != 'www.geoportail-urbanisme.gouv.fr' or parsed.path != expected_parsed.path or parsed.params or parsed.query or parsed.fragment or (parsed.username is not None) or (parsed.password is not None)` is true.
- Rejects or diverts the path when `type(written_file) is not GpuWrittenFile` is true.
- Rejects or diverts the path when `type(filename) is not str or not filename or filename != filename.strip() or any((ord(character) < 32 or ord(character) == 127 for character in filename)) or (filename in written_filenames)` is true.
- Rejects or diverts the path when `written_file.source_url != expected_written_url` is true.

**Exceptions**

- Explicitly raises: `GpuDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuDownloadError`, `build_gpu_partition_download_url`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuDownloadError`, `_api_url`, `_safe_gpu_archive_filename`, `any`, `build_gpu_partition`, `build_gpu_partition_download_url`, `document.document_id.strip`, `filename.strip`, `isinstance`, `ord`, `quote`, `re.fullmatch`, `set`, `type`, `urlparse`, `written_filenames.add`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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
2. Enters managed context(s) `path.open('rb')` and executes: Repeats the guarded body while `(chunk := stream.read(DOWNLOAD_CHUNK_SIZE))` remains true.
3. Returns `digest.hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `digest.hexdigest`, `digest.update`, `path.open`, `sha256`, `stream.read`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_inventory`
- `src/landscout/sources/gpu_fr.py` — `_load_cached_archive`
- `src/landscout/sources/gpu_fr.py` — `_revalidate_gpu_spatial_layer_source`
- `src/landscout/sources/gpu_fr.py` — `_spatial_source_family`
- `src/landscout/sources/gpu_fr.py` — `_validate_gpu_archive_download`
- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`

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

1. Returns `path.is_symlink() or path.is_junction()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `path.is_junction`, `path.is_symlink`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_contained_spatial_path`
- `src/landscout/sources/gpu_fr.py` — `_inventory`
- `src/landscout/sources/gpu_fr.py` — `_prepare_temporary_cache_file`
- `src/landscout/sources/gpu_fr.py` — `_publish_extraction_directory`
- `src/landscout/sources/gpu_fr.py` — `_require_no_cache_recovery_material`
- `src/landscout/sources/gpu_fr.py` — `_spatial_dataset_relative_path`
- `src/landscout/sources/gpu_fr.py` — `_validate_extraction_manifest`
- `src/landscout/sources/gpu_fr.py` — `_validate_gpu_archive_download`
- `src/landscout/sources/gpu_fr.py` — `_validated_spatial_root`
- `src/landscout/sources/gpu_fr.py` — `extract_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_gpu_archive_download`

**Signature**

```python
def _validate_gpu_archive_download(
    download: GpuArchiveDownload,
) -> tuple[str, ...]:
```

**Purpose**

Validates and rejects malformed gpu archive download according to the exact implementation and guards in this file.

**Inputs**

- `download` (`GpuArchiveDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `validate_gpu_archive(path)`.

**Algorithm**

1. Checks `not isinstance(download, GpuArchiveDownload)`. When true: Raises `GpuArchiveError('GPU archive download object is invalid')`.
2. Checks `not isinstance(download.document, GpuDocumentMetadata)`. When true: Raises `GpuArchiveError('GPU archive document lineage object is invalid')`.
3. Computes `path` from `download.path`.
4. Checks `not isinstance(path, Path) or _is_link_or_junction(path) or (not path.is_file())`. When true: Raises `GpuArchiveError('GPU archive path is not a regular local file')`.
5. Checks `download.archive_format != 'zip'`. When true: Raises `GpuArchiveError('GPU archive object does not declare ZIP format')`.
6. Checks `not isinstance(download.filename, str) or download.filename != path.name`. When true: Raises `GpuArchiveError('GPU archive filename does not match its path')`.
7. Checks `type(download.file_size) is not int or download.file_size <= 0`. When true: Raises `GpuArchiveError('GPU archive object has an invalid file size')`.
8. Checks `not isinstance(download.sha256, str) or re.fullmatch('[0-9a-f]{64}', download.sha256) is None`. When true: Raises `GpuArchiveError('GPU archive object has an invalid SHA256')`.
9. Runs guarded operation: Computes `expected_filename` from `_safe_gpu_archive_filename(download.document.archive_name)`. Handles `(AttributeError, GpuDownloadError)`.
10. Checks `download.filename != expected_filename`. When true: Raises `GpuArchiveError('GPU archive filename does not match document lineage')`.
11. Runs guarded operation: Computes `actual_size` from `path.stat().st_size`. Computes `actual_sha256` from `_sha256(path)`. Handles `OSError`.
12. Checks `actual_size != download.file_size`. When true: Raises `GpuArchiveError('GPU archive size does not match immutable download lineage')`.
13. Checks `actual_sha256 != download.sha256`. When true: Raises `GpuArchiveError('GPU archive SHA256 does not match immutable download lineage')`.
14. Returns `validate_gpu_archive(path)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(download, GpuArchiveDownload)` is true.
- Rejects or diverts the path when `not isinstance(download.document, GpuDocumentMetadata)` is true.
- Rejects or diverts the path when `not isinstance(path, Path) or _is_link_or_junction(path) or (not path.is_file())` is true.
- Rejects or diverts the path when `download.archive_format != 'zip'` is true.
- Rejects or diverts the path when `not isinstance(download.filename, str) or download.filename != path.name` is true.
- Rejects or diverts the path when `type(download.file_size) is not int or download.file_size <= 0` is true.
- Rejects or diverts the path when `not isinstance(download.sha256, str) or re.fullmatch('[0-9a-f]{64}', download.sha256) is None` is true.
- Rejects or diverts the path when `download.filename != expected_filename` is true.
- Rejects or diverts the path when `actual_size != download.file_size` is true.
- Rejects or diverts the path when `actual_sha256 != download.sha256` is true.

**Exceptions**

- Explicitly raises: `GpuArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuArchiveError`, `_is_link_or_junction`, `_safe_gpu_archive_filename`, `_sha256`, `isinstance`, `path.is_file`, `path.stat`, `re.fullmatch`, `type`, `validate_gpu_archive`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `extract_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_safe_archive_member`

**Signature**

```python
def _safe_archive_member(name: str) -> bool:
```

**Purpose**

Implements safe archive member according to the exact implementation and guards in this file.

**Inputs**

- `name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `not (posix.is_absolute() or windows.is_absolute() or windows.drive or any((part == '..' for part in posix.parts)))`; `False`.

**Algorithm**

1. Checks `not name or '\x00' in name`. When true: Returns `False`.
2. Computes `posix` from `PurePosixPath(name.replace('\\', '/'))`.
3. Computes `windows` from `PureWindowsPath(name)`.
4. Returns `not (posix.is_absolute() or windows.is_absolute() or windows.drive or any((part == '..' for part in posix.parts)))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `name.replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PurePosixPath`, `PureWindowsPath`, `any`, `name.replace`, `posix.is_absolute`, `windows.is_absolute`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_validate_extraction_manifest`
- `src/landscout/sources/gpu_fr.py` — `_validated_zip_destinations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_windows_member_component`

**Signature**

```python
def _windows_member_component(component: str) -> str:
```

**Purpose**

Implements windows member component according to the exact implementation and guards in this file.

**Inputs**

- `component` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `normalized.casefold()`.

**Algorithm**

1. Computes `normalized` from `unicodedata.normalize('NFKC', component)`.
2. Checks `not normalized or normalized in {'.', '..'} or normalized.endswith((' ', '.')) or any((ord(character) < 32 or ord(character) == 127 for character in normalized)) or any((character in '<>:"/\\|?*' for character in normalized))`. When true: Raises `GpuArchiveError(f'Unsafe Windows-compatible ZIP component: {component}')`.
3. Computes `stem` from `normalized.split('.', 1)[0].casefold()`.
4. Checks `stem in _WINDOWS_RESERVED_BASENAMES`. When true: Raises `GpuArchiveError(f'Reserved Windows ZIP component: {component}')`.
5. Returns `normalized.casefold()`.

**Validation and invariants**

- Rejects or diverts the path when `not normalized or normalized in {'.', '..'} or normalized.endswith((' ', '.')) or any((ord(character) < 32 or ord(character) == 127 for character in normalized)) or any((character in '<>:"/\\|?*' for character in normalized))` is true.
- Rejects or diverts the path when `stem in _WINDOWS_RESERVED_BASENAMES` is true.

**Exceptions**

- Explicitly raises: `GpuArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuArchiveError`, `any`, `normalized.casefold`, `normalized.endswith`, `normalized.split`, `normalized.split('.', 1)[0].casefold`, `ord`, `unicodedata.normalize`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_validated_zip_destinations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_zip_destinations`

**Signature**

```python
def _validated_zip_destinations(
    members: list[zipfile.ZipInfo],
) -> tuple[tuple[zipfile.ZipInfo, PurePosixPath], ...]:
```

**Purpose**

Validates and returns canonical zip destinations according to the exact implementation and guards in this file.

**Inputs**

- `members` (`list[zipfile.ZipInfo]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[tuple[zipfile.ZipInfo, PurePosixPath], ...]`. Observed return expression(s): `tuple(result)`.

**Algorithm**

1. Defines `raw_names` with annotation `set[str]` from `set()`.
2. Defines `explicit_destinations` with annotation `dict[tuple[str, ...], str]` from `{}`.
3. Defines `file_destinations` with annotation `set[tuple[str, ...]]` from `set()`.
4. Defines `directory_destinations` with annotation `set[tuple[str, ...]]` from `set()`.
5. Defines `result` with annotation `list[tuple[zipfile.ZipInfo, PurePosixPath]]` from `[]`.
6. Iterates `member` over `members`. For each value: Computes `raw_name` from `member.filename`. Checks `raw_name in raw_names`. When true: Raises `GpuArchiveError(f'Duplicate member name in GPU ZIP: {raw_name}')`. Calls `raw_names.add(raw_name)` for its validation or side effect. Executes 18 additional source-ordered statement(s).
7. Returns `tuple(result)`.

**Validation and invariants**

- Rejects or diverts the path when `raw_name in raw_names` is true.
- Rejects or diverts the path when `not _safe_archive_member(raw_name)` is true.
- Rejects or diverts the path when `stat.S_ISLNK(mode)` is true.
- Rejects or diverts the path when `member.create_system == 3 and file_type not in {0, stat.S_IFREG, stat.S_IFDIR}` is true.
- Rejects or diverts the path when `not parts` is true.
- Rejects or diverts the path when `canonical[0] == EXTRACTION_MANIFEST_NAME.casefold()` is true.
- Rejects or diverts the path when `canonical in explicit_destinations` is true.
- Rejects or diverts the path when `any((parent in file_destinations for parent in parents))` is true.
- Rejects or diverts the path when `is_directory` is true.
- Rejects or diverts the path when `canonical in file_destinations` is true.
- Rejects or diverts the path when `canonical in directory_destinations` is true.

**Exceptions**

- Explicitly raises: `GpuArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `raw_name.replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `EXTRACTION_MANIFEST_NAME.casefold`, `GpuArchiveError`, `PurePosixPath`, `_safe_archive_member`, `_windows_member_component`, `any`, `directory_destinations.add`, `directory_destinations.update`, `file_destinations.add`, `len`, `member.is_dir`, `range`, `raw_name.endswith`, `raw_name.replace`, `raw_names.add`, `result.append`, `set`, `stat.S_IFMT`, `stat.S_ISLNK`, `tuple`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `extract_gpu_document`
- `src/landscout/sources/gpu_fr.py` — `validate_gpu_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_gpu_archive`

**Signature**

```python
def validate_gpu_archive(path: Path) -> tuple[str, ...]:
```

**Purpose**

Fully validate a ZIP archive and return its deterministic member inventory.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `tuple(sorted((destination.as_posix() for _, destination in destinations), key=str.casefold))`.

**Algorithm**

1. Checks `not path.is_file() or path.stat().st_size <= 0`. When true: Raises `GpuArchiveError(f'GPU archive is missing or empty: {path}')`.
2. Checks `not zipfile.is_zipfile(path)`. When true: Raises `GpuArchiveError(f'GPU archive is not a readable ZIP: {path}')`.
3. Runs guarded operation: Enters managed context(s) `zipfile.ZipFile(path)` and executes: Computes `members` from `archive.infolist()`. Checks `not members`. When true: Raises `GpuArchiveError('GPU ZIP contains no members')`. Computes `destinations` from `_validated_zip_destinations(members)`. Computes `bad_member` from `archive.testzip()`. Executes 1 additional source-ordered statement(s). Handles `GpuArchiveError`, `(OSError, zipfile.BadZipFile, RuntimeError)`.
4. Returns `tuple(sorted((destination.as_posix() for _, destination in destinations), key=str.casefold))`.

**Validation and invariants**

- Rejects or diverts the path when `not path.is_file() or path.stat().st_size <= 0` is true.
- Rejects or diverts the path when `not zipfile.is_zipfile(path)` is true.
- Rejects or diverts the path when `not members` is true.
- Rejects or diverts the path when `bad_member is not None` is true.

**Exceptions**

- Explicitly raises: `GpuArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuArchiveError`, `_validated_zip_destinations`, `archive.infolist`, `archive.testzip`, `destination.as_posix`, `path.is_file`, `path.stat`, `sorted`, `tuple`, `zipfile.ZipFile`, `zipfile.is_zipfile`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_load_cached_archive`
- `src/landscout/sources/gpu_fr.py` — `_validate_gpu_archive_download`
- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`
- `tests/unit/test_gpu_fr.py` — `test_archive_path_traversal_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_archive_symlink_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_duplicate_zip_extraction_targets_are_rejected`
- `tests/unit/test_gpu_fr.py` — `test_zip_cannot_claim_extraction_manifest_path`
- `tests/unit/test_gpu_fr.py` — `test_zip_file_directory_target_collision_is_rejected`

**Tests**

- `tests/unit/test_gpu_fr.py::test_archive_path_traversal_is_rejected`
- `tests/unit/test_gpu_fr.py::test_archive_symlink_is_rejected`
- `tests/unit/test_gpu_fr.py::test_duplicate_zip_extraction_targets_are_rejected`
- `tests/unit/test_gpu_fr.py::test_zip_cannot_claim_extraction_manifest_path`
- `tests/unit/test_gpu_fr.py::test_zip_file_directory_target_collision_is_rejected`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_document_identity`

**Signature**

```python
def _document_identity(document: GpuDocumentMetadata) -> dict[str, Any]:
```

**Purpose**

Implements document identity according to the exact implementation and guards in this file.

**Inputs**

- `document` (`GpuDocumentMetadata`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, Any]`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `result` from `asdict(document)`.
2. Computes `result['written_files']` from `[asdict(item) for item in document.written_files]`.
3. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `asdict`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_document_from_dict`

**Signature**

```python
def _document_from_dict(payload: Any) -> GpuDocumentMetadata:
```

**Purpose**

Implements document from dict according to the exact implementation and guards in this file.

**Inputs**

- `payload` (`Any`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuDocumentMetadata`. Observed return expression(s): `GpuDocumentMetadata(**values, written_files=tuple(written))`.

**Algorithm**

1. Checks `not isinstance(payload, dict)`. When true: Raises `TypeError('Cached GPU document metadata is invalid')`.
2. Computes `values` from `dict(payload)`.
3. Computes `files` from `values.pop('written_files')`.
4. Checks `not isinstance(files, list)`. When true: Raises `TypeError('Cached GPU written-file metadata is invalid')`.
5. Defines `written` with annotation `list[GpuWrittenFile]` from `[]`.
6. Iterates `item` over `files`. For each value: Checks `not isinstance(item, dict)`. When true: Raises `TypeError('Cached GPU written-file entry is invalid')`. Calls `written.append(GpuWrittenFile(**item))` for its validation or side effect.
7. Returns `GpuDocumentMetadata(**values, written_files=tuple(written))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, dict)` is true.
- Rejects or diverts the path when `not isinstance(files, list)` is true.
- Rejects or diverts the path when `not isinstance(item, dict)` is true.

**Exceptions**

- Explicitly raises: `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuDocumentMetadata`, `GpuWrittenFile`, `TypeError`, `dict`, `isinstance`, `tuple`, `values.pop`, `written.append`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_load_cached_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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

- `src/landscout/sources/gpu_fr.py` — `_publish_cache_pair`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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

- `src/landscout/sources/gpu_fr.py` — `_publish_cache_pair`
- `src/landscout/sources/gpu_fr.py` — `_require_no_cache_recovery_material`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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

1. Computes `recovery_paths` from `_cache_recovery_paths(archive_path, metadata_path)`.
2. Checks `any((path.exists() or _is_link_or_junction(path) for path in recovery_paths))`. When true: Raises `GpuDownloadError('GPU cache recovery backup already exists; manual recovery is required')`.

**Validation and invariants**

- Rejects or diverts the path when `any((path.exists() or _is_link_or_junction(path) for path in recovery_paths))` is true.

**Exceptions**

- Explicitly raises: `GpuDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuDownloadError`, `_cache_recovery_paths`, `_is_link_or_junction`, `any`, `path.exists`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_publish_cache_pair`
- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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

1. Runs guarded operation: Checks `_is_link_or_junction(path)`. When true: Raises `GpuDownloadError('GPU cache temporary path is a link or junction')`. Checks `path.exists()`. When true: Checks `not path.is_file()`. When true: Raises `GpuDownloadError('GPU cache temporary path is not a regular file')`. Calls `path.unlink()` for its validation or side effect. Handles `GpuDownloadError`, `OSError`.

**Validation and invariants**

- Rejects or diverts the path when `_is_link_or_junction(path)` is true.
- Rejects or diverts the path when `path.exists()` is true.
- Rejects or diverts the path when `not path.is_file()` is true.

**Exceptions**

- Explicitly raises: `GpuDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuDownloadError`, `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuDownloadError`, `_is_link_or_junction`, `path.exists`, `path.is_file`, `path.unlink`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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
3. Checks `cleanup_error is not None and primary_error is None`. When true: Raises `GpuDownloadError('GPU cache temporary files could not be cleaned safely')`.

**Validation and invariants**

- Rejects or diverts the path when `cleanup_error is not None and primary_error is None` is true.

**Exceptions**

- Explicitly raises: `GpuDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuDownloadError`, `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuDownloadError`, `path.unlink`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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
6. Computes `publication_started` from `False`.
7. Runs guarded operation: Computes `publication_started` from `True`. Calls `_replace_file(temporary_archive, archive_path)` for its validation or side effect. Calls `_replace_file(temporary_metadata, metadata_path)` for its validation or side effect. Handles `OSError`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `GpuDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuDownloadError`, `_replace_file`, `archive_backup.unlink`, `archive_path.unlink`, `copy2`, `metadata_backup.unlink`, `metadata_path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuDownloadError`, `_cache_recovery_paths`, `_replace_file`, `_require_no_cache_recovery_material`, `archive_backup.unlink`, `archive_path.is_file`, `archive_path.unlink`, `copy2`, `metadata_backup.unlink`, `metadata_path.is_file`, `metadata_path.unlink`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_load_cached_archive`

**Signature**

```python
def _load_cached_archive(
    archive_path: Path,
    metadata_path: Path,
    document: GpuDocumentMetadata,
    max_age_hours: float,
) -> GpuArchiveDownload | None:
```

**Purpose**

Loads cached archive according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `document` (`GpuDocumentMetadata`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `max_age_hours` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuArchiveDownload | None`. Observed return expression(s): `None`; `GpuArchiveDownload(document=document, download_timestamp=timestamp, filename=archive_path.name, archive_format='zip', file_size=size, sha256=checksum, path=archive_path, cache_hit=True)`.

**Algorithm**

1. Checks `not archive_path.is_file() or not metadata_path.is_file()`. When true: Returns `None`.
2. Runs guarded operation: Computes `payload` from `json.loads(metadata_path.read_text(encoding='utf-8'))`. Checks `not isinstance(payload, dict)`. When true: Returns `None`. Computes `cached_document` from `_document_from_dict(payload['document'])`. Computes `timestamp` from `payload['download_timestamp']`. Executes 9 additional source-ordered statement(s). Handles `(KeyError, OSError, TypeError, ValueError, json.JSONDecodeError, GpuArchiveError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds`, `GpuArchiveDownload`, `downloaded_at.astimezone`, `downloaded_at.utcoffset`, `metadata_path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds`, `GpuArchiveDownload`, `_document_from_dict`, `_sha256`, `archive_path.is_file`, `archive_path.stat`, `datetime.fromisoformat`, `datetime.now`, `downloaded_at.astimezone`, `downloaded_at.utcoffset`, `isinstance`, `json.loads`, `len`, `metadata_path.is_file`, `metadata_path.read_text`, `payload.get`, `validate_gpu_archive`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `download_gpu_document`

**Signature**

```python
def download_gpu_document(
    document: GpuDocumentMetadata,
    config: GpuSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> GpuArchiveDownload:
```

**Purpose**

Download and transactionally cache one discovered official GPU ZIP.

**Inputs**

- `document` (`GpuDocumentMetadata`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cache_dir` (`Path`; optional/default `DEFAULT_CACHE_DIR`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; optional/default `120.0`) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuArchiveDownload`. Observed return expression(s): `cached`; `result`.

**Algorithm**

1. Runs guarded operation: Computes `validated_config` from `_validated_source_config(config)`. Handles `GpuConfigError`.
2. Computes `filename` from `_validate_gpu_document_for_config(document, validated_config)`.
3. Computes `archive_path` from `cache_dir / filename`.
4. Computes `metadata_path` from `cache_dir / f'{filename}.metadata.json'`.
5. Calls `_require_no_cache_recovery_material(archive_path, metadata_path)` for its validation or side effect.
6. Computes `cached` from `_load_cached_archive(archive_path, metadata_path, document, validated_config.cache.max_age_hours)`.
7. Checks `cached is not None`. When true: Returns `cached`.
8. Calls `cache_dir.mkdir(parents=True, exist_ok=True)` for its validation or side effect.
9. Computes `temporary_archive` from `archive_path.with_suffix(f'{archive_path.suffix}.part')`.
10. Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
11. Calls `_prepare_temporary_cache_file(temporary_archive)` for its validation or side effect.
12. Calls `_prepare_temporary_cache_file(temporary_metadata)` for its validation or side effect.
13. Runs guarded operation: Enters managed context(s) `open_safe_https(document.source_url, timeout=timeout, headers={'User-Agent': USER_AGENT}), temporary_archive.open('wb')` and executes: Calls `copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)` for its validation or side effect. Computes `members` from `validate_gpu_archive(temporary_archive)`. Computes `result` from `GpuArchiveDownload(document=document, download_timestamp=datetime.now(UTC).isoformat(), filename=filename, archive_format='zip', file_size=temporary_archive.stat().st_size, sha256=_sha256(temporary_archive), path=archive_path, cache_hit=False)`. Computes `lineage` from `{'document': _document_identity(document), 'download_timestamp': result.download_timestamp, 'filename': filename, 'archive_format': result.archive_format, 'file_size': result.file_size, 'sha256': result.sha256, 'member_count': len(members)}`. Executes 3 additional source-ordered statement(s). Handles `(HTTPError, URLError, OSError, GpuArchiveError)`. Finally: Calls `_cleanup_temporary_cache_files((temporary_archive, temporary_metadata), sys.exception())` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `GpuDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `GpuArchiveDownload`, `GpuDownloadError`, `_load_cached_archive`, `cache_dir.mkdir`, `copyfileobj`, `open_safe_https`, `temporary_archive.open`, `temporary_metadata.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuArchiveDownload`, `GpuDownloadError`, `_cleanup_temporary_cache_files`, `_document_identity`, `_load_cached_archive`, `_prepare_temporary_cache_file`, `_publish_cache_pair`, `_require_no_cache_recovery_material`, `_sha256`, `_validate_gpu_document_for_config`, `_validated_source_config`, `archive_path.with_suffix`, `cache_dir.mkdir`, `copyfileobj`, `datetime.now`, `datetime.now(UTC).isoformat`, `json.dumps`, `len`, `metadata_path.with_suffix`, `open_safe_https`, `sys.exception`, `temporary_archive.open`, `temporary_archive.stat`, `temporary_metadata.write_text`, `validate_gpu_archive`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `ingest_gpu_planning_document`
- `tests/unit/test_gpu_fr.py` — `_download`
- `tests/unit/test_gpu_fr.py` — `test_archive_name_with_one_zip_suffix_is_not_duplicated`
- `tests/unit/test_gpu_fr.py` — `test_cached_document_lineage_change_forces_refresh`
- `tests/unit/test_gpu_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_gpu_fr.py` — `test_corrupt_download_is_rejected`
- `tests/unit/test_gpu_fr.py` — `test_download_rejects_document_inconsistent_with_config`
- `tests/unit/test_gpu_fr.py` — `test_download_rejects_forged_unsafe_archive_name_before_io`
- `tests/unit/test_gpu_fr.py` — `test_download_rejects_forged_written_file_provenance_before_network`
- `tests/unit/test_gpu_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_gpu_fr.py` — `test_failed_refresh_preserves_previous_cache`
- `tests/unit/test_gpu_fr.py` — `test_fresh_cache_is_reused`
- `tests/unit/test_gpu_fr.py` — `test_metadata_publication_failure_rolls_back_both_cache_files`
- `tests/unit/test_gpu_fr.py` — `test_preexisting_temporary_archive_symlink_cannot_modify_target`
- `tests/unit/test_gpu_fr.py` — `test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_gpu_fr.py` — `test_tampered_sidecar_invalidates_cache`

**Tests**

- `tests/unit/test_gpu_fr.py::test_archive_name_with_one_zip_suffix_is_not_duplicated`
- `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh`
- `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_gpu_fr.py::test_corrupt_download_is_rejected`
- `tests/unit/test_gpu_fr.py::test_download_rejects_document_inconsistent_with_config`
- `tests/unit/test_gpu_fr.py::test_download_rejects_forged_unsafe_archive_name_before_io`
- `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network`
- `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache`
- `tests/unit/test_gpu_fr.py::test_fresh_cache_is_reused`
- `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files`
- `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target`
- `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_classify_file`

**Signature**

```python
def _classify_file(path: Path) -> FileCategory:
```

**Purpose**

Implements classify file according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `FileCategory`. Observed return expression(s): `'OTHER_ATTACHMENT'`; `'SPATIAL_DATA'`; `'METADATA'`; `'WRITTEN_REGULATION'`.

**Algorithm**

1. Computes `suffix` from `path.suffix.casefold()`.
2. Checks `suffix in {'.gpkg', '.shp', '.shx', '.dbf', '.prj', '.cpg', '.qmd', '.qix', '.sbn', '.sbx'}`. When true: Returns `'SPATIAL_DATA'`.
3. Checks `suffix in {'.xml', '.json', '.yaml', '.yml', '.csv', '.txt'}`. When true: Returns `'METADATA'`.
4. Checks `suffix in {'.pdf', '.odt', '.doc', '.docx'}`. When true: Returns `'WRITTEN_REGULATION'`.
5. Returns `'OTHER_ATTACHMENT'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `path.suffix.casefold`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_inventory`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_inventory`

**Signature**

```python
def _inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

**Purpose**

Implements inventory according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuExtractedFile, ...]`. Observed return expression(s): `tuple(files)`.

**Algorithm**

1. Checks `_is_link_or_junction(root) or not root.is_dir()`. When true: Raises `GpuArchiveError(f'GPU extraction root is not a regular directory: {root}')`.
2. Iterates `path` over `root.rglob('*')`. For each value: Checks `_is_link_or_junction(path)`. When true: Raises `GpuArchiveError(f'Extracted GPU symbolic link is forbidden: {path}')`.
3. Defines `files` with annotation `list[GpuExtractedFile]` from `[]`.
4. Iterates `path` over `sorted((item for item in root.rglob('*') if item.is_file()), key=str)`. For each value: Checks `path.parent == root and path.name == EXTRACTION_MANIFEST_NAME`. When true: Executes `continue` control flow. Computes `resolved` from `path.resolve()`. Runs guarded operation: Computes `relative` from `resolved.relative_to(root.resolve())`. Handles `ValueError`. Executes 1 additional source-ordered statement(s).
5. Checks `not files`. When true: Raises `GpuArchiveError('Extracted GPU package contains no files')`.
6. Calls `files.sort(key=lambda item: item.relative_path)` for its validation or side effect.
7. Returns `tuple(files)`.

**Validation and invariants**

- Rejects or diverts the path when `_is_link_or_junction(root) or not root.is_dir()` is true.
- Rejects or diverts the path when `not files` is true.
- Rejects or diverts the path when `_is_link_or_junction(path)` is true.

**Exceptions**

- Explicitly raises: `GpuArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuArchiveError`, `GpuExtractedFile`, `_classify_file`, `_is_link_or_junction`, `_sha256`, `files.append`, `files.sort`, `item.is_file`, `path.resolve`, `path.stat`, `path.suffix.casefold`, `path.suffix.casefold().lstrip`, `relative.as_posix`, `resolved.relative_to`, `root.is_dir`, `root.resolve`, `root.rglob`, `sorted`, `tuple`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_validate_extraction_manifest`
- `src/landscout/sources/gpu_fr.py` — `extract_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_manifest_payload`

**Signature**

```python
def _manifest_payload(
    download: GpuArchiveDownload, files: tuple[GpuExtractedFile, ...]
) -> dict[str, Any]:
```

**Purpose**

Implements manifest payload according to the exact implementation and guards in this file.

**Inputs**

- `download` (`GpuArchiveDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `files` (`tuple[GpuExtractedFile, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, Any]`. Observed return expression(s): `{'schema_version': EXTRACTION_MANIFEST_SCHEMA_VERSION, 'archive_sha256': download.sha256, 'files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in files]}`.

**Algorithm**

1. Returns `{'schema_version': EXTRACTION_MANIFEST_SCHEMA_VERSION, 'archive_sha256': download.sha256, 'files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in files]}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `extract_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_extraction_manifest`

**Signature**

```python
def _validate_extraction_manifest(
    root: Path, download: GpuArchiveDownload
) -> tuple[GpuExtractedFile, ...]:
```

**Purpose**

Validates and rejects malformed extraction manifest according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `download` (`GpuArchiveDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuExtractedFile, ...]`. Observed return expression(s): `actual_files`.

**Algorithm**

1. Computes `marker` from `root / EXTRACTION_MANIFEST_NAME`.
2. Checks `_is_link_or_junction(marker) or not marker.is_file()`. When true: Raises `GpuArchiveError('GPU extraction manifest is missing or unsafe')`.
3. Runs guarded operation: Computes `payload` from `json.loads(marker.read_text(encoding='utf-8'))`. Handles `(OSError, UnicodeDecodeError, json.JSONDecodeError)`.
4. Checks `not isinstance(payload, dict) or set(payload) != {'schema_version', 'archive_sha256', 'files'}`. When true: Raises `GpuArchiveError('GPU extraction manifest has an invalid structure')`.
5. Checks `type(payload['schema_version']) is not int or payload['schema_version'] != EXTRACTION_MANIFEST_SCHEMA_VERSION`. When true: Raises `GpuArchiveError('GPU extraction manifest schema is unsupported')`.
6. Checks `payload['archive_sha256'] != download.sha256`. When true: Raises `GpuArchiveError('GPU extraction manifest archive lineage differs')`.
7. Computes `entries` from `payload['files']`.
8. Checks `not isinstance(entries, list)`. When true: Raises `GpuArchiveError('GPU extraction manifest files are invalid')`.
9. Defines `expected` with annotation `list[tuple[str, int, str]]` from `[]`.
10. Defines `previous_path` with annotation `str | None` from `None`.
11. Iterates `entry` over `entries`. For each value: Checks `not isinstance(entry, dict) or set(entry) != {'relative_path', 'size_bytes', 'sha256'}`. When true: Raises `GpuArchiveError('GPU extraction manifest file entry is invalid')`. Computes `relative_path` from `entry['relative_path']`. Computes `size_bytes` from `entry['size_bytes']`. Executes 5 additional source-ordered statement(s).
12. Computes `actual_files` from `_inventory(root)`.
13. Computes `actual` from `[(item.relative_path, item.size_bytes, item.sha256) for item in actual_files]`.
14. Checks `actual != expected`. When true: Raises `GpuArchiveError('GPU extraction files do not match the versioned integrity manifest')`.
15. Returns `actual_files`.

**Validation and invariants**

- Rejects or diverts the path when `_is_link_or_junction(marker) or not marker.is_file()` is true.
- Rejects or diverts the path when `not isinstance(payload, dict) or set(payload) != {'schema_version', 'archive_sha256', 'files'}` is true.
- Rejects or diverts the path when `type(payload['schema_version']) is not int or payload['schema_version'] != EXTRACTION_MANIFEST_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `payload['archive_sha256'] != download.sha256` is true.
- Rejects or diverts the path when `not isinstance(entries, list)` is true.
- Rejects or diverts the path when `actual != expected` is true.
- Rejects or diverts the path when `not isinstance(entry, dict) or set(entry) != {'relative_path', 'size_bytes', 'sha256'}` is true.
- Rejects or diverts the path when `not isinstance(relative_path, str) or not _safe_archive_member(relative_path) or relative_path == EXTRACTION_MANIFEST_NAME or (type(size_bytes) is not int) or (size_bytes < 0) or (not isinstance(checksum, str)) or (re.fullmatch('[0-9a-f]{64}', checksum) is None)` is true.
- Rejects or diverts the path when `previous_path is not None and relative_path <= previous_path` is true.

**Exceptions**

- Explicitly raises: `GpuArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `marker.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuArchiveError`, `_inventory`, `_is_link_or_junction`, `_safe_archive_member`, `expected.append`, `isinstance`, `json.loads`, `marker.is_file`, `marker.read_text`, `re.fullmatch`, `set`, `type`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_revalidate_gpu_spatial_layer_source`
- `src/landscout/sources/gpu_fr.py` — `_revalidate_gpu_spatial_layer_sources`
- `src/landscout/sources/gpu_fr.py` — `extract_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_remove_extraction_path`

**Signature**

```python
def _remove_extraction_path(path: Path) -> None:
```

**Purpose**

Implements remove extraction path according to the exact implementation and guards in this file.

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

- `src/landscout/sources/gpu_fr.py` — `_publish_extraction_directory`
- `src/landscout/sources/gpu_fr.py` — `extract_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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
2. Calls `_remove_extraction_path(backup)` for its validation or side effect.
3. Computes `old_moved` from `False`.
4. Runs guarded operation: Checks `root.exists() or _is_link_or_junction(root)`. When true: Calls `shutil.move(str(root), str(backup))` for its validation or side effect. Computes `old_moved` from `True`. Calls `shutil.move(str(temporary_root), str(root))` for its validation or side effect. Handles `OSError`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `GpuArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuArchiveError`, `_is_link_or_junction`, `_remove_extraction_path`, `root.exists`, `root.with_name`, `shutil.move`, `str`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `extract_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_discover_standard_models`

**Signature**

```python
def _discover_standard_models(root: Path) -> tuple[str, ...]:
```

**Purpose**

Discovers standard models according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `tuple(sorted(models, key=str.casefold))`.

**Algorithm**

1. Defines `models` with annotation `set[str]` from `set()`.
2. Iterates `path` over `sorted(root.rglob('*.xml'), key=str)`. For each value: Runs guarded operation: Computes `parsed` from `ElementTree.parse(path)`. Handles `(OSError, ElementTree.ParseError)`. Iterates `element` over `parsed.iter()`. For each value: Computes `text` from `element.text.strip() if element.text else ''`. Checks `re.fullmatch('CNIG\\s+[A-Za-z]+\\s+v\\d{4}', text, re.IGNORECASE)`. When true: Calls `models.add(text)` for its validation or side effect.
3. Returns `tuple(sorted(models, key=str.casefold))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ElementTree.parse`, `element.text.strip`, `models.add`, `parsed.iter`, `re.fullmatch`, `root.rglob`, `set`, `sorted`, `tuple`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `extract_gpu_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `extract_gpu_document`

**Signature**

```python
def extract_gpu_document(
    download: GpuArchiveDownload, cache_dir: Path = DEFAULT_CACHE_DIR
) -> GpuExtraction:
```

**Purpose**

Safely extract a validated GPU ZIP into a content-addressed cache.

**Inputs**

- `download` (`GpuArchiveDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cache_dir` (`Path`; optional/default `DEFAULT_CACHE_DIR`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuExtraction`. Observed return expression(s): `GpuExtraction(archive=download, extraction_root=root, files=files, standard_models=standard_models, cache_hit=False)`; `GpuExtraction(archive=download, extraction_root=root, files=files, standard_models=_discover_standard_models(root), cache_hit=True)`.

**Algorithm**

1. Calls `_validate_gpu_archive_download(download)` for its validation or side effect.
2. Computes `root` from `cache_dir / 'x' / download.sha256[:16]`.
3. Checks `root.is_dir() and (not _is_link_or_junction(root))`. When true: Runs guarded operation: Computes `files` from `_validate_extraction_manifest(root, download)`. Returns `GpuExtraction(archive=download, extraction_root=root, files=files, standard_models=_discover_standard_models(root), cache_hit=True)`. Handles `(GpuArchiveError, OSError)`.
4. Calls `root.parent.mkdir(parents=True, exist_ok=True)` for its validation or side effect.
5. Computes `temporary_root` from `root.with_name(f'{root.name}.part')`.
6. Calls `_remove_extraction_path(temporary_root)` for its validation or side effect.
7. Calls `temporary_root.mkdir()` for its validation or side effect.
8. Runs guarded operation: Enters managed context(s) `zipfile.ZipFile(download.path)` and executes: Computes `destinations` from `_validated_zip_destinations(archive.infolist())`. Iterates `(member, destination)` over `destinations`. For each value: Computes `target` from `temporary_root.joinpath(*destination.parts)`. Checks `member.is_dir() or member.filename.endswith(('/', '\\'))`. When true: Calls `target.mkdir(parents=True, exist_ok=True)` for its validation or side effect. Executes `continue` control flow. Calls `target.parent.mkdir(parents=True, exist_ok=True)` for its validation or side effect. Executes 1 additional source-ordered statement(s). Computes `files` from `_inventory(temporary_root)`. Calls `_validate_gpu_archive_download(download)` for its validation or side effect. Computes `marker` from `temporary_root / EXTRACTION_MANIFEST_NAME`. Executes 5 additional source-ordered statement(s). Handles `(OSError, zipfile.BadZipFile, RuntimeError, GpuArchiveError)`. Finally: Calls `_remove_extraction_path(temporary_root)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(error, GpuArchiveError)` is true.

**Exceptions**

- Explicitly raises: `GpuArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_validate_gpu_archive_download`, `archive.open`, `copyfileobj`, `marker.write_text`, `root.parent.mkdir`, `target.mkdir`, `target.open`, `target.parent.mkdir`, `temporary_root.mkdir`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuArchiveError`, `GpuExtraction`, `_discover_standard_models`, `_inventory`, `_is_link_or_junction`, `_manifest_payload`, `_publish_extraction_directory`, `_remove_extraction_path`, `_validate_extraction_manifest`, `_validate_gpu_archive_download`, `_validated_zip_destinations`, `archive.infolist`, `archive.open`, `copyfileobj`, `isinstance`, `json.dumps`, `marker.write_text`, `member.filename.endswith`, `member.is_dir`, `root.is_dir`, `root.parent.mkdir`, `root.with_name`, `target.mkdir`, `target.open`, `target.parent.mkdir`, `temporary_root.joinpath`, `temporary_root.mkdir`, `zipfile.ZipFile`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `ingest_gpu_planning_document`
- `tests/unit/test_gpu_fr.py` — `_extraction_from_archive`
- `tests/unit/test_gpu_fr.py` — `test_extraction_inventory_and_cache`
- `tests/unit/test_gpu_fr.py` — `test_extraction_rejects_archive_object_inconsistent_with_path`
- `tests/unit/test_gpu_fr.py` — `test_stale_download_object_rejects_replaced_valid_archive`
- `tests/unit/test_gpu_fr.py` — `test_tampered_extraction_is_rebuilt_from_verified_archive`

**Tests**

- `tests/unit/test_gpu_fr.py::test_extraction_inventory_and_cache`
- `tests/unit/test_gpu_fr.py::test_extraction_rejects_archive_object_inconsistent_with_path`
- `tests/unit/test_gpu_fr.py::test_stale_download_object_rejects_replaced_valid_archive`
- `tests/unit/test_gpu_fr.py::test_tampered_extraction_is_rebuilt_from_verified_archive`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `discover_gpu_spatial_layers`

**Signature**

```python
def discover_gpu_spatial_layers(
    extraction: GpuExtraction,
) -> tuple[GpuSpatialLayerReference, ...]:
```

**Purpose**

Discover every real GeoPackage or Shapefile layer in an extraction.

**Inputs**

- `extraction` (`GpuExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuSpatialLayerReference, ...]`. Observed return expression(s): `tuple(sorted(references, key=lambda item: (str(item.dataset_path), item.source_layer)))`.

**Algorithm**

1. Computes `root` from `extraction.extraction_root`.
2. Defines `references` with annotation `list[GpuSpatialLayerReference]` from `[]`.
3. Computes `gpkg_paths` from `sorted(root.rglob('*.gpkg'), key=str)`.
4. Computes `shp_paths` from `sorted(root.rglob('*.shp'), key=str)`.
5. Iterates `path` over `gpkg_paths`. For each value: Runs guarded operation: Computes `layers` from `pyogrio.list_layers(path)`. Handles `Exception`. Iterates `raw_name` over `layers[:, 0].tolist()`. For each value: Checks `isinstance(raw_name, str) and raw_name`. When true: Calls `references.append(GpuSpatialLayerReference(path, raw_name, 'GPKG'))` for its validation or side effect.
6. Iterates `path` over `shp_paths`. For each value: Calls `references.append(GpuSpatialLayerReference(path, path.stem, 'ESRI Shapefile'))` for its validation or side effect.
7. Checks `not references`. When true: Raises `GpuSpatialInspectionError('GPU document contains no supported spatial data')`.
8. Computes `unique` from `{(item.dataset_path.resolve(), item.source_layer) for item in references}`.
9. Checks `len(unique) != len(references)`. When true: Raises `GpuSpatialInspectionError('GPU document exposes duplicate spatial layers')`.
10. Returns `tuple(sorted(references, key=lambda item: (str(item.dataset_path), item.source_layer)))`.

**Validation and invariants**

- Rejects or diverts the path when `not references` is true.
- Rejects or diverts the path when `len(unique) != len(references)` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `GpuSpatialLayerReference`, `isinstance`, `item.dataset_path.resolve`, `layers[:, 0].tolist`, `len`, `pyogrio.list_layers`, `references.append`, `root.rglob`, `sorted`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `inspect_gpu_planning_document`
- `tests/unit/test_gpu_fr.py` — `test_spatial_inventory_and_inspection_preserve_source_quality`

**Tests**

- `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_layer_config`

**Signature**

```python
def _layer_config(
    config: GpuSourceConfig, logical_name: LogicalLayerName
) -> GpuLogicalLayerConfig:
```

**Purpose**

Implements layer config according to the exact implementation and guards in this file.

**Inputs**

- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalLayerName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuLogicalLayerConfig`. Observed return expression(s): `getattr(config.spatial_layers, logical_name)`.

**Algorithm**

1. Returns `getattr(config.spatial_layers, logical_name)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `getattr`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_discover_logical_layer`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_discover_logical_layer`

**Signature**

```python
def _discover_logical_layer(
    references: tuple[GpuSpatialLayerReference, ...],
    config: GpuSourceConfig,
    logical_name: LogicalLayerName,
    *,
    required: bool,
) -> GpuSpatialLayerReference | None:
```

**Purpose**

Discovers logical layer according to the exact implementation and guards in this file.

**Inputs**

- `references` (`tuple[GpuSpatialLayerReference, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalLayerName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `required` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuSpatialLayerReference | None`. Observed return expression(s): `matches[0]`; `None`.

**Algorithm**

1. Computes `configured` from `_layer_config(config, logical_name)`.
2. Computes `tokens` from `{_normalize_words(value) for value in configured.match_tokens}`.
3. Computes `matches` from `[]`.
4. Iterates `item` over `references`. For each value: Computes `normalized_name` from `f'_{_normalize_words(item.source_layer)}_'`. Checks `any((f'_{token}_' in normalized_name for token in tokens))`. When true: Calls `matches.append(item)` for its validation or side effect.
5. Checks `not matches and (not required)`. When true: Returns `None`.
6. Checks `len(matches) != 1`. When true: Computes `adjective` from `'exactly one' if required else 'at most one'`. Raises `GpuSpatialInspectionError(f'Expected {adjective} {logical_name} layer, found {len(matches)}')`.
7. Returns `matches[0]`.

**Validation and invariants**

- Rejects or diverts the path when `len(matches) != 1` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `_layer_config`, `_normalize_words`, `any`, `len`, `matches.append`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `inspect_gpu_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_load_reference`

**Signature**

```python
def _load_reference(reference: GpuSpatialLayerReference) -> gpd.GeoDataFrame:
```

**Purpose**

Loads reference according to the exact implementation and guards in this file.

**Inputs**

- `reference` (`GpuSpatialLayerReference`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.read_file(reference.dataset_path, engine='pyogrio')`; `gpd.read_file(reference.dataset_path, layer=reference.source_layer, engine='pyogrio')`.

**Algorithm**

1. Runs guarded operation: Checks `reference.driver == 'GPKG'`. When true: Returns `gpd.read_file(reference.dataset_path, layer=reference.source_layer, engine='pyogrio')`. Returns `gpd.read_file(reference.dataset_path, engine='pyogrio')`. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.read_file`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuSpatialInspectionError`, `gpd.read_file`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `inspect_gpu_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_inventory_path`

**Signature**

```python
def _validated_inventory_path(value: object) -> PurePosixPath:
```

**Purpose**

Validates and returns canonical inventory path according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PurePosixPath`. Observed return expression(s): `relative`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `GpuSpatialInspectionError('GPU extraction inventory path must be an exact string')`.
2. Checks `'\\' in value or '\x00' in value`. When true: Raises `GpuSpatialInspectionError('GPU extraction inventory path is unsafe')`.
3. Computes `parts` from `value.split('/')`.
4. Computes `relative` from `PurePosixPath(value)`.
5. Checks `relative.is_absolute() or any((part in {'', '.', '..'} for part in parts)) or relative.as_posix() != value`. When true: Raises `GpuSpatialInspectionError('GPU extraction inventory path is unsafe')`.
6. Returns `relative`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.
- Rejects or diverts the path when `'\\' in value or '\x00' in value` is true.
- Rejects or diverts the path when `relative.is_absolute() or any((part in {'', '.', '..'} for part in parts)) or relative.as_posix() != value` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `PurePosixPath`, `any`, `isinstance`, `relative.as_posix`, `relative.is_absolute`, `value.split`, `value.strip`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_contained_spatial_path`
- `src/landscout/sources/gpu_fr.py` — `_spatial_dataset_relative_path`
- `src/landscout/sources/gpu_fr.py` — `_spatial_inventory`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_spatial_root`

**Signature**

```python
def _validated_spatial_root(extraction: GpuExtraction) -> tuple[Path, Path]:
```

**Purpose**

Validates and returns canonical spatial root according to the exact implementation and guards in this file.

**Inputs**

- `extraction` (`GpuExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[Path, Path]`. Observed return expression(s): `(root, root.resolve(strict=True))`.

**Algorithm**

1. Computes `root` from `extraction.extraction_root`.
2. Runs guarded operation: Checks `not isinstance(root, Path) or _is_link_or_junction(root) or (not root.is_dir())`. When true: Raises `GpuSpatialInspectionError('GPU extraction root must be a regular directory')`. Returns `(root, root.resolve(strict=True))`. Handles `GpuSpatialInspectionError`, `OSError`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(root, Path) or _is_link_or_junction(root) or (not root.is_dir())` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `_is_link_or_junction`, `isinstance`, `root.is_dir`, `root.resolve`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_revalidate_gpu_spatial_layer_source`
- `src/landscout/sources/gpu_fr.py` — `_revalidate_gpu_spatial_layer_sources`
- `src/landscout/sources/gpu_fr.py` — `_spatial_source_family`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_spatial_inventory`

**Signature**

```python
def _spatial_inventory(
    extraction: GpuExtraction,
) -> dict[str, GpuExtractedFile]:
```

**Purpose**

Implements spatial inventory according to the exact implementation and guards in this file.

**Inputs**

- `extraction` (`GpuExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, GpuExtractedFile]`. Observed return expression(s): `inventory`.

**Algorithm**

1. Checks `type(extraction.files) is not tuple`. When true: Raises `GpuSpatialInspectionError('GPU extraction inventory must be an immutable tuple')`.
2. Defines `inventory` with annotation `dict[str, GpuExtractedFile]` from `{}`.
3. Iterates `item` over `extraction.files`. For each value: Checks `not isinstance(item, GpuExtractedFile)`. When true: Raises `GpuSpatialInspectionError('GPU extraction inventory is invalid')`. Computes `relative` from `_validated_inventory_path(item.relative_path).as_posix()`. Checks `relative.casefold() in {key.casefold() for key in inventory}`. When true: Raises `GpuSpatialInspectionError('GPU extraction inventory contains duplicate paths')`. Executes 1 additional source-ordered statement(s).
4. Returns `inventory`.

**Validation and invariants**

- Rejects or diverts the path when `type(extraction.files) is not tuple` is true.
- Rejects or diverts the path when `not isinstance(item, GpuExtractedFile)` is true.
- Rejects or diverts the path when `relative.casefold() in {key.casefold() for key in inventory}` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `_validated_inventory_path`, `_validated_inventory_path(item.relative_path).as_posix`, `isinstance`, `key.casefold`, `relative.casefold`, `type`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_spatial_source_family`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_contained_spatial_path`

**Signature**

```python
def _contained_spatial_path(
    root: Path,
    root_resolved: Path,
    relative: str,
) -> Path:
```

**Purpose**

Implements contained spatial path according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `root_resolved` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relative` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `path`.

**Algorithm**

1. Computes `relative_path` from `_validated_inventory_path(relative)`.
2. Computes `path` from `root.joinpath(*relative_path.parts)`.
3. Computes `current` from `root`.
4. Runs guarded operation: Iterates `part` over `relative_path.parts`. For each value: Updates `current` using `` and `part`. Checks `_is_link_or_junction(current)`. When true: Raises `GpuSpatialInspectionError('GPU spatial source path contains a symbolic link or junction')`. Computes `resolved` from `path.resolve(strict=True)`. Calls `resolved.relative_to(root_resolved)` for its validation or side effect. Checks `not path.is_file()`. When true: Raises `GpuSpatialInspectionError('GPU spatial source must be an extracted regular file')`. Executes 1 additional source-ordered statement(s). Handles `GpuSpatialInspectionError`, `(OSError, ValueError)`.

**Validation and invariants**

- Rejects or diverts the path when `not path.is_file()` is true.
- Rejects or diverts the path when `_is_link_or_junction(current)` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `_is_link_or_junction`, `_validated_inventory_path`, `path.is_file`, `path.resolve`, `resolved.relative_to`, `root.joinpath`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_spatial_source_family`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_spatial_dataset_relative_path`

**Signature**

```python
def _spatial_dataset_relative_path(
    reference: GpuSpatialLayerReference,
    root_resolved: Path,
) -> str:
```

**Purpose**

Implements spatial dataset relative path according to the exact implementation and guards in this file.

**Inputs**

- `reference` (`GpuSpatialLayerReference`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `root_resolved` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_validated_inventory_path(relative.as_posix()).as_posix()`.

**Algorithm**

1. Computes `path` from `reference.dataset_path`.
2. Runs guarded operation: Checks `not isinstance(path, Path) or _is_link_or_junction(path)`. When true: Raises `GpuSpatialInspectionError('GPU spatial dataset path is invalid')`. Computes `relative` from `path.resolve(strict=True).relative_to(root_resolved)`. Returns `_validated_inventory_path(relative.as_posix()).as_posix()`. Handles `GpuSpatialInspectionError`, `(OSError, ValueError)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(path, Path) or _is_link_or_junction(path)` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `_is_link_or_junction`, `_validated_inventory_path`, `_validated_inventory_path(relative.as_posix()).as_posix`, `isinstance`, `path.resolve`, `path.resolve(strict=True).relative_to`, `relative.as_posix`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_spatial_source_family`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_spatial_source_family`

**Signature**

```python
def _spatial_source_family(
    reference: GpuSpatialLayerReference,
    extraction: GpuExtraction,
) -> tuple[str, tuple[tuple[Path, GpuExtractedFile], ...]]:
```

**Purpose**

Implements spatial source family according to the exact implementation and guards in this file.

**Inputs**

- `reference` (`GpuSpatialLayerReference`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `extraction` (`GpuExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, tuple[tuple[Path, GpuExtractedFile], ...]]`. Observed return expression(s): `(relative, tuple(verified))`.

**Algorithm**

1. Computes `(root, root_resolved)` from `_validated_spatial_root(extraction)`.
2. Computes `inventory` from `_spatial_inventory(extraction)`.
3. Computes `relative` from `_spatial_dataset_relative_path(reference, root_resolved)`.
4. Computes `pure` from `PurePosixPath(relative)`.
5. Computes `driver` from `reference.driver`.
6. Checks `driver == 'GPKG'`. When true: Checks `pure.suffix.casefold() != '.gpkg'`. When true: Raises `GpuSpatialInspectionError('GPU GeoPackage source has an inconsistent extension')`. Computes `expected_paths` from `{relative}`. Iterates `suffix` over `('-wal', '-shm', '-journal')`. For each value: Checks `Path(f'{reference.dataset_path}{suffix}').exists()`. When true: Raises `GpuSpatialInspectionError('GPU GeoPackage has an unbound SQLite sidecar')`. Executes 2 additional source-ordered statement(s). Otherwise: Checks `driver == 'ESRI Shapefile'`. When true: Checks `pure.suffix.casefold() != '.shp' or reference.source_layer != pure.stem`. When true: Raises `GpuSpatialInspectionError('GPU Shapefile source identity is inconsistent')`. Computes `family_names` from `{f'{pure.stem}{suffix}'.casefold() for suffix in ('.shp', '.shx', '.dbf', '.prj', '.cpg', '.qix', '.qmd', '.sbn', '.sbx', '.shp.xml')}`. Computes `expected_paths` from `{candidate for candidate in inventory if PurePosixPath(candidate).parent == pure.parent and PurePosixPath(candidate).name.casefold() in family_names}`. Executes 5 additional source-ordered statement(s). Otherwise: Raises `GpuSpatialInspectionError('GPU spatial source driver must be GPKG or ESRI Shapefile')`.
7. Defines `verified` with annotation `list[tuple[Path, GpuExtractedFile]]` from `[]`.
8. Iterates `candidate` over `sorted(expected_paths)`. For each value: Computes `item` from `inventory.get(candidate)`. Checks `item is None`. When true: Raises `GpuSpatialInspectionError('GPU spatial source is absent from the extraction inventory')`. Checks `type(item.size_bytes) is not int or item.size_bytes <= 0 or (not isinstance(item.sha256, str)) or (re.fullmatch('[0-9a-f]{64}', item.sha256) is None)`. When true: Raises `GpuSpatialInspectionError('GPU spatial source inventory integrity is invalid')`. Executes 5 additional source-ordered statement(s).
9. Returns `(relative, tuple(verified))`.

**Validation and invariants**

- Rejects or diverts the path when `driver == 'GPKG'` is true.
- Rejects or diverts the path when `pure.suffix.casefold() != '.gpkg'` is true.
- Rejects or diverts the path when `len(exposed) != 1` is true.
- Rejects or diverts the path when `driver == 'ESRI Shapefile'` is true.
- Rejects or diverts the path when `item is None` is true.
- Rejects or diverts the path when `type(item.size_bytes) is not int or item.size_bytes <= 0 or (not isinstance(item.sha256, str)) or (re.fullmatch('[0-9a-f]{64}', item.sha256) is None)` is true.
- Rejects or diverts the path when `actual_size != item.size_bytes` is true.
- Rejects or diverts the path when `actual_sha != item.sha256` is true.
- Rejects or diverts the path when `Path(f'{reference.dataset_path}{suffix}').exists()` is true.
- Rejects or diverts the path when `pure.suffix.casefold() != '.shp' or reference.source_layer != pure.stem` is true.
- Rejects or diverts the path when `not required.issubset({PurePosixPath(candidate).suffix.casefold() for candidate in expected_paths})` is true.
- Rejects or diverts the path when `actual_paths != expected_paths` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `Path`, `Path(f'{reference.dataset_path}{suffix}').exists`, `PurePosixPath`, `PurePosixPath(candidate).name.casefold`, `PurePosixPath(candidate).suffix.casefold`, `_contained_spatial_path`, `_sha256`, `_spatial_dataset_relative_path`, `_spatial_inventory`, `_validated_spatial_root`, `candidate.name.casefold`, `candidate.resolve`, `candidate.resolve(strict=True).relative_to`, `candidate.resolve(strict=True).relative_to(root_resolved).as_posix`, `f'{pure.stem}{suffix}'.casefold`, `inventory.get`, `isinstance`, `layers[:, 0].tolist`, `len`, `parent.iterdir`, `path.stat`, `pure.suffix.casefold`, `pyogrio.list_layers`, `re.fullmatch`, `required.issubset`, `root.joinpath`, `sorted`, `tuple`, `type`, `verified.append`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_revalidate_gpu_spatial_layer_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_same_spatial_crs`

**Signature**

```python
def _same_spatial_crs(left: object, right: object) -> bool:
```

**Purpose**

Returns whether `spatial crs` agrees under the implementation's exact comparison contract.

**Inputs**

- `left` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `right` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `bool(CRS.from_user_input(left).equals(CRS.from_user_input(right)))`.

**Algorithm**

1. Runs guarded operation: Returns `bool(CRS.from_user_input(left).equals(CRS.from_user_input(right)))`. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_user_input`, `CRS.from_user_input(left).equals`, `GpuSpatialInspectionError`, `bool`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_compare_inspected_spatial_layer`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_inspected_spatial_layer`

**Signature**

```python
def _compare_inspected_spatial_layer(
    inspected: GpuInspectedLayer,
    reread: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Compares inspected spatial layer according to the exact implementation and guards in this file.

**Inputs**

- `inspected` (`GpuInspectedLayer`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `reread` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `loaded` from `inspected.data`.
2. Runs guarded operation: Checks `not isinstance(loaded, gpd.GeoDataFrame) or not isinstance(reread, gpd.GeoDataFrame)`. When true: Raises `GpuSpatialInspectionError('GPU spatial layer must be a GeoDataFrame')`. Checks `len(loaded) != len(reread)`. When true: Raises `GpuSpatialInspectionError('Loaded GPU spatial row count differs from its source')`. Checks `tuple(loaded.columns) != tuple(reread.columns)`. When true: Raises `GpuSpatialInspectionError('Loaded GPU spatial columns differ from its source')`. Checks `tuple((str(dtype) for dtype in loaded.dtypes)) != tuple((str(dtype) for dtype in reread.dtypes))`. When true: Raises `GpuSpatialInspectionError('Loaded GPU spatial dtypes differ from its source')`. Executes 6 additional source-ordered statement(s). Handles `GpuSpatialInspectionError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(loaded, gpd.GeoDataFrame) or not isinstance(reread, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `len(loaded) != len(reread)` is true.
- Rejects or diverts the path when `tuple(loaded.columns) != tuple(reread.columns)` is true.
- Rejects or diverts the path when `tuple((str(dtype) for dtype in loaded.dtypes)) != tuple((str(dtype) for dtype in reread.dtypes))` is true.
- Rejects or diverts the path when `loaded.geometry.name != reread.geometry.name or not _same_spatial_crs(loaded.crs, reread.crs)` is true.
- Rejects or diverts the path when `loaded.attrs != reread.attrs` is true.
- Rejects or diverts the path when `not loaded[attributes].reset_index(drop=True).equals(reread[attributes].reset_index(drop=True))` is true.
- Rejects or diverts the path when `loaded.geometry.to_wkb().tolist() != reread.geometry.to_wkb().tolist()` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `_same_spatial_crs`, `isinstance`, `len`, `loaded.geometry.to_wkb`, `loaded.geometry.to_wkb().tolist`, `loaded[attributes].reset_index`, `loaded[attributes].reset_index(drop=True).equals`, `reread.geometry.to_wkb`, `reread.geometry.to_wkb().tolist`, `reread[attributes].reset_index`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_revalidate_gpu_spatial_layer_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_revalidate_gpu_spatial_layer_source`

**Signature**

```python
def _revalidate_gpu_spatial_layer_source(
    planning_document: GpuPlanningDocument,
    inspected_layer: GpuInspectedLayer,
    *,
    verify_extraction_manifest: bool,
) -> GpuValidatedSpatialLayerSource:
```

**Purpose**

Verify and freshly reload one extracted GPU spatial-layer source.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `inspected_layer` (`GpuInspectedLayer`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `verify_extraction_manifest` (`bool`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuValidatedSpatialLayerSource`. Observed return expression(s): `GpuValidatedSpatialLayerSource(logical_name=inspected_layer.logical_name, source_layer=reference.source_layer, driver=reference.driver, dataset_relative_path=relative, source_crs=expected_summary.crs, feature_count=len(reread), files=tuple((GpuSpatialSourceFileIntegrity(relative_path=item.relative_path, file_type=item.file_type, size_bytes=item.size_bytes, sha256=item.sha256, category=item.catego…`.

**Algorithm**

1. Runs guarded operation: Checks `not isinstance(planning_document, GpuPlanningDocument) or not isinstance(inspected_layer, GpuInspectedLayer)`. When true: Raises `GpuSpatialInspectionError('GPU planning document or inspected layer is invalid')`. Checks `not any((inspected_layer is candidate for candidate in (planning_document.zoning, *planning_document.related_layers)))`. When true: Raises `GpuSpatialInspectionError('Inspected GPU layer does not belong to the planning document')`. Checks `sum((reference == inspected_layer.reference for reference in planning_document.all_spatial_layers)) != 1`. When true: Raises `GpuSpatialInspectionError('Inspected GPU reference must occur exactly once in the spatial inventory')`. Checks `verify_extraction_manifest`. When true: Computes `(root, _)` from `_validated_spatial_root(planning_document.extraction)`. Runs guarded operation: Computes `manifest_files` from `_validate_extraction_manifest(root, planning_document.extraction.archive)`. Handles `GpuArchiveError`. Checks `planning_document.extraction.files != manifest_files`. When true: Raises `GpuSpatialInspectionError('GPU extraction inventory differs from its verified manifest')`. Executes 13 additional source-ordered statement(s). Handles `GpuSpatialInspectionError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(planning_document, GpuPlanningDocument) or not isinstance(inspected_layer, GpuInspectedLayer)` is true.
- Rejects or diverts the path when `not any((inspected_layer is candidate for candidate in (planning_document.zoning, *planning_document.related_layers)))` is true.
- Rejects or diverts the path when `sum((reference == inspected_layer.reference for reference in planning_document.all_spatial_layers)) != 1` is true.
- Rejects or diverts the path when `verify_extraction_manifest` is true.
- Rejects or diverts the path when `not with_fids.index.is_unique or any((isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0 for value in with_fids.index))` is true.
- Rejects or diverts the path when `inspected_layer.summary != expected_summary` is true.
- Rejects or diverts the path when `post_relative != relative or tuple((item.relative_path for _, item in post_family)) != tuple((item.relative_path for _, item in family))` is true.
- Rejects or diverts the path when `planning_document.extraction.files != manifest_files` is true.
- Rejects or diverts the path when `path.stat().st_size != item.size_bytes or _sha256(path) != item.sha256` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `pyogrio.read_dataframe`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuSpatialInspectionError`, `GpuSpatialSourceFileIntegrity`, `GpuValidatedSpatialLayerSource`, `_compare_inspected_spatial_layer`, `_sha256`, `_spatial_source_family`, `_summarize_layer`, `_validate_extraction_manifest`, `_validated_spatial_root`, `any`, `int`, `isinstance`, `len`, `path.stat`, `pyogrio.read_dataframe`, `sum`, `tuple`, `with_fids.reset_index`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_revalidate_gpu_spatial_layer_sources`
- `src/landscout/sources/gpu_fr.py` — `revalidate_gpu_spatial_layer_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `revalidate_gpu_spatial_layer_source`

**Signature**

```python
def revalidate_gpu_spatial_layer_source(
    planning_document: GpuPlanningDocument,
    inspected_layer: GpuInspectedLayer,
) -> GpuValidatedSpatialLayerSource:
```

**Purpose**

Verify and freshly reload one extracted GPU spatial-layer source.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `inspected_layer` (`GpuInspectedLayer`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuValidatedSpatialLayerSource`. Observed return expression(s): `_revalidate_gpu_spatial_layer_source(planning_document, inspected_layer, verify_extraction_manifest=True)`.

**Algorithm**

1. Returns `_revalidate_gpu_spatial_layer_source(planning_document, inspected_layer, verify_extraction_manifest=True)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_revalidate_gpu_spatial_layer_source`.

**Known repository callers**

- `src/landscout/stages/index_planning_regulation.py` — `_revalidate_zoning_source`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_revalidate_gpu_spatial_layer_sources`

**Signature**

```python
def _revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
```

**Purpose**

Implements revalidate gpu spatial layer sources according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `inspected_layers` (`tuple[GpuInspectedLayer, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuValidatedSpatialLayerSource, ...]`. Observed return expression(s): `tuple((_revalidate_gpu_spatial_layer_source(planning_document, layer, verify_extraction_manifest=False) for layer in inspected_layers))`.

**Algorithm**

1. Checks `not isinstance(planning_document, GpuPlanningDocument)`. When true: Raises `GpuSpatialInspectionError('planning_document must be a GpuPlanningDocument')`.
2. Checks `type(inspected_layers) is not tuple`. When true: Raises `GpuSpatialInspectionError('Inspected GPU spatial layers must be an immutable tuple')`.
3. Checks `any((not isinstance(layer, GpuInspectedLayer) for layer in inspected_layers))`. When true: Raises `GpuSpatialInspectionError('Every inspected GPU spatial layer must be a GpuInspectedLayer')`.
4. Checks `len({layer.logical_name for layer in inspected_layers}) != len(inspected_layers)`. When true: Raises `GpuSpatialInspectionError('Inspected GPU spatial layers contain a duplicate logical name')`.
5. Runs guarded operation: Computes `(root, _)` from `_validated_spatial_root(planning_document.extraction)`. Computes `manifest_files` from `_validate_extraction_manifest(root, planning_document.extraction.archive)`. Handles `(AttributeError, TypeError, GpuArchiveError)`.
6. Checks `planning_document.extraction.files != manifest_files`. When true: Raises `GpuSpatialInspectionError('GPU extraction inventory differs from its verified manifest')`.
7. Returns `tuple((_revalidate_gpu_spatial_layer_source(planning_document, layer, verify_extraction_manifest=False) for layer in inspected_layers))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(planning_document, GpuPlanningDocument)` is true.
- Rejects or diverts the path when `type(inspected_layers) is not tuple` is true.
- Rejects or diverts the path when `any((not isinstance(layer, GpuInspectedLayer) for layer in inspected_layers))` is true.
- Rejects or diverts the path when `len({layer.logical_name for layer in inspected_layers}) != len(inspected_layers)` is true.
- Rejects or diverts the path when `planning_document.extraction.files != manifest_files` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `_revalidate_gpu_spatial_layer_source`, `_validate_extraction_manifest`, `_validated_spatial_root`, `any`, `isinstance`, `len`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `revalidate_gpu_spatial_layer_sources`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `revalidate_gpu_spatial_layer_sources`

**Signature**

```python
def revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
```

**Purpose**

Verify an ordered collection of extracted GPU spatial-layer sources.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `inspected_layers` (`tuple[GpuInspectedLayer, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[GpuValidatedSpatialLayerSource, ...]`. Observed return expression(s): `_revalidate_gpu_spatial_layer_sources(planning_document, inspected_layers)`.

**Algorithm**

1. Runs guarded operation: Returns `_revalidate_gpu_spatial_layer_sources(planning_document, inspected_layers)`. Handles `GpuSpatialInspectionError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `_revalidate_gpu_spatial_layer_sources`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalized_catalogs`
- `src/landscout/stages/enrich_planning_zoning.py` — `validate_normalized_planning_zoning_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_crs_text`

**Signature**

```python
def _crs_text(frame: gpd.GeoDataFrame) -> str:
```

**Purpose**

Implements crs text according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `f'{authority[0]}:{authority[1]}' if authority else frame.crs.to_string()`; `'UNKNOWN'`.

**Algorithm**

1. Checks `frame.crs is None`. When true: Returns `'UNKNOWN'`.
2. Computes `authority` from `CRS.from_user_input(frame.crs).to_authority()`.
3. Returns `f'{authority[0]}:{authority[1]}' if authority else frame.crs.to_string()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_user_input`, `CRS.from_user_input(frame.crs).to_authority`, `frame.crs.to_string`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_summarize_layer`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_summarize_layer`

**Signature**

```python
def _summarize_layer(
    frame: gpd.GeoDataFrame,
    reference: GpuSpatialLayerReference,
    extraction: GpuExtraction,
) -> GpuLayerSummary:
```

**Purpose**

Implements summarize layer according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `reference` (`GpuSpatialLayerReference`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `extraction` (`GpuExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuLayerSummary`. Observed return expression(s): `GpuLayerSummary(source_document_id=extraction.archive.document.document_id, source_archive_sha256=extraction.archive.sha256, source_layer=reference.source_layer, crs=_crs_text(frame), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((str(column), int(frame[col…`.

**Algorithm**

1. Checks `frame.geometry.name not in frame.columns`. When true: Raises `GpuSpatialInspectionError(f'GPU layer has no active geometry: {reference.source_layer}')`.
2. Computes `geometry` from `frame.geometry`.
3. Computes `non_null` from `geometry.notna()`.
4. Computes `non_empty` from `non_null & ~geometry.is_empty`.
5. Computes `invalid` from `non_empty & ~geometry.is_valid`.
6. Computes `geometry_types` from `tuple(((str(key), int(value)) for key, value in geometry[non_null].geom_type.value_counts().sort_index().items()))`.
7. Returns `GpuLayerSummary(source_document_id=extraction.archive.document.document_id, source_archive_sha256=extraction.archive.sha256, source_layer=reference.source_layer, crs=_crs_text(frame), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_c…`.

**Validation and invariants**

- Rejects or diverts the path when `frame.geometry.name not in frame.columns` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(non_null & geometry.is_empty).sum`, `(~non_null).sum`, `GpuLayerSummary`, `GpuSpatialInspectionError`, `_crs_text`, `frame.dtypes.items`, `frame[column].isna`, `frame[column].isna().sum`, `geometry.notna`, `geometry[non_null].geom_type.value_counts`, `geometry[non_null].geom_type.value_counts().sort_index`, `geometry[non_null].geom_type.value_counts().sort_index().items`, `int`, `invalid.sum`, `len`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `_revalidate_gpu_spatial_layer_source`
- `src/landscout/sources/gpu_fr.py` — `inspect_gpu_planning_document`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `inspect_gpu_planning_document`

**Signature**

```python
def inspect_gpu_planning_document(
    extraction: GpuExtraction, config: GpuSourceConfig
) -> GpuPlanningDocument:
```

**Purpose**

Discover and inspect zoning/prescription layers without interpretation.

**Inputs**

- `extraction` (`GpuExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `GpuPlanningDocument(extraction=extraction, all_spatial_layers=references, zoning=zoning, related_layers=tuple(related))`.

**Algorithm**

1. Computes `references` from `discover_gpu_spatial_layers(extraction)`.
2. Computes `zoning_reference` from `_discover_logical_layer(references, config, 'zoning', required=True)`.
3. Asserts `zoning_reference is not None`.
4. Computes `zoning_data` from `_load_reference(zoning_reference)`.
5. Computes `zoning` from `GpuInspectedLayer(logical_name='zoning', reference=zoning_reference, data=zoning_data, summary=_summarize_layer(zoning_data, zoning_reference, extraction))`.
6. Defines `related` with annotation `list[GpuInspectedLayer]` from `[]`.
7. Defines `logical_names` with annotation `tuple[LogicalLayerName, ...]` from `('prescription_surface', 'prescription_line', 'prescription_point', 'information_surface', 'information_line', 'information_point')`.
8. Iterates `logical_name` over `logical_names`. For each value: Computes `reference` from `_discover_logical_layer(references, config, logical_name, required=False)`. Checks `reference is None`. When true: Executes `continue` control flow. Computes `data` from `_load_reference(reference)`. Executes 1 additional source-ordered statement(s).
9. Returns `GpuPlanningDocument(extraction=extraction, all_spatial_layers=references, zoning=zoning, related_layers=tuple(related))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_load_reference`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GpuInspectedLayer`, `GpuPlanningDocument`, `_discover_logical_layer`, `_load_reference`, `_summarize_layer`, `discover_gpu_spatial_layers`, `related.append`, `tuple`.

**Known repository callers**

- `src/landscout/sources/gpu_fr.py` — `ingest_gpu_planning_document`
- `tests/unit/test_gpu_fr.py` — `test_ambiguous_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py` — `test_missing_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py` — `test_spatial_inventory_and_inspection_preserve_source_quality`

**Tests**

- `tests/unit/test_gpu_fr.py::test_ambiguous_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py::test_missing_zoning_layer_fails_clearly`
- `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `ingest_gpu_planning_document`

**Signature**

```python
def ingest_gpu_planning_document(
    config: GpuSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> GpuPlanningDocument:
```

**Purpose**

High-level official GPU discovery, acquisition, extraction and inspection.

**Inputs**

- `config` (`GpuSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cache_dir` (`Path`; optional/default `DEFAULT_CACHE_DIR`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; optional/default `120.0`) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GpuPlanningDocument`. Observed return expression(s): `inspect_gpu_planning_document(extraction, config)`.

**Algorithm**

1. Computes `document` from `discover_current_gpu_document(config, timeout=timeout)`.
2. Computes `download` from `download_gpu_document(document, config, cache_dir, timeout)`.
3. Computes `extraction` from `extract_gpu_document(download, cache_dir)`.
4. Returns `inspect_gpu_planning_document(extraction, config)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `download_gpu_document`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `discover_current_gpu_document`, `download_gpu_document`, `extract_gpu_document`, `inspect_gpu_planning_document`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `finite_numeric_vocabulary`

**Signature**

```python
def finite_numeric_vocabulary(
    frame: gpd.GeoDataFrame, column: str
) -> tuple[tuple[str, int], ...]:
```

**Purpose**

Return deterministic raw value counts for inspection-only reporting.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `column` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[tuple[str, int], ...]`. Observed return expression(s): `tuple(sorted(result, key=lambda item: item[0]))`.

**Algorithm**

1. Checks `column not in frame.columns or column == frame.geometry.name`. When true: Raises `GpuSpatialInspectionError(f'Cannot inspect GPU attribute: {column}')`.
2. Computes `counts` from `frame[column].value_counts(dropna=False)`.
3. Defines `result` with annotation `list[tuple[str, int]]` from `[]`.
4. Iterates `(value, count)` over `counts.items()`. For each value: Checks `isinstance(value, float) and math.isnan(value) or value is None`. When true: Computes `label` from `'<NULL>'`. Otherwise: Computes `label` from `str(value)`. Calls `result.append((label, int(count)))` for its validation or side effect.
5. Returns `tuple(sorted(result, key=lambda item: item[0]))`.

**Validation and invariants**

- Rejects or diverts the path when `column not in frame.columns or column == frame.geometry.name` is true.

**Exceptions**

- Explicitly raises: `GpuSpatialInspectionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GpuSpatialInspectionError`, `counts.items`, `frame[column].value_counts`, `int`, `isinstance`, `math.isnan`, `result.append`, `sorted`, `str`, `tuple`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `FR` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `METADATA` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `OTHER_ATTACHMENT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `SPATIAL_DATA` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `WRITTEN_REGULATION` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `document` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `files` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `information_line` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `information_point` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `information_surface` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `partition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `prescription_line` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `prescription_point` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `prescription_surface` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `relative_path` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sha256` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `size_bytes` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `written_files` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
