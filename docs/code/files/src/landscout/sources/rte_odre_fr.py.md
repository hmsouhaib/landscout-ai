# `src/landscout/sources/rte_odre_fr.py`

## File identity

- Repository path: `src/landscout/sources/rte_odre_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: official source acquisition and physical authority
- Responsibility: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.
- Source SHA256: `0954d4025b779a7fa75813edb81c8f3b3227243da6b22b2066a0443762927c0e`

## 1. STEP 7F.1A.4 contract delta

- Moves RTE/ODRE configuration, source GeoJSON, and cache metadata to shared strict serialization and strict finite numeric/source-identity validation.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

The file belongs to the **source adapter** layer and **official source acquisition and physical authority** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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
- `from typing import Annotated, Any, Literal, cast`
- `from urllib.error import HTTPError, URLError`
- `from urllib.parse import quote, urlsplit`

### Third-party packages

- `from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
)`
- `from pydantic_core import PydanticCustomError`

### Internal LandScout imports

- `from landscout.common.safe_http import open_safe_https`
- `from landscout.common.strict_json import StrictJsonError, loads_strict_json_object`
- `from landscout.common.strict_yaml import loads_strict_yaml`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `DEFAULT_CONFIG_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEFAULT_CONFIG_PATH = Path("configs/sources/rte_odre_fr.yaml")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DEFAULT_CACHE_DIR`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEFAULT_CACHE_DIR = Path("data/cache/rte_odre")
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

### `LOGICAL_DATASET_NAMES`

- Category: module constant or closed domain.
- Exact declaration:

```python
LOGICAL_DATASET_NAMES = ("sites", "overhead_lines", "underground_lines")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `sites`
  - `overhead_lines`
  - `underground_lines`

