# `src/landscout/sources/gpu_fr.py`

## File identity

- Repository path: `src/landscout/sources/gpu_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: planning
- Responsibility: Discovers and verifies the authoritative GPU planning document, archive, spatial layers, written files, and provenance.
- Source SHA256: `ae581db5e8719611b98d3d57e2de9016b688bece5e7d1375f498660442d1ce06`

## 1. Purpose

Discovers and verifies the authoritative GPU planning document, archive, spatial layers, written files, and provenance.

## 2. Position in LandScout architecture

This file belongs to the **source adapter** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import math`
- `import re`
- `import shutil`
- `import stat`
- `import sys`
- `import unicodedata`
- `import zipfile`
- `from dataclasses import asdict, dataclass`
- `from datetime import UTC, datetime`
- `from hashlib import sha256`
- `from numbers import Integral`
- `from pathlib import Path, PurePosixPath, PureWindowsPath`
- `from shutil import copy2, copyfileobj`
- `from typing import Annotated, Any, Literal`
- `from urllib.error import HTTPError, URLError`
- `from urllib.parse import quote, urlencode, urljoin, urlparse`
- `from xml.etree import ElementTree`

### Third-party packages

- `import geopandas as gpd`
- `import pyogrio`
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
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.common.safe_http import open_safe_https`

## 4. Contract taxonomy

### A. Python constants

#### `DEFAULT_CONFIG_PATH`

```python
DEFAULT_CONFIG_PATH = Path("configs/sources/gpu_fr.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `DEFAULT_CACHE_DIR`

```python
DEFAULT_CACHE_DIR = Path("data/cache/gpu")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `DOWNLOAD_CHUNK_SIZE`

```python
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/sources/gpu_fr.py::_sha256` (value argument/reference), `src/landscout/sources/gpu_fr.py::download_gpu_document` (value argument/reference), `src/landscout/sources/gpu_fr.py::extract_gpu_document` (value argument/reference), `src/landscout/sources/ign_bdtopo_fr.py::_calculate_checksums` (value argument/reference), `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` (value argument/reference), `src/landscout/sources/ign_bdtopo_fr.py::_geopackage_integrity` (value argument/reference), `src/landscout/sources/inpn_protected_areas_fr.py::_sha256_file` (value argument/reference), `src/landscout/sources/inpn_protected_areas_fr.py::_download_archive_bytes` (value argument/reference), `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` (value argument/reference), `src/landscout/sources/rte_odre_fr.py::_sha256` (value argument/reference), `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` (value argument/reference).

#### `USER_AGENT`

```python
USER_AGENT = "LandScout-AI/0.1"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `EXTRACTION_MANIFEST_NAME`

```python
EXTRACTION_MANIFEST_NAME = ".landscout-gpu-extraction.json"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_enrich_planning_features.py::<module>` (import/re-export), `tests/unit/test_enrich_planning_zoning.py::<module>` (import/re-export), `tests/unit/test_gpu_fr.py::test_zip_cannot_claim_extraction_manifest_path` (property/attribute access), `tests/unit/test_gpu_fr.py::test_extraction_inventory_and_cache` (property/attribute access), `tests/unit/test_resolve_planning_feature_codes.py::<module>` (import/re-export).

#### `EXTRACTION_MANIFEST_SCHEMA_VERSION`

```python
EXTRACTION_MANIFEST_SCHEMA_VERSION = 2
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing.

#### `_WINDOWS_RESERVED_BASENAMES`

```python
_WINDOWS_RESERVED_BASENAMES = {
    "con",
    "prn",
    "aux",
    "nul",
    *(f"com{index}" for index in range(1, 10)),
    *(f"lpt{index}" for index in range(1, 10)),
}
```

Module-level technical/source/policy constant consumed by the exact references below.


### B. Type aliases and closed domains

#### `NonEmptyString`

```python
NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
```

String constrained non-empty after the exact StringConstraints behavior in the declaration. It is consumed by annotations or Pydantic validation in this module.

#### `CommuneCode`

```python
CommuneCode = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[0-9]{5}$"),
]
```

Canonical French commune identity constrained by the exact regex in the declaration. It is consumed by annotations or Pydantic validation in this module.

#### `DownloadStrategy`

```python
DownloadStrategy = Literal["partition"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. It is consumed by annotations or Pydantic validation in this module.

#### `LogicalLayerName`

```python
LogicalLayerName = Literal[
    "zoning",
    "prescription_surface",
    "prescription_line",
    "prescription_point",
    "information_surface",
    "information_line",
    "information_point",
]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. It is consumed by annotations or Pydantic validation in this module.

#### `FileCategory`

```python
FileCategory = Literal[
    "SPATIAL_DATA", "METADATA", "WRITTEN_REGULATION", "OTHER_ATTACHMENT"
]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. It is consumed by annotations or Pydantic validation in this module.


### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `GpuApiConfig`

**Purpose:** Validates the planning contract carried by `base_url`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `base_url` | `base_url: HttpUrl` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |

**Validators (exact source)**

`_official_api`:

```python
def _official_api(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlparse(str(value))
        if (
            parsed.scheme != "https"
            or parsed.hostname != "www.geoportail-urbanisme.gouv.fr"
            or parsed.port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path.rstrip("/") != "/api"
            or parsed.params
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("GPU API URL must use the exact official HTTPS /api base")
        return value
```

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class GpuApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    base_url: HttpUrl

    @field_validator("base_url")
    @classmethod
    def _official_api(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlparse(str(value))
        if (
            parsed.scheme != "https"
            or parsed.hostname != "www.geoportail-urbanisme.gouv.fr"
            or parsed.port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path.rstrip("/") != "/api"
            or parsed.params
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("GPU API URL must use the exact official HTTPS /api base")
        return value
```

### `GpuDownloadConfig`

**Purpose:** Validates the planning contract carried by `strategy`, `partition_template`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `strategy` | `strategy: DownloadStrategy` | Stores `GpuDownloadConfig`'s `strategy` value under exact annotation `DownloadStrategy`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `partition_template` | `partition_template: NonEmptyString` | Stores `GpuDownloadConfig`'s `partition template` value under exact annotation `NonEmptyString`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Validators (exact source)**

`_valid_partition_template`:

```python
def _valid_partition_template(cls, value: str) -> str:
        if value != value.strip() or value.count("{code_insee}") != 1:
            raise ValueError(
                "partition_template must contain exactly one {code_insee} placeholder"
            )
        try:
            rendered = value.format(code_insee="31395")
        except (KeyError, ValueError) as error:
            raise ValueError("partition_template is malformed") from error
        if not rendered or "/" in rendered or "\\" in rendered:
            raise ValueError("partition_template must render one safe path component")
        return value
```

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class GpuDownloadConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    strategy: DownloadStrategy
    partition_template: NonEmptyString

    @field_validator("partition_template")
    @classmethod
    def _valid_partition_template(cls, value: str) -> str:
        if value != value.strip() or value.count("{code_insee}") != 1:
            raise ValueError(
                "partition_template must contain exactly one {code_insee} placeholder"
            )
        try:
            rendered = value.format(code_insee="31395")
        except (KeyError, ValueError) as error:
            raise ValueError("partition_template is malformed") from error
        if not rendered or "/" in rendered or "\\" in rendered:
            raise ValueError("partition_template must render one safe path component")
        return value
```

### `GpuCacheConfig`

**Purpose:** Validates the planning contract carried by `max_age_hours`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `max_age_hours` | `max_age_hours: float = Field(ge=0, allow_inf_nan=False)` | Stores `GpuCacheConfig`'s `max age hours` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class GpuCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    max_age_hours: float = Field(ge=0, allow_inf_nan=False)
```

### `GpuPilotConfig`

**Purpose:** Validates the planning contract carried by `commune_code`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `commune_code` | `commune_code: CommuneCode` | Stores `GpuPilotConfig`'s `commune code` value under exact annotation `CommuneCode`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class GpuPilotConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commune_code: CommuneCode
```

### `GpuLogicalLayerConfig`

**Purpose:** Validates the planning contract carried by `class_label`, `match_tokens`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `class_label` | `class_label: NonEmptyString` | Closed or validated `class label` classification on `GpuLogicalLayerConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `match_tokens` | `match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)` | Structured `match tokens` collection owned by `GpuLogicalLayerConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Validators (exact source)**

`_unique_tokens`:

```python
def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(value) for value in values)
        if any(not value for value in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(normalized) != len(set(normalized)):
            raise ValueError("Layer match tokens must be unique after normalization")
        return values
```

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class GpuLogicalLayerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    class_label: NonEmptyString
    match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)

    @field_validator("match_tokens")
    @classmethod
    def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(value) for value in values)
        if any(not value for value in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(normalized) != len(set(normalized)):
            raise ValueError("Layer match tokens must be unique after normalization")
        return values
```

### `GpuSpatialLayersConfig`

**Purpose:** Validates the planning contract carried by `zoning`, `prescription_surface`, `prescription_line`, `prescription_point`, `information_surface`, `information_line`, `information_point`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `zoning` | `zoning: GpuLogicalLayerConfig` | Stores `GpuSpatialLayersConfig`'s `zoning` value under exact annotation `GpuLogicalLayerConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `prescription_surface` | `prescription_surface: GpuLogicalLayerConfig` | Stores `GpuSpatialLayersConfig`'s `prescription surface` value under exact annotation `GpuLogicalLayerConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `prescription_line` | `prescription_line: GpuLogicalLayerConfig` | Stores `GpuSpatialLayersConfig`'s `prescription line` value under exact annotation `GpuLogicalLayerConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `prescription_point` | `prescription_point: GpuLogicalLayerConfig` | Stores `GpuSpatialLayersConfig`'s `prescription point` value under exact annotation `GpuLogicalLayerConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `information_surface` | `information_surface: GpuLogicalLayerConfig` | Closed or validated `information surface` classification on `GpuSpatialLayersConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `information_line` | `information_line: GpuLogicalLayerConfig` | Closed or validated `information line` classification on `GpuSpatialLayersConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `information_point` | `information_point: GpuLogicalLayerConfig` | Closed or validated `information point` classification on `GpuSpatialLayersConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class GpuSpatialLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    zoning: GpuLogicalLayerConfig
    prescription_surface: GpuLogicalLayerConfig
    prescription_line: GpuLogicalLayerConfig
    prescription_point: GpuLogicalLayerConfig
    information_surface: GpuLogicalLayerConfig
    information_line: GpuLogicalLayerConfig
    information_point: GpuLogicalLayerConfig
```

### `GpuSourceConfig`

**Purpose:** Strict configuration for official French GPU ingestion.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `provider` | `provider: NonEmptyString` | Stores `GpuSourceConfig`'s `provider` value under exact annotation `NonEmptyString`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `portal` | `portal: NonEmptyString` | Stores `GpuSourceConfig`'s `portal` value under exact annotation `NonEmptyString`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `country` | `country: Literal["FR"]` | Stores `GpuSourceConfig`'s `country` value under exact annotation `Literal['FR']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `api` | `api: GpuApiConfig` | Stores `GpuSourceConfig`'s `api` value under exact annotation `GpuApiConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `download` | `download: GpuDownloadConfig` | Stores `GpuSourceConfig`'s `download` value under exact annotation `GpuDownloadConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `cache` | `cache: GpuCacheConfig` | Stores `GpuSourceConfig`'s `cache` value under exact annotation `GpuCacheConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `pilot` | `pilot: GpuPilotConfig` | Stores `GpuSourceConfig`'s `pilot` value under exact annotation `GpuPilotConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `spatial_layers` | `spatial_layers: GpuSpatialLayersConfig` | Stores `GpuSourceConfig`'s `spatial layers` value under exact annotation `GpuSpatialLayersConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Exact class source**

```python
class GpuSourceConfig(BaseModel):
    """Strict configuration for official French GPU ingestion."""

    model_config = ConfigDict(extra="forbid")

    provider: NonEmptyString
    portal: NonEmptyString
    country: Literal["FR"]
    api: GpuApiConfig
    download: GpuDownloadConfig
    cache: GpuCacheConfig
    pilot: GpuPilotConfig
    spatial_layers: GpuSpatialLayersConfig
```

### `GpuError`

**Purpose:** Base class for controlled GPU source failures.

**Kind:** controlled exception.

**Inheritance:** `RuntimeError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.

**Exact class source**

```python
class GpuError(RuntimeError):
    """Base class for controlled GPU source failures."""
```

### `GpuConfigError`

**Purpose:** Raised when GPU source configuration is invalid.

**Kind:** controlled exception.

**Inheritance:** `GpuError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::load_gpu_source_config` via `GpuConfigError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validated_source_config` via `GpuConfigError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::build_gpu_partition` via `GpuConfigError`.

**Exact class source**

```python
class GpuConfigError(GpuError):
    """Raised when GPU source configuration is invalid."""
```

### `GpuDiscoveryError`

**Purpose:** Raised when the current planning document cannot be resolved safely.

**Kind:** controlled exception.

**Inheritance:** `GpuError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_request_json` via `GpuDiscoveryError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_required_string` via `GpuDiscoveryError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_optional_string` via `GpuDiscoveryError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_written_files` via `GpuDiscoveryError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `GpuDiscoveryError`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `pytest.raises(GpuDiscoveryError, match='config|official|origin')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url` via `pytest.raises(GpuDiscoveryError, match='written material URL')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `pytest.raises(GpuDiscoveryError, match='archive URL')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_no_current_document_is_rejected` via `pytest.raises(GpuDiscoveryError, match='No current')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_ambiguous_current_documents_are_rejected` via `pytest.raises(GpuDiscoveryError, match='Ambiguous')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_missing_document_identity_is_rejected` via `pytest.raises(GpuDiscoveryError, match='missing')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing` via `pytest.raises(GpuDiscoveryError, match='match|changed|current')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing` via `pytest.raises(GpuDiscoveryError, match='match')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name` via `pytest.raises(GpuDiscoveryError, match='archive name|safe')`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Exact class source**

```python
class GpuDiscoveryError(GpuError):
    """Raised when the current planning document cannot be resolved safely."""
```

### `GpuDownloadError`

**Purpose:** Raised when the GPU archive cannot be downloaded or cached safely.

**Kind:** controlled exception.

**Inheritance:** `GpuError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_safe_gpu_archive_filename` via `GpuDownloadError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_document_for_config` via `GpuDownloadError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_require_no_cache_recovery_material` via `GpuDownloadError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_prepare_temporary_cache_file` via `GpuDownloadError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_cleanup_temporary_cache_files` via `GpuDownloadError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_publish_cache_pair` via `GpuDownloadError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `GpuDownloadError`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_download_rejects_document_inconsistent_with_config` via `pytest.raises(GpuDownloadError, match='document|identity|config')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network` via `pytest.raises(GpuDownloadError, match='written|document|source|URL')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_unsafe_archive_name_before_io` via `pytest.raises(GpuDownloadError, match='archive name|archive filename|safe')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `pytest.raises(GpuDownloadError, match='backup|recovery|manual')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache` via `pytest.raises(GpuDownloadError)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files` via `pytest.raises(GpuDownloadError)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `pytest.raises(GpuDownloadError, match='rollback')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `pytest.raises(GpuDownloadError, match='rollback')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `pytest.raises(GpuDownloadError, match='backup|recovery|manual')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `pytest.raises(GpuDownloadError)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_corrupt_download_is_rejected` via `pytest.raises(GpuDownloadError)`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Exact class source**

```python
class GpuDownloadError(GpuError):
    """Raised when the GPU archive cannot be downloaded or cached safely."""
```

### `GpuArchiveError`

**Purpose:** Raised when a GPU archive or extraction is corrupt or unsafe.

**Kind:** controlled exception.

**Inheritance:** `GpuError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_archive_download` via `GpuArchiveError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_windows_member_component` via `GpuArchiveError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validated_zip_destinations` via `GpuArchiveError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::validate_gpu_archive` via `GpuArchiveError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_inventory` via `GpuArchiveError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_extraction_manifest` via `GpuArchiveError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_publish_extraction_directory` via `GpuArchiveError`.
- callback/function object: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `isinstance(error, GpuArchiveError)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `GpuArchiveError`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_archive_path_traversal_is_rejected` via `pytest.raises(GpuArchiveError, match='Unsafe')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_archive_symlink_is_rejected` via `pytest.raises(GpuArchiveError, match='Symbolic')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_duplicate_zip_extraction_targets_are_rejected` via `pytest.raises(GpuArchiveError, match='(?i)duplicate|collid')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_zip_file_directory_target_collision_is_rejected` via `pytest.raises(GpuArchiveError, match='collision|target')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_zip_cannot_claim_extraction_manifest_path` via `pytest.raises(GpuArchiveError, match='manifest')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_stale_download_object_rejects_replaced_valid_archive` via `pytest.raises(GpuArchiveError, match='checksum|SHA|stale|metadata')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_extraction_rejects_archive_object_inconsistent_with_path` via `pytest.raises(GpuArchiveError, match='archive|metadata|checksum|size')`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Exact class source**

```python
class GpuArchiveError(GpuError):
    """Raised when a GPU archive or extraction is corrupt or unsafe."""
```

### `GpuSpatialInspectionError`

**Purpose:** Raised when required GPU spatial layers cannot be inspected safely.

**Kind:** controlled exception.

**Inheritance:** `GpuError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_gpu_spatial_layers` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_discover_logical_layer` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_load_reference` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validated_inventory_path` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validated_spatial_root` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_inventory` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_contained_spatial_path` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_dataset_relative_path` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_same_spatial_crs` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_compare_inspected_spatial_layer` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_sources` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::revalidate_gpu_spatial_layer_sources` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_summarize_layer` via `GpuSpatialInspectionError`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::finite_numeric_vocabulary` via `GpuSpatialInspectionError`.
- import/re-export: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`.
- import/re-export: `src/landscout/stages/enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    revalidate_gpu_spatial_layer_sources,
)`.
- import/re-export: `src/landscout/stages/index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`.
- callback/property argument: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_malformed_layer_items` via `pytest.raises(gpu_source_module.GpuSpatialInspectionError)`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_malformed_layer_items` via `gpu_source_module.GpuSpatialInspectionError`.
- callback/property argument: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_malformed_planning_document` via `pytest.raises(gpu_source_module.GpuSpatialInspectionError)`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_malformed_planning_document` via `gpu_source_module.GpuSpatialInspectionError`.
- callback/property argument: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_duplicate_logical_name` via `pytest.raises(gpu_source_module.GpuSpatialInspectionError, match='duplicate')`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_duplicate_logical_name` via `gpu_source_module.GpuSpatialInspectionError`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_missing_zoning_layer_fails_clearly` via `pytest.raises(GpuSpatialInspectionError, match='zoning')`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_ambiguous_zoning_layer_fails_clearly` via `pytest.raises(GpuSpatialInspectionError, match='found 2')`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Exact class source**

```python
class GpuSpatialInspectionError(GpuError):
    """Raised when required GPU spatial layers cannot be inspected safely."""
```

### `GpuWrittenFile`

**Purpose:** Immutable result/value envelope carrying `filename`, `title`, `document_path`, `source_url`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `filename` | `filename: str` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `title` | `title: str \| None` | `GpuWrittenFile`'s `title` evidence/text field; it retains the exact configured or source meaning under annotation `str | None` and is not promoted to a legal conclusion. |
| `document_path` | `document_path: str \| None` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `source_url` | `source_url: str \| None` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_written_files` via `GpuWrittenFile`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_document_from_dict` via `GpuWrittenFile`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::_written_file_matches` via `isinstance(item, GpuWrittenFile)`.
- import/re-export: `src/landscout/stages/index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_document` via `GpuWrittenFile`.
- import/re-export: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`.

**Exact class source**

```python
class GpuWrittenFile:
    filename: str
    title: str | None
    document_path: str | None
    source_url: str | None
```

### `GpuDocumentMetadata`

**Purpose:** Immutable result/value envelope carrying `provider`, `portal`, `commune_code`, `partition`, `document_id`, `document_family`, `document_type`, `document_title`, `status`, `legal_status`, `effective_status`, `version`, `archive_name`, `publication_timestamp`, `update_timestamp`, `revision_date`, `producer`, `standard_model`, `projection`, `metadata_identifier`, `source_url`, `written_files`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `provider` | `provider: str` | Stores `GpuDocumentMetadata`'s `provider` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `portal` | `portal: str` | Stores `GpuDocumentMetadata`'s `portal` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `commune_code` | `commune_code: str` | Stores `GpuDocumentMetadata`'s `commune code` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `partition` | `partition: str` | Stores `GpuDocumentMetadata`'s `partition` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `document_id` | `document_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `document_family` | `document_family: str` | Closed or validated `document family` classification on `GpuDocumentMetadata`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `document_type` | `document_type: str` | Closed or validated `document type` classification on `GpuDocumentMetadata`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `document_title` | `document_title: str \| None` | `GpuDocumentMetadata`'s `document title` evidence/text field; it retains the exact configured or source meaning under annotation `str | None` and is not promoted to a legal conclusion. |
| `status` | `status: str` | Closed or validated `status` classification on `GpuDocumentMetadata`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `legal_status` | `legal_status: str` | Closed or validated `legal status` classification on `GpuDocumentMetadata`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `effective_status` | `effective_status: str` | Closed or validated `effective status` classification on `GpuDocumentMetadata`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `version` | `version: str \| None` | Stores `GpuDocumentMetadata`'s `version` value under exact annotation `str | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `archive_name` | `archive_name: str` | Stores `GpuDocumentMetadata`'s `archive name` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `publication_timestamp` | `publication_timestamp: str \| None` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `update_timestamp` | `update_timestamp: str \| None` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `revision_date` | `revision_date: str \| None` | Stores `GpuDocumentMetadata`'s `revision date` value under exact annotation `str | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `producer` | `producer: str \| None` | Stores `GpuDocumentMetadata`'s `producer` value under exact annotation `str | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `standard_model` | `standard_model: str \| None` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `projection` | `projection: str \| None` | Stores `GpuDocumentMetadata`'s `projection` value under exact annotation `str | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `metadata_identifier` | `metadata_identifier: str \| None` | Stores `GpuDocumentMetadata`'s `metadata identifier` value under exact annotation `str | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `source_url` | `source_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `written_files` | `written_files: tuple[GpuWrittenFile, ...]` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `GpuDocumentMetadata`.
- callback/function object: `src/landscout/sources/gpu_fr.py::_validate_gpu_document_for_config` via `isinstance(document, GpuDocumentMetadata)`.
- callback/function object: `src/landscout/sources/gpu_fr.py::_validate_gpu_archive_download` via `isinstance(download.document, GpuDocumentMetadata)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_document_from_dict` via `GpuDocumentMetadata`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::_validate_document_lineage` via `isinstance(archive.document, GpuDocumentMetadata)`.
- import/re-export: `src/landscout/stages/index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `GpuDocumentMetadata`.
- import/re-export: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_planning_document` via `GpuDocumentMetadata`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_gpu_fr.py::_extraction_from_archive` via `gpu.GpuDocumentMetadata`.
- property/attribute access: `tests/unit/test_gpu_fr.py::_extraction_from_archive` via `gpu.GpuDocumentMetadata`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_document` via `GpuDocumentMetadata`.
- import/re-export: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_planning_document` via `GpuDocumentMetadata`.
- import/re-export: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.

**Exact class source**

```python
class GpuDocumentMetadata:
    provider: str
    portal: str
    commune_code: str
    partition: str
    document_id: str
    document_family: str
    document_type: str
    document_title: str | None
    status: str
    legal_status: str
    effective_status: str
    version: str | None
    archive_name: str
    publication_timestamp: str | None
    update_timestamp: str | None
    revision_date: str | None
    producer: str | None
    standard_model: str | None
    projection: str | None
    metadata_identifier: str | None
    source_url: str
    written_files: tuple[GpuWrittenFile, ...]
```

### `GpuArchiveDownload`

**Purpose:** Immutable result/value envelope carrying `document`, `download_timestamp`, `filename`, `archive_format`, `file_size`, `sha256`, `path`, `cache_hit`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `document` | `document: GpuDocumentMetadata` | Stores `GpuArchiveDownload`'s `document` value under exact annotation `GpuDocumentMetadata`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `download_timestamp` | `download_timestamp: str` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `filename` | `filename: str` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `archive_format` | `archive_format: str` | Closed or validated `archive format` classification on `GpuArchiveDownload`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `file_size` | `file_size: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `path` | `path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `cache_hit` | `cache_hit: bool` | True only when already verified local cache state was reused. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- callback/function object: `src/landscout/sources/gpu_fr.py::_validate_gpu_archive_download` via `isinstance(download, GpuArchiveDownload)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_load_cached_archive` via `GpuArchiveDownload`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `GpuArchiveDownload`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::_validate_document_lineage` via `isinstance(archive, GpuArchiveDownload)`.
- import/re-export: `src/landscout/stages/index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `GpuArchiveDownload`.
- import/re-export: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_planning_document` via `GpuArchiveDownload`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_gpu_fr.py::_extraction_from_archive` via `GpuArchiveDownload`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_document` via `GpuArchiveDownload`.
- import/re-export: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_planning_document` via `GpuArchiveDownload`.
- import/re-export: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.

**Exact class source**

```python
class GpuArchiveDownload:
    document: GpuDocumentMetadata
    download_timestamp: str
    filename: str
    archive_format: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool
```

### `GpuExtractedFile`

**Purpose:** Immutable result/value envelope carrying `relative_path`, `file_type`, `size_bytes`, `sha256`, `category`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `relative_path` | `relative_path: str` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `file_type` | `file_type: str` | Closed or validated `file type` classification on `GpuExtractedFile`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `size_bytes` | `size_bytes: int` | Stores `GpuExtractedFile`'s `size bytes` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `category` | `category: FileCategory` | Stores `GpuExtractedFile`'s `category` value under exact annotation `FileCategory`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_inventory` via `GpuExtractedFile`.
- callback/function object: `src/landscout/sources/gpu_fr.py::_spatial_inventory` via `isinstance(item, GpuExtractedFile)`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `isinstance(item, GpuExtractedFile)`.
- import/re-export: `src/landscout/stages/index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_physical_inventory` via `GpuExtractedFile`.
- import/re-export: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_physical_planning_document` via `GpuExtractedFile`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_inventory_item` via `GpuExtractedFile`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_spatial_inventory_item` via `GpuExtractedFile`.
- import/re-export: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_physical_inventory` via `GpuExtractedFile`.
- import/re-export: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.

**Exact class source**

```python
class GpuExtractedFile:
    relative_path: str
    file_type: str
    size_bytes: int
    sha256: str
    category: FileCategory
```

### `GpuExtraction`

**Purpose:** Immutable result/value envelope carrying `archive`, `extraction_root`, `files`, `standard_models`, `cache_hit`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `archive` | `archive: GpuArchiveDownload` | Stores `GpuExtraction`'s `archive` value under exact annotation `GpuArchiveDownload`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `extraction_root` | `extraction_root: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `files` | `files: tuple[GpuExtractedFile, ...]` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |
| `standard_models` | `standard_models: tuple[str, ...]` | Structured `standard models` collection owned by `GpuExtraction`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `cache_hit` | `cache_hit: bool` | True only when already verified local cache state was reused. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `GpuExtraction`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::_validate_document_lineage` via `isinstance(extraction, GpuExtraction)`.
- import/re-export: `src/landscout/stages/index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `GpuExtraction`.
- import/re-export: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_planning_document` via `GpuExtraction`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_document` via `GpuExtraction`.
- import/re-export: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_planning_document` via `GpuExtraction`.
- import/re-export: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.

**Exact class source**

```python
class GpuExtraction:
    archive: GpuArchiveDownload
    extraction_root: Path
    files: tuple[GpuExtractedFile, ...]
    standard_models: tuple[str, ...]
    cache_hit: bool
```

### `GpuSpatialLayerReference`

**Purpose:** Immutable result/value envelope carrying `dataset_path`, `source_layer`, `driver`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `dataset_path` | `dataset_path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `source_layer` | `source_layer: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `driver` | `driver: str` | Stores `GpuSpatialLayerReference`'s `driver` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_gpu_spatial_layers` via `GpuSpatialLayerReference`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_inspected` via `GpuSpatialLayerReference`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `GpuSpatialLayerReference`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_source_complete_contract` via `GpuSpatialLayerReference`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_ogr_fid_source_complete_contract` via `GpuSpatialLayerReference`.
- import/re-export: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_planning_document` via `GpuSpatialLayerReference`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_write_zoning_source` via `GpuSpatialLayerReference`.
- import/re-export: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_planning_document` via `GpuSpatialLayerReference`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_integration_layer` via `GpuSpatialLayerReference`.
- import/re-export: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.

**Exact class source**

```python
class GpuSpatialLayerReference:
    dataset_path: Path
    source_layer: str
    driver: str
```

### `GpuLayerSummary`

**Purpose:** Immutable result/value envelope carrying `source_document_id`, `source_archive_sha256`, `source_layer`, `crs`, `feature_count`, `columns`, `dtypes`, `null_counts`, `geometry_types`, `null_geometry_count`, `empty_geometry_count`, `invalid_geometry_count`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `source_document_id` | `source_document_id: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_layer` | `source_layer: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `crs` | `crs: str` | Coordinate reference system identity; exact accepted/storage/calculation behavior is enforced by the owning CRS validator. |
| `feature_count` | `feature_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `columns` | `columns: tuple[str, ...]` | Structured `columns` collection owned by `GpuLayerSummary`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `dtypes` | `dtypes: tuple[tuple[str, str], ...]` | Closed or validated `dtypes` classification on `GpuLayerSummary`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `null_counts` | `null_counts: tuple[tuple[str, int], ...]` | Structured `null counts` collection owned by `GpuLayerSummary`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `geometry_types` | `geometry_types: tuple[tuple[str, int], ...]` | Closed or validated `geometry types` classification on `GpuLayerSummary`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `null_geometry_count` | `null_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `empty_geometry_count` | `empty_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `invalid_geometry_count` | `invalid_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_summarize_layer` via `GpuLayerSummary`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_summary` via `GpuLayerSummary`.
- import/re-export: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_planning_document` via `GpuLayerSummary`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_summary` via `GpuLayerSummary`.
- import/re-export: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_layer_summary` via `GpuLayerSummary`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_integration_layer` via `GpuLayerSummary`.
- import/re-export: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.

**Exact class source**

```python
class GpuLayerSummary:
    source_document_id: str
    source_archive_sha256: str
    source_layer: str
    crs: str
    feature_count: int
    columns: tuple[str, ...]
    dtypes: tuple[tuple[str, str], ...]
    null_counts: tuple[tuple[str, int], ...]
    geometry_types: tuple[tuple[str, int], ...]
    null_geometry_count: int
    empty_geometry_count: int
    invalid_geometry_count: int
```

### `GpuInspectedLayer`

**Purpose:** Immutable result/value envelope carrying `logical_name`, `reference`, `data`, `summary`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `logical_name` | `logical_name: LogicalLayerName` | Stores `GpuInspectedLayer`'s `logical name` value under exact annotation `LogicalLayerName`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `reference` | `reference: GpuSpatialLayerReference` | `GpuInspectedLayer`'s `reference` evidence/text field; it retains the exact configured or source meaning under annotation `GpuSpatialLayerReference` and is not promoted to a legal conclusion. |
| `data` | `data: gpd.GeoDataFrame` | Stores `GpuInspectedLayer`'s `data` value under exact annotation `gpd.GeoDataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `summary` | `summary: GpuLayerSummary` | Stores `GpuInspectedLayer`'s `summary` value under exact annotation `GpuLayerSummary`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- callback/function object: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `isinstance(inspected_layer, GpuInspectedLayer)`.
- callback/function object: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_sources` via `isinstance(layer, GpuInspectedLayer)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::inspect_gpu_planning_document` via `GpuInspectedLayer`.
- import/re-export: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`.
- import/re-export: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import GpuInspectedLayer, GpuPlanningDocument`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_inspected` via `GpuInspectedLayer`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `GpuInspectedLayer`.
- import/re-export: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_planning_document` via `GpuInspectedLayer`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_write_zoning_source` via `GpuInspectedLayer`.
- import/re-export: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_planning_document` via `GpuInspectedLayer`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_integration_layer` via `GpuInspectedLayer`.
- import/re-export: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.

**Exact class source**

```python
class GpuInspectedLayer:
    logical_name: LogicalLayerName
    reference: GpuSpatialLayerReference
    data: gpd.GeoDataFrame
    summary: GpuLayerSummary
```

### `GpuSpatialSourceFileIntegrity`

**Purpose:** One verified physical member of an extracted GPU spatial dataset.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `relative_path` | `relative_path: str` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `file_type` | `file_type: str` | Closed or validated `file type` classification on `GpuSpatialSourceFileIntegrity`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `size_bytes` | `size_bytes: int` | Stores `GpuSpatialSourceFileIntegrity`'s `size bytes` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `category` | `category: str` | Stores `GpuSpatialSourceFileIntegrity`'s `category` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `GpuSpatialSourceFileIntegrity`.

**Exact class source**

```python
class GpuSpatialSourceFileIntegrity:
    """One verified physical member of an extracted GPU spatial dataset."""

    relative_path: str
    file_type: str
    size_bytes: int
    sha256: str
    category: str
```

### `GpuValidatedSpatialLayerSource`

**Purpose:** Freshly reloaded GPU layer plus its extraction-inventory evidence.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `logical_name` | `logical_name: LogicalLayerName` | Stores `GpuValidatedSpatialLayerSource`'s `logical name` value under exact annotation `LogicalLayerName`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `source_layer` | `source_layer: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `driver` | `driver: str` | Stores `GpuValidatedSpatialLayerSource`'s `driver` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `dataset_relative_path` | `dataset_relative_path: str` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `source_crs` | `source_crs: str` | Coordinate reference system identity; exact accepted/storage/calculation behavior is enforced by the owning CRS validator. |
| `feature_count` | `feature_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `files` | `files: tuple[GpuSpatialSourceFileIntegrity, ...]` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |
| `ogr_fids` | `ogr_fids: tuple[int, ...]` | Structured `ogr fids` collection owned by `GpuValidatedSpatialLayerSource`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `data` | `data: gpd.GeoDataFrame` | Stores `GpuValidatedSpatialLayerSource`'s `data` value under exact annotation `gpd.GeoDataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `GpuValidatedSpatialLayerSource`.
- import/re-export: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`.

**Exact class source**

```python
class GpuValidatedSpatialLayerSource:
    """Freshly reloaded GPU layer plus its extraction-inventory evidence."""

    logical_name: LogicalLayerName
    source_layer: str
    driver: str
    dataset_relative_path: str
    source_crs: str
    feature_count: int
    files: tuple[GpuSpatialSourceFileIntegrity, ...]
    ogr_fids: tuple[int, ...]
    data: gpd.GeoDataFrame
```

### `GpuPlanningDocument`

**Purpose:** Immutable result/value envelope carrying `extraction`, `all_spatial_layers`, `zoning`, `related_layers`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `extraction` | `extraction: GpuExtraction` | `GpuPlanningDocument`'s `extraction` evidence/text field; it retains the exact configured or source meaning under annotation `GpuExtraction` and is not promoted to a legal conclusion. |
| `all_spatial_layers` | `all_spatial_layers: tuple[GpuSpatialLayerReference, ...]` | Structured `all spatial layers` collection owned by `GpuPlanningDocument`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `zoning` | `zoning: GpuInspectedLayer` | Stores `GpuPlanningDocument`'s `zoning` value under exact annotation `GpuInspectedLayer`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `related_layers` | `related_layers: tuple[GpuInspectedLayer, ...]` | Structured `related layers` collection owned by `GpuPlanningDocument`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- callback/function object: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `isinstance(planning_document, GpuPlanningDocument)`.
- callback/function object: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_sources` via `isinstance(planning_document, GpuPlanningDocument)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::inspect_gpu_planning_document` via `GpuPlanningDocument`.
- import/re-export: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.sources.gpu_fr import GpuPlanningDocument`.
- import/re-export: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.sources.gpu_fr import GpuPlanningDocument`.
- import/re-export: `src/landscout/stages/bess_planning_feature_policy.py::<module>` via `from landscout.sources.gpu_fr import GpuPlanningDocument`.
- callback/function object: `src/landscout/stages/enrich_planning_features.py::_planning_context` via `isinstance(document, GpuPlanningDocument)`.
- import/re-export: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`.
- callback/function object: `src/landscout/stages/enrich_planning_zoning.py::_validate_planning_document` via `isinstance(planning_document, GpuPlanningDocument)`.
- import/re-export: `src/landscout/stages/enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    revalidate_gpu_spatial_layer_sources,
)`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::_validate_document_lineage` via `isinstance(planning_document, GpuPlanningDocument)`.
- import/re-export: `src/landscout/stages/index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`.
- import/re-export: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.sources.gpu_fr import GpuPlanningDocument`.
- callback/function object: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_standard` via `isinstance(document, GpuPlanningDocument)`.
- import/re-export: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import GpuInspectedLayer, GpuPlanningDocument`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `GpuPlanningDocument`.
- import/re-export: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_planning_document` via `GpuPlanningDocument`.
- import/re-export: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_document` via `GpuPlanningDocument`.
- import/re-export: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    GpuWrittenFile,
)`.
- direct call or construction: `tests/unit/test_resolve_planning_feature_codes.py::_planning_document` via `GpuPlanningDocument`.
- import/re-export: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)`.

**Exact class source**

```python
class GpuPlanningDocument:
    extraction: GpuExtraction
    all_spatial_layers: tuple[GpuSpatialLayerReference, ...]
    zoning: GpuInspectedLayer
    related_layers: tuple[GpuInspectedLayer, ...]
