# `src/landscout/sources/ign_bdtopo_fr.py`

## File identity

- Repository path: `src/landscout/sources/ign_bdtopo_fr.py`
- File type: Python source
- Primary responsibility: Acquires, verifies, extracts, inventories, selects, loads, and source-completely revalidates IGN BD TOPO layers.
- Layer / domain: `source adapter` / `grid`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `c9c43bb6568e7137ed6c9dd69e2605c419568bb95efbc0132800eb0915253ba5`

## 1. Purpose

Acquires, verifies, extracts, inventories, selects, loads, and source-completely revalidates IGN BD TOPO layers.

## 2. Position in LandScout architecture

This file is a `source adapter` artifact in the `grid` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import shutil` — required by the implementation paths and symbols documented below.
- `import sys` — required by the implementation paths and symbols documented below.
- `import unicodedata` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from datetime import UTC, date, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import md5, sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path, PurePosixPath, PureWindowsPath` — required by the implementation paths and symbols documented below.
- `from shutil import copy2, copyfileobj` — required by the implementation paths and symbols documented below.
- `from typing import Annotated, Any, Literal, Self` — required by the implementation paths and symbols documented below.
- `from urllib.error import HTTPError, URLError` — required by the implementation paths and symbols documented below.
- `from urllib.parse import unquote, urlparse` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import py7zr` — required by the implementation paths and symbols documented below.
- `import pyogrio` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from py7zr.exceptions import ArchiveError` — required by the implementation paths and symbols documented below.
- `from pydantic import ( BaseModel, ConfigDict, Field, HttpUrl, StringConstraints, ValidationError, field_validator, model_validator, )` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.safe_http import open_safe_https` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `DEFAULT_CONFIG_PATH` | `Path("configs/sources/ign_bdtopo_fr.yaml")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DEFAULT_CACHE_DIR` | `Path("data/cache/ign_bdtopo")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DOWNLOAD_CHUNK_SIZE` | `1024 * 1024` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SPATIAL_ROLE` | `"PROXY_GEOMETRY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `COVERAGE_SPATIAL_ROLE` | `"SOURCE_COVERAGE_BOUNDARY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `IgnBdTopoLogicalLayerConfig`

**Purpose:** Catalogue class label and normalized tokens used for layer discovery.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `class_label` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `match_tokens` | `tuple[NonEmptyString, ...]` | `Field(min_length=1)` | `tuple[NonEmptyString, ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_unique_tokens` — `def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:`; decorators `field_validator('match_tokens'), classmethod`. The complete method algorithm appears in the function/method section.

### `IgnBdTopoLogicalLayersConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `electric_lines` | `IgnBdTopoLogicalLayerConfig` | `required` | `IgnBdTopoLogicalLayerConfig` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `transformation_posts` | `IgnBdTopoLogicalLayerConfig` | `required` | `IgnBdTopoLogicalLayerConfig` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_different_token_sets` — `def _different_token_sets(self) -> Self:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `IgnBdTopoDepartmentLayerConfig`

**Purpose:** Configured department layer and its observed identity field.

**Inheritance:** `IgnBdTopoLogicalLayerConfig`.

**Model form and mutability:** class inheriting from `IgnBdTopoLogicalLayerConfig`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `department_code_field` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoAccessConfig`

**Purpose:** Configured factual transport layers loaded outside extraction metadata.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `road_segments` | `IgnBdTopoLogicalLayerConfig` | `required` | `IgnBdTopoLogicalLayerConfig` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoCoverageConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `department_layer` | `IgnBdTopoDepartmentLayerConfig` | `required` | `IgnBdTopoDepartmentLayerConfig` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoSourceConfig`

**Purpose:** Strict, reproducible description of one official IGN package.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `provider` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `product` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `department_code` | `DepartmentCode` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `edition` | `EditionString` | `required` | `EditionString` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `product_version` | `NonEmptyString | None` | `None` | `NonEmptyString | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `projection` | `Projection` | `required` | `Projection` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `format` | `PackageFormat` | `required` | `PackageFormat` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `archive_format` | `ArchiveFormat` | `required` | `ArchiveFormat` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_url` | `HttpUrl` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `checksum_url` | `HttpUrl | None` | `None` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `official_checksum_algorithm` | `ChecksumAlgorithm | None` | `None` | `ChecksumAlgorithm | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_checksum` | `HexChecksum | None` | `None` | `HexChecksum | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `expected_archive_size_bytes` | `int | None` | `Field(default=None, gt=0)` | `int | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache_max_age_hours` | `float` | `Field(ge=0, allow_inf_nan=False)` | `float` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `logical_layers` | `IgnBdTopoLogicalLayersConfig` | `required` | `IgnBdTopoLogicalLayersConfig` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `access` | `IgnBdTopoAccessConfig` | `required` | `IgnBdTopoAccessConfig` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `coverage` | `IgnBdTopoCoverageConfig` | `required` | `IgnBdTopoCoverageConfig` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_valid_edition_date` — `def _valid_edition_date(cls, value: str) -> str:`; decorators `field_validator('edition'), classmethod`. The complete method algorithm appears in the function/method section.
- `_consistent_package_and_checksum` — `def _consistent_package_and_checksum(self) -> Self:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `IgnBdTopoError`

**Purpose:** Base error for controlled IGN BD TOPO source failures.

**Inheritance:** `RuntimeError`.

**Model form and mutability:** class inheriting from `RuntimeError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `IgnBdTopoDownloadError`

**Purpose:** Raised when an IGN archive cannot be downloaded or cached safely.

**Inheritance:** `IgnBdTopoError`.

**Model form and mutability:** class inheriting from `IgnBdTopoError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `IgnBdTopoArchiveError`

**Purpose:** Raised when an IGN archive or its extraction is unsafe or invalid.

**Inheritance:** `IgnBdTopoError`.

**Model form and mutability:** class inheriting from `IgnBdTopoError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `IgnBdTopoLayerError`

**Purpose:** Raised when required GeoPackage layers cannot be discovered or loaded.

**Inheritance:** `IgnBdTopoError`.

**Model form and mutability:** class inheriting from `IgnBdTopoError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `IgnBdTopoArchiveIntegrity`

**Purpose:** Groups the `IgnBdTopoArchiveIntegrity` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `file_size` | `int` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `official_checksum_algorithm` | `ChecksumAlgorithm | None` | `required` | `ChecksumAlgorithm | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_checksum` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_checksum_validated` | `bool` | `required` | `bool` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoDownload`

**Purpose:** Carries an immutable downloaded-source lineage envelope including byte identity and cache status.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `provider` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `product` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `department_code` | `str` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `edition` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `product_version` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `projection` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `package_format` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `archive_format` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `checksum_url` | `str | None` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `download_timestamp` | `str` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `filename` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `file_size` | `int` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `official_checksum_algorithm` | `ChecksumAlgorithm | None` | `required` | `ChecksumAlgorithm | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_checksum` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_checksum_validated` | `bool` | `required` | `bool` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `path` | `Path` | `required` | `Path` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache_hit` | `bool` | `required` | Boolean recording whether verified local bytes were reused instead of acquired during this call. |
| `spatial_role` | `SpatialRole` | `'PROXY_GEOMETRY'` | `SpatialRole` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoLayerSelection`

**Purpose:** Groups the `IgnBdTopoLayerSelection` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `all_layer_names` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `electric_lines_layer` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `transformation_posts_layer` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoExtraction`

**Purpose:** Carries an immutable extraction envelope binding extracted files to their source archive.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `archive` | `IgnBdTopoDownload` | `required` | `IgnBdTopoDownload` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `extraction_path` | `Path` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `geopackage_path` | `Path` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `geopackage_filename` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `geopackage_size_bytes` | `int` | `required` | `int` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `geopackage_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `all_layer_names` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `electric_lines_layer` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `transformation_posts_layer` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache_hit` | `bool` | `required` | Boolean recording whether verified local bytes were reused instead of acquired during this call. |
| `spatial_role` | `SpatialRole` | `'PROXY_GEOMETRY'` | `SpatialRole` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoLayerSummary`

**Purpose:** Carries deterministic factual counts, schema, or geometry summary data used to validate a frame or source.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `logical_name` | `LogicalLayerName` | `required` | `LogicalLayerName` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_layer_name` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `crs` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `feature_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `columns` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `dtypes` | `tuple[tuple[str, str], ...]` | `required` | `tuple[tuple[str, str], ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `null_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `empty_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `invalid_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `geometry_types` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `spatial_role` | `SpatialRole` | `'PROXY_GEOMETRY'` | `SpatialRole` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoLoadedLayer`

**Purpose:** Groups the `IgnBdTopoLoadedLayer` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `data` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `summary` | `IgnBdTopoLayerSummary` | `required` | `IgnBdTopoLayerSummary` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoElectricityData`

**Purpose:** Groups the `IgnBdTopoElectricityData` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `extraction` | `IgnBdTopoExtraction` | `required` | `IgnBdTopoExtraction` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `electric_lines` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `transformation_posts` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `electric_lines_summary` | `IgnBdTopoLayerSummary` | `required` | `IgnBdTopoLayerSummary` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `transformation_posts_summary` | `IgnBdTopoLayerSummary` | `required` | `IgnBdTopoLayerSummary` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `spatial_role` | `SpatialRole` | `'PROXY_GEOMETRY'` | `SpatialRole` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoRoadData`

**Purpose:** Unfiltered factual road geometry from one verified IGN extraction.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `extraction` | `IgnBdTopoExtraction` | `required` | `IgnBdTopoExtraction` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `road_segments` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `road_segments_summary` | `IgnBdTopoLayerSummary` | `required` | `IgnBdTopoLayerSummary` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoCoverageLayerSummary`

