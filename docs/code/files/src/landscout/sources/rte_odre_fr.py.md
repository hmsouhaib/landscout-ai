# `src/landscout/sources/rte_odre_fr.py`

## File identity

- Repository path: `src/landscout/sources/rte_odre_fr.py`
- File type: Python source
- Primary responsibility: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.
- Layer / domain: `source adapter` / `grid`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `b7d422d29f7155399a8dac87422811cc87b2c856f7432ef78fbbe68bfff1edb3`

## 1. Purpose

Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

## 2. Position in LandScout architecture

This file is a `source adapter` artifact in the `grid` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `import json` — required by the implementation paths and symbols documented below.
- `import sys` — required by the implementation paths and symbols documented below.
- `from dataclasses import asdict, dataclass, replace` — required by the implementation paths and symbols documented below.
- `from datetime import UTC, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from shutil import copy2, copyfileobj` — required by the implementation paths and symbols documented below.
- `from typing import Annotated, Any, Literal` — required by the implementation paths and symbols documented below.
- `from urllib.error import HTTPError, URLError` — required by the implementation paths and symbols documented below.
- `from urllib.parse import quote, urlsplit` — required by the implementation paths and symbols documented below.

### Third-party

- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import ( BaseModel, ConfigDict, Field, HttpUrl, StringConstraints, ValidationError, field_validator, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.safe_http import open_safe_https` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `DEFAULT_CONFIG_PATH` | `Path("configs/sources/rte_odre_fr.yaml")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DEFAULT_CACHE_DIR` | `Path("data/cache/rte_odre")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DOWNLOAD_CHUNK_SIZE` | `1024 * 1024` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LOGICAL_DATASET_NAMES` | `("sites", "overhead_lines", "underground_lines")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `COORDINATE_GEOMETRY_TYPES` | `frozenset( { "Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `GEOJSON_GEOMETRY_TYPES` | `COORDINATE_GEOMETRY_TYPES &#124; {"GeometryCollection"}` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `RteDatasetConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `dataset_id` | `DatasetIdentifier` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `preferred_format` | `ExportFormat` | `required` | `ExportFormat` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `RteDatasetsConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `sites` | `RteDatasetConfig` | `required` | `RteDatasetConfig` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `overhead_lines` | `RteDatasetConfig` | `required` | `RteDatasetConfig` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `underground_lines` | `RteDatasetConfig` | `required` | `RteDatasetConfig` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `RteOdreApiConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `base_url` | `HttpUrl` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |

**Validators and methods:**

- `_official_api_origin` — `def _official_api_origin(cls, value: HttpUrl) -> HttpUrl:`; decorators `field_validator('base_url'), classmethod`. The complete method algorithm appears in the function/method section.

### `RteOdreCacheConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `max_age_hours` | `float` | `Field(ge=0, allow_inf_nan=False)` | `float` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `RteOdreSourceConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `provider` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `portal` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `api` | `RteOdreApiConfig` | `required` | `RteOdreApiConfig` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `datasets` | `RteDatasetsConfig` | `required` | `RteDatasetsConfig` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache` | `RteOdreCacheConfig` | `required` | `RteOdreCacheConfig` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `RteOdreDownloadError`

**Purpose:** Raised when RTE/ODRE metadata or exports cannot be retrieved safely.

**Inheritance:** `RuntimeError`.

**Model form and mutability:** class inheriting from `RuntimeError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `RteOdreDatasetMetadata`

**Purpose:** Represents strict metadata used to reconstruct or validate a byte-bound cache/source object.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `dataset_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `title` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `publisher` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `modified` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `data_processed` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `metadata_processed` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `license` | `str | None` | `required` | `str | None` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `records_count` | `int | None` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `geometry_precision_status` | `GeometryPrecisionStatus` | `required` | Categorical factual, technical, policy, or diagnostic status; the owning constants/validators define the closed vocabulary. |

**Validators and methods:**

- `__post_init__` — `def __post_init__(self) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.

### `RteOdreExportSummary`

**Purpose:** Carries deterministic factual counts, schema, or geometry summary data used to validate a frame or source.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `feature_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `null_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `non_null_geometry_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `geometry_types` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__post_init__` — `def __post_init__(self) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.

### `RteOdreDownload`

**Purpose:** Carries an immutable downloaded-source lineage envelope including byte identity and cache status.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `logical_name` | `LogicalDatasetName` | `required` | `LogicalDatasetName` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `dataset_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `provider` | `str` | `required` | `str` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `portal` | `str` | `required` | `str` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |
| `export_format` | `ExportFormat` | `required` | `ExportFormat` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `download_timestamp` | `str` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `filename` | `str` | `required` | `str` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `file_size` | `int` | `required` | Exact physical byte count used with SHA256 to validate cached or downloaded content. |
| `sha256` | `str` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `path` | `Path` | `required` | `Path` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cache_hit` | `bool` | `required` | Boolean recording whether verified local bytes were reused instead of acquired during this call. |
| `dataset_metadata` | `RteOdreDatasetMetadata` | `required` | `RteOdreDatasetMetadata` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `export_summary` | `RteOdreExportSummary` | `required` | `RteOdreExportSummary` state used by `src/landscout/sources/rte_odre_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `RteOdreApiConfig._official_api_origin`

**Signature**

```python
def _official_api_origin(cls, value: HttpUrl) -> HttpUrl:
```

**Purpose**

Implements official api origin according to the exact implementation and guards in this file.

**Inputs**

- `cls` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`HttpUrl`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `HttpUrl`. Observed return expression(s): `value`.

**Algorithm**

1. Computes `parsed` from `urlsplit(str(value))`.
2. Checks `parsed.scheme != 'https' or parsed.hostname != 'odre.opendatasoft.com' or parsed.port not in {None, 443} or (parsed.username is not None) or (parsed.password is not None) or (parsed.path.rstrip('/') != '/api/explore/v2.1') or parsed.query or parsed.fragment`. When true: Raises `ValueError('RTE/ODRE API must use the exact official HTTPS origin')`.
3. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `parsed.scheme != 'https' or parsed.hostname != 'odre.opendatasoft.com' or parsed.port not in {None, 443} or (parsed.username is not None) or (parsed.password is not None) or (parsed.path.rstrip('/') != '/api/explore/v2.1') or parsed.query or parsed.fragment` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `field_validator`, `parsed.path.rstrip`, `str`, `urlsplit`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `RteOdreDatasetMetadata.__post_init__`

**Signature**

```python
def __post_init__(self) -> None:
```

**Purpose**

Implements post init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `self.records_count is not None and (not isinstance(self.records_count, int) or isinstance(self.records_count, bool) or self.records_count < 0)`. When true: Raises `ValueError('records_count must be a non-negative integer or None')`.

**Validation and invariants**

- Rejects or diverts the path when `self.records_count is not None and (not isinstance(self.records_count, int) or isinstance(self.records_count, bool) or self.records_count < 0)` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `isinstance`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `RteOdreExportSummary.__post_init__`

**Signature**

```python
def __post_init__(self) -> None:
```

**Purpose**

Implements post init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `counts` from `{'feature_count': self.feature_count, 'null_geometry_count': self.null_geometry_count, 'non_null_geometry_count': self.non_null_geometry_count}`.
2. Iterates `(name, value)` over `counts.items()`. For each value: Checks `not isinstance(value, int) or isinstance(value, bool) or value < 0`. When true: Raises `ValueError(f'{name} must be a non-negative integer')`.
3. Checks `self.null_geometry_count + self.non_null_geometry_count != self.feature_count`. When true: Raises `ValueError('Geometry counts must add up to feature_count')`.
4. Checks `not isinstance(self.geometry_types, tuple) or any((not isinstance(value, str) or not value for value in self.geometry_types))`. When true: Raises `TypeError('geometry_types must be a tuple of non-empty strings')`.

**Validation and invariants**

- Rejects or diverts the path when `self.null_geometry_count + self.non_null_geometry_count != self.feature_count` is true.
- Rejects or diverts the path when `not isinstance(self.geometry_types, tuple) or any((not isinstance(value, str) or not value for value in self.geometry_types))` is true.
- Rejects or diverts the path when `not isinstance(value, int) or isinstance(value, bool) or value < 0` is true.

**Exceptions**

- Explicitly raises: `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `TypeError`, `ValueError`, `any`, `counts.items`, `isinstance`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_rte_odre_source_config`

**Signature**

```python
def load_rte_odre_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> RteOdreSourceConfig:
```

**Purpose**

Loads rte odre source config according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; optional/default `DEFAULT_CONFIG_PATH`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RteOdreSourceConfig`. Observed return expression(s): `RteOdreSourceConfig.model_validate(content)`.

**Algorithm**

1. Enters managed context(s) `path.open(encoding='utf-8')` and executes: Computes `content` from `yaml.safe_load(stream)`.
2. Checks `not isinstance(content, dict)`. When true: Raises `TypeError(f'Expected a YAML mapping in {path}')`.
3. Returns `RteOdreSourceConfig.model_validate(content)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(content, dict)` is true.

**Exceptions**

- Explicitly raises: `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreSourceConfig.model_validate`, `TypeError`, `isinstance`, `path.open`, `yaml.safe_load`.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `source_config`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validated_source_config`

**Signature**

```python
def _validated_source_config(config: object) -> RteOdreSourceConfig:
```

**Purpose**

Validates and returns canonical source config according to the exact implementation and guards in this file.

**Inputs**

- `config` (`object`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RteOdreSourceConfig`. Observed return expression(s): `RteOdreSourceConfig.model_validate(config.model_dump(mode='python'))`.

**Algorithm**

1. Runs guarded operation: Checks `type(config) is not RteOdreSourceConfig`. When true: Raises `TypeError('RTE/ODRE source config type is invalid')`. Returns `RteOdreSourceConfig.model_validate(config.model_dump(mode='python'))`. Handles `(AttributeError, TypeError, ValidationError, ValueError)`.

**Validation and invariants**

- Rejects or diverts the path when `type(config) is not RteOdreSourceConfig` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `RteOdreSourceConfig.model_validate`, `TypeError`, `config.model_dump`, `type`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `build_rte_odre_export_url`
- `src/landscout/sources/rte_odre_fr.py` — `build_rte_odre_metadata_url`
- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`
- `src/landscout/sources/rte_odre_fr.py` — `fetch_rte_odre_dataset_metadata`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_get_dataset_config`

**Signature**

```python
def _get_dataset_config(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> RteDatasetConfig:
```

**Purpose**

Implements get dataset config according to the exact implementation and guards in this file.

**Inputs**

- `config` (`RteOdreSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalDatasetName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RteDatasetConfig`. Observed return expression(s): `getattr(config.datasets, logical_name)`.

**Algorithm**

1. Checks `logical_name not in LOGICAL_DATASET_NAMES`. When true: Raises `ValueError(f'Unsupported RTE/ODRE logical dataset: {logical_name}')`.
2. Returns `getattr(config.datasets, logical_name)`.

**Validation and invariants**

- Rejects or diverts the path when `logical_name not in LOGICAL_DATASET_NAMES` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `getattr`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `_dataset_api_url`
- `src/landscout/sources/rte_odre_fr.py` — `_load_cached_download`
- `src/landscout/sources/rte_odre_fr.py` — `build_rte_odre_export_url`
- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`
- `src/landscout/sources/rte_odre_fr.py` — `fetch_rte_odre_dataset_metadata`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_dataset_api_url`

**Signature**

```python
def _dataset_api_url(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    suffix: str,
) -> str:
```

**Purpose**

Implements dataset api url according to the exact implementation and guards in this file.

**Inputs**

- `config` (`RteOdreSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalDatasetName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `suffix` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `f"{str(config.api.base_url).rstrip('/')}/catalog/datasets/{encoded_dataset_id}{suffix}"`.

**Algorithm**

1. Computes `dataset` from `_get_dataset_config(config, logical_name)`.
2. Computes `encoded_dataset_id` from `quote(dataset.dataset_id, safe='')`.
3. Returns `f"{str(config.api.base_url).rstrip('/')}/catalog/datasets/{encoded_dataset_id}{suffix}"`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_get_dataset_config`, `quote`, `str`, `str(config.api.base_url).rstrip`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `build_rte_odre_export_url`
- `src/landscout/sources/rte_odre_fr.py` — `build_rte_odre_metadata_url`
- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`
- `src/landscout/sources/rte_odre_fr.py` — `fetch_rte_odre_dataset_metadata`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `build_rte_odre_metadata_url`

**Signature**

```python
def build_rte_odre_metadata_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
```

**Purpose**

Builds rte odre metadata url according to the exact implementation and guards in this file.

**Inputs**

- `config` (`RteOdreSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalDatasetName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_dataset_api_url(validated_config, logical_name, '')`.

**Algorithm**

1. Computes `validated_config` from `_validated_source_config(config)`.
2. Returns `_dataset_api_url(validated_config, logical_name, '')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_dataset_api_url`, `_validated_source_config`.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `test_build_metadata_url`
- `tests/unit/test_rte_odre_fr.py` — `test_failed_refresh_preserves_previous_valid_cache`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_build_metadata_url`
- `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `build_rte_odre_export_url`

**Signature**

```python
def build_rte_odre_export_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
```

**Purpose**

Builds rte odre export url according to the exact implementation and guards in this file.

**Inputs**

- `config` (`RteOdreSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalDatasetName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_dataset_api_url(validated_config, logical_name, f'/exports/{export_format}')`.

**Algorithm**

1. Computes `validated_config` from `_validated_source_config(config)`.
2. Computes `dataset` from `_get_dataset_config(validated_config, logical_name)`.
3. Computes `export_format` from `quote(dataset.preferred_format, safe='')`.
4. Returns `_dataset_api_url(validated_config, logical_name, f'/exports/{export_format}')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_dataset_api_url`, `_get_dataset_config`, `_validated_source_config`, `quote`.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `test_build_export_url`
- `tests/unit/test_rte_odre_fr.py` — `test_export_url_uses_configured_dataset_id`
- `tests/unit/test_rte_odre_fr.py` — `test_http_failure_raises_and_cleans_temporary_files`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_build_export_url`
- `tests/unit/test_rte_odre_fr.py::test_export_url_uses_configured_dataset_id`
- `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_optional_string`

**Signature**

```python
def _optional_string(mapping: dict[str, Any], key: str) -> str | None:
```

**Purpose**

Implements optional string according to the exact implementation and guards in this file.

**Inputs**

- `mapping` (`dict[str, Any]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `key` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str | None`. Observed return expression(s): `normalized or None`; `None`.

**Algorithm**

1. Computes `value` from `mapping.get(key)`.
2. Checks `not isinstance(value, str)`. When true: Returns `None`.
3. Computes `normalized` from `value.strip()`.
4. Returns `normalized or None`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `isinstance`, `mapping.get`, `value.strip`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `fetch_rte_odre_dataset_metadata`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_metadata_precision_status`

**Signature**

```python
def _metadata_precision_status(description: str | None) -> GeometryPrecisionStatus:
```

**Purpose**

Implements metadata precision status according to the exact implementation and guards in this file.

**Inputs**

- `description` (`str | None`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GeometryPrecisionStatus`. Observed return expression(s): `'UNKNOWN'`; `'GENERALIZED_OR_RESTRICTED'`.

**Algorithm**

1. Checks `description is None`. When true: Returns `'UNKNOWN'`.
2. Computes `normalized` from `description.casefold()`.
3. Checks `'données gps' in normalized and 'sécurité publique' in normalized`. When true: Returns `'GENERALIZED_OR_RESTRICTED'`.
4. Returns `'UNKNOWN'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `description.casefold`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `fetch_rte_odre_dataset_metadata`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_read_response_json`

**Signature**

```python
def _read_response_json(source_url: str, timeout: float) -> dict[str, Any]:
```

**Purpose**

Reads and validates response json according to the exact implementation and guards in this file.

**Inputs**

- `source_url` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; required) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, Any]`. Observed return expression(s): `payload`.

**Algorithm**

1. Runs guarded operation: Enters managed context(s) `open_safe_https(source_url, timeout=timeout, headers={'User-Agent': 'LandScout-AI/0.1'})` and executes: Computes `payload` from `json.loads(response.read().decode('utf-8'))`. Handles `(HTTPError, URLError, OSError, UnicodeDecodeError, json.JSONDecodeError)`.
2. Checks `not isinstance(payload, dict)`. When true: Raises `RteOdreDownloadError(f'RTE/ODRE response is not a JSON object: {source_url}')`.
3. Returns `payload`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, dict)` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`, `open_safe_https`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `isinstance`, `json.loads`, `open_safe_https`, `response.read`, `response.read().decode`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `fetch_rte_odre_dataset_metadata`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `fetch_rte_odre_dataset_metadata`

**Signature**

```python
def fetch_rte_odre_dataset_metadata(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    timeout: float = 60.0,
) -> RteOdreDatasetMetadata:
```

**Purpose**

Implements fetch rte odre dataset metadata according to the exact implementation and guards in this file.

**Inputs**

- `config` (`RteOdreSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalDatasetName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; optional/default `60.0`) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RteOdreDatasetMetadata`. Observed return expression(s): `RteOdreDatasetMetadata(dataset_id=dataset.dataset_id, title=_optional_string(default_metas, 'title'), publisher=_optional_string(default_metas, 'publisher'), modified=_optional_string(default_metas, 'modified'), data_processed=_optional_string(default_metas, 'data_processed'), metadata_processed=_optional_string(default_metas, 'metadata_processed'), license=_optional_string(default_metas, 'licens…`.

**Algorithm**

1. Computes `validated_config` from `_validated_source_config(config)`.
2. Computes `dataset` from `_get_dataset_config(validated_config, logical_name)`.
3. Computes `metadata_url` from `_dataset_api_url(validated_config, logical_name, '')`.
4. Computes `payload` from `_read_response_json(metadata_url, timeout)`.
5. Computes `response_dataset_id` from `payload.get('dataset_id')`.
6. Checks `response_dataset_id != dataset.dataset_id`. When true: Raises `RteOdreDownloadError(f'Unexpected dataset metadata response for {dataset.dataset_id}')`.
7. Computes `metas` from `payload.get('metas')`.
8. Computes `default_metas` from `metas.get('default') if isinstance(metas, dict) else None`.
9. Checks `not isinstance(default_metas, dict)`. When true: Computes `default_metas` from `{}`.
10. Computes `records_count_value` from `default_metas.get('records_count')`.
11. Checks `records_count_value is None`. When true: Computes `records_count` from `None`. Otherwise: Checks `not isinstance(records_count_value, int) or isinstance(records_count_value, bool)`. When true: Raises `RteOdreDownloadError('RTE/ODRE records_count must be an integer or null')`. Otherwise: Checks `records_count_value < 0`. When true: Raises `RteOdreDownloadError('RTE/ODRE records_count must not be negative')`. Otherwise: Computes `records_count` from `records_count_value`.
12. Computes `description` from `_optional_string(default_metas, 'description')`.
13. Returns `RteOdreDatasetMetadata(dataset_id=dataset.dataset_id, title=_optional_string(default_metas, 'title'), publisher=_optional_string(default_metas, 'publisher'), modified=_optional_string(default_metas, 'modified'), data_processed=_optional_string(default_metas, 'data_processed'), metadata_processed=_optional_string(default_metas, 'metadata_processed'), license…`.

**Validation and invariants**

- Rejects or diverts the path when `response_dataset_id != dataset.dataset_id` is true.
- Rejects or diverts the path when `not isinstance(records_count_value, int) or isinstance(records_count_value, bool)` is true.
- Rejects or diverts the path when `records_count_value < 0` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`, `_read_response_json`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDatasetMetadata`, `RteOdreDownloadError`, `_dataset_api_url`, `_get_dataset_config`, `_metadata_precision_status`, `_optional_string`, `_read_response_json`, `_validated_source_config`, `default_metas.get`, `isinstance`, `metas.get`, `payload.get`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_is_captured_without_fabrication`
- `tests/unit/test_rte_odre_fr.py` — `test_mutated_loaded_api_origin_is_rejected_before_metadata_network`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_metadata_is_captured_without_fabrication`
- `tests/unit/test_rte_odre_fr.py::test_mutated_loaded_api_origin_is_rejected_before_metadata_network`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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

- `src/landscout/sources/rte_odre_fr.py` — `_load_cached_download`
- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_geojson`

**Signature**

```python
def _validate_geojson(path: Path) -> RteOdreExportSummary:
```

**Purpose**

Validates and rejects malformed geojson according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RteOdreExportSummary`. Observed return expression(s): `RteOdreExportSummary(feature_count=len(features), null_geometry_count=null_geometry_count, non_null_geometry_count=len(features) - null_geometry_count, geometry_types=tuple(sorted(geometry_types)))`.

**Algorithm**

1. Checks `not path.is_file() or path.stat().st_size == 0`. When true: Raises `RteOdreDownloadError(f'GeoJSON export is missing or empty: {path}')`.
2. Runs guarded operation: Enters managed context(s) `path.open(encoding='utf-8')` and executes: Computes `payload` from `json.load(stream)`. Handles `(OSError, UnicodeDecodeError, json.JSONDecodeError)`.
3. Checks `not isinstance(payload, dict) or payload.get('type') != 'FeatureCollection'`. When true: Raises `RteOdreDownloadError('GeoJSON export must be a FeatureCollection')`.
4. Computes `features` from `payload.get('features')`.
5. Checks `not isinstance(features, list)`. When true: Raises `RteOdreDownloadError('GeoJSON FeatureCollection must contain a features list')`.
6. Computes `null_geometry_count` from `0`.
7. Defines `geometry_types` with annotation `set[str]` from `set()`.
8. Iterates `feature` over `features`. For each value: Checks `not isinstance(feature, dict) or feature.get('type') != 'Feature'`. When true: Raises `RteOdreDownloadError('Every GeoJSON feature must be an object with type Feature')`. Computes `geometry` from `feature.get('geometry')`. Checks `geometry is None`. When true: Updates `null_geometry_count` using `` and `1`. Executes `continue` control flow. Executes 3 additional source-ordered statement(s).
9. Returns `RteOdreExportSummary(feature_count=len(features), null_geometry_count=null_geometry_count, non_null_geometry_count=len(features) - null_geometry_count, geometry_types=tuple(sorted(geometry_types)))`.

**Validation and invariants**

- Rejects or diverts the path when `not path.is_file() or path.stat().st_size == 0` is true.
- Rejects or diverts the path when `not isinstance(payload, dict) or payload.get('type') != 'FeatureCollection'` is true.
- Rejects or diverts the path when `not isinstance(features, list)` is true.
- Rejects or diverts the path when `not isinstance(feature, dict) or feature.get('type') != 'Feature'` is true.
- Rejects or diverts the path when `not isinstance(geometry, dict)` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`, `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `RteOdreExportSummary`, `_validate_geojson_geometry`, `feature.get`, `geometry_types.add`, `isinstance`, `json.load`, `len`, `path.is_file`, `path.open`, `path.stat`, `payload.get`, `set`, `sorted`, `tuple`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `_load_cached_download`
- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_position`

**Signature**

```python
def _validate_position(value: object, geometry_type: str) -> None:
```

**Purpose**

Validates and rejects malformed position according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometry_type` (`str`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `not isinstance(value, list) or len(value) < 2`. When true: Raises `RteOdreDownloadError(f'GeoJSON {geometry_type} coordinates must contain an X/Y position')`.
2. Checks `any((isinstance(coordinate, bool) or not isinstance(coordinate, Real) or (not isfinite(float(coordinate))) for coordinate in value))`. When true: Raises `RteOdreDownloadError(f'GeoJSON {geometry_type} coordinates must be finite numeric values')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, list) or len(value) < 2` is true.
- Rejects or diverts the path when `any((isinstance(coordinate, bool) or not isinstance(coordinate, Real) or (not isfinite(float(coordinate))) for coordinate in value))` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `any`, `float`, `isfinite`, `isinstance`, `len`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `_validate_nested_coordinates`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_nested_coordinates`

**Signature**

```python
def _validate_nested_coordinates(
    value: object,
    *,
    depth: int,
    geometry_type: str,
) -> None:
```

**Purpose**

Validates and rejects malformed nested coordinates according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `depth` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometry_type` (`str`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `None`.

**Algorithm**

1. Checks `not isinstance(value, list)`. When true: Raises `RteOdreDownloadError(f'GeoJSON {geometry_type} coordinate structure must use JSON arrays')`.
2. Checks `depth == 0`. When true: Calls `_validate_position(value, geometry_type)` for its validation or side effect. Returns `None`.
3. Iterates `member` over `value`. For each value: Calls `_validate_nested_coordinates(member, depth=depth - 1, geometry_type=geometry_type)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, list)` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `_validate_nested_coordinates`, `_validate_position`, `isinstance`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `_validate_geojson_geometry`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_geojson_geometry`

**Signature**

```python
def _validate_geojson_geometry(geometry: object) -> str:
```

**Purpose**

Validates and rejects malformed geojson geometry according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`object`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `geometry_type`.

**Algorithm**

1. Checks `not isinstance(geometry, dict)`. When true: Raises `RteOdreDownloadError('GeoJSON geometry member must be an object')`.
2. Computes `geometry_type` from `geometry.get('type')`.
3. Checks `geometry_type not in GEOJSON_GEOMETRY_TYPES`. When true: Raises `RteOdreDownloadError('GeoJSON feature has an unsupported geometry type')`.
4. Checks `geometry_type == 'GeometryCollection'`. When true: Computes `members` from `geometry.get('geometries')`. Checks `not isinstance(members, list)`. When true: Raises `RteOdreDownloadError('GeoJSON GeometryCollection must contain a geometries list')`. Iterates `member` over `members`. For each value: Calls `_validate_geojson_geometry(member)` for its validation or side effect. Executes 1 additional source-ordered statement(s).
5. Checks `'coordinates' not in geometry`. When true: Raises `RteOdreDownloadError(f'GeoJSON {geometry_type} geometry must contain coordinates')`.
6. Computes `depth_by_type` from `{'Point': 0, 'MultiPoint': 1, 'LineString': 1, 'MultiLineString': 2, 'Polygon': 2, 'MultiPolygon': 3}`.
7. Calls `_validate_nested_coordinates(geometry['coordinates'], depth=depth_by_type[geometry_type], geometry_type=geometry_type)` for its validation or side effect.
8. Returns `geometry_type`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(geometry, dict)` is true.
- Rejects or diverts the path when `geometry_type not in GEOJSON_GEOMETRY_TYPES` is true.
- Rejects or diverts the path when `geometry_type == 'GeometryCollection'` is true.
- Rejects or diverts the path when `'coordinates' not in geometry` is true.
- Rejects or diverts the path when `not isinstance(members, list)` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `_validate_geojson_geometry`, `_validate_nested_coordinates`, `geometry.get`, `isinstance`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `_validate_geojson`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_metadata_from_dict`

**Signature**

```python
def _metadata_from_dict(payload: Any) -> RteOdreDatasetMetadata:
```

**Purpose**

Implements metadata from dict according to the exact implementation and guards in this file.

**Inputs**

- `payload` (`Any`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RteOdreDatasetMetadata`. Observed return expression(s): `RteOdreDatasetMetadata(dataset_id=str(payload['dataset_id']), title=optional_values['title'], publisher=optional_values['publisher'], modified=optional_values['modified'], data_processed=optional_values['data_processed'], metadata_processed=optional_values['metadata_processed'], license=optional_values['license'], records_count=records_count, geometry_precision_status=precision_status)`.

**Algorithm**

1. Checks `not isinstance(payload, dict)`. When true: Raises `TypeError('Missing cached dataset metadata')`.
2. Computes `precision_status` from `payload['geometry_precision_status']`.
3. Computes `allowed_statuses` from `{'EXACT_NOT_CLAIMED', 'GENERALIZED_OR_RESTRICTED', 'MISSING', 'UNKNOWN'}`.
4. Checks `precision_status not in allowed_statuses`. When true: Raises `ValueError('Invalid cached geometry precision status')`.
5. Computes `records_count` from `payload['records_count']`.
6. Checks `records_count is not None and (not isinstance(records_count, int) or isinstance(records_count, bool))`. When true: Raises `TypeError('Invalid cached records count')`.
7. Defines `optional_values` with annotation `dict[str, str | None]` from `{}`.
8. Iterates `field_name` over `('title', 'publisher', 'modified', 'data_processed', 'metadata_processed', 'license')`. For each value: Computes `value` from `payload[field_name]`. Checks `value is not None and (not isinstance(value, str))`. When true: Raises `TypeError(f'Invalid cached metadata value: {field_name}')`. Computes `optional_values[field_name]` from `value`.
9. Returns `RteOdreDatasetMetadata(dataset_id=str(payload['dataset_id']), title=optional_values['title'], publisher=optional_values['publisher'], modified=optional_values['modified'], data_processed=optional_values['data_processed'], metadata_processed=optional_values['metadata_processed'], license=optional_values['license'], records_count=records_count, geometry_preci…`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, dict)` is true.
- Rejects or diverts the path when `precision_status not in allowed_statuses` is true.
- Rejects or diverts the path when `records_count is not None and (not isinstance(records_count, int) or isinstance(records_count, bool))` is true.
- Rejects or diverts the path when `value is not None and (not isinstance(value, str))` is true.

**Exceptions**

- Explicitly raises: `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RteOdreDatasetMetadata`, `TypeError`, `ValueError`, `isinstance`, `str`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `_load_cached_download`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_export_summary_from_dict`

**Signature**

```python
def _export_summary_from_dict(payload: Any) -> RteOdreExportSummary:
```

**Purpose**

Implements export summary from dict according to the exact implementation and guards in this file.

**Inputs**

- `payload` (`Any`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RteOdreExportSummary`. Observed return expression(s): `RteOdreExportSummary(feature_count=payload['feature_count'], null_geometry_count=payload['null_geometry_count'], non_null_geometry_count=payload['non_null_geometry_count'], geometry_types=tuple(geometry_types))`.

**Algorithm**

1. Checks `not isinstance(payload, dict)`. When true: Raises `TypeError('Missing cached export summary')`.
2. Computes `geometry_types` from `payload['geometry_types']`.
3. Checks `not isinstance(geometry_types, list) or any((not isinstance(value, str) for value in geometry_types))`. When true: Raises `TypeError('Invalid cached geometry types')`.
4. Returns `RteOdreExportSummary(feature_count=payload['feature_count'], null_geometry_count=payload['null_geometry_count'], non_null_geometry_count=payload['non_null_geometry_count'], geometry_types=tuple(geometry_types))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, dict)` is true.
- Rejects or diverts the path when `not isinstance(geometry_types, list) or any((not isinstance(value, str) for value in geometry_types))` is true.

**Exceptions**

- Explicitly raises: `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RteOdreExportSummary`, `TypeError`, `any`, `isinstance`, `tuple`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `_load_cached_download`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_records_count`

**Signature**

```python
def _validate_records_count(
    dataset_metadata: RteOdreDatasetMetadata,
    export_summary: RteOdreExportSummary,
) -> None:
```

**Purpose**

Validates and rejects malformed records count according to the exact implementation and guards in this file.

**Inputs**

- `dataset_metadata` (`RteOdreDatasetMetadata`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `export_summary` (`RteOdreExportSummary`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `records_count` from `dataset_metadata.records_count`.
2. Checks `records_count is not None and records_count != export_summary.feature_count`. When true: Raises `RteOdreDownloadError(f'RTE/ODRE metadata records_count does not match export feature_count: {records_count} != {export_summary.feature_count}')`.

**Validation and invariants**

- Rejects or diverts the path when `records_count is not None and records_count != export_summary.feature_count` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `_load_cached_download`
- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`

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

- `src/landscout/sources/rte_odre_fr.py` — `_publish_cache_pair`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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

- `src/landscout/sources/rte_odre_fr.py` — `_prepare_temporary_cache_file`
- `src/landscout/sources/rte_odre_fr.py` — `_require_no_cache_recovery_material`

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

- `src/landscout/sources/rte_odre_fr.py` — `_publish_cache_pair`
- `src/landscout/sources/rte_odre_fr.py` — `_require_no_cache_recovery_material`

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

1. Checks `any((path.exists() or _is_link_or_junction(path) for path in _cache_recovery_paths(archive_path, metadata_path)))`. When true: Raises `RteOdreDownloadError('RTE/ODRE cache recovery backup already exists; manual recovery is required')`.

**Validation and invariants**

- Rejects or diverts the path when `any((path.exists() or _is_link_or_junction(path) for path in _cache_recovery_paths(archive_path, metadata_path)))` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `_cache_recovery_paths`, `_is_link_or_junction`, `any`, `path.exists`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `_publish_cache_pair`
- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`

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

1. Runs guarded operation: Checks `_is_link_or_junction(path)`. When true: Raises `RteOdreDownloadError('RTE/ODRE cache temporary path is a link or junction')`. Checks `path.exists()`. When true: Checks `not path.is_file()`. When true: Raises `RteOdreDownloadError('RTE/ODRE cache temporary path is not a regular file')`. Calls `path.unlink()` for its validation or side effect. Handles `RteOdreDownloadError`, `OSError`.

**Validation and invariants**

- Rejects or diverts the path when `_is_link_or_junction(path)` is true.
- Rejects or diverts the path when `path.exists()` is true.
- Rejects or diverts the path when `not path.is_file()` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`, `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `_is_link_or_junction`, `path.exists`, `path.is_file`, `path.unlink`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`

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
3. Checks `cleanup_error is not None and primary_error is None`. When true: Raises `RteOdreDownloadError('RTE/ODRE cache temporary files could not be cleaned safely')`.

**Validation and invariants**

- Rejects or diverts the path when `cleanup_error is not None and primary_error is None` is true.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`, `path.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `path.unlink`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`

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

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownloadError`, `_replace_file`, `archive_backup.unlink`, `archive_path.unlink`, `copy2`, `metadata_backup.unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownloadError`, `_cache_recovery_paths`, `_replace_file`, `_require_no_cache_recovery_material`, `archive_backup.unlink`, `archive_path.is_file`, `archive_path.unlink`, `copy2`, `metadata_backup.unlink`, `metadata_path.is_file`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`

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
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    source_url: str,
) -> RteOdreDownload | None:
```

**Purpose**

Loads cached download according to the exact implementation and guards in this file.

**Inputs**

- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`RteOdreSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `logical_name` (`LogicalDatasetName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_url` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RteOdreDownload | None`. Observed return expression(s): `None`; `RteOdreDownload(logical_name=logical_name, dataset_id=dataset.dataset_id, provider=config.provider, portal=config.portal, source_url=source_url, export_format=dataset.preferred_format, download_timestamp=download_timestamp, filename=archive_path.name, file_size=file_size, sha256=checksum, path=archive_path, cache_hit=True, dataset_metadata=dataset_metadata, export_summary=cached_summary)`.

**Algorithm**

1. Checks `not archive_path.is_file() or not metadata_path.is_file()`. When true: Returns `None`.
2. Computes `dataset` from `_get_dataset_config(config, logical_name)`.
3. Runs guarded operation: Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`. Checks `not isinstance(metadata, dict)`. When true: Returns `None`. Computes `fresh_summary` from `_validate_geojson(archive_path)`. Computes `file_size` from `archive_path.stat().st_size`. Executes 13 additional source-ordered statement(s). Handles `(KeyError, OSError, TypeError, ValueError, json.JSONDecodeError, RteOdreDownloadError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds`, `RteOdreDownload`, `downloaded_at.astimezone`, `metadata_path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds`, `RteOdreDownload`, `_export_summary_from_dict`, `_get_dataset_config`, `_metadata_from_dict`, `_sha256`, `_validate_geojson`, `_validate_records_count`, `archive_path.is_file`, `archive_path.stat`, `datetime.fromisoformat`, `datetime.now`, `downloaded_at.astimezone`, `isinstance`, `json.loads`, `metadata_path.is_file`, `metadata_path.read_text`, `str`.

**Known repository callers**

- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `download_rte_odre_dataset`

**Signature**

```python
def download_rte_odre_dataset(
    logical_name: LogicalDatasetName,
    config: RteOdreSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
) -> RteOdreDownload:
```

**Purpose**

Downloads and validates rte odre dataset according to the exact implementation and guards in this file.

**Inputs**

- `logical_name` (`LogicalDatasetName`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`RteOdreSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cache_dir` (`Path`; optional/default `DEFAULT_CACHE_DIR`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; optional/default `60.0`) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RteOdreDownload`. Observed return expression(s): `cached`; `result`.

**Algorithm**

1. Computes `validated_config` from `_validated_source_config(config)`.
2. Computes `dataset` from `_get_dataset_config(validated_config, logical_name)`.
3. Computes `export_format` from `quote(dataset.preferred_format, safe='')`.
4. Computes `source_url` from `_dataset_api_url(validated_config, logical_name, f'/exports/{export_format}')`.
5. Computes `filename` from `f'{dataset.dataset_id}.{dataset.preferred_format}'`.
6. Computes `archive_path` from `cache_dir / filename`.
7. Computes `metadata_path` from `cache_dir / f'{filename}.metadata.json'`.
8. Calls `_require_no_cache_recovery_material(archive_path, metadata_path)` for its validation or side effect.
9. Computes `cached` from `_load_cached_download(archive_path, metadata_path, validated_config, logical_name, source_url)`.
10. Checks `cached is not None`. When true: Returns `cached`.
11. Computes `temporary_archive` from `archive_path.with_suffix(f'{archive_path.suffix}.part')`.
12. Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
13. Runs guarded operation: Calls `cache_dir.mkdir(parents=True, exist_ok=True)` for its validation or side effect. Calls `_prepare_temporary_cache_file(temporary_archive)` for its validation or side effect. Calls `_prepare_temporary_cache_file(temporary_metadata)` for its validation or side effect. Handles `RteOdreDownloadError`, `OSError`.
14. Runs guarded operation: Computes `dataset_metadata` from `fetch_rte_odre_dataset_metadata(validated_config, logical_name, timeout=timeout)`. Enters managed context(s) `open_safe_https(source_url, timeout=timeout, headers={'User-Agent': 'LandScout-AI/0.1'}), temporary_archive.open('xb')` and executes: Calls `copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)` for its validation or side effect. Computes `summary` from `_validate_geojson(temporary_archive)`. Calls `_validate_records_count(dataset_metadata, summary)` for its validation or side effect. Executes 8 additional source-ordered statement(s). Handles `RteOdreDownloadError`, `(HTTPError, URLError, OSError)`. Finally: Calls `_cleanup_temporary_cache_files((temporary_archive, temporary_metadata), sys.exception())` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `RteOdreDownloadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `RteOdreDownload`, `RteOdreDownloadError`, `_load_cached_download`, `cache_dir.mkdir`, `copyfileobj`, `open_safe_https`, `output.write`, `replace`, `temporary_archive.open`, `temporary_metadata.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RteOdreDownload`, `RteOdreDownloadError`, `_cleanup_temporary_cache_files`, `_dataset_api_url`, `_get_dataset_config`, `_load_cached_download`, `_prepare_temporary_cache_file`, `_publish_cache_pair`, `_require_no_cache_recovery_material`, `_sha256`, `_validate_geojson`, `_validate_records_count`, `_validated_source_config`, `archive_path.with_suffix`, `asdict`, `cache_dir.mkdir`, `copyfileobj`, `datetime.now`, `datetime.now(UTC).isoformat`, `fetch_rte_odre_dataset_metadata`, `json.dumps`, `lineage.pop`, `metadata_path.with_suffix`, `open_safe_https`, `output.write`, `quote`, `replace`, `sys.exception`, `temporary_archive.open`, `temporary_archive.stat`, `temporary_metadata.open`.

**Known repository callers**

- `tests/unit/test_rte_odre_fr.py` — `test_broken_recovery_symlink_rejects_rte_before_network`
- `tests/unit/test_rte_odre_fr.py` — `test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_cached_export_triggers_refresh`
- `tests/unit/test_rte_odre_fr.py` — `test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py` — `test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py` — `test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_fresh_cache_is_reused`
- `tests/unit/test_rte_odre_fr.py` — `test_http_failure_raises_and_cleans_temporary_files`
- `tests/unit/test_rte_odre_fr.py` — `test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py` — `test_invalid_geojson_download_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_export_record_count_mismatch_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py` — `test_negative_source_record_count_is_rejected`
- `tests/unit/test_rte_odre_fr.py` — `test_null_feature_geometries_are_accepted`
- `tests/unit/test_rte_odre_fr.py` — `test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py` — `test_successful_download`
- `tests/unit/test_rte_odre_fr.py` — `test_temporary_link_or_junction_cannot_modify_target_before_rte_network`
- `tests/unit/test_rte_odre_fr.py` — `test_unavailable_metadata_record_count_is_accepted`

**Tests**

- `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network`
- `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_corrupted_cached_export_triggers_refresh`
- `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network`
- `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed`
- `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache`
- `tests/unit/test_rte_odre_fr.py::test_fresh_cache_is_reused`
- `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files`
- `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache`
- `tests/unit/test_rte_odre_fr.py::test_invalid_geojson_download_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity`
- `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair`
- `tests/unit/test_rte_odre_fr.py::test_negative_source_record_count_is_rejected`
- `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted`
- `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_rte_odre_fr.py::test_successful_download`
- `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network`
- `tests/unit/test_rte_odre_fr.py::test_unavailable_metadata_record_count_is_accepted`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `EXACT_NOT_CLAIMED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `GENERALIZED_OR_RESTRICTED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `MISSING` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNKNOWN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `coordinates` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `data_processed` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `dataset_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dataset_metadata` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `export_format` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `export_summary` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `file_size` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `filename` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geojson` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_precision_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_types` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `license` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `logical_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `metadata_processed` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `modified` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `non_null_geometry_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `null_geometry_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `overhead_lines` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `portal` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `publisher` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `records_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `sha256` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sites` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `title` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `underground_lines` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