```


## 6. Functions and methods

### `GpuApiConfig._official_api`

**Exact signature**

```python
def _official_api(cls, value: HttpUrl) -> HttpUrl:
```

**Purpose**

Private `planning` helper for official api; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `HttpUrl`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `parsed.scheme != 'https' or parsed.hostname != 'www.geoportail-urbanisme.gouv.fr' or parsed.port not in {None, 443} or (parsed.username is not None) or (parsed.password is not None) or (parsed.path.rstrip('/') != '/api') or parsed.params or parsed.query or parsed.fragment`.
- Explicit raise expressions: `ValueError('GPU API URL must use the exact official HTTPS /api base')`.

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
def _official_api(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlparse(str(value))
        if (
            parsed.scheme != "https"
            or parsed.hostname != "www.geoportail-urbanisme.gouv.fr"
            or parsed.port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path.rstrip("/") != "/api"
            or parsed.params
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("GPU API URL must use the exact official HTTPS /api base")
        return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `GpuDownloadConfig._valid_partition_template`

**Exact signature**

```python
def _valid_partition_template(cls, value: str) -> str:
```

**Purpose**

Private `planning` helper for valid partition template; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `value != value.strip() or value.count('{code_insee}') != 1`.
- Guard with a raise path: `not rendered or '/' in rendered or '\\' in rendered`.
- Explicit raise expressions: `ValueError('partition_template is malformed')`, `ValueError('partition_template must contain exactly one {code_insee} placeholder')`, `ValueError('partition_template must render one safe path component')`.

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
def _valid_partition_template(cls, value: str) -> str:
        if value != value.strip() or value.count("{code_insee}") != 1:
            raise ValueError(
                "partition_template must contain exactly one {code_insee} placeholder"
            )
        try:
            rendered = value.format(code_insee="31395")
        except (KeyError, ValueError) as error:
            raise ValueError("partition_template is malformed") from error
        if not rendered or "/" in rendered or "\\" in rendered:
            raise ValueError("partition_template must render one safe path component")
        return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `GpuLogicalLayerConfig._unique_tokens`

**Exact signature**

```python
def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:
```

**Purpose**

Private `planning` helper for unique tokens; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
values
```