**Purpose:** Observed source-layer schema plus the authoritative selected feature.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `source_layer_name` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `crs` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_feature_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `selected_feature_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `columns` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `dtypes` | `tuple[tuple[str, str], ...]` | `required` | `tuple[tuple[str, str], ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `null_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `empty_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `invalid_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `geometry_types` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `department_code_field` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `selected_department_code` | `str` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `spatial_role` | `CoverageSpatialRole` | `'SOURCE_COVERAGE_BOUNDARY'` | `CoverageSpatialRole` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnBdTopoDepartmentCoverage`

**Purpose:** Selected department coverage with package lineage and source schema.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `extraction` | `IgnBdTopoExtraction` | `required` | `IgnBdTopoExtraction` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `coverage` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `summary` | `IgnBdTopoCoverageLayerSummary` | `required` | `IgnBdTopoCoverageLayerSummary` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_provider` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `source_product` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `source_department_code` | `str` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `source_edition` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `source_product_version` | `str | None` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `source_archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_layer` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `spatial_role` | `CoverageSpatialRole` | `'SOURCE_COVERAGE_BOUNDARY'` | `CoverageSpatialRole` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_CacheMetadata`

**Purpose:** Represents strict metadata used to reconstruct or validate a byte-bound cache/source object.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `Literal[1]` | `required` | `Literal[1]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `provider` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `product` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `department_code` | `str` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `edition` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `product_version` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `projection` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `package_format` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `archive_format` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `checksum_url` | `str | None` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `download_timestamp` | `str` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `filename` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `file_size` | `int` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `official_checksum_algorithm` | `ChecksumAlgorithm | None` | `required` | `ChecksumAlgorithm | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_checksum` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_checksum_validated` | `bool` | `required` | `bool` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `spatial_role` | `SpatialRole` | `required` | `SpatialRole` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_ExtractionMetadata`

**Purpose:** Carries an immutable extraction envelope binding extracted files to their source archive.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `Literal[2]` | `required` | `Literal[2]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `archive_sha256` | `CanonicalSha256` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `geopackage_relative_path` | `str` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |
| `geopackage_size_bytes` | `StrictPositiveInt` | `required` | `StrictPositiveInt` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `geopackage_sha256` | `CanonicalSha256` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `all_layer_names` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `electric_lines_layer` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `transformation_posts_layer` | `str` | `required` | `str` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `spatial_role` | `SpatialRole` | `required` | `SpatialRole` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_VerifiedIgnExtraction`

**Purpose:** Carries an immutable extraction envelope binding extracted files to their source archive.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `extraction` | `IgnBdTopoExtraction` | `required` | `IgnBdTopoExtraction` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `metadata` | `_ExtractionMetadata` | `required` | `_ExtractionMetadata` state used by `src/landscout/sources/ign_bdtopo_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `geopackage_path` | `Path` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `IgnBdTopoLogicalLayerConfig._unique_tokens`

**Signature**

```python
def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
```

**Purpose**

Implements unique tokens according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `value`.

**Algorithm**

1. Computes `normalized` from `tuple((_normalize_words(token) for token in value))`.
2. Checks `any((not token for token in normalized))`. When true: Raises `ValueError('Layer match tokens must contain letters or digits')`.
3. Checks `len(set(normalized)) != len(normalized)`. When true: Raises `ValueError('Layer match tokens must be unique after normalization')`.
4. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `any((not token for token in normalized))` is true.
- Rejects or diverts the path when `len(set(normalized)) != len(normalized)` is true.

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

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `IgnBdTopoLogicalLayersConfig._different_token_sets`

**Signature**

```python
def _different_token_sets(self) -> Self:
```

**Purpose**

Implements different token sets according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Computes `electric` from `{_normalize_words(token) for token in self.electric_lines.match_tokens}`.
2. Computes `posts` from `{_normalize_words(token) for token in self.transformation_posts.match_tokens}`.
3. Checks `electric == posts`. When true: Raises `ValueError('Logical layers must use different match tokens')`.
4. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `electric == posts` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_normalize_words`, `model_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `IgnBdTopoSourceConfig._valid_edition_date`

**Signature**

```python
def _valid_edition_date(cls, value: str) -> str:
```

**Purpose**

Implements valid edition date according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Runs guarded operation: Calls `date.fromisoformat(value)` for its validation or side effect. Handles `ValueError`.
2. Returns `value`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `date.fromisoformat`, `field_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `IgnBdTopoSourceConfig._consistent_package_and_checksum`

**Signature**

```python
def _consistent_package_and_checksum(self) -> Self:
```

**Purpose**

Implements consistent package and checksum according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Computes `path` from `unquote(urlparse(str(self.source_url)).path)`.
2. Checks `Path(path).suffix.casefold() != f'.{self.archive_format}'`. When true: Raises `ValueError('source_url extension does not match archive_format')`.
3. Computes `has_algorithm` from `self.official_checksum_algorithm is not None`.
4. Computes `has_checksum` from `self.official_checksum is not None`.
5. Checks `has_algorithm != has_checksum`. When true: Raises `ValueError('official_checksum_algorithm and official_checksum must be set together')`.
6. Checks `self.official_checksum_algorithm == 'md5' and len(self.official_checksum or '') != 32`. When true: Raises `ValueError('An official MD5 checksum must contain 32 hexadecimal digits')`.
7. Checks `self.official_checksum_algorithm == 'sha256' and len(self.official_checksum or '') != 64`. When true: Raises `ValueError('An official SHA256 checksum must contain 64 hexadecimal digits')`.
8. Checks `self.checksum_url is not None and (not has_checksum)`. When true: Raises `ValueError('checksum_url requires a pinned official checksum and algorithm')`.
9. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `Path(path).suffix.casefold() != f'.{self.archive_format}'` is true.
- Rejects or diverts the path when `has_algorithm != has_checksum` is true.
- Rejects or diverts the path when `self.official_checksum_algorithm == 'md5' and len(self.official_checksum or '') != 32` is true.
- Rejects or diverts the path when `self.official_checksum_algorithm == 'sha256' and len(self.official_checksum or '') != 64` is true.
- Rejects or diverts the path when `self.checksum_url is not None and (not has_checksum)` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Path`, `Path(path).suffix.casefold`, `ValueError`, `len`, `model_validator`, `str`, `unquote`, `urlparse`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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

- Declared return type: `str`. Observed return expression(s): `' '.join(re.findall('[a-z0-9]+', ascii_like))`.

**Algorithm**

1. Computes `decomposed` from `unicodedata.normalize('NFKD', value.casefold())`.
2. Computes `ascii_like` from `''.join((char for char in decomposed if not unicodedata.combining(char)))`.
3. Returns `' '.join(re.findall('[a-z0-9]+', ascii_like))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `' '.join`, `''.join`, `re.findall`, `unicodedata.combining`, `unicodedata.normalize`, `value.casefold`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `IgnBdTopoLogicalLayerConfig._unique_tokens`
- `src/landscout/sources/ign_bdtopo_fr.py` — `IgnBdTopoLogicalLayersConfig._different_token_sets`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_matching_layers`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_source_config`

**Signature**

```python
def load_ign_bdtopo_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> IgnBdTopoSourceConfig:
```

**Purpose**

Load and strictly validate the pinned IGN source configuration.

**Inputs**

- `path` (`Path`; optional/default `DEFAULT_CONFIG_PATH`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoSourceConfig`. Observed return expression(s): `IgnBdTopoSourceConfig.model_validate(content)`.

**Algorithm**

1. Runs guarded operation: Enters managed context(s) `path.open(encoding='utf-8')` and executes: Computes `content` from `yaml.safe_load(stream)`. Handles `OSError`.
2. Checks `not isinstance(content, dict)`. When true: Raises `TypeError(f'Expected a YAML mapping in {path}')`.
3. Returns `IgnBdTopoSourceConfig.model_validate(content)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(content, dict)` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoDownloadError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `IgnBdTopoDownloadError`, `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoDownloadError`, `IgnBdTopoSourceConfig.model_validate`, `TypeError`, `isinstance`, `path.open`, `yaml.safe_load`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `source_config`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_archive_filename`

**Signature**

```python
def _archive_filename(config: IgnBdTopoSourceConfig) -> str:
```

**Purpose**

Implements archive filename according to the exact implementation and guards in this file.

**Inputs**

- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `filename`.

**Algorithm**

1. Computes `filename` from `Path(unquote(urlparse(str(config.source_url)).path)).name`.
2. Checks `not filename or Path(filename).suffix.casefold() != '.7z'`. When true: Raises `IgnBdTopoDownloadError('IGN source URL does not identify a .7z archive')`.
3. Returns `filename`.

**Validation and invariants**

- Rejects or diverts the path when `not filename or Path(filename).suffix.casefold() != '.7z'` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `IgnBdTopoDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoDownloadError`, `Path`, `Path(filename).suffix.casefold`, `str`, `unquote`, `urlparse`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_validate_archive_config_lineage`
- `src/landscout/sources/ign_bdtopo_fr.py` — `download_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_calculate_checksums`

**Signature**

```python
def _calculate_checksums(
    path: Path, official_algorithm: ChecksumAlgorithm | None
) -> tuple[str, str | None]:
```

**Purpose**

Implements calculate checksums according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `official_algorithm` (`ChecksumAlgorithm | None`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, str | None]`. Observed return expression(s): `(sha256_digest.hexdigest(), official_digest.hexdigest() if official_digest is not None else None)`.

**Algorithm**

1. Computes `sha256_digest` from `sha256()`.
2. Computes `official_digest` from `None`.
3. Checks `official_algorithm == 'md5'`. When true: Computes `official_digest` from `md5(usedforsecurity=False)`. Otherwise: Checks `official_algorithm == 'sha256'`. When true: Computes `official_digest` from `sha256()`.
4. Runs guarded operation: Enters managed context(s) `path.open('rb')` and executes: Iterates `chunk` over `iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b'')`. For each value: Calls `sha256_digest.update(chunk)` for its validation or side effect. Checks `official_digest is not None`. When true: Calls `official_digest.update(chunk)` for its validation or side effect. Handles `OSError`.
5. Returns `(sha256_digest.hexdigest(), official_digest.hexdigest() if official_digest is not None else None)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `IgnBdTopoArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoArchiveError`, `iter`, `md5`, `official_digest.hexdigest`, `official_digest.update`, `path.open`, `sha256`, `sha256_digest.hexdigest`, `sha256_digest.update`, `stream.read`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `validate_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `validate_ign_bdtopo_archive`

**Signature**

```python
def validate_ign_bdtopo_archive(
    path: Path, config: IgnBdTopoSourceConfig
) -> IgnBdTopoArchiveIntegrity:
```

**Purpose**

Validate size, configured official checksum, and available 7z CRC data. Some official IGN archives omit container CRC metadata, for which py7zr returns ``None``. Such archives still require exact official size/checksum validation here and a successful full extraction before they are usable.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoArchiveIntegrity`. Observed return expression(s): `IgnBdTopoArchiveIntegrity(file_size=file_size, sha256=local_sha256, official_checksum_algorithm=config.official_checksum_algorithm, official_checksum=config.official_checksum, official_checksum_validated=official_validated)`.

**Algorithm**

1. Checks `not path.is_file()`. When true: Raises `IgnBdTopoArchiveError(f'IGN archive does not exist: {path}')`.
2. Runs guarded operation: Computes `file_size` from `path.stat().st_size`. Handles `OSError`.
3. Checks `file_size <= 0`. When true: Raises `IgnBdTopoArchiveError(f'IGN archive is empty: {path}')`.
4. Checks `config.expected_archive_size_bytes is not None and file_size != config.expected_archive_size_bytes`. When true: Raises `IgnBdTopoArchiveError(f'IGN archive size does not match the official catalogue: {file_size} != {config.expected_archive_size_bytes}')`.
5. Computes `(local_sha256, calculated_official)` from `_calculate_checksums(path, config.official_checksum_algorithm)`.
6. Computes `official_validated` from `config.official_checksum is not None`.
7. Checks `official_validated and calculated_official != config.official_checksum`. When true: Raises `IgnBdTopoArchiveError(f'IGN archive does not match the pinned official {config.official_checksum_algorithm} checksum')`.
8. Runs guarded operation: Enters managed context(s) `py7zr.SevenZipFile(path, mode='r')` and executes: Computes `integrity_result` from `archive.test()`. Handles `(ArchiveError, EOFError, OSError, ValueError)`.
9. Checks `integrity_result is False`. When true: Raises `IgnBdTopoArchiveError(f'IGN archive failed its 7z CRC integrity check: {path}')`.
10. Returns `IgnBdTopoArchiveIntegrity(file_size=file_size, sha256=local_sha256, official_checksum_algorithm=config.official_checksum_algorithm, official_checksum=config.official_checksum, official_checksum_validated=official_validated)`.

**Validation and invariants**