### `COORDINATE_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `GEOJSON_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
GEOJSON_GEOMETRY_TYPES = COORDINATE_GEOMETRY_TYPES | {"GeometryCollection"}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `LogicalDatasetName`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
LogicalDatasetName = Literal["sites", "overhead_lines", "underground_lines"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ExportFormat`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
ExportFormat = Literal["geojson"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `GeometryPrecisionStatus`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
GeometryPrecisionStatus = Literal[
    "EXACT_NOT_CLAIMED",
    "GENERALIZED_OR_RESTRICTED",
    "MISSING",
    "UNKNOWN",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `NonEmptyString`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DatasetIdentifier`

- Category: type alias or closed annotated domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `StrictNonNegativeFloat`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
StrictNonNegativeFloat = Annotated[
    float,
    BeforeValidator(_strict_nonnegative_finite_number),
    Field(ge=0, allow_inf_nan=False),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `RteDatasetConfig`

**Source purpose:** Defines `RteDatasetConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `dataset_id` | `DatasetIdentifier` | `required` | `dataset_id: DatasetIdentifier` |
| `preferred_format` | `ExportFormat` | `required` | `preferred_format: ExportFormat` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- value/type reference: `landscout.sources.rte_odre_fr::_get_dataset_config` via `RteDatasetConfig`

**Exact class source**

```python
class RteDatasetConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    dataset_id: DatasetIdentifier
    preferred_format: ExportFormat
```

### `RteDatasetsConfig`

**Source purpose:** Defines `RteDatasetsConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `sites` | `RteDatasetConfig` | `required` | `sites: RteDatasetConfig` |
| `overhead_lines` | `RteDatasetConfig` | `required` | `overhead_lines: RteDatasetConfig` |
| `underground_lines` | `RteDatasetConfig` | `required` | `underground_lines: RteDatasetConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class RteDatasetsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    sites: RteDatasetConfig
    overhead_lines: RteDatasetConfig
    underground_lines: RteDatasetConfig
```

### `RteOdreApiConfig`

**Source purpose:** Defines `RteOdreApiConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `base_url` | `HttpUrl` | `required` | `base_url: HttpUrl` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class RteOdreApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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

**Source purpose:** Defines `RteOdreCacheConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `max_age_hours` | `StrictNonNegativeFloat` | `required` | `max_age_hours: StrictNonNegativeFloat` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class RteOdreCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    max_age_hours: StrictNonNegativeFloat
```

### `RteOdreSourceConfig`

**Source purpose:** Defines `RteOdreSourceConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `provider` | `Literal['RTE']` | `required` | `provider: Literal["RTE"]` |
| `portal` | `Literal['ODRE']` | `required` | `portal: Literal["ODRE"]` |
| `api` | `RteOdreApiConfig` | `required` | `api: RteOdreApiConfig` |
| `datasets` | `RteDatasetsConfig` | `required` | `datasets: RteDatasetsConfig` |
| `cache` | `RteOdreCacheConfig` | `required` | `cache: RteOdreCacheConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- value/type reference: `landscout.sources.rte_odre_fr::load_rte_odre_source_config` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::_validated_source_config` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::_get_dataset_config` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::_dataset_api_url` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::build_rte_odre_metadata_url` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::build_rte_odre_export_url` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `RteOdreSourceConfig`
- import: `tests.unit.test_rte_odre_fr::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- value/type reference: `tests.unit.test_rte_odre_fr::source_config` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_valid_source_config_loads` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_loaded_source_config_is_immutable` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_source_identity_is_exact` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cache_age_is_a_strict_finite_number` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_missing_dataset_id_fails` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_empty_base_url_fails` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_api_base_is_pinned_to_the_official_https_origin_and_path` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_cache_age_fails` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unsupported_export_format_fails` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_build_export_url` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_build_metadata_url` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_export_url_uses_configured_dataset_id` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_is_captured_without_fabrication` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_successful_download` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_broken_recovery_symlink_rejects_rte_before_network` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `RteOdreSourceConfig`

**Exact class source**

```python
class RteOdreSourceConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: Literal["RTE"]
    portal: Literal["ODRE"]
    api: RteOdreApiConfig
    datasets: RteDatasetsConfig
    cache: RteOdreCacheConfig
```

### `RteOdreDownloadError`

**Source purpose:** Raised when RTE/ODRE metadata or exports cannot be retrieved safely.

- Exact decorators: none.
- Exact bases: `RuntimeError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- constructor call: `landscout.sources.rte_odre_fr::_validated_source_config` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_validated_source_config` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_read_response_json` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_read_response_json` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_validate_geojson` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_geojson` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_validate_position` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_position` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_validate_nested_coordinates` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_nested_coordinates` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_validate_geojson_geometry` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_geojson_geometry` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_validate_records_count` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_records_count` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_require_no_cache_recovery_material` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_require_no_cache_recovery_material` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_prepare_temporary_cache_file` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_prepare_temporary_cache_file` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_cleanup_temporary_cache_files` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_cleanup_temporary_cache_files` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::_publish_cache_pair` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_publish_cache_pair` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `RteOdreDownloadError`
- constructor call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `RteOdreDownloadError`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `RteOdreDownloadError`
- import: `tests.unit.test_rte_odre_fr::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- value/type reference: `tests.unit.test_rte_odre_fr::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_geojson_export_rejects_duplicate_json_keys` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_malformed_geojson_feature_or_geometry_is_rejected` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_point_requires_a_finite_numeric_position` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_nested_coordinate_geometries_reject_obvious_invalid_structure` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_geometry_collection_members_are_validated_recursively` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_broken_recovery_symlink_rejects_rte_before_network` via `RteOdreDownloadError`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `RteOdreDownloadError`

**Exact class source**

```python
class RteOdreDownloadError(RuntimeError):
    """Raised when RTE/ODRE metadata or exports cannot be retrieved safely."""
```

### `RteOdreDatasetMetadata`

**Source purpose:** Defines `RteOdreDatasetMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `dataset_id` | `str` | `required` | `dataset_id: str` |
| `title` | `str \| None` | `required` | `title: str \| None` |
| `publisher` | `str \| None` | `required` | `publisher: str \| None` |
| `modified` | `str \| None` | `required` | `modified: str \| None` |
| `data_processed` | `str \| None` | `required` | `data_processed: str \| None` |
| `metadata_processed` | `str \| None` | `required` | `metadata_processed: str \| None` |
| `license` | `str \| None` | `required` | `license: str \| None` |
| `records_count` | `int \| None` | `required` | `records_count: int \| None` |
| `geometry_precision_status` | `GeometryPrecisionStatus` | `required` | `geometry_precision_status: GeometryPrecisionStatus` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- constructor call: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `RteOdreDatasetMetadata`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `RteOdreDatasetMetadata`
- constructor call: `landscout.sources.rte_odre_fr::_metadata_from_dict` via `RteOdreDatasetMetadata`
- value/type reference: `landscout.sources.rte_odre_fr::_metadata_from_dict` via `RteOdreDatasetMetadata`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_records_count` via `RteOdreDatasetMetadata`

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

**Source purpose:** Defines `RteOdreExportSummary`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `feature_count` | `int` | `required` | `feature_count: int` |
| `null_geometry_count` | `int` | `required` | `null_geometry_count: int` |
| `non_null_geometry_count` | `int` | `required` | `non_null_geometry_count: int` |
| `geometry_types` | `tuple[str, ...]` | `required` | `geometry_types: tuple[str, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- constructor call: `landscout.sources.rte_odre_fr::_validate_geojson` via `RteOdreExportSummary`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_geojson` via `RteOdreExportSummary`
- constructor call: `landscout.sources.rte_odre_fr::_export_summary_from_dict` via `RteOdreExportSummary`
- value/type reference: `landscout.sources.rte_odre_fr::_export_summary_from_dict` via `RteOdreExportSummary`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_records_count` via `RteOdreExportSummary`
- import: `tests.unit.test_rte_odre_fr::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- constructor call: `tests.unit.test_rte_odre_fr::test_successful_download` via `RteOdreExportSummary`
- value/type reference: `tests.unit.test_rte_odre_fr::test_successful_download` via `RteOdreExportSummary`
- constructor call: `tests.unit.test_rte_odre_fr::test_export_summary_rejects_invalid_geometry_counts` via `RteOdreExportSummary`
- value/type reference: `tests.unit.test_rte_odre_fr::test_export_summary_rejects_invalid_geometry_counts` via `RteOdreExportSummary`
- constructor call: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `RteOdreExportSummary`
- value/type reference: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `RteOdreExportSummary`

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
        if (
            self.null_geometry_count + self.non_null_geometry_count
            != self.feature_count
        ):
            raise ValueError("Geometry counts must add up to feature_count")
        if not isinstance(self.geometry_types, tuple) or any(
            not isinstance(value, str) or not value for value in self.geometry_types
        ):
            raise TypeError("geometry_types must be a tuple of non-empty strings")
```

### `RteOdreDownload`

**Source purpose:** Defines `RteOdreDownload`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `logical_name` | `LogicalDatasetName` | `required` | `logical_name: LogicalDatasetName` |
| `dataset_id` | `str` | `required` | `dataset_id: str` |
| `provider` | `str` | `required` | `provider: str` |
| `portal` | `str` | `required` | `portal: str` |
| `source_url` | `str` | `required` | `source_url: str` |
| `export_format` | `ExportFormat` | `required` | `export_format: ExportFormat` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `filename` | `str` | `required` | `filename: str` |
| `file_size` | `int` | `required` | `file_size: int` |
| `sha256` | `str` | `required` | `sha256: str` |
| `path` | `Path` | `required` | `path: Path` |
| `cache_hit` | `bool` | `required` | `cache_hit: bool` |
| `dataset_metadata` | `RteOdreDatasetMetadata` | `required` | `dataset_metadata: RteOdreDatasetMetadata` |
| `export_summary` | `RteOdreExportSummary` | `required` | `export_summary: RteOdreExportSummary` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- constructor call: `landscout.sources.rte_odre_fr::_load_cached_download` via `RteOdreDownload`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `RteOdreDownload`
- constructor call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `RteOdreDownload`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `RteOdreDownload`

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


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_strict_nonnegative_finite_number`

**Purpose:** Implements `strict nonnegative finite number` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _strict_nonnegative_finite_number(value: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `PydanticCustomError(<br>            "strict_number",<br>            "value must be a strict finite non-negative number",<br>        )` under lexical guard `isinstance(value, bool) or not isinstance(value, Real)`.
  - `ValueError("value must be a strict finite non-negative number")`.
  - `ValueError("value must be a strict finite non-negative number")` under lexical guard `not isfinite(numeric_value) or value < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PydanticCustomError` | `pydantic_core.PydanticCustomError` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |

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
def _strict_nonnegative_finite_number(value: object) -> object:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise PydanticCustomError(
            "strict_number",
            "value must be a strict finite non-negative number",
        )
    try:
        numeric_value = float(value)
    except (OverflowError, TypeError, ValueError) as error:
        raise ValueError("value must be a strict finite non-negative number") from error
    if not isfinite(numeric_value) or value < 0:
        raise ValueError("value must be a strict finite non-negative number")
    return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `RteOdreApiConfig._official_api_origin`

**Purpose:** Implements `official api origin` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _official_api_origin(cls, value: HttpUrl) -> HttpUrl:
```

- Exact decorators: `field_validator("base_url")`, `classmethod`.
- Declared return annotation: `HttpUrl`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cls` | positional-or-keyword | `None` | `required` |
| `value` | positional-or-keyword | `HttpUrl` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError("RTE/ODRE API must use the exact official HTTPS origin")` under lexical guard `parsed.scheme != "https"<br>            or parsed.hostname != "odre.opendatasoft.com"<br>            or parsed.port not in {None, 443}<br>            or parsed.username is not None<br>            or parsed.password is not None<br>            or parsed.path.rstrip("/") != "/api/explore/v2.1"<br>            or parsed.query<br>            or parsed.fragment`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `urlsplit` | `urllib.parse.urlsplit` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `parsed.path.rstrip` | `unresolved local/third-party receiver; no ownership inferred` |
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `RteOdreDatasetMetadata.__post_init__`

**Purpose:** Implements `post init` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def __post_init__(self) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError("records_count must be a non-negative integer or None")` under lexical guard `self.records_count is not None and (<br>            not isinstance(self.records_count, int)<br>            or isinstance(self.records_count, bool)<br>            or self.records_count < 0<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def __post_init__(self) -> None:
        if self.records_count is not None and (
            not isinstance(self.records_count, int)
            or isinstance(self.records_count, bool)
            or self.records_count < 0
        ):
            raise ValueError("records_count must be a non-negative integer or None")
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `RteOdreExportSummary.__post_init__`

**Purpose:** Implements `post init` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def __post_init__(self) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError(f"{name} must be a non-negative integer")` under lexical guard `not isinstance(value, int) or isinstance(value, bool) or value < 0`.
  - `ValueError("Geometry counts must add up to feature_count")` under lexical guard `self.null_geometry_count + self.non_null_geometry_count<br>            != self.feature_count`.
  - `TypeError("geometry_types must be a tuple of non-empty strings")` under lexical guard `not isinstance(self.geometry_types, tuple) or any(<br>            not isinstance(value, str) or not value for value in self.geometry_types<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `counts.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def __post_init__(self) -> None:
        counts = {
            "feature_count": self.feature_count,
            "null_geometry_count": self.null_geometry_count,
            "non_null_geometry_count": self.non_null_geometry_count,
        }
        for name, value in counts.items():
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError(f"{name} must be a non-negative integer")
        if (
            self.null_geometry_count + self.non_null_geometry_count
            != self.feature_count
        ):
            raise ValueError("Geometry counts must add up to feature_count")
        if not isinstance(self.geometry_types, tuple) or any(
            not isinstance(value, str) or not value for value in self.geometry_types
        ):
            raise TypeError("geometry_types must be a tuple of non-empty strings")
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `load_rte_odre_source_config`

**Purpose:** Implements `load rte odre source config` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def load_rte_odre_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> RteOdreSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `RteOdreSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `DEFAULT_CONFIG_PATH` |

**Return and exception contract**

- Exact observed return expressions:
  - `RteOdreSourceConfig.model_validate(content)`
- Explicit raise paths:
  - `TypeError(f"Expected a YAML mapping in {path}")` under lexical guard `type(content) is not dict`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- import: `tests.unit.test_rte_odre_fr::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- direct call: `tests.unit.test_rte_odre_fr::source_config` via `load_rte_odre_source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::source_config` via `load_rte_odre_source_config`
- direct call: `tests.unit.test_rte_odre_fr::test_source_config_yaml_rejects_duplicate_keys` via `load_rte_odre_source_config`
- value/type reference: `tests.unit.test_rte_odre_fr::test_source_config_yaml_rejects_duplicate_keys` via `load_rte_odre_source_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |

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
def load_rte_odre_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> RteOdreSourceConfig:
    content = loads_strict_yaml(path.read_bytes())
    if type(content) is not dict:
        raise TypeError(f"Expected a YAML mapping in {path}")
    return RteOdreSourceConfig.model_validate(content)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validated_source_config`

**Purpose:** Implements `validated source config` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _validated_source_config(config: object) -> RteOdreSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `RteOdreSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `RteOdreSourceConfig.model_validate(config.model_dump(mode="python"))`
- Explicit raise paths:
  - `TypeError("RTE/ODRE source config type is invalid")` under lexical guard `type(config) is not RteOdreSourceConfig`.
  - `RteOdreDownloadError(<br>            "RTE/ODRE source config no longer satisfies the official origin contract"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::build_rte_odre_metadata_url` via `_validated_source_config`
- value/type reference: `landscout.sources.rte_odre_fr::build_rte_odre_metadata_url` via `_validated_source_config`
- direct call: `landscout.sources.rte_odre_fr::build_rte_odre_export_url` via `_validated_source_config`
- value/type reference: `landscout.sources.rte_odre_fr::build_rte_odre_export_url` via `_validated_source_config`
- direct call: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_validated_source_config`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_validated_source_config`
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_validated_source_config`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_validated_source_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreSourceConfig.model_validate` | `landscout.sources.rte_odre_fr.RteOdreSourceConfig.model_validate` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_get_dataset_config`

**Purpose:** Implements `get dataset config` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _get_dataset_config(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> RteDatasetConfig:
```

- Exact decorators: none.
- Declared return annotation: `RteDatasetConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `logical_name` | positional-or-keyword | `LogicalDatasetName` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `getattr(config.datasets, logical_name)`
- Explicit raise paths:
  - `ValueError(f"Unsupported RTE/ODRE logical dataset: {logical_name}")` under lexical guard `logical_name not in LOGICAL_DATASET_NAMES`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::_dataset_api_url` via `_get_dataset_config`
- value/type reference: `landscout.sources.rte_odre_fr::_dataset_api_url` via `_get_dataset_config`
- direct call: `landscout.sources.rte_odre_fr::build_rte_odre_export_url` via `_get_dataset_config`
- value/type reference: `landscout.sources.rte_odre_fr::build_rte_odre_export_url` via `_get_dataset_config`
- direct call: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_get_dataset_config`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_get_dataset_config`
- direct call: `landscout.sources.rte_odre_fr::_load_cached_download` via `_get_dataset_config`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `_get_dataset_config`
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_get_dataset_config`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_get_dataset_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _get_dataset_config(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> RteDatasetConfig:
    if logical_name not in LOGICAL_DATASET_NAMES:
        raise ValueError(f"Unsupported RTE/ODRE logical dataset: {logical_name}")
    return getattr(config.datasets, logical_name)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_dataset_api_url`

**Purpose:** Implements `dataset api url` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _dataset_api_url(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    suffix: str,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `logical_name` | positional-or-keyword | `LogicalDatasetName` | `required` |
| `suffix` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `f"{str(config.api.base_url).rstrip('/')}/catalog/datasets/"<br>        f"{encoded_dataset_id}{suffix}"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::build_rte_odre_metadata_url` via `_dataset_api_url`
- value/type reference: `landscout.sources.rte_odre_fr::build_rte_odre_metadata_url` via `_dataset_api_url`
- direct call: `landscout.sources.rte_odre_fr::build_rte_odre_export_url` via `_dataset_api_url`
- value/type reference: `landscout.sources.rte_odre_fr::build_rte_odre_export_url` via `_dataset_api_url`
- direct call: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_dataset_api_url`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_dataset_api_url`
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_dataset_api_url`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_dataset_api_url`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_get_dataset_config` | `landscout.sources.rte_odre_fr._get_dataset_config` |
| `quote` | `urllib.parse.quote` |
| `str(config.api.base_url).rstrip` | `unresolved local/third-party receiver; no ownership inferred` |
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `build_rte_odre_metadata_url`

**Purpose:** Implements `build rte odre metadata url` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def build_rte_odre_metadata_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `logical_name` | positional-or-keyword | `LogicalDatasetName` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_dataset_api_url(validated_config, logical_name, "")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- import: `tests.unit.test_rte_odre_fr::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- direct call: `tests.unit.test_rte_odre_fr::test_build_metadata_url` via `build_rte_odre_metadata_url`
- value/type reference: `tests.unit.test_rte_odre_fr::test_build_metadata_url` via `build_rte_odre_metadata_url`
- direct call: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `build_rte_odre_metadata_url`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `build_rte_odre_metadata_url`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.rte_odre_fr._validated_source_config` |
| `_dataset_api_url` | `landscout.sources.rte_odre_fr._dataset_api_url` |

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
def build_rte_odre_metadata_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
    validated_config = _validated_source_config(config)
    return _dataset_api_url(validated_config, logical_name, "")
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `build_rte_odre_export_url`

**Purpose:** Implements `build rte odre export url` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def build_rte_odre_export_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `logical_name` | positional-or-keyword | `LogicalDatasetName` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_dataset_api_url(validated_config, logical_name, f"/exports/{export_format}")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- import: `tests.unit.test_rte_odre_fr::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- direct call: `tests.unit.test_rte_odre_fr::test_build_export_url` via `build_rte_odre_export_url`
- value/type reference: `tests.unit.test_rte_odre_fr::test_build_export_url` via `build_rte_odre_export_url`
- direct call: `tests.unit.test_rte_odre_fr::test_export_url_uses_configured_dataset_id` via `build_rte_odre_export_url`
- value/type reference: `tests.unit.test_rte_odre_fr::test_export_url_uses_configured_dataset_id` via `build_rte_odre_export_url`
- direct call: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `build_rte_odre_export_url`
- value/type reference: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `build_rte_odre_export_url`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.rte_odre_fr._validated_source_config` |
| `_get_dataset_config` | `landscout.sources.rte_odre_fr._get_dataset_config` |
| `quote` | `urllib.parse.quote` |
| `_dataset_api_url` | `landscout.sources.rte_odre_fr._dataset_api_url` |

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
def build_rte_odre_export_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
    validated_config = _validated_source_config(config)
    dataset = _get_dataset_config(validated_config, logical_name)
    export_format = quote(dataset.preferred_format, safe="")
    return _dataset_api_url(validated_config, logical_name, f"/exports/{export_format}")
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_optional_string`

**Purpose:** Implements `optional string` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _optional_string(mapping: dict[str, Any], key: str) -> str | None:
```

- Exact decorators: none.
- Declared return annotation: `str | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mapping` | positional-or-keyword | `dict[str, Any]` | `required` |
| `key` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `normalized or None`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_optional_string`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_optional_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `mapping.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _optional_string(mapping: dict[str, Any], key: str) -> str | None:
    value = mapping.get(key)
    if not isinstance(value, str):
        return None
    normalized = value.strip()
    return normalized or None
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_metadata_precision_status`

**Purpose:** Implements `metadata precision status` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _metadata_precision_status(description: str | None) -> GeometryPrecisionStatus:
```

- Exact decorators: none.
- Declared return annotation: `GeometryPrecisionStatus`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `description` | positional-or-keyword | `str \| None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `"UNKNOWN"`
  - `"GENERALIZED_OR_RESTRICTED"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_metadata_precision_status`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_metadata_precision_status`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `description.casefold` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _metadata_precision_status(description: str | None) -> GeometryPrecisionStatus:
    if description is None:
        return "UNKNOWN"
    normalized = description.casefold()
    if "données gps" in normalized and "sécurité publique" in normalized:
        return "GENERALIZED_OR_RESTRICTED"
    return "UNKNOWN"
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_read_response_json`

**Purpose:** Implements `read response json` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _read_response_json(source_url: str, timeout: float) -> dict[str, Any]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, Any]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_url` | positional-or-keyword | `str` | `required` |
| `timeout` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `payload`
- Explicit raise paths:
  - `RteOdreDownloadError(f"RTE/ODRE request failed: {source_url}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_read_response_json`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `_read_response_json`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `response.read` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _read_response_json(source_url: str, timeout: float) -> dict[str, Any]:
    try:
        with open_safe_https(
            source_url,
            timeout=timeout,
            headers={"User-Agent": "LandScout-AI/0.1"},
        ) as response:
            payload = loads_strict_json_object(response.read())
    except (HTTPError, URLError, OSError, StrictJsonError) as error:
        raise RteOdreDownloadError(f"RTE/ODRE request failed: {source_url}") from error
    return payload
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `fetch_rte_odre_dataset_metadata`

**Purpose:** Implements `fetch rte odre dataset metadata` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def fetch_rte_odre_dataset_metadata(
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    timeout: float = 60.0,
) -> RteOdreDatasetMetadata:
```

- Exact decorators: none.
- Declared return annotation: `RteOdreDatasetMetadata`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `logical_name` | positional-or-keyword | `LogicalDatasetName` | `required` |
| `timeout` | positional-or-keyword | `float` | `60.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `RteOdreDatasetMetadata(<br>        dataset_id=dataset.dataset_id,<br>        title=_optional_string(default_metas, "title"),<br>        publisher=_optional_string(default_metas, "publisher"),<br>        modified=_optional_string(default_metas, "modified"),<br>        data_processed=_optional_string(default_metas, "data_processed"),<br>        metadata_processed=_optional_string(default_metas, "metadata_processed"),<br>        license=_optional_string(default_metas, "license"),<br>        records_count=records_count,<br>        geometry_precision_status=_metadata_precision_status(description),<br>    )`
- Explicit raise paths:
  - `RteOdreDownloadError(<br>            f"Unexpected dataset metadata response for {dataset.dataset_id}"<br>        )` under lexical guard `response_dataset_id != dataset.dataset_id`.
  - `RteOdreDownloadError("RTE/ODRE records_count must be an integer or null")` under lexical guard `records_count_value is None`.
  - `RteOdreDownloadError("RTE/ODRE records_count must not be negative")` under lexical guard `records_count_value is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `fetch_rte_odre_dataset_metadata`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `fetch_rte_odre_dataset_metadata`
- import: `tests.unit.test_rte_odre_fr::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- direct call: `tests.unit.test_rte_odre_fr::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `fetch_rte_odre_dataset_metadata`
- value/type reference: `tests.unit.test_rte_odre_fr::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `fetch_rte_odre_dataset_metadata`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_is_captured_without_fabrication` via `fetch_rte_odre_dataset_metadata`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_is_captured_without_fabrication` via `fetch_rte_odre_dataset_metadata`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `fetch_rte_odre_dataset_metadata`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `fetch_rte_odre_dataset_metadata`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `fetch_rte_odre_dataset_metadata`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `fetch_rte_odre_dataset_metadata`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.rte_odre_fr._validated_source_config` |
| `_get_dataset_config` | `landscout.sources.rte_odre_fr._get_dataset_config` |
| `_dataset_api_url` | `landscout.sources.rte_odre_fr._dataset_api_url` |
| `_read_response_json` | `landscout.sources.rte_odre_fr._read_response_json` |
| `payload.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `metas.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `default_metas.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `_optional_string` | `landscout.sources.rte_odre_fr._optional_string` |
| `RteOdreDatasetMetadata` | `landscout.sources.rte_odre_fr.RteOdreDatasetMetadata` |
| `_metadata_precision_status` | `landscout.sources.rte_odre_fr._metadata_precision_status` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_sha256`

**Purpose:** Implements `sha256` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

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
- direct call: `landscout.sources.rte_odre_fr::_load_cached_download` via `_sha256`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `_sha256`
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_sha256`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_sha256`

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
        for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_geojson`

**Purpose:** Implements `validate geojson` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _validate_geojson(path: Path) -> RteOdreExportSummary:
```

- Exact decorators: none.
- Declared return annotation: `RteOdreExportSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `RteOdreExportSummary(<br>        feature_count=len(features),<br>        null_geometry_count=null_geometry_count,<br>        non_null_geometry_count=len(features) - null_geometry_count,<br>        geometry_types=tuple(sorted(geometry_types)),<br>    )`
- Explicit raise paths:
  - `RteOdreDownloadError(f"GeoJSON export is missing or empty: {path}")` under lexical guard `not path.is_file() or path.stat().st_size == 0`.
  - `RteOdreDownloadError(<br>            f"GeoJSON export is not valid finite UTF-8 JSON: {path}"<br>        )`.
  - `RteOdreDownloadError("GeoJSON export must be a FeatureCollection")` under lexical guard `payload.get("type") != "FeatureCollection"`.
  - `RteOdreDownloadError(<br>            "GeoJSON FeatureCollection must contain a features list"<br>        )` under lexical guard `not isinstance(features, list)`.
  - `RteOdreDownloadError(<br>                "Every GeoJSON feature must be an object with type Feature"<br>            )` under lexical guard `not isinstance(feature, dict) or feature.get("type") != "Feature"`.
  - `RteOdreDownloadError(<br>                "GeoJSON feature geometry must be an object or null"<br>            )` under lexical guard `not isinstance(geometry, dict)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::_load_cached_download` via `_validate_geojson`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `_validate_geojson`
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_validate_geojson`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_validate_geojson`
- direct call: `tests.unit.test_rte_odre_fr::test_geojson_export_rejects_duplicate_json_keys` via `rte_odre_fr._validate_geojson`
- direct call: `tests.unit.test_rte_odre_fr::test_malformed_geojson_feature_or_geometry_is_rejected` via `rte_odre_fr._validate_geojson`
- direct call: `tests.unit.test_rte_odre_fr::test_standard_geojson_geometry_types_are_summarized` via `rte_odre_fr._validate_geojson`
- direct call: `tests.unit.test_rte_odre_fr::test_point_requires_a_finite_numeric_position` via `rte_odre_fr._validate_geojson`
- direct call: `tests.unit.test_rte_odre_fr::test_nested_coordinate_geometries_reject_obvious_invalid_structure` via `rte_odre_fr._validate_geojson`
- direct call: `tests.unit.test_rte_odre_fr::test_geometry_collection_members_are_validated_recursively` via `rte_odre_fr._validate_geojson`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `payload.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `feature.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_geojson_geometry` | `landscout.sources.rte_odre_fr._validate_geojson_geometry` |
| `geometry_types.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreExportSummary` | `landscout.sources.rte_odre_fr.RteOdreExportSummary` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file`<br>`path.stat`<br>`path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_validate_geojson_geometry`<br>`geometry_types.add` |
| External process/environment | None directly present. |
| In-memory mutation | `geometry_types.add(geometry_type)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_geojson(path: Path) -> RteOdreExportSummary:
    if not path.is_file() or path.stat().st_size == 0:
        raise RteOdreDownloadError(f"GeoJSON export is missing or empty: {path}")
    try:
        payload = loads_strict_json_object(path.read_bytes())
    except (OSError, StrictJsonError) as error:
        raise RteOdreDownloadError(
            f"GeoJSON export is not valid finite UTF-8 JSON: {path}"
        ) from error
    if payload.get("type") != "FeatureCollection":
        raise RteOdreDownloadError("GeoJSON export must be a FeatureCollection")
    features = payload.get("features")
    if not isinstance(features, list):
        raise RteOdreDownloadError(
            "GeoJSON FeatureCollection must contain a features list"
        )

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_position`

**Purpose:** Implements `validate position` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _validate_position(value: object, geometry_type: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `geometry_type` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RteOdreDownloadError(<br>            f"GeoJSON {geometry_type} coordinates must contain an X/Y position"<br>        )` under lexical guard `not isinstance(value, list) or len(value) < 2`.
  - `RteOdreDownloadError(<br>            f"GeoJSON {geometry_type} coordinates must be finite numeric values"<br>        )` under lexical guard `any(<br>        isinstance(coordinate, bool)<br>        or not isinstance(coordinate, Real)<br>        or not isfinite(float(coordinate))<br>        for coordinate in value<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::_validate_nested_coordinates` via `_validate_position`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_nested_coordinates` via `_validate_position`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_nested_coordinates`

**Purpose:** Implements `validate nested coordinates` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _validate_nested_coordinates(
    value: object,
    *,
    depth: int,
    geometry_type: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `depth` | keyword-only | `int` | `required` |
| `geometry_type` | keyword-only | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
- Explicit raise paths:
  - `RteOdreDownloadError(<br>            f"GeoJSON {geometry_type} coordinate structure must use JSON arrays"<br>        )` under lexical guard `not isinstance(value, list)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::_validate_nested_coordinates` via `_validate_nested_coordinates`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_nested_coordinates` via `_validate_nested_coordinates`
- direct call: `landscout.sources.rte_odre_fr::_validate_geojson_geometry` via `_validate_nested_coordinates`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_geojson_geometry` via `_validate_nested_coordinates`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |
| `_validate_position` | `landscout.sources.rte_odre_fr._validate_position` |
| `_validate_nested_coordinates` | `landscout.sources.rte_odre_fr._validate_nested_coordinates` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_geojson_geometry`

**Purpose:** Implements `validate geojson geometry` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _validate_geojson_geometry(geometry: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `geometry_type`
- Explicit raise paths:
  - `RteOdreDownloadError("GeoJSON geometry member must be an object")` under lexical guard `not isinstance(geometry, dict)`.
  - `RteOdreDownloadError("GeoJSON feature has an unsupported geometry type")` under lexical guard `geometry_type not in GEOJSON_GEOMETRY_TYPES`.
  - `RteOdreDownloadError(<br>                "GeoJSON GeometryCollection must contain a geometries list"<br>            )` under lexical guard `geometry_type == "GeometryCollection"`.
  - `RteOdreDownloadError(<br>            f"GeoJSON {geometry_type} geometry must contain coordinates"<br>        )` under lexical guard `"coordinates" not in geometry`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::_validate_geojson` via `_validate_geojson_geometry`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_geojson` via `_validate_geojson_geometry`
- direct call: `landscout.sources.rte_odre_fr::_validate_geojson_geometry` via `_validate_geojson_geometry`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_geojson_geometry` via `_validate_geojson_geometry`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |
| `geometry.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_geojson_geometry` | `landscout.sources.rte_odre_fr._validate_geojson_geometry` |
| `_validate_nested_coordinates` | `landscout.sources.rte_odre_fr._validate_nested_coordinates` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.get`<br>`_validate_geojson_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_metadata_from_dict`

**Purpose:** Implements `metadata from dict` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _metadata_from_dict(payload: Any) -> RteOdreDatasetMetadata:
```

- Exact decorators: none.
- Declared return annotation: `RteOdreDatasetMetadata`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `payload` | positional-or-keyword | `Any` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `RteOdreDatasetMetadata(<br>        dataset_id=dataset_id,<br>        title=optional_values["title"],<br>        publisher=optional_values["publisher"],<br>        modified=optional_values["modified"],<br>        data_processed=optional_values["data_processed"],<br>        metadata_processed=optional_values["metadata_processed"],<br>        license=optional_values["license"],<br>        records_count=records_count,<br>        geometry_precision_status=cast(GeometryPrecisionStatus, precision_status),<br>    )`
- Explicit raise paths:
  - `TypeError("Missing cached dataset metadata")` under lexical guard `type(payload) is not dict`.
  - `ValueError("Cached dataset metadata schema differs")` under lexical guard `set(payload) != expected_keys`.
  - `TypeError("Invalid cached dataset ID")` under lexical guard `type(dataset_id) is not str or not dataset_id`.
  - `ValueError("Invalid cached geometry precision status")` under lexical guard `type(precision_status) is not str or precision_status not in allowed_statuses`.
  - `TypeError("Invalid cached records count")` under lexical guard `records_count is not None and (type(records_count) is not int)`.
  - `TypeError(f"Invalid cached metadata value: {field_name}")` under lexical guard `value is not None and type(value) is not str`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::_load_cached_download` via `_metadata_from_dict`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `_metadata_from_dict`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDatasetMetadata` | `landscout.sources.rte_odre_fr.RteOdreDatasetMetadata` |
| `cast` | `typing.cast` |

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
| In-memory mutation | `optional_values[field_name] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _metadata_from_dict(payload: Any) -> RteOdreDatasetMetadata:
    if type(payload) is not dict:
        raise TypeError("Missing cached dataset metadata")
    expected_keys = {
        "dataset_id",
        "title",
        "publisher",
        "modified",
        "data_processed",
        "metadata_processed",
        "license",
        "records_count",
        "geometry_precision_status",
    }
    if set(payload) != expected_keys:
        raise ValueError("Cached dataset metadata schema differs")
    dataset_id = payload["dataset_id"]
    if type(dataset_id) is not str or not dataset_id:
        raise TypeError("Invalid cached dataset ID")
    precision_status = payload["geometry_precision_status"]
    allowed_statuses = {
        "EXACT_NOT_CLAIMED",
        "GENERALIZED_OR_RESTRICTED",
        "MISSING",
        "UNKNOWN",
    }
    if type(precision_status) is not str or precision_status not in allowed_statuses:
        raise ValueError("Invalid cached geometry precision status")
    records_count = payload["records_count"]
    if records_count is not None and (type(records_count) is not int):
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
        if value is not None and type(value) is not str:
            raise TypeError(f"Invalid cached metadata value: {field_name}")
        optional_values[field_name] = value
    return RteOdreDatasetMetadata(
        dataset_id=dataset_id,
        title=optional_values["title"],
        publisher=optional_values["publisher"],
        modified=optional_values["modified"],
        data_processed=optional_values["data_processed"],
        metadata_processed=optional_values["metadata_processed"],
        license=optional_values["license"],
        records_count=records_count,
        geometry_precision_status=cast(GeometryPrecisionStatus, precision_status),
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_export_summary_from_dict`

**Purpose:** Implements `export summary from dict` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _export_summary_from_dict(payload: Any) -> RteOdreExportSummary:
```

- Exact decorators: none.
- Declared return annotation: `RteOdreExportSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `payload` | positional-or-keyword | `Any` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `RteOdreExportSummary(<br>        feature_count=payload["feature_count"],<br>        null_geometry_count=payload["null_geometry_count"],<br>        non_null_geometry_count=payload["non_null_geometry_count"],<br>        geometry_types=tuple(geometry_types),<br>    )`
- Explicit raise paths:
  - `TypeError("Missing cached export summary")` under lexical guard `type(payload) is not dict`.
  - `ValueError("Cached export summary schema differs")` under lexical guard `set(payload) != expected_keys`.
  - `TypeError("Invalid cached geometry types")` under lexical guard `type(geometry_types) is not list or any(<br>        type(value) is not str for value in geometry_types<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::_load_cached_download` via `_export_summary_from_dict`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `_export_summary_from_dict`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreExportSummary` | `landscout.sources.rte_odre_fr.RteOdreExportSummary` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _export_summary_from_dict(payload: Any) -> RteOdreExportSummary:
    if type(payload) is not dict:
        raise TypeError("Missing cached export summary")
    expected_keys = {
        "feature_count",
        "null_geometry_count",
        "non_null_geometry_count",
        "geometry_types",
    }
    if set(payload) != expected_keys:
        raise ValueError("Cached export summary schema differs")
    geometry_types = payload["geometry_types"]
    if type(geometry_types) is not list or any(
        type(value) is not str for value in geometry_types
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_records_count`

**Purpose:** Implements `validate records count` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def _validate_records_count(
    dataset_metadata: RteOdreDatasetMetadata,
    export_summary: RteOdreExportSummary,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `dataset_metadata` | positional-or-keyword | `RteOdreDatasetMetadata` | `required` |
| `export_summary` | positional-or-keyword | `RteOdreExportSummary` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RteOdreDownloadError(<br>            "RTE/ODRE metadata records_count does not match export feature_count: "<br>            f"{records_count} != {export_summary.feature_count}"<br>        )` under lexical guard `records_count is not None and records_count != export_summary.feature_count`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::_load_cached_download` via `_validate_records_count`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `_validate_records_count`
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_validate_records_count`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_validate_records_count`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_replace_file`

**Purpose:** Implements `replace file` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

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
- direct call: `landscout.sources.rte_odre_fr::_publish_cache_pair` via `_replace_file`
- value/type reference: `landscout.sources.rte_odre_fr::_publish_cache_pair` via `_replace_file`

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

**Purpose:** Implements `is link or junction` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

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
- direct call: `landscout.sources.rte_odre_fr::_require_no_cache_recovery_material` via `_is_link_or_junction`
- value/type reference: `landscout.sources.rte_odre_fr::_require_no_cache_recovery_material` via `_is_link_or_junction`
- direct call: `landscout.sources.rte_odre_fr::_prepare_temporary_cache_file` via `_is_link_or_junction`
- value/type reference: `landscout.sources.rte_odre_fr::_prepare_temporary_cache_file` via `_is_link_or_junction`

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

**Purpose:** Implements `cache recovery paths` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

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
- direct call: `landscout.sources.rte_odre_fr::_require_no_cache_recovery_material` via `_cache_recovery_paths`
- value/type reference: `landscout.sources.rte_odre_fr::_require_no_cache_recovery_material` via `_cache_recovery_paths`
- direct call: `landscout.sources.rte_odre_fr::_publish_cache_pair` via `_cache_recovery_paths`
- value/type reference: `landscout.sources.rte_odre_fr::_publish_cache_pair` via `_cache_recovery_paths`

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

**Purpose:** Implements `require no cache recovery material` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

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
  - `RteOdreDownloadError(<br>            "RTE/ODRE cache recovery backup already exists; manual recovery is required"<br>        )` under lexical guard `any(<br>        path.exists() or _is_link_or_junction(path)<br>        for path in _cache_recovery_paths(archive_path, metadata_path)<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::_publish_cache_pair` via `_require_no_cache_recovery_material`
- value/type reference: `landscout.sources.rte_odre_fr::_publish_cache_pair` via `_require_no_cache_recovery_material`
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_require_no_cache_recovery_material`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_require_no_cache_recovery_material`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.rte_odre_fr._is_link_or_junction` |
| `_cache_recovery_paths` | `landscout.sources.rte_odre_fr._cache_recovery_paths` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |

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
        raise RteOdreDownloadError(
            "RTE/ODRE cache recovery backup already exists; manual recovery is required"
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_prepare_temporary_cache_file`

**Purpose:** Implements `prepare temporary cache file` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

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
  - `RteOdreDownloadError(<br>                "RTE/ODRE cache temporary path is a link or junction"<br>            )` under lexical guard `_is_link_or_junction(path)`.
  - `RteOdreDownloadError(<br>                    "RTE/ODRE cache temporary path is not a regular file"<br>                )` under lexical guard `path.exists()`.
  - `re-raise`.
  - `RteOdreDownloadError(<br>            "RTE/ODRE cache temporary path cannot be prepared safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_prepare_temporary_cache_file`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_prepare_temporary_cache_file`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_link_or_junction` | `landscout.sources.rte_odre_fr._is_link_or_junction` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_cleanup_temporary_cache_files`

**Purpose:** Implements `cleanup temporary cache files` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

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
  - `RteOdreDownloadError(<br>            "RTE/ODRE cache temporary files could not be cleaned safely"<br>        )` under lexical guard `cleanup_error is not None and primary_error is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_cleanup_temporary_cache_files`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_cleanup_temporary_cache_files`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |

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
        raise RteOdreDownloadError(
            "RTE/ODRE cache temporary files could not be cleaned safely"
        ) from cleanup_error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_publish_cache_pair`

**Purpose:** Implements `publish cache pair` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

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
  - `RteOdreDownloadError(<br>                "RTE/ODRE cache publication and rollback both failed"<br>            )`.
  - `re-raise`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_publish_cache_pair`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_publish_cache_pair`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_cache_recovery_paths` | `landscout.sources.rte_odre_fr._cache_recovery_paths` |
| `archive_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_no_cache_recovery_material` | `landscout.sources.rte_odre_fr._require_no_cache_recovery_material` |
| `copy2` | `shutil.copy2` |
| `archive_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_file` | `landscout.sources.rte_odre_fr._replace_file` |
| `archive_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_path.is_file`<br>`metadata_path.is_file` |
| Filesystem/archive write or publication | `archive_backup.unlink`<br>`metadata_backup.unlink`<br>`archive_path.unlink` |
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_load_cached_download`

**Purpose:** Implements `load cached download` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

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

- Exact decorators: none.
- Declared return annotation: `RteOdreDownload | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `metadata_path` | positional-or-keyword | `Path` | `required` |
| `config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `logical_name` | positional-or-keyword | `LogicalDatasetName` | `required` |
| `source_url` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `RteOdreDownload(<br>            logical_name=logical_name,<br>            dataset_id=dataset.dataset_id,<br>            provider=config.provider,<br>            portal=config.portal,<br>            source_url=source_url,<br>            export_format=dataset.preferred_format,<br>            download_timestamp=download_timestamp,<br>            filename=archive_path.name,<br>            file_size=file_size,<br>            sha256=checksum,<br>            path=archive_path,<br>            cache_hit=True,<br>            dataset_metadata=dataset_metadata,<br>            export_summary=cached_summary,<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(download_timestamp, str)`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_load_cached_download`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `_load_cached_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_get_dataset_config` | `landscout.sources.rte_odre_fr._get_dataset_config` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_geojson` | `landscout.sources.rte_odre_fr._validate_geojson` |
| `archive_path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `landscout.sources.rte_odre_fr._sha256` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `(<br>            datetime.now(UTC) - downloaded_at.astimezone(UTC)<br>        ).total_seconds` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `downloaded_at.astimezone` | `unresolved local/third-party receiver; no ownership inferred` |
| `_metadata_from_dict` | `landscout.sources.rte_odre_fr._metadata_from_dict` |
| `_export_summary_from_dict` | `landscout.sources.rte_odre_fr._export_summary_from_dict` |
| `_validate_records_count` | `landscout.sources.rte_odre_fr._validate_records_count` |
| `RteOdreDownload` | `landscout.sources.rte_odre_fr.RteOdreDownload` |

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
    config: RteOdreSourceConfig,
    logical_name: LogicalDatasetName,
    source_url: str,
) -> RteOdreDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    dataset = _get_dataset_config(config, logical_name)
    try:
        metadata = loads_strict_json_object(metadata_path.read_bytes())
        expected_keys = {
            "logical_name",
            "dataset_id",
            "provider",
            "portal",
            "source_url",
            "export_format",
            "download_timestamp",
            "filename",
            "file_size",
            "sha256",
            "dataset_metadata",
            "export_summary",
        }
        if set(metadata) != expected_keys:
            return None
        string_fields = (
            "logical_name",
            "dataset_id",
            "provider",
            "portal",
            "source_url",
            "export_format",
            "download_timestamp",
            "filename",
            "sha256",
        )
        if any(type(metadata[field]) is not str for field in string_fields):
            return None
        if type(metadata["file_size"]) is not int:
            return None
        fresh_summary = _validate_geojson(archive_path)
        file_size = archive_path.stat().st_size
        checksum = _sha256(archive_path)
        download_timestamp = metadata["download_timestamp"]
        assert isinstance(download_timestamp, str)
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
        RteOdreDownloadError,
    ):
        return None
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `download_rte_odre_dataset`

**Purpose:** Implements `download rte odre dataset` within the file role: Loads RTE/ODRÉ configuration and acquires official GeoJSON datasets with source, geometry, cache, and recovery validation.

**Exact signature**

```python
def download_rte_odre_dataset(
    logical_name: LogicalDatasetName,
    config: RteOdreSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 60.0,
) -> RteOdreDownload:
```

- Exact decorators: none.
- Declared return annotation: `RteOdreDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `logical_name` | positional-or-keyword | `LogicalDatasetName` | `required` |
| `config` | positional-or-keyword | `RteOdreSourceConfig` | `required` |
| `cache_dir` | positional-or-keyword | `Path` | `DEFAULT_CACHE_DIR` |
| `timeout` | positional-or-keyword | `float` | `60.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `cached`
  - `result`
- Explicit raise paths:
  - `re-raise`.
  - `RteOdreDownloadError(<br>            "RTE/ODRE cache paths cannot be prepared safely"<br>        )`.
  - `re-raise`.
  - `RteOdreDownloadError(f"RTE/ODRE download failed: {source_url}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
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
)`
- import: `tests.unit.test_rte_odre_fr::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- direct call: `tests.unit.test_rte_odre_fr::test_successful_download` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_successful_download` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_broken_recovery_symlink_rejects_rte_before_network` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_broken_recovery_symlink_rejects_rte_before_network` via `download_rte_odre_dataset`
- direct call: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_rte_odre_dataset`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_rte_odre_dataset`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.rte_odre_fr._validated_source_config` |
| `_get_dataset_config` | `landscout.sources.rte_odre_fr._get_dataset_config` |
| `quote` | `urllib.parse.quote` |
| `_dataset_api_url` | `landscout.sources.rte_odre_fr._dataset_api_url` |
| `_require_no_cache_recovery_material` | `landscout.sources.rte_odre_fr._require_no_cache_recovery_material` |
| `_load_cached_download` | `landscout.sources.rte_odre_fr._load_cached_download` |
| `archive_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `cache_dir.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `_prepare_temporary_cache_file` | `landscout.sources.rte_odre_fr._prepare_temporary_cache_file` |
| `RteOdreDownloadError` | `landscout.sources.rte_odre_fr.RteOdreDownloadError` |
| `fetch_rte_odre_dataset_metadata` | `landscout.sources.rte_odre_fr.fetch_rte_odre_dataset_metadata` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `temporary_archive.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `copyfileobj` | `shutil.copyfileobj` |
| `_validate_geojson` | `landscout.sources.rte_odre_fr._validate_geojson` |
| `_validate_records_count` | `landscout.sources.rte_odre_fr._validate_records_count` |
| `replace` | `dataclasses.replace` |
| `RteOdreDownload` | `landscout.sources.rte_odre_fr.RteOdreDownload` |
| `datetime.now(UTC).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `temporary_archive.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `landscout.sources.rte_odre_fr._sha256` |
| `asdict` | `dataclasses.asdict` |
| `lineage.pop` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_metadata.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `_publish_cache_pair` | `landscout.sources.rte_odre_fr._publish_cache_pair` |
| `_cleanup_temporary_cache_files` | `landscout.sources.rte_odre_fr._cleanup_temporary_cache_files` |
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
| In-memory mutation | `lineage.pop("path")`<br>`lineage.pop("cache_hit")` |
| Direct parameter mutation | None directly present. |

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
import json
import sys
from dataclasses import asdict, dataclass, replace
from datetime import UTC, datetime
from hashlib import sha256
from math import isfinite
from numbers import Real
from pathlib import Path
from shutil import copy2, copyfileobj
from typing import Annotated, Any, Literal, cast
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
)
from pydantic_core import PydanticCustomError

from landscout.common.safe_http import open_safe_https
from landscout.common.strict_json import StrictJsonError, loads_strict_json_object
from landscout.common.strict_yaml import loads_strict_yaml

DEFAULT_CONFIG_PATH = Path("configs/sources/rte_odre_fr.yaml")
DEFAULT_CACHE_DIR = Path("data/cache/rte_odre")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
LOGICAL_DATASET_NAMES = ("sites", "overhead_lines", "underground_lines")
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
GEOJSON_GEOMETRY_TYPES = COORDINATE_GEOMETRY_TYPES | {"GeometryCollection"}

LogicalDatasetName = Literal["sites", "overhead_lines", "underground_lines"]
ExportFormat = Literal["geojson"]
GeometryPrecisionStatus = Literal[
    "EXACT_NOT_CLAIMED",
    "GENERALIZED_OR_RESTRICTED",
    "MISSING",
    "UNKNOWN",
]

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
DatasetIdentifier = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]*$",
    ),
]


def _strict_nonnegative_finite_number(value: object) -> object:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise PydanticCustomError(
            "strict_number",
            "value must be a strict finite non-negative number",
        )
    try:
        numeric_value = float(value)
    except (OverflowError, TypeError, ValueError) as error:
        raise ValueError("value must be a strict finite non-negative number") from error
    if not isfinite(numeric_value) or value < 0:
        raise ValueError("value must be a strict finite non-negative number")
    return value


StrictNonNegativeFloat = Annotated[
    float,
    BeforeValidator(_strict_nonnegative_finite_number),
    Field(ge=0, allow_inf_nan=False),
]


class RteDatasetConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    dataset_id: DatasetIdentifier
    preferred_format: ExportFormat


class RteDatasetsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    sites: RteDatasetConfig
    overhead_lines: RteDatasetConfig
    underground_lines: RteDatasetConfig


class RteOdreApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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


class RteOdreCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    max_age_hours: StrictNonNegativeFloat


class RteOdreSourceConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: Literal["RTE"]
    portal: Literal["ODRE"]
    api: RteOdreApiConfig
    datasets: RteDatasetsConfig
    cache: RteOdreCacheConfig


class RteOdreDownloadError(RuntimeError):
    """Raised when RTE/ODRE metadata or exports cannot be retrieved safely."""


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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
        if (
            self.null_geometry_count + self.non_null_geometry_count
            != self.feature_count
        ):
            raise ValueError("Geometry counts must add up to feature_count")
        if not isinstance(self.geometry_types, tuple) or any(
            not isinstance(value, str) or not value for value in self.geometry_types
        ):
            raise TypeError("geometry_types must be a tuple of non-empty strings")


@dataclass(frozen=True)
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


def load_rte_odre_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> RteOdreSourceConfig:
    content = loads_strict_yaml(path.read_bytes())
    if type(content) is not dict:
        raise TypeError(f"Expected a YAML mapping in {path}")
    return RteOdreSourceConfig.model_validate(content)


def _validated_source_config(config: object) -> RteOdreSourceConfig:
    try:
        if type(config) is not RteOdreSourceConfig:
            raise TypeError("RTE/ODRE source config type is invalid")
        return RteOdreSourceConfig.model_validate(config.model_dump(mode="python"))
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise RteOdreDownloadError(
            "RTE/ODRE source config no longer satisfies the official origin contract"
        ) from error


def _get_dataset_config(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> RteDatasetConfig:
    if logical_name not in LOGICAL_DATASET_NAMES:
        raise ValueError(f"Unsupported RTE/ODRE logical dataset: {logical_name}")
    return getattr(config.datasets, logical_name)


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


def build_rte_odre_metadata_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
    validated_config = _validated_source_config(config)
    return _dataset_api_url(validated_config, logical_name, "")


def build_rte_odre_export_url(
    config: RteOdreSourceConfig, logical_name: LogicalDatasetName
) -> str:
    validated_config = _validated_source_config(config)
    dataset = _get_dataset_config(validated_config, logical_name)
    export_format = quote(dataset.preferred_format, safe="")
    return _dataset_api_url(validated_config, logical_name, f"/exports/{export_format}")


def _optional_string(mapping: dict[str, Any], key: str) -> str | None:
    value = mapping.get(key)
    if not isinstance(value, str):
        return None
    normalized = value.strip()
    return normalized or None


def _metadata_precision_status(description: str | None) -> GeometryPrecisionStatus:
    if description is None:
        return "UNKNOWN"
    normalized = description.casefold()
    if "données gps" in normalized and "sécurité publique" in normalized:
        return "GENERALIZED_OR_RESTRICTED"
    return "UNKNOWN"


def _read_response_json(source_url: str, timeout: float) -> dict[str, Any]:
    try:
        with open_safe_https(
            source_url,
            timeout=timeout,
            headers={"User-Agent": "LandScout-AI/0.1"},
        ) as response:
            payload = loads_strict_json_object(response.read())
    except (HTTPError, URLError, OSError, StrictJsonError) as error:
        raise RteOdreDownloadError(f"RTE/ODRE request failed: {source_url}") from error
    return payload


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


def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_geojson(path: Path) -> RteOdreExportSummary:
    if not path.is_file() or path.stat().st_size == 0:
        raise RteOdreDownloadError(f"GeoJSON export is missing or empty: {path}")
    try:
        payload = loads_strict_json_object(path.read_bytes())
    except (OSError, StrictJsonError) as error:
        raise RteOdreDownloadError(
            f"GeoJSON export is not valid finite UTF-8 JSON: {path}"
        ) from error
    if payload.get("type") != "FeatureCollection":
        raise RteOdreDownloadError("GeoJSON export must be a FeatureCollection")
    features = payload.get("features")
    if not isinstance(features, list):
        raise RteOdreDownloadError(
            "GeoJSON FeatureCollection must contain a features list"
        )

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


def _metadata_from_dict(payload: Any) -> RteOdreDatasetMetadata:
    if type(payload) is not dict:
        raise TypeError("Missing cached dataset metadata")
    expected_keys = {
        "dataset_id",
        "title",
        "publisher",
        "modified",
        "data_processed",
        "metadata_processed",
        "license",
        "records_count",
        "geometry_precision_status",
    }
    if set(payload) != expected_keys:
        raise ValueError("Cached dataset metadata schema differs")
    dataset_id = payload["dataset_id"]
    if type(dataset_id) is not str or not dataset_id:
        raise TypeError("Invalid cached dataset ID")
    precision_status = payload["geometry_precision_status"]
    allowed_statuses = {
        "EXACT_NOT_CLAIMED",
        "GENERALIZED_OR_RESTRICTED",
        "MISSING",
        "UNKNOWN",
    }
    if type(precision_status) is not str or precision_status not in allowed_statuses:
        raise ValueError("Invalid cached geometry precision status")
    records_count = payload["records_count"]
    if records_count is not None and (type(records_count) is not int):
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
        if value is not None and type(value) is not str:
            raise TypeError(f"Invalid cached metadata value: {field_name}")
        optional_values[field_name] = value
    return RteOdreDatasetMetadata(
        dataset_id=dataset_id,
        title=optional_values["title"],
        publisher=optional_values["publisher"],
        modified=optional_values["modified"],
        data_processed=optional_values["data_processed"],
        metadata_processed=optional_values["metadata_processed"],
        license=optional_values["license"],
        records_count=records_count,
        geometry_precision_status=cast(GeometryPrecisionStatus, precision_status),
    )


def _export_summary_from_dict(payload: Any) -> RteOdreExportSummary:
    if type(payload) is not dict:
        raise TypeError("Missing cached export summary")
    expected_keys = {
        "feature_count",
        "null_geometry_count",
        "non_null_geometry_count",
        "geometry_types",
    }
    if set(payload) != expected_keys:
        raise ValueError("Cached export summary schema differs")
    geometry_types = payload["geometry_types"]
    if type(geometry_types) is not list or any(
        type(value) is not str for value in geometry_types
    ):
        raise TypeError("Invalid cached geometry types")
    return RteOdreExportSummary(
        feature_count=payload["feature_count"],
        null_geometry_count=payload["null_geometry_count"],
        non_null_geometry_count=payload["non_null_geometry_count"],
        geometry_types=tuple(geometry_types),
    )


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
        raise RteOdreDownloadError(
            "RTE/ODRE cache recovery backup already exists; manual recovery is required"
        )


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
        metadata = loads_strict_json_object(metadata_path.read_bytes())
        expected_keys = {
            "logical_name",
            "dataset_id",
            "provider",
            "portal",
            "source_url",
            "export_format",
            "download_timestamp",
            "filename",
            "file_size",
            "sha256",
            "dataset_metadata",
            "export_summary",
        }
        if set(metadata) != expected_keys:
            return None
        string_fields = (
            "logical_name",
            "dataset_id",
            "provider",
            "portal",
            "source_url",
            "export_format",
            "download_timestamp",
            "filename",
            "sha256",
        )
        if any(type(metadata[field]) is not str for field in string_fields):
            return None
        if type(metadata["file_size"]) is not int:
            return None
        fresh_summary = _validate_geojson(archive_path)
        file_size = archive_path.stat().st_size
        checksum = _sha256(archive_path)
        download_timestamp = metadata["download_timestamp"]
        assert isinstance(download_timestamp, str)
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
        RteOdreDownloadError,
    ):
        return None


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