**Validation and exceptions**

- Guard with a raise path: `any((not value for value in normalized))`.
- Guard with a raise path: `len(normalized) != len(set(normalized))`.
- Explicit raise expressions: `ValueError('Layer match tokens must be unique after normalization')`, `ValueError('Layer match tokens must contain letters or digits')`.

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
def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(value) for value in values)
        if any(not value for value in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(normalized) != len(set(normalized)):
            raise ValueError("Layer match tokens must be unique after normalization")
        return values
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalize_words`

**Exact signature**

```python
def _normalize_words(value: str) -> str:
```

**Purpose**

Projects validated source facts into words; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
'_'.join(re.findall('[a-z0-9]+', ascii_value.casefold()))
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

- direct call or construction: `src/landscout/sources/gpu_fr.py::GpuLogicalLayerConfig._unique_tokens` via `_normalize_words`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_discover_logical_layer` via `_normalize_words`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoLogicalLayerConfig._unique_tokens` via `_normalize_words`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoLogicalLayersConfig._different_token_sets` via `_normalize_words`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_matching_layers` via `_normalize_words`.

**Complete source-ordered implementation**

```python
def _normalize_words(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_value = "".join(char for char in decomposed if not unicodedata.combining(char))
    return "_".join(re.findall(r"[a-z0-9]+", ascii_value.casefold()))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_gpu_source_config`

**Exact signature**

```python
def load_gpu_source_config(path: Path = DEFAULT_CONFIG_PATH) -> GpuSourceConfig:
```

**Purpose**

Load and validate the strict GPU source configuration.

**Return contract**

- Declared return annotation: `GpuSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
GpuSourceConfig.model_validate(payload)
```

**Validation and exceptions**

- Guard with a raise path: `not path.is_file()`.
- Guard with a raise path: `not isinstance(payload, dict)`.
- Explicit raise expressions: `GpuConfigError(f'GPU source configuration does not exist: {path}')`, `GpuConfigError(f'Invalid GPU source configuration: {path}')`, `TypeError('GPU source configuration must be a mapping')`.

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

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `tests/unit/test_gpu_fr.py::_config` via `load_gpu_source_config`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def load_gpu_source_config(path: Path = DEFAULT_CONFIG_PATH) -> GpuSourceConfig:
    """Load and validate the strict GPU source configuration."""

    if not path.is_file():
        raise GpuConfigError(f"GPU source configuration does not exist: {path}")
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise TypeError("GPU source configuration must be a mapping")
        return GpuSourceConfig.model_validate(payload)
    except (OSError, TypeError, yaml.YAMLError, ValidationError) as error:
        raise GpuConfigError(f"Invalid GPU source configuration: {path}") from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_source_config`

**Exact signature**

```python
def _validated_source_config(config: object) -> GpuSourceConfig:
```

**Purpose**

Checks and returns canonical source config; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `GpuSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
GpuSourceConfig.model_validate(config.model_dump(mode='python'))
```

**Validation and exceptions**

- Guard with a raise path: `type(config) is not GpuSourceConfig`.
- Explicit raise expressions: `GpuConfigError('GPU source config no longer satisfies the official origin contract')`, `TypeError('GPU source config type is invalid')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::build_gpu_partition` via `_validated_source_config`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::build_gpu_document_list_url` via `_validated_source_config`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::build_gpu_partition_download_url` via `_validated_source_config`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `_validated_source_config`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `_validated_source_config`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::build_rte_odre_metadata_url` via `_validated_source_config`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::build_rte_odre_export_url` via `_validated_source_config`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `_validated_source_config`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_validated_source_config`.

**Complete source-ordered implementation**

```python
def _validated_source_config(config: object) -> GpuSourceConfig:
    try:
        if type(config) is not GpuSourceConfig:
            raise TypeError("GPU source config type is invalid")
        return GpuSourceConfig.model_validate(config.model_dump(mode="python"))
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise GpuConfigError(
            "GPU source config no longer satisfies the official origin contract"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `build_gpu_partition`

**Exact signature**

```python
def build_gpu_partition(config: GpuSourceConfig, commune_code: str | None = None) -> str:
```

**Purpose**

Constructs gpu partition; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
validated_config.download.partition_template.format(code_insee=code)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(code, str) or re.fullmatch('[0-9]{5}', code) is None`.
- Explicit raise expressions: `GpuConfigError('GPU commune code must contain exactly five digits')`.

**Side effects**

- Network I/O: `validated_config.download.partition_template.format`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::build_gpu_document_list_url` via `build_gpu_partition`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::build_gpu_partition_download_url` via `build_gpu_partition`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `build_gpu_partition`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_document_for_config` via `build_gpu_partition`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_valid_config_and_urls` via `build_gpu_partition`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def build_gpu_partition(config: GpuSourceConfig, commune_code: str | None = None) -> str:
    validated_config = _validated_source_config(config)
    code = commune_code or validated_config.pilot.commune_code
    if not isinstance(code, str) or re.fullmatch(r"[0-9]{5}", code) is None:
        raise GpuConfigError("GPU commune code must contain exactly five digits")
    return validated_config.download.partition_template.format(code_insee=code)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_api_url`

**Exact signature**

```python
def _api_url(config: GpuSourceConfig, path: str) -> str:
```

**Purpose**

Private `planning` helper for api url; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
urljoin(f"{str(config.api.base_url).rstrip('/')}/", path.lstrip('/'))
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

- direct call or construction: `src/landscout/sources/gpu_fr.py::build_gpu_document_list_url` via `_api_url`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::build_gpu_partition_download_url` via `_api_url`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_written_files` via `_api_url`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `_api_url`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_document_for_config` via `_api_url`.

**Complete source-ordered implementation**

```python
def _api_url(config: GpuSourceConfig, path: str) -> str:
    return urljoin(f"{str(config.api.base_url).rstrip('/')}/", path.lstrip("/"))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `build_gpu_document_list_url`

**Exact signature**

```python
def build_gpu_document_list_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
```

**Purpose**

Constructs gpu document list url; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
f"{_api_url(validated_config, 'document')}?{query}"
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

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `build_gpu_document_list_url`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_valid_config_and_urls` via `build_gpu_document_list_url`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def build_gpu_document_list_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
    validated_config = _validated_source_config(config)
    query = urlencode(
        {
            "partition": build_gpu_partition(validated_config, commune_code),
            "page": 0,
            "limit": 100,
        }
    )
    return f"{_api_url(validated_config, 'document')}?{query}"
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `build_gpu_partition_download_url`

**Exact signature**

```python
def build_gpu_partition_download_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
```

**Purpose**

Constructs gpu partition download url; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_api_url(validated_config, f'document/download-by-partition/{partition}')
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

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `build_gpu_partition_download_url`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_document_for_config` via `build_gpu_partition_download_url`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_valid_config_and_urls` via `build_gpu_partition_download_url`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def build_gpu_partition_download_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
    validated_config = _validated_source_config(config)
    partition = quote(build_gpu_partition(validated_config, commune_code), safe="")
    return _api_url(
        validated_config, f"document/download-by-partition/{partition}"
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_request_json`

**Exact signature**

```python
def _request_json(url: str, timeout: float) -> Any:
```

**Purpose**

Private `planning` helper for request json; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Any`.
- Every observed return expression is reproduced without truncation:
```python
json.loads(response.read().decode('utf-8'))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `GpuDiscoveryError(f'GPU metadata request failed: {url}')`.

**Side effects**

- Network I/O: `open_safe_https`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `_request_json`.

**Complete source-ordered implementation**

```python
def _request_json(url: str, timeout: float) -> Any:
    try:
        with open_safe_https(
            url,
            timeout=timeout,
            headers={"Accept": "application/json", "User-Agent": USER_AGENT},
        ) as response:
            return json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise GpuDiscoveryError(f"GPU metadata request failed: {url}") from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_required_string`

**Exact signature**

```python
def _required_string(payload: dict[str, Any], key: str, label: str) -> str:
```

**Purpose**

Private `planning` helper for required string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value.strip()`.
- Explicit raise expressions: `GpuDiscoveryError(f'GPU {label} is missing or invalid')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_written_files` via `_required_string`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `_required_string`.

**Complete source-ordered implementation**

```python
def _required_string(payload: dict[str, Any], key: str, label: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise GpuDiscoveryError(f"GPU {label} is missing or invalid")
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_optional_string`

**Exact signature**

```python
def _optional_string(payload: dict[str, Any], *keys: str) -> str | None:
```

**Purpose**

Private `planning` helper for optional string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str | None`.
- Every observed return expression is reproduced without truncation:
```python
None

text
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, (str, int, float)) or isinstance(value, bool)`.
- Explicit raise expressions: `GpuDiscoveryError(f'GPU metadata field {key} has an invalid value')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_written_files` via `_optional_string`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `_optional_string`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::fetch_rte_odre_dataset_metadata` via `_optional_string`.

**Complete source-ordered implementation**

```python
def _optional_string(payload: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = payload.get(key)
        if value is None:
            continue
        if not isinstance(value, (str, int, float)) or isinstance(value, bool):
            raise GpuDiscoveryError(f"GPU metadata field {key} has an invalid value")
        text = str(value)
        if text.strip():
            return text
    return None
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_written_files`

**Exact signature**

```python
def _written_files(
    details: dict[str, Any],
    payload: Any,
    document_id: str,
    config: GpuSourceConfig,
) -> tuple[GpuWrittenFile, ...]:
```

**Purpose**

Private `planning` helper for written files; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[GpuWrittenFile, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(sorted(result, key=lambda item: item.filename.casefold()))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, list)`.
- Guard with a raise path: `not isinstance(item, dict)`.
- Guard with a raise path: `filename in seen`.
- Guard with a raise path: `source_url is not None and source_url != expected_source_url`.
- Explicit raise expressions: `GpuDiscoveryError('GPU written material URL is not the exact official HTTPS API URL')`, `GpuDiscoveryError('GPU written-file entry is invalid')`, `GpuDiscoveryError('GPU written-file metadata is not a list')`, `GpuDiscoveryError(f'Duplicate GPU written filename: {filename}')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `_written_files`.

**Complete source-ordered implementation**

```python
def _written_files(
    details: dict[str, Any],
    payload: Any,
    document_id: str,
    config: GpuSourceConfig,
) -> tuple[GpuWrittenFile, ...]:
    if not isinstance(payload, list):
        raise GpuDiscoveryError("GPU written-file metadata is not a list")
    materials = details.get("writingMaterials")
    material_urls = materials if isinstance(materials, dict) else {}
    result: list[GpuWrittenFile] = []
    seen: set[str] = set()
    for item in payload:
        if not isinstance(item, dict):
            raise GpuDiscoveryError("GPU written-file entry is invalid")
        filename = _required_string(item, "name", "written filename")
        if filename in seen:
            raise GpuDiscoveryError(f"Duplicate GPU written filename: {filename}")
        seen.add(filename)
        expected_source_url = _api_url(
            config,
            "document/"
            f"{quote(document_id, safe='')}/files/{quote(filename, safe='')}",
        )
        source_url = material_urls.get(filename)
        if source_url is not None and source_url != expected_source_url:
            raise GpuDiscoveryError(
                "GPU written material URL is not the exact official HTTPS API URL"
            )
        result.append(
            GpuWrittenFile(
                filename=filename,
                title=_optional_string(item, "title"),
                document_path=_optional_string(item, "path"),
                source_url=expected_source_url,
            )
        )
    return tuple(sorted(result, key=lambda item: item.filename.casefold()))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `discover_current_gpu_document`

**Exact signature**

```python
def discover_current_gpu_document(
    config: GpuSourceConfig, commune_code: str | None = None, timeout: float = 60.0
) -> GpuDocumentMetadata:
```

**Purpose**

Resolve exactly one official production, approved and in-force DU.

**Return contract**

- Declared return annotation: `GpuDocumentMetadata`.
- Every observed return expression is reproduced without truncation:
```python
GpuDocumentMetadata(provider=validated_config.provider, portal=validated_config.portal, commune_code=code, partition=partition, document_id=document_id, document_family='DU', document_type=document_type, document_title=_optional_string(details, 'title'), status=_required_string(details, 'status', 'status'), legal_status=_required_string(details, 'legalStatus', 'legal status'), effective_status=_required_string(details, 'effectiveStatus', 'effective status'), version=_optional_string(details, 'version'), archive_name=archive_name, publication_timestamp=_optional_string(details, 'publicationDate'), update_timestamp=_optional_string(details, 'updateDate'), revision_date=_optional_string(details, 'revisionDate', 'referenceDate'), producer=_optional_string(details, 'producer'), standard_model=_optional_string(details, 'standard', 'model', 'documentModel'), projection=_optional_string(details, 'projectionCode'), metadata_identifier=_optional_string(details, 'metadata', 'fileIdentifier'), source_url=source_url, written_files=_written_files(details, files_payload, document_id, validated_config))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(listing, list)`.
- Guard with a raise path: `not current`.
- Guard with a raise path: `len(current) != 1`.
- Guard with a raise path: `not isinstance(details_payload, dict)`.
- Guard with a raise path: `details.get('id') != document_id or details.get('originalName') != archive_name`.
- Guard with a raise path: `any((details.get(key) != value for key, value in expected_state.items()))`.
- Guard with a raise path: `not isinstance(detail_grid, dict) or detail_grid.get('name') != code`.
- Guard with a raise path: `details.get('name') != partition`.
- Guard with a raise path: `details.get('archiveUrl') != expected_details_archive_url`.
- Guard with a raise path: `listing_type != document_type`.
- Explicit raise expressions: `GpuDiscoveryError('GPU archive name is unsafe')`, `GpuDiscoveryError('GPU document archive URL is not the exact official HTTPS API URL')`, `GpuDiscoveryError('GPU document details are not an object')`, `GpuDiscoveryError('GPU document details do not match the commune')`, `GpuDiscoveryError('GPU document details do not match the partition')`, `GpuDiscoveryError('GPU document details do not match the selected document')`, `GpuDiscoveryError('GPU document details no longer describe a current approved and in-force document')`, `GpuDiscoveryError('GPU document listing is not a list')`, `GpuDiscoveryError('GPU document type changed between listing and details')`, `GpuDiscoveryError('GPU source config is invalid')`, `GpuDiscoveryError(f'Ambiguous current GPU document selection for {partition}: {len(current)}')`, `GpuDiscoveryError(f'No current approved and in-force GPU document for {partition}')`.

**Side effects**

- Network I/O: `build_gpu_partition_download_url`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::ingest_gpu_planning_document` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::_document` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_written_material_url_must_be_exact_official_https_api_url` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_no_current_document_is_rejected` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_ambiguous_current_documents_are_rejected` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_missing_document_identity_is_rejected` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_document_details_must_match_selected_listing` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_document_details_commune_must_match_selected_listing` via `discover_current_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_discovery_rejects_unsafe_archive_name` via `discover_current_gpu_document`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def discover_current_gpu_document(
    config: GpuSourceConfig, commune_code: str | None = None, timeout: float = 60.0
) -> GpuDocumentMetadata:
    """Resolve exactly one official production, approved and in-force DU."""

    try:
        validated_config = _validated_source_config(config)
    except GpuConfigError as error:
        raise GpuDiscoveryError("GPU source config is invalid") from error
    code = commune_code or validated_config.pilot.commune_code
    partition = build_gpu_partition(validated_config, code)
    listing = _request_json(
        build_gpu_document_list_url(validated_config, code), timeout
    )
    if not isinstance(listing, list):
        raise GpuDiscoveryError("GPU document listing is not a list")
    current: list[dict[str, Any]] = []
    for item in listing:
        if not isinstance(item, dict):
            continue
        grid = item.get("grid")
        grid_code = grid.get("name") if isinstance(grid, dict) else None
        if (
            item.get("status") == "document.production"
            and item.get("legalStatus") == "APPROVED"
            and item.get("effectiveStatus") == "EN_VIGUEUR"
            and item.get("name") == partition
            and grid_code == code
        ):
            current.append(item)
    if not current:
        raise GpuDiscoveryError(
            f"No current approved and in-force GPU document for {partition}"
        )
    if len(current) != 1:
        raise GpuDiscoveryError(
            f"Ambiguous current GPU document selection for {partition}: {len(current)}"
        )

    selected = current[0]
    document_id = _required_string(selected, "id", "document ID")
    archive_name = _required_string(selected, "originalName", "archive name")
    listing_type = _required_string(selected, "type", "listing document type")
    try:
        archive_filename = _safe_gpu_archive_filename(archive_name)
    except GpuDownloadError as error:
        raise GpuDiscoveryError("GPU archive name is unsafe") from error
    details_url = _api_url(
        validated_config, f"document/{quote(document_id, safe='')}/details"
    )
    files_url = _api_url(
        validated_config, f"document/{quote(document_id, safe='')}/files"
    )
    details_payload = _request_json(details_url, timeout)
    if not isinstance(details_payload, dict):
        raise GpuDiscoveryError("GPU document details are not an object")
    details = details_payload
    if details.get("id") != document_id or details.get("originalName") != archive_name:
        raise GpuDiscoveryError("GPU document details do not match the selected document")
    expected_state = {
        "status": "document.production",
        "legalStatus": "APPROVED",
        "effectiveStatus": "EN_VIGUEUR",
    }
    if any(details.get(key) != value for key, value in expected_state.items()):
        raise GpuDiscoveryError(
            "GPU document details no longer describe a current approved and "
            "in-force document"
        )
    detail_grid = details.get("grid")
    if not isinstance(detail_grid, dict) or detail_grid.get("name") != code:
        raise GpuDiscoveryError("GPU document details do not match the commune")
    if details.get("name") != partition:
        raise GpuDiscoveryError("GPU document details do not match the partition")
    expected_details_archive_url = _api_url(
        validated_config,
        "document/"
        f"{quote(document_id, safe='')}/download/"
        f"{quote(archive_filename, safe='')}",
    )
    if details.get("archiveUrl") != expected_details_archive_url:
        raise GpuDiscoveryError(
            "GPU document archive URL is not the exact official HTTPS API URL"
        )
    document_type = _required_string(details, "type", "document type")
    if listing_type != document_type:
        raise GpuDiscoveryError("GPU document type changed between listing and details")
    files_payload = _request_json(files_url, timeout)
    source_url = build_gpu_partition_download_url(validated_config, code)
    return GpuDocumentMetadata(
        provider=validated_config.provider,
        portal=validated_config.portal,
        commune_code=code,
        partition=partition,
        document_id=document_id,
        document_family="DU",
        document_type=document_type,
        document_title=_optional_string(details, "title"),
        status=_required_string(details, "status", "status"),
        legal_status=_required_string(details, "legalStatus", "legal status"),
        effective_status=_required_string(details, "effectiveStatus", "effective status"),
        version=_optional_string(details, "version"),
        archive_name=archive_name,
        publication_timestamp=_optional_string(details, "publicationDate"),
        update_timestamp=_optional_string(details, "updateDate"),
        revision_date=_optional_string(details, "revisionDate", "referenceDate"),
        producer=_optional_string(details, "producer"),
        standard_model=_optional_string(details, "standard", "model", "documentModel"),
        projection=_optional_string(details, "projectionCode"),
        metadata_identifier=_optional_string(details, "metadata", "fileIdentifier"),
        source_url=source_url,
        written_files=_written_files(
            details,
            files_payload,
            document_id,
            validated_config,
        ),
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_safe_gpu_archive_filename`

**Exact signature**

```python
def _safe_gpu_archive_filename(archive_name: object) -> str:
```

**Purpose**

Private `planning` helper for safe gpu archive filename; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
filename
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(archive_name, str)`.
- Guard with a raise path: `not archive_name or archive_name != archive_name.strip()`.
- Guard with a raise path: `any((ord(character) < 32 or ord(character) == 127 for character in archive_name))`.
- Guard with a raise path: `normalized in {'.', '..'} or '/' in normalized or '\\' in normalized or PurePosixPath(normalized).is_absolute() or PureWindowsPath(normalized).is_absolute() or bool(PureWindowsPath(normalized).drive) or normalized.endswith((' ', '.')) or any((character in '<>:"/\\|?*' for character in normalized))`.
- Guard with a raise path: `normalized.casefold().endswith('.zip')`.
- Guard with a raise path: `not basename or normalized_basename in {'.', '..'} or normalized_basename.endswith((' ', '.'))`.
- Guard with a raise path: `windows_stem in _WINDOWS_RESERVED_BASENAMES`.
- Guard with a raise path: `len(unicodedata.normalize('NFKC', filename).encode('utf-16-le')) // 2 > 255`.
- Guard with a raise path: `normalized_basename.casefold().endswith('.zip')`.
- Explicit raise expressions: `GpuDownloadError('GPU archive filename exceeds Windows component limits')`, `GpuDownloadError('GPU archive name contains control characters')`, `GpuDownloadError('GPU archive name contains repeated .zip suffixes')`, `GpuDownloadError('GPU archive name has no safe logical basename')`, `GpuDownloadError('GPU archive name is empty or has edge whitespace')`, `GpuDownloadError('GPU archive name is not a safe local basename')`, `GpuDownloadError('GPU archive name is reserved on Windows')`, `GpuDownloadError('GPU archive name must be a string')`.

**Side effects**

- Network I/O: `GpuDownloadError`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_current_gpu_document` via `_safe_gpu_archive_filename`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_document_for_config` via `_safe_gpu_archive_filename`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_archive_download` via `_safe_gpu_archive_filename`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `gpu._safe_gpu_archive_filename`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `gpu._safe_gpu_archive_filename`.

**Complete source-ordered implementation**

```python
def _safe_gpu_archive_filename(archive_name: object) -> str:
    if not isinstance(archive_name, str):
        raise GpuDownloadError("GPU archive name must be a string")
    if not archive_name or archive_name != archive_name.strip():
        raise GpuDownloadError("GPU archive name is empty or has edge whitespace")
    if any(ord(character) < 32 or ord(character) == 127 for character in archive_name):
        raise GpuDownloadError("GPU archive name contains control characters")

    normalized = unicodedata.normalize("NFKC", archive_name)
    if (
        normalized in {".", ".."}
        or "/" in normalized
        or "\\" in normalized
        or PurePosixPath(normalized).is_absolute()
        or PureWindowsPath(normalized).is_absolute()
        or bool(PureWindowsPath(normalized).drive)
        or normalized.endswith((" ", "."))
        or any(character in '<>:"/\\|?*' for character in normalized)
    ):
        raise GpuDownloadError("GPU archive name is not a safe local basename")

    if normalized.casefold().endswith(".zip"):
        basename = archive_name[:-4]
        normalized_basename = normalized[:-4]
        if normalized_basename.casefold().endswith(".zip"):
            raise GpuDownloadError("GPU archive name contains repeated .zip suffixes")
    else:
        basename = archive_name
        normalized_basename = normalized
    if (
        not basename
        or normalized_basename in {".", ".."}
        or normalized_basename.endswith((" ", "."))
    ):
        raise GpuDownloadError("GPU archive name has no safe logical basename")
    windows_stem = normalized_basename.split(".", 1)[0].casefold()
    if windows_stem in _WINDOWS_RESERVED_BASENAMES:
        raise GpuDownloadError("GPU archive name is reserved on Windows")
    filename = f"{basename}.zip"
    if len(unicodedata.normalize("NFKC", filename).encode("utf-16-le")) // 2 > 255:
        raise GpuDownloadError("GPU archive filename exceeds Windows component limits")
    return filename
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_gpu_document_for_config`

**Exact signature**

```python
def _validate_gpu_document_for_config(
    document: GpuDocumentMetadata, config: GpuSourceConfig
) -> str:
```

**Purpose**

Rejects malformed or inconsistent gpu document for config; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_safe_gpu_archive_filename(document.archive_name)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(document, GpuDocumentMetadata)`.
- Guard with a raise path: `document.provider != config.provider or document.portal != config.portal`.
- Guard with a raise path: `type(document.document_id) is not str or not document.document_id or document.document_id != document.document_id.strip() or any((ord(character) < 32 or ord(character) == 127 for character in document.document_id))`.
- Guard with a raise path: `type(document.written_files) is not tuple`.
- Guard with a raise path: `not isinstance(code, str) or re.fullmatch('[0-9]{5}', code) is None`.
- Guard with a raise path: `code != config.pilot.commune_code`.
- Guard with a raise path: `document.partition != expected_partition`.
- Guard with a raise path: `document.document_family != 'DU'`.
- Guard with a raise path: `document.status != 'document.production' or document.legal_status != 'APPROVED' or document.effective_status != 'EN_VIGUEUR'`.
- Guard with a raise path: `not isinstance(document.source_url, str) or document.source_url != expected_url`.
- Guard with a raise path: `parsed.scheme != 'https' or parsed.hostname != 'www.geoportail-urbanisme.gouv.fr' or parsed.path != expected_parsed.path or parsed.params or parsed.query or parsed.fragment or (parsed.username is not None) or (parsed.password is not None)`.
- Guard with a raise path: `type(written_file) is not GpuWrittenFile`.
- Guard with a raise path: `type(filename) is not str or not filename or filename != filename.strip() or any((ord(character) < 32 or ord(character) == 127 for character in filename)) or (filename in written_filenames)`.
- Guard with a raise path: `written_file.source_url != expected_written_url`.
- Explicit raise expressions: `GpuDownloadError('GPU document ID is invalid')`, `GpuDownloadError('GPU document commune code is invalid')`, `GpuDownloadError('GPU document commune does not match configured pilot')`, `GpuDownloadError('GPU document commune/partition is invalid')`, `GpuDownloadError('GPU document family is not a planning document')`, `GpuDownloadError('GPU document is not current, approved, and in force')`, `GpuDownloadError('GPU document metadata object is invalid')`, `GpuDownloadError('GPU document partition does not match configuration')`, `GpuDownloadError('GPU document provider/portal does not match configuration')`, `GpuDownloadError('GPU document source URL has an unsafe identity')`, `GpuDownloadError('GPU document source URL is not the official partition URL')`, `GpuDownloadError('GPU document written filename is invalid')`, `GpuDownloadError('GPU document written source URL is not the exact official API URL')`, `GpuDownloadError('GPU document written-file provenance is invalid')`, `GpuDownloadError('GPU document written-file type is invalid')`.

**Side effects**

- Network I/O: `GpuDownloadError`, `build_gpu_partition_download_url`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `_validate_gpu_document_for_config`.

**Complete source-ordered implementation**

```python
def _validate_gpu_document_for_config(
    document: GpuDocumentMetadata, config: GpuSourceConfig
) -> str:
    if not isinstance(document, GpuDocumentMetadata):
        raise GpuDownloadError("GPU document metadata object is invalid")
    if document.provider != config.provider or document.portal != config.portal:
        raise GpuDownloadError("GPU document provider/portal does not match configuration")
    if (
        type(document.document_id) is not str
        or not document.document_id
        or document.document_id != document.document_id.strip()
        or any(
            ord(character) < 32 or ord(character) == 127
            for character in document.document_id
        )
    ):
        raise GpuDownloadError("GPU document ID is invalid")
    if type(document.written_files) is not tuple:
        raise GpuDownloadError("GPU document written-file provenance is invalid")
    written_filenames: set[str] = set()
    for written_file in document.written_files:
        if type(written_file) is not GpuWrittenFile:
            raise GpuDownloadError("GPU document written-file type is invalid")
        filename = written_file.filename
        if (
            type(filename) is not str
            or not filename
            or filename != filename.strip()
            or any(
                ord(character) < 32 or ord(character) == 127
                for character in filename
            )
            or filename in written_filenames
        ):
            raise GpuDownloadError("GPU document written filename is invalid")
        written_filenames.add(filename)
        expected_written_url = _api_url(
            config,
            "document/"
            f"{quote(document.document_id, safe='')}/files/"
            f"{quote(filename, safe='')}",
        )
        if written_file.source_url != expected_written_url:
            raise GpuDownloadError(
                "GPU document written source URL is not the exact official API URL"
            )
    code = document.commune_code
    if not isinstance(code, str) or re.fullmatch(r"[0-9]{5}", code) is None:
        raise GpuDownloadError("GPU document commune code is invalid")
    if code != config.pilot.commune_code:
        raise GpuDownloadError("GPU document commune does not match configured pilot")
    try:
        expected_partition = build_gpu_partition(config, code)
        expected_url = build_gpu_partition_download_url(config, code)
    except GpuConfigError as error:
        raise GpuDownloadError("GPU document commune/partition is invalid") from error
    if document.partition != expected_partition:
        raise GpuDownloadError("GPU document partition does not match configuration")
    if document.document_family != "DU":
        raise GpuDownloadError("GPU document family is not a planning document")
    if (
        document.status != "document.production"
        or document.legal_status != "APPROVED"
        or document.effective_status != "EN_VIGUEUR"
    ):
        raise GpuDownloadError("GPU document is not current, approved, and in force")
    if not isinstance(document.source_url, str) or document.source_url != expected_url:
        raise GpuDownloadError("GPU document source URL is not the official partition URL")
    parsed = urlparse(document.source_url)
    expected_parsed = urlparse(expected_url)
    if (
        parsed.scheme != "https"
        or parsed.hostname != "www.geoportail-urbanisme.gouv.fr"
        or parsed.path != expected_parsed.path
        or parsed.params
        or parsed.query
        or parsed.fragment
        or parsed.username is not None
        or parsed.password is not None
    ):
        raise GpuDownloadError("GPU document source URL has an unsafe identity")
    return _safe_gpu_archive_filename(document.archive_name)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_sha256`

**Exact signature**

```python
def _sha256(path: Path) -> str:
```

**Purpose**

Private `planning` helper for sha256; its complete implementation below is the authoritative behavioral contract.

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

- direct call or construction: `src/landscout/common/bess_application_contract.py::_validate_official_row` via `_sha256`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_sha256`.
- direct call or construction: `src/landscout/sources/cadastre_fr.py::_load_cached_download` via `_sha256`.
- direct call or construction: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_sha256`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_archive_download` via `_sha256`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_load_cached_archive` via `_sha256`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `_sha256`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_inventory` via `_sha256`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `_sha256`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `_sha256`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_load_cached_download` via `_sha256`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_sha256`.
- direct call or construction: `tests/unit/test_gpu_fr.py::_extraction_from_archive` via `gpu._sha256`.
- property/attribute access: `tests/unit/test_gpu_fr.py::_extraction_from_archive` via `gpu._sha256`.

**Complete source-ordered implementation**

```python
def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(DOWNLOAD_CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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
    return path.is_symlink() or path.is_junction()
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_gpu_archive_download`

**Exact signature**

```python
def _validate_gpu_archive_download(
    download: GpuArchiveDownload,
) -> tuple[str, ...]:
```

**Purpose**

Rejects malformed or inconsistent gpu archive download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
validate_gpu_archive(path)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(download, GpuArchiveDownload)`.
- Guard with a raise path: `not isinstance(download.document, GpuDocumentMetadata)`.
- Guard with a raise path: `not isinstance(path, Path) or _is_link_or_junction(path) or (not path.is_file())`.
- Guard with a raise path: `download.archive_format != 'zip'`.
- Guard with a raise path: `not isinstance(download.filename, str) or download.filename != path.name`.
- Guard with a raise path: `type(download.file_size) is not int or download.file_size <= 0`.
- Guard with a raise path: `not isinstance(download.sha256, str) or re.fullmatch('[0-9a-f]{64}', download.sha256) is None`.
- Guard with a raise path: `download.filename != expected_filename`.
- Guard with a raise path: `actual_size != download.file_size`.
- Guard with a raise path: `actual_sha256 != download.sha256`.
- Explicit raise expressions: `GpuArchiveError('Cannot read GPU archive bytes')`, `GpuArchiveError('GPU archive SHA256 does not match immutable download lineage')`, `GpuArchiveError('GPU archive document identity is invalid')`, `GpuArchiveError('GPU archive document lineage object is invalid')`, `GpuArchiveError('GPU archive download object is invalid')`, `GpuArchiveError('GPU archive filename does not match document lineage')`, `GpuArchiveError('GPU archive filename does not match its path')`, `GpuArchiveError('GPU archive object does not declare ZIP format')`, `GpuArchiveError('GPU archive object has an invalid SHA256')`, `GpuArchiveError('GPU archive object has an invalid file size')`, `GpuArchiveError('GPU archive path is not a regular local file')`, `GpuArchiveError('GPU archive size does not match immutable download lineage')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.stat`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `_validate_gpu_archive_download`.

**Complete source-ordered implementation**

```python
def _validate_gpu_archive_download(
    download: GpuArchiveDownload,
) -> tuple[str, ...]:
    if not isinstance(download, GpuArchiveDownload):
        raise GpuArchiveError("GPU archive download object is invalid")
    if not isinstance(download.document, GpuDocumentMetadata):
        raise GpuArchiveError("GPU archive document lineage object is invalid")
    path = download.path
    if not isinstance(path, Path) or _is_link_or_junction(path) or not path.is_file():
        raise GpuArchiveError("GPU archive path is not a regular local file")
    if download.archive_format != "zip":
        raise GpuArchiveError("GPU archive object does not declare ZIP format")
    if not isinstance(download.filename, str) or download.filename != path.name:
        raise GpuArchiveError("GPU archive filename does not match its path")
    if type(download.file_size) is not int or download.file_size <= 0:
        raise GpuArchiveError("GPU archive object has an invalid file size")
    if (
        not isinstance(download.sha256, str)
        or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
    ):
        raise GpuArchiveError("GPU archive object has an invalid SHA256")
    try:
        expected_filename = _safe_gpu_archive_filename(download.document.archive_name)
    except (AttributeError, GpuDownloadError) as error:
        raise GpuArchiveError("GPU archive document identity is invalid") from error
    if download.filename != expected_filename:
        raise GpuArchiveError("GPU archive filename does not match document lineage")
    try:
        actual_size = path.stat().st_size
        actual_sha256 = _sha256(path)
    except OSError as error:
        raise GpuArchiveError("Cannot read GPU archive bytes") from error
    if actual_size != download.file_size:
        raise GpuArchiveError(
            "GPU archive size does not match immutable download lineage"
        )
    if actual_sha256 != download.sha256:
        raise GpuArchiveError(
            "GPU archive SHA256 does not match immutable download lineage"
        )
    return validate_gpu_archive(path)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_safe_archive_member`

**Exact signature**

```python
def _safe_archive_member(name: str) -> bool:
```

**Purpose**

Private `planning` helper for safe archive member; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
not (posix.is_absolute() or windows.is_absolute() or windows.drive or any((part == '..' for part in posix.parts)))

False
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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_validated_zip_destinations` via `_safe_archive_member`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_extraction_manifest` via `_safe_archive_member`.

**Complete source-ordered implementation**

```python
def _safe_archive_member(name: str) -> bool:
    if not name or "\x00" in name:
        return False
    posix = PurePosixPath(name.replace("\\", "/"))
    windows = PureWindowsPath(name)
    return not (
        posix.is_absolute()
        or windows.is_absolute()
        or windows.drive
        or any(part == ".." for part in posix.parts)
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_windows_member_component`

**Exact signature**

```python
def _windows_member_component(component: str) -> str:
```

**Purpose**

Private `planning` helper for windows member component; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
normalized.casefold()
```

**Validation and exceptions**

- Guard with a raise path: `not normalized or normalized in {'.', '..'} or normalized.endswith((' ', '.')) or any((ord(character) < 32 or ord(character) == 127 for character in normalized)) or any((character in '<>:"/\\|?*' for character in normalized))`.
- Guard with a raise path: `stem in _WINDOWS_RESERVED_BASENAMES`.
- Explicit raise expressions: `GpuArchiveError(f'Reserved Windows ZIP component: {component}')`, `GpuArchiveError(f'Unsafe Windows-compatible ZIP component: {component}')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_validated_zip_destinations` via `_windows_member_component`.

**Complete source-ordered implementation**

```python
def _windows_member_component(component: str) -> str:
    normalized = unicodedata.normalize("NFKC", component)
    if (
        not normalized
        or normalized in {".", ".."}
        or normalized.endswith((" ", "."))
        or any(ord(character) < 32 or ord(character) == 127 for character in normalized)
        or any(character in '<>:"/\\|?*' for character in normalized)
    ):
        raise GpuArchiveError(f"Unsafe Windows-compatible ZIP component: {component}")
    stem = normalized.split(".", 1)[0].casefold()
    if stem in _WINDOWS_RESERVED_BASENAMES:
        raise GpuArchiveError(f"Reserved Windows ZIP component: {component}")
    return normalized.casefold()
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_zip_destinations`

**Exact signature**

```python
def _validated_zip_destinations(
    members: list[zipfile.ZipInfo],
) -> tuple[tuple[zipfile.ZipInfo, PurePosixPath], ...]:
```

**Purpose**

Checks and returns canonical zip destinations; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[tuple[zipfile.ZipInfo, PurePosixPath], ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(result)
```

**Validation and exceptions**

- Guard with a raise path: `raw_name in raw_names`.
- Guard with a raise path: `not _safe_archive_member(raw_name)`.
- Guard with a raise path: `stat.S_ISLNK(mode)`.
- Guard with a raise path: `member.create_system == 3 and file_type not in {0, stat.S_IFREG, stat.S_IFDIR}`.
- Guard with a raise path: `not parts`.
- Guard with a raise path: `canonical[0] == EXTRACTION_MANIFEST_NAME.casefold()`.
- Guard with a raise path: `canonical in explicit_destinations`.
- Guard with a raise path: `any((parent in file_destinations for parent in parents))`.
- Guard with a raise path: `is_directory`.
- Guard with a raise path: `canonical in file_destinations`.
- Guard with a raise path: `canonical in directory_destinations`.
- Explicit raise expressions: `GpuArchiveError('GPU ZIP member collides with extraction manifest')`, `GpuArchiveError(f'Duplicate member name in GPU ZIP: {raw_name}')`, `GpuArchiveError(f'GPU ZIP file/directory destination collision: {raw_name}')`, `GpuArchiveError(f'GPU ZIP member has no extraction target: {raw_name}')`, `GpuArchiveError(f'GPU ZIP members collide at one Windows-compatible destination: {previous} / {raw_name}')`, `GpuArchiveError(f'Special files are not allowed in GPU archive: {raw_name}')`, `GpuArchiveError(f'Symbolic links are not allowed in GPU archive: {raw_name}')`, `GpuArchiveError(f'Unsafe path in GPU archive: {raw_name}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `explicit_destinations[canonical]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::validate_gpu_archive` via `_validated_zip_destinations`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `_validated_zip_destinations`.

**Complete source-ordered implementation**

```python
def _validated_zip_destinations(
    members: list[zipfile.ZipInfo],
) -> tuple[tuple[zipfile.ZipInfo, PurePosixPath], ...]:
    raw_names: set[str] = set()
    explicit_destinations: dict[tuple[str, ...], str] = {}
    file_destinations: set[tuple[str, ...]] = set()
    directory_destinations: set[tuple[str, ...]] = set()
    result: list[tuple[zipfile.ZipInfo, PurePosixPath]] = []

    for member in members:
        raw_name = member.filename
        if raw_name in raw_names:
            raise GpuArchiveError(f"Duplicate member name in GPU ZIP: {raw_name}")
        raw_names.add(raw_name)
        if not _safe_archive_member(raw_name):
            raise GpuArchiveError(f"Unsafe path in GPU archive: {raw_name}")
        mode = member.external_attr >> 16
        if stat.S_ISLNK(mode):
            raise GpuArchiveError(
                f"Symbolic links are not allowed in GPU archive: {raw_name}"
            )
        file_type = stat.S_IFMT(mode)
        if member.create_system == 3 and file_type not in {
            0,
            stat.S_IFREG,
            stat.S_IFDIR,
        }:
            raise GpuArchiveError(f"Special files are not allowed in GPU archive: {raw_name}")

        destination = PurePosixPath(raw_name.replace("\\", "/"))
        parts = tuple(part for part in destination.parts if part not in {"", "."})
        if not parts:
            raise GpuArchiveError(f"GPU ZIP member has no extraction target: {raw_name}")
        canonical = tuple(_windows_member_component(part) for part in parts)
        if canonical[0] == EXTRACTION_MANIFEST_NAME.casefold():
            raise GpuArchiveError("GPU ZIP member collides with extraction manifest")
        if canonical in explicit_destinations:
            previous = explicit_destinations[canonical]
            raise GpuArchiveError(
                "GPU ZIP members collide at one Windows-compatible destination: "
                f"{previous} / {raw_name}"
            )
        explicit_destinations[canonical] = raw_name
        parents = tuple(canonical[:index] for index in range(1, len(canonical)))
        if any(parent in file_destinations for parent in parents):
            raise GpuArchiveError(
                f"GPU ZIP file/directory destination collision: {raw_name}"
            )
        is_directory = member.is_dir() or raw_name.endswith(("/", "\\"))
        if is_directory:
            if canonical in file_destinations:
                raise GpuArchiveError(
                    f"GPU ZIP file/directory destination collision: {raw_name}"
                )
            directory_destinations.add(canonical)
        else:
            if canonical in directory_destinations:
                raise GpuArchiveError(
                    f"GPU ZIP file/directory destination collision: {raw_name}"
                )
            file_destinations.add(canonical)
        directory_destinations.update(parents)
        result.append((member, PurePosixPath(*parts)))
    return tuple(result)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_gpu_archive`

**Exact signature**

```python
def validate_gpu_archive(path: Path) -> tuple[str, ...]:
```

**Purpose**

Fully validate a ZIP archive and return its deterministic member inventory.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(sorted((destination.as_posix() for _, destination in destinations), key=str.casefold))
```

**Validation and exceptions**

- Guard with a raise path: `not path.is_file() or path.stat().st_size <= 0`.
- Guard with a raise path: `not zipfile.is_zipfile(path)`.
- Guard with a raise path: `not members`.
- Guard with a raise path: `bad_member is not None`.
- Explicit raise expressions: `GpuArchiveError('GPU ZIP contains no members')`, `GpuArchiveError(f'Cannot validate GPU ZIP archive: {path}')`, `GpuArchiveError(f'Corrupt GPU ZIP member: {bad_member}')`, `GpuArchiveError(f'GPU archive is missing or empty: {path}')`, `GpuArchiveError(f'GPU archive is not a readable ZIP: {path}')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.stat`, `zipfile.ZipFile`, `zipfile.is_zipfile`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validate_gpu_archive_download` via `validate_gpu_archive`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_load_cached_archive` via `validate_gpu_archive`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `validate_gpu_archive`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_archive_path_traversal_is_rejected` via `validate_gpu_archive`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_archive_symlink_is_rejected` via `validate_gpu_archive`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_duplicate_zip_extraction_targets_are_rejected` via `validate_gpu_archive`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_zip_file_directory_target_collision_is_rejected` via `validate_gpu_archive`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_zip_cannot_claim_extraction_manifest_path` via `validate_gpu_archive`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def validate_gpu_archive(path: Path) -> tuple[str, ...]:
    """Fully validate a ZIP archive and return its deterministic member inventory."""

    if not path.is_file() or path.stat().st_size <= 0:
        raise GpuArchiveError(f"GPU archive is missing or empty: {path}")
    if not zipfile.is_zipfile(path):
        raise GpuArchiveError(f"GPU archive is not a readable ZIP: {path}")
    try:
        with zipfile.ZipFile(path) as archive:
            members = archive.infolist()
            if not members:
                raise GpuArchiveError("GPU ZIP contains no members")
            destinations = _validated_zip_destinations(members)
            bad_member = archive.testzip()
            if bad_member is not None:
                raise GpuArchiveError(f"Corrupt GPU ZIP member: {bad_member}")
    except GpuArchiveError:
        raise
    except (OSError, zipfile.BadZipFile, RuntimeError) as error:
        raise GpuArchiveError(f"Cannot validate GPU ZIP archive: {path}") from error
    return tuple(
        sorted((destination.as_posix() for _, destination in destinations), key=str.casefold)
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_document_identity`

**Exact signature**

```python
def _document_identity(document: GpuDocumentMetadata) -> dict[str, Any]:
```

**Purpose**

Private `planning` helper for document identity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, Any]`.
- Every observed return expression is reproduced without truncation:
```python
result
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
- In-memory mutation: `result['written_files']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `_document_identity`.

**Complete source-ordered implementation**

```python
def _document_identity(document: GpuDocumentMetadata) -> dict[str, Any]:
    result = asdict(document)
    result["written_files"] = [asdict(item) for item in document.written_files]
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_document_from_dict`

**Exact signature**

```python
def _document_from_dict(payload: Any) -> GpuDocumentMetadata:
```

**Purpose**

Private `planning` helper for document from dict; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuDocumentMetadata`.
- Every observed return expression is reproduced without truncation:
```python
GpuDocumentMetadata(**values, written_files=tuple(written))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, dict)`.
- Guard with a raise path: `not isinstance(files, list)`.
- Guard with a raise path: `not isinstance(item, dict)`.
- Explicit raise expressions: `TypeError('Cached GPU document metadata is invalid')`, `TypeError('Cached GPU written-file entry is invalid')`, `TypeError('Cached GPU written-file metadata is invalid')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_load_cached_archive` via `_document_from_dict`.

**Complete source-ordered implementation**

```python
def _document_from_dict(payload: Any) -> GpuDocumentMetadata:
    if not isinstance(payload, dict):
        raise TypeError("Cached GPU document metadata is invalid")
    values = dict(payload)
    files = values.pop("written_files")
    if not isinstance(files, list):
        raise TypeError("Cached GPU written-file metadata is invalid")
    written: list[GpuWrittenFile] = []
    for item in files:
        if not isinstance(item, dict):
            raise TypeError("Cached GPU written-file entry is invalid")
        written.append(GpuWrittenFile(**item))
    return GpuDocumentMetadata(**values, written_files=tuple(written))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_replace_file`

**Exact signature**

```python
def _replace_file(source: Path, target: Path) -> None:
```

**Purpose**

Private `planning` helper for replace file; its complete implementation below is the authoritative behavioral contract.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_cache_recovery_paths`

**Exact signature**

```python
def _cache_recovery_paths(
    archive_path: Path,
    metadata_path: Path,
) -> tuple[Path, Path]:
```

**Purpose**

Private `planning` helper for cache recovery paths; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::_require_no_cache_recovery_material` via `_cache_recovery_paths`.
- direct call or construction: `src/landscout/sources/cadastre_fr.py::_publish_cache_pair` via `_cache_recovery_paths`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_require_no_cache_recovery_material` via `_cache_recovery_paths`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_publish_cache_pair` via `_cache_recovery_paths`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_require_no_cache_recovery_material` via `_cache_recovery_paths`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_publish_cache_pair` via `_cache_recovery_paths`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_require_no_cache_recovery_material` via `_cache_recovery_paths`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_publish_cache_pair` via `_cache_recovery_paths`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_require_no_cache_recovery_material`

**Exact signature**

```python
def _require_no_cache_recovery_material(
    archive_path: Path,
    metadata_path: Path,
) -> None:
```

**Purpose**

Private `planning` helper for require no cache recovery material; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `any((path.exists() or _is_link_or_junction(path) for path in recovery_paths))`.
- Explicit raise expressions: `GpuDownloadError('GPU cache recovery backup already exists; manual recovery is required')`.

**Side effects**

- Network I/O: `GpuDownloadError`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::_publish_cache_pair` via `_require_no_cache_recovery_material`.
- direct call or construction: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_require_no_cache_recovery_material`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_publish_cache_pair` via `_require_no_cache_recovery_material`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `_require_no_cache_recovery_material`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_publish_cache_pair` via `_require_no_cache_recovery_material`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_require_no_cache_recovery_material`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_publish_cache_pair` via `_require_no_cache_recovery_material`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_require_no_cache_recovery_material`.

**Complete source-ordered implementation**

```python
def _require_no_cache_recovery_material(
    archive_path: Path,
    metadata_path: Path,
) -> None:
    recovery_paths = _cache_recovery_paths(archive_path, metadata_path)
    if any(
        path.exists() or _is_link_or_junction(path)
        for path in recovery_paths
    ):
        raise GpuDownloadError(
            "GPU cache recovery backup already exists; manual recovery is required"
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_prepare_temporary_cache_file`

**Exact signature**

```python
def _prepare_temporary_cache_file(path: Path) -> None:
```

**Purpose**

Private `planning` helper for prepare temporary cache file; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `_is_link_or_junction(path)`.
- Guard with a raise path: `path.exists()`.
- Guard with a raise path: `not path.is_file()`.
- Explicit raise expressions: `GpuDownloadError('GPU cache temporary path cannot be prepared safely')`, `GpuDownloadError('GPU cache temporary path is a link or junction')`, `GpuDownloadError('GPU cache temporary path is not a regular file')`, `re-raise`.

**Side effects**

- Network I/O: `GpuDownloadError`.
- Filesystem read: none directly visible.
- Filesystem write: `path.unlink`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_prepare_temporary_cache_file`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `_prepare_temporary_cache_file`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_prepare_temporary_cache_file`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_prepare_temporary_cache_file`.

**Complete source-ordered implementation**

```python
def _prepare_temporary_cache_file(path: Path) -> None:
    try:
        if _is_link_or_junction(path):
            raise GpuDownloadError(
                "GPU cache temporary path is a link or junction"
            )
        if path.exists():
            if not path.is_file():
                raise GpuDownloadError(
                    "GPU cache temporary path is not a regular file"
                )
            path.unlink()
    except GpuDownloadError:
        raise
    except OSError as error:
        raise GpuDownloadError(
            "GPU cache temporary path cannot be prepared safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_cleanup_temporary_cache_files`

**Exact signature**

```python
def _cleanup_temporary_cache_files(
    paths: tuple[Path, ...],
    primary_error: BaseException | None,
) -> None:
```

**Purpose**

Private `planning` helper for cleanup temporary cache files; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `cleanup_error is not None and primary_error is None`.
- Explicit raise expressions: `GpuDownloadError('GPU cache temporary files could not be cleaned safely')`.

**Side effects**

- Network I/O: `GpuDownloadError`.
- Filesystem read: none directly visible.
- Filesystem write: `path.unlink`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `_cleanup_temporary_cache_files`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `_cleanup_temporary_cache_files`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_cleanup_temporary_cache_files`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `_cleanup_temporary_cache_files`.

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
        raise GpuDownloadError(
            "GPU cache temporary files could not be cleaned safely"
        ) from cleanup_error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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

Private `planning` helper for publish cache pair; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `GpuDownloadError('GPU cache publication and rollback both failed')`, `re-raise`.

**Side effects**

- Network I/O: `GpuDownloadError`.
- Filesystem read: none directly visible.
- Filesystem write: `archive_backup.unlink`, `archive_path.unlink`, `metadata_backup.unlink`, `metadata_path.unlink`.
- CRS/geometry calculation: none directly visible.
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
    publication_started = False
    try:
        publication_started = True
        _replace_file(temporary_archive, archive_path)
        _replace_file(temporary_metadata, metadata_path)
    except OSError:
        try:
            if publication_started:
                if archive_existed:
                    _replace_file(archive_backup, archive_path)
                else:
                    archive_path.unlink(missing_ok=True)
                if metadata_existed:
                    _replace_file(metadata_backup, metadata_path)
                else:
                    metadata_path.unlink(missing_ok=True)
        except OSError as rollback_error:
            raise GpuDownloadError(
                "GPU cache publication and rollback both failed"
            ) from rollback_error
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise
    else:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_load_cached_archive`

**Exact signature**

```python
def _load_cached_archive(
    archive_path: Path,
    metadata_path: Path,
    document: GpuDocumentMetadata,
    max_age_hours: float,
) -> GpuArchiveDownload | None:
```

**Purpose**

Reads and validates cached archive; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `GpuArchiveDownload | None`.
- Every observed return expression is reproduced without truncation:
```python
None

GpuArchiveDownload(document=document, download_timestamp=timestamp, filename=archive_path.name, archive_format='zip', file_size=size, sha256=checksum, path=archive_path, cache_hit=True)

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

- Network I/O: `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds`, `GpuArchiveDownload`, `downloaded_at.astimezone`, `downloaded_at.utcoffset`.
- Filesystem read: `archive_path.stat`, `metadata_path.read_text`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `_load_cached_archive`.

**Complete source-ordered implementation**

```python
def _load_cached_archive(
    archive_path: Path,
    metadata_path: Path,
    document: GpuDocumentMetadata,
    max_age_hours: float,
) -> GpuArchiveDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        payload = json.loads(metadata_path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            return None
        cached_document = _document_from_dict(payload["document"])
        timestamp = payload["download_timestamp"]
        if not isinstance(timestamp, str):
            return None
        downloaded_at = datetime.fromisoformat(timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() is None:
            return None
        age = (datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds()
        members = validate_gpu_archive(archive_path)
        checksum = _sha256(archive_path)
        size = archive_path.stat().st_size
        if not (
            0 <= age <= max_age_hours * 3600
            and cached_document == document
            and payload.get("filename") == archive_path.name
            and payload.get("archive_format") == "zip"
            and payload.get("file_size") == size
            and payload.get("sha256") == checksum
            and payload.get("member_count") == len(members)
        ):
            return None
        return GpuArchiveDownload(
            document=document,
            download_timestamp=timestamp,
            filename=archive_path.name,
            archive_format="zip",
            file_size=size,
            sha256=checksum,
            path=archive_path,
            cache_hit=True,
        )
    except (
        KeyError,
        OSError,
        TypeError,
        ValueError,
        json.JSONDecodeError,
        GpuArchiveError,
    ):
        return None
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `download_gpu_document`

**Exact signature**

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

**Return contract**

- Declared return annotation: `GpuArchiveDownload`.
- Every observed return expression is reproduced without truncation:
```python
cached

result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `GpuDownloadError('GPU source config is invalid')`, `GpuDownloadError(f'GPU document download failed: {document.source_url}')`.

**Side effects**

- Network I/O: `GpuArchiveDownload`, `GpuDownloadError`, `open_safe_https`.
- Filesystem read: `temporary_archive.stat`.
- Filesystem write: `cache_dir.mkdir`, `copyfileobj`, `temporary_metadata.write_text`.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::ingest_gpu_planning_document` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::_download` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_download_rejects_document_inconsistent_with_config` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_unsafe_archive_name_before_io` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_fresh_cache_is_reused` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_corrupt_download_is_rejected` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache` via `download_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh` via `download_gpu_document`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def download_gpu_document(
    document: GpuDocumentMetadata,
    config: GpuSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> GpuArchiveDownload:
    """Download and transactionally cache one discovered official GPU ZIP."""

    try:
        validated_config = _validated_source_config(config)
    except GpuConfigError as error:
        raise GpuDownloadError("GPU source config is invalid") from error
    filename = _validate_gpu_document_for_config(document, validated_config)
    archive_path = cache_dir / filename
    metadata_path = cache_dir / f"{filename}.metadata.json"
    _require_no_cache_recovery_material(archive_path, metadata_path)
    cached = _load_cached_archive(
        archive_path,
        metadata_path,
        document,
        validated_config.cache.max_age_hours,
    )
    if cached is not None:
        return cached
    cache_dir.mkdir(parents=True, exist_ok=True)
    temporary_archive = archive_path.with_suffix(f"{archive_path.suffix}.part")
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    _prepare_temporary_cache_file(temporary_archive)
    _prepare_temporary_cache_file(temporary_metadata)
    try:
        with (
            open_safe_https(
                document.source_url,
                timeout=timeout,
                headers={"User-Agent": USER_AGENT},
            ) as response,
            temporary_archive.open("wb") as output,
        ):
            copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)
        members = validate_gpu_archive(temporary_archive)
        result = GpuArchiveDownload(
            document=document,
            download_timestamp=datetime.now(UTC).isoformat(),
            filename=filename,
            archive_format="zip",
            file_size=temporary_archive.stat().st_size,
            sha256=_sha256(temporary_archive),
            path=archive_path,
            cache_hit=False,
        )
        lineage = {
            "document": _document_identity(document),
            "download_timestamp": result.download_timestamp,
            "filename": filename,
            "archive_format": result.archive_format,
            "file_size": result.file_size,
            "sha256": result.sha256,
            "member_count": len(members),
        }
        temporary_metadata.write_text(
            json.dumps(lineage, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        _publish_cache_pair(
            temporary_archive, temporary_metadata, archive_path, metadata_path
        )
        return result
    except (HTTPError, URLError, OSError, GpuArchiveError) as error:
        raise GpuDownloadError(
            f"GPU document download failed: {document.source_url}"
        ) from error
    finally:
        _cleanup_temporary_cache_files(
            (temporary_archive, temporary_metadata),
            sys.exception(),
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_classify_file`

**Exact signature**

```python
def _classify_file(path: Path) -> FileCategory:
```

**Purpose**

Private `planning` helper for classify file; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `FileCategory`.
- Every observed return expression is reproduced without truncation:
```python
'OTHER_ATTACHMENT'

'SPATIAL_DATA'

'METADATA'

'WRITTEN_REGULATION'
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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_inventory` via `_classify_file`.

**Complete source-ordered implementation**

```python
def _classify_file(path: Path) -> FileCategory:
    suffix = path.suffix.casefold()
    if suffix in {
        ".gpkg",
        ".shp",
        ".shx",
        ".dbf",
        ".prj",
        ".cpg",
        ".qmd",
        ".qix",
        ".sbn",
        ".sbx",
    }:
        return "SPATIAL_DATA"
    if suffix in {".xml", ".json", ".yaml", ".yml", ".csv", ".txt"}:
        return "METADATA"
    if suffix in {".pdf", ".odt", ".doc", ".docx"}:
        return "WRITTEN_REGULATION"
    return "OTHER_ATTACHMENT"
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_inventory`

**Exact signature**

```python
def _inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

**Purpose**

Private `planning` helper for inventory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[GpuExtractedFile, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(files)
```

**Validation and exceptions**

- Guard with a raise path: `_is_link_or_junction(root) or not root.is_dir()`.
- Guard with a raise path: `not files`.
- Guard with a raise path: `_is_link_or_junction(path)`.
- Explicit raise expressions: `GpuArchiveError('Extracted GPU package contains no files')`, `GpuArchiveError(f'Extracted GPU file escapes cache: {path}')`, `GpuArchiveError(f'Extracted GPU symbolic link is forbidden: {path}')`, `GpuArchiveError(f'GPU extraction root is not a regular directory: {root}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.stat`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256`.
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
def _inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    if _is_link_or_junction(root) or not root.is_dir():
        raise GpuArchiveError(f"GPU extraction root is not a regular directory: {root}")
    for path in root.rglob("*"):
        if _is_link_or_junction(path):
            raise GpuArchiveError(f"Extracted GPU symbolic link is forbidden: {path}")
    files: list[GpuExtractedFile] = []
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=str):
        if path.parent == root and path.name == EXTRACTION_MANIFEST_NAME:
            continue
        resolved = path.resolve()
        try:
            relative = resolved.relative_to(root.resolve())
        except ValueError as error:
            raise GpuArchiveError(f"Extracted GPU file escapes cache: {path}") from error
        files.append(
            GpuExtractedFile(
                relative_path=relative.as_posix(),
                file_type=path.suffix.casefold().lstrip(".") or "none",
                size_bytes=path.stat().st_size,
                sha256=_sha256(path),
                category=_classify_file(path),
            )
        )
    if not files:
        raise GpuArchiveError("Extracted GPU package contains no files")
    files.sort(key=lambda item: item.relative_path)
    return tuple(files)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_manifest_payload`

**Exact signature**

```python
def _manifest_payload(
    download: GpuArchiveDownload, files: tuple[GpuExtractedFile, ...]
) -> dict[str, Any]:
```

**Purpose**

Private `planning` helper for manifest payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, Any]`.
- Every observed return expression is reproduced without truncation:
```python
{'schema_version': EXTRACTION_MANIFEST_SCHEMA_VERSION, 'archive_sha256': download.sha256, 'files': [{'relative_path': item.relative_path, 'size_bytes': item.size_bytes, 'sha256': item.sha256} for item in files]}
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

- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `_manifest_payload`.

**Complete source-ordered implementation**

```python
def _manifest_payload(
    download: GpuArchiveDownload, files: tuple[GpuExtractedFile, ...]
) -> dict[str, Any]:
    return {
        "schema_version": EXTRACTION_MANIFEST_SCHEMA_VERSION,
        "archive_sha256": download.sha256,
        "files": [
            {
                "relative_path": item.relative_path,
                "size_bytes": item.size_bytes,
                "sha256": item.sha256,
            }
            for item in files
        ],
    }
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_extraction_manifest`

**Exact signature**

```python
def _validate_extraction_manifest(
    root: Path, download: GpuArchiveDownload
) -> tuple[GpuExtractedFile, ...]:
```

**Purpose**

Rejects malformed or inconsistent extraction manifest; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[GpuExtractedFile, ...]`.
- Every observed return expression is reproduced without truncation:
```python
actual_files
```

**Validation and exceptions**

- Guard with a raise path: `_is_link_or_junction(marker) or not marker.is_file()`.
- Guard with a raise path: `not isinstance(payload, dict) or set(payload) != {'schema_version', 'archive_sha256', 'files'}`.
- Guard with a raise path: `type(payload['schema_version']) is not int or payload['schema_version'] != EXTRACTION_MANIFEST_SCHEMA_VERSION`.
- Guard with a raise path: `payload['archive_sha256'] != download.sha256`.
- Guard with a raise path: `not isinstance(entries, list)`.
- Guard with a raise path: `actual != expected`.
- Guard with a raise path: `not isinstance(entry, dict) or set(entry) != {'relative_path', 'size_bytes', 'sha256'}`.
- Guard with a raise path: `not isinstance(relative_path, str) or not _safe_archive_member(relative_path) or relative_path == EXTRACTION_MANIFEST_NAME or (type(size_bytes) is not int) or (size_bytes < 0) or (not isinstance(checksum, str)) or (re.fullmatch('[0-9a-f]{64}', checksum) is None)`.
- Guard with a raise path: `previous_path is not None and relative_path <= previous_path`.
- Explicit raise expressions: `GpuArchiveError('GPU extraction files do not match the versioned integrity manifest')`, `GpuArchiveError('GPU extraction manifest archive lineage differs')`, `GpuArchiveError('GPU extraction manifest file entry is invalid')`, `GpuArchiveError('GPU extraction manifest file value is invalid')`, `GpuArchiveError('GPU extraction manifest files are invalid')`, `GpuArchiveError('GPU extraction manifest has an invalid structure')`, `GpuArchiveError('GPU extraction manifest is missing or unsafe')`, `GpuArchiveError('GPU extraction manifest is unreadable')`, `GpuArchiveError('GPU extraction manifest paths are duplicated or not deterministic')`, `GpuArchiveError('GPU extraction manifest schema is unsupported')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `marker.read_text`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `_validate_extraction_manifest`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `_validate_extraction_manifest`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_sources` via `_validate_extraction_manifest`.

**Complete source-ordered implementation**

```python
def _validate_extraction_manifest(
    root: Path, download: GpuArchiveDownload
) -> tuple[GpuExtractedFile, ...]:
    marker = root / EXTRACTION_MANIFEST_NAME
    if _is_link_or_junction(marker) or not marker.is_file():
        raise GpuArchiveError("GPU extraction manifest is missing or unsafe")
    try:
        payload = json.loads(marker.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise GpuArchiveError("GPU extraction manifest is unreadable") from error
    if not isinstance(payload, dict) or set(payload) != {
        "schema_version",
        "archive_sha256",
        "files",
    }:
        raise GpuArchiveError("GPU extraction manifest has an invalid structure")
    if (
        type(payload["schema_version"]) is not int
        or payload["schema_version"] != EXTRACTION_MANIFEST_SCHEMA_VERSION
    ):
        raise GpuArchiveError("GPU extraction manifest schema is unsupported")
    if payload["archive_sha256"] != download.sha256:
        raise GpuArchiveError("GPU extraction manifest archive lineage differs")
    entries = payload["files"]
    if not isinstance(entries, list):
        raise GpuArchiveError("GPU extraction manifest files are invalid")

    expected: list[tuple[str, int, str]] = []
    previous_path: str | None = None
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {
            "relative_path",
            "size_bytes",
            "sha256",
        }:
            raise GpuArchiveError("GPU extraction manifest file entry is invalid")
        relative_path = entry["relative_path"]
        size_bytes = entry["size_bytes"]
        checksum = entry["sha256"]
        if (
            not isinstance(relative_path, str)
            or not _safe_archive_member(relative_path)
            or relative_path == EXTRACTION_MANIFEST_NAME
            or type(size_bytes) is not int
            or size_bytes < 0
            or not isinstance(checksum, str)
            or re.fullmatch(r"[0-9a-f]{64}", checksum) is None
        ):
            raise GpuArchiveError("GPU extraction manifest file value is invalid")
        if previous_path is not None and relative_path <= previous_path:
            raise GpuArchiveError(
                "GPU extraction manifest paths are duplicated or not deterministic"
            )
        previous_path = relative_path
        expected.append((relative_path, size_bytes, checksum))

    actual_files = _inventory(root)
    actual = [
        (item.relative_path, item.size_bytes, item.sha256) for item in actual_files
    ]
    if actual != expected:
        raise GpuArchiveError(
            "GPU extraction files do not match the versioned integrity manifest"
        )
    return actual_files
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_remove_extraction_path`

**Exact signature**

```python
def _remove_extraction_path(path: Path) -> None:
```

**Purpose**

Private `planning` helper for remove extraction path; its complete implementation below is the authoritative behavioral contract.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_publish_extraction_directory` via `_remove_extraction_path`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `_remove_extraction_path`.

**Complete source-ordered implementation**

```python
def _remove_extraction_path(path: Path) -> None:
    if path.is_junction():
        path.rmdir()
    elif path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.exists():
        shutil.rmtree(path)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_publish_extraction_directory`

**Exact signature**

```python
def _publish_extraction_directory(temporary_root: Path, root: Path) -> None:
```

**Purpose**

Private `planning` helper for publish extraction directory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `GpuArchiveError('GPU extraction publication and rollback both failed')`, `GpuArchiveError('GPU extraction publication failed')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: `shutil.move`.
- CRS/geometry calculation: none directly visible.
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
    _remove_extraction_path(backup)
    old_moved = False
    try:
        if root.exists() or _is_link_or_junction(root):
            shutil.move(str(root), str(backup))
            old_moved = True
        shutil.move(str(temporary_root), str(root))
    except OSError as error:
        try:
            _remove_extraction_path(root)
            if old_moved:
                shutil.move(str(backup), str(root))
        except OSError as rollback_error:
            raise GpuArchiveError(
                "GPU extraction publication and rollback both failed"
            ) from rollback_error
        raise GpuArchiveError("GPU extraction publication failed") from error
    else:
        _remove_extraction_path(backup)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_discover_standard_models`

**Exact signature**

```python
def _discover_standard_models(root: Path) -> tuple[str, ...]:
```

**Purpose**

Private `planning` helper for discover standard models; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(sorted(models, key=str.casefold))
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

- direct call or construction: `src/landscout/sources/gpu_fr.py::extract_gpu_document` via `_discover_standard_models`.

**Complete source-ordered implementation**

```python
def _discover_standard_models(root: Path) -> tuple[str, ...]:
    models: set[str] = set()
    for path in sorted(root.rglob("*.xml"), key=str):
        try:
            parsed = ElementTree.parse(path)
        except (OSError, ElementTree.ParseError):
            continue
        for element in parsed.iter():
            text = element.text.strip() if element.text else ""
            if re.fullmatch(r"CNIG\s+[A-Za-z]+\s+v\d{4}", text, re.IGNORECASE):
                models.add(text)
    return tuple(sorted(models, key=str.casefold))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `extract_gpu_document`

**Exact signature**

```python
def extract_gpu_document(
    download: GpuArchiveDownload, cache_dir: Path = DEFAULT_CACHE_DIR
) -> GpuExtraction:
```

**Purpose**

Safely extract a validated GPU ZIP into a content-addressed cache.

**Return contract**

- Declared return annotation: `GpuExtraction`.
- Every observed return expression is reproduced without truncation:
```python
GpuExtraction(archive=download, extraction_root=root, files=files, standard_models=standard_models, cache_hit=False)

GpuExtraction(archive=download, extraction_root=root, files=files, standard_models=_discover_standard_models(root), cache_hit=True)
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(error, GpuArchiveError)`.
- Explicit raise expressions: `GpuArchiveError('Cannot safely extract GPU document')`, `re-raise`.

**Side effects**

- Network I/O: `_validate_gpu_archive_download`.
- Filesystem read: `zipfile.ZipFile`.
- Filesystem write: `copyfileobj`, `marker.write_text`, `root.parent.mkdir`, `target.mkdir`, `target.parent.mkdir`, `temporary_root.mkdir`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::ingest_gpu_planning_document` via `extract_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_extraction_inventory_and_cache` via `extract_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_stale_download_object_rejects_replaced_valid_archive` via `extract_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_extraction_rejects_archive_object_inconsistent_with_path` via `extract_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_tampered_extraction_is_rebuilt_from_verified_archive` via `extract_gpu_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::_extraction_from_archive` via `extract_gpu_document`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def extract_gpu_document(
    download: GpuArchiveDownload, cache_dir: Path = DEFAULT_CACHE_DIR
) -> GpuExtraction:
    """Safely extract a validated GPU ZIP into a content-addressed cache."""

    _validate_gpu_archive_download(download)
    root = cache_dir / "x" / download.sha256[:16]
    if root.is_dir() and not _is_link_or_junction(root):
        try:
            files = _validate_extraction_manifest(root, download)
            return GpuExtraction(
                archive=download,
                extraction_root=root,
                files=files,
                standard_models=_discover_standard_models(root),
                cache_hit=True,
            )
        except (GpuArchiveError, OSError):
            pass
    root.parent.mkdir(parents=True, exist_ok=True)
    temporary_root = root.with_name(f"{root.name}.part")
    _remove_extraction_path(temporary_root)
    temporary_root.mkdir()
    try:
        with zipfile.ZipFile(download.path) as archive:
            destinations = _validated_zip_destinations(archive.infolist())
            for member, destination in destinations:
                target = temporary_root.joinpath(*destination.parts)
                if member.is_dir() or member.filename.endswith(("/", "\\")):
                    target.mkdir(parents=True, exist_ok=True)
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(member) as source, target.open("xb") as output:
                    copyfileobj(source, output, length=DOWNLOAD_CHUNK_SIZE)
        files = _inventory(temporary_root)
        _validate_gpu_archive_download(download)
        marker = temporary_root / EXTRACTION_MANIFEST_NAME
        marker.write_text(
            json.dumps(
                _manifest_payload(download, files), indent=2, sort_keys=True
            )
            + "\n",
            encoding="utf-8",
        )
        files = _validate_extraction_manifest(temporary_root, download)
        standard_models = _discover_standard_models(temporary_root)
        _publish_extraction_directory(temporary_root, root)
        return GpuExtraction(
            archive=download,
            extraction_root=root,
            files=files,
            standard_models=standard_models,
            cache_hit=False,
        )
    except (OSError, zipfile.BadZipFile, RuntimeError, GpuArchiveError) as error:
        if isinstance(error, GpuArchiveError):
            raise
        raise GpuArchiveError("Cannot safely extract GPU document") from error
    finally:
        _remove_extraction_path(temporary_root)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `discover_gpu_spatial_layers`

**Exact signature**

```python
def discover_gpu_spatial_layers(
    extraction: GpuExtraction,
) -> tuple[GpuSpatialLayerReference, ...]:
```

**Purpose**

Discover every real GeoPackage or Shapefile layer in an extraction.

**Return contract**

- Declared return annotation: `tuple[GpuSpatialLayerReference, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(sorted(references, key=lambda item: (str(item.dataset_path), item.source_layer)))
```

**Validation and exceptions**

- Guard with a raise path: `not references`.
- Guard with a raise path: `len(unique) != len(references)`.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU document contains no supported spatial data')`, `GpuSpatialInspectionError('GPU document exposes duplicate spatial layers')`, `GpuSpatialInspectionError(f'Cannot list GPU GeoPackage layers: {path}')`.

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

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::inspect_gpu_planning_document` via `discover_gpu_spatial_layers`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality` via `discover_gpu_spatial_layers`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def discover_gpu_spatial_layers(
    extraction: GpuExtraction,
) -> tuple[GpuSpatialLayerReference, ...]:
    """Discover every real GeoPackage or Shapefile layer in an extraction."""

    root = extraction.extraction_root
    references: list[GpuSpatialLayerReference] = []
    gpkg_paths = sorted(root.rglob("*.gpkg"), key=str)
    shp_paths = sorted(root.rglob("*.shp"), key=str)
    for path in gpkg_paths:
        try:
            layers = pyogrio.list_layers(path)
        except Exception as error:
            raise GpuSpatialInspectionError(
                f"Cannot list GPU GeoPackage layers: {path}"
            ) from error
        for raw_name in layers[:, 0].tolist():
            if isinstance(raw_name, str) and raw_name:
                references.append(
                    GpuSpatialLayerReference(path, raw_name, "GPKG")
                )
    for path in shp_paths:
        references.append(GpuSpatialLayerReference(path, path.stem, "ESRI Shapefile"))
    if not references:
        raise GpuSpatialInspectionError("GPU document contains no supported spatial data")
    unique = {(item.dataset_path.resolve(), item.source_layer) for item in references}
    if len(unique) != len(references):
        raise GpuSpatialInspectionError("GPU document exposes duplicate spatial layers")
    return tuple(
        sorted(references, key=lambda item: (str(item.dataset_path), item.source_layer))
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_layer_config`

**Exact signature**

```python
def _layer_config(
    config: GpuSourceConfig, logical_name: LogicalLayerName
) -> GpuLogicalLayerConfig:
```

**Purpose**

Private `planning` helper for layer config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuLogicalLayerConfig`.
- Every observed return expression is reproduced without truncation:
```python
getattr(config.spatial_layers, logical_name)
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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_discover_logical_layer` via `_layer_config`.

**Complete source-ordered implementation**

```python
def _layer_config(
    config: GpuSourceConfig, logical_name: LogicalLayerName
) -> GpuLogicalLayerConfig:
    return getattr(config.spatial_layers, logical_name)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_discover_logical_layer`

**Exact signature**

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

Private `planning` helper for discover logical layer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuSpatialLayerReference | None`.
- Every observed return expression is reproduced without truncation:
```python
matches[0]

None
```

**Validation and exceptions**

- Guard with a raise path: `len(matches) != 1`.
- Explicit raise expressions: `GpuSpatialInspectionError(f'Expected {adjective} {logical_name} layer, found {len(matches)}')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::inspect_gpu_planning_document` via `_discover_logical_layer`.

**Complete source-ordered implementation**

```python
def _discover_logical_layer(
    references: tuple[GpuSpatialLayerReference, ...],
    config: GpuSourceConfig,
    logical_name: LogicalLayerName,
    *,
    required: bool,
) -> GpuSpatialLayerReference | None:
    configured = _layer_config(config, logical_name)
    tokens = {_normalize_words(value) for value in configured.match_tokens}
    matches = []
    for item in references:
        normalized_name = f"_{_normalize_words(item.source_layer)}_"
        if any(f"_{token}_" in normalized_name for token in tokens):
            matches.append(item)
    if not matches and not required:
        return None
    if len(matches) != 1:
        adjective = "exactly one" if required else "at most one"
        raise GpuSpatialInspectionError(
            f"Expected {adjective} {logical_name} layer, found {len(matches)}"
        )
    return matches[0]
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_load_reference`

**Exact signature**

```python
def _load_reference(reference: GpuSpatialLayerReference) -> gpd.GeoDataFrame:
```

**Purpose**

Reads and validates reference; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.read_file(reference.dataset_path, engine='pyogrio')

gpd.read_file(reference.dataset_path, layer=reference.source_layer, engine='pyogrio')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `GpuSpatialInspectionError(f'Cannot load GPU spatial layer: {reference.source_layer}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `gpd.read_file`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::inspect_gpu_planning_document` via `_load_reference`.

**Complete source-ordered implementation**

```python
def _load_reference(reference: GpuSpatialLayerReference) -> gpd.GeoDataFrame:
    try:
        if reference.driver == "GPKG":
            return gpd.read_file(
                reference.dataset_path, layer=reference.source_layer, engine="pyogrio"
            )
        return gpd.read_file(reference.dataset_path, engine="pyogrio")
    except Exception as error:
        raise GpuSpatialInspectionError(
            f"Cannot load GPU spatial layer: {reference.source_layer}"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_inventory_path`

**Exact signature**

```python
def _validated_inventory_path(value: object) -> PurePosixPath:
```

**Purpose**

Checks and returns canonical inventory path; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `PurePosixPath`.
- Every observed return expression is reproduced without truncation:
```python
relative
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Guard with a raise path: `'\\' in value or '\x00' in value`.
- Guard with a raise path: `relative.is_absolute() or any((part in {'', '.', '..'} for part in parts)) or relative.as_posix() != value`.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU extraction inventory path is unsafe')`, `GpuSpatialInspectionError('GPU extraction inventory path must be an exact string')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_inventory` via `_validated_inventory_path`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_contained_spatial_path` via `_validated_inventory_path`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_dataset_relative_path` via `_validated_inventory_path`.

**Complete source-ordered implementation**

```python
def _validated_inventory_path(value: object) -> PurePosixPath:
    if not isinstance(value, str) or not value or value != value.strip():
        raise GpuSpatialInspectionError(
            "GPU extraction inventory path must be an exact string"
        )
    if "\\" in value or "\x00" in value:
        raise GpuSpatialInspectionError("GPU extraction inventory path is unsafe")
    parts = value.split("/")
    relative = PurePosixPath(value)
    if (
        relative.is_absolute()
        or any(part in {"", ".", ".."} for part in parts)
        or relative.as_posix() != value
    ):
        raise GpuSpatialInspectionError("GPU extraction inventory path is unsafe")
    return relative
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_spatial_root`

**Exact signature**

```python
def _validated_spatial_root(extraction: GpuExtraction) -> tuple[Path, Path]:
```

**Purpose**

Checks and returns canonical spatial root; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[Path, Path]`.
- Every observed return expression is reproduced without truncation:
```python
(root, root.resolve(strict=True))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(root, Path) or _is_link_or_junction(root) or (not root.is_dir())`.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU extraction root cannot be resolved safely')`, `GpuSpatialInspectionError('GPU extraction root must be a regular directory')`, `re-raise`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `_validated_spatial_root`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `_validated_spatial_root`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_sources` via `_validated_spatial_root`.

**Complete source-ordered implementation**

```python
def _validated_spatial_root(extraction: GpuExtraction) -> tuple[Path, Path]:
    root = extraction.extraction_root
    try:
        if (
            not isinstance(root, Path)
            or _is_link_or_junction(root)
            or not root.is_dir()
        ):
            raise GpuSpatialInspectionError(
                "GPU extraction root must be a regular directory"
            )
        return root, root.resolve(strict=True)
    except GpuSpatialInspectionError:
        raise
    except OSError as error:
        raise GpuSpatialInspectionError(
            "GPU extraction root cannot be resolved safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_spatial_inventory`

**Exact signature**

```python
def _spatial_inventory(
    extraction: GpuExtraction,
) -> dict[str, GpuExtractedFile]:
```

**Purpose**

Private `planning` helper for spatial inventory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, GpuExtractedFile]`.
- Every observed return expression is reproduced without truncation:
```python
inventory
```

**Validation and exceptions**

- Guard with a raise path: `type(extraction.files) is not tuple`.
- Guard with a raise path: `not isinstance(item, GpuExtractedFile)`.
- Guard with a raise path: `relative.casefold() in {key.casefold() for key in inventory}`.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU extraction inventory contains duplicate paths')`, `GpuSpatialInspectionError('GPU extraction inventory is invalid')`, `GpuSpatialInspectionError('GPU extraction inventory must be an immutable tuple')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `inventory[relative]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `_spatial_inventory`.

**Complete source-ordered implementation**

```python
def _spatial_inventory(
    extraction: GpuExtraction,
) -> dict[str, GpuExtractedFile]:
    if type(extraction.files) is not tuple:
        raise GpuSpatialInspectionError(
            "GPU extraction inventory must be an immutable tuple"
        )
    inventory: dict[str, GpuExtractedFile] = {}
    for item in extraction.files:
        if not isinstance(item, GpuExtractedFile):
            raise GpuSpatialInspectionError("GPU extraction inventory is invalid")
        relative = _validated_inventory_path(item.relative_path).as_posix()
        if relative.casefold() in {key.casefold() for key in inventory}:
            raise GpuSpatialInspectionError(
                "GPU extraction inventory contains duplicate paths"
            )
        inventory[relative] = item
    return inventory
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_contained_spatial_path`

**Exact signature**

```python
def _contained_spatial_path(
    root: Path,
    root_resolved: Path,
    relative: str,
) -> Path:
```

**Purpose**

Private `planning` helper for contained spatial path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
path
```

**Validation and exceptions**

- Guard with a raise path: `not path.is_file()`.
- Guard with a raise path: `_is_link_or_junction(current)`.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU spatial source escapes the verified extraction root')`, `GpuSpatialInspectionError('GPU spatial source must be an extracted regular file')`, `GpuSpatialInspectionError('GPU spatial source path contains a symbolic link or junction')`, `re-raise`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `_contained_spatial_path`.

**Complete source-ordered implementation**

```python
def _contained_spatial_path(
    root: Path,
    root_resolved: Path,
    relative: str,
) -> Path:
    relative_path = _validated_inventory_path(relative)
    path = root.joinpath(*relative_path.parts)
    current = root
    try:
        for part in relative_path.parts:
            current /= part
            if _is_link_or_junction(current):
                raise GpuSpatialInspectionError(
                    "GPU spatial source path contains a symbolic link or junction"
                )
        resolved = path.resolve(strict=True)
        resolved.relative_to(root_resolved)
        if not path.is_file():
            raise GpuSpatialInspectionError(
                "GPU spatial source must be an extracted regular file"
            )
        return path
    except GpuSpatialInspectionError:
        raise
    except (OSError, ValueError) as error:
        raise GpuSpatialInspectionError(
            "GPU spatial source escapes the verified extraction root"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_spatial_dataset_relative_path`

**Exact signature**

```python
def _spatial_dataset_relative_path(
    reference: GpuSpatialLayerReference,
    root_resolved: Path,
) -> str:
```

**Purpose**

Private `planning` helper for spatial dataset relative path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_validated_inventory_path(relative.as_posix()).as_posix()
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(path, Path) or _is_link_or_junction(path)`.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU spatial dataset path escapes the verified extraction root')`, `GpuSpatialInspectionError('GPU spatial dataset path is invalid')`, `re-raise`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `_spatial_dataset_relative_path`.

**Complete source-ordered implementation**

```python
def _spatial_dataset_relative_path(
    reference: GpuSpatialLayerReference,
    root_resolved: Path,
) -> str:
    path = reference.dataset_path
    try:
        if not isinstance(path, Path) or _is_link_or_junction(path):
            raise GpuSpatialInspectionError("GPU spatial dataset path is invalid")
        relative = path.resolve(strict=True).relative_to(root_resolved)
        return _validated_inventory_path(relative.as_posix()).as_posix()
    except GpuSpatialInspectionError:
        raise
    except (OSError, ValueError) as error:
        raise GpuSpatialInspectionError(
            "GPU spatial dataset path escapes the verified extraction root"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_spatial_source_family`

**Exact signature**

```python
def _spatial_source_family(
    reference: GpuSpatialLayerReference,
    extraction: GpuExtraction,
) -> tuple[str, tuple[tuple[Path, GpuExtractedFile], ...]]:
```

**Purpose**

Private `planning` helper for spatial source family; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, tuple[tuple[Path, GpuExtractedFile], ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(relative, tuple(verified))
```

**Validation and exceptions**

- Guard with a raise path: `driver == 'GPKG'`.
- Guard with a raise path: `pure.suffix.casefold() != '.gpkg'`.
- Guard with a raise path: `len(exposed) != 1`.
- Guard with a raise path: `driver == 'ESRI Shapefile'`.
- Guard with a raise path: `item is None`.
- Guard with a raise path: `type(item.size_bytes) is not int or item.size_bytes <= 0 or (not isinstance(item.sha256, str)) or (re.fullmatch('[0-9a-f]{64}', item.sha256) is None)`.
- Guard with a raise path: `actual_size != item.size_bytes`.
- Guard with a raise path: `actual_sha != item.sha256`.
- Guard with a raise path: `Path(f'{reference.dataset_path}{suffix}').exists()`.
- Guard with a raise path: `pure.suffix.casefold() != '.shp' or reference.source_layer != pure.stem`.
- Guard with a raise path: `not required.issubset({PurePosixPath(candidate).suffix.casefold() for candidate in expected_paths})`.
- Guard with a raise path: `actual_paths != expected_paths`.
- Explicit raise expressions: `GpuSpatialInspectionError('Cannot list the verified GPU GeoPackage source')`, `GpuSpatialInspectionError('Cannot read GPU spatial source integrity')`, `GpuSpatialInspectionError('GPU GeoPackage has an unbound SQLite sidecar')`, `GpuSpatialInspectionError('GPU GeoPackage source has an inconsistent extension')`, `GpuSpatialInspectionError('GPU GeoPackage source layer is missing or ambiguous')`, `GpuSpatialInspectionError('GPU Shapefile family cannot be inventoried safely')`, `GpuSpatialInspectionError('GPU Shapefile family differs from the extraction inventory')`, `GpuSpatialInspectionError('GPU Shapefile inventory is missing a required family member')`, `GpuSpatialInspectionError('GPU Shapefile source identity is inconsistent')`, `GpuSpatialInspectionError('GPU spatial source SHA256 differs from the extraction inventory')`, `GpuSpatialInspectionError('GPU spatial source driver must be GPKG or ESRI Shapefile')`, `GpuSpatialInspectionError('GPU spatial source inventory integrity is invalid')`, `GpuSpatialInspectionError('GPU spatial source is absent from the extraction inventory')`, `GpuSpatialInspectionError('GPU spatial source size differs from the extraction inventory')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.stat`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `_spatial_source_family`.

**Complete source-ordered implementation**

```python
def _spatial_source_family(
    reference: GpuSpatialLayerReference,
    extraction: GpuExtraction,
) -> tuple[str, tuple[tuple[Path, GpuExtractedFile], ...]]:
    root, root_resolved = _validated_spatial_root(extraction)
    inventory = _spatial_inventory(extraction)
    relative = _spatial_dataset_relative_path(reference, root_resolved)
    pure = PurePosixPath(relative)
    driver = reference.driver
    if driver == "GPKG":
        if pure.suffix.casefold() != ".gpkg":
            raise GpuSpatialInspectionError(
                "GPU GeoPackage source has an inconsistent extension"
            )
        expected_paths = {relative}
        for suffix in ("-wal", "-shm", "-journal"):
            if Path(f"{reference.dataset_path}{suffix}").exists():
                raise GpuSpatialInspectionError(
                    "GPU GeoPackage has an unbound SQLite sidecar"
                )
        try:
            layers = pyogrio.list_layers(reference.dataset_path)
            exposed = [
                value
                for value in layers[:, 0].tolist()
                if value == reference.source_layer
            ]
        except Exception as error:
            raise GpuSpatialInspectionError(
                "Cannot list the verified GPU GeoPackage source"
            ) from error
        if len(exposed) != 1:
            raise GpuSpatialInspectionError(
                "GPU GeoPackage source layer is missing or ambiguous"
            )
    elif driver == "ESRI Shapefile":
        if pure.suffix.casefold() != ".shp" or reference.source_layer != pure.stem:
            raise GpuSpatialInspectionError(
                "GPU Shapefile source identity is inconsistent"
            )
        family_names = {
            f"{pure.stem}{suffix}".casefold()
            for suffix in (
                ".shp",
                ".shx",
                ".dbf",
                ".prj",
                ".cpg",
                ".qix",
                ".qmd",
                ".sbn",
                ".sbx",
                ".shp.xml",
            )
        }
        expected_paths = {
            candidate
            for candidate in inventory
            if PurePosixPath(candidate).parent == pure.parent
            and PurePosixPath(candidate).name.casefold() in family_names
        }
        required = {".shp", ".shx", ".dbf"}
        if not required.issubset(
            {PurePosixPath(candidate).suffix.casefold() for candidate in expected_paths}
        ):
            raise GpuSpatialInspectionError(
                "GPU Shapefile inventory is missing a required family member"
            )
        parent = root.joinpath(*pure.parent.parts)
        try:
            actual_paths = {
                candidate.resolve(strict=True)
                .relative_to(root_resolved)
                .as_posix()
                for candidate in parent.iterdir()
                if candidate.name.casefold() in family_names
            }
        except (OSError, ValueError) as error:
            raise GpuSpatialInspectionError(
                "GPU Shapefile family cannot be inventoried safely"
            ) from error
        if actual_paths != expected_paths:
            raise GpuSpatialInspectionError(
                "GPU Shapefile family differs from the extraction inventory"
            )
    else:
        raise GpuSpatialInspectionError(
            "GPU spatial source driver must be GPKG or ESRI Shapefile"
        )

    verified: list[tuple[Path, GpuExtractedFile]] = []
    for candidate in sorted(expected_paths):
        item = inventory.get(candidate)
        if item is None:
            raise GpuSpatialInspectionError(
                "GPU spatial source is absent from the extraction inventory"
            )
        if (
            type(item.size_bytes) is not int
            or item.size_bytes <= 0
            or not isinstance(item.sha256, str)
            or re.fullmatch(r"[0-9a-f]{64}", item.sha256) is None
        ):
            raise GpuSpatialInspectionError(
                "GPU spatial source inventory integrity is invalid"
            )
        path = _contained_spatial_path(root, root_resolved, candidate)
        try:
            actual_size = path.stat().st_size
            actual_sha = _sha256(path)
        except OSError as error:
            raise GpuSpatialInspectionError(
                "Cannot read GPU spatial source integrity"
            ) from error
        if actual_size != item.size_bytes:
            raise GpuSpatialInspectionError(
                "GPU spatial source size differs from the extraction inventory"
            )
        if actual_sha != item.sha256:
            raise GpuSpatialInspectionError(
                "GPU spatial source SHA256 differs from the extraction inventory"
            )
        verified.append((path, item))
    return relative, tuple(verified)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_same_spatial_crs`

**Exact signature**

```python
def _same_spatial_crs(left: object, right: object) -> bool:
```

**Purpose**

Compares spatial crs; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
bool(CRS.from_user_input(left).equals(CRS.from_user_input(right)))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU spatial source CRS cannot be validated')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_compare_inspected_spatial_layer` via `_same_spatial_crs`.

**Complete source-ordered implementation**

```python
def _same_spatial_crs(left: object, right: object) -> bool:
    try:
        return bool(CRS.from_user_input(left).equals(CRS.from_user_input(right)))
    except Exception as error:
        raise GpuSpatialInspectionError(
            "GPU spatial source CRS cannot be validated"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_inspected_spatial_layer`

**Exact signature**

```python
def _compare_inspected_spatial_layer(
    inspected: GpuInspectedLayer,
    reread: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Private `planning` helper for compare inspected spatial layer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(loaded, gpd.GeoDataFrame) or not isinstance(reread, gpd.GeoDataFrame)`.
- Guard with a raise path: `len(loaded) != len(reread)`.
- Guard with a raise path: `tuple(loaded.columns) != tuple(reread.columns)`.
- Guard with a raise path: `tuple((str(dtype) for dtype in loaded.dtypes)) != tuple((str(dtype) for dtype in reread.dtypes))`.
- Guard with a raise path: `loaded.geometry.name != reread.geometry.name or not _same_spatial_crs(loaded.crs, reread.crs)`.
- Guard with a raise path: `loaded.attrs != reread.attrs`.
- Guard with a raise path: `not loaded[attributes].reset_index(drop=True).equals(reread[attributes].reset_index(drop=True))`.
- Guard with a raise path: `loaded.geometry.to_wkb().tolist() != reread.geometry.to_wkb().tolist()`.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU spatial layer must be a GeoDataFrame')`, `GpuSpatialInspectionError('Loaded GPU spatial attributes metadata differs from its source')`, `GpuSpatialInspectionError('Loaded GPU spatial attributes or row order differ from its source')`, `GpuSpatialInspectionError('Loaded GPU spatial columns differ from its source')`, `GpuSpatialInspectionError('Loaded GPU spatial dtypes differ from its source')`, `GpuSpatialInspectionError('Loaded GPU spatial geometry metadata differs from its source')`, `GpuSpatialInspectionError('Loaded GPU spatial geometry or row order differs from its source')`, `GpuSpatialInspectionError('Loaded GPU spatial layer cannot be compared safely')`, `GpuSpatialInspectionError('Loaded GPU spatial row count differs from its source')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `loaded.geometry.to_wkb`, `loaded.geometry.to_wkb().tolist`, `reread.geometry.to_wkb`, `reread.geometry.to_wkb().tolist`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `_compare_inspected_spatial_layer`.

**Complete source-ordered implementation**

```python
def _compare_inspected_spatial_layer(
    inspected: GpuInspectedLayer,
    reread: gpd.GeoDataFrame,
) -> None:
    loaded = inspected.data
    try:
        if not isinstance(loaded, gpd.GeoDataFrame) or not isinstance(
            reread, gpd.GeoDataFrame
        ):
            raise GpuSpatialInspectionError(
                "GPU spatial layer must be a GeoDataFrame"
            )
        if len(loaded) != len(reread):
            raise GpuSpatialInspectionError(
                "Loaded GPU spatial row count differs from its source"
            )
        if tuple(loaded.columns) != tuple(reread.columns):
            raise GpuSpatialInspectionError(
                "Loaded GPU spatial columns differ from its source"
            )
        if tuple(str(dtype) for dtype in loaded.dtypes) != tuple(
            str(dtype) for dtype in reread.dtypes
        ):
            raise GpuSpatialInspectionError(
                "Loaded GPU spatial dtypes differ from its source"
            )
        if loaded.geometry.name != reread.geometry.name or not _same_spatial_crs(
            loaded.crs, reread.crs
        ):
            raise GpuSpatialInspectionError(
                "Loaded GPU spatial geometry metadata differs from its source"
            )
        if loaded.attrs != reread.attrs:
            raise GpuSpatialInspectionError(
                "Loaded GPU spatial attributes metadata differs from its source"
            )
        geometry_column = reread.geometry.name
        attributes = [column for column in reread.columns if column != geometry_column]
        if not loaded[attributes].reset_index(drop=True).equals(
            reread[attributes].reset_index(drop=True)
        ):
            raise GpuSpatialInspectionError(
                "Loaded GPU spatial attributes or row order differ from its source"
            )
        if loaded.geometry.to_wkb().tolist() != reread.geometry.to_wkb().tolist():
            raise GpuSpatialInspectionError(
                "Loaded GPU spatial geometry or row order differs from its source"
            )
    except GpuSpatialInspectionError:
        raise
    except Exception as error:
        raise GpuSpatialInspectionError(
            "Loaded GPU spatial layer cannot be compared safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_revalidate_gpu_spatial_layer_source`

**Exact signature**

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

**Return contract**

- Declared return annotation: `GpuValidatedSpatialLayerSource`.
- Every observed return expression is reproduced without truncation:
```python
GpuValidatedSpatialLayerSource(logical_name=inspected_layer.logical_name, source_layer=reference.source_layer, driver=reference.driver, dataset_relative_path=relative, source_crs=expected_summary.crs, feature_count=len(reread), files=tuple((GpuSpatialSourceFileIntegrity(relative_path=item.relative_path, file_type=item.file_type, size_bytes=item.size_bytes, sha256=item.sha256, category=item.category) for _, item in family)), ogr_fids=ogr_fids, data=reread)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(planning_document, GpuPlanningDocument) or not isinstance(inspected_layer, GpuInspectedLayer)`.
- Guard with a raise path: `not any((inspected_layer is candidate for candidate in (planning_document.zoning, *planning_document.related_layers)))`.
- Guard with a raise path: `sum((reference == inspected_layer.reference for reference in planning_document.all_spatial_layers)) != 1`.
- Guard with a raise path: `verify_extraction_manifest`.
- Guard with a raise path: `not with_fids.index.is_unique or any((isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0 for value in with_fids.index))`.
- Guard with a raise path: `inspected_layer.summary != expected_summary`.
- Guard with a raise path: `post_relative != relative or tuple((item.relative_path for _, item in post_family)) != tuple((item.relative_path for _, item in family))`.
- Guard with a raise path: `planning_document.extraction.files != manifest_files`.
- Guard with a raise path: `path.stat().st_size != item.size_bytes or _sha256(path) != item.sha256`.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU extraction inventory differs from its verified manifest')`, `GpuSpatialInspectionError('GPU extraction manifest cannot verify the spatial source')`, `GpuSpatialInspectionError('GPU inspected-layer summary differs from its fresh source')`, `GpuSpatialInspectionError('GPU planning document or inspected layer is invalid')`, `GpuSpatialInspectionError('GPU spatial source cannot be revalidated')`, `GpuSpatialInspectionError('GPU spatial source changed during verification')`, `GpuSpatialInspectionError('GPU spatial source exposes invalid source FIDs')`, `GpuSpatialInspectionError('GPU spatial source family changed during verification')`, `GpuSpatialInspectionError('Inspected GPU layer does not belong to the planning document')`, `GpuSpatialInspectionError('Inspected GPU reference must occur exactly once in the spatial inventory')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.stat`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::revalidate_gpu_spatial_layer_source` via `_revalidate_gpu_spatial_layer_source`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_sources` via `_revalidate_gpu_spatial_layer_source`.

**Complete source-ordered implementation**

```python
def _revalidate_gpu_spatial_layer_source(
    planning_document: GpuPlanningDocument,
    inspected_layer: GpuInspectedLayer,
    *,
    verify_extraction_manifest: bool,
) -> GpuValidatedSpatialLayerSource:
    """Verify and freshly reload one extracted GPU spatial-layer source."""

    try:
        if not isinstance(planning_document, GpuPlanningDocument) or not isinstance(
            inspected_layer, GpuInspectedLayer
        ):
            raise GpuSpatialInspectionError(
                "GPU planning document or inspected layer is invalid"
            )
        if not any(
            inspected_layer is candidate
            for candidate in (
                planning_document.zoning,
                *planning_document.related_layers,
            )
        ):
            raise GpuSpatialInspectionError(
                "Inspected GPU layer does not belong to the planning document"
            )
        if (
            sum(
                reference == inspected_layer.reference
                for reference in planning_document.all_spatial_layers
            )
            != 1
        ):
            raise GpuSpatialInspectionError(
                "Inspected GPU reference must occur exactly once in the spatial inventory"
            )
        if verify_extraction_manifest:
            root, _ = _validated_spatial_root(planning_document.extraction)
            try:
                manifest_files = _validate_extraction_manifest(
                    root, planning_document.extraction.archive
                )
            except GpuArchiveError as error:
                raise GpuSpatialInspectionError(
                    "GPU extraction manifest cannot verify the spatial source"
                ) from error
            if planning_document.extraction.files != manifest_files:
                raise GpuSpatialInspectionError(
                    "GPU extraction inventory differs from its verified manifest"
                )
        reference = inspected_layer.reference
        relative, family = _spatial_source_family(
            reference, planning_document.extraction
        )
        with_fids = pyogrio.read_dataframe(
            reference.dataset_path,
            layer=reference.source_layer,
            fid_as_index=True,
        )
        if (
            not with_fids.index.is_unique
            or any(
                isinstance(value, bool)
                or not isinstance(value, Integral)
                or int(value) < 0
                for value in with_fids.index
            )
        ):
            raise GpuSpatialInspectionError(
                "GPU spatial source exposes invalid source FIDs"
            )
        ogr_fids = tuple(int(value) for value in with_fids.index)
        reread = with_fids.reset_index(drop=True)
        _compare_inspected_spatial_layer(inspected_layer, reread)
        expected_summary = _summarize_layer(
            reread, reference, planning_document.extraction
        )
        if inspected_layer.summary != expected_summary:
            raise GpuSpatialInspectionError(
                "GPU inspected-layer summary differs from its fresh source"
            )
        post_relative, post_family = _spatial_source_family(
            reference, planning_document.extraction
        )
        if post_relative != relative or tuple(
            item.relative_path for _, item in post_family
        ) != tuple(item.relative_path for _, item in family):
            raise GpuSpatialInspectionError(
                "GPU spatial source family changed during verification"
            )
        for path, item in post_family:
            if path.stat().st_size != item.size_bytes or _sha256(path) != item.sha256:
                raise GpuSpatialInspectionError(
                    "GPU spatial source changed during verification"
                )
        return GpuValidatedSpatialLayerSource(
            logical_name=inspected_layer.logical_name,
            source_layer=reference.source_layer,
            driver=reference.driver,
            dataset_relative_path=relative,
            source_crs=expected_summary.crs,
            feature_count=len(reread),
            files=tuple(
                GpuSpatialSourceFileIntegrity(
                    relative_path=item.relative_path,
                    file_type=item.file_type,
                    size_bytes=item.size_bytes,
                    sha256=item.sha256,
                    category=item.category,
                )
                for _, item in family
            ),
            ogr_fids=ogr_fids,
            data=reread,
        )
    except GpuSpatialInspectionError:
        raise
    except Exception as error:
        raise GpuSpatialInspectionError(
            "GPU spatial source cannot be revalidated"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `revalidate_gpu_spatial_layer_source`

**Exact signature**

```python
def revalidate_gpu_spatial_layer_source(
    planning_document: GpuPlanningDocument,
    inspected_layer: GpuInspectedLayer,
) -> GpuValidatedSpatialLayerSource:
```

**Purpose**

Verify and freshly reload one extracted GPU spatial-layer source.

**Return contract**

- Declared return annotation: `GpuValidatedSpatialLayerSource`.
- Every observed return expression is reproduced without truncation:
```python
_revalidate_gpu_spatial_layer_source(planning_document, inspected_layer, verify_extraction_manifest=True)
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

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_revalidate_zoning_source` via `revalidate_gpu_spatial_layer_source`.
- import/re-export: `src/landscout/stages/index_planning_regulation.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`.

**Complete source-ordered implementation**

```python
def revalidate_gpu_spatial_layer_source(
    planning_document: GpuPlanningDocument,
    inspected_layer: GpuInspectedLayer,
) -> GpuValidatedSpatialLayerSource:
    """Verify and freshly reload one extracted GPU spatial-layer source."""

    return _revalidate_gpu_spatial_layer_source(
        planning_document,
        inspected_layer,
        verify_extraction_manifest=True,
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_revalidate_gpu_spatial_layer_sources`

**Exact signature**

```python
def _revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
```

**Purpose**

Private `planning` helper for revalidate gpu spatial layer sources; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[GpuValidatedSpatialLayerSource, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple((_revalidate_gpu_spatial_layer_source(planning_document, layer, verify_extraction_manifest=False) for layer in inspected_layers))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(planning_document, GpuPlanningDocument)`.
- Guard with a raise path: `type(inspected_layers) is not tuple`.
- Guard with a raise path: `any((not isinstance(layer, GpuInspectedLayer) for layer in inspected_layers))`.
- Guard with a raise path: `len({layer.logical_name for layer in inspected_layers}) != len(inspected_layers)`.
- Guard with a raise path: `planning_document.extraction.files != manifest_files`.
- Explicit raise expressions: `GpuSpatialInspectionError('Every inspected GPU spatial layer must be a GpuInspectedLayer')`, `GpuSpatialInspectionError('GPU extraction inventory differs from its verified manifest')`, `GpuSpatialInspectionError('GPU extraction manifest cannot verify the spatial sources')`, `GpuSpatialInspectionError('Inspected GPU spatial layers contain a duplicate logical name')`, `GpuSpatialInspectionError('Inspected GPU spatial layers must be an immutable tuple')`, `GpuSpatialInspectionError('planning_document must be a GpuPlanningDocument')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::revalidate_gpu_spatial_layer_sources` via `_revalidate_gpu_spatial_layer_sources`.

**Complete source-ordered implementation**

```python
def _revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
    if not isinstance(planning_document, GpuPlanningDocument):
        raise GpuSpatialInspectionError(
            "planning_document must be a GpuPlanningDocument"
        )
    if type(inspected_layers) is not tuple:
        raise GpuSpatialInspectionError(
            "Inspected GPU spatial layers must be an immutable tuple"
        )
    if any(not isinstance(layer, GpuInspectedLayer) for layer in inspected_layers):
        raise GpuSpatialInspectionError(
            "Every inspected GPU spatial layer must be a GpuInspectedLayer"
        )
    if len({layer.logical_name for layer in inspected_layers}) != len(
        inspected_layers
    ):
        raise GpuSpatialInspectionError(
            "Inspected GPU spatial layers contain a duplicate logical name"
        )
    try:
        root, _ = _validated_spatial_root(planning_document.extraction)
        manifest_files = _validate_extraction_manifest(
            root, planning_document.extraction.archive
        )
    except (AttributeError, TypeError, GpuArchiveError) as error:
        raise GpuSpatialInspectionError(
            "GPU extraction manifest cannot verify the spatial sources"
        ) from error
    if planning_document.extraction.files != manifest_files:
        raise GpuSpatialInspectionError(
            "GPU extraction inventory differs from its verified manifest"
        )
    return tuple(
        _revalidate_gpu_spatial_layer_source(
            planning_document,
            layer,
            verify_extraction_manifest=False,
        )
        for layer in inspected_layers
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `revalidate_gpu_spatial_layer_sources`

**Exact signature**

```python
def revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
```

**Purpose**

Verify an ordered collection of extracted GPU spatial-layer sources.

**Return contract**

- Declared return annotation: `tuple[GpuValidatedSpatialLayerSource, ...]`.
- Every observed return expression is reproduced without truncation:
```python
_revalidate_gpu_spatial_layer_sources(planning_document, inspected_layers)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `GpuSpatialInspectionError('GPU spatial-layer batch input or validation is malformed')`, `re-raise`.

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

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs` via `revalidate_gpu_spatial_layer_sources`.
- import/re-export: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::validate_normalized_planning_zoning_inputs` via `revalidate_gpu_spatial_layer_sources`.
- import/re-export: `src/landscout/stages/enrich_planning_zoning.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    revalidate_gpu_spatial_layer_sources,
)`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_malformed_layer_items` via `gpu_source_module.revalidate_gpu_spatial_layer_sources`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_malformed_layer_items` via `gpu_source_module.revalidate_gpu_spatial_layer_sources`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_malformed_planning_document` via `gpu_source_module.revalidate_gpu_spatial_layer_sources`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_malformed_planning_document` via `gpu_source_module.revalidate_gpu_spatial_layer_sources`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_duplicate_logical_name` via `gpu_source_module.revalidate_gpu_spatial_layer_sources`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::test_batch_gpu_revalidation_rejects_duplicate_logical_name` via `gpu_source_module.revalidate_gpu_spatial_layer_sources`.
- property/attribute access: `tests/unit/test_enrich_planning_zoning.py::test_source_complete_zoning_validation_revalidates_physical_source_once` via `module.revalidate_gpu_spatial_layer_sources`.
- property/attribute access: `tests/unit/test_resolve_planning_feature_codes.py::test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats` via `enrich_module.revalidate_gpu_spatial_layer_sources`.

**Complete source-ordered implementation**

```python
def revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
    """Verify an ordered collection of extracted GPU spatial-layer sources."""

    try:
        return _revalidate_gpu_spatial_layer_sources(
            planning_document, inspected_layers
        )
    except GpuSpatialInspectionError:
        raise
    except Exception as error:
        raise GpuSpatialInspectionError(
            "GPU spatial-layer batch input or validation is malformed"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_crs_text`

**Exact signature**

```python
def _crs_text(frame: gpd.GeoDataFrame) -> str:
```

**Purpose**

Private `planning` helper for crs text; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
f'{authority[0]}:{authority[1]}' if authority else frame.crs.to_string()

'UNKNOWN'
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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_summarize_layer` via `_crs_text`.

**Complete source-ordered implementation**

```python
def _crs_text(frame: gpd.GeoDataFrame) -> str:
    if frame.crs is None:
        return "UNKNOWN"
    authority = CRS.from_user_input(frame.crs).to_authority()
    return f"{authority[0]}:{authority[1]}" if authority else frame.crs.to_string()
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_summarize_layer`

**Exact signature**

```python
def _summarize_layer(
    frame: gpd.GeoDataFrame,
    reference: GpuSpatialLayerReference,
    extraction: GpuExtraction,
) -> GpuLayerSummary:
```

**Purpose**

Private `planning` helper for summarize layer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `GpuLayerSummary`.
- Every observed return expression is reproduced without truncation:
```python
GpuLayerSummary(source_document_id=extraction.archive.document.document_id, source_archive_sha256=extraction.archive.sha256, source_layer=reference.source_layer, crs=_crs_text(frame), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_counts=tuple(((str(column), int(frame[column].isna().sum())) for column in frame.columns)), geometry_types=geometry_types, null_geometry_count=int((~non_null).sum()), empty_geometry_count=int((non_null & geometry.is_empty).sum()), invalid_geometry_count=int(invalid.sum()))
```

**Validation and exceptions**

- Guard with a raise path: `frame.geometry.name not in frame.columns`.
- Explicit raise expressions: `GpuSpatialInspectionError(f'GPU layer has no active geometry: {reference.source_layer}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(non_null & geometry.is_empty).sum`, `geometry.notna`, `geometry[non_null].geom_type.value_counts`, `geometry[non_null].geom_type.value_counts().sort_index`, `geometry[non_null].geom_type.value_counts().sort_index().items`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/gpu_fr.py::_revalidate_gpu_spatial_layer_source` via `_summarize_layer`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::inspect_gpu_planning_document` via `_summarize_layer`.

**Complete source-ordered implementation**

```python
def _summarize_layer(
    frame: gpd.GeoDataFrame,
    reference: GpuSpatialLayerReference,
    extraction: GpuExtraction,
) -> GpuLayerSummary:
    if frame.geometry.name not in frame.columns:
        raise GpuSpatialInspectionError(
            f"GPU layer has no active geometry: {reference.source_layer}"
        )
    geometry = frame.geometry
    non_null = geometry.notna()
    non_empty = non_null & ~geometry.is_empty
    invalid = non_empty & ~geometry.is_valid
    geometry_types = tuple(
        (str(key), int(value))
        for key, value in geometry[non_null].geom_type.value_counts().sort_index().items()
    )
    return GpuLayerSummary(
        source_document_id=extraction.archive.document.document_id,
        source_archive_sha256=extraction.archive.sha256,
        source_layer=reference.source_layer,
        crs=_crs_text(frame),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in frame.dtypes.items()),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=geometry_types,
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int(invalid.sum()),
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `inspect_gpu_planning_document`

**Exact signature**

```python
def inspect_gpu_planning_document(
    extraction: GpuExtraction, config: GpuSourceConfig
) -> GpuPlanningDocument:
```

**Purpose**

Discover and inspect zoning/prescription layers without interpretation.

**Return contract**

- Declared return annotation: `GpuPlanningDocument`.
- Every observed return expression is reproduced without truncation:
```python
GpuPlanningDocument(extraction=extraction, all_spatial_layers=references, zoning=zoning, related_layers=tuple(related))
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

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::ingest_gpu_planning_document` via `inspect_gpu_planning_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_spatial_inventory_and_inspection_preserve_source_quality` via `inspect_gpu_planning_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_missing_zoning_layer_fails_clearly` via `inspect_gpu_planning_document`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_ambiguous_zoning_layer_fails_clearly` via `inspect_gpu_planning_document`.
- import/re-export: `tests/unit/test_gpu_fr.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def inspect_gpu_planning_document(
    extraction: GpuExtraction, config: GpuSourceConfig
) -> GpuPlanningDocument:
    """Discover and inspect zoning/prescription layers without interpretation."""

    references = discover_gpu_spatial_layers(extraction)
    zoning_reference = _discover_logical_layer(
        references, config, "zoning", required=True
    )
    assert zoning_reference is not None
    zoning_data = _load_reference(zoning_reference)
    zoning = GpuInspectedLayer(
        logical_name="zoning",
        reference=zoning_reference,
        data=zoning_data,
        summary=_summarize_layer(zoning_data, zoning_reference, extraction),
    )
    related: list[GpuInspectedLayer] = []
    logical_names: tuple[LogicalLayerName, ...] = (
        "prescription_surface",
        "prescription_line",
        "prescription_point",
        "information_surface",
        "information_line",
        "information_point",
    )
    for logical_name in logical_names:
        reference = _discover_logical_layer(
            references, config, logical_name, required=False
        )
        if reference is None:
            continue
        data = _load_reference(reference)
        related.append(
            GpuInspectedLayer(
                logical_name=logical_name,
                reference=reference,
                data=data,
                summary=_summarize_layer(data, reference, extraction),
            )
        )
    return GpuPlanningDocument(
        extraction=extraction,
        all_spatial_layers=references,
        zoning=zoning,
        related_layers=tuple(related),
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `ingest_gpu_planning_document`

**Exact signature**

```python
def ingest_gpu_planning_document(
    config: GpuSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> GpuPlanningDocument:
```

**Purpose**

High-level official GPU discovery, acquisition, extraction and inspection.

**Return contract**

- Declared return annotation: `GpuPlanningDocument`.
- Every observed return expression is reproduced without truncation:
```python
inspect_gpu_planning_document(extraction, config)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `download_gpu_document`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`.

**Complete source-ordered implementation**

```python
def ingest_gpu_planning_document(
    config: GpuSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> GpuPlanningDocument:
    """High-level official GPU discovery, acquisition, extraction and inspection."""

    document = discover_current_gpu_document(config, timeout=timeout)
    download = download_gpu_document(document, config, cache_dir, timeout)
    extraction = extract_gpu_document(download, cache_dir)
    return inspect_gpu_planning_document(extraction, config)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `finite_numeric_vocabulary`

**Exact signature**

```python
def finite_numeric_vocabulary(
    frame: gpd.GeoDataFrame, column: str
) -> tuple[tuple[str, int], ...]:
```

**Purpose**

Return deterministic raw value counts for inspection-only reporting.

**Return contract**

- Declared return annotation: `tuple[tuple[str, int], ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(sorted(result, key=lambda item: item[0]))
```

**Validation and exceptions**

- Guard with a raise path: `column not in frame.columns or column == frame.geometry.name`.
- Explicit raise expressions: `GpuSpatialInspectionError(f'Cannot inspect GPU attribute: {column}')`.

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
def finite_numeric_vocabulary(
    frame: gpd.GeoDataFrame, column: str
) -> tuple[tuple[str, int], ...]:
    """Return deterministic raw value counts for inspection-only reporting."""

    if column not in frame.columns or column == frame.geometry.name:
        raise GpuSpatialInspectionError(f"Cannot inspect GPU attribute: {column}")
    counts = frame[column].value_counts(dropna=False)
    result: list[tuple[str, int]] = []
    for value, count in counts.items():
        if isinstance(value, float) and math.isnan(value) or value is None:
            label = "<NULL>"
        else:
            label = str(value)
        result.append((label, int(count)))
    return tuple(sorted(result, key=lambda item: item[0]))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### Frame-preservation and semantic notes

- `written_files` is a GPU metadata/sidecar mapping field. It is not a spatial-frame column unless a later documented result schema explicitly introduces a same-named field.

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

- Configured source identity: exact official GPU API origin, partition/commune/document type/status and logical layer rules; loaded config is revalidated before URL construction.
- URL/safe transport: metadata/archive requests use open_safe_https; written-file and document archive URLs must match exact official document-specific paths.
- Physical bytes/cache/archive/extraction: ZIP size/SHA/sidecar/member paths and extraction inventory/marker are validated transactionally.
- Physical layer selection: inspected GeoPackages and logical layers carry per-file/layer integrity envelopes; later planning stages call revalidate_gpu_spatial_layer_source(s) before use.
- Result/later revalidation: GpuPlanningDocument packages document, extraction, spatial and written evidence; caller-forged nested written-file provenance is rejected before network.

## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the planning flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