- Rejects or diverts the path when `not path.is_file()` is true.
- Rejects or diverts the path when `file_size <= 0` is true.
- Rejects or diverts the path when `config.expected_archive_size_bytes is not None and file_size != config.expected_archive_size_bytes` is true.
- Rejects or diverts the path when `official_validated and calculated_official != config.official_checksum` is true.
- Rejects or diverts the path when `integrity_result is False` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoArchiveError`, `IgnBdTopoArchiveIntegrity`, `_calculate_checksums`, `archive.test`, `path.is_file`, `path.stat`, `py7zr.SevenZipFile`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_load_cached_download`
- `src/landscout/sources/ign_bdtopo_fr.py` — `download_ign_bdtopo_archive`
- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_cache_metadata_from_download`

**Signature**

```python
def _cache_metadata_from_download(download: IgnBdTopoDownload) -> _CacheMetadata:
```

**Purpose**

Implements cache metadata from download according to the exact implementation and guards in this file.

**Inputs**

- `download` (`IgnBdTopoDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_CacheMetadata`. Observed return expression(s): `_CacheMetadata(schema_version=1, provider=download.provider, product=download.product, department_code=download.department_code, edition=download.edition, product_version=download.product_version, projection=download.projection, package_format=download.package_format, archive_format=download.archive_format, source_url=download.source_url, checksum_url=download.checksum_url, download_timestamp=dow…`.

**Algorithm**

1. Returns `_CacheMetadata(schema_version=1, provider=download.provider, product=download.product, department_code=download.department_code, edition=download.edition, product_version=download.product_version, projection=download.projection, package_format=download.package_format, archive_format=download.archive_format, source_url=download.source_url, checksum_url=downl…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_CacheMetadata`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `download_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_download_from_metadata`

**Signature**

```python
def _download_from_metadata(
    metadata: _CacheMetadata, archive_path: Path, *, cache_hit: bool
) -> IgnBdTopoDownload:
```

**Purpose**

Downloads and validates from metadata according to the exact implementation and guards in this file.

**Inputs**

- `metadata` (`_CacheMetadata`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cache_hit` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoDownload`. Observed return expression(s): `IgnBdTopoDownload(provider=metadata.provider, product=metadata.product, department_code=metadata.department_code, edition=metadata.edition, product_version=metadata.product_version, projection=metadata.projection, package_format=metadata.package_format, archive_format=metadata.archive_format, source_url=metadata.source_url, checksum_url=metadata.checksum_url, download_timestamp=metadata.download_…`.

**Algorithm**

1. Returns `IgnBdTopoDownload(provider=metadata.provider, product=metadata.product, department_code=metadata.department_code, edition=metadata.edition, product_version=metadata.product_version, projection=metadata.projection, package_format=metadata.package_format, archive_format=metadata.archive_format, source_url=metadata.source_url, checksum_url=metadata.checksum_ur…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `IgnBdTopoDownload`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoDownload`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_load_cached_download`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_load_cached_download`

**Signature**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDownload | None:
```

**Purpose**

Loads cached download according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoDownload | None`. Observed return expression(s): `None`; `_download_from_metadata(metadata, archive_path, cache_hit=True)`.

**Algorithm**

1. Checks `not archive_path.is_file() or not metadata_path.is_file()`. When true: Returns `None`.
2. Runs guarded operation: Computes `metadata` from `_CacheMetadata.model_validate_json(metadata_path.read_text(encoding='utf-8'))`. Computes `downloaded_at` from `datetime.fromisoformat(metadata.download_timestamp)`. Checks `downloaded_at.tzinfo is None`. When true: Returns `None`. Computes `age_seconds` from `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds()`. Executes 6 additional source-ordered statement(s). Handles `(IgnBdTopoArchiveError, OSError, TypeError, ValueError, ValidationError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds`, `_download_from_metadata`, `downloaded_at.astimezone`, `metadata_path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds`, `_CacheMetadata.model_validate_json`, `_download_from_metadata`, `any`, `archive_path.is_file`, `datetime.fromisoformat`, `datetime.now`, `downloaded_at.astimezone`, `metadata_path.is_file`, `metadata_path.read_text`, `str`, `validate_ign_bdtopo_archive`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `download_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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

- `src/landscout/sources/ign_bdtopo_fr.py` — `_publish_cache_pair`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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

- Declared return type: `tuple[Path, Path]`. Observed return expression(s): `(archive_path.with_name(f'{archive_path.name}.bak'), metadata_path.with_name(f'{metadata_path.name}.bak'))`.

**Algorithm**

1. Returns `(archive_path.with_name(f'{archive_path.name}.bak'), metadata_path.with_name(f'{metadata_path.name}.bak'))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `archive_path.with_name`, `metadata_path.with_name`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_publish_cache_pair`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_require_no_cache_recovery_material`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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
2. Checks `any((path.exists() or path.is_symlink() or path.is_junction() for path in recovery_paths))`. When true: Raises `IgnBdTopoDownloadError('IGN cache recovery backup already exists; manual recovery is required')`.

**Validation and invariants**

- Rejects or diverts the path when `any((path.exists() or path.is_symlink() or path.is_junction() for path in recovery_paths))` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `IgnBdTopoDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoDownloadError`, `_cache_recovery_paths`, `any`, `path.exists`, `path.is_junction`, `path.is_symlink`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_publish_cache_pair`
- `src/landscout/sources/ign_bdtopo_fr.py` — `download_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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

1. Runs guarded operation: Checks `path.is_symlink() or path.is_junction()`. When true: Raises `IgnBdTopoDownloadError('IGN cache temporary path is a link or junction')`. Checks `path.exists()`. When true: Checks `not path.is_file()`. When true: Raises `IgnBdTopoDownloadError('IGN cache temporary path is not a regular file')`. Calls `path.unlink()` for its validation or side effect. Handles `IgnBdTopoDownloadError`, `OSError`.

**Validation and invariants**

- Rejects or diverts the path when `path.is_symlink() or path.is_junction()` is true.
- Rejects or diverts the path when `path.exists()` is true.
- Rejects or diverts the path when `not path.is_file()` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `IgnBdTopoDownloadError`, `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoDownloadError`, `path.exists`, `path.is_file`, `path.is_junction`, `path.is_symlink`, `path.unlink`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `download_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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
3. Checks `cleanup_error is not None and primary_error is None`. When true: Raises `IgnBdTopoDownloadError('IGN cache temporary files could not be cleaned safely')`.

**Validation and invariants**

- Rejects or diverts the path when `cleanup_error is not None and primary_error is None` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `IgnBdTopoDownloadError`, `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoDownloadError`, `path.unlink`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `download_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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
6. Computes `archive_published` from `False`.
7. Runs guarded operation: Calls `_replace_file(temporary_archive, archive_path)` for its validation or side effect. Computes `archive_published` from `True`. Calls `_replace_file(temporary_metadata, metadata_path)` for its validation or side effect. Handles `OSError`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `IgnBdTopoDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `IgnBdTopoDownloadError`, `_replace_file`, `archive_backup.unlink`, `archive_path.unlink`, `copy2`, `metadata_backup.unlink`, `metadata_path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoDownloadError`, `_cache_recovery_paths`, `_replace_file`, `_require_no_cache_recovery_material`, `archive_backup.unlink`, `archive_path.is_file`, `archive_path.unlink`, `copy2`, `metadata_backup.unlink`, `metadata_path.is_file`, `metadata_path.unlink`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `download_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `download_ign_bdtopo_archive`

**Signature**

```python
def download_ign_bdtopo_archive(
    config: IgnBdTopoSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> IgnBdTopoDownload:
```

**Purpose**

Download or reuse the pinned IGN package with atomic cache publication.

**Inputs**

- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cache_dir` (`Path`; optional/default `DEFAULT_CACHE_DIR`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; optional/default `120.0`) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoDownload`. Observed return expression(s): `cached`; `result`.

**Algorithm**

1. Computes `filename` from `_archive_filename(config)`.
2. Computes `archive_path` from `cache_dir / filename`.
3. Computes `metadata_path` from `cache_dir / f'{filename}.metadata.json'`.
4. Calls `_require_no_cache_recovery_material(archive_path, metadata_path)` for its validation or side effect.
5. Computes `cached` from `_load_cached_download(archive_path, metadata_path, config)`.
6. Checks `cached is not None`. When true: Returns `cached`.
7. Calls `cache_dir.mkdir(parents=True, exist_ok=True)` for its validation or side effect.
8. Computes `temporary_archive` from `archive_path.with_name(f'{archive_path.name}.part')`.
9. Computes `temporary_metadata` from `metadata_path.with_name(f'{metadata_path.name}.part')`.
10. Calls `_prepare_temporary_cache_file(temporary_archive)` for its validation or side effect.
11. Calls `_prepare_temporary_cache_file(temporary_metadata)` for its validation or side effect.
12. Computes `source_url` from `str(config.source_url)`.
13. Runs guarded operation: Enters managed context(s) `open_safe_https(source_url, timeout=timeout, headers={'User-Agent': 'LandScout-AI/0.1'}), temporary_archive.open('wb')` and executes: Calls `copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)` for its validation or side effect. Computes `integrity` from `validate_ign_bdtopo_archive(temporary_archive, config)`. Computes `download_timestamp` from `datetime.now(UTC).isoformat()`. Computes `result` from `IgnBdTopoDownload(provider=config.provider, product=config.product, department_code=config.department_code, edition=config.edition, product_version=config.product_version, projection=config.projection, package_format=config.format, archive_format=config.archive_format, source_url=source_url, checksum_url=str(config.ch…`. Executes 4 additional source-ordered statement(s). Handles `IgnBdTopoArchiveError`, `(HTTPError, URLError, OSError)`. Finally: Calls `_cleanup_temporary_cache_files((temporary_archive, temporary_metadata), sys.exception())` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `IgnBdTopoDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `IgnBdTopoDownload`, `IgnBdTopoDownloadError`, `_cache_metadata_from_download`, `_load_cached_download`, `cache_dir.mkdir`, `copyfileobj`, `open_safe_https`, `temporary_archive.open`, `temporary_metadata.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoDownload`, `IgnBdTopoDownloadError`, `_archive_filename`, `_cache_metadata_from_download`, `_cleanup_temporary_cache_files`, `_load_cached_download`, `_prepare_temporary_cache_file`, `_publish_cache_pair`, `_require_no_cache_recovery_material`, `archive_path.with_name`, `cache_dir.mkdir`, `copyfileobj`, `datetime.now`, `datetime.now(UTC).isoformat`, `metadata.model_dump_json`, `metadata_path.with_name`, `open_safe_https`, `str`, `sys.exception`, `temporary_archive.open`, `temporary_metadata.write_text`, `validate_ign_bdtopo_archive`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `_extracted_fixture`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_fresh_cache_is_reused_without_network`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_official_checksum_mismatch_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_successful_archive_download_persists_sha256`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_synthetic_archive_extracts_and_discovers_required_layers`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_unsafe_parent_archive_member_is_rejected`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`
- `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network`
- `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network`
- `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256`
- `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers`
- `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_archive_members`

**Signature**

```python
def _validate_archive_members(archive: py7zr.SevenZipFile) -> None:
```

**Purpose**

Validates and rejects malformed archive members according to the exact implementation and guards in this file.

**Inputs**

- `archive` (`py7zr.SevenZipFile`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `infos` from `archive.list()`.
2. Checks `not infos`. When true: Raises `IgnBdTopoArchiveError('IGN archive contains no members')`.
3. Iterates `info` over `infos`. For each value: Computes `name` from `info.filename`. Checks `not name or '\x00' in name`. When true: Raises `IgnBdTopoArchiveError('IGN archive contains an invalid member name')`. Computes `normalized_name` from `name.replace('\\', '/')`. Executes 4 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `not infos` is true.
- Rejects or diverts the path when `not name or '\x00' in name` is true.
- Rejects or diverts the path when `posix_path.is_absolute() or windows_path.is_absolute() or bool(windows_path.drive) or ('..' in posix_path.parts)` is true.
- Rejects or diverts the path when `info.is_symlink or not (info.is_file or info.is_directory)` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `name.replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoArchiveError`, `PurePosixPath`, `PureWindowsPath`, `archive.list`, `bool`, `name.replace`, `posix_path.is_absolute`, `windows_path.is_absolute`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `discover_ign_bdtopo_geopackage`

**Signature**

```python
def discover_ign_bdtopo_geopackage(root: Path) -> Path:
```

**Purpose**

Return the sole GeoPackage below an extracted package root.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `geopackages[0]`; `root`.

**Algorithm**

1. Checks `root.is_file()`. When true: Checks `root.suffix.casefold() == '.gpkg'`. When true: Returns `root`. Raises `IgnBdTopoArchiveError(f'Expected a GeoPackage, got: {root}')`.
2. Checks `not root.is_dir()`. When true: Raises `IgnBdTopoArchiveError(f'Extraction directory does not exist: {root}')`.
3. Computes `geopackages` from `sorted((path for path in root.rglob('*') if path.is_file() and path.suffix.casefold() == '.gpkg'), key=lambda path: path.as_posix().casefold())`.
4. Checks `len(geopackages) != 1`. When true: Raises `IgnBdTopoArchiveError(f'Expected exactly one GeoPackage in the IGN package, found {len(geopackages)}')`.
5. Returns `geopackages[0]`.

**Validation and invariants**

- Rejects or diverts the path when `root.is_file()` is true.
- Rejects or diverts the path when `not root.is_dir()` is true.
- Rejects or diverts the path when `len(geopackages) != 1` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoArchiveError`, `len`, `path.as_posix`, `path.as_posix().casefold`, `path.is_file`, `path.suffix.casefold`, `root.is_dir`, `root.is_file`, `root.rglob`, `root.suffix.casefold`, `sorted`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_load_cached_extraction`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_validate_extraction_envelope`
- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_geopackage_is_discovered_recursively`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_multiple_geopackages_are_rejected_as_ambiguous`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_geopackage_is_discovered_recursively`
- `tests/unit/test_ign_bdtopo_fr.py::test_multiple_geopackages_are_rejected_as_ambiguous`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `list_ign_bdtopo_layers`

**Signature**

```python
def list_ign_bdtopo_layers(geopackage_path: Path) -> tuple[str, ...]:
```

**Purpose**

List every real layer name exposed by an IGN GeoPackage.

**Inputs**

- `geopackage_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `names`.

**Algorithm**

1. Checks `not geopackage_path.is_file()`. When true: Raises `IgnBdTopoLayerError(f'GeoPackage does not exist: {geopackage_path}')`.
2. Runs guarded operation: Computes `listed` from `pyogrio.list_layers(geopackage_path)`. Computes `names` from `tuple((str(row[0]) for row in listed))`. Handles `Exception`.
3. Checks `not names or any((not name.strip() for name in names))`. When true: Raises `IgnBdTopoLayerError('GeoPackage exposes no valid layer names')`.
4. Checks `len(set(names)) != len(names)`. When true: Raises `IgnBdTopoLayerError('GeoPackage exposes duplicate layer names')`.
5. Returns `names`.

**Validation and invariants**

- Rejects or diverts the path when `not geopackage_path.is_file()` is true.
- Rejects or diverts the path when `not names or any((not name.strip() for name in names))` is true.
- Rejects or diverts the path when `len(set(names)) != len(names)` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `any`, `geopackage_path.is_file`, `len`, `name.strip`, `pyogrio.list_layers`, `set`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_validate_extraction_envelope`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_verify_unchanged_extraction`
- `src/landscout/sources/ign_bdtopo_fr.py` — `discover_ign_bdtopo_layers`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_real_layer_names_are_listed_and_discovered`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_real_layer_names_are_listed_and_discovered`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_matching_layers`

**Signature**

```python
def _matching_layers(
    layer_names: tuple[str, ...], logical_config: IgnBdTopoLogicalLayerConfig
) -> tuple[str, ...]:
```

**Purpose**

Implements matching layers according to the exact implementation and guards in this file.

**Inputs**

- `layer_names` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_config` (`IgnBdTopoLogicalLayerConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `tuple(matches)`.

**Algorithm**

1. Defines `token_words` with annotation `set[str]` from `set()`.
2. Iterates `token` over `logical_config.match_tokens`. For each value: Calls `token_words.update(_normalize_words(token).split())` for its validation or side effect.
3. Computes `matches` from `[]`.
4. Iterates `layer_name` over `layer_names`. For each value: Computes `layer_words` from `set(_normalize_words(layer_name).split())`. Checks `token_words.issubset(layer_words)`. When true: Calls `matches.append(layer_name)` for its validation or side effect.
5. Returns `tuple(matches)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_normalize_words`, `_normalize_words(layer_name).split`, `_normalize_words(token).split`, `matches.append`, `set`, `token_words.issubset`, `token_words.update`, `tuple`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_discover_department_coverage_layer`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_discover_road_layer`
- `src/landscout/sources/ign_bdtopo_fr.py` — `discover_ign_bdtopo_layers`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `discover_ign_bdtopo_layers`

**Signature**

```python
def discover_ign_bdtopo_layers(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoLayerSelection:
```

**Purpose**

Resolve both configured logical classes without assuming exact casing.

**Inputs**

- `geopackage_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoLayerSelection`. Observed return expression(s): `IgnBdTopoLayerSelection(all_layer_names=layer_names, electric_lines_layer=electric_matches[0], transformation_posts_layer=post_matches[0])`.

**Algorithm**

1. Computes `layer_names` from `list_ign_bdtopo_layers(geopackage_path)`.
2. Computes `electric_matches` from `_matching_layers(layer_names, config.logical_layers.electric_lines)`.
3. Computes `post_matches` from `_matching_layers(layer_names, config.logical_layers.transformation_posts)`.
4. Checks `len(electric_matches) != 1`. When true: Raises `IgnBdTopoLayerError(f"Expected one unambiguous electric-line layer for '{config.logical_layers.electric_lines.class_label}', found {len(electric_matches)}: {electric_matches}")`.
5. Checks `len(post_matches) != 1`. When true: Raises `IgnBdTopoLayerError(f"Expected one unambiguous transformation-post layer for '{config.logical_layers.transformation_posts.class_label}', found {len(post_matches)}: {post_matches}")`.
6. Checks `electric_matches[0] == post_matches[0]`. When true: Raises `IgnBdTopoLayerError('Electric-line and transformation-post discovery selected the same layer')`.
7. Returns `IgnBdTopoLayerSelection(all_layer_names=layer_names, electric_lines_layer=electric_matches[0], transformation_posts_layer=post_matches[0])`.

**Validation and invariants**

- Rejects or diverts the path when `len(electric_matches) != 1` is true.
- Rejects or diverts the path when `len(post_matches) != 1` is true.
- Rejects or diverts the path when `electric_matches[0] == post_matches[0]` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `IgnBdTopoLayerSelection`, `_matching_layers`, `len`, `list_ign_bdtopo_layers`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_load_cached_extraction`
- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`
- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_electricity`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_ambiguous_electric_line_layers_fail`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_electric_line_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_transformation_post_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_real_layer_names_are_listed_and_discovered`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_electric_line_layers_fail`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_electric_line_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_transformation_post_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_real_layer_names_are_listed_and_discovered`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_discover_department_coverage_layer`

**Signature**

```python
def _discover_department_coverage_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
```

**Purpose**

Discovers department coverage layer according to the exact implementation and guards in this file.

**Inputs**

- `layer_names` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `matches[0]`.

**Algorithm**

1. Computes `matches` from `_matching_layers(layer_names, config.coverage.department_layer)`.
2. Checks `len(matches) != 1`. When true: Raises `IgnBdTopoLayerError(f"Expected one unambiguous department coverage layer for '{config.coverage.department_layer.class_label}', found {len(matches)}: {matches}")`.
3. Returns `matches[0]`.

**Validation and invariants**

- Rejects or diverts the path when `len(matches) != 1` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `_matching_layers`, `len`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_department_coverage`
- `src/landscout/stages/assess_grid_coverage.py` — `_validate_configured_coverage_identity`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_source_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_discover_road_layer`

**Signature**

```python
def _discover_road_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
```

**Purpose**

Discovers road layer according to the exact implementation and guards in this file.

**Inputs**

- `layer_names` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `matches[0]`.

**Algorithm**

1. Computes `matches` from `_matching_layers(layer_names, config.access.road_segments)`.
2. Checks `len(matches) != 1`. When true: Raises `IgnBdTopoLayerError(f"Expected one unambiguous road-segment layer for '{config.access.road_segments.class_label}', found {len(matches)}: {matches}")`.
3. Returns `matches[0]`.

**Validation and invariants**

- Rejects or diverts the path when `len(matches) != 1` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `_matching_layers`, `len`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_safe_relative_path`

**Signature**

```python
def _safe_relative_path(path: Path, root: Path) -> str:
```

**Purpose**

Implements safe relative path according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `path.resolve().relative_to(root.resolve()).as_posix()`.

**Algorithm**

1. Runs guarded operation: Returns `path.resolve().relative_to(root.resolve()).as_posix()`. Handles `(OSError, ValueError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `IgnBdTopoArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoArchiveError`, `path.resolve`, `path.resolve().relative_to`, `path.resolve().relative_to(root.resolve()).as_posix`, `root.resolve`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_resolve_relative_path`

**Signature**

```python
def _resolve_relative_path(root: Path, relative_path: str) -> Path:
```

**Purpose**

Resolves relative path according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relative_path` (`str`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `candidate`.

**Algorithm**

1. Computes `posix_path` from `PurePosixPath(relative_path)`.
2. Computes `windows_path` from `PureWindowsPath(relative_path)`.
3. Checks `not relative_path or posix_path.is_absolute() or windows_path.is_absolute() or bool(windows_path.drive) or ('..' in posix_path.parts)`. When true: Raises `IgnBdTopoArchiveError('Cached extraction metadata contains an unsafe GeoPackage path')`.
4. Computes `candidate` from `root.joinpath(*posix_path.parts)`.
5. Runs guarded operation: Calls `candidate.resolve().relative_to(root.resolve())` for its validation or side effect. Handles `(OSError, ValueError)`.
6. Returns `candidate`.

**Validation and invariants**

- Rejects or diverts the path when `not relative_path or posix_path.is_absolute() or windows_path.is_absolute() or bool(windows_path.drive) or ('..' in posix_path.parts)` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoArchiveError`, `PurePosixPath`, `PureWindowsPath`, `bool`, `candidate.resolve`, `candidate.resolve().relative_to`, `posix_path.is_absolute`, `root.joinpath`, `root.resolve`, `windows_path.is_absolute`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_load_cached_extraction`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_validate_extraction_envelope`
- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_geopackage_integrity`

**Signature**

```python
def _geopackage_integrity(path: Path) -> tuple[int, str]:
```

**Purpose**

Implements geopackage integrity according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[int, str]`. Observed return expression(s): `(size_bytes, digest.hexdigest())`.

**Algorithm**

1. Checks `not path.is_file()`. When true: Raises `IgnBdTopoArchiveError(f'IGN GeoPackage does not exist: {path}')`.
2. Runs guarded operation: Computes `size_bytes` from `path.stat().st_size`. Handles `OSError`.
3. Checks `size_bytes <= 0`. When true: Raises `IgnBdTopoArchiveError(f'IGN GeoPackage is empty: {path}')`.
4. Computes `digest` from `sha256()`.
5. Runs guarded operation: Enters managed context(s) `path.open('rb')` and executes: Iterates `chunk` over `iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b'')`. For each value: Calls `digest.update(chunk)` for its validation or side effect. Handles `OSError`.
6. Returns `(size_bytes, digest.hexdigest())`.

**Validation and invariants**

- Rejects or diverts the path when `not path.is_file()` is true.
- Rejects or diverts the path when `size_bytes <= 0` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoArchiveError`, `digest.hexdigest`, `digest.update`, `iter`, `path.is_file`, `path.open`, `path.stat`, `sha256`, `stream.read`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_load_cached_extraction`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_validate_extraction_envelope`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_verify_unchanged_extraction`
- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_valid_layer_inventory`

**Signature**

```python
def _valid_layer_inventory(value: object) -> bool:
```

**Purpose**

Implements valid layer inventory according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `type(value) is tuple and bool(value) and all((isinstance(name, str) and bool(name) and (name == name.strip()) for name in value)) and (len(set(value)) == len(value))`.

**Algorithm**

1. Returns `type(value) is tuple and bool(value) and all((isinstance(name, str) and bool(name) and (name == name.strip()) for name in value)) and (len(set(value)) == len(value))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `all`, `bool`, `isinstance`, `len`, `name.strip`, `set`, `type`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_validate_extraction_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_extraction_envelope`

**Signature**

```python
def _validate_extraction_envelope(
    extraction: object,
) -> _VerifiedIgnExtraction:
```

**Purpose**

Bind one extraction envelope to its schema-v2 marker and current GPKG.

**Inputs**

- `extraction` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_VerifiedIgnExtraction`. Observed return expression(s): `_VerifiedIgnExtraction(extraction=extraction, metadata=metadata, geopackage_path=discovered_path)`.

**Algorithm**

1. Runs guarded operation: Checks `type(extraction) is not IgnBdTopoExtraction`. When true: Raises `TypeError('IGN extraction must be an exact IgnBdTopoExtraction')`. Checks `type(extraction.archive) is not IgnBdTopoDownload`. When true: Raises `TypeError('IGN extraction archive type is invalid')`. Checks `extraction.spatial_role != SPATIAL_ROLE or extraction.archive.spatial_role != SPATIAL_ROLE`. When true: Raises `ValueError('IGN extraction lineage must be PROXY_GEOMETRY')`. Checks `not isinstance(extraction.archive.sha256, str) or re.fullmatch('[0-9a-f]{64}', extraction.archive.sha256) is None`. When true: Raises `ValueError('IGN archive SHA256 lineage is invalid')`. Executes 22 additional source-ordered statement(s). Handles `IgnBdTopoLayerError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(extraction) is not IgnBdTopoExtraction` is true.
- Rejects or diverts the path when `type(extraction.archive) is not IgnBdTopoDownload` is true.
- Rejects or diverts the path when `extraction.spatial_role != SPATIAL_ROLE or extraction.archive.spatial_role != SPATIAL_ROLE` is true.
- Rejects or diverts the path when `not isinstance(extraction.archive.sha256, str) or re.fullmatch('[0-9a-f]{64}', extraction.archive.sha256) is None` is true.
- Rejects or diverts the path when `type(extraction.geopackage_size_bytes) is not int or extraction.geopackage_size_bytes <= 0` is true.
- Rejects or diverts the path when `not isinstance(extraction.geopackage_sha256, str) or re.fullmatch('[0-9a-f]{64}', extraction.geopackage_sha256) is None` is true.
- Rejects or diverts the path when `not isinstance(extraction.extraction_path, Path) or not isinstance(extraction.geopackage_path, Path)` is true.
- Rejects or diverts the path when `not marker_path.is_file()` is true.
- Rejects or diverts the path when `expected_path.resolve() != discovered_path.resolve() or extraction.geopackage_path.resolve() != discovered_path.resolve() or extraction.geopackage_filename != discovered_path.name` is true.
- Rejects or diverts the path when `metadata.archive_sha256 != extraction.archive.sha256` is true.
- Rejects or diverts the path when `metadata.spatial_role != extraction.spatial_role` is true.
- Rejects or diverts the path when `not _valid_layer_inventory(extraction.all_layer_names)` is true.
- Rejects or diverts the path when `metadata.all_layer_names != extraction.all_layer_names` is true.
- Rejects or diverts the path when `selected_roles != (metadata.electric_lines_layer, metadata.transformation_posts_layer)` is true.
- Rejects or diverts the path when `selected_roles[0] == selected_roles[1] or any((role not in extraction.all_layer_names for role in selected_roles))` is true.
- Rejects or diverts the path when `metadata.geopackage_size_bytes != extraction.geopackage_size_bytes or metadata.geopackage_sha256 != extraction.geopackage_sha256` is true.
- Rejects or diverts the path when `current_size != extraction.geopackage_size_bytes or current_sha != extraction.geopackage_sha256` is true.
- Rejects or diverts the path when `current_layers != extraction.all_layer_names` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`, `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `marker_path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoLayerError`, `TypeError`, `ValueError`, `_ExtractionMetadata.model_validate_json`, `_VerifiedIgnExtraction`, `_geopackage_integrity`, `_resolve_relative_path`, `_valid_layer_inventory`, `any`, `discover_ign_bdtopo_geopackage`, `discovered_path.resolve`, `expected_path.resolve`, `extraction.geopackage_path.resolve`, `isinstance`, `list_ign_bdtopo_layers`, `marker_path.is_file`, `marker_path.read_text`, `re.fullmatch`, `type`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_department_coverage`
- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_electricity`
- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_verify_unchanged_extraction`

**Signature**

```python
def _verify_unchanged_extraction(context: _VerifiedIgnExtraction) -> None:
```

**Purpose**

Implements verify unchanged extraction according to the exact implementation and guards in this file.

**Inputs**

- `context` (`_VerifiedIgnExtraction`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `(size, digest)` from `_geopackage_integrity(context.geopackage_path)`.
2. Checks `size != context.extraction.geopackage_size_bytes or digest != context.extraction.geopackage_sha256 or list_ign_bdtopo_layers(context.geopackage_path) != context.extraction.all_layer_names`. When true: Raises `IgnBdTopoLayerError('IGN physical GeoPackage changed during source layer loading')`.

**Validation and invariants**

- Rejects or diverts the path when `size != context.extraction.geopackage_size_bytes or digest != context.extraction.geopackage_sha256 or list_ign_bdtopo_layers(context.geopackage_path) != context.extraction.all_layer_names` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `_geopackage_integrity`, `list_ign_bdtopo_layers`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_read_verified_layer_frames`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_read_layer_frame`

**Signature**

```python
def _read_layer_frame(geopackage_path: Path, layer_name: str) -> gpd.GeoDataFrame:
```

**Purpose**

Reads and validates layer frame according to the exact implementation and guards in this file.

**Inputs**

- `geopackage_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Checks `not isinstance(layer_name, str) or not layer_name or layer_name != layer_name.strip()`. When true: Raises `IgnBdTopoLayerError('IGN source layer name must be an exact string')`.
2. Runs guarded operation: Computes `frame` from `gpd.read_file(geopackage_path, layer=layer_name, engine='pyogrio')`. Handles `Exception`.
3. Checks `not isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `IgnBdTopoLayerError(f'IGN layer is not spatial: {layer_name}')`.
4. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(layer_name, str) or not layer_name or layer_name != layer_name.strip()` is true.
- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame)` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.read_file`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoLayerError`, `gpd.read_file`, `isinstance`, `layer_name.strip`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_read_verified_layer_frames`
- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_layer`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_read_verified_layer_frames`

**Signature**

```python
def _read_verified_layer_frames(
    context: _VerifiedIgnExtraction,
    layer_names: tuple[str, ...],
) -> tuple[gpd.GeoDataFrame, ...]:
```

**Purpose**

Reads and validates verified layer frames according to the exact implementation and guards in this file.

**Inputs**

- `context` (`_VerifiedIgnExtraction`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer_names` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[gpd.GeoDataFrame, ...]`. Observed return expression(s): `frames`.

**Algorithm**

1. Checks `type(layer_names) is not tuple or not layer_names`. When true: Raises `IgnBdTopoLayerError('IGN verified layer batch must be a non-empty tuple')`.
2. Checks `len(set(layer_names)) != len(layer_names) or any((layer not in context.extraction.all_layer_names for layer in layer_names))`. When true: Raises `IgnBdTopoLayerError('IGN verified layer batch is invalid')`.
3. Computes `frames` from `tuple((_read_layer_frame(context.geopackage_path, layer_name) for layer_name in layer_names))`.
4. Calls `_verify_unchanged_extraction(context)` for its validation or side effect.
5. Returns `frames`.

**Validation and invariants**

- Rejects or diverts the path when `type(layer_names) is not tuple or not layer_names` is true.
- Rejects or diverts the path when `len(set(layer_names)) != len(layer_names) or any((layer not in context.extraction.all_layer_names for layer in layer_names))` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_read_layer_frame`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoLayerError`, `_read_layer_frame`, `_verify_unchanged_extraction`, `any`, `len`, `set`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_department_coverage`
- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_electricity`
- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_layer_summary_contract`

**Signature**

```python
def _validate_layer_summary_contract(summary: object) -> IgnBdTopoLayerSummary:
```

**Purpose**

Validates and rejects malformed layer summary contract according to the exact implementation and guards in this file.

**Inputs**

- `summary` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoLayerSummary`. Observed return expression(s): `summary`.

**Algorithm**

1. Checks `type(summary) is not IgnBdTopoLayerSummary`. When true: Raises `IgnBdTopoLayerError('IGN layer summary type is invalid')`.
2. Iterates `name` over `('feature_count', 'null_geometry_count', 'empty_geometry_count', 'invalid_geometry_count')`. For each value: Computes `value` from `getattr(summary, name)`. Checks `type(value) is not int or value < 0`. When true: Raises `IgnBdTopoLayerError(f'IGN layer summary {name} must be a strict non-negative integer')`.
3. Checks `type(summary.columns) is not tuple or not summary.columns or any((not isinstance(column, str) or not column or column != column.strip() for column in summary.columns)) or (len(set(summary.columns)) != len(summary.columns))`. When true: Raises `IgnBdTopoLayerError('IGN layer summary columns are invalid')`.
4. Checks `type(summary.dtypes) is not tuple or len(summary.dtypes) != len(summary.columns) or any((type(item) is not tuple or len(item) != 2 or any((not isinstance(value, str) or not value for value in item)) for item in summary.dtypes)) or (tuple((column for column, _ in summary.dtypes)) != summary.columns)`. When true: Raises `IgnBdTopoLayerError('IGN layer summary dtypes are invalid')`.
5. Checks `type(summary.geometry_types) is not tuple or any((not isinstance(value, str) or not value or value != value.strip() for value in summary.geometry_types)) or summary.geometry_types != tuple(sorted(set(summary.geometry_types)))`. When true: Raises `IgnBdTopoLayerError('IGN layer summary geometry types are invalid')`.
6. Checks `summary.spatial_role != SPATIAL_ROLE`. When true: Raises `IgnBdTopoLayerError('IGN layer summary spatial role is invalid')`.
7. Checks `any((getattr(summary, name) > summary.feature_count for name in ('null_geometry_count', 'empty_geometry_count', 'invalid_geometry_count')))`. When true: Raises `IgnBdTopoLayerError('IGN layer summary geometry count is impossible')`.
8. Returns `summary`.

**Validation and invariants**

- Rejects or diverts the path when `type(summary) is not IgnBdTopoLayerSummary` is true.
- Rejects or diverts the path when `type(summary.columns) is not tuple or not summary.columns or any((not isinstance(column, str) or not column or column != column.strip() for column in summary.columns)) or (len(set(summary.columns)) != len(summary.columns))` is true.
- Rejects or diverts the path when `type(summary.dtypes) is not tuple or len(summary.dtypes) != len(summary.columns) or any((type(item) is not tuple or len(item) != 2 or any((not isinstance(value, str) or not value for value in item)) for item in summary.dtypes)) or (tuple((column for column, _ in summary.dtypes)) != summary.columns)` is true.
- Rejects or diverts the path when `type(summary.geometry_types) is not tuple or any((not isinstance(value, str) or not value or value != value.strip() for value in summary.geometry_types)) or summary.geometry_types != tuple(sorted(set(summary.geometry_types)))` is true.
- Rejects or diverts the path when `summary.spatial_role != SPATIAL_ROLE` is true.
- Rejects or diverts the path when `any((getattr(summary, name) > summary.feature_count for name in ('null_geometry_count', 'empty_geometry_count', 'invalid_geometry_count')))` is true.
- Rejects or diverts the path when `type(value) is not int or value < 0` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `any`, `column.strip`, `getattr`, `isinstance`, `len`, `set`, `sorted`, `tuple`, `type`, `value.strip`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_compare_layer_summary`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_loaded_layer_from_frame`
- `src/landscout/stages/normalize_access_ign.py` — `_validate_layer_summary`
- `src/landscout/stages/normalize_grid_ign.py` — `_validate_layer_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_compare_layer_summary`

**Signature**

```python
def _compare_layer_summary(
    supplied: object,
    expected: IgnBdTopoLayerSummary,
) -> None:
```

**Purpose**

Compares layer summary according to the exact implementation and guards in this file.

**Inputs**

- `supplied` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`IgnBdTopoLayerSummary`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `validated` from `_validate_layer_summary_contract(supplied)`.
2. Checks `validated != expected`. When true: Raises `IgnBdTopoLayerError('IGN supplied layer summary differs from physical source')`.

**Validation and invariants**

- Rejects or diverts the path when `validated != expected` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `_validate_layer_summary_contract`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_revalidate_ign_bdtopo_electricity_data`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_revalidate_ign_bdtopo_road_data`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_compare_loaded_frame`

**Signature**

```python
def _compare_loaded_frame(
    supplied: object,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
```

**Purpose**

Compares loaded frame according to the exact implementation and guards in this file.

**Inputs**

- `supplied` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Checks `not isinstance(supplied, gpd.GeoDataFrame)`. When true: Raises `TypeError('supplied layer is not a GeoDataFrame')`. Checks `tuple(supplied.columns) != tuple(expected.columns)`. When true: Raises `AssertionError('columns differ')`. Checks `tuple((str(dtype) for dtype in supplied.dtypes)) != tuple((str(dtype) for dtype in expected.dtypes))`. When true: Raises `AssertionError('dtypes differ')`. Checks `type(supplied.index) is not type(expected.index)`. When true: Raises `AssertionError('index type differs')`. Executes 10 additional source-ordered statement(s). Handles `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(supplied, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `tuple(supplied.columns) != tuple(expected.columns)` is true.
- Rejects or diverts the path when `tuple((str(dtype) for dtype in supplied.dtypes)) != tuple((str(dtype) for dtype in expected.dtypes))` is true.
- Rejects or diverts the path when `type(supplied.index) is not type(expected.index)` is true.
- Rejects or diverts the path when `supplied.index.names != expected.index.names or not supplied.index.equals(expected.index)` is true.
- Rejects or diverts the path when `supplied.active_geometry_name != expected.active_geometry_name` is true.
- Rejects or diverts the path when `not supplied_crs.equals(expected_crs)` is true.
- Rejects or diverts the path when `geometry_name is None` is true.
- Rejects or diverts the path when `supplied.geometry.to_wkb(hex=True).tolist() != expected.geometry.to_wkb(hex=True).tolist()` is true.
- Rejects or diverts the path when `supplied.attrs != expected.attrs` is true.

**Exceptions**

- Explicitly raises: `AssertionError`, `IgnBdTopoLayerError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`, `IgnBdTopoLayerError`, `TypeError`, `_validate_lambert93`, `expected.drop`, `expected.geometry.to_wkb`, `expected.geometry.to_wkb(hex=True).tolist`, `isinstance`, `pd.DataFrame`, `pd.testing.assert_frame_equal`, `str`, `supplied.drop`, `supplied.geometry.to_wkb`, `supplied.geometry.to_wkb(hex=True).tolist`, `supplied.index.equals`, `supplied_crs.equals`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_revalidate_ign_bdtopo_department_coverage`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_revalidate_ign_bdtopo_electricity_data`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_revalidate_ign_bdtopo_road_data`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_load_cached_extraction`

**Signature**

```python
def _load_cached_extraction(
    extraction_path: Path,
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoExtraction | None:
```

**Purpose**

Loads cached extraction according to the exact implementation and guards in this file.

**Inputs**

- `extraction_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `download` (`IgnBdTopoDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoExtraction | None`. Observed return expression(s): `None`; `IgnBdTopoExtraction(archive=download, extraction_path=extraction_path, geopackage_path=geopackage_path, geopackage_filename=geopackage_path.name, geopackage_size_bytes=metadata.geopackage_size_bytes, geopackage_sha256=metadata.geopackage_sha256, all_layer_names=selection.all_layer_names, electric_lines_layer=selection.electric_lines_layer, transformation_posts_layer=selection.transformation_posts…`.

**Algorithm**

1. Computes `metadata_path` from `extraction_path / '.landscout-extraction.json'`.
2. Checks `not extraction_path.is_dir() or not metadata_path.is_file()`. When true: Returns `None`.
3. Runs guarded operation: Computes `metadata` from `_ExtractionMetadata.model_validate_json(metadata_path.read_text(encoding='utf-8'))`. Checks `metadata.archive_sha256 != download.sha256 or metadata.spatial_role != SPATIAL_ROLE`. When true: Returns `None`. Computes `geopackage_path` from `_resolve_relative_path(extraction_path, metadata.geopackage_relative_path)`. Computes `discovered_path` from `discover_ign_bdtopo_geopackage(extraction_path)`. Executes 6 additional source-ordered statement(s). Handles `(IgnBdTopoArchiveError, IgnBdTopoLayerError, OSError, ValidationError, ValueError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `metadata_path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoExtraction`, `_ExtractionMetadata.model_validate_json`, `_geopackage_integrity`, `_resolve_relative_path`, `discover_ign_bdtopo_geopackage`, `discover_ign_bdtopo_layers`, `discovered_path.resolve`, `extraction_path.is_dir`, `geopackage_path.resolve`, `metadata_path.is_file`, `metadata_path.read_text`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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

- `src/landscout/sources/ign_bdtopo_fr.py` — `_publish_extraction_directory`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_remove_tree`

**Signature**

```python
def _remove_tree(path: Path) -> None:
```

**Purpose**

Implements remove tree according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `path.is_dir()`. When true: Calls `shutil.rmtree(path)` for its validation or side effect. Otherwise: Checks `path.exists()`. When true: Calls `path.unlink()` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `path.exists`, `path.is_dir`, `path.unlink`, `shutil.rmtree`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_publish_extraction_directory`
- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_publish_extraction_directory`

**Signature**

```python
def _publish_extraction_directory(
    temporary_path: Path, extraction_path: Path
) -> None:
```

**Purpose**

Implements publish extraction directory according to the exact implementation and guards in this file.

**Inputs**

- `temporary_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `extraction_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `backup_path` from `extraction_path.with_name(f'{extraction_path.name}.bak')`.
2. Calls `_remove_tree(backup_path)` for its validation or side effect.
3. Computes `extraction_existed` from `extraction_path.exists()`.
4. Checks `extraction_existed`. When true: Calls `_replace_directory(extraction_path, backup_path)` for its validation or side effect.
5. Runs guarded operation: Calls `_replace_directory(temporary_path, extraction_path)` for its validation or side effect. Handles `OSError`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `IgnBdTopoArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_replace_directory`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoArchiveError`, `_remove_tree`, `_replace_directory`, `extraction_path.exists`, `extraction_path.with_name`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `extract_ign_bdtopo_archive`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `extract_ign_bdtopo_archive`

**Signature**

```python
def extract_ign_bdtopo_archive(
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
    extraction_dir: Path | None = None,
) -> IgnBdTopoExtraction:
```

**Purpose**

Safely extract the package and resolve its required electricity layers.

**Inputs**

- `download` (`IgnBdTopoDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `extraction_dir` (`Path | None`; optional/default `None`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoExtraction`. Observed return expression(s): `cached`; `IgnBdTopoExtraction(archive=download, extraction_path=extraction_path, geopackage_path=published_geopackage, geopackage_filename=published_geopackage.name, geopackage_size_bytes=metadata.geopackage_size_bytes, geopackage_sha256=metadata.geopackage_sha256, all_layer_names=selection.all_layer_names, electric_lines_layer=selection.electric_lines_layer, transformation_posts_layer=selection.transforma…`.

**Algorithm**

1. Computes `integrity` from `validate_ign_bdtopo_archive(download.path, config)`.
2. Checks `integrity.sha256 != download.sha256`. When true: Raises `IgnBdTopoArchiveError('Downloaded IGN archive checksum changed before extraction')`.
3. Computes `extraction_path` from `extraction_dir or download.path.parent / 'x' / download.sha256[:16]`.
4. Checks `extraction_path.exists() and (not extraction_path.is_dir())`. When true: Raises `IgnBdTopoArchiveError(f'IGN extraction target exists and is not a directory: {extraction_path}')`.
5. Computes `cached` from `_load_cached_extraction(extraction_path, download, config)`.
6. Checks `cached is not None`. When true: Returns `cached`.
7. Calls `extraction_path.parent.mkdir(parents=True, exist_ok=True)` for its validation or side effect.
8. Computes `temporary_path` from `extraction_path.with_name(f'{extraction_path.name}.part')`.
9. Calls `_remove_tree(temporary_path)` for its validation or side effect.
10. Calls `temporary_path.mkdir(parents=True)` for its validation or side effect.
11. Runs guarded operation: Enters managed context(s) `py7zr.SevenZipFile(download.path, mode='r')` and executes: Calls `_validate_archive_members(archive)` for its validation or side effect. Calls `archive.extractall(path=temporary_path)` for its validation or side effect. Computes `geopackage_path` from `discover_ign_bdtopo_geopackage(temporary_path)`. Computes `selection` from `discover_ign_bdtopo_layers(geopackage_path, config)`. Computes `relative_path` from `_safe_relative_path(geopackage_path, temporary_path)`. Executes 6 additional source-ordered statement(s). Handles `(ArchiveError, EOFError, OSError, ValueError)`. Finally: Calls `_remove_tree(temporary_path)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `integrity.sha256 != download.sha256` is true.
- Rejects or diverts the path when `extraction_path.exists() and (not extraction_path.is_dir())` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoArchiveError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(temporary_path / '.landscout-extraction.json').write_text`, `_load_cached_extraction`, `extraction_path.parent.mkdir`, `temporary_path.mkdir`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(temporary_path / '.landscout-extraction.json').write_text`, `IgnBdTopoArchiveError`, `IgnBdTopoExtraction`, `_ExtractionMetadata`, `_geopackage_integrity`, `_load_cached_extraction`, `_publish_extraction_directory`, `_remove_tree`, `_resolve_relative_path`, `_safe_relative_path`, `_validate_archive_members`, `archive.extractall`, `discover_ign_bdtopo_geopackage`, `discover_ign_bdtopo_layers`, `extraction_path.exists`, `extraction_path.is_dir`, `extraction_path.parent.mkdir`, `extraction_path.with_name`, `metadata.model_dump_json`, `py7zr.SevenZipFile`, `temporary_path.mkdir`, `validate_ign_bdtopo_archive`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `_extracted_fixture`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_forged_extraction_metadata_never_returns_cache_hit`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_malformed_geopackage_sha_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_malformed_geopackage_size_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_same_size_geopackage_tamper_invalidates_extraction_cache`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_schema_v2_extraction_metadata_binds_physical_geopackage`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_synthetic_archive_extracts_and_discovers_required_layers`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_unsafe_parent_archive_member_is_rejected`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py::test_forged_extraction_metadata_never_returns_cache_hit`
- `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_sha_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_size_is_not_trusted`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department`
- `tests/unit/test_ign_bdtopo_fr.py::test_same_size_geopackage_tamper_invalidates_extraction_cache`
- `tests/unit/test_ign_bdtopo_fr.py::test_schema_v2_extraction_metadata_binds_physical_geopackage`
- `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers`
- `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_lambert93`

**Signature**

```python
def _validate_lambert93(crs_value: Any, layer_name: str) -> CRS:
```

**Purpose**

Validates and rejects malformed lambert93 according to the exact implementation and guards in this file.

**Inputs**

- `crs_value` (`Any`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `crs`.

**Algorithm**

1. Checks `crs_value is None`. When true: Raises `IgnBdTopoLayerError(f'IGN layer has no CRS: {layer_name}')`.
2. Runs guarded operation: Computes `crs` from `CRS.from_user_input(crs_value)`. Handles `Exception`.
3. Checks `not crs.is_projected`. When true: Raises `IgnBdTopoLayerError(f'IGN layer CRS must be projected: {layer_name} ({crs.to_string()})')`.
4. Computes `expected` from `CRS.from_epsg(2154)`.
5. Checks `not crs.equals(expected)`. When true: Raises `IgnBdTopoLayerError(f'IGN layer CRS is not Lambert-93 / EPSG:2154 compatible: {layer_name} ({crs.to_string()})')`.
6. Returns `crs`.

**Validation and invariants**

- Rejects or diverts the path when `crs_value is None` is true.
- Rejects or diverts the path when `not crs.is_projected` is true.
- Rejects or diverts the path when `not crs.equals(expected)` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `CRS.from_user_input`, `IgnBdTopoLayerError`, `crs.equals`, `crs.to_string`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_compare_loaded_frame`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_department_coverage_from_frame`
- `src/landscout/sources/ign_bdtopo_fr.py` — `_loaded_layer_from_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_loaded_layer_from_frame`

**Signature**

```python
def _loaded_layer_from_frame(
    frame: gpd.GeoDataFrame,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
```

**Purpose**

Implements loaded layer from frame according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalLayerName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoLoadedLayer`. Observed return expression(s): `IgnBdTopoLoadedLayer(data=frame, summary=summary)`.

**Algorithm**

1. Runs guarded operation: Computes `geometry_name` from `frame.geometry.name`. Handles `(AttributeError, ValueError)`.
2. Checks `geometry_name not in frame.columns`. When true: Raises `IgnBdTopoLayerError(f'IGN layer geometry column is missing: {layer_name}')`.
3. Computes `crs` from `_validate_lambert93(frame.crs, layer_name)`.
4. Checks `frame.empty`. When true: Raises `IgnBdTopoLayerError(f'IGN layer contains no features: {layer_name}')`.
5. Computes `geometry` from `frame.geometry`.
6. Computes `null_mask` from `geometry.isna()`.
7. Computes `non_null_mask` from `~null_mask`.
8. Computes `empty_mask` from `non_null_mask & geometry.is_empty`.
9. Computes `measurable_mask` from `non_null_mask & ~geometry.is_empty`.
10. Computes `invalid_mask` from `measurable_mask & ~geometry.is_valid`.
11. Computes `geometry_types` from `tuple(sorted((str(value) for value in geometry[non_null_mask].geom_type.dropna().unique())))`.
12. Computes `summary` from `IgnBdTopoLayerSummary(logical_name=logical_name, source_layer_name=layer_name, crs=crs.to_string(), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_ge…`.
13. Calls `_validate_layer_summary_contract(summary)` for its validation or side effect.
14. Returns `IgnBdTopoLoadedLayer(data=frame, summary=summary)`.

**Validation and invariants**

- Rejects or diverts the path when `geometry_name not in frame.columns` is true.
- Rejects or diverts the path when `frame.empty` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `IgnBdTopoLayerSummary`, `IgnBdTopoLoadedLayer`, `_validate_lambert93`, `_validate_layer_summary_contract`, `crs.to_string`, `empty_mask.sum`, `frame.dtypes.items`, `geometry.isna`, `geometry[non_null_mask].geom_type.dropna`, `geometry[non_null_mask].geom_type.dropna().unique`, `int`, `invalid_mask.sum`, `len`, `null_mask.sum`, `sorted`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_electricity`
- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_layer`
- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_layer`

**Signature**

```python
def load_ign_bdtopo_layer(
    geopackage_path: Path,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
```

**Purpose**

Load and validate one selected IGN layer without repairing geometry.

**Inputs**

- `geopackage_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalLayerName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoLoadedLayer`. Observed return expression(s): `_loaded_layer_from_frame(frame, layer_name, logical_name)`.

**Algorithm**

1. Checks `not geopackage_path.is_file()`. When true: Raises `IgnBdTopoLayerError(f'GeoPackage does not exist: {geopackage_path}')`.
2. Checks `not layer_name.strip()`. When true: Raises `IgnBdTopoLayerError('IGN source layer name must not be empty')`.
3. Computes `frame` from `_read_layer_frame(geopackage_path, layer_name)`.
4. Returns `_loaded_layer_from_frame(frame, layer_name, logical_name)`.

**Validation and invariants**

- Rejects or diverts the path when `not geopackage_path.is_file()` is true.
- Rejects or diverts the path when `not layer_name.strip()` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_read_layer_frame`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoLayerError`, `_loaded_layer_from_frame`, `_read_layer_frame`, `geopackage_path.is_file`, `layer_name.strip`.

**Known repository callers**

- `tests/unit/test_ign_bdtopo_fr.py` — `test_geographic_crs_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_invalid_geometry_is_preserved_without_repair`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_layer_loader_retains_crs_counts_and_null_geometries`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_geographic_crs_is_rejected`
- `tests/unit/test_ign_bdtopo_fr.py::test_invalid_geometry_is_preserved_without_repair`
- `tests/unit/test_ign_bdtopo_fr.py::test_layer_loader_retains_crs_counts_and_null_geometries`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validated_layer_source_config`

**Signature**

```python
def _validated_layer_source_config(config: object) -> IgnBdTopoSourceConfig:
```

**Purpose**

Validates and returns canonical layer source config according to the exact implementation and guards in this file.

**Inputs**

- `config` (`object`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoSourceConfig`. Observed return expression(s): `IgnBdTopoSourceConfig.model_validate(config.model_dump(mode='python'))`.

**Algorithm**

1. Runs guarded operation: Checks `type(config) is not IgnBdTopoSourceConfig`. When true: Raises `TypeError('IGN electricity source config type is invalid')`. Returns `IgnBdTopoSourceConfig.model_validate(config.model_dump(mode='python'))`. Handles `(AttributeError, TypeError, ValidationError, ValueError)`.

**Validation and invariants**

- Rejects or diverts the path when `type(config) is not IgnBdTopoSourceConfig` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `IgnBdTopoSourceConfig.model_validate`, `TypeError`, `config.model_dump`, `type`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_electricity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_archive_config_lineage`

**Signature**

```python
def _validate_archive_config_lineage(
    extraction: object,
    config: IgnBdTopoSourceConfig,
) -> None:
```

**Purpose**

Validates and rejects malformed archive config lineage according to the exact implementation and guards in this file.

**Inputs**

- `extraction` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Checks `type(extraction) is not IgnBdTopoExtraction`. When true: Raises `TypeError('IGN electricity extraction type is invalid')`. Computes `archive` from `extraction.archive`. Checks `type(archive) is not IgnBdTopoDownload`. When true: Raises `TypeError('IGN electricity archive type is invalid')`. Checks `type(archive.file_size) is not int or archive.file_size <= 0`. When true: Raises `TypeError('IGN electricity archive size is invalid')`. Executes 5 additional source-ordered statement(s). Handles `IgnBdTopoLayerError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(extraction) is not IgnBdTopoExtraction` is true.
- Rejects or diverts the path when `type(archive) is not IgnBdTopoDownload` is true.
- Rejects or diverts the path when `type(archive.file_size) is not int or archive.file_size <= 0` is true.
- Rejects or diverts the path when `type(archive.official_checksum_validated) is not bool` is true.
- Rejects or diverts the path when `any((actual != expected for actual, expected in expected_values))` is true.
- Rejects or diverts the path when `config.expected_archive_size_bytes is not None and archive.file_size != config.expected_archive_size_bytes` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`, `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `TypeError`, `ValueError`, `_archive_filename`, `any`, `str`, `type`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_electricity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_electricity`

**Signature**

```python
def load_ign_bdtopo_electricity(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Load the two electricity layers reproduced from the source config.

**Inputs**

- `extraction` (`IgnBdTopoExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoElectricityData`. Observed return expression(s): `IgnBdTopoElectricityData(extraction=extraction, electric_lines=electric_lines.data, transformation_posts=transformation_posts.data, electric_lines_summary=electric_lines.summary, transformation_posts_summary=transformation_posts.summary)`.

**Algorithm**

1. Computes `validated_config` from `_validated_layer_source_config(config)`.
2. Calls `_validate_archive_config_lineage(extraction, validated_config)` for its validation or side effect.
3. Computes `context` from `_validate_extraction_envelope(extraction)`.
4. Computes `configured_selection` from `discover_ign_bdtopo_layers(context.geopackage_path, validated_config)`.
5. Checks `configured_selection.all_layer_names != extraction.all_layer_names or configured_selection.electric_lines_layer != extraction.electric_lines_layer or configured_selection.transformation_posts_layer != extraction.transformation_posts_layer`. When true: Raises `IgnBdTopoLayerError('IGN electricity roles differ from the configured physical layers')`.
6. Computes `(line_frame, post_frame)` from `_read_verified_layer_frames(context, (configured_selection.electric_lines_layer, configured_selection.transformation_posts_layer))`.
7. Computes `electric_lines` from `_loaded_layer_from_frame(line_frame, configured_selection.electric_lines_layer, 'electric_lines')`.
8. Computes `transformation_posts` from `_loaded_layer_from_frame(post_frame, configured_selection.transformation_posts_layer, 'transformation_posts')`.
9. Returns `IgnBdTopoElectricityData(extraction=extraction, electric_lines=electric_lines.data, transformation_posts=transformation_posts.data, electric_lines_summary=electric_lines.summary, transformation_posts_summary=transformation_posts.summary)`.

**Validation and invariants**

- Rejects or diverts the path when `configured_selection.all_layer_names != extraction.all_layer_names or configured_selection.electric_lines_layer != extraction.electric_lines_layer or configured_selection.transformation_posts_layer != extraction.transformation_posts_layer` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_read_verified_layer_frames`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoElectricityData`, `IgnBdTopoLayerError`, `_loaded_layer_from_frame`, `_read_verified_layer_frames`, `_validate_archive_config_lineage`, `_validate_extraction_envelope`, `_validated_layer_source_config`, `discover_ign_bdtopo_layers`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_revalidate_ign_bdtopo_electricity_data`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_road_layer_does_not_change_electricity_loading_or_cache_shape`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts`
- `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_roads`

**Signature**

```python
def load_ign_bdtopo_roads(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
```

**Purpose**

Load the configured factual road layer without filtering or repair.

**Inputs**

- `extraction` (`IgnBdTopoExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoRoadData`. Observed return expression(s): `IgnBdTopoRoadData(extraction=extraction, road_segments=loaded.data, road_segments_summary=loaded.summary)`.

**Algorithm**

1. Computes `context` from `_validate_extraction_envelope(extraction)`.
2. Checks `config.department_code != extraction.archive.department_code`. When true: Raises `IgnBdTopoLayerError('IGN road config department does not match archive lineage')`.
3. Computes `layer_name` from `_discover_road_layer(extraction.all_layer_names, config)`.
4. Checks `layer_name in {extraction.electric_lines_layer, extraction.transformation_posts_layer}`. When true: Raises `IgnBdTopoLayerError('Road, electric-line, and transformation-post roles must use distinct layers')`.
5. Computes `(road_frame,)` from `_read_verified_layer_frames(context, (layer_name,))`.
6. Computes `loaded` from `_loaded_layer_from_frame(road_frame, layer_name, 'road_segments')`.
7. Returns `IgnBdTopoRoadData(extraction=extraction, road_segments=loaded.data, road_segments_summary=loaded.summary)`.

**Validation and invariants**

- Rejects or diverts the path when `config.department_code != extraction.archive.department_code` is true.
- Rejects or diverts the path when `layer_name in {extraction.electric_lines_layer, extraction.transformation_posts_layer}` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_read_verified_layer_frames`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoLayerError`, `IgnBdTopoRoadData`, `_discover_road_layer`, `_loaded_layer_from_frame`, `_read_verified_layer_frames`, `_validate_extraction_envelope`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_revalidate_ign_bdtopo_road_data`
- `tests/unit/test_normalize_access_ign.py` — `_with_alternate_road_layer`
- `tests/unit/test_normalize_access_ign.py` — `test_road_normalization_reproduces_configured_logical_layer`

**Tests**

- `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_department_coverage_from_frame`

**Signature**

```python
def _department_coverage_from_frame(
    extraction: IgnBdTopoExtraction,
    frame: gpd.GeoDataFrame,
    layer_name: str,
    department_field: str,
) -> IgnBdTopoDepartmentCoverage:
```

**Purpose**

Implements department coverage from frame according to the exact implementation and guards in this file.

**Inputs**

- `extraction` (`IgnBdTopoExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `layer_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `department_field` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoDepartmentCoverage`. Observed return expression(s): `IgnBdTopoDepartmentCoverage(extraction=extraction, coverage=selected, summary=summary, source_provider=archive.provider, source_product=archive.product, source_department_code=archive.department_code, source_edition=archive.edition, source_product_version=archive.product_version, source_archive_sha256=archive.sha256, source_layer=layer_name)`.

**Algorithm**

1. Computes `archive` from `extraction.archive`.
2. Runs guarded operation: Computes `geometry_name` from `frame.geometry.name`. Handles `(AttributeError, ValueError)`.
3. Checks `geometry_name not in frame.columns`. When true: Raises `IgnBdTopoLayerError(f'IGN department coverage geometry column is missing: {layer_name}')`.
4. Computes `crs` from `_validate_lambert93(frame.crs, layer_name)`.
5. Checks `frame.empty`. When true: Raises `IgnBdTopoLayerError(f'IGN department coverage layer contains no features: {layer_name}')`.
6. Computes `geometry` from `frame.geometry`.
7. Computes `null_mask` from `geometry.isna()`.
8. Computes `non_null_mask` from `~null_mask`.
9. Computes `empty_mask` from `non_null_mask & geometry.is_empty`.
10. Computes `measurable_mask` from `non_null_mask & ~geometry.is_empty`.
11. Computes `invalid_mask` from `measurable_mask & ~geometry.is_valid`.
12. Computes `geometry_types` from `tuple(sorted((str(value) for value in geometry[non_null_mask].geom_type.dropna().unique())))`.
13. Checks `department_field not in frame.columns`. When true: Raises `IgnBdTopoLayerError(f'Configured department identity field is missing from IGN coverage layer: {department_field}')`.
14. Computes `selected_mask` from `frame[department_field].eq(archive.department_code)`.
15. Computes `selected_count` from `int(selected_mask.sum())`.
16. Checks `selected_count != 1`. When true: Raises `IgnBdTopoLayerError(f'Expected exactly one authoritative department coverage feature for {archive.department_code}, found {selected_count}')`.
17. Computes `selected` from `frame.loc[selected_mask].reset_index(drop=True).copy()`.
18. Computes `selected_geometry` from `selected.geometry`.
19. Checks `selected_geometry.isna().any()`. When true: Raises `IgnBdTopoLayerError('Selected department coverage geometry is null')`.
20. Checks `selected_geometry.is_empty.any()`. When true: Raises `IgnBdTopoLayerError('Selected department coverage geometry is empty')`.
21. Checks `not selected_geometry.is_valid.all()`. When true: Raises `IgnBdTopoLayerError('Selected department coverage geometry is invalid')`.
22. Computes `selected_types` from `set(selected_geometry.geom_type.dropna())`.
23. Checks `not selected_types <= {'Polygon', 'MultiPolygon'}`. When true: Raises `IgnBdTopoLayerError('Selected department coverage geometry must be Polygon or MultiPolygon')`.
24. Computes `lineage` from `{'source_provider': archive.provider, 'source_product': archive.product, 'source_department_code': archive.department_code, 'source_edition': archive.edition, 'source_product_version': archive.product_version, 'source_archive_sha256': archive.sha256, 'source_layer': layer_name, 'spatial_role': COVERAGE_SPATIAL_ROLE}`.
25. Computes `collisions` from `set(lineage) & set(selected.columns)`.
26. Checks `collisions`. When true: Raises `IgnBdTopoLayerError('IGN department coverage attributes collide with lineage columns: ' + ', '.join(sorted(collisions)))`.
27. Iterates `(column, value)` over `lineage.items()`. For each value: Computes `selected[column]` from `value`.
28. Computes `summary` from `IgnBdTopoCoverageLayerSummary(source_layer_name=layer_name, crs=crs.to_string(), source_feature_count=len(frame), selected_feature_count=selected_count, columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int…`.
29. Returns `IgnBdTopoDepartmentCoverage(extraction=extraction, coverage=selected, summary=summary, source_provider=archive.provider, source_product=archive.product, source_department_code=archive.department_code, source_edition=archive.edition, source_product_version=archive.product_version, source_archive_sha256=archive.sha256, source_layer=layer_name)`.

**Validation and invariants**

- Rejects or diverts the path when `geometry_name not in frame.columns` is true.
- Rejects or diverts the path when `frame.empty` is true.
- Rejects or diverts the path when `department_field not in frame.columns` is true.
- Rejects or diverts the path when `selected_count != 1` is true.
- Rejects or diverts the path when `selected_geometry.isna().any()` is true.
- Rejects or diverts the path when `selected_geometry.is_empty.any()` is true.
- Rejects or diverts the path when `not selected_geometry.is_valid.all()` is true.
- Rejects or diverts the path when `not selected_types <= {'Polygon', 'MultiPolygon'}` is true.
- Rejects or diverts the path when `collisions` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.loc[selected_mask].reset_index(drop=True).copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `', '.join`, `IgnBdTopoCoverageLayerSummary`, `IgnBdTopoDepartmentCoverage`, `IgnBdTopoLayerError`, `_validate_lambert93`, `crs.to_string`, `empty_mask.sum`, `frame.dtypes.items`, `frame.loc[selected_mask].reset_index`, `frame.loc[selected_mask].reset_index(drop=True).copy`, `frame[department_field].eq`, `geometry.isna`, `geometry[non_null_mask].geom_type.dropna`, `geometry[non_null_mask].geom_type.dropna().unique`, `int`, `invalid_mask.sum`, `len`, `lineage.items`, `null_mask.sum`, `selected_geometry.geom_type.dropna`, `selected_geometry.is_empty.any`, `selected_geometry.is_valid.all`, `selected_geometry.isna`, `selected_geometry.isna().any`, `selected_mask.sum`, `set`, `sorted`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `load_ign_bdtopo_department_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_department_coverage`

**Signature**

```python
def load_ign_bdtopo_department_coverage(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
```

**Purpose**

Load the one authoritative configured department coverage feature.

**Inputs**

- `extraction` (`IgnBdTopoExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoDepartmentCoverage`. Observed return expression(s): `_department_coverage_from_frame(extraction, frame, layer_name, config.coverage.department_layer.department_code_field)`.

**Algorithm**

1. Computes `context` from `_validate_extraction_envelope(extraction)`.
2. Computes `archive` from `extraction.archive`.
3. Checks `config.department_code != archive.department_code`. When true: Raises `IgnBdTopoLayerError('IGN coverage config department does not match archive lineage')`.
4. Computes `layer_name` from `_discover_department_coverage_layer(extraction.all_layer_names, config)`.
5. Computes `(frame,)` from `_read_verified_layer_frames(context, (layer_name,))`.
6. Returns `_department_coverage_from_frame(extraction, frame, layer_name, config.coverage.department_layer.department_code_field)`.

**Validation and invariants**

- Rejects or diverts the path when `config.department_code != archive.department_code` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_read_verified_layer_frames`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoLayerError`, `_department_coverage_from_frame`, `_discover_department_coverage_layer`, `_read_verified_layer_frames`, `_validate_extraction_envelope`.

**Known repository callers**

- `src/landscout/sources/ign_bdtopo_fr.py` — `_revalidate_ign_bdtopo_department_coverage`
- `src/landscout/stages/assess_grid_coverage.py` — `assess_grid_coverage`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py` — `test_missing_department_coverage_layer_fails`

**Tests**

- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field`
- `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature`
- `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering`
- `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_revalidate_ign_bdtopo_electricity_data`

**Signature**

```python
def _revalidate_ign_bdtopo_electricity_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Fresh-read and exact-compare one supplied electricity source bundle.

**Inputs**

- `source` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoElectricityData`. Observed return expression(s): `fresh`.

**Algorithm**

1. Runs guarded operation: Checks `type(source) is not IgnBdTopoElectricityData`. When true: Raises `TypeError('IGN electricity source type is invalid')`. Checks `type(config) is not IgnBdTopoSourceConfig`. When true: Raises `TypeError('IGN electricity source config type is invalid')`. Computes `fresh` from `load_ign_bdtopo_electricity(source.extraction, config)`. Calls `_compare_loaded_frame(source.electric_lines, fresh.electric_lines, 'electric lines')` for its validation or side effect. Executes 5 additional source-ordered statement(s). Handles `IgnBdTopoLayerError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(source) is not IgnBdTopoElectricityData` is true.
- Rejects or diverts the path when `type(config) is not IgnBdTopoSourceConfig` is true.
- Rejects or diverts the path when `source.spatial_role != SPATIAL_ROLE` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`, `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_bdtopo_electricity`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoLayerError`, `TypeError`, `ValueError`, `_compare_layer_summary`, `_compare_loaded_frame`, `load_ign_bdtopo_electricity`, `type`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `normalize_ign_electricity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_revalidate_ign_bdtopo_road_data`

**Signature**

```python
def _revalidate_ign_bdtopo_road_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
```

**Purpose**

Fresh-read and exact-compare one supplied road source bundle.

**Inputs**

- `source` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoRoadData`. Observed return expression(s): `fresh`.

**Algorithm**

1. Runs guarded operation: Checks `type(source) is not IgnBdTopoRoadData`. When true: Raises `TypeError('IGN road source type is invalid')`. Checks `type(config) is not IgnBdTopoSourceConfig`. When true: Raises `TypeError('IGN road source config type is invalid')`. Computes `fresh` from `load_ign_bdtopo_roads(source.extraction, config)`. Calls `_compare_loaded_frame(source.road_segments, fresh.road_segments, 'road segments')` for its validation or side effect. Executes 2 additional source-ordered statement(s). Handles `IgnBdTopoLayerError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(source) is not IgnBdTopoRoadData` is true.
- Rejects or diverts the path when `type(config) is not IgnBdTopoSourceConfig` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_bdtopo_roads`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoLayerError`, `TypeError`, `_compare_layer_summary`, `_compare_loaded_frame`, `load_ign_bdtopo_roads`, `type`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_normalize_ign_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_coverage_summary_contract`

**Signature**

```python
def _validate_coverage_summary_contract(
    summary: object,
) -> IgnBdTopoCoverageLayerSummary:
```

**Purpose**

Validates and rejects malformed coverage summary contract according to the exact implementation and guards in this file.

**Inputs**

- `summary` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoCoverageLayerSummary`. Observed return expression(s): `summary`.

**Algorithm**

1. Checks `type(summary) is not IgnBdTopoCoverageLayerSummary`. When true: Raises `IgnBdTopoLayerError('IGN coverage summary type is invalid')`.
2. Iterates `name` over `('source_feature_count', 'selected_feature_count', 'null_geometry_count', 'empty_geometry_count', 'invalid_geometry_count')`. For each value: Computes `value` from `getattr(summary, name)`. Checks `type(value) is not int or value < 0`. When true: Raises `IgnBdTopoLayerError(f'IGN coverage summary {name} must be a strict non-negative integer')`.
3. Checks `summary.selected_feature_count > summary.source_feature_count`. When true: Raises `IgnBdTopoLayerError('IGN coverage summary counts are inconsistent')`.
4. Checks `type(summary.columns) is not tuple or not summary.columns or any((not isinstance(value, str) or not value or value != value.strip() for value in summary.columns)) or (len(set(summary.columns)) != len(summary.columns))`. When true: Raises `IgnBdTopoLayerError('IGN coverage summary columns are invalid')`.
5. Checks `type(summary.dtypes) is not tuple or len(summary.dtypes) != len(summary.columns) or any((type(item) is not tuple or len(item) != 2 or any((not isinstance(value, str) or not value for value in item)) for item in summary.dtypes)) or (tuple((name for name, _ in summary.dtypes)) != summary.columns)`. When true: Raises `IgnBdTopoLayerError('IGN coverage summary dtypes are invalid')`.
6. Checks `type(summary.geometry_types) is not tuple or summary.geometry_types != tuple(sorted(set(summary.geometry_types))) or any((not isinstance(value, str) or not value for value in summary.geometry_types))`. When true: Raises `IgnBdTopoLayerError('IGN coverage summary geometry types are invalid')`.
7. Checks `summary.spatial_role != COVERAGE_SPATIAL_ROLE`. When true: Raises `IgnBdTopoLayerError('IGN coverage summary spatial role is invalid')`.
8. Returns `summary`.

**Validation and invariants**

- Rejects or diverts the path when `type(summary) is not IgnBdTopoCoverageLayerSummary` is true.
- Rejects or diverts the path when `summary.selected_feature_count > summary.source_feature_count` is true.
- Rejects or diverts the path when `type(summary.columns) is not tuple or not summary.columns or any((not isinstance(value, str) or not value or value != value.strip() for value in summary.columns)) or (len(set(summary.columns)) != len(summary.columns))` is true.
- Rejects or diverts the path when `type(summary.dtypes) is not tuple or len(summary.dtypes) != len(summary.columns) or any((type(item) is not tuple or len(item) != 2 or any((not isinstance(value, str) or not value for value in item)) for item in summary.dtypes)) or (tuple((name for name, _ in summary.dtypes)) != summary.columns)` is true.
- Rejects or diverts the path when `type(summary.geometry_types) is not tuple or summary.geometry_types != tuple(sorted(set(summary.geometry_types))) or any((not isinstance(value, str) or not value for value in summary.geometry_types))` is true.
- Rejects or diverts the path when `summary.spatial_role != COVERAGE_SPATIAL_ROLE` is true.
- Rejects or diverts the path when `type(value) is not int or value < 0` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoLayerError`, `any`, `getattr`, `isinstance`, `len`, `set`, `sorted`, `tuple`, `type`, `value.strip`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_revalidate_ign_bdtopo_department_coverage`

**Signature**

```python
def _revalidate_ign_bdtopo_department_coverage(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
```

**Purpose**

Fresh-read and exact-compare selected coverage with its physical layer.

**Inputs**

- `source` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnBdTopoDepartmentCoverage`. Observed return expression(s): `fresh`.

**Algorithm**

1. Runs guarded operation: Checks `type(source) is not IgnBdTopoDepartmentCoverage`. When true: Raises `TypeError('IGN department coverage type is invalid')`. Checks `type(config) is not IgnBdTopoSourceConfig`. When true: Raises `TypeError('IGN coverage source config type is invalid')`. Computes `fresh` from `load_ign_bdtopo_department_coverage(source.extraction, config)`. Calls `_compare_loaded_frame(source.coverage, fresh.coverage, 'department coverage')` for its validation or side effect. Executes 4 additional source-ordered statement(s). Handles `IgnBdTopoLayerError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(source) is not IgnBdTopoDepartmentCoverage` is true.
- Rejects or diverts the path when `type(config) is not IgnBdTopoSourceConfig` is true.
- Rejects or diverts the path when `source.summary != fresh.summary` is true.
- Rejects or diverts the path when `any((getattr(source, name) != getattr(fresh, name) for name in scalar_names))` is true.

**Exceptions**

- Explicitly raises: `IgnBdTopoLayerError`, `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_bdtopo_department_coverage`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnBdTopoLayerError`, `TypeError`, `ValueError`, `_compare_loaded_frame`, `any`, `getattr`, `load_ign_bdtopo_department_coverage`, `type`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `7z` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `EPSG:2154` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `GPKG` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `PROXY_GEOMETRY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `SOURCE_COVERAGE_BOUNDARY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `electric_lines` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `md5` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_segments` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sha256` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `transformation_posts` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `grid` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
