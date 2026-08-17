# `src/landscout/sources/rte_odre_fr.py`

## File identity

- Repository path: `src/landscout/sources/rte_odre_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: grid/source
- Responsibility: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.
- Source SHA256: `b7d422d29f7155399a8dac87422811cc87b2c856f7432ef78fbbe68bfff1edb3`

## 1. Purpose

Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

## 2. Position in LandScout architecture

This file belongs to the **source adapter** layer and the **grid/source** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import json`
- `import sys`
- `from dataclasses import asdict, dataclass, replace`
- `from datetime import UTC, datetime`
- `from hashlib import sha256`
- `from math import isfinite`
- `from numbers import Real`
- `from pathlib import Path`
- `from shutil import copy2, copyfileobj`
- `from typing import Annotated, Any, Literal`
- `from urllib.error import HTTPError, URLError`
- `from urllib.parse import quote, urlsplit`

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
)`

### Internal LandScout imports

- `from landscout.common.safe_http import open_safe_https`

## 4. Contract taxonomy

### A. Python constants

#### `DEFAULT_CONFIG_PATH`

```python
DEFAULT_CONFIG_PATH = Path("configs/sources/rte_odre_fr.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `DEFAULT_CACHE_DIR`

```python
DEFAULT_CACHE_DIR = Path("data/cache/rte_odre")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `DOWNLOAD_CHUNK_SIZE`

```python
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/sources/rte_odre_fr.py::_sha256` (value reference), `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` (value reference).

#### `LOGICAL_DATASET_NAMES`

```python
LOGICAL_DATASET_NAMES = ("sites", "overhead_lines", "underground_lines")
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/sources/rte_odre_fr.py::_get_dataset_config` (value reference).

#### `COORDINATE_GEOMETRY_TYPES`

```python
COORDINATE_GEOMETRY_TYPES = frozenset(
    {
        "Point",
        "MultiPoint",
        "LineString",
        "MultiLineString",
        "Polygon",
        "MultiPolygon",
    }
)
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/sources/rte_odre_fr.py::<module>` (value reference).

#### `GEOJSON_GEOMETRY_TYPES`

```python
GEOJSON_GEOMETRY_TYPES = COORDINATE_GEOMETRY_TYPES | {"GeometryCollection"}
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/sources/rte_odre_fr.py::_validate_geojson_geometry` (value reference).


### B. Type aliases and closed domains

#### `LogicalDatasetName`

```python
LogicalDatasetName = Literal["sites", "overhead_lines", "underground_lines"]
```

Configured RTE/ODRÉ logical dataset role: sites, overhead_lines, or underground_lines. Enforced/consumed by `src/landscout/sources/rte_odre_fr.py::RteOdreDownload` (type annotation), `src/landscout/sources/rte_odre_fr.py::_get_dataset_config` (type annotation), `src/landscout/sources/rte_odre_fr.py::_dataset_api_url` (type annotation), `src/landscout/sources/rte_odre_fr.py::build_rte_odre_metadata_url` (type annotation), `src/landscout/sources/rte_odre_fr.py::build_rte_odre_export_url` (type annotation), `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` (type annotation), `src/landscout/sources/rte_odre_fr.py::_load_cached_download` (type annotation), `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` (type annotation).

#### `ExportFormat`

```python
ExportFormat = Literal["geojson"]
```

ODRÉ export-format domain, currently only geojson. Enforced/consumed by `src/landscout/sources/rte_odre_fr.py::RteDatasetConfig` (type annotation), `src/landscout/sources/rte_odre_fr.py::RteOdreDownload` (type annotation).

#### `GeometryPrecisionStatus`

```python
GeometryPrecisionStatus = Literal[
    "EXACT_NOT_CLAIMED",
    "GENERALIZED_OR_RESTRICTED",
    "MISSING",
    "UNKNOWN",
]
```

RTE source metadata precision assessment: EXACT_NOT_CLAIMED, GENERALIZED_OR_RESTRICTED, MISSING, or UNKNOWN; these are values, not columns. Enforced/consumed by `src/landscout/sources/rte_odre_fr.py::RteOdreDatasetMetadata` (type annotation), `src/landscout/sources/rte_odre_fr.py::_metadata_precision_status` (type annotation).

#### `NonEmptyString`

```python
NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
```

String constrained non-empty after the exact StringConstraints behavior in the declaration. Enforced/consumed by `src/landscout/sources/rte_odre_fr.py::RteOdreSourceConfig` (type annotation).

#### `DatasetIdentifier`

```python
DatasetIdentifier = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]*$",
    ),
]
```

Annotated validation alias whose strictness, regex/bounds, and callbacks are exactly those shown above. Enforced/consumed by `src/landscout/sources/rte_odre_fr.py::RteDatasetConfig` (type annotation).


### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `RteDatasetConfig`

**Purpose:** Validates the grid/source contract carried by `dataset_id`, `preferred_format`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `dataset_id` | `dataset_id: DatasetIdentifier` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `preferred_format` | `preferred_format: ExportFormat` | `RteDatasetConfig.preferred_format` represents the `preferred_format` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::RteDatasetsConfig` via `RteDatasetConfig`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_get_dataset_config` via `RteDatasetConfig`.

**Exact class source**

```python
class RteDatasetConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    dataset_id: DatasetIdentifier
    preferred_format: ExportFormat
```

### `RteDatasetsConfig`

**Purpose:** Validates the grid/source contract carried by `sites`, `overhead_lines`, `underground_lines`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `sites` | `sites: RteDatasetConfig` | Configuration for the RTE electrical-sites logical dataset. |
| `overhead_lines` | `overhead_lines: RteDatasetConfig` | Configuration for the RTE overhead-lines logical dataset. |
| `underground_lines` | `underground_lines: RteDatasetConfig` | Configuration for the RTE underground-lines logical dataset. |

**Interface consumers**

- type annotation: `src/landscout/sources/rte_odre_fr.py::RteOdreSourceConfig` via `RteDatasetsConfig`.

**Exact class source**

```python
class RteDatasetsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sites: RteDatasetConfig
    overhead_lines: RteDatasetConfig
    underground_lines: RteDatasetConfig
```

### `RteOdreApiConfig`

**Purpose:** Validates the grid/source contract carried by `base_url`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `base_url` | `base_url: HttpUrl` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |

**Validators (exact source)**

`_official_api_origin`:

```python
def _official_api_origin(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlsplit(str(value))
        if (
            parsed.scheme != "https"
            or parsed.hostname != "odre.opendatasoft.com"
            or parsed.port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path.rstrip("/") != "/api/explore/v2.1"
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("RTE/ODRE API must use the exact official HTTPS origin")
        return value
```

**Interface consumers**

- type annotation: `src/landscout/sources/rte_odre_fr.py::RteOdreSourceConfig` via `RteOdreApiConfig`.

**Exact class source**

```python
class RteOdreApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    base_url: HttpUrl

    @field_validator("base_url")
    @classmethod
    def _official_api_origin(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlsplit(str(value))
        if (
            parsed.scheme != "https"
            or parsed.hostname != "odre.opendatasoft.com"
            or parsed.port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path.rstrip("/") != "/api/explore/v2.1"
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("RTE/ODRE API must use the exact official HTTPS origin")
        return value
```

### `RteOdreCacheConfig`

**Purpose:** Validates the grid/source contract carried by `max_age_hours`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `max_age_hours` | `max_age_hours: float = Field(ge=0, allow_inf_nan=False)` | Configured maximum cache age in hours; zero requires immediate refresh. |

**Interface consumers**

- type annotation: `src/landscout/sources/rte_odre_fr.py::RteOdreSourceConfig` via `RteOdreCacheConfig`.

**Exact class source**

```python
class RteOdreCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    max_age_hours: float = Field(ge=0, allow_inf_nan=False)
```

### `RteOdreSourceConfig`

**Purpose:** Validates the grid/source contract carried by `provider`, `portal`, `api`, `datasets`, `cache`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `provider` | `provider: NonEmptyString` | Source-provider identity carried by this configuration/result and checked against its owning source contract. |
| `portal` | `portal: NonEmptyString` | Source-portal identity carried by this configuration/result; it is provenance rather than physical proof by itself. |
| `api` | `api: RteOdreApiConfig` | Nested official API-origin/path configuration. |
| `datasets` | `datasets: RteDatasetsConfig` | Nested configuration for the three logical RTE/ODRÉ datasets. |
| `cache` | `cache: RteOdreCacheConfig` | Nested cache-path and freshness configuration. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- import: `tests/unit/test_rte_odre_fr.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::load_rte_odre_source_config` via `RteOdreSourceConfig`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_validated_source_config` via `RteOdreSourceConfig`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_get_dataset_config` via `RteOdreSourceConfig`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_dataset_api_url` via `RteOdreSourceConfig`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::build_rte_odre_metadata_url` via `RteOdreSourceConfig`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::build_rte_odre_export_url` via `RteOdreSourceConfig`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `RteOdreSourceConfig`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `RteOdreSourceConfig`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::source_config` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_valid_source_config_loads` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_build_export_url` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_build_metadata_url` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_metadata_is_captured_without_fabrication` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_successful_download` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_unavailable_metadata_record_count_is_accepted` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_negative_source_record_count_is_rejected` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_fresh_cache_is_reused` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_invalid_geojson_download_is_rejected` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_corrupted_cached_export_triggers_refresh` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `RteOdreSourceConfig`.
- type annotation: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `RteOdreSourceConfig`.

**Exact class source**

```python
class RteOdreSourceConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    provider: NonEmptyString
    portal: NonEmptyString
    api: RteOdreApiConfig
    datasets: RteDatasetsConfig
    cache: RteOdreCacheConfig
```

### `RteOdreDownloadError`

**Purpose:** Raised when RTE/ODRE metadata or exports cannot be retrieved safely.

**Kind:** controlled exception.

**Inheritance:** `RuntimeError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- import: `tests/unit/test_rte_odre_fr.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_validated_source_config` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_read_response_json` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_validate_geojson` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_validate_position` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_validate_nested_coordinates` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_validate_geojson_geometry` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_validate_records_count` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_require_no_cache_recovery_material` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_prepare_temporary_cache_file` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_cleanup_temporary_cache_files` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_publish_cache_pair` via `RteOdreDownloadError`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `RteOdreDownloadError`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `pytest.raises(RteOdreDownloadError, match='config|official|origin')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected` via `pytest.raises(RteOdreDownloadError, match='records_count')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_negative_source_record_count_is_rejected` via `pytest.raises(RteOdreDownloadError, match='must not be negative')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files` via `pytest.raises(RteOdreDownloadError)`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `pytest.raises(RteOdreDownloadError)`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache` via `pytest.raises(RteOdreDownloadError)`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `pytest.raises(RteOdreDownloadError)`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_invalid_geojson_download_is_rejected` via `pytest.raises(RteOdreDownloadError)`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_malformed_geojson_feature_or_geometry_is_rejected` via `pytest.raises(RteOdreDownloadError)`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_point_requires_a_finite_numeric_position` via `pytest.raises(RteOdreDownloadError, match='coordinate|Point|finite')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_nested_coordinate_geometries_reject_obvious_invalid_structure` via `pytest.raises(RteOdreDownloadError, match='coordinate|structure|finite')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_geometry_collection_members_are_validated_recursively` via `pytest.raises(RteOdreDownloadError, match='coordinate|Point')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `pytest.raises(RteOdreDownloadError, match='rollback')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `pytest.raises(RteOdreDownloadError, match='backup|recovery|manual')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `pytest.raises(RteOdreDownloadError, match='temporary|link|cache')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `pytest.raises(RteOdreDownloadError, match='backup|recovery|manual')`.
- expected exception type: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `pytest.raises(RteOdreDownloadError, match='rollback')`.

**Exact class source**

```python
class RteOdreDownloadError(RuntimeError):
    """Raised when RTE/ODRE metadata or exports cannot be retrieved safely."""
```

### `RteOdreDatasetMetadata`

**Purpose:** Immutable result/value envelope carrying `dataset_id`, `title`, `publisher`, `modified`, `data_processed`, `metadata_processed`, `license`, `records_count`, `geometry_precision_status`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `dataset_id` | `dataset_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `title` | `title: str \| None` | `RteOdreDatasetMetadata.title` carries the title used by the reproduced constructors and validators; its declared type is `str | None` and no legal meaning is inferred beyond that owner. |
| `publisher` | `publisher: str \| None` | Publisher text reported by the owning source metadata or checked-in reference. |
| `modified` | `modified: str \| None` | Nullable source-reported dataset modification timestamp text. |
| `data_processed` | `data_processed: str \| None` | Nullable source-reported timestamp for data processing. |
| `metadata_processed` | `metadata_processed: str \| None` | Nullable source-reported timestamp for metadata processing. |
| `license` | `license: str \| None` | Nullable source-reported dataset licence text. |
| `records_count` | `records_count: int \| None` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `geometry_precision_status` | `geometry_precision_status: GeometryPrecisionStatus` | `RteOdreDatasetMetadata.geometry_precision_status` represents the `geometry_precision_status` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::RteOdreDownload` via `RteOdreDatasetMetadata`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `RteOdreDatasetMetadata`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `RteOdreDatasetMetadata`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_metadata_from_dict` via `RteOdreDatasetMetadata`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_metadata_from_dict` via `RteOdreDatasetMetadata`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_validate_records_count` via `RteOdreDatasetMetadata`.

**Exact class source**

```python
class RteOdreDatasetMetadata:
    dataset_id: str
    title: str | None
    publisher: str | None
    modified: str | None
    data_processed: str | None
    metadata_processed: str | None
    license: str | None
    records_count: int | None
    geometry_precision_status: GeometryPrecisionStatus

    def __post_init__(self) -> None:
        if self.records_count is not None and (
            not isinstance(self.records_count, int)
            or isinstance(self.records_count, bool)
            or self.records_count < 0
        ):
            raise ValueError("records_count must be a non-negative integer or None")
```

### `RteOdreExportSummary`

**Purpose:** Immutable result/value envelope carrying `feature_count`, `null_geometry_count`, `non_null_geometry_count`, `geometry_types`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `feature_count` | `feature_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `null_geometry_count` | `null_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `non_null_geometry_count` | `non_null_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `geometry_types` | `geometry_types: tuple[str, ...]` | `RteOdreExportSummary.geometry_types` represents the `geometry_types` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- import: `tests/unit/test_rte_odre_fr.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::RteOdreDownload` via `RteOdreExportSummary`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_validate_geojson` via `RteOdreExportSummary`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_validate_geojson` via `RteOdreExportSummary`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_export_summary_from_dict` via `RteOdreExportSummary`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_export_summary_from_dict` via `RteOdreExportSummary`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_validate_records_count` via `RteOdreExportSummary`.
- constructor call: `tests/unit/test_rte_odre_fr.py::test_successful_download` via `RteOdreExportSummary`.
- constructor call: `tests/unit/test_rte_odre_fr.py::test_export_summary_rejects_invalid_geometry_counts` via `RteOdreExportSummary`.
- constructor call: `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted` via `RteOdreExportSummary`.

**Exact class source**

```python
class RteOdreExportSummary:
    feature_count: int
    null_geometry_count: int
    non_null_geometry_count: int
    geometry_types: tuple[str, ...]

    def __post_init__(self) -> None:
        counts = {
            "feature_count": self.feature_count,
            "null_geometry_count": self.null_geometry_count,
            "non_null_geometry_count": self.non_null_geometry_count,
        }
        for name, value in counts.items():
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError(f"{name} must be a non-negative integer")
        if self.null_geometry_count + self.non_null_geometry_count != self.feature_count:
            raise ValueError("Geometry counts must add up to feature_count")
        if not isinstance(self.geometry_types, tuple) or any(
            not isinstance(value, str) or not value for value in self.geometry_types
        ):
            raise TypeError("geometry_types must be a tuple of non-empty strings")
```

### `RteOdreDownload`

**Purpose:** Immutable result/value envelope carrying `logical_name`, `dataset_id`, `provider`, `portal`, `source_url`, `export_format`, `download_timestamp`, `filename`, `file_size`, `sha256`, `path`, `cache_hit`, `dataset_metadata`, `export_summary`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `logical_name` | `logical_name: LogicalDatasetName` | LandScout logical dataset/layer role bound to the selected physical source. |
| `dataset_id` | `dataset_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `provider` | `provider: str` | Source-provider identity carried by this configuration/result and checked against its owning source contract. |
| `portal` | `portal: str` | Source-portal identity carried by this configuration/result; it is provenance rather than physical proof by itself. |
| `source_url` | `source_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `export_format` | `export_format: ExportFormat` | `RteOdreDownload.export_format` represents the `export_format` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `download_timestamp` | `download_timestamp: str` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `filename` | `filename: str` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `file_size` | `file_size: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `path` | `path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `cache_hit` | `cache_hit: bool` | True only when already verified local cache state was reused. |
| `dataset_metadata` | `dataset_metadata: RteOdreDatasetMetadata` | Validated RTE/ODRÉ API metadata associated with the downloaded logical dataset. |
| `export_summary` | `export_summary: RteOdreExportSummary` | Geometry/count summary calculated from the validated RTE/ODRÉ GeoJSON export. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `RteOdreDownload`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `RteOdreDownload`.
- type annotation: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `RteOdreDownload`.
- constructor call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `RteOdreDownload`.

**Exact class source**

```python
class RteOdreDownload:
    logical_name: LogicalDatasetName
    dataset_id: str
    provider: str
    portal: str
    source_url: str
    export_format: ExportFormat
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool
    dataset_metadata: RteOdreDatasetMetadata
    export_summary: RteOdreExportSummary
```


## 6. Functions and methods

### `RteOdreApiConfig._official_api_origin`

**Exact signature**

```python
def _official_api_origin(cls, value: HttpUrl) -> HttpUrl:
```

**Purpose**

Private `grid/source` helper for official api origin; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `HttpUrl`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `parsed.scheme != 'https' or parsed.hostname != 'odre.opendatasoft.com' or parsed.port not in {None, 443} or (parsed.username is not None) or (parsed.password is not None) or (parsed.path.rstrip('/') != '/api/explore/v2.1') or parsed.query or parsed.fragment`.
- Explicit raise expressions: `ValueError('RTE/ODRE API must use the exact official HTTPS origin')`.

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

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _official_api_origin(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlsplit(str(value))
        if (
            parsed.scheme != "https"
            or parsed.hostname != "odre.opendatasoft.com"
            or parsed.port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path.rstrip("/") != "/api/explore/v2.1"
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("RTE/ODRE API must use the exact official HTTPS origin")
        return value
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `RteOdreDatasetMetadata.__post_init__`

**Exact signature**

```python
def __post_init__(self) -> None:
```

**Purpose**

Private `grid/source` helper for post init; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `self.records_count is not None and (not isinstance(self.records_count, int) or isinstance(self.records_count, bool) or self.records_count < 0)`.
- Explicit raise expressions: `ValueError('records_count must be a non-negative integer or None')`.

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

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __post_init__(self) -> None:
        if self.records_count is not None and (
            not isinstance(self.records_count, int)
            or isinstance(self.records_count, bool)
            or self.records_count < 0
        ):
            raise ValueError("records_count must be a non-negative integer or None")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `RteOdreExportSummary.__post_init__`

**Exact signature**

```python
def __post_init__(self) -> None:
```

**Purpose**

Private `grid/source` helper for post init; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `self.null_geometry_count + self.non_null_geometry_count != self.feature_count`.
- Guard with a raise path: `not isinstance(self.geometry_types, tuple) or any((not isinstance(value, str) or not value for value in self.geometry_types))`.
- Guard with a raise path: `not isinstance(value, int) or isinstance(value, bool) or value < 0`.
- Explicit raise expressions: `TypeError('geometry_types must be a tuple of non-empty strings')`, `ValueError('Geometry counts must add up to feature_count')`, `ValueError(f'{name} must be a non-negative integer')`.

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

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __post_init__(self) -> None:
        counts = {
            "feature_count": self.feature_count,
            "null_geometry_count": self.null_geometry_count,
            "non_null_geometry_count": self.non_null_geometry_count,
        }
        for name, value in counts.items():
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError(f"{name} must be a non-negative integer")
        if self.null_geometry_count + self.non_null_geometry_count != self.feature_count:
            raise ValueError("Geometry counts must add up to feature_count")
        if not isinstance(self.geometry_types, tuple) or any(
            not isinstance(value, str) or not value for value in self.geometry_types
        ):
            raise TypeError("geometry_types must be a tuple of non-empty strings")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_rte_odre_source_config`

**Exact signature**

```python
def load_rte_odre_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> RteOdreSourceConfig:
```

**Purpose**

Reads and validates rte odre source config; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `RteOdreSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
RteOdreSourceConfig.model_validate(content)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(content, dict)`.
- Explicit raise expressions: `TypeError(f'Expected a YAML mapping in {path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.open`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- import: `tests/unit/test_rte_odre_fr.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- direct call: `tests/unit/test_rte_odre_fr.py::source_config` via `load_rte_odre_source_config`.

**Complete source-ordered implementation**

```python
def load_rte_odre_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> RteOdreSourceConfig:
    with path.open(encoding="utf-8") as stream:
        content = yaml.safe_load(stream)
    if not isinstance(content, dict):
        raise TypeError(f"Expected a YAML mapping in {path}")
    return RteOdreSourceConfig.model_validate(content)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validated_source_config`

**Exact signature**

```python
def _validated_source_config(config: object) -> RteOdreSourceConfig:
```

**Purpose**

Checks and returns canonical source config; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `RteOdreSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
RteOdreSourceConfig.model_validate(config.model_dump(mode='python'))
```

**Validation and exceptions**

- Guard with a raise path: `type(config) is not RteOdreSourceConfig`.
- Explicit raise expressions: `RteOdreDownloadError('RTE/ODRE source config no longer satisfies the official origin contract')`, `TypeError('RTE/ODRE source config type is invalid')`.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::build_rte_odre_metadata_url` via `_validated_source_config`.
- direct call: `src/landscout/sources/rte_odre_fr.py::build_rte_odre_export_url` via `_validated_source_config`.
- direct call: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `_validated_source_config`.
- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_validated_source_config`.

**Complete source-ordered implementation**

```python
def _validated_source_config(config: object) -> RteOdreSourceConfig:
    try:
        if type(config) is not RteOdreSourceConfig:
            raise TypeError("RTE/ODRE source config type is invalid")
        return RteOdreSourceConfig.model_validate(config.model_dump(mode="python"))
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise RteOdreDownloadError(
            "RTE/ODRE source config no longer satisfies the official origin contract"
        ) from error
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_get_dataset_config`

**Exact signature**

```python
def _get_dataset_config(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> RteDatasetConfig:
```

**Purpose**

Private `grid/source` helper for get dataset config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `RteDatasetConfig`.
- Every observed return expression is reproduced without truncation:
```python
getattr(config.datasets, logical_name)
```

**Validation and exceptions**

- Guard with a raise path: `logical_name not in LOGICAL_DATASET_NAMES`.
- Explicit raise expressions: `ValueError(f'Unsupported RTE/ODRE logical dataset: {logical_name}')`.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_dataset_api_url` via `_get_dataset_config`.
- direct call: `src/landscout/sources/rte_odre_fr.py::build_rte_odre_export_url` via `_get_dataset_config`.
- direct call: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `_get_dataset_config`.
- direct call: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `_get_dataset_config`.
- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_get_dataset_config`.

**Complete source-ordered implementation**

```python
def _get_dataset_config(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> RteDatasetConfig:
    if logical_name not in LOGICAL_DATASET_NAMES:
        raise ValueError(f"Unsupported RTE/ODRE logical dataset: {logical_name}")
    return getattr(config.datasets, logical_name)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_dataset_api_url`

**Exact signature**

```python
def _dataset_api_url(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    suffix: str,
) -> str:
```

**Purpose**

Private `grid/source` helper for dataset api url; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
f"{str(config.api.base_url).rstrip('/')}/catalog/datasets/{encoded_dataset_id}{suffix}"
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

- direct call: `src/landscout/sources/rte_odre_fr.py::build_rte_odre_metadata_url` via `_dataset_api_url`.
- direct call: `src/landscout/sources/rte_odre_fr.py::build_rte_odre_export_url` via `_dataset_api_url`.
- direct call: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `_dataset_api_url`.
- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_dataset_api_url`.

**Complete source-ordered implementation**

```python
def _dataset_api_url(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    suffix: str,
) -> str:
    dataset = _get_dataset_config(config, logical_name)
    encoded_dataset_id = quote(dataset.dataset_id, safe="")
    return (
        f"{str(config.api.base_url).rstrip('/')}/catalog/datasets/"
        f"{encoded_dataset_id}{suffix}"
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `build_rte_odre_metadata_url`

**Exact signature**

```python
def build_rte_odre_metadata_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
```

**Purpose**

Constructs rte odre metadata url; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_dataset_api_url(validated_config, logical_name, '')
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

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- import: `tests/unit/test_rte_odre_fr.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_build_metadata_url` via `build_rte_odre_metadata_url`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `build_rte_odre_metadata_url`.

**Complete source-ordered implementation**

```python
def build_rte_odre_metadata_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
    validated_config = _validated_source_config(config)
    return _dataset_api_url(validated_config, logical_name, "")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `build_rte_odre_export_url`

**Exact signature**

```python
def build_rte_odre_export_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
```

**Purpose**

Constructs rte odre export url; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_dataset_api_url(validated_config, logical_name, f'/exports/{export_format}')
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

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- import: `tests/unit/test_rte_odre_fr.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_build_export_url` via `build_rte_odre_export_url`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_export_url_uses_configured_dataset_id` via `build_rte_odre_export_url`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files` via `build_rte_odre_export_url`.

**Complete source-ordered implementation**

```python
def build_rte_odre_export_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
    validated_config = _validated_source_config(config)
    dataset = _get_dataset_config(validated_config, logical_name)
    export_format = quote(dataset.preferred_format, safe="")
    return _dataset_api_url(
        validated_config, logical_name, f"/exports/{export_format}"
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_optional_string`

**Exact signature**

```python
def _optional_string(mapping: dict[str, Any], key: str) -> str | None:
```

**Purpose**

Private `grid/source` helper for optional string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str | None`.
- Every observed return expression is reproduced without truncation:
```python
normalized or None

None
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

- direct call: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `_optional_string`.

**Complete source-ordered implementation**

```python
def _optional_string(mapping: dict[str, Any], key: str) -> str | None:
    value = mapping.get(key)
    if not isinstance(value, str):
        return None
    normalized = value.strip()
    return normalized or None
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_metadata_precision_status`

**Exact signature**

```python
def _metadata_precision_status(description: str | None) -> GeometryPrecisionStatus:
```

**Purpose**

Private `grid/source` helper for metadata precision status; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GeometryPrecisionStatus`.
- Every observed return expression is reproduced without truncation:
```python
'UNKNOWN'

'UNKNOWN'

'GENERALIZED_OR_RESTRICTED'
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

- direct call: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `_metadata_precision_status`.

**Complete source-ordered implementation**

```python
def _metadata_precision_status(description: str | None) -> GeometryPrecisionStatus:
    if description is None:
        return "UNKNOWN"
    normalized = description.casefold()
    if "données gps" in normalized and "sécurité publique" in normalized:
        return "GENERALIZED_OR_RESTRICTED"
    return "UNKNOWN"
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_read_response_json`

**Exact signature**

```python
def _read_response_json(source_url: str, timeout: float) -> dict[str, Any]:
```

**Purpose**

Reads response json; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `dict[str, Any]`.
- Every observed return expression is reproduced without truncation:
```python
payload
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, dict)`.
- Explicit raise expressions: `RteOdreDownloadError(f'RTE/ODRE request failed: {source_url}')`, `RteOdreDownloadError(f'RTE/ODRE response is not a JSON object: {source_url}')`.

**Side effects**

- Network I/O: `open_safe_https`.
- Filesystem read: `response.read`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `_read_response_json`.

**Complete source-ordered implementation**

```python
def _read_response_json(source_url: str, timeout: float) -> dict[str, Any]:
    try:
        with open_safe_https(
            source_url,
            timeout=timeout,
            headers={"User-Agent": "LandScout-AI/0.1"},
        ) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RteOdreDownloadError(f"RTE/ODRE request failed: {source_url}") from error
    if not isinstance(payload, dict):
        raise RteOdreDownloadError(
            f"RTE/ODRE response is not a JSON object: {source_url}"
        )
    return payload
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `fetch_rte_odre_dataset_metadata`

**Exact signature**

```python
def fetch_rte_odre_dataset_metadata(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    timeout: float = 60.0,
) -> RteOdreDatasetMetadata:
```

**Purpose**

Private `grid/source` helper for fetch rte odre dataset metadata; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `RteOdreDatasetMetadata`.
- Every observed return expression is reproduced without truncation:
```python
RteOdreDatasetMetadata(dataset_id=dataset.dataset_id, title=_optional_string(default_metas, 'title'), publisher=_optional_string(default_metas, 'publisher'), modified=_optional_string(default_metas, 'modified'), data_processed=_optional_string(default_metas, 'data_processed'), metadata_processed=_optional_string(default_metas, 'metadata_processed'), license=_optional_string(default_metas, 'license'), records_count=records_count, geometry_precision_status=_metadata_precision_status(description))
```

**Validation and exceptions**

- Guard with a raise path: `response_dataset_id != dataset.dataset_id`.
- Guard with a raise path: `not isinstance(records_count_value, int) or isinstance(records_count_value, bool)`.
- Guard with a raise path: `records_count_value < 0`.
- Explicit raise expressions: `RteOdreDownloadError('RTE/ODRE records_count must be an integer or null')`, `RteOdreDownloadError('RTE/ODRE records_count must not be negative')`, `RteOdreDownloadError(f'Unexpected dataset metadata response for {dataset.dataset_id}')`.

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

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- import: `tests/unit/test_rte_odre_fr.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `fetch_rte_odre_dataset_metadata`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `fetch_rte_odre_dataset_metadata`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_metadata_is_captured_without_fabrication` via `fetch_rte_odre_dataset_metadata`.

**Complete source-ordered implementation**

```python
def fetch_rte_odre_dataset_metadata(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    timeout: float = 60.0,
) -> RteOdreDatasetMetadata:
    validated_config = _validated_source_config(config)
    dataset = _get_dataset_config(validated_config, logical_name)
    metadata_url = _dataset_api_url(validated_config, logical_name, "")
    payload = _read_response_json(metadata_url, timeout)
    response_dataset_id = payload.get("dataset_id")
    if response_dataset_id != dataset.dataset_id:
        raise RteOdreDownloadError(
            f"Unexpected dataset metadata response for {dataset.dataset_id}"
        )

    metas = payload.get("metas")
    default_metas = metas.get("default") if isinstance(metas, dict) else None
    if not isinstance(default_metas, dict):
        default_metas = {}
    records_count_value = default_metas.get("records_count")
    if records_count_value is None:
        records_count = None
    elif not isinstance(records_count_value, int) or isinstance(
        records_count_value, bool
    ):
        raise RteOdreDownloadError("RTE/ODRE records_count must be an integer or null")
    elif records_count_value < 0:
        raise RteOdreDownloadError("RTE/ODRE records_count must not be negative")
    else:
        records_count = records_count_value
    description = _optional_string(default_metas, "description")
    return RteOdreDatasetMetadata(
        dataset_id=dataset.dataset_id,
        title=_optional_string(default_metas, "title"),
        publisher=_optional_string(default_metas, "publisher"),
        modified=_optional_string(default_metas, "modified"),
        data_processed=_optional_string(default_metas, "data_processed"),
        metadata_processed=_optional_string(default_metas, "metadata_processed"),
        license=_optional_string(default_metas, "license"),
        records_count=records_count,
        geometry_precision_status=_metadata_precision_status(description),
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_sha256`

**Exact signature**

```python
def _sha256(path: Path) -> str:
```

**Purpose**

Private `grid/source` helper for sha256; its complete implementation below is the authoritative behavioral contract.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `_sha256`.
- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_sha256`.

**Complete source-ordered implementation**

```python
def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_geojson`

**Exact signature**

```python
def _validate_geojson(path: Path) -> RteOdreExportSummary:
```

**Purpose**

Rejects malformed or inconsistent geojson; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `RteOdreExportSummary`.
- Every observed return expression is reproduced without truncation:
```python
RteOdreExportSummary(feature_count=len(features), null_geometry_count=null_geometry_count, non_null_geometry_count=len(features) - null_geometry_count, geometry_types=tuple(sorted(geometry_types)))
```

**Validation and exceptions**

- Guard with a raise path: `not path.is_file() or path.stat().st_size == 0`.
- Guard with a raise path: `not isinstance(payload, dict) or payload.get('type') != 'FeatureCollection'`.
- Guard with a raise path: `not isinstance(features, list)`.
- Guard with a raise path: `not isinstance(feature, dict) or feature.get('type') != 'Feature'`.
- Guard with a raise path: `not isinstance(geometry, dict)`.
- Explicit raise expressions: `RteOdreDownloadError('Every GeoJSON feature must be an object with type Feature')`, `RteOdreDownloadError('GeoJSON FeatureCollection must contain a features list')`, `RteOdreDownloadError('GeoJSON export must be a FeatureCollection')`, `RteOdreDownloadError('GeoJSON feature geometry must be an object or null')`, `RteOdreDownloadError(f'GeoJSON export is missing or empty: {path}')`, `RteOdreDownloadError(f'GeoJSON export is not valid UTF-8 JSON: {path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.is_file`, `path.open`, `path.stat`.
- Filesystem write: none.
- CRS/geometry calculation: `_validate_geojson_geometry`, `geometry_types.add`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `geometry_types`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `_validate_geojson`.
- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_validate_geojson`.

**Complete source-ordered implementation**

```python
def _validate_geojson(path: Path) -> RteOdreExportSummary:
    if not path.is_file() or path.stat().st_size == 0:
        raise RteOdreDownloadError(f"GeoJSON export is missing or empty: {path}")
    try:
        with path.open(encoding="utf-8") as stream:
            payload = json.load(stream)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RteOdreDownloadError(f"GeoJSON export is not valid UTF-8 JSON: {path}") from error
    if not isinstance(payload, dict) or payload.get("type") != "FeatureCollection":
        raise RteOdreDownloadError("GeoJSON export must be a FeatureCollection")
    features = payload.get("features")
    if not isinstance(features, list):
        raise RteOdreDownloadError("GeoJSON FeatureCollection must contain a features list")

    null_geometry_count = 0
    geometry_types: set[str] = set()
    for feature in features:
        if not isinstance(feature, dict) or feature.get("type") != "Feature":
            raise RteOdreDownloadError(
                "Every GeoJSON feature must be an object with type Feature"
            )
        geometry = feature.get("geometry")
        if geometry is None:
            null_geometry_count += 1
            continue
        if not isinstance(geometry, dict):
            raise RteOdreDownloadError(
                "GeoJSON feature geometry must be an object or null"
            )
        geometry_type = _validate_geojson_geometry(geometry)
        geometry_types.add(geometry_type)
    return RteOdreExportSummary(
        feature_count=len(features),
        null_geometry_count=null_geometry_count,
        non_null_geometry_count=len(features) - null_geometry_count,
        geometry_types=tuple(sorted(geometry_types)),
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_position`

**Exact signature**

```python
def _validate_position(value: object, geometry_type: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent position; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, list) or len(value) < 2`.
- Guard with a raise path: `any((isinstance(coordinate, bool) or not isinstance(coordinate, Real) or (not isfinite(float(coordinate))) for coordinate in value))`.
- Explicit raise expressions: `RteOdreDownloadError(f'GeoJSON {geometry_type} coordinates must be finite numeric values')`, `RteOdreDownloadError(f'GeoJSON {geometry_type} coordinates must contain an X/Y position')`.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_validate_nested_coordinates` via `_validate_position`.

**Complete source-ordered implementation**

```python
def _validate_position(value: object, geometry_type: str) -> None:
    if not isinstance(value, list) or len(value) < 2:
        raise RteOdreDownloadError(
            f"GeoJSON {geometry_type} coordinates must contain an X/Y position"
        )
    if any(
        isinstance(coordinate, bool)
        or not isinstance(coordinate, Real)
        or not isfinite(float(coordinate))
        for coordinate in value
    ):
        raise RteOdreDownloadError(
            f"GeoJSON {geometry_type} coordinates must be finite numeric values"
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_nested_coordinates`

**Exact signature**

```python
def _validate_nested_coordinates(
    value: object,
    *,
    depth: int,
    geometry_type: str,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent nested coordinates; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
None
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, list)`.
- Explicit raise expressions: `RteOdreDownloadError(f'GeoJSON {geometry_type} coordinate structure must use JSON arrays')`.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_validate_geojson_geometry` via `_validate_nested_coordinates`.

**Complete source-ordered implementation**

```python
def _validate_nested_coordinates(
    value: object,
    *,
    depth: int,
    geometry_type: str,
) -> None:
    if not isinstance(value, list):
        raise RteOdreDownloadError(
            f"GeoJSON {geometry_type} coordinate structure must use JSON arrays"
        )
    if depth == 0:
        _validate_position(value, geometry_type)
        return
    for member in value:
        _validate_nested_coordinates(
            member,
            depth=depth - 1,
            geometry_type=geometry_type,
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_geojson_geometry`

**Exact signature**

```python
def _validate_geojson_geometry(geometry: object) -> str:
```

**Purpose**

Rejects malformed or inconsistent geojson geometry; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
geometry_type

geometry_type
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(geometry, dict)`.
- Guard with a raise path: `geometry_type not in GEOJSON_GEOMETRY_TYPES`.
- Guard with a raise path: `geometry_type == 'GeometryCollection'`.
- Guard with a raise path: `'coordinates' not in geometry`.
- Guard with a raise path: `not isinstance(members, list)`.
- Explicit raise expressions: `RteOdreDownloadError('GeoJSON GeometryCollection must contain a geometries list')`, `RteOdreDownloadError('GeoJSON feature has an unsupported geometry type')`, `RteOdreDownloadError('GeoJSON geometry member must be an object')`, `RteOdreDownloadError(f'GeoJSON {geometry_type} geometry must contain coordinates')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_validate_geojson_geometry`, `geometry.get`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/rte_odre_fr.py::_validate_geojson` via `_validate_geojson_geometry`.

**Complete source-ordered implementation**

```python
def _validate_geojson_geometry(geometry: object) -> str:
    if not isinstance(geometry, dict):
        raise RteOdreDownloadError("GeoJSON geometry member must be an object")
    geometry_type = geometry.get("type")
    if geometry_type not in GEOJSON_GEOMETRY_TYPES:
        raise RteOdreDownloadError("GeoJSON feature has an unsupported geometry type")
    if geometry_type == "GeometryCollection":
        members = geometry.get("geometries")
        if not isinstance(members, list):
            raise RteOdreDownloadError(
                "GeoJSON GeometryCollection must contain a geometries list"
            )
        for member in members:
            _validate_geojson_geometry(member)
        return geometry_type

    if "coordinates" not in geometry:
        raise RteOdreDownloadError(
            f"GeoJSON {geometry_type} geometry must contain coordinates"
        )
    depth_by_type = {
        "Point": 0,
        "MultiPoint": 1,
        "LineString": 1,
        "MultiLineString": 2,
        "Polygon": 2,
        "MultiPolygon": 3,
    }
    _validate_nested_coordinates(
        geometry["coordinates"],
        depth=depth_by_type[geometry_type],
        geometry_type=geometry_type,
    )
    return geometry_type
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_metadata_from_dict`

**Exact signature**

```python
def _metadata_from_dict(payload: Any) -> RteOdreDatasetMetadata:
```

**Purpose**

Private `grid/source` helper for metadata from dict; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `RteOdreDatasetMetadata`.
- Every observed return expression is reproduced without truncation:
```python
RteOdreDatasetMetadata(dataset_id=str(payload['dataset_id']), title=optional_values['title'], publisher=optional_values['publisher'], modified=optional_values['modified'], data_processed=optional_values['data_processed'], metadata_processed=optional_values['metadata_processed'], license=optional_values['license'], records_count=records_count, geometry_precision_status=precision_status)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, dict)`.
- Guard with a raise path: `precision_status not in allowed_statuses`.
- Guard with a raise path: `records_count is not None and (not isinstance(records_count, int) or isinstance(records_count, bool))`.
- Guard with a raise path: `value is not None and (not isinstance(value, str))`.
- Explicit raise expressions: `TypeError('Invalid cached records count')`, `TypeError('Missing cached dataset metadata')`, `TypeError(f'Invalid cached metadata value: {field_name}')`, `ValueError('Invalid cached geometry precision status')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `optional_values[field_name]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `_metadata_from_dict`.

**Complete source-ordered implementation**

```python
def _metadata_from_dict(payload: Any) -> RteOdreDatasetMetadata:
    if not isinstance(payload, dict):
        raise TypeError("Missing cached dataset metadata")
    precision_status = payload["geometry_precision_status"]
    allowed_statuses = {
        "EXACT_NOT_CLAIMED",
        "GENERALIZED_OR_RESTRICTED",
        "MISSING",
        "UNKNOWN",
    }
    if precision_status not in allowed_statuses:
        raise ValueError("Invalid cached geometry precision status")
    records_count = payload["records_count"]
    if records_count is not None and (
        not isinstance(records_count, int) or isinstance(records_count, bool)
    ):
        raise TypeError("Invalid cached records count")
    optional_values: dict[str, str | None] = {}
    for field_name in (
        "title",
        "publisher",
        "modified",
        "data_processed",
        "metadata_processed",
        "license",
    ):
        value = payload[field_name]
        if value is not None and not isinstance(value, str):
            raise TypeError(f"Invalid cached metadata value: {field_name}")
        optional_values[field_name] = value
    return RteOdreDatasetMetadata(
        dataset_id=str(payload["dataset_id"]),
        title=optional_values["title"],
        publisher=optional_values["publisher"],
        modified=optional_values["modified"],
        data_processed=optional_values["data_processed"],
        metadata_processed=optional_values["metadata_processed"],
        license=optional_values["license"],
        records_count=records_count,
        geometry_precision_status=precision_status,
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_export_summary_from_dict`

**Exact signature**

```python
def _export_summary_from_dict(payload: Any) -> RteOdreExportSummary:
```

**Purpose**

Private `grid/source` helper for export summary from dict; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `RteOdreExportSummary`.
- Every observed return expression is reproduced without truncation:
```python
RteOdreExportSummary(feature_count=payload['feature_count'], null_geometry_count=payload['null_geometry_count'], non_null_geometry_count=payload['non_null_geometry_count'], geometry_types=tuple(geometry_types))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, dict)`.
- Guard with a raise path: `not isinstance(geometry_types, list) or any((not isinstance(value, str) for value in geometry_types))`.
- Explicit raise expressions: `TypeError('Invalid cached geometry types')`, `TypeError('Missing cached export summary')`.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `_export_summary_from_dict`.

**Complete source-ordered implementation**

```python
def _export_summary_from_dict(payload: Any) -> RteOdreExportSummary:
    if not isinstance(payload, dict):
        raise TypeError("Missing cached export summary")
    geometry_types = payload["geometry_types"]
    if not isinstance(geometry_types, list) or any(
        not isinstance(value, str) for value in geometry_types
    ):
        raise TypeError("Invalid cached geometry types")
    return RteOdreExportSummary(
        feature_count=payload["feature_count"],
        null_geometry_count=payload["null_geometry_count"],
        non_null_geometry_count=payload["non_null_geometry_count"],
        geometry_types=tuple(geometry_types),
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_records_count`

**Exact signature**

```python
def _validate_records_count(
    dataset_metadata: RteOdreDatasetMetadata,
    export_summary: RteOdreExportSummary,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent records count; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `records_count is not None and records_count != export_summary.feature_count`.
- Explicit raise expressions: `RteOdreDownloadError(f'RTE/ODRE metadata records_count does not match export feature_count: {records_count} != {export_summary.feature_count}')`.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `_validate_records_count`.
- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_validate_records_count`.

**Complete source-ordered implementation**

```python
def _validate_records_count(
    dataset_metadata: RteOdreDatasetMetadata,
    export_summary: RteOdreExportSummary,
) -> None:
    records_count = dataset_metadata.records_count
    if records_count is not None and records_count != export_summary.feature_count:
        raise RteOdreDownloadError(
            "RTE/ODRE metadata records_count does not match export feature_count: "
            f"{records_count} != {export_summary.feature_count}"
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_replace_file`

**Exact signature**

```python
def _replace_file(source: Path, target: Path) -> None:
```

**Purpose**

Private `grid/source` helper for replace file; its complete implementation below is the authoritative behavioral contract.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_publish_cache_pair` via `_replace_file`.

**Complete source-ordered implementation**

```python
def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_require_no_cache_recovery_material` via `_is_link_or_junction`.
- direct call: `src/landscout/sources/rte_odre_fr.py::_prepare_temporary_cache_file` via `_is_link_or_junction`.

**Complete source-ordered implementation**

```python
def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_cache_recovery_paths`

**Exact signature**

```python
def _cache_recovery_paths(
    archive_path: Path,
    metadata_path: Path,
) -> tuple[Path, Path]:
```

**Purpose**

Private `grid/source` helper for cache recovery paths; its complete implementation below is the authoritative behavioral contract.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_require_no_cache_recovery_material` via `_cache_recovery_paths`.
- direct call: `src/landscout/sources/rte_odre_fr.py::_publish_cache_pair` via `_cache_recovery_paths`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_require_no_cache_recovery_material`

**Exact signature**

```python
def _require_no_cache_recovery_material(
    archive_path: Path,
    metadata_path: Path,
) -> None:
```

**Purpose**

Private `grid/source` helper for require no cache recovery material; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `any((path.exists() or _is_link_or_junction(path) for path in _cache_recovery_paths(archive_path, metadata_path)))`.
- Explicit raise expressions: `RteOdreDownloadError('RTE/ODRE cache recovery backup already exists; manual recovery is required')`.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::_publish_cache_pair` via `_require_no_cache_recovery_material`.
- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_require_no_cache_recovery_material`.

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
        raise RteOdreDownloadError(
            "RTE/ODRE cache recovery backup already exists; manual recovery is required"
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_prepare_temporary_cache_file`

**Exact signature**

```python
def _prepare_temporary_cache_file(path: Path) -> None:
```

**Purpose**

Private `grid/source` helper for prepare temporary cache file; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `_is_link_or_junction(path)`.
- Guard with a raise path: `path.exists()`.
- Guard with a raise path: `not path.is_file()`.
- Explicit raise expressions: `RteOdreDownloadError('RTE/ODRE cache temporary path cannot be prepared safely')`, `RteOdreDownloadError('RTE/ODRE cache temporary path is a link or junction')`, `RteOdreDownloadError('RTE/ODRE cache temporary path is not a regular file')`, `re-raise`.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_prepare_temporary_cache_file`.

**Complete source-ordered implementation**

```python
def _prepare_temporary_cache_file(path: Path) -> None:
    try:
        if _is_link_or_junction(path):
            raise RteOdreDownloadError(
                "RTE/ODRE cache temporary path is a link or junction"
            )
        if path.exists():
            if not path.is_file():
                raise RteOdreDownloadError(
                    "RTE/ODRE cache temporary path is not a regular file"
                )
            path.unlink()
    except RteOdreDownloadError:
        raise
    except OSError as error:
        raise RteOdreDownloadError(
            "RTE/ODRE cache temporary path cannot be prepared safely"
        ) from error
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_cleanup_temporary_cache_files`

**Exact signature**

```python
def _cleanup_temporary_cache_files(
    paths: tuple[Path, ...],
    primary_error: BaseException | None,
) -> None:
```

**Purpose**

Private `grid/source` helper for cleanup temporary cache files; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `cleanup_error is not None and primary_error is None`.
- Explicit raise expressions: `RteOdreDownloadError('RTE/ODRE cache temporary files could not be cleaned safely')`.

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

- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_cleanup_temporary_cache_files`.

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
        raise RteOdreDownloadError(
            "RTE/ODRE cache temporary files could not be cleaned safely"
        ) from cleanup_error
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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

Private `grid/source` helper for publish cache pair; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `RteOdreDownloadError('RTE/ODRE cache publication and rollback both failed')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `archive_path.is_file`, `metadata_path.is_file`.
- Filesystem write: `archive_backup.unlink`, `archive_path.unlink`, `metadata_backup.unlink`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_publish_cache_pair`.

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

    archive_published = False
    try:
        _replace_file(temporary_archive, archive_path)
        archive_published = True
        _replace_file(temporary_metadata, metadata_path)
    except OSError:
        try:
            if archive_published:
                if archive_existed:
                    _replace_file(archive_backup, archive_path)
                else:
                    archive_path.unlink(missing_ok=True)
        except OSError as rollback_error:
            raise RteOdreDownloadError(
                "RTE/ODRE cache publication and rollback both failed"
            ) from rollback_error
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise
    else:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_load_cached_download`

**Exact signature**

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

Reads and validates cached download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `RteOdreDownload | None`.
- Every observed return expression is reproduced without truncation:
```python
None

RteOdreDownload(logical_name=logical_name, dataset_id=dataset.dataset_id, provider=config.provider, portal=config.portal, source_url=source_url, export_format=dataset.preferred_format, download_timestamp=download_timestamp, filename=archive_path.name, file_size=file_size, sha256=checksum, path=archive_path, cache_hit=True, dataset_metadata=dataset_metadata, export_summary=cached_summary)

None

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

- direct call: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_load_cached_download`.

**Complete source-ordered implementation**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    source_url: str,
) -> RteOdreDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    dataset = _get_dataset_config(config, logical_name)
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        if not isinstance(metadata, dict):
            return None
        fresh_summary = _validate_geojson(archive_path)
        file_size = archive_path.stat().st_size
        checksum = _sha256(archive_path)
        download_timestamp = str(metadata["download_timestamp"])
        downloaded_at = datetime.fromisoformat(download_timestamp)
        if downloaded_at.tzinfo is None:
            return None
        age_seconds = (
            datetime.now(UTC) - downloaded_at.astimezone(UTC)
        ).total_seconds()
        valid = (
            0 <= age_seconds <= config.cache.max_age_hours * 3600
            and metadata["logical_name"] == logical_name
            and metadata["dataset_id"] == dataset.dataset_id
            and metadata["provider"] == config.provider
            and metadata["portal"] == config.portal
            and metadata["source_url"] == source_url
            and metadata["export_format"] == dataset.preferred_format
            and metadata["filename"] == archive_path.name
            and metadata["file_size"] == file_size
            and metadata["sha256"] == checksum
        )
        if not valid:
            return None
        dataset_metadata = _metadata_from_dict(metadata["dataset_metadata"])
        cached_summary = _export_summary_from_dict(metadata["export_summary"])
        if dataset_metadata.dataset_id != dataset.dataset_id:
            return None
        if fresh_summary != cached_summary:
            return None
        _validate_records_count(dataset_metadata, cached_summary)
        return RteOdreDownload(
            logical_name=logical_name,
            dataset_id=dataset.dataset_id,
            provider=config.provider,
            portal=config.portal,
            source_url=source_url,
            export_format=dataset.preferred_format,
            download_timestamp=download_timestamp,
            filename=archive_path.name,
            file_size=file_size,
            sha256=checksum,
            path=archive_path,
            cache_hit=True,
            dataset_metadata=dataset_metadata,
            export_summary=cached_summary,
        )
    except (
        KeyError,
        OSError,
        TypeError,
        ValueError,
        json.JSONDecodeError,
        RteOdreDownloadError,
    ):
        return None
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `download_rte_odre_dataset`

**Exact signature**

```python
def download_rte_odre_dataset(
    logical_name: LogicalDatasetName,
    config: RteOdreSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
) -> RteOdreDownload:
```

**Purpose**

Acquires, verifies, and records rte odre dataset; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `RteOdreDownload`.
- Every observed return expression is reproduced without truncation:
```python
cached

result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `RteOdreDownloadError('RTE/ODRE cache paths cannot be prepared safely')`, `RteOdreDownloadError(f'RTE/ODRE download failed: {source_url}')`, `re-raise`.

**Side effects**

- Network I/O: `open_safe_https`.
- Filesystem read: `temporary_archive.open`, `temporary_archive.stat`, `temporary_metadata.open`.
- Filesystem write: `cache_dir.mkdir`, `copyfileobj`.
- CRS/geometry calculation: none.
- Hashing: `_sha256`.
- Environment/process effects: none.
- In-memory mutation: `lineage`.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- import: `tests/unit/test_rte_odre_fr.py::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_successful_download` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_metadata_export_record_count_mismatch_is_rejected` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_unavailable_metadata_record_count_is_accepted` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_negative_source_record_count_is_rejected` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_fresh_cache_is_reused` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_expired_cache_is_refreshed` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_http_failure_raises_and_cleans_temporary_files` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_failed_refresh_preserves_previous_valid_cache` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_corrupted_refresh_preserves_previous_valid_cache` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_invalid_geojson_download_is_rejected` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_null_feature_geometries_are_accepted` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_lineage_sidecar_records_integrity` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_invalid_cached_record_count_invalidates_cache` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_cached_export_summary_mismatch_invalidates_cache` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_corrupted_cached_export_triggers_refresh` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `download_rte_odre_dataset`.
- direct call: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_rte_odre_dataset`.

**Complete source-ordered implementation**

```python
def download_rte_odre_dataset(
    logical_name: LogicalDatasetName,
    config: RteOdreSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
) -> RteOdreDownload:
    validated_config = _validated_source_config(config)
    dataset = _get_dataset_config(validated_config, logical_name)
    export_format = quote(dataset.preferred_format, safe="")
    source_url = _dataset_api_url(
        validated_config, logical_name, f"/exports/{export_format}"
    )
    filename = f"{dataset.dataset_id}.{dataset.preferred_format}"
    archive_path = cache_dir / filename
    metadata_path = cache_dir / f"{filename}.metadata.json"
    _require_no_cache_recovery_material(archive_path, metadata_path)
    cached = _load_cached_download(
        archive_path,
        metadata_path,
        validated_config,
        logical_name,
        source_url,
    )
    if cached is not None:
        return cached

    temporary_archive = archive_path.with_suffix(f"{archive_path.suffix}.part")
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        _prepare_temporary_cache_file(temporary_archive)
        _prepare_temporary_cache_file(temporary_metadata)
    except RteOdreDownloadError:
        raise
    except OSError as error:
        raise RteOdreDownloadError(
            "RTE/ODRE cache paths cannot be prepared safely"
        ) from error
    try:
        dataset_metadata = fetch_rte_odre_dataset_metadata(
            validated_config, logical_name, timeout=timeout
        )
        with (
            open_safe_https(
                source_url,
                timeout=timeout,
                headers={"User-Agent": "LandScout-AI/0.1"},
            ) as response,
            temporary_archive.open("xb") as output,
        ):
            copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)
        summary = _validate_geojson(temporary_archive)
        _validate_records_count(dataset_metadata, summary)
        if summary.feature_count > 0 and summary.non_null_geometry_count == 0:
            dataset_metadata = replace(
                dataset_metadata, geometry_precision_status="MISSING"
            )

        result = RteOdreDownload(
            logical_name=logical_name,
            dataset_id=dataset.dataset_id,
            provider=validated_config.provider,
            portal=validated_config.portal,
            source_url=source_url,
            export_format=dataset.preferred_format,
            download_timestamp=datetime.now(UTC).isoformat(),
            filename=filename,
            file_size=temporary_archive.stat().st_size,
            sha256=_sha256(temporary_archive),
            path=archive_path,
            cache_hit=False,
            dataset_metadata=dataset_metadata,
            export_summary=summary,
        )
        lineage = asdict(result)
        lineage.pop("path")
        lineage.pop("cache_hit")
        with temporary_metadata.open("x", encoding="utf-8") as output:
            output.write(json.dumps(lineage, indent=2, sort_keys=True) + "\n")
        _publish_cache_pair(
            temporary_archive, temporary_metadata, archive_path, metadata_path
        )
        return result
    except RteOdreDownloadError:
        raise
    except (HTTPError, URLError, OSError) as error:
        raise RteOdreDownloadError(f"RTE/ODRE download failed: {source_url}") from error
    finally:
        _cleanup_temporary_cache_files(
            (temporary_archive, temporary_metadata),
            sys.exception(),
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.


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

- Configured source identity: frozen/revalidated official ODRÉ API origin/path and exact logical dataset IDs/export format.
- URL/safe transport: metadata/export URLs are config-built and use open_safe_https.
- Physical bytes/cache: GeoJSON and strict sidecar are size/SHA/source/summary/count validated; recovery material fails before network.
- Archive/extraction/layer: no archive extraction; the GeoJSON dataset is the physical payload and recursive geometry structure is validated.
- Result/later revalidation: immutable metadata/download/export summaries bind the payload; downstream consumers must use those envelopes rather than textual provider fields alone.

## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the grid/source flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
