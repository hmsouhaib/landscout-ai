# `src/landscout/sources/gpu_fr.py`

## File identity

- Repository path: `src/landscout/sources/gpu_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: official source acquisition and physical authority
- Responsibility: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.
- Source SHA256: `fe34ea035dc7536ef448f23f5cb3df9b8731a8cc866418732cc9f558c60400e4`

## 1. STEP 7F.1A.4 contract delta

- Binds full immutable GPU config identity, strict JSON, globally unique logical roles, complete fresh physical-layer inventory, and link-safe transactional archive/extraction recovery.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

The file belongs to the **source adapter** layer and **official source acquisition and physical authority** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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
- `from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)`
- `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `DEFAULT_CONFIG_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEFAULT_CONFIG_PATH = Path("configs/sources/gpu_fr.yaml")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DEFAULT_CACHE_DIR`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEFAULT_CACHE_DIR = Path("data/cache/gpu")
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

### `USER_AGENT`

- Category: module constant or closed domain.
- Exact declaration:

```python
USER_AGENT = "LandScout-AI/0.1"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXTRACTION_MANIFEST_NAME`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXTRACTION_MANIFEST_NAME = ".landscout-gpu-extraction.json"
```

- Qualified consumers:
  - import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
  - value/type reference: `tests.unit.test_enrich_planning_features::_physical_inventory` via `EXTRACTION_MANIFEST_NAME`
  - value/type reference: `tests.unit.test_enrich_planning_features::_write_extraction_manifest` via `EXTRACTION_MANIFEST_NAME`
  - import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
  - value/type reference: `tests.unit.test_enrich_planning_zoning::_physical_planning_document` via `EXTRACTION_MANIFEST_NAME`
  - import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
  - value/type reference: `tests.unit.test_resolve_planning_feature_codes::_physical_inventory` via `EXTRACTION_MANIFEST_NAME`
  - value/type reference: `tests.unit.test_resolve_planning_feature_codes::_write_extraction_manifest` via `EXTRACTION_MANIFEST_NAME`

### `EXTRACTION_MANIFEST_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
EXTRACTION_MANIFEST_SCHEMA_VERSION = 2
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

### `CommuneCode`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
CommuneCode = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[0-9]{5}$"),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DownloadStrategy`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
DownloadStrategy = Literal["partition"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `LogicalLayerName`

- Category: type alias or closed annotated domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `FileCategory`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
FileCategory = Literal[
    "SPATIAL_DATA", "METADATA", "WRITTEN_REGULATION", "OTHER_ATTACHMENT"
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `GpuOfficialSourceIdentity`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
GpuOfficialSourceIdentity = Literal["G\u00e9oportail de l'Urbanisme"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_WINDOWS_RESERVED_BASENAMES`

- Category: module constant or closed domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_GPU_LOGICAL_LAYER_NAMES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_GPU_LOGICAL_LAYER_NAMES: tuple[LogicalLayerName, ...] = (
    "zoning",
    "prescription_surface",
    "prescription_line",
    "prescription_point",
    "information_surface",
    "information_line",
    "information_point",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `zoning`
  - `prescription_surface`
  - `prescription_line`
  - `prescription_point`
  - `information_surface`
  - `information_line`
  - `information_point`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `GpuApiConfig`

**Source purpose:** Defines `GpuApiConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

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
class GpuApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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

**Source purpose:** Defines `GpuDownloadConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `strategy` | `DownloadStrategy` | `required` | `strategy: DownloadStrategy` |
| `partition_template` | `NonEmptyString` | `required` | `partition_template: NonEmptyString` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class GpuDownloadConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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

**Source purpose:** Defines `GpuCacheConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `max_age_hours` | `float` | `Field(ge=0, allow_inf_nan=False)` | `max_age_hours: float = Field(ge=0, allow_inf_nan=False)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class GpuCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    max_age_hours: float = Field(ge=0, allow_inf_nan=False)

    @field_validator("max_age_hours", mode="before")
    @classmethod
    def _strict_finite_number(cls, value: object) -> object:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or type(value) not in {int, float}
        ):
            raise ValueError("max_age_hours must be an exact finite number")
        if not math.isfinite(value):
            raise ValueError("max_age_hours must be finite")
        return value
```

### `GpuPilotConfig`

**Source purpose:** Defines `GpuPilotConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `commune_code` | `CommuneCode` | `required` | `commune_code: CommuneCode` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class GpuPilotConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    commune_code: CommuneCode
```

### `GpuLogicalLayerConfig`

**Source purpose:** Defines `GpuLogicalLayerConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `class_label` | `NonEmptyString` | `required` | `class_label: NonEmptyString` |
| `match_tokens` | `tuple[NonEmptyString, ...]` | `Field(min_length=1)` | `match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.sources.gpu_fr::_layer_config` via `GpuLogicalLayerConfig`

**Exact class source**

```python
class GpuLogicalLayerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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

**Source purpose:** Defines `GpuSpatialLayersConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `zoning` | `GpuLogicalLayerConfig` | `required` | `zoning: GpuLogicalLayerConfig` |
| `prescription_surface` | `GpuLogicalLayerConfig` | `required` | `prescription_surface: GpuLogicalLayerConfig` |
| `prescription_line` | `GpuLogicalLayerConfig` | `required` | `prescription_line: GpuLogicalLayerConfig` |
| `prescription_point` | `GpuLogicalLayerConfig` | `required` | `prescription_point: GpuLogicalLayerConfig` |
| `information_surface` | `GpuLogicalLayerConfig` | `required` | `information_surface: GpuLogicalLayerConfig` |
| `information_line` | `GpuLogicalLayerConfig` | `required` | `information_line: GpuLogicalLayerConfig` |
| `information_point` | `GpuLogicalLayerConfig` | `required` | `information_point: GpuLogicalLayerConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class GpuSpatialLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    zoning: GpuLogicalLayerConfig
    prescription_surface: GpuLogicalLayerConfig
    prescription_line: GpuLogicalLayerConfig
    prescription_point: GpuLogicalLayerConfig
    information_surface: GpuLogicalLayerConfig
    information_line: GpuLogicalLayerConfig
    information_point: GpuLogicalLayerConfig
```

### `GpuSourceConfig`

**Source purpose:** Strict configuration for official French GPU ingestion.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `provider` | `GpuOfficialSourceIdentity` | `required` | `provider: GpuOfficialSourceIdentity` |
| `portal` | `GpuOfficialSourceIdentity` | `required` | `portal: GpuOfficialSourceIdentity` |
| `country` | `Literal['FR']` | `required` | `country: Literal["FR"]` |
| `api` | `GpuApiConfig` | `required` | `api: GpuApiConfig` |
| `download` | `GpuDownloadConfig` | `required` | `download: GpuDownloadConfig` |
| `cache` | `GpuCacheConfig` | `required` | `cache: GpuCacheConfig` |
| `pilot` | `GpuPilotConfig` | `required` | `pilot: GpuPilotConfig` |
| `spatial_layers` | `GpuSpatialLayersConfig` | `required` | `spatial_layers: GpuSpatialLayersConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `landscout.sources.gpu_fr::load_gpu_source_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_validated_source_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_partition` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_api_url` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_document_list_url` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_partition_download_url` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_written_files` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_layer_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_discover_logical_layer` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_configured_logical_references` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `GpuSourceConfig`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `GpuSourceConfig`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuSourceConfig`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `tests.unit.test_gpu_fr::_config` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_invalid_config_values_are_rejected` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_source_identity_is_exact` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_cache_age_rejects_coercion_and_nonfinite` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_source_config_identity_is_deterministic_and_content_bound` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_unknown_config_field_is_rejected` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::_config_with_shared_role_token` via `GpuSourceConfig`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `GpuSourceConfig`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuSourceConfig`

**Exact class source**

```python
class GpuSourceConfig(BaseModel):
    """Strict configuration for official French GPU ingestion."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: GpuOfficialSourceIdentity
    portal: GpuOfficialSourceIdentity
    country: Literal["FR"]
    api: GpuApiConfig
    download: GpuDownloadConfig
    cache: GpuCacheConfig
    pilot: GpuPilotConfig
    spatial_layers: GpuSpatialLayersConfig
```

### `GpuError`

**Source purpose:** Base class for controlled GPU source failures.

- Exact decorators: none.
- Exact bases: `RuntimeError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`

**Exact class source**

```python
class GpuError(RuntimeError):
    """Base class for controlled GPU source failures."""
```

### `GpuConfigError`

**Source purpose:** Raised when GPU source configuration is invalid.

- Exact decorators: none.
- Exact bases: `GpuError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::load_gpu_source_config` via `GpuConfigError`
- value/type reference: `landscout.sources.gpu_fr::load_gpu_source_config` via `GpuConfigError`
- constructor call: `landscout.sources.gpu_fr::_validated_source_config` via `GpuConfigError`
- value/type reference: `landscout.sources.gpu_fr::_validated_source_config` via `GpuConfigError`
- constructor call: `landscout.sources.gpu_fr::_source_config_sha256` via `GpuConfigError`
- value/type reference: `landscout.sources.gpu_fr::_source_config_sha256` via `GpuConfigError`
- constructor call: `landscout.sources.gpu_fr::build_gpu_partition` via `GpuConfigError`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_partition` via `GpuConfigError`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `GpuConfigError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `GpuConfigError`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `GpuConfigError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuConfigError`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuConfigError`

**Exact class source**

```python
class GpuConfigError(GpuError):
    """Raised when GPU source configuration is invalid."""
```

### `GpuDiscoveryError`

**Source purpose:** Raised when the current planning document cannot be resolved safely.

- Exact decorators: none.
- Exact bases: `GpuError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::_request_json` via `GpuDiscoveryError`
- value/type reference: `landscout.sources.gpu_fr::_request_json` via `GpuDiscoveryError`
- constructor call: `landscout.sources.gpu_fr::_required_string` via `GpuDiscoveryError`
- value/type reference: `landscout.sources.gpu_fr::_required_string` via `GpuDiscoveryError`
- constructor call: `landscout.sources.gpu_fr::_optional_string` via `GpuDiscoveryError`
- value/type reference: `landscout.sources.gpu_fr::_optional_string` via `GpuDiscoveryError`
- constructor call: `landscout.sources.gpu_fr::_written_files` via `GpuDiscoveryError`
- value/type reference: `landscout.sources.gpu_fr::_written_files` via `GpuDiscoveryError`
- constructor call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `GpuDiscoveryError`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `GpuDiscoveryError`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `tests.unit.test_gpu_fr::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `GpuDiscoveryError`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_api_json_is_strict_before_document_selection` via `GpuDiscoveryError`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `GpuDiscoveryError`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `GpuDiscoveryError`
- value/type reference: `tests.unit.test_gpu_fr::test_no_current_document_is_rejected` via `GpuDiscoveryError`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_current_documents_are_rejected` via `GpuDiscoveryError`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_document_identity_is_rejected` via `GpuDiscoveryError`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `GpuDiscoveryError`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `GpuDiscoveryError`
- value/type reference: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `GpuDiscoveryError`

**Exact class source**

```python
class GpuDiscoveryError(GpuError):
    """Raised when the current planning document cannot be resolved safely."""
```

### `GpuDownloadError`

**Source purpose:** Raised when the GPU archive cannot be downloaded or cached safely.

- Exact decorators: none.
- Exact bases: `GpuError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `GpuDownloadError`
- constructor call: `landscout.sources.gpu_fr::_safe_gpu_archive_filename` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::_safe_gpu_archive_filename` via `GpuDownloadError`
- constructor call: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `GpuDownloadError`
- constructor call: `landscout.sources.gpu_fr::_require_no_cache_recovery_material` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::_require_no_cache_recovery_material` via `GpuDownloadError`
- constructor call: `landscout.sources.gpu_fr::_prepare_temporary_cache_file` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::_prepare_temporary_cache_file` via `GpuDownloadError`
- constructor call: `landscout.sources.gpu_fr::_cleanup_temporary_cache_files` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::_cleanup_temporary_cache_files` via `GpuDownloadError`
- constructor call: `landscout.sources.gpu_fr::_publish_cache_pair` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::_publish_cache_pair` via `GpuDownloadError`
- constructor call: `landscout.sources.gpu_fr::download_gpu_document` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `GpuDownloadError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuDownloadError`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_document_inconsistent_with_config` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_forged_written_file_provenance_before_network` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_forged_unsafe_archive_name_before_io` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_recovery_backup_rejects_cache_before_network` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_failed_refresh_preserves_previous_cache` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_metadata_publication_failure_rolls_back_both_cache_files` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `GpuDownloadError`
- value/type reference: `tests.unit.test_gpu_fr::test_corrupt_download_is_rejected` via `GpuDownloadError`

**Exact class source**

```python
class GpuDownloadError(GpuError):
    """Raised when the GPU archive cannot be downloaded or cached safely."""
```

### `GpuArchiveError`

**Source purpose:** Raised when a GPU archive or extraction is corrupt or unsafe.

- Exact decorators: none.
- Exact bases: `GpuError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::_windows_member_component` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_windows_member_component` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::_validated_zip_destinations` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_validated_zip_destinations` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::validate_gpu_archive` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::validate_gpu_archive` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_load_cached_archive` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::_inventory` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_inventory` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::_cleanup_temporary_extraction_directory` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_cleanup_temporary_extraction_directory` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::_require_no_extraction_recovery_material` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_require_no_extraction_recovery_material` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::_prepare_temporary_extraction_directory` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_prepare_temporary_extraction_directory` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::_publish_extraction_directory` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_publish_extraction_directory` via `GpuArchiveError`
- constructor call: `landscout.sources.gpu_fr::extract_gpu_document` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `GpuArchiveError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuArchiveError`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `tests.unit.test_gpu_fr::test_archive_path_traversal_is_rejected` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_archive_symlink_is_rejected` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_duplicate_zip_extraction_targets_are_rejected` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_zip_file_directory_target_collision_is_rejected` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_zip_cannot_claim_extraction_manifest_path` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_extraction_backup_fails_closed_and_is_preserved` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_publication_and_rollback_failure_preserves_backup` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_publication_failure_restores_existing_root` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_backup_move_failure_preserves_existing_root` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_inventory_rejects_special_entry` via `GpuArchiveError`
- constructor call: `tests.unit.test_gpu_fr::test_extraction_cleanup_preserves_primary_controlled_error` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_cleanup_preserves_primary_controlled_error` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_temporary_link_is_rejected_without_unlinking_target` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_extraction_temporary_directory_fails_closed_and_is_preserved` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_download_object_rejects_replaced_valid_archive` via `GpuArchiveError`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_rejects_archive_object_inconsistent_with_path` via `GpuArchiveError`

**Exact class source**

```python
class GpuArchiveError(GpuError):
    """Raised when a GPU archive or extraction is corrupt or unsafe."""
```

### `GpuSpatialInspectionError`

**Source purpose:** Raised when required GPU spatial layers cannot be inspected safely.

- Exact decorators: none.
- Exact bases: `GpuError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::discover_gpu_spatial_layers` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::discover_gpu_spatial_layers` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_discover_logical_layer` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_discover_logical_layer` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_configured_logical_references` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_configured_logical_references` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_load_reference` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_load_reference` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_validated_inventory_path` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_validated_inventory_path` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_validated_spatial_root` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_validated_spatial_root` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_spatial_inventory` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_spatial_inventory` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_contained_spatial_path` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_contained_spatial_path` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_spatial_dataset_relative_path` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_spatial_dataset_relative_path` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_spatial_source_family` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_spatial_source_family` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_same_spatial_crs` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_same_spatial_crs` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_compare_inspected_spatial_layer` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_compare_inspected_spatial_layer` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_sources` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_sources` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_sources` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_sources` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::_summarize_layer` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::_summarize_layer` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuSpatialInspectionError`
- constructor call: `landscout.sources.gpu_fr::finite_numeric_vocabulary` via `GpuSpatialInspectionError`
- value/type reference: `landscout.sources.gpu_fr::finite_numeric_vocabulary` via `GpuSpatialInspectionError`
- import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`
- value/type reference: `landscout.stages.enrich_planning_features::_normalized_catalogs` via `GpuSpatialInspectionError`
- import: `landscout.stages.enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    revalidate_gpu_spatial_layer_sources,
)`
- value/type reference: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `GpuSpatialInspectionError`
- import: `landscout.stages.index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`
- value/type reference: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `GpuSpatialInspectionError`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `GpuSpatialInspectionError`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `GpuSpatialInspectionError`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_one_physical_layer_for_two_logical_roles` via `GpuSpatialInspectionError`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_mutated_config_before_layer_discovery` via `GpuSpatialInspectionError`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_archive_byte_mutation_before_layer_discovery` via `GpuSpatialInspectionError`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_document_lineage_not_matching_config` via `GpuSpatialInspectionError`
- value/type reference: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `GpuSpatialInspectionError`
- value/type reference: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `GpuSpatialInspectionError`

**Exact class source**

```python
class GpuSpatialInspectionError(GpuError):
    """Raised when required GPU spatial layers cannot be inspected safely."""
```

### `GpuWrittenFile`

**Source purpose:** Defines `GpuWrittenFile`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `filename` | `str` | `required` | `filename: str` |
| `title` | `str \| None` | `required` | `title: str \| None` |
| `document_path` | `str \| None` | `required` | `document_path: str \| None` |
| `source_url` | `str \| None` | `required` | `source_url: str \| None` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::_written_files` via `GpuWrittenFile`
- value/type reference: `landscout.sources.gpu_fr::_written_files` via `GpuWrittenFile`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `GpuWrittenFile`
- constructor call: `landscout.sources.gpu_fr::_document_from_dict` via `GpuWrittenFile`
- value/type reference: `landscout.sources.gpu_fr::_document_from_dict` via `GpuWrittenFile`
- import: `landscout.stages.index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`
- value/type reference: `landscout.stages.index_planning_regulation::_written_file_matches` via `GpuWrittenFile`
- value/type reference: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `GpuWrittenFile`
- value/type reference: `landscout.stages.index_planning_regulation::_source_selection_sha256` via `GpuWrittenFile`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- constructor call: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `GpuWrittenFile`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `GpuWrittenFile`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_index_planning_regulation::_document` via `GpuWrittenFile`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `GpuWrittenFile`

**Exact class source**

```python
class GpuWrittenFile:
    filename: str
    title: str | None
    document_path: str | None
    source_url: str | None
```

### `GpuDocumentMetadata`

**Source purpose:** Defines `GpuDocumentMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `provider` | `str` | `required` | `provider: str` |
| `portal` | `str` | `required` | `portal: str` |
| `commune_code` | `str` | `required` | `commune_code: str` |
| `partition` | `str` | `required` | `partition: str` |
| `document_id` | `str` | `required` | `document_id: str` |
| `document_family` | `str` | `required` | `document_family: str` |
| `document_type` | `str` | `required` | `document_type: str` |
| `document_title` | `str \| None` | `required` | `document_title: str \| None` |
| `status` | `str` | `required` | `status: str` |
| `legal_status` | `str` | `required` | `legal_status: str` |
| `effective_status` | `str` | `required` | `effective_status: str` |
| `version` | `str \| None` | `required` | `version: str \| None` |
| `archive_name` | `str` | `required` | `archive_name: str` |
| `publication_timestamp` | `str \| None` | `required` | `publication_timestamp: str \| None` |
| `update_timestamp` | `str \| None` | `required` | `update_timestamp: str \| None` |
| `revision_date` | `str \| None` | `required` | `revision_date: str \| None` |
| `producer` | `str \| None` | `required` | `producer: str \| None` |
| `standard_model` | `str \| None` | `required` | `standard_model: str \| None` |
| `projection` | `str \| None` | `required` | `projection: str \| None` |
| `metadata_identifier` | `str \| None` | `required` | `metadata_identifier: str \| None` |
| `source_url` | `str` | `required` | `source_url: str` |
| `written_files` | `tuple[GpuWrittenFile, ...]` | `required` | `written_files: tuple[GpuWrittenFile, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `GpuDocumentMetadata`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `GpuDocumentMetadata`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `GpuDocumentMetadata`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `GpuDocumentMetadata`
- value/type reference: `landscout.sources.gpu_fr::_document_identity` via `GpuDocumentMetadata`
- constructor call: `landscout.sources.gpu_fr::_document_from_dict` via `GpuDocumentMetadata`
- value/type reference: `landscout.sources.gpu_fr::_document_from_dict` via `GpuDocumentMetadata`
- value/type reference: `landscout.sources.gpu_fr::_load_cached_archive` via `GpuDocumentMetadata`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `GpuDocumentMetadata`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `GpuDocumentMetadata`
- import: `landscout.stages.index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `GpuDocumentMetadata`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- constructor call: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `GpuDocumentMetadata`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `GpuDocumentMetadata`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuDocumentMetadata`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuDocumentMetadata`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuDocumentMetadata`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuDocumentMetadata`
- constructor call: `tests.unit.test_gpu_fr::_extraction_from_archive` via `gpu.GpuDocumentMetadata`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_index_planning_regulation::_document` via `GpuDocumentMetadata`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `GpuDocumentMetadata`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuDocumentMetadata`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuDocumentMetadata`

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

**Source purpose:** Defines `GpuArchiveDownload`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document` | `GpuDocumentMetadata` | `required` | `document: GpuDocumentMetadata` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `filename` | `str` | `required` | `filename: str` |
| `archive_format` | `str` | `required` | `archive_format: str` |
| `file_size` | `int` | `required` | `file_size: int` |
| `sha256` | `str` | `required` | `sha256: str` |
| `path` | `Path` | `required` | `path: Path` |
| `cache_hit` | `bool` | `required` | `cache_hit: bool` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `GpuArchiveDownload`
- constructor call: `landscout.sources.gpu_fr::_load_cached_archive` via `GpuArchiveDownload`
- value/type reference: `landscout.sources.gpu_fr::_load_cached_archive` via `GpuArchiveDownload`
- constructor call: `landscout.sources.gpu_fr::download_gpu_document` via `GpuArchiveDownload`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `GpuArchiveDownload`
- value/type reference: `landscout.sources.gpu_fr::_manifest_payload` via `GpuArchiveDownload`
- value/type reference: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `GpuArchiveDownload`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `GpuArchiveDownload`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `GpuArchiveDownload`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuArchiveDownload`
- import: `landscout.stages.index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `GpuArchiveDownload`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- constructor call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `GpuArchiveDownload`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `GpuArchiveDownload`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuArchiveDownload`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuArchiveDownload`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuArchiveDownload`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuArchiveDownload`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `tests.unit.test_gpu_fr::_download` via `GpuArchiveDownload`
- constructor call: `tests.unit.test_gpu_fr::_extraction_from_archive` via `GpuArchiveDownload`
- value/type reference: `tests.unit.test_gpu_fr::_extraction_from_archive` via `GpuArchiveDownload`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_index_planning_regulation::_document` via `GpuArchiveDownload`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `GpuArchiveDownload`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuArchiveDownload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuArchiveDownload`

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

**Source purpose:** Defines `GpuExtractedFile`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `relative_path` | `str` | `required` | `relative_path: str` |
| `file_type` | `str` | `required` | `file_type: str` |
| `size_bytes` | `int` | `required` | `size_bytes: int` |
| `sha256` | `str` | `required` | `sha256: str` |
| `category` | `FileCategory` | `required` | `category: FileCategory` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::_inventory` via `GpuExtractedFile`
- value/type reference: `landscout.sources.gpu_fr::_inventory` via `GpuExtractedFile`
- value/type reference: `landscout.sources.gpu_fr::_manifest_payload` via `GpuExtractedFile`
- value/type reference: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `GpuExtractedFile`
- value/type reference: `landscout.sources.gpu_fr::_spatial_inventory` via `GpuExtractedFile`
- value/type reference: `landscout.sources.gpu_fr::_spatial_source_family` via `GpuExtractedFile`
- import: `landscout.stages.index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`
- value/type reference: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `GpuExtractedFile`
- value/type reference: `landscout.stages.index_planning_regulation::_source_selection_sha256` via `GpuExtractedFile`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_features::_physical_inventory` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_enrich_planning_features::_physical_inventory` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_enrich_planning_features::_write_extraction_manifest` via `GpuExtractedFile`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_zoning::_physical_planning_document` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_physical_planning_document` via `GpuExtractedFile`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_index_planning_regulation::_inventory_item` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_index_planning_regulation::_inventory_item` via `GpuExtractedFile`
- constructor call: `tests.unit.test_index_planning_regulation::_spatial_inventory_item` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_index_planning_regulation::_spatial_inventory_item` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_index_planning_regulation::_write_zoning_source` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_index_planning_regulation::_fixture_document` via `GpuExtractedFile`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_physical_inventory` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_physical_inventory` via `GpuExtractedFile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_write_extraction_manifest` via `GpuExtractedFile`

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

**Source purpose:** Defines `GpuExtraction`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `archive` | `GpuArchiveDownload` | `required` | `archive: GpuArchiveDownload` |
| `extraction_root` | `Path` | `required` | `extraction_root: Path` |
| `files` | `tuple[GpuExtractedFile, ...]` | `required` | `files: tuple[GpuExtractedFile, ...]` |
| `standard_models` | `tuple[str, ...]` | `required` | `standard_models: tuple[str, ...]` |
| `cache_hit` | `bool` | `required` | `cache_hit: bool` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::extract_gpu_document` via `GpuExtraction`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `GpuExtraction`
- value/type reference: `landscout.sources.gpu_fr::discover_gpu_spatial_layers` via `GpuExtraction`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `GpuExtraction`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuExtraction`
- value/type reference: `landscout.sources.gpu_fr::_validated_spatial_root` via `GpuExtraction`
- value/type reference: `landscout.sources.gpu_fr::_spatial_inventory` via `GpuExtraction`
- value/type reference: `landscout.sources.gpu_fr::_spatial_source_family` via `GpuExtraction`
- value/type reference: `landscout.sources.gpu_fr::_summarize_layer` via `GpuExtraction`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuExtraction`
- import: `landscout.stages.index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `GpuExtraction`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuExtraction`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuExtraction`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuExtraction`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuExtraction`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `tests.unit.test_gpu_fr::_extraction_from_archive` via `GpuExtraction`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_index_planning_regulation::_document` via `GpuExtraction`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `GpuExtraction`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuExtraction`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuExtraction`

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

**Source purpose:** Defines `GpuSpatialLayerReference`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `dataset_path` | `Path` | `required` | `dataset_path: Path` |
| `source_layer` | `str` | `required` | `source_layer: str` |
| `driver` | `str` | `required` | `driver: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::discover_gpu_spatial_layers` via `GpuSpatialLayerReference`
- value/type reference: `landscout.sources.gpu_fr::discover_gpu_spatial_layers` via `GpuSpatialLayerReference`
- value/type reference: `landscout.sources.gpu_fr::_discover_logical_layer` via `GpuSpatialLayerReference`
- value/type reference: `landscout.sources.gpu_fr::_configured_logical_references` via `GpuSpatialLayerReference`
- value/type reference: `landscout.sources.gpu_fr::_load_reference` via `GpuSpatialLayerReference`
- value/type reference: `landscout.sources.gpu_fr::_spatial_dataset_relative_path` via `GpuSpatialLayerReference`
- value/type reference: `landscout.sources.gpu_fr::_spatial_source_family` via `GpuSpatialLayerReference`
- value/type reference: `landscout.sources.gpu_fr::_summarize_layer` via `GpuSpatialLayerReference`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_features::_inspected` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_enrich_planning_features::_inspected` via `GpuSpatialLayerReference`
- constructor call: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_enrich_planning_features::_replace_layer_reference` via `GpuSpatialLayerReference`
- constructor call: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `GpuSpatialLayerReference`
- constructor call: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `GpuSpatialLayerReference`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuSpatialLayerReference`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_index_planning_regulation::_write_zoning_source` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_index_planning_regulation::_write_zoning_source` via `GpuSpatialLayerReference`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuSpatialLayerReference`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_integration_layer` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_layer` via `GpuSpatialLayerReference`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_gpu_related_source_hash_is_deterministic_across_cache_roots.relocated_reference` via `GpuSpatialLayerReference`

**Exact class source**

```python
class GpuSpatialLayerReference:
    dataset_path: Path
    source_layer: str
    driver: str
```

### `GpuLayerSummary`

**Source purpose:** Defines `GpuLayerSummary`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `source_document_id` | `str` | `required` | `source_document_id: str` |
| `source_archive_sha256` | `str` | `required` | `source_archive_sha256: str` |
| `source_layer` | `str` | `required` | `source_layer: str` |
| `crs` | `str` | `required` | `crs: str` |
| `feature_count` | `int` | `required` | `feature_count: int` |
| `columns` | `tuple[str, ...]` | `required` | `columns: tuple[str, ...]` |
| `dtypes` | `tuple[tuple[str, str], ...]` | `required` | `dtypes: tuple[tuple[str, str], ...]` |
| `null_counts` | `tuple[tuple[str, int], ...]` | `required` | `null_counts: tuple[tuple[str, int], ...]` |
| `geometry_types` | `tuple[tuple[str, int], ...]` | `required` | `geometry_types: tuple[tuple[str, int], ...]` |
| `null_geometry_count` | `int` | `required` | `null_geometry_count: int` |
| `empty_geometry_count` | `int` | `required` | `empty_geometry_count: int` |
| `invalid_geometry_count` | `int` | `required` | `invalid_geometry_count: int` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::_summarize_layer` via `GpuLayerSummary`
- value/type reference: `landscout.sources.gpu_fr::_summarize_layer` via `GpuLayerSummary`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_features::_summary` via `GpuLayerSummary`
- value/type reference: `tests.unit.test_enrich_planning_features::_summary` via `GpuLayerSummary`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuLayerSummary`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuLayerSummary`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_index_planning_regulation::_summary` via `GpuLayerSummary`
- value/type reference: `tests.unit.test_index_planning_regulation::_summary` via `GpuLayerSummary`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_layer_summary` via `GpuLayerSummary`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_layer_summary` via `GpuLayerSummary`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_integration_layer` via `GpuLayerSummary`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_layer` via `GpuLayerSummary`

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

**Source purpose:** Defines `GpuInspectedLayer`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `logical_name` | `LogicalLayerName` | `required` | `logical_name: LogicalLayerName` |
| `reference` | `GpuSpatialLayerReference` | `required` | `reference: GpuSpatialLayerReference` |
| `data` | `gpd.GeoDataFrame` | `required` | `data: gpd.GeoDataFrame` |
| `summary` | `GpuLayerSummary` | `required` | `summary: GpuLayerSummary` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuInspectedLayer`
- value/type reference: `landscout.sources.gpu_fr::_compare_inspected_spatial_layer` via `GpuInspectedLayer`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `GpuInspectedLayer`
- value/type reference: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_source` via `GpuInspectedLayer`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_sources` via `GpuInspectedLayer`
- value/type reference: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_sources` via `GpuInspectedLayer`
- constructor call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuInspectedLayer`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuInspectedLayer`
- import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`
- value/type reference: `landscout.stages.enrich_planning_features::_validate_layer_summary` via `GpuInspectedLayer`
- value/type reference: `landscout.stages.enrich_planning_features::_source_feature_ids` via `GpuInspectedLayer`
- value/type reference: `landscout.stages.enrich_planning_features::_normalize_layer` via `GpuInspectedLayer`
- value/type reference: `landscout.stages.enrich_planning_features::_normalized_catalogs` via `GpuInspectedLayer`
- import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import GpuInspectedLayer, GpuPlanningDocument`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_inspected_layer_payload` via `GpuInspectedLayer`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_features::_inspected` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_enrich_planning_features::_inspected` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_enrich_planning_features::_materialize_layer` via `GpuInspectedLayer`
- constructor call: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_enrich_planning_features::_run` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_enrich_planning_features::_replace_related_layer` via `GpuInspectedLayer`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuInspectedLayer`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_index_planning_regulation::_write_zoning_source` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_index_planning_regulation::_write_zoning_source` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `GpuInspectedLayer`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuInspectedLayer`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_integration_layer` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_layer` via `GpuInspectedLayer`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_multi_geometries_are_accepted` via `GpuInspectedLayer`

**Exact class source**

```python
class GpuInspectedLayer:
    logical_name: LogicalLayerName
    reference: GpuSpatialLayerReference
    data: gpd.GeoDataFrame
    summary: GpuLayerSummary
```

### `GpuSpatialSourceFileIntegrity`

**Source purpose:** One verified physical member of an extracted GPU spatial dataset.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `relative_path` | `str` | `required` | `relative_path: str` |
| `file_type` | `str` | `required` | `file_type: str` |
| `size_bytes` | `int` | `required` | `size_bytes: int` |
| `sha256` | `str` | `required` | `sha256: str` |
| `category` | `str` | `required` | `category: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `GpuSpatialSourceFileIntegrity`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `GpuSpatialSourceFileIntegrity`

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

**Source purpose:** Freshly reloaded GPU layer plus its extraction-inventory evidence.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `logical_name` | `LogicalLayerName` | `required` | `logical_name: LogicalLayerName` |
| `source_layer` | `str` | `required` | `source_layer: str` |
| `driver` | `str` | `required` | `driver: str` |
| `dataset_relative_path` | `str` | `required` | `dataset_relative_path: str` |
| `source_crs` | `str` | `required` | `source_crs: str` |
| `feature_count` | `int` | `required` | `feature_count: int` |
| `files` | `tuple[GpuSpatialSourceFileIntegrity, ...]` | `required` | `files: tuple[GpuSpatialSourceFileIntegrity, ...]` |
| `ogr_fids` | `tuple[int, ...]` | `required` | `ogr_fids: tuple[int, ...]` |
| `data` | `gpd.GeoDataFrame` | `required` | `data: gpd.GeoDataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- constructor call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `GpuValidatedSpatialLayerSource`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `GpuValidatedSpatialLayerSource`
- value/type reference: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_source` via `GpuValidatedSpatialLayerSource`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_sources` via `GpuValidatedSpatialLayerSource`
- value/type reference: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_sources` via `GpuValidatedSpatialLayerSource`
- import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`
- value/type reference: `landscout.stages.enrich_planning_features::_source_feature_ids` via `GpuValidatedSpatialLayerSource`
- value/type reference: `landscout.stages.enrich_planning_features::_normalize_layer` via `GpuValidatedSpatialLayerSource`
- value/type reference: `landscout.stages.enrich_planning_features::_normalized_catalogs` via `GpuValidatedSpatialLayerSource`
- value/type reference: `landscout.stages.enrich_planning_features::_gpu_related_source_files_sha256` via `GpuValidatedSpatialLayerSource`

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

**Source purpose:** Defines `GpuPlanningDocument`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `source_config` | `GpuSourceConfig` | `required` | `source_config: GpuSourceConfig` |
| `source_config_sha256` | `str` | `required` | `source_config_sha256: str` |
| `extraction` | `GpuExtraction` | `required` | `extraction: GpuExtraction` |
| `all_spatial_layers` | `tuple[GpuSpatialLayerReference, ...]` | `required` | `all_spatial_layers: tuple[GpuSpatialLayerReference, ...]` |
| `zoning` | `GpuInspectedLayer` | `required` | `zoning: GpuInspectedLayer` |
| `related_layers` | `tuple[GpuInspectedLayer, ...]` | `required` | `related_layers: tuple[GpuInspectedLayer, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuPlanningDocument`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `GpuPlanningDocument`
- value/type reference: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_source` via `GpuPlanningDocument`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_sources` via `GpuPlanningDocument`
- value/type reference: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_sources` via `GpuPlanningDocument`
- constructor call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuPlanningDocument`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuPlanningDocument`
- value/type reference: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `GpuPlanningDocument`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.sources.gpu_fr import GpuPlanningDocument`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `GpuPlanningDocument`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.sources.gpu_fr import GpuPlanningDocument`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `GpuPlanningDocument`
- import: `landscout.stages.bess_planning_feature_policy::<module>` via `from landscout.sources.gpu_fr import GpuPlanningDocument`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_coded_source` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `GpuPlanningDocument`
- import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`
- value/type reference: `landscout.stages.enrich_planning_features::_standard_model` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_features::_planning_context` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_features::_normalized_catalogs` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_features::_gpu_related_source_files_sha256` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_features::_validate_normalized_planning_feature_inputs` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_features::validate_normalized_planning_feature_inputs` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_features::_validate_result` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_features::intersect_parcels_with_gpu_planning_features` via `GpuPlanningDocument`
- import: `landscout.stages.enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    revalidate_gpu_spatial_layer_sources,
)`
- value/type reference: `landscout.stages.enrich_planning_zoning::_standard_model` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_zoning::_validate_planning_document` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.enrich_planning_zoning::intersect_parcels_with_gpu_zoning` via `GpuPlanningDocument`
- import: `landscout.stages.index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`
- value/type reference: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.index_planning_regulation::_validate_document_lineage` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.index_planning_regulation::_written_file_matches` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.index_planning_regulation::_resolve_regulation_filename` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.index_planning_regulation::_locate_regulation_pdf` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.index_planning_regulation::_index_planning_regulation` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.index_planning_regulation::index_planning_regulation` via `GpuPlanningDocument`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.sources.gpu_fr import GpuPlanningDocument`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `GpuPlanningDocument`
- import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import GpuInspectedLayer, GpuPlanningDocument`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_planning_standard` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_catalog_document_lineage` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_planning_document_context_sha256` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `GpuPlanningDocument`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `GpuPlanningDocument`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_contract_result` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_source_complete_contract` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_two_parcel_source_complete_contract` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_validate_source_complete` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_replace_related_layer` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_without_related_layer` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_refresh_extraction_inventory` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_replace_layer_reference` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_source_complete_contract` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_features::_shapefile_ogr_fid_source_complete_contract` via `GpuPlanningDocument`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_planning_document` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_physical_planning_document` via `GpuPlanningDocument`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_index_planning_regulation::_document` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_index_planning_regulation::_fixture_document` via `GpuPlanningDocument`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- constructor call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_inputs` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::resolve_planning_feature_codes` via `GpuPlanningDocument`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::validate_planning_feature_code_result` via `GpuPlanningDocument`

**Exact class source**

```python
class GpuPlanningDocument:
    source_config: GpuSourceConfig
    source_config_sha256: str
    extraction: GpuExtraction
    all_spatial_layers: tuple[GpuSpatialLayerReference, ...]
    zoning: GpuInspectedLayer
    related_layers: tuple[GpuInspectedLayer, ...]
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `GpuApiConfig._official_api`

**Purpose:** Implements `official api` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _official_api(cls, value: HttpUrl) -> HttpUrl:
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
  - `ValueError("GPU API URL must use the exact official HTTPS /api base")` under lexical guard `parsed.scheme != "https"<br>            or parsed.hostname != "www.geoportail-urbanisme.gouv.fr"<br>            or parsed.port not in {None, 443}<br>            or parsed.username is not None<br>            or parsed.password is not None<br>            or parsed.path.rstrip("/") != "/api"<br>            or parsed.params<br>            or parsed.query<br>            or parsed.fragment`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `urlparse` | `urllib.parse.urlparse` |
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `GpuDownloadConfig._valid_partition_template`

**Purpose:** Implements `valid partition template` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _valid_partition_template(cls, value: str) -> str:
```

- Exact decorators: `field_validator("partition_template")`, `classmethod`.
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
  - `ValueError(<br>                "partition_template must contain exactly one {code_insee} placeholder"<br>            )` under lexical guard `value != value.strip() or value.count("{code_insee}") != 1`.
  - `ValueError("partition_template is malformed")`.
  - `ValueError("partition_template must render one safe path component")` under lexical guard `not rendered or "/" in rendered or "\\" in rendered`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.count` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.format` | `unresolved local/third-party receiver; no ownership inferred` |
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `GpuCacheConfig._strict_finite_number`

**Purpose:** Implements `strict finite number` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _strict_finite_number(cls, value: object) -> object:
```

- Exact decorators: `field_validator("max_age_hours", mode="before")`, `classmethod`.
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
  - `ValueError("max_age_hours must be an exact finite number")` under lexical guard `isinstance(value, bool)<br>            or not isinstance(value, (int, float))<br>            or type(value) not in {int, float}`.
  - `ValueError("max_age_hours must be finite")` under lexical guard `not math.isfinite(value)`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isfinite` | `math.isfinite` |
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
def _strict_finite_number(cls, value: object) -> object:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or type(value) not in {int, float}
        ):
            raise ValueError("max_age_hours must be an exact finite number")
        if not math.isfinite(value):
            raise ValueError("max_age_hours must be finite")
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `GpuLogicalLayerConfig._unique_tokens`

**Purpose:** Implements `unique tokens` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:
```

- Exact decorators: `field_validator("match_tokens")`, `classmethod`.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cls` | positional-or-keyword | `None` | `required` |
| `values` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `values`
- Explicit raise paths:
  - `ValueError("Layer match tokens must contain letters or digits")` under lexical guard `any(not value for value in normalized)`.
  - `ValueError("Layer match tokens must be unique after normalization")` under lexical guard `len(normalized) != len(set(normalized))`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_words` | `landscout.sources.gpu_fr._normalize_words` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(value) for value in values)
        if any(not value for value in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(normalized) != len(set(normalized)):
            raise ValueError("Layer match tokens must be unique after normalization")
        return values
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_normalize_words`

**Purpose:** Implements `normalize words` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _normalize_words(value: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `"_".join(re.findall(r"[a-z0-9]+", ascii_value.casefold()))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::GpuLogicalLayerConfig._unique_tokens` via `_normalize_words`
- value/type reference: `landscout.sources.gpu_fr::GpuLogicalLayerConfig._unique_tokens` via `_normalize_words`
- direct call: `landscout.sources.gpu_fr::_discover_logical_layer` via `_normalize_words`
- value/type reference: `landscout.sources.gpu_fr::_discover_logical_layer` via `_normalize_words`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `unicodedata.normalize` | `unicodedata.normalize` |
| `"".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `unicodedata.combining` | `unicodedata.combining` |
| `"_".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.findall` | `re.findall` |
| `ascii_value.casefold` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _normalize_words(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_value = "".join(
        char for char in decomposed if not unicodedata.combining(char)
    )
    return "_".join(re.findall(r"[a-z0-9]+", ascii_value.casefold()))
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `load_gpu_source_config`

**Purpose:** Load and validate the strict GPU source configuration.

**Exact signature**

```python
def load_gpu_source_config(path: Path = DEFAULT_CONFIG_PATH) -> GpuSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `GpuSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `DEFAULT_CONFIG_PATH` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuSourceConfig.model_validate(payload)`
- Explicit raise paths:
  - `GpuConfigError(f"GPU source configuration does not exist: {path}")` under lexical guard `not path.is_file()`.
  - `TypeError("GPU source configuration must be a mapping")` under lexical guard `type(payload) is not dict`.
  - `GpuConfigError(f"Invalid GPU source configuration: {path}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `load_gpu_source_config`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `load_gpu_source_config`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- direct call: `tests.unit.test_enrich_planning_features::_planning_document` via `load_gpu_source_config`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `load_gpu_source_config`
- import: `tests.unit.test_enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- direct call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `load_gpu_source_config`
- value/type reference: `tests.unit.test_enrich_planning_zoning::_planning_document` via `load_gpu_source_config`
- direct call: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `load_gpu_source_config`
- value/type reference: `tests.unit.test_enrich_planning_zoning::test_one_parcel_fully_inside_one_zone` via `load_gpu_source_config`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::_config` via `load_gpu_source_config`
- value/type reference: `tests.unit.test_gpu_fr::_config` via `load_gpu_source_config`
- direct call: `tests.unit.test_gpu_fr::test_duplicate_gpu_yaml_key_is_rejected` via `load_gpu_source_config`
- value/type reference: `tests.unit.test_gpu_fr::test_duplicate_gpu_yaml_key_is_rejected` via `load_gpu_source_config`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- direct call: `tests.unit.test_index_planning_regulation::_document` via `load_gpu_source_config`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `load_gpu_source_config`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `load_gpu_source_config`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `load_gpu_source_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuConfigError` | `landscout.sources.gpu_fr.GpuConfigError` |
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file`<br>`path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def load_gpu_source_config(path: Path = DEFAULT_CONFIG_PATH) -> GpuSourceConfig:
    """Load and validate the strict GPU source configuration."""

    if not path.is_file():
        raise GpuConfigError(f"GPU source configuration does not exist: {path}")
    try:
        payload = loads_strict_yaml(path.read_bytes())
        if type(payload) is not dict:
            raise TypeError("GPU source configuration must be a mapping")
        return GpuSourceConfig.model_validate(payload)
    except (OSError, TypeError, StrictYamlError, ValidationError) as error:
        raise GpuConfigError(f"Invalid GPU source configuration: {path}") from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validated_source_config`

**Purpose:** Implements `validated source config` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _validated_source_config(config: object) -> GpuSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `GpuSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuSourceConfig.model_validate(config.model_dump(mode="python"))`
- Explicit raise paths:
  - `TypeError("GPU source config type is invalid")` under lexical guard `type(config) is not GpuSourceConfig`.
  - `GpuConfigError(<br>            "GPU source config no longer satisfies the official origin contract"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_source_config_sha256` via `_validated_source_config`
- value/type reference: `landscout.sources.gpu_fr::_source_config_sha256` via `_validated_source_config`
- direct call: `landscout.sources.gpu_fr::build_gpu_partition` via `_validated_source_config`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_partition` via `_validated_source_config`
- direct call: `landscout.sources.gpu_fr::build_gpu_document_list_url` via `_validated_source_config`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_document_list_url` via `_validated_source_config`
- direct call: `landscout.sources.gpu_fr::build_gpu_partition_download_url` via `_validated_source_config`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_partition_download_url` via `_validated_source_config`
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_validated_source_config`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_validated_source_config`
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `_validated_source_config`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `_validated_source_config`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_validated_source_config`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_validated_source_config`
- direct call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_validated_source_config`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_validated_source_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuConfigError` | `landscout.sources.gpu_fr.GpuConfigError` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_source_config_sha256`

**Purpose:** Return the private canonical identity of one validated GPU config.

**Exact signature**

```python
def _source_config_sha256(config: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(payload).hexdigest()`
- Explicit raise paths:
  - `GpuConfigError("GPU source config cannot be serialized safely")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_source_config_sha256`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_source_config_sha256`
- direct call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_source_config_sha256`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_source_config_sha256`
- direct call: `tests.unit.test_enrich_planning_features::_planning_document` via `gpu_source_module._source_config_sha256`
- direct call: `tests.unit.test_enrich_planning_zoning::_planning_document` via `gpu_source_module._source_config_sha256`
- direct call: `tests.unit.test_gpu_fr::test_gpu_source_config_identity_is_deterministic_and_content_bound` via `gpu._source_config_sha256`
- direct call: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `gpu._source_config_sha256`
- direct call: `tests.unit.test_index_planning_regulation::_document` via `gpu_source_module._source_config_sha256`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `gpu_source_module._source_config_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.gpu_fr._validated_source_config` |
| `json.dumps(<br>            {<br>                "domain": "landscout.gpu.source_config",<br>                "config": validated.model_dump(mode="json"),<br>            },<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `validated.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuConfigError` | `landscout.sources.gpu_fr.GpuConfigError` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _source_config_sha256(config: object) -> str:
    """Return the private canonical identity of one validated GPU config."""

    validated = _validated_source_config(config)
    try:
        payload = json.dumps(
            {
                "domain": "landscout.gpu.source_config",
                "config": validated.model_dump(mode="json"),
            },
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise GpuConfigError("GPU source config cannot be serialized safely") from error
    return sha256(payload).hexdigest()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `build_gpu_partition`

**Purpose:** Implements `build gpu partition` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def build_gpu_partition(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |
| `commune_code` | positional-or-keyword | `str \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `validated_config.download.partition_template.format(code_insee=code)`
- Explicit raise paths:
  - `GpuConfigError("GPU commune code must contain exactly five digits")` under lexical guard `not isinstance(code, str) or re.fullmatch(r"[0-9]{5}", code) is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `landscout.sources.gpu_fr::build_gpu_document_list_url` via `build_gpu_partition`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_document_list_url` via `build_gpu_partition`
- direct call: `landscout.sources.gpu_fr::build_gpu_partition_download_url` via `build_gpu_partition`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_partition_download_url` via `build_gpu_partition`
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `build_gpu_partition`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `build_gpu_partition`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `build_gpu_partition`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `build_gpu_partition`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `build_gpu_partition`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `build_gpu_partition`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::test_valid_config_and_urls` via `build_gpu_partition`
- value/type reference: `tests.unit.test_gpu_fr::test_valid_config_and_urls` via `build_gpu_partition`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.gpu_fr._validated_source_config` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.fullmatch` | `re.fullmatch` |
| `GpuConfigError` | `landscout.sources.gpu_fr.GpuConfigError` |
| `validated_config.download.partition_template.format` | `unresolved local/third-party receiver; no ownership inferred` |

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
def build_gpu_partition(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
    validated_config = _validated_source_config(config)
    code = commune_code or validated_config.pilot.commune_code
    if not isinstance(code, str) or re.fullmatch(r"[0-9]{5}", code) is None:
        raise GpuConfigError("GPU commune code must contain exactly five digits")
    return validated_config.download.partition_template.format(code_insee=code)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_api_url`

**Purpose:** Implements `api url` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _api_url(config: GpuSourceConfig, path: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |
| `path` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `urljoin(f"{str(config.api.base_url).rstrip('/')}/", path.lstrip("/"))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::build_gpu_document_list_url` via `_api_url`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_document_list_url` via `_api_url`
- direct call: `landscout.sources.gpu_fr::build_gpu_partition_download_url` via `_api_url`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_partition_download_url` via `_api_url`
- direct call: `landscout.sources.gpu_fr::_written_files` via `_api_url`
- value/type reference: `landscout.sources.gpu_fr::_written_files` via `_api_url`
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_api_url`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_api_url`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `_api_url`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `_api_url`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `urljoin` | `urllib.parse.urljoin` |
| `str(config.api.base_url).rstrip` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.lstrip` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _api_url(config: GpuSourceConfig, path: str) -> str:
    return urljoin(f"{str(config.api.base_url).rstrip('/')}/", path.lstrip("/"))
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `build_gpu_document_list_url`

**Purpose:** Implements `build gpu document list url` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def build_gpu_document_list_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |
| `commune_code` | positional-or-keyword | `str \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `f"{_api_url(validated_config, 'document')}?{query}"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `build_gpu_document_list_url`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `build_gpu_document_list_url`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::test_valid_config_and_urls` via `build_gpu_document_list_url`
- value/type reference: `tests.unit.test_gpu_fr::test_valid_config_and_urls` via `build_gpu_document_list_url`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.gpu_fr._validated_source_config` |
| `urlencode` | `urllib.parse.urlencode` |
| `build_gpu_partition` | `landscout.sources.gpu_fr.build_gpu_partition` |
| `_api_url` | `landscout.sources.gpu_fr._api_url` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `build_gpu_partition_download_url`

**Purpose:** Implements `build gpu partition download url` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def build_gpu_partition_download_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |
| `commune_code` | positional-or-keyword | `str \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_api_url(validated_config, f"document/download-by-partition/{partition}")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `build_gpu_partition_download_url`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `build_gpu_partition_download_url`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `build_gpu_partition_download_url`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `build_gpu_partition_download_url`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `build_gpu_partition_download_url`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `build_gpu_partition_download_url`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::test_valid_config_and_urls` via `build_gpu_partition_download_url`
- value/type reference: `tests.unit.test_gpu_fr::test_valid_config_and_urls` via `build_gpu_partition_download_url`
- direct call: `tests.unit.test_gpu_fr::_extraction_from_archive` via `build_gpu_partition_download_url`
- value/type reference: `tests.unit.test_gpu_fr::_extraction_from_archive` via `build_gpu_partition_download_url`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.gpu_fr._validated_source_config` |
| `quote` | `urllib.parse.quote` |
| `build_gpu_partition` | `landscout.sources.gpu_fr.build_gpu_partition` |
| `_api_url` | `landscout.sources.gpu_fr._api_url` |

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
def build_gpu_partition_download_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
    validated_config = _validated_source_config(config)
    partition = quote(build_gpu_partition(validated_config, commune_code), safe="")
    return _api_url(validated_config, f"document/download-by-partition/{partition}")
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_request_json`

**Purpose:** Implements `request json` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _request_json(url: str, timeout: float) -> Any:
```

- Exact decorators: none.
- Declared return annotation: `Any`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `url` | positional-or-keyword | `str` | `required` |
| `timeout` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `loads_strict_json(response.read())`
- Explicit raise paths:
  - `GpuDiscoveryError(f"GPU metadata request failed: {url}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_request_json`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_request_json`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `loads_strict_json` | `landscout.common.strict_json.loads_strict_json` |
| `response.read` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuDiscoveryError` | `landscout.sources.gpu_fr.GpuDiscoveryError` |

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
def _request_json(url: str, timeout: float) -> Any:
    try:
        with open_safe_https(
            url,
            timeout=timeout,
            headers={"Accept": "application/json", "User-Agent": USER_AGENT},
        ) as response:
            return loads_strict_json(response.read())
    except (HTTPError, URLError, OSError, StrictJsonError) as error:
        raise GpuDiscoveryError(f"GPU metadata request failed: {url}") from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_required_string`

**Purpose:** Implements `required string` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _required_string(payload: dict[str, Any], key: str, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `payload` | positional-or-keyword | `dict[str, Any]` | `required` |
| `key` | positional-or-keyword | `str` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `GpuDiscoveryError(f"GPU {label} is missing or invalid")` under lexical guard `not isinstance(value, str) or not value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_written_files` via `_required_string`
- value/type reference: `landscout.sources.gpu_fr::_written_files` via `_required_string`
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_required_string`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_required_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `payload.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuDiscoveryError` | `landscout.sources.gpu_fr.GpuDiscoveryError` |

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
def _required_string(payload: dict[str, Any], key: str, label: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise GpuDiscoveryError(f"GPU {label} is missing or invalid")
    return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_optional_string`

**Purpose:** Implements `optional string` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _optional_string(payload: dict[str, Any], *keys: str) -> str | None:
```

- Exact decorators: none.
- Declared return annotation: `str | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `payload` | positional-or-keyword | `dict[str, Any]` | `required` |
| `*keys` | variadic positional | `str` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `text`
  - `None`
- Explicit raise paths:
  - `GpuDiscoveryError(f"GPU metadata field {key} has an invalid value")` under lexical guard `not isinstance(value, (str, int, float)) or isinstance(value, bool)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_written_files` via `_optional_string`
- value/type reference: `landscout.sources.gpu_fr::_written_files` via `_optional_string`
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_optional_string`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_optional_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `payload.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuDiscoveryError` | `landscout.sources.gpu_fr.GpuDiscoveryError` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `text.strip` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_written_files`

**Purpose:** Implements `written files` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _written_files(
    details: dict[str, Any],
    payload: Any,
    document_id: str,
    config: GpuSourceConfig,
) -> tuple[GpuWrittenFile, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuWrittenFile, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `details` | positional-or-keyword | `dict[str, Any]` | `required` |
| `payload` | positional-or-keyword | `Any` | `required` |
| `document_id` | positional-or-keyword | `str` | `required` |
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(sorted(result, key=lambda item: item.filename.casefold()))`
- Explicit raise paths:
  - `GpuDiscoveryError("GPU written-file metadata is not a list")` under lexical guard `not isinstance(payload, list)`.
  - `GpuDiscoveryError("GPU written-file entry is invalid")` under lexical guard `not isinstance(item, dict)`.
  - `GpuDiscoveryError(f"Duplicate GPU written filename: {filename}")` under lexical guard `filename in seen`.
  - `GpuDiscoveryError(<br>                "GPU written material URL is not the exact official HTTPS API URL"<br>            )` under lexical guard `source_url is not None and source_url != expected_source_url`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_written_files`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_written_files`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuDiscoveryError` | `landscout.sources.gpu_fr.GpuDiscoveryError` |
| `details.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_required_string` | `landscout.sources.gpu_fr._required_string` |
| `seen.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `_api_url` | `landscout.sources.gpu_fr._api_url` |
| `quote` | `urllib.parse.quote` |
| `material_urls.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuWrittenFile` | `landscout.sources.gpu_fr.GpuWrittenFile` |
| `_optional_string` | `landscout.sources.gpu_fr._optional_string` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `seen.add(filename)`<br>`result.append(<br>            GpuWrittenFile(<br>                filename=filename,<br>                title=_optional_string(item, "title"),<br>                document_path=_optional_string(item, "path"),<br>                source_url=expected_source_url,<br>            )<br>        )` |
| Direct parameter mutation | None directly present. |

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
            f"document/{quote(document_id, safe='')}/files/{quote(filename, safe='')}",
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `discover_current_gpu_document`

**Purpose:** Resolve exactly one official production, approved and in-force DU.

**Exact signature**

```python
def discover_current_gpu_document(
    config: GpuSourceConfig, commune_code: str | None = None, timeout: float = 60.0
) -> GpuDocumentMetadata:
```

- Exact decorators: none.
- Declared return annotation: `GpuDocumentMetadata`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |
| `commune_code` | positional-or-keyword | `str \| None` | `None` |
| `timeout` | positional-or-keyword | `float` | `60.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuDocumentMetadata(<br>        provider=validated_config.provider,<br>        portal=validated_config.portal,<br>        commune_code=code,<br>        partition=partition,<br>        document_id=document_id,<br>        document_family="DU",<br>        document_type=document_type,<br>        document_title=_optional_string(details, "title"),<br>        status=_required_string(details, "status", "status"),<br>        legal_status=_required_string(details, "legalStatus", "legal status"),<br>        effective_status=_required_string(<br>            details, "effectiveStatus", "effective status"<br>        ),<br>        version=_optional_string(details, "version"),<br>        archive_name=archive_name,<br>        publication_timestamp=_optional_string(details, "publicationDate"),<br>        update_timestamp=_optional_string(details, "updateDate"),<br>        revision_date=_optional_string(details, "revisionDate", "referenceDate"),<br>        producer=_optional_string(details, "producer"),<br>        standard_model=_optional_string(details, "standard", "model", "documentModel"),<br>        projection=_optional_string(details, "projectionCode"),<br>        metadata_identifier=_optional_string(details, "metadata", "fileIdentifier"),<br>        source_url=source_url,<br>        written_files=_written_files(<br>            details,<br>            files_payload,<br>            document_id,<br>            validated_config,<br>        ),<br>    )`
- Explicit raise paths:
  - `GpuDiscoveryError("GPU source config is invalid")`.
  - `GpuDiscoveryError("GPU document listing is not a list")` under lexical guard `not isinstance(listing, list)`.
  - `GpuDiscoveryError(<br>            f"No current approved and in-force GPU document for {partition}"<br>        )` under lexical guard `not current`.
  - `GpuDiscoveryError(<br>            f"Ambiguous current GPU document selection for {partition}: {len(current)}"<br>        )` under lexical guard `len(current) != 1`.
  - `GpuDiscoveryError("GPU archive name is unsafe")`.
  - `GpuDiscoveryError("GPU document details are not an object")` under lexical guard `not isinstance(details_payload, dict)`.
  - `GpuDiscoveryError(<br>            "GPU document details do not match the selected document"<br>        )` under lexical guard `details.get("id") != document_id or details.get("originalName") != archive_name`.
  - `GpuDiscoveryError(<br>            "GPU document details no longer describe a current approved and "<br>            "in-force document"<br>        )` under lexical guard `any(details.get(key) != value for key, value in expected_state.items())`.
  - `GpuDiscoveryError("GPU document details do not match the commune")` under lexical guard `not isinstance(detail_grid, dict) or detail_grid.get("name") != code`.
  - `GpuDiscoveryError("GPU document details do not match the partition")` under lexical guard `details.get("name") != partition`.
  - `GpuDiscoveryError(<br>            "GPU document archive URL is not the exact official HTTPS API URL"<br>        )` under lexical guard `details.get("archiveUrl") != expected_details_archive_url`.
  - `GpuDiscoveryError("GPU document type changed between listing and details")` under lexical guard `listing_type != document_type`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `discover_current_gpu_document`
- value/type reference: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `discover_current_gpu_document`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::_document` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::_document` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_gpu_api_json_is_strict_before_document_selection` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_api_json_is_strict_before_document_selection` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_url_must_be_exact_official_https_api_url` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_written_material_fallback_rejects_unsafe_archive_url_provenance` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_no_current_document_is_rejected` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_no_current_document_is_rejected` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_ambiguous_current_documents_are_rejected` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_current_documents_are_rejected` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_missing_document_identity_is_rejected` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_document_identity_is_rejected` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_must_match_selected_listing` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_document_details_commune_must_match_selected_listing` via `discover_current_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `discover_current_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_discovery_rejects_unsafe_archive_name` via `discover_current_gpu_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.gpu_fr._validated_source_config` |
| `GpuDiscoveryError` | `landscout.sources.gpu_fr.GpuDiscoveryError` |
| `build_gpu_partition` | `landscout.sources.gpu_fr.build_gpu_partition` |
| `_request_json` | `landscout.sources.gpu_fr._request_json` |
| `build_gpu_document_list_url` | `landscout.sources.gpu_fr.build_gpu_document_list_url` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `item.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `grid.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `current.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_required_string` | `landscout.sources.gpu_fr._required_string` |
| `_safe_gpu_archive_filename` | `landscout.sources.gpu_fr._safe_gpu_archive_filename` |
| `_api_url` | `landscout.sources.gpu_fr._api_url` |
| `quote` | `urllib.parse.quote` |
| `details.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_state.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `detail_grid.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `build_gpu_partition_download_url` | `landscout.sources.gpu_fr.build_gpu_partition_download_url` |
| `GpuDocumentMetadata` | `landscout.sources.gpu_fr.GpuDocumentMetadata` |
| `_optional_string` | `landscout.sources.gpu_fr._optional_string` |
| `_written_files` | `landscout.sources.gpu_fr._written_files` |

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
| In-memory mutation | `current.append(item)` |
| Direct parameter mutation | None directly present. |

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
        raise GpuDiscoveryError(
            "GPU document details do not match the selected document"
        )
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
        effective_status=_required_string(
            details, "effectiveStatus", "effective status"
        ),
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_safe_gpu_archive_filename`

**Purpose:** Implements `safe gpu archive filename` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _safe_gpu_archive_filename(archive_name: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_name` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `filename`
- Explicit raise paths:
  - `GpuDownloadError("GPU archive name must be a string")` under lexical guard `not isinstance(archive_name, str)`.
  - `GpuDownloadError("GPU archive name is empty or has edge whitespace")` under lexical guard `not archive_name or archive_name != archive_name.strip()`.
  - `GpuDownloadError("GPU archive name contains control characters")` under lexical guard `any(ord(character) < 32 or ord(character) == 127 for character in archive_name)`.
  - `GpuDownloadError("GPU archive name is not a safe local basename")` under lexical guard `normalized in {".", ".."}<br>        or "/" in normalized<br>        or "\\" in normalized<br>        or PurePosixPath(normalized).is_absolute()<br>        or PureWindowsPath(normalized).is_absolute()<br>        or bool(PureWindowsPath(normalized).drive)<br>        or normalized.endswith((" ", "."))<br>        or any(character in '<>:"/\\\|?*' for character in normalized)`.
  - `GpuDownloadError("GPU archive name contains repeated .zip suffixes")` under lexical guard `normalized.casefold().endswith(".zip")`.
  - `GpuDownloadError("GPU archive name has no safe logical basename")` under lexical guard `not basename<br>        or normalized_basename in {".", ".."}<br>        or normalized_basename.endswith((" ", "."))`.
  - `GpuDownloadError("GPU archive name is reserved on Windows")` under lexical guard `windows_stem in _WINDOWS_RESERVED_BASENAMES`.
  - `GpuDownloadError("GPU archive filename exceeds Windows component limits")` under lexical guard `len(unicodedata.normalize("NFKC", filename).encode("utf-16-le")) // 2 > 255`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_safe_gpu_archive_filename`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `_safe_gpu_archive_filename`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `_safe_gpu_archive_filename`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `_safe_gpu_archive_filename`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `_safe_gpu_archive_filename`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `_safe_gpu_archive_filename`
- direct call: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `gpu._safe_gpu_archive_filename`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuDownloadError` | `landscout.sources.gpu_fr.GpuDownloadError` |
| `archive_name.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ord` | `unresolved local/third-party receiver; no ownership inferred` |
| `unicodedata.normalize` | `unicodedata.normalize` |
| `PurePosixPath(normalized).is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `PureWindowsPath(normalized).is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `PureWindowsPath` | `pathlib.PureWindowsPath` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.casefold().endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_basename.casefold().endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_basename.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_basename.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_basename.split(".", 1)[0].casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_basename.split` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `unicodedata.normalize("NFKC", filename).encode` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_gpu_document_for_config`

**Purpose:** Implements `validate gpu document for config` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _validate_gpu_document_for_config(
    document: GpuDocumentMetadata, config: GpuSourceConfig
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `document` | positional-or-keyword | `GpuDocumentMetadata` | `required` |
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_safe_gpu_archive_filename(document.archive_name)`
- Explicit raise paths:
  - `GpuDownloadError("GPU document metadata object is invalid")` under lexical guard `type(document) is not GpuDocumentMetadata`.
  - `GpuDownloadError(<br>            "GPU document provider/portal does not match configuration"<br>        )` under lexical guard `document.provider != config.provider or document.portal != config.portal`.
  - `GpuDownloadError("GPU document ID is invalid")` under lexical guard `type(document.document_id) is not str<br>        or not document.document_id<br>        or document.document_id != document.document_id.strip()<br>        or any(<br>            ord(character) < 32 or ord(character) == 127<br>            for character in document.document_id<br>        )`.
  - `GpuDownloadError("GPU document written-file provenance is invalid")` under lexical guard `type(document.written_files) is not tuple`.
  - `GpuDownloadError("GPU document written-file type is invalid")` under lexical guard `type(written_file) is not GpuWrittenFile`.
  - `GpuDownloadError("GPU document written filename is invalid")` under lexical guard `type(filename) is not str<br>            or not filename<br>            or filename != filename.strip()<br>            or any(<br>                ord(character) < 32 or ord(character) == 127 for character in filename<br>            )<br>            or filename in written_filenames`.
  - `GpuDownloadError(<br>                "GPU document written source URL is not the exact official API URL"<br>            )` under lexical guard `written_file.source_url != expected_written_url`.
  - `GpuDownloadError("GPU document commune code is invalid")` under lexical guard `not isinstance(code, str) or re.fullmatch(r"[0-9]{5}", code) is None`.
  - `GpuDownloadError("GPU document commune does not match configured pilot")` under lexical guard `code != config.pilot.commune_code`.
  - `GpuDownloadError("GPU document commune/partition is invalid")`.
  - `GpuDownloadError("GPU document partition does not match configuration")` under lexical guard `document.partition != expected_partition`.
  - `GpuDownloadError("GPU document family is not a planning document")` under lexical guard `document.document_family != "DU" or (<br>        type(document.document_type) is not str<br>        or not document.document_type<br>        or document.document_type != document.document_type.strip()<br>        or any(<br>            ord(character) < 32 or ord(character) == 127<br>            for character in document.document_type<br>        )<br>    )`.
  - `GpuDownloadError("GPU document is not current, approved, and in force")` under lexical guard `document.status != "document.production"<br>        or document.legal_status != "APPROVED"<br>        or document.effective_status != "EN_VIGUEUR"`.
  - `GpuDownloadError(<br>            "GPU document source URL is not the official partition URL"<br>        )` under lexical guard `not isinstance(document.source_url, str) or document.source_url != expected_url`.
  - `GpuDownloadError("GPU document source URL has an unsafe identity")` under lexical guard `parsed.scheme != "https"<br>        or parsed.hostname != "www.geoportail-urbanisme.gouv.fr"<br>        or parsed.path != expected_parsed.path<br>        or parsed.params<br>        or parsed.query<br>        or parsed.fragment<br>        or parsed.username is not None<br>        or parsed.password is not None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `_validate_gpu_document_for_config`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `_validate_gpu_document_for_config`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_validate_gpu_document_for_config`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_validate_gpu_document_for_config`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_validate_gpu_document_for_config`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_validate_gpu_document_for_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuDownloadError` | `landscout.sources.gpu_fr.GpuDownloadError` |
| `document.document_id.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ord` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `filename.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `written_filenames.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `_api_url` | `landscout.sources.gpu_fr._api_url` |
| `quote` | `urllib.parse.quote` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.fullmatch` | `re.fullmatch` |
| `build_gpu_partition` | `landscout.sources.gpu_fr.build_gpu_partition` |
| `build_gpu_partition_download_url` | `landscout.sources.gpu_fr.build_gpu_partition_download_url` |
| `document.document_type.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `urlparse` | `urllib.parse.urlparse` |
| `_safe_gpu_archive_filename` | `landscout.sources.gpu_fr._safe_gpu_archive_filename` |

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
| In-memory mutation | `written_filenames.add(filename)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_gpu_document_for_config(
    document: GpuDocumentMetadata, config: GpuSourceConfig
) -> str:
    if type(document) is not GpuDocumentMetadata:
        raise GpuDownloadError("GPU document metadata object is invalid")
    if document.provider != config.provider or document.portal != config.portal:
        raise GpuDownloadError(
            "GPU document provider/portal does not match configuration"
        )
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
                ord(character) < 32 or ord(character) == 127 for character in filename
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
    if document.document_family != "DU" or (
        type(document.document_type) is not str
        or not document.document_type
        or document.document_type != document.document_type.strip()
        or any(
            ord(character) < 32 or ord(character) == 127
            for character in document.document_type
        )
    ):
        raise GpuDownloadError("GPU document family is not a planning document")
    if (
        document.status != "document.production"
        or document.legal_status != "APPROVED"
        or document.effective_status != "EN_VIGUEUR"
    ):
        raise GpuDownloadError("GPU document is not current, approved, and in force")
    if not isinstance(document.source_url, str) or document.source_url != expected_url:
        raise GpuDownloadError(
            "GPU document source URL is not the official partition URL"
        )
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_sha256`

**Purpose:** Implements `sha256` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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
- direct call: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `_sha256`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `_sha256`
- direct call: `landscout.sources.gpu_fr::_load_cached_archive` via `_sha256`
- value/type reference: `landscout.sources.gpu_fr::_load_cached_archive` via `_sha256`
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `_sha256`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `_sha256`
- direct call: `landscout.sources.gpu_fr::_inventory` via `_sha256`
- value/type reference: `landscout.sources.gpu_fr::_inventory` via `_sha256`
- direct call: `landscout.sources.gpu_fr::_spatial_source_family` via `_sha256`
- value/type reference: `landscout.sources.gpu_fr::_spatial_source_family` via `_sha256`
- direct call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_sha256`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_sha256`
- direct call: `tests.unit.test_gpu_fr::_extraction_from_archive` via `gpu._sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sha256` | `hashlib.sha256` |
| `path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `stream.read` | `unresolved local/third-party receiver; no ownership inferred` |
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
        while chunk := stream.read(DOWNLOAD_CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_is_link_or_junction`

**Purpose:** Implements `is link or junction` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_require_no_cache_recovery_material` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_require_no_cache_recovery_material` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_prepare_temporary_cache_file` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_prepare_temporary_cache_file` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_inventory` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_inventory` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_require_no_extraction_recovery_material` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_require_no_extraction_recovery_material` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_prepare_temporary_extraction_directory` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_prepare_temporary_extraction_directory` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_publish_extraction_directory` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_publish_extraction_directory` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_validated_spatial_root` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_validated_spatial_root` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_contained_spatial_path` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_contained_spatial_path` via `_is_link_or_junction`
- direct call: `landscout.sources.gpu_fr::_spatial_dataset_relative_path` via `_is_link_or_junction`
- value/type reference: `landscout.sources.gpu_fr::_spatial_dataset_relative_path` via `_is_link_or_junction`

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
    return path.is_symlink() or path.is_junction()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_gpu_archive_download`

**Purpose:** Implements `validate gpu archive download` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _validate_gpu_archive_download(
    download: GpuArchiveDownload,
) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `GpuArchiveDownload` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `validate_gpu_archive(path)`
- Explicit raise paths:
  - `GpuArchiveError("GPU archive download object is invalid")` under lexical guard `type(download) is not GpuArchiveDownload`.
  - `GpuArchiveError("GPU archive document lineage object is invalid")` under lexical guard `type(download.document) is not GpuDocumentMetadata`.
  - `GpuArchiveError("GPU archive path is not a regular local file")` under lexical guard `not isinstance(path, Path) or _is_link_or_junction(path) or not path.is_file()`.
  - `GpuArchiveError("GPU archive object does not declare ZIP format")` under lexical guard `download.archive_format != "zip"`.
  - `GpuArchiveError("GPU archive filename does not match its path")` under lexical guard `not isinstance(download.filename, str) or download.filename != path.name`.
  - `GpuArchiveError("GPU archive object has an invalid file size")` under lexical guard `type(download.file_size) is not int or download.file_size <= 0`.
  - `GpuArchiveError("GPU archive object has an invalid SHA256")` under lexical guard `not isinstance(download.sha256, str)<br>        or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None`.
  - `GpuArchiveError("GPU archive document identity is invalid")`.
  - `GpuArchiveError("GPU archive filename does not match document lineage")` under lexical guard `download.filename != expected_filename`.
  - `GpuArchiveError("Cannot read GPU archive bytes")`.
  - `GpuArchiveError(<br>            "GPU archive size does not match immutable download lineage"<br>        )` under lexical guard `actual_size != download.file_size`.
  - `GpuArchiveError(<br>            "GPU archive SHA256 does not match immutable download lineage"<br>        )` under lexical guard `actual_sha256 != download.sha256`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_validate_gpu_archive_download`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_validate_gpu_archive_download`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_validate_gpu_archive_download`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_validate_gpu_archive_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.fullmatch` | `re.fullmatch` |
| `_safe_gpu_archive_filename` | `landscout.sources.gpu_fr._safe_gpu_archive_filename` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `landscout.sources.gpu_fr._sha256` |
| `validate_gpu_archive` | `landscout.sources.gpu_fr.validate_gpu_archive` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file`<br>`path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_gpu_archive_download(
    download: GpuArchiveDownload,
) -> tuple[str, ...]:
    if type(download) is not GpuArchiveDownload:
        raise GpuArchiveError("GPU archive download object is invalid")
    if type(download.document) is not GpuDocumentMetadata:
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_safe_archive_member`

**Purpose:** Implements `safe archive member` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _safe_archive_member(name: str) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `False`
  - `not (<br>        posix.is_absolute()<br>        or windows.is_absolute()<br>        or windows.drive<br>        or any(part == ".." for part in posix.parts)<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_validated_zip_destinations` via `_safe_archive_member`
- value/type reference: `landscout.sources.gpu_fr::_validated_zip_destinations` via `_safe_archive_member`
- direct call: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `_safe_archive_member`
- value/type reference: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `_safe_archive_member`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `name.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `PureWindowsPath` | `pathlib.PureWindowsPath` |
| `posix.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `windows.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_windows_member_component`

**Purpose:** Implements `windows member component` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _windows_member_component(component: str) -> str:
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
  - `GpuArchiveError(f"Unsafe Windows-compatible ZIP component: {component}")` under lexical guard `not normalized<br>        or normalized in {".", ".."}<br>        or normalized.endswith((" ", "."))<br>        or any(ord(character) < 32 or ord(character) == 127 for character in normalized)<br>        or any(character in '<>:"/\\\|?*' for character in normalized)`.
  - `GpuArchiveError(f"Reserved Windows ZIP component: {component}")` under lexical guard `stem in _WINDOWS_RESERVED_BASENAMES`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_validated_zip_destinations` via `_windows_member_component`
- value/type reference: `landscout.sources.gpu_fr::_validated_zip_destinations` via `_windows_member_component`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `unicodedata.normalize` | `unicodedata.normalize` |
| `normalized.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ord` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validated_zip_destinations`

**Purpose:** Implements `validated zip destinations` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _validated_zip_destinations(
    members: list[zipfile.ZipInfo],
) -> tuple[tuple[zipfile.ZipInfo, PurePosixPath], ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[zipfile.ZipInfo, PurePosixPath], ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `members` | positional-or-keyword | `list[zipfile.ZipInfo]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(result)`
- Explicit raise paths:
  - `GpuArchiveError(f"Duplicate member name in GPU ZIP: {raw_name}")` under lexical guard `raw_name in raw_names`.
  - `GpuArchiveError(f"Unsafe path in GPU archive: {raw_name}")` under lexical guard `not _safe_archive_member(raw_name)`.
  - `GpuArchiveError(<br>                f"Symbolic links are not allowed in GPU archive: {raw_name}"<br>            )` under lexical guard `stat.S_ISLNK(mode)`.
  - `GpuArchiveError(<br>                f"Special files are not allowed in GPU archive: {raw_name}"<br>            )` under lexical guard `member.create_system == 3 and file_type not in {<br>            0,<br>            stat.S_IFREG,<br>            stat.S_IFDIR,<br>        }`.
  - `GpuArchiveError(<br>                f"GPU ZIP member has no extraction target: {raw_name}"<br>            )` under lexical guard `not parts`.
  - `GpuArchiveError("GPU ZIP member collides with extraction manifest")` under lexical guard `canonical[0] == EXTRACTION_MANIFEST_NAME.casefold()`.
  - `GpuArchiveError(<br>                "GPU ZIP members collide at one Windows-compatible destination: "<br>                f"{previous} / {raw_name}"<br>            )` under lexical guard `canonical in explicit_destinations`.
  - `GpuArchiveError(<br>                f"GPU ZIP file/directory destination collision: {raw_name}"<br>            )` under lexical guard `any(parent in file_destinations for parent in parents)`.
  - `GpuArchiveError(<br>                    f"GPU ZIP file/directory destination collision: {raw_name}"<br>                )` under lexical guard `is_directory`.
  - `GpuArchiveError(<br>                    f"GPU ZIP file/directory destination collision: {raw_name}"<br>                )` under lexical guard `is_directory`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::validate_gpu_archive` via `_validated_zip_destinations`
- value/type reference: `landscout.sources.gpu_fr::validate_gpu_archive` via `_validated_zip_destinations`
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_validated_zip_destinations`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_validated_zip_destinations`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `raw_names.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `_safe_archive_member` | `landscout.sources.gpu_fr._safe_archive_member` |
| `stat.S_ISLNK` | `stat.S_ISLNK` |
| `stat.S_IFMT` | `stat.S_IFMT` |
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `raw_name.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_windows_member_component` | `landscout.sources.gpu_fr._windows_member_component` |
| `EXTRACTION_MANIFEST_NAME.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `member.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_name.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `directory_destinations.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `file_destinations.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `directory_destinations.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.append` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `member.is_dir` |
| Filesystem/archive write or publication | `raw_name.replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `raw_names.add(raw_name)`<br>`explicit_destinations[canonical] = raw_name`<br>`directory_destinations.add(canonical)`<br>`file_destinations.add(canonical)`<br>`directory_destinations.update(parents)`<br>`result.append((member, PurePosixPath(*parts)))` |
| Direct parameter mutation | None directly present. |

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
            raise GpuArchiveError(
                f"Special files are not allowed in GPU archive: {raw_name}"
            )

        destination = PurePosixPath(raw_name.replace("\\", "/"))
        parts = tuple(part for part in destination.parts if part not in {"", "."})
        if not parts:
            raise GpuArchiveError(
                f"GPU ZIP member has no extraction target: {raw_name}"
            )
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `validate_gpu_archive`

**Purpose:** Fully validate a ZIP archive and return its deterministic member inventory.

**Exact signature**

```python
def validate_gpu_archive(path: Path) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(<br>        sorted(<br>            (destination.as_posix() for _, destination in destinations),<br>            key=str.casefold,<br>        )<br>    )`
- Explicit raise paths:
  - `GpuArchiveError(f"GPU archive is missing or empty: {path}")` under lexical guard `not path.is_file() or path.stat().st_size <= 0`.
  - `GpuArchiveError(f"GPU archive is not a readable ZIP: {path}")` under lexical guard `not zipfile.is_zipfile(path)`.
  - `GpuArchiveError("GPU ZIP contains no members")` under lexical guard `not members`.
  - `GpuArchiveError(f"Corrupt GPU ZIP member: {bad_member}")` under lexical guard `bad_member is not None`.
  - `re-raise`.
  - `GpuArchiveError(f"Cannot validate GPU ZIP archive: {path}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `validate_gpu_archive`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_archive_download` via `validate_gpu_archive`
- direct call: `landscout.sources.gpu_fr::_load_cached_archive` via `validate_gpu_archive`
- value/type reference: `landscout.sources.gpu_fr::_load_cached_archive` via `validate_gpu_archive`
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `validate_gpu_archive`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `validate_gpu_archive`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::test_archive_path_traversal_is_rejected` via `validate_gpu_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_archive_path_traversal_is_rejected` via `validate_gpu_archive`
- direct call: `tests.unit.test_gpu_fr::test_archive_symlink_is_rejected` via `validate_gpu_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_archive_symlink_is_rejected` via `validate_gpu_archive`
- direct call: `tests.unit.test_gpu_fr::test_duplicate_zip_extraction_targets_are_rejected` via `validate_gpu_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_duplicate_zip_extraction_targets_are_rejected` via `validate_gpu_archive`
- direct call: `tests.unit.test_gpu_fr::test_zip_file_directory_target_collision_is_rejected` via `validate_gpu_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_zip_file_directory_target_collision_is_rejected` via `validate_gpu_archive`
- direct call: `tests.unit.test_gpu_fr::test_zip_cannot_claim_extraction_manifest_path` via `validate_gpu_archive`
- value/type reference: `tests.unit.test_gpu_fr::test_zip_cannot_claim_extraction_manifest_path` via `validate_gpu_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `zipfile.is_zipfile` | `zipfile.is_zipfile` |
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `archive.infolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_zip_destinations` | `landscout.sources.gpu_fr._validated_zip_destinations` |
| `archive.testzip` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `destination.as_posix` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file`<br>`path.stat`<br>`zipfile.is_zipfile`<br>`zipfile.ZipFile` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
        sorted(
            (destination.as_posix() for _, destination in destinations),
            key=str.casefold,
        )
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_document_identity`

**Purpose:** Implements `document identity` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _document_identity(document: GpuDocumentMetadata) -> dict[str, Any]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, Any]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `document` | positional-or-keyword | `GpuDocumentMetadata` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `_document_identity`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `_document_identity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `asdict` | `dataclasses.asdict` |

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
| In-memory mutation | `result["written_files"] = [asdict(item) for item in document.written_files]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _document_identity(document: GpuDocumentMetadata) -> dict[str, Any]:
    result = asdict(document)
    result["written_files"] = [asdict(item) for item in document.written_files]
    return result
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_document_from_dict`

**Purpose:** Implements `document from dict` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _document_from_dict(payload: Any) -> GpuDocumentMetadata:
```

- Exact decorators: none.
- Declared return annotation: `GpuDocumentMetadata`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `payload` | positional-or-keyword | `Any` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuDocumentMetadata(**values, written_files=tuple(written))`
- Explicit raise paths:
  - `TypeError("Cached GPU document metadata is invalid")` under lexical guard `not isinstance(payload, dict)`.
  - `TypeError("Cached GPU written-file metadata is invalid")` under lexical guard `not isinstance(files, list)`.
  - `TypeError("Cached GPU written-file entry is invalid")` under lexical guard `not isinstance(item, dict)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_load_cached_archive` via `_document_from_dict`
- value/type reference: `landscout.sources.gpu_fr::_load_cached_archive` via `_document_from_dict`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.pop` | `unresolved local/third-party receiver; no ownership inferred` |
| `written.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuWrittenFile` | `landscout.sources.gpu_fr.GpuWrittenFile` |
| `GpuDocumentMetadata` | `landscout.sources.gpu_fr.GpuDocumentMetadata` |
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
| In-memory mutation | `values.pop("written_files")`<br>`written.append(GpuWrittenFile(**item))` |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_replace_file`

**Purpose:** Implements `replace file` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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
- direct call: `landscout.sources.gpu_fr::_publish_cache_pair` via `_replace_file`
- value/type reference: `landscout.sources.gpu_fr::_publish_cache_pair` via `_replace_file`

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

### `_cache_recovery_paths`

**Purpose:** Implements `cache recovery paths` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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
- direct call: `landscout.sources.gpu_fr::_require_no_cache_recovery_material` via `_cache_recovery_paths`
- value/type reference: `landscout.sources.gpu_fr::_require_no_cache_recovery_material` via `_cache_recovery_paths`
- direct call: `landscout.sources.gpu_fr::_publish_cache_pair` via `_cache_recovery_paths`
- value/type reference: `landscout.sources.gpu_fr::_publish_cache_pair` via `_cache_recovery_paths`

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

**Purpose:** Implements `require no cache recovery material` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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
  - `GpuDownloadError(<br>            "GPU cache recovery backup already exists; manual recovery is required"<br>        )` under lexical guard `any(path.exists() or _is_link_or_junction(path) for path in recovery_paths)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_publish_cache_pair` via `_require_no_cache_recovery_material`
- value/type reference: `landscout.sources.gpu_fr::_publish_cache_pair` via `_require_no_cache_recovery_material`
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `_require_no_cache_recovery_material`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `_require_no_cache_recovery_material`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_cache_recovery_paths` | `landscout.sources.gpu_fr._cache_recovery_paths` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `GpuDownloadError` | `landscout.sources.gpu_fr.GpuDownloadError` |

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
    recovery_paths = _cache_recovery_paths(archive_path, metadata_path)
    if any(path.exists() or _is_link_or_junction(path) for path in recovery_paths):
        raise GpuDownloadError(
            "GPU cache recovery backup already exists; manual recovery is required"
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_prepare_temporary_cache_file`

**Purpose:** Implements `prepare temporary cache file` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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
  - `GpuDownloadError("GPU cache temporary path is a link or junction")` under lexical guard `_is_link_or_junction(path)`.
  - `GpuDownloadError("GPU cache temporary path is not a regular file")` under lexical guard `path.exists()`.
  - `re-raise`.
  - `GpuDownloadError(<br>            "GPU cache temporary path cannot be prepared safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `_prepare_temporary_cache_file`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `_prepare_temporary_cache_file`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `GpuDownloadError` | `landscout.sources.gpu_fr.GpuDownloadError` |
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
            raise GpuDownloadError("GPU cache temporary path is a link or junction")
        if path.exists():
            if not path.is_file():
                raise GpuDownloadError("GPU cache temporary path is not a regular file")
            path.unlink()
    except GpuDownloadError:
        raise
    except OSError as error:
        raise GpuDownloadError(
            "GPU cache temporary path cannot be prepared safely"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_cleanup_temporary_cache_files`

**Purpose:** Implements `cleanup temporary cache files` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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
  - `GpuDownloadError(<br>            "GPU cache temporary files could not be cleaned safely"<br>        )` under lexical guard `cleanup_error is not None and primary_error is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `_cleanup_temporary_cache_files`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `_cleanup_temporary_cache_files`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuDownloadError` | `landscout.sources.gpu_fr.GpuDownloadError` |

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
        raise GpuDownloadError(
            "GPU cache temporary files could not be cleaned safely"
        ) from cleanup_error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_publish_cache_pair`

**Purpose:** Implements `publish cache pair` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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
  - `GpuDownloadError(<br>                "GPU cache publication and rollback both failed"<br>            )`.
  - `re-raise`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `_publish_cache_pair`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `_publish_cache_pair`
- direct call: `tests.unit.test_gpu_fr::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `gpu._publish_cache_pair`
- direct call: `tests.unit.test_gpu_fr::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `gpu._publish_cache_pair`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_cache_recovery_paths` | `landscout.sources.gpu_fr._cache_recovery_paths` |
| `archive_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_no_cache_recovery_material` | `landscout.sources.gpu_fr._require_no_cache_recovery_material` |
| `copy2` | `shutil.copy2` |
| `archive_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_file` | `landscout.sources.gpu_fr._replace_file` |
| `archive_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuDownloadError` | `landscout.sources.gpu_fr.GpuDownloadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_path.is_file`<br>`metadata_path.is_file` |
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_load_cached_archive`

**Purpose:** Implements `load cached archive` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _load_cached_archive(
    archive_path: Path,
    metadata_path: Path,
    document: GpuDocumentMetadata,
    max_age_hours: float,
) -> GpuArchiveDownload | None:
```

- Exact decorators: none.
- Declared return annotation: `GpuArchiveDownload | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `metadata_path` | positional-or-keyword | `Path` | `required` |
| `document` | positional-or-keyword | `GpuDocumentMetadata` | `required` |
| `max_age_hours` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `GpuArchiveDownload(<br>            document=document,<br>            download_timestamp=timestamp,<br>            filename=archive_path.name,<br>            archive_format="zip",<br>            file_size=size,<br>            sha256=checksum,<br>            path=archive_path,<br>            cache_hit=True,<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `_load_cached_archive`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `_load_cached_archive`
- direct call: `tests.unit.test_gpu_fr::test_boolean_cache_integrity_counts_are_not_accepted_as_integers` via `gpu._load_cached_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_document_from_dict` | `landscout.sources.gpu_fr._document_from_dict` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `downloaded_at.utcoffset` | `unresolved local/third-party receiver; no ownership inferred` |
| `(datetime.now(UTC) - downloaded_at.astimezone(UTC)).total_seconds` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `downloaded_at.astimezone` | `unresolved local/third-party receiver; no ownership inferred` |
| `validate_gpu_archive` | `landscout.sources.gpu_fr.validate_gpu_archive` |
| `_sha256` | `landscout.sources.gpu_fr._sha256` |
| `archive_path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `payload.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveDownload` | `landscout.sources.gpu_fr.GpuArchiveDownload` |

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
def _load_cached_archive(
    archive_path: Path,
    metadata_path: Path,
    document: GpuDocumentMetadata,
    max_age_hours: float,
) -> GpuArchiveDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        payload = loads_strict_json_object(metadata_path.read_bytes())
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
            and type(payload.get("file_size")) is int
            and payload["file_size"] == size
            and payload.get("sha256") == checksum
            and type(payload.get("member_count")) is int
            and payload["member_count"] == len(members)
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
        StrictJsonError,
        GpuArchiveError,
    ):
        return None
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `download_gpu_document`

**Purpose:** Download and transactionally cache one discovered official GPU ZIP.

**Exact signature**

```python
def download_gpu_document(
    document: GpuDocumentMetadata,
    config: GpuSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> GpuArchiveDownload:
```

- Exact decorators: none.
- Declared return annotation: `GpuArchiveDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `document` | positional-or-keyword | `GpuDocumentMetadata` | `required` |
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |
| `cache_dir` | positional-or-keyword | `Path` | `DEFAULT_CACHE_DIR` |
| `timeout` | positional-or-keyword | `float` | `120.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `cached`
  - `result`
- Explicit raise paths:
  - `GpuDownloadError("GPU source config is invalid")`.
  - `GpuDownloadError(<br>            f"GPU document download failed: {document.source_url}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `download_gpu_document`
- value/type reference: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `download_gpu_document`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::_download` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::_download` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_download_rejects_document_inconsistent_with_config` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_document_inconsistent_with_config` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_download_rejects_forged_written_file_provenance_before_network` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_forged_written_file_provenance_before_network` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_download_rejects_forged_unsafe_archive_name_before_io` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_download_rejects_forged_unsafe_archive_name_before_io` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_archive_name_with_one_zip_suffix_is_not_duplicated` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_fresh_cache_is_reused` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_fresh_cache_is_reused` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_stale_recovery_backup_rejects_cache_before_network` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_recovery_backup_rejects_cache_before_network` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_expired_cache_is_refreshed` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_expired_cache_is_refreshed` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_failed_refresh_preserves_previous_cache` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_failed_refresh_preserves_previous_cache` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_metadata_publication_failure_rolls_back_both_cache_files` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_metadata_publication_failure_rolls_back_both_cache_files` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_corrupt_download_is_rejected` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_corrupt_download_is_rejected` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_tampered_sidecar_invalidates_cache` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_tampered_sidecar_invalidates_cache` via `download_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_cached_document_lineage_change_forces_refresh` via `download_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_cached_document_lineage_change_forces_refresh` via `download_gpu_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.gpu_fr._validated_source_config` |
| `GpuDownloadError` | `landscout.sources.gpu_fr.GpuDownloadError` |
| `_validate_gpu_document_for_config` | `landscout.sources.gpu_fr._validate_gpu_document_for_config` |
| `_require_no_cache_recovery_material` | `landscout.sources.gpu_fr._require_no_cache_recovery_material` |
| `_load_cached_archive` | `landscout.sources.gpu_fr._load_cached_archive` |
| `cache_dir.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `_prepare_temporary_cache_file` | `landscout.sources.gpu_fr._prepare_temporary_cache_file` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `temporary_archive.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `copyfileobj` | `shutil.copyfileobj` |
| `validate_gpu_archive` | `landscout.sources.gpu_fr.validate_gpu_archive` |
| `GpuArchiveDownload` | `landscout.sources.gpu_fr.GpuArchiveDownload` |
| `datetime.now(UTC).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `temporary_archive.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `landscout.sources.gpu_fr._sha256` |
| `_document_identity` | `landscout.sources.gpu_fr._document_identity` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_metadata.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `_publish_cache_pair` | `landscout.sources.gpu_fr._publish_cache_pair` |
| `_cleanup_temporary_cache_files` | `landscout.sources.gpu_fr._cleanup_temporary_cache_files` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
            temporary_archive.open("xb") as output,
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
        with temporary_metadata.open("x", encoding="utf-8") as output:
            output.write(
                json.dumps(lineage, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_classify_file`

**Purpose:** Implements `classify file` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _classify_file(path: Path) -> FileCategory:
```

- Exact decorators: none.
- Declared return annotation: `FileCategory`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `"SPATIAL_DATA"`
  - `"METADATA"`
  - `"WRITTEN_REGULATION"`
  - `"OTHER_ATTACHMENT"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_inventory` via `_classify_file`
- value/type reference: `landscout.sources.gpu_fr::_inventory` via `_classify_file`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_inventory`

**Purpose:** Implements `inventory` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuExtractedFile, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(files)`
- Explicit raise paths:
  - `GpuArchiveError(f"GPU extraction root is not a regular directory: {root}")` under lexical guard `_is_link_or_junction(root) or not root.is_dir()`.
  - `GpuArchiveError(f"Extracted GPU symbolic link is forbidden: {path}")` under lexical guard `_is_link_or_junction(path)`.
  - `GpuArchiveError(<br>                f"Extracted GPU special filesystem entry is forbidden: {path}"<br>            )` under lexical guard `not path.is_file() and not path.is_dir()`.
  - `GpuArchiveError(<br>                f"Extracted GPU file escapes cache: {path}"<br>            )`.
  - `GpuArchiveError("Extracted GPU package contains no files")` under lexical guard `not files`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `_inventory`
- value/type reference: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `_inventory`
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_inventory`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_inventory`
- direct call: `tests.unit.test_gpu_fr::test_extraction_inventory_rejects_special_entry` via `gpu._inventory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `root.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `root.rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `item.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `resolved.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `files.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuExtractedFile` | `landscout.sources.gpu_fr.GpuExtractedFile` |
| `relative.as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.suffix.casefold().lstrip` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `landscout.sources.gpu_fr._sha256` |
| `_classify_file` | `landscout.sources.gpu_fr._classify_file` |
| `files.sort` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.is_dir`<br>`path.is_file`<br>`path.is_dir`<br>`item.is_file`<br>`path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `files.append(<br>            GpuExtractedFile(<br>                relative_path=relative.as_posix(),<br>                file_type=path.suffix.casefold().lstrip(".") or "none",<br>                size_bytes=path.stat().st_size,<br>                sha256=_sha256(path),<br>                category=_classify_file(path),<br>            )<br>        )`<br>`files.sort(key=lambda item: item.relative_path)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    if _is_link_or_junction(root) or not root.is_dir():
        raise GpuArchiveError(f"GPU extraction root is not a regular directory: {root}")
    for path in root.rglob("*"):
        if _is_link_or_junction(path):
            raise GpuArchiveError(f"Extracted GPU symbolic link is forbidden: {path}")
        if not path.is_file() and not path.is_dir():
            raise GpuArchiveError(
                f"Extracted GPU special filesystem entry is forbidden: {path}"
            )
    files: list[GpuExtractedFile] = []
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=str):
        if path.parent == root and path.name == EXTRACTION_MANIFEST_NAME:
            continue
        resolved = path.resolve()
        try:
            relative = resolved.relative_to(root.resolve())
        except ValueError as error:
            raise GpuArchiveError(
                f"Extracted GPU file escapes cache: {path}"
            ) from error
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_manifest_payload`

**Purpose:** Implements `manifest payload` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _manifest_payload(
    download: GpuArchiveDownload, files: tuple[GpuExtractedFile, ...]
) -> dict[str, Any]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, Any]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `GpuArchiveDownload` | `required` |
| `files` | positional-or-keyword | `tuple[GpuExtractedFile, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "schema_version": EXTRACTION_MANIFEST_SCHEMA_VERSION,<br>        "archive_sha256": download.sha256,<br>        "files": [<br>            {<br>                "relative_path": item.relative_path,<br>                "size_bytes": item.size_bytes,<br>                "sha256": item.sha256,<br>            }<br>            for item in files<br>        ],<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_manifest_payload`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_manifest_payload`

Outbound call expressions and conservative ownership:
- No calls.

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_extraction_manifest`

**Purpose:** Implements `validate extraction manifest` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _validate_extraction_manifest(
    root: Path, download: GpuArchiveDownload
) -> tuple[GpuExtractedFile, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuExtractedFile, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `download` | positional-or-keyword | `GpuArchiveDownload` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `actual_files`
- Explicit raise paths:
  - `GpuArchiveError("GPU extraction manifest is missing or unsafe")` under lexical guard `_is_link_or_junction(marker) or not marker.is_file()`.
  - `GpuArchiveError("GPU extraction manifest is unreadable")`.
  - `GpuArchiveError("GPU extraction manifest has an invalid structure")` under lexical guard `set(payload) != {<br>        "schema_version",<br>        "archive_sha256",<br>        "files",<br>    }`.
  - `GpuArchiveError("GPU extraction manifest schema is unsupported")` under lexical guard `type(payload["schema_version"]) is not int<br>        or payload["schema_version"] != EXTRACTION_MANIFEST_SCHEMA_VERSION`.
  - `GpuArchiveError("GPU extraction manifest archive lineage differs")` under lexical guard `payload["archive_sha256"] != download.sha256`.
  - `GpuArchiveError("GPU extraction manifest files are invalid")` under lexical guard `not isinstance(entries, list)`.
  - `GpuArchiveError("GPU extraction manifest file entry is invalid")` under lexical guard `not isinstance(entry, dict) or set(entry) != {<br>            "relative_path",<br>            "size_bytes",<br>            "sha256",<br>        }`.
  - `GpuArchiveError("GPU extraction manifest file value is invalid")` under lexical guard `not isinstance(relative_path, str)<br>            or not _safe_archive_member(relative_path)<br>            or relative_path == EXTRACTION_MANIFEST_NAME<br>            or type(size_bytes) is not int<br>            or size_bytes < 0<br>            or not isinstance(checksum, str)<br>            or re.fullmatch(r"[0-9a-f]{64}", checksum) is None`.
  - `GpuArchiveError(<br>                "GPU extraction manifest paths are duplicated or not deterministic"<br>            )` under lexical guard `previous_path is not None and relative_path <= previous_path`.
  - `GpuArchiveError(<br>            "GPU extraction files do not match the versioned integrity manifest"<br>        )` under lexical guard `actual != expected`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_validate_extraction_manifest`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_validate_extraction_manifest`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_validate_extraction_manifest`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_validate_extraction_manifest`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_validate_extraction_manifest`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_validate_extraction_manifest`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `marker.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `marker.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_safe_archive_member` | `landscout.sources.gpu_fr._safe_archive_member` |
| `re.fullmatch` | `re.fullmatch` |
| `expected.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inventory` | `landscout.sources.gpu_fr._inventory` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `marker.is_file`<br>`marker.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `expected.append((relative_path, size_bytes, checksum))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_extraction_manifest(
    root: Path, download: GpuArchiveDownload
) -> tuple[GpuExtractedFile, ...]:
    marker = root / EXTRACTION_MANIFEST_NAME
    if _is_link_or_junction(marker) or not marker.is_file():
        raise GpuArchiveError("GPU extraction manifest is missing or unsafe")
    try:
        payload = loads_strict_json_object(marker.read_bytes())
    except (OSError, StrictJsonError) as error:
        raise GpuArchiveError("GPU extraction manifest is unreadable") from error
    if set(payload) != {
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_remove_extraction_path`

**Purpose:** Implements `remove extraction path` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _remove_extraction_path(path: Path) -> None:
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
- direct call: `landscout.sources.gpu_fr::_cleanup_temporary_extraction_directory` via `_remove_extraction_path`
- value/type reference: `landscout.sources.gpu_fr::_cleanup_temporary_extraction_directory` via `_remove_extraction_path`
- direct call: `landscout.sources.gpu_fr::_publish_extraction_directory` via `_remove_extraction_path`
- value/type reference: `landscout.sources.gpu_fr::_publish_extraction_directory` via `_remove_extraction_path`

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
def _remove_extraction_path(path: Path) -> None:
    if path.is_junction():
        path.rmdir()
    elif path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.exists():
        shutil.rmtree(path)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_cleanup_temporary_extraction_directory`

**Purpose:** Implements `cleanup temporary extraction directory` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _cleanup_temporary_extraction_directory(
    path: Path,
    primary_error: BaseException | None,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `primary_error` | positional-or-keyword | `BaseException \| None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GpuArchiveError(<br>                "GPU extraction temporary directory could not be cleaned safely"<br>            )` under lexical guard `primary_error is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_cleanup_temporary_extraction_directory`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_cleanup_temporary_extraction_directory`
- direct call: `tests.unit.test_gpu_fr::test_extraction_cleanup_preserves_primary_controlled_error` via `gpu._cleanup_temporary_extraction_directory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_remove_extraction_path` | `landscout.sources.gpu_fr._remove_extraction_path` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |

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
def _cleanup_temporary_extraction_directory(
    path: Path,
    primary_error: BaseException | None,
) -> None:
    try:
        _remove_extraction_path(path)
    except OSError as error:
        if primary_error is None:
            raise GpuArchiveError(
                "GPU extraction temporary directory could not be cleaned safely"
            ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_require_no_extraction_recovery_material`

**Purpose:** Implements `require no extraction recovery material` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _require_no_extraction_recovery_material(root: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GpuArchiveError(<br>            "GPU extraction recovery backup exists; manual recovery is required"<br>        )` under lexical guard `backup.exists() or _is_link_or_junction(backup)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_publish_extraction_directory` via `_require_no_extraction_recovery_material`
- value/type reference: `landscout.sources.gpu_fr::_publish_extraction_directory` via `_require_no_extraction_recovery_material`
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_require_no_extraction_recovery_material`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_require_no_extraction_recovery_material`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `backup.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `backup.exists` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _require_no_extraction_recovery_material(root: Path) -> None:
    backup = root.with_name(f"{root.name}.bak")
    if backup.exists() or _is_link_or_junction(backup):
        raise GpuArchiveError(
            "GPU extraction recovery backup exists; manual recovery is required"
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_prepare_temporary_extraction_directory`

**Purpose:** Implements `prepare temporary extraction directory` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _prepare_temporary_extraction_directory(path: Path) -> None:
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
  - `GpuArchiveError("GPU extraction temporary path is a link or junction")` under lexical guard `_is_link_or_junction(path)`.
  - `GpuArchiveError(<br>                "GPU extraction temporary path already exists; manual recovery is required"<br>            )` under lexical guard `path.exists()`.
  - `re-raise`.
  - `GpuArchiveError(<br>            "GPU extraction temporary path cannot be prepared safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_prepare_temporary_extraction_directory`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_prepare_temporary_extraction_directory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.exists` |
| Filesystem/archive write or publication | `path.mkdir` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _prepare_temporary_extraction_directory(path: Path) -> None:
    try:
        if _is_link_or_junction(path):
            raise GpuArchiveError("GPU extraction temporary path is a link or junction")
        if path.exists():
            raise GpuArchiveError(
                "GPU extraction temporary path already exists; manual recovery is required"
            )
        path.mkdir()
    except GpuArchiveError:
        raise
    except OSError as error:
        raise GpuArchiveError(
            "GPU extraction temporary path cannot be prepared safely"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_publish_extraction_directory`

**Purpose:** Implements `publish extraction directory` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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
  - `GpuArchiveError(<br>                "GPU extraction backup publication failed before replacement"<br>            )` under lexical guard `root.exists() or _is_link_or_junction(root)`.
  - `GpuArchiveError(<br>                "GPU extraction publication and rollback both failed"<br>            )`.
  - `GpuArchiveError("GPU extraction publication failed")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_publish_extraction_directory`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_publish_extraction_directory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_no_extraction_recovery_material` | `landscout.sources.gpu_fr._require_no_extraction_recovery_material` |
| `root.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `shutil.move` | `shutil.move` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `_remove_extraction_path` | `landscout.sources.gpu_fr._remove_extraction_path` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.exists` |
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
    _require_no_extraction_recovery_material(root)
    old_moved = False
    if root.exists() or _is_link_or_junction(root):
        try:
            shutil.move(str(root), str(backup))
            old_moved = True
        except OSError as error:
            raise GpuArchiveError(
                "GPU extraction backup publication failed before replacement"
            ) from error
    try:
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_discover_standard_models`

**Purpose:** Implements `discover standard models` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _discover_standard_models(root: Path) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(sorted(models, key=str.casefold))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::extract_gpu_document` via `_discover_standard_models`
- value/type reference: `landscout.sources.gpu_fr::extract_gpu_document` via `_discover_standard_models`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_discover_standard_models`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_discover_standard_models`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `ElementTree.parse` | `xml.etree.ElementTree.parse` |
| `parsed.iter` | `unresolved local/third-party receiver; no ownership inferred` |
| `element.text.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.fullmatch` | `re.fullmatch` |
| `models.add` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `models.add(text)` |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `extract_gpu_document`

**Purpose:** Safely extract a validated GPU ZIP into a content-addressed cache.

**Exact signature**

```python
def extract_gpu_document(
    download: GpuArchiveDownload, cache_dir: Path = DEFAULT_CACHE_DIR
) -> GpuExtraction:
```

- Exact decorators: none.
- Declared return annotation: `GpuExtraction`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `GpuArchiveDownload` | `required` |
| `cache_dir` | positional-or-keyword | `Path` | `DEFAULT_CACHE_DIR` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuExtraction(<br>                archive=download,<br>                extraction_root=root,<br>                files=files,<br>                standard_models=_discover_standard_models(root),<br>                cache_hit=True,<br>            )`
  - `GpuExtraction(<br>            archive=download,<br>            extraction_root=root,<br>            files=files,<br>            standard_models=standard_models,<br>            cache_hit=False,<br>        )`
- Explicit raise paths:
  - `re-raise` under lexical guard `isinstance(error, GpuArchiveError)`.
  - `GpuArchiveError("Cannot safely extract GPU document")`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `extract_gpu_document`
- value/type reference: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `extract_gpu_document`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `extract_gpu_document`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `extract_gpu_document`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::test_extraction_inventory_and_cache` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_inventory_and_cache` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_extraction_manifest_is_created_exclusively` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_manifest_is_created_exclusively` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_stale_extraction_backup_fails_closed_and_is_preserved` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_extraction_backup_fails_closed_and_is_preserved` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_extraction_publication_and_rollback_failure_preserves_backup` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_publication_and_rollback_failure_preserves_backup` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_extraction_publication_failure_restores_existing_root` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_publication_failure_restores_existing_root` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_extraction_backup_move_failure_preserves_existing_root` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_backup_move_failure_preserves_existing_root` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_extraction_temporary_link_is_rejected_without_unlinking_target` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_temporary_link_is_rejected_without_unlinking_target` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_stale_extraction_temporary_directory_fails_closed_and_is_preserved` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_extraction_temporary_directory_fails_closed_and_is_preserved` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_duplicate_extraction_manifest_key_forces_verified_rebuild` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_duplicate_extraction_manifest_key_forces_verified_rebuild` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_stale_download_object_rejects_replaced_valid_archive` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_stale_download_object_rejects_replaced_valid_archive` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_extraction_rejects_archive_object_inconsistent_with_path` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_extraction_rejects_archive_object_inconsistent_with_path` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::test_tampered_extraction_is_rebuilt_from_verified_archive` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::test_tampered_extraction_is_rebuilt_from_verified_archive` via `extract_gpu_document`
- direct call: `tests.unit.test_gpu_fr::_extraction_from_archive` via `extract_gpu_document`
- value/type reference: `tests.unit.test_gpu_fr::_extraction_from_archive` via `extract_gpu_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_gpu_archive_download` | `landscout.sources.gpu_fr._validate_gpu_archive_download` |
| `_require_no_extraction_recovery_material` | `landscout.sources.gpu_fr._require_no_extraction_recovery_material` |
| `root.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `_validate_extraction_manifest` | `landscout.sources.gpu_fr._validate_extraction_manifest` |
| `GpuExtraction` | `landscout.sources.gpu_fr.GpuExtraction` |
| `_discover_standard_models` | `landscout.sources.gpu_fr._discover_standard_models` |
| `root.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `_prepare_temporary_extraction_directory` | `landscout.sources.gpu_fr._prepare_temporary_extraction_directory` |
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `_validated_zip_destinations` | `landscout.sources.gpu_fr._validated_zip_destinations` |
| `archive.infolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_root.joinpath` | `unresolved local/third-party receiver; no ownership inferred` |
| `member.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `member.filename.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `target.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `target.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `target.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `copyfileobj` | `shutil.copyfileobj` |
| `_inventory` | `landscout.sources.gpu_fr._inventory` |
| `marker.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `_manifest_payload` | `landscout.sources.gpu_fr._manifest_payload` |
| `_publish_extraction_directory` | `landscout.sources.gpu_fr._publish_extraction_directory` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuArchiveError` | `landscout.sources.gpu_fr.GpuArchiveError` |
| `_cleanup_temporary_extraction_directory` | `landscout.sources.gpu_fr._cleanup_temporary_extraction_directory` |
| `sys.exception` | `sys.exception` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.is_dir`<br>`zipfile.ZipFile`<br>`member.is_dir`<br>`archive.open`<br>`target.open`<br>`marker.open` |
| Filesystem/archive write or publication | `root.parent.mkdir`<br>`target.mkdir`<br>`target.parent.mkdir`<br>`copyfileobj` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def extract_gpu_document(
    download: GpuArchiveDownload, cache_dir: Path = DEFAULT_CACHE_DIR
) -> GpuExtraction:
    """Safely extract a validated GPU ZIP into a content-addressed cache."""

    _validate_gpu_archive_download(download)
    root = cache_dir / "x" / download.sha256[:16]
    _require_no_extraction_recovery_material(root)
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
    _prepare_temporary_extraction_directory(temporary_root)
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
        with marker.open("x", encoding="utf-8") as output:
            output.write(
                json.dumps(_manifest_payload(download, files), indent=2, sort_keys=True)
                + "\n"
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
        _cleanup_temporary_extraction_directory(
            temporary_root,
            sys.exception(),
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `discover_gpu_spatial_layers`

**Purpose:** Discover every real GeoPackage or Shapefile layer in an extraction.

**Exact signature**

```python
def discover_gpu_spatial_layers(
    extraction: GpuExtraction,
) -> tuple[GpuSpatialLayerReference, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuSpatialLayerReference, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `GpuExtraction` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(<br>        sorted(references, key=lambda item: (str(item.dataset_path), item.source_layer))<br>    )`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>                f"Cannot list GPU GeoPackage layers: {path}"<br>            )`.
  - `GpuSpatialInspectionError(<br>            "GPU document contains no supported spatial data"<br>        )` under lexical guard `not references`.
  - `GpuSpatialInspectionError("GPU document exposes duplicate spatial layers")` under lexical guard `len(unique) != len(references)`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `discover_gpu_spatial_layers`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `discover_gpu_spatial_layers`
- direct call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `discover_gpu_spatial_layers`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `discover_gpu_spatial_layers`
- direct call: `tests.unit.test_enrich_planning_features::_planning_document` via `gpu_source_module.discover_gpu_spatial_layers`
- direct call: `tests.unit.test_enrich_planning_features::_refresh_extraction_inventory` via `gpu_source_module.discover_gpu_spatial_layers`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `discover_gpu_spatial_layers`
- value/type reference: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `discover_gpu_spatial_layers`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `gpu_source_module.discover_gpu_spatial_layers`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `pyogrio.list_layers` | `pyogrio.list_layers` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `layers[:, 0].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `references.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `item.dataset_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `references.append(GpuSpatialLayerReference(path, raw_name, "GPKG"))`<br>`references.append(GpuSpatialLayerReference(path, path.stem, "ESRI Shapefile"))` |
| Direct parameter mutation | None directly present. |

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
                references.append(GpuSpatialLayerReference(path, raw_name, "GPKG"))
    for path in shp_paths:
        references.append(GpuSpatialLayerReference(path, path.stem, "ESRI Shapefile"))
    if not references:
        raise GpuSpatialInspectionError(
            "GPU document contains no supported spatial data"
        )
    unique = {(item.dataset_path.resolve(), item.source_layer) for item in references}
    if len(unique) != len(references):
        raise GpuSpatialInspectionError("GPU document exposes duplicate spatial layers")
    return tuple(
        sorted(references, key=lambda item: (str(item.dataset_path), item.source_layer))
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_layer_config`

**Purpose:** Implements `layer config` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _layer_config(
    config: GpuSourceConfig, logical_name: LogicalLayerName
) -> GpuLogicalLayerConfig:
```

- Exact decorators: none.
- Declared return annotation: `GpuLogicalLayerConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |
| `logical_name` | positional-or-keyword | `LogicalLayerName` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `getattr(config.spatial_layers, logical_name)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_discover_logical_layer` via `_layer_config`
- value/type reference: `landscout.sources.gpu_fr::_discover_logical_layer` via `_layer_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
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
def _layer_config(
    config: GpuSourceConfig, logical_name: LogicalLayerName
) -> GpuLogicalLayerConfig:
    return getattr(config.spatial_layers, logical_name)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_discover_logical_layer`

**Purpose:** Implements `discover logical layer` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

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

- Exact decorators: none.
- Declared return annotation: `GpuSpatialLayerReference | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `references` | positional-or-keyword | `tuple[GpuSpatialLayerReference, ...]` | `required` |
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |
| `logical_name` | positional-or-keyword | `LogicalLayerName` | `required` |
| `required` | keyword-only | `bool` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `matches[0]`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>            f"Expected {adjective} {logical_name} layer, found {len(matches)}"<br>        )` under lexical guard `len(matches) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_configured_logical_references` via `_discover_logical_layer`
- value/type reference: `landscout.sources.gpu_fr::_configured_logical_references` via `_discover_logical_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_layer_config` | `landscout.sources.gpu_fr._layer_config` |
| `_normalize_words` | `landscout.sources.gpu_fr._normalize_words` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |

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
| In-memory mutation | `matches.append(item)` |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_configured_logical_references`

**Purpose:** Implements `configured logical references` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _configured_logical_references(
    references: tuple[GpuSpatialLayerReference, ...],
    config: GpuSourceConfig,
) -> tuple[tuple[LogicalLayerName, GpuSpatialLayerReference], ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[LogicalLayerName, GpuSpatialLayerReference], ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `references` | positional-or-keyword | `tuple[GpuSpatialLayerReference, ...]` | `required` |
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(selected)`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>            "GPU spatial-layer inventory must be an exact immutable tuple"<br>        )` under lexical guard `type(references) is not tuple or any(<br>        type(reference) is not GpuSpatialLayerReference for reference in references<br>    )`.
  - `GpuSpatialInspectionError(<br>            "Two GPU logical roles resolve to the same physical layer"<br>        )` under lexical guard `len(physical_roles) != len(set(physical_roles))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_configured_logical_references`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_configured_logical_references`
- direct call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_configured_logical_references`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_configured_logical_references`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `_discover_logical_layer` | `landscout.sources.gpu_fr._discover_logical_layer` |
| `selected.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `reference.dataset_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `selected.append((logical_name, reference))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _configured_logical_references(
    references: tuple[GpuSpatialLayerReference, ...],
    config: GpuSourceConfig,
) -> tuple[tuple[LogicalLayerName, GpuSpatialLayerReference], ...]:
    if type(references) is not tuple or any(
        type(reference) is not GpuSpatialLayerReference for reference in references
    ):
        raise GpuSpatialInspectionError(
            "GPU spatial-layer inventory must be an exact immutable tuple"
        )
    selected: list[tuple[LogicalLayerName, GpuSpatialLayerReference]] = []
    for logical_name in _GPU_LOGICAL_LAYER_NAMES:
        reference = _discover_logical_layer(
            references,
            config,
            logical_name,
            required=logical_name == "zoning",
        )
        if reference is not None:
            selected.append((logical_name, reference))
    physical_roles = [
        (reference.dataset_path.resolve(), reference.source_layer)
        for _, reference in selected
    ]
    if len(physical_roles) != len(set(physical_roles)):
        raise GpuSpatialInspectionError(
            "Two GPU logical roles resolve to the same physical layer"
        )
    return tuple(selected)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_gpu_extraction_for_config`

**Purpose:** Implements `validate gpu extraction for config` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _validate_gpu_extraction_for_config(
    extraction: object,
    config: GpuSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `object` | `required` |
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>                "GPU extraction must be exactly a GpuExtraction"<br>            )` under lexical guard `type(extraction) is not GpuExtraction`.
  - `GpuSpatialInspectionError(<br>                "GPU extraction archive must be exactly a GpuArchiveDownload"<br>            )` under lexical guard `type(extraction.archive) is not GpuArchiveDownload`.
  - `GpuSpatialInspectionError(<br>                "GPU extraction document must be exactly a GpuDocumentMetadata"<br>            )` under lexical guard `type(extraction.archive.document) is not GpuDocumentMetadata`.
  - `GpuSpatialInspectionError(<br>                "GPU extraction inventory differs from its verified manifest"<br>            )` under lexical guard `extraction.files != manifest_files`.
  - `GpuSpatialInspectionError(<br>                "GPU extraction standard-model inventory differs from source"<br>            )` under lexical guard `type(extraction.standard_models) is not tuple or (<br>            extraction.standard_models != _discover_standard_models(root)<br>        )`.
  - `re-raise`.
  - `GpuSpatialInspectionError(<br>            "GPU extraction does not match its configured physical source"<br>        )`.
  - `GpuSpatialInspectionError(<br>            "GPU extraction/config lineage cannot be validated safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_validate_gpu_extraction_for_config`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_validate_gpu_extraction_for_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `_validate_gpu_document_for_config` | `landscout.sources.gpu_fr._validate_gpu_document_for_config` |
| `_validate_gpu_archive_download` | `landscout.sources.gpu_fr._validate_gpu_archive_download` |
| `_validated_spatial_root` | `landscout.sources.gpu_fr._validated_spatial_root` |
| `_validate_extraction_manifest` | `landscout.sources.gpu_fr._validate_extraction_manifest` |
| `_discover_standard_models` | `landscout.sources.gpu_fr._discover_standard_models` |

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
def _validate_gpu_extraction_for_config(
    extraction: object,
    config: GpuSourceConfig,
) -> None:
    try:
        if type(extraction) is not GpuExtraction:
            raise GpuSpatialInspectionError(
                "GPU extraction must be exactly a GpuExtraction"
            )
        if type(extraction.archive) is not GpuArchiveDownload:
            raise GpuSpatialInspectionError(
                "GPU extraction archive must be exactly a GpuArchiveDownload"
            )
        if type(extraction.archive.document) is not GpuDocumentMetadata:
            raise GpuSpatialInspectionError(
                "GPU extraction document must be exactly a GpuDocumentMetadata"
            )
        _validate_gpu_document_for_config(extraction.archive.document, config)
        _validate_gpu_archive_download(extraction.archive)
        root, _ = _validated_spatial_root(extraction)
        manifest_files = _validate_extraction_manifest(root, extraction.archive)
        if extraction.files != manifest_files:
            raise GpuSpatialInspectionError(
                "GPU extraction inventory differs from its verified manifest"
            )
        if type(extraction.standard_models) is not tuple or (
            extraction.standard_models != _discover_standard_models(root)
        ):
            raise GpuSpatialInspectionError(
                "GPU extraction standard-model inventory differs from source"
            )
        _validate_gpu_archive_download(extraction.archive)
    except GpuSpatialInspectionError:
        raise
    except (GpuArchiveError, GpuDownloadError) as error:
        raise GpuSpatialInspectionError(
            "GPU extraction does not match its configured physical source"
        ) from error
    except Exception as error:
        raise GpuSpatialInspectionError(
            "GPU extraction/config lineage cannot be validated safely"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_gpu_planning_document_config_identity`

**Purpose:** Implements `validate gpu planning document config identity` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _validate_gpu_planning_document_config_identity(
    planning_document: object,
) -> GpuSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `GpuSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `config`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>                "planning_document must be exactly a GpuPlanningDocument"<br>            )` under lexical guard `type(planning_document) is not GpuPlanningDocument`.
  - `GpuSpatialInspectionError(<br>                "GPU planning-document extraction lineage is malformed"<br>            )` under lexical guard `type(planning_document.extraction) is not GpuExtraction<br>            or type(planning_document.extraction.archive) is not GpuArchiveDownload`.
  - `GpuSpatialInspectionError(<br>                "GPU planning-document config SHA256 differs"<br>            )` under lexical guard `type(checksum) is not str<br>            or re.fullmatch(r"[0-9a-f]{64}", checksum) is None<br>            or checksum != _source_config_sha256(config)`.
  - `GpuSpatialInspectionError(<br>                "GPU extraction inventory differs from its verified manifest"<br>            )` under lexical guard `planning_document.extraction.files != manifest_files`.
  - `GpuSpatialInspectionError(<br>                "GPU planning-document spatial inventory differs from its "<br>                "physical extraction"<br>            )` under lexical guard `planning_document.all_spatial_layers != physical_references`.
  - `GpuSpatialInspectionError(<br>                "GPU planning-document inspected layers are malformed"<br>            )` under lexical guard `type(planning_document.related_layers) is not tuple or any(<br>            type(layer) is not GpuInspectedLayer for layer in inspected<br>        )`.
  - `GpuSpatialInspectionError(<br>                "GPU planning-document logical roles differ from its config"<br>            )` under lexical guard `actual != configured`.
  - `re-raise`.
  - `GpuSpatialInspectionError(<br>            "GPU planning-document source config is invalid"<br>        )`.
  - `GpuSpatialInspectionError(<br>            "GPU planning-document config identity cannot be validated safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_validate_gpu_planning_document_config_identity`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_validate_gpu_planning_document_config_identity`
- direct call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_sources` via `_validate_gpu_planning_document_config_identity`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_sources` via `_validate_gpu_planning_document_config_identity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `_validated_source_config` | `landscout.sources.gpu_fr._validated_source_config` |
| `re.fullmatch` | `re.fullmatch` |
| `_source_config_sha256` | `landscout.sources.gpu_fr._source_config_sha256` |
| `_validate_gpu_document_for_config` | `landscout.sources.gpu_fr._validate_gpu_document_for_config` |
| `_validated_spatial_root` | `landscout.sources.gpu_fr._validated_spatial_root` |
| `_validate_extraction_manifest` | `landscout.sources.gpu_fr._validate_extraction_manifest` |
| `discover_gpu_spatial_layers` | `landscout.sources.gpu_fr.discover_gpu_spatial_layers` |
| `_configured_logical_references` | `landscout.sources.gpu_fr._configured_logical_references` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_source_config_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_gpu_planning_document_config_identity(
    planning_document: object,
) -> GpuSourceConfig:
    try:
        if type(planning_document) is not GpuPlanningDocument:
            raise GpuSpatialInspectionError(
                "planning_document must be exactly a GpuPlanningDocument"
            )
        if (
            type(planning_document.extraction) is not GpuExtraction
            or type(planning_document.extraction.archive) is not GpuArchiveDownload
        ):
            raise GpuSpatialInspectionError(
                "GPU planning-document extraction lineage is malformed"
            )
        config = _validated_source_config(planning_document.source_config)
        checksum = planning_document.source_config_sha256
        if (
            type(checksum) is not str
            or re.fullmatch(r"[0-9a-f]{64}", checksum) is None
            or checksum != _source_config_sha256(config)
        ):
            raise GpuSpatialInspectionError(
                "GPU planning-document config SHA256 differs"
            )
        _validate_gpu_document_for_config(
            planning_document.extraction.archive.document,
            config,
        )
        root, _ = _validated_spatial_root(planning_document.extraction)
        manifest_files = _validate_extraction_manifest(
            root,
            planning_document.extraction.archive,
        )
        if planning_document.extraction.files != manifest_files:
            raise GpuSpatialInspectionError(
                "GPU extraction inventory differs from its verified manifest"
            )
        physical_references = discover_gpu_spatial_layers(planning_document.extraction)
        if planning_document.all_spatial_layers != physical_references:
            raise GpuSpatialInspectionError(
                "GPU planning-document spatial inventory differs from its "
                "physical extraction"
            )
        configured = _configured_logical_references(
            planning_document.all_spatial_layers,
            config,
        )
        inspected = (planning_document.zoning, *planning_document.related_layers)
        if type(planning_document.related_layers) is not tuple or any(
            type(layer) is not GpuInspectedLayer for layer in inspected
        ):
            raise GpuSpatialInspectionError(
                "GPU planning-document inspected layers are malformed"
            )
        actual = tuple((layer.logical_name, layer.reference) for layer in inspected)
        if actual != configured:
            raise GpuSpatialInspectionError(
                "GPU planning-document logical roles differ from its config"
            )
        return config
    except GpuSpatialInspectionError:
        raise
    except (GpuArchiveError, GpuConfigError, GpuDownloadError) as error:
        raise GpuSpatialInspectionError(
            "GPU planning-document source config is invalid"
        ) from error
    except Exception as error:
        raise GpuSpatialInspectionError(
            "GPU planning-document config identity cannot be validated safely"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_load_reference`

**Purpose:** Implements `load reference` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _load_reference(reference: GpuSpatialLayerReference) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `reference` | positional-or-keyword | `GpuSpatialLayerReference` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.read_file(<br>                reference.dataset_path, layer=reference.source_layer, engine="pyogrio"<br>            )`
  - `gpd.read_file(reference.dataset_path, engine="pyogrio")`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>            f"Cannot load GPU spatial layer: {reference.source_layer}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_load_reference`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_load_reference`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.read_file` | `geopandas.read_file` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validated_inventory_path`

**Purpose:** Implements `validated inventory path` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _validated_inventory_path(value: object) -> PurePosixPath:
```

- Exact decorators: none.
- Declared return annotation: `PurePosixPath`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `relative`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>            "GPU extraction inventory path must be an exact string"<br>        )` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.
  - `GpuSpatialInspectionError("GPU extraction inventory path is unsafe")` under lexical guard `"\\" in value or "\x00" in value`.
  - `GpuSpatialInspectionError("GPU extraction inventory path is unsafe")` under lexical guard `relative.is_absolute()<br>        or any(part in {"", ".", ".."} for part in parts)<br>        or relative.as_posix() != value`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_spatial_inventory` via `_validated_inventory_path`
- value/type reference: `landscout.sources.gpu_fr::_spatial_inventory` via `_validated_inventory_path`
- direct call: `landscout.sources.gpu_fr::_contained_spatial_path` via `_validated_inventory_path`
- value/type reference: `landscout.sources.gpu_fr::_contained_spatial_path` via `_validated_inventory_path`
- direct call: `landscout.sources.gpu_fr::_spatial_dataset_relative_path` via `_validated_inventory_path`
- value/type reference: `landscout.sources.gpu_fr::_spatial_dataset_relative_path` via `_validated_inventory_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `value.split` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `relative.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `relative.as_posix` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validated_spatial_root`

**Purpose:** Implements `validated spatial root` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _validated_spatial_root(extraction: GpuExtraction) -> tuple[Path, Path]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[Path, Path]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `GpuExtraction` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `root, root.resolve(strict=True)`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>                "GPU extraction root must be a regular directory"<br>            )` under lexical guard `not isinstance(root, Path)<br>            or _is_link_or_junction(root)<br>            or not root.is_dir()`.
  - `re-raise`.
  - `GpuSpatialInspectionError(<br>            "GPU extraction root cannot be resolved safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_validated_spatial_root`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `_validated_spatial_root`
- direct call: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_validated_spatial_root`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `_validated_spatial_root`
- direct call: `landscout.sources.gpu_fr::_spatial_source_family` via `_validated_spatial_root`
- value/type reference: `landscout.sources.gpu_fr::_spatial_source_family` via `_validated_spatial_root`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `root.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `root.resolve` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.is_dir` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_spatial_inventory`

**Purpose:** Implements `spatial inventory` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _spatial_inventory(
    extraction: GpuExtraction,
) -> dict[str, GpuExtractedFile]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, GpuExtractedFile]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `GpuExtraction` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `inventory`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>            "GPU extraction inventory must be an immutable tuple"<br>        )` under lexical guard `type(extraction.files) is not tuple`.
  - `GpuSpatialInspectionError("GPU extraction inventory is invalid")` under lexical guard `not isinstance(item, GpuExtractedFile)`.
  - `GpuSpatialInspectionError(<br>                "GPU extraction inventory contains duplicate paths"<br>            )` under lexical guard `relative.casefold() in {key.casefold() for key in inventory}`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_spatial_source_family` via `_spatial_inventory`
- value/type reference: `landscout.sources.gpu_fr::_spatial_source_family` via `_spatial_inventory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_inventory_path(item.relative_path).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_inventory_path` | `landscout.sources.gpu_fr._validated_inventory_path` |
| `relative.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `key.casefold` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `inventory[relative] = item` |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_contained_spatial_path`

**Purpose:** Implements `contained spatial path` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _contained_spatial_path(
    root: Path,
    root_resolved: Path,
    relative: str,
) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `root_resolved` | positional-or-keyword | `Path` | `required` |
| `relative` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>                    "GPU spatial source path contains a symbolic link or junction"<br>                )` under lexical guard `_is_link_or_junction(current)`.
  - `GpuSpatialInspectionError(<br>                "GPU spatial source must be an extracted regular file"<br>            )` under lexical guard `not path.is_file()`.
  - `re-raise`.
  - `GpuSpatialInspectionError(<br>            "GPU spatial source escapes the verified extraction root"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_spatial_source_family` via `_contained_spatial_path`
- value/type reference: `landscout.sources.gpu_fr::_spatial_source_family` via `_contained_spatial_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_inventory_path` | `landscout.sources.gpu_fr._validated_inventory_path` |
| `root.joinpath` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `resolved.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_spatial_dataset_relative_path`

**Purpose:** Implements `spatial dataset relative path` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _spatial_dataset_relative_path(
    reference: GpuSpatialLayerReference,
    root_resolved: Path,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `reference` | positional-or-keyword | `GpuSpatialLayerReference` | `required` |
| `root_resolved` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_validated_inventory_path(relative.as_posix()).as_posix()`
- Explicit raise paths:
  - `GpuSpatialInspectionError("GPU spatial dataset path is invalid")` under lexical guard `not isinstance(path, Path) or _is_link_or_junction(path)`.
  - `re-raise`.
  - `GpuSpatialInspectionError(<br>            "GPU spatial dataset path escapes the verified extraction root"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_spatial_source_family` via `_spatial_dataset_relative_path`
- value/type reference: `landscout.sources.gpu_fr::_spatial_source_family` via `_spatial_dataset_relative_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.gpu_fr._is_link_or_junction` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `path.resolve(strict=True).relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_inventory_path(relative.as_posix()).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_inventory_path` | `landscout.sources.gpu_fr._validated_inventory_path` |
| `relative.as_posix` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_spatial_source_family`

**Purpose:** Implements `spatial source family` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _spatial_source_family(
    reference: GpuSpatialLayerReference,
    extraction: GpuExtraction,
) -> tuple[str, tuple[tuple[Path, GpuExtractedFile], ...]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, tuple[tuple[Path, GpuExtractedFile], ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `reference` | positional-or-keyword | `GpuSpatialLayerReference` | `required` |
| `extraction` | positional-or-keyword | `GpuExtraction` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `relative, tuple(verified)`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>                "GPU GeoPackage source has an inconsistent extension"<br>            )` under lexical guard `driver == "GPKG"`.
  - `GpuSpatialInspectionError(<br>                    "GPU GeoPackage has an unbound SQLite sidecar"<br>                )` under lexical guard `driver == "GPKG"`.
  - `GpuSpatialInspectionError(<br>                "Cannot list the verified GPU GeoPackage source"<br>            )` under lexical guard `driver == "GPKG"`.
  - `GpuSpatialInspectionError(<br>                "GPU GeoPackage source layer is missing or ambiguous"<br>            )` under lexical guard `driver == "GPKG"`.
  - `GpuSpatialInspectionError(<br>                "GPU Shapefile source identity is inconsistent"<br>            )` under lexical guard `driver == "GPKG"`.
  - `GpuSpatialInspectionError(<br>                "GPU Shapefile inventory is missing a required family member"<br>            )` under lexical guard `driver == "GPKG"`.
  - `GpuSpatialInspectionError(<br>                "GPU Shapefile family cannot be inventoried safely"<br>            )` under lexical guard `driver == "GPKG"`.
  - `GpuSpatialInspectionError(<br>                "GPU Shapefile family differs from the extraction inventory"<br>            )` under lexical guard `driver == "GPKG"`.
  - `GpuSpatialInspectionError(<br>            "GPU spatial source driver must be GPKG or ESRI Shapefile"<br>        )` under lexical guard `driver == "GPKG"`.
  - `GpuSpatialInspectionError(<br>                "GPU spatial source is absent from the extraction inventory"<br>            )` under lexical guard `item is None`.
  - `GpuSpatialInspectionError(<br>                "GPU spatial source inventory integrity is invalid"<br>            )` under lexical guard `type(item.size_bytes) is not int<br>            or item.size_bytes <= 0<br>            or not isinstance(item.sha256, str)<br>            or re.fullmatch(r"[0-9a-f]{64}", item.sha256) is None`.
  - `GpuSpatialInspectionError(<br>                "Cannot read GPU spatial source integrity"<br>            )`.
  - `GpuSpatialInspectionError(<br>                "GPU spatial source size differs from the extraction inventory"<br>            )` under lexical guard `actual_size != item.size_bytes`.
  - `GpuSpatialInspectionError(<br>                "GPU spatial source SHA256 differs from the extraction inventory"<br>            )` under lexical guard `actual_sha != item.sha256`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_spatial_source_family`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_spatial_source_family`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_spatial_root` | `landscout.sources.gpu_fr._validated_spatial_root` |
| `_spatial_inventory` | `landscout.sources.gpu_fr._spatial_inventory` |
| `_spatial_dataset_relative_path` | `landscout.sources.gpu_fr._spatial_dataset_relative_path` |
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `pure.suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `Path(f"{reference.dataset_path}{suffix}").exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `pyogrio.list_layers` | `pyogrio.list_layers` |
| `layers[:, 0].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `f"{pure.stem}{suffix}".casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath(candidate).name.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `required.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath(candidate).suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.joinpath` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidate.resolve(strict=True).relative_to(root_resolved).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidate.resolve(strict=True).relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidate.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `parent.iterdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidate.name.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `inventory.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.fullmatch` | `re.fullmatch` |
| `_contained_spatial_path` | `landscout.sources.gpu_fr._contained_spatial_path` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `landscout.sources.gpu_fr._sha256` |
| `verified.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `Path(f"{reference.dataset_path}{suffix}").exists`<br>`parent.iterdir`<br>`path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `verified.append((path, item))` |
| Direct parameter mutation | None directly present. |

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
                candidate.resolve(strict=True).relative_to(root_resolved).as_posix()
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_same_spatial_crs`

**Purpose:** Implements `same spatial crs` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _same_spatial_crs(left: object, right: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `left` | positional-or-keyword | `object` | `required` |
| `right` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `bool(CRS.from_user_input(left).equals(CRS.from_user_input(right)))`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>            "GPU spatial source CRS cannot be validated"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_compare_inspected_spatial_layer` via `_same_spatial_crs`
- value/type reference: `landscout.sources.gpu_fr::_compare_inspected_spatial_layer` via `_same_spatial_crs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input(left).equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |

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
def _same_spatial_crs(left: object, right: object) -> bool:
    try:
        return bool(CRS.from_user_input(left).equals(CRS.from_user_input(right)))
    except Exception as error:
        raise GpuSpatialInspectionError(
            "GPU spatial source CRS cannot be validated"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_compare_inspected_spatial_layer`

**Purpose:** Implements `compare inspected spatial layer` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _compare_inspected_spatial_layer(
    inspected: GpuInspectedLayer,
    reread: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inspected` | positional-or-keyword | `GpuInspectedLayer` | `required` |
| `reread` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GpuSpatialInspectionError("GPU spatial layer must be a GeoDataFrame")` under lexical guard `not isinstance(loaded, gpd.GeoDataFrame) or not isinstance(<br>            reread, gpd.GeoDataFrame<br>        )`.
  - `GpuSpatialInspectionError(<br>                "Loaded GPU spatial row count differs from its source"<br>            )` under lexical guard `len(loaded) != len(reread)`.
  - `GpuSpatialInspectionError(<br>                "Loaded GPU spatial columns differ from its source"<br>            )` under lexical guard `tuple(loaded.columns) != tuple(reread.columns)`.
  - `GpuSpatialInspectionError(<br>                "Loaded GPU spatial dtypes differ from its source"<br>            )` under lexical guard `tuple(str(dtype) for dtype in loaded.dtypes) != tuple(<br>            str(dtype) for dtype in reread.dtypes<br>        )`.
  - `GpuSpatialInspectionError(<br>                "Loaded GPU spatial geometry metadata differs from its source"<br>            )` under lexical guard `loaded.geometry.name != reread.geometry.name or not _same_spatial_crs(<br>            loaded.crs, reread.crs<br>        )`.
  - `GpuSpatialInspectionError(<br>                "Loaded GPU spatial attributes metadata differs from its source"<br>            )` under lexical guard `loaded.attrs != reread.attrs`.
  - `GpuSpatialInspectionError(<br>                "Loaded GPU spatial attributes or row order differ from its source"<br>            )` under lexical guard `not loaded[attributes]<br>            .reset_index(drop=True)<br>            .equals(reread[attributes].reset_index(drop=True))`.
  - `GpuSpatialInspectionError(<br>                "Loaded GPU spatial geometry or row order differs from its source"<br>            )` under lexical guard `loaded.geometry.to_wkb().tolist() != reread.geometry.to_wkb().tolist()`.
  - `re-raise`.
  - `GpuSpatialInspectionError(<br>            "Loaded GPU spatial layer cannot be compared safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_compare_inspected_spatial_layer`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_compare_inspected_spatial_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_same_spatial_crs` | `landscout.sources.gpu_fr._same_spatial_crs` |
| `loaded[attributes]<br>            .reset_index(drop=True)<br>            .equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `loaded[attributes]<br>            .reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `reread[attributes].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `loaded.geometry.to_wkb().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `loaded.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `reread.geometry.to_wkb().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `reread.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `loaded.geometry.to_wkb().tolist`<br>`loaded.geometry.to_wkb`<br>`reread.geometry.to_wkb().tolist`<br>`reread.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
            raise GpuSpatialInspectionError("GPU spatial layer must be a GeoDataFrame")
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
        if (
            not loaded[attributes]
            .reset_index(drop=True)
            .equals(reread[attributes].reset_index(drop=True))
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_revalidate_gpu_spatial_layer_source`

**Purpose:** Verify and freshly reload one extracted GPU spatial-layer source.

**Exact signature**

```python
def _revalidate_gpu_spatial_layer_source(
    planning_document: GpuPlanningDocument,
    inspected_layer: GpuInspectedLayer,
    *,
    verify_extraction_manifest: bool,
) -> GpuValidatedSpatialLayerSource:
```

- Exact decorators: none.
- Declared return annotation: `GpuValidatedSpatialLayerSource`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `inspected_layer` | positional-or-keyword | `GpuInspectedLayer` | `required` |
| `verify_extraction_manifest` | keyword-only | `bool` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuValidatedSpatialLayerSource(<br>            logical_name=inspected_layer.logical_name,<br>            source_layer=reference.source_layer,<br>            driver=reference.driver,<br>            dataset_relative_path=relative,<br>            source_crs=expected_summary.crs,<br>            feature_count=len(reread),<br>            files=tuple(<br>                GpuSpatialSourceFileIntegrity(<br>                    relative_path=item.relative_path,<br>                    file_type=item.file_type,<br>                    size_bytes=item.size_bytes,<br>                    sha256=item.sha256,<br>                    category=item.category,<br>                )<br>                for _, item in family<br>            ),<br>            ogr_fids=ogr_fids,<br>            data=reread,<br>        )`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>                "GPU planning document or inspected layer is invalid"<br>            )` under lexical guard `type(planning_document) is not GpuPlanningDocument<br>            or type(inspected_layer) is not GpuInspectedLayer`.
  - `GpuSpatialInspectionError(<br>                "Inspected GPU layer does not belong to the planning document"<br>            )` under lexical guard `not any(<br>            inspected_layer is candidate<br>            for candidate in (<br>                planning_document.zoning,<br>                *planning_document.related_layers,<br>            )<br>        )`.
  - `GpuSpatialInspectionError(<br>                "Inspected GPU reference must occur exactly once in the spatial inventory"<br>            )` under lexical guard `sum(<br>                reference == inspected_layer.reference<br>                for reference in planning_document.all_spatial_layers<br>            )<br>            != 1`.
  - `GpuSpatialInspectionError(<br>                "GPU spatial source exposes invalid source FIDs"<br>            )` under lexical guard `not with_fids.index.is_unique or any(<br>            isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0<br>            for value in with_fids.index<br>        )`.
  - `GpuSpatialInspectionError(<br>                "GPU inspected-layer summary differs from its fresh source"<br>            )` under lexical guard `inspected_layer.summary != expected_summary`.
  - `GpuSpatialInspectionError(<br>                "GPU spatial source family changed during verification"<br>            )` under lexical guard `post_relative != relative or tuple(<br>            item.relative_path for _, item in post_family<br>        ) != tuple(item.relative_path for _, item in family)`.
  - `GpuSpatialInspectionError(<br>                    "GPU spatial source changed during verification"<br>                )` under lexical guard `path.stat().st_size != item.size_bytes or _sha256(path) != item.sha256`.
  - `re-raise`.
  - `GpuSpatialInspectionError(<br>            "GPU spatial source cannot be revalidated"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_source` via `_revalidate_gpu_spatial_layer_source`
- value/type reference: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_source` via `_revalidate_gpu_spatial_layer_source`
- direct call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_sources` via `_revalidate_gpu_spatial_layer_source`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_sources` via `_revalidate_gpu_spatial_layer_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_gpu_planning_document_config_identity` | `landscout.sources.gpu_fr._validate_gpu_planning_document_config_identity` |
| `_spatial_source_family` | `landscout.sources.gpu_fr._spatial_source_family` |
| `pyogrio.read_dataframe` | `pyogrio.read_dataframe` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `with_fids.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_compare_inspected_spatial_layer` | `landscout.sources.gpu_fr._compare_inspected_spatial_layer` |
| `_summarize_layer` | `landscout.sources.gpu_fr._summarize_layer` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256` | `landscout.sources.gpu_fr._sha256` |
| `GpuValidatedSpatialLayerSource` | `landscout.sources.gpu_fr.GpuValidatedSpatialLayerSource` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialSourceFileIntegrity` | `landscout.sources.gpu_fr.GpuSpatialSourceFileIntegrity` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
        if (
            type(planning_document) is not GpuPlanningDocument
            or type(inspected_layer) is not GpuInspectedLayer
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
            _validate_gpu_planning_document_config_identity(planning_document)
        reference = inspected_layer.reference
        relative, family = _spatial_source_family(
            reference, planning_document.extraction
        )
        with_fids = pyogrio.read_dataframe(
            reference.dataset_path,
            layer=reference.source_layer,
            fid_as_index=True,
        )
        if not with_fids.index.is_unique or any(
            isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0
            for value in with_fids.index
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `revalidate_gpu_spatial_layer_source`

**Purpose:** Verify and freshly reload one extracted GPU spatial-layer source.

**Exact signature**

```python
def revalidate_gpu_spatial_layer_source(
    planning_document: GpuPlanningDocument,
    inspected_layer: GpuInspectedLayer,
) -> GpuValidatedSpatialLayerSource:
```

- Exact decorators: none.
- Declared return annotation: `GpuValidatedSpatialLayerSource`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `inspected_layer` | positional-or-keyword | `GpuInspectedLayer` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_revalidate_gpu_spatial_layer_source(<br>        planning_document,<br>        inspected_layer,<br>        verify_extraction_manifest=True,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- import: `landscout.stages.index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuWrittenFile,
    revalidate_gpu_spatial_layer_source,
)`
- direct call: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `revalidate_gpu_spatial_layer_source`
- value/type reference: `landscout.stages.index_planning_regulation::_revalidate_zoning_source` via `revalidate_gpu_spatial_layer_source`
- direct call: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `gpu.revalidate_gpu_spatial_layer_source`
- direct call: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `gpu.revalidate_gpu_spatial_layer_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_revalidate_gpu_spatial_layer_source` | `landscout.sources.gpu_fr._revalidate_gpu_spatial_layer_source` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_revalidate_gpu_spatial_layer_sources`

**Purpose:** Implements `revalidate gpu spatial layer sources` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuValidatedSpatialLayerSource, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `inspected_layers` | positional-or-keyword | `tuple[GpuInspectedLayer, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(<br>        _revalidate_gpu_spatial_layer_source(<br>            planning_document,<br>            layer,<br>            verify_extraction_manifest=False,<br>        )<br>        for layer in inspected_layers<br>    )`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>            "Inspected GPU spatial layers must be an immutable tuple"<br>        )` under lexical guard `type(inspected_layers) is not tuple`.
  - `GpuSpatialInspectionError(<br>            "Every inspected GPU spatial layer must be a GpuInspectedLayer"<br>        )` under lexical guard `any(not isinstance(layer, GpuInspectedLayer) for layer in inspected_layers)`.
  - `GpuSpatialInspectionError(<br>            "Inspected GPU spatial layers contain a duplicate logical name"<br>        )` under lexical guard `len({layer.logical_name for layer in inspected_layers}) != len(inspected_layers)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_sources` via `_revalidate_gpu_spatial_layer_sources`
- value/type reference: `landscout.sources.gpu_fr::revalidate_gpu_spatial_layer_sources` via `_revalidate_gpu_spatial_layer_sources`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_gpu_planning_document_config_identity` | `landscout.sources.gpu_fr._validate_gpu_planning_document_config_identity` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_revalidate_gpu_spatial_layer_source` | `landscout.sources.gpu_fr._revalidate_gpu_spatial_layer_source` |

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
def _revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
    _validate_gpu_planning_document_config_identity(planning_document)
    if type(inspected_layers) is not tuple:
        raise GpuSpatialInspectionError(
            "Inspected GPU spatial layers must be an immutable tuple"
        )
    if any(not isinstance(layer, GpuInspectedLayer) for layer in inspected_layers):
        raise GpuSpatialInspectionError(
            "Every inspected GPU spatial layer must be a GpuInspectedLayer"
        )
    if len({layer.logical_name for layer in inspected_layers}) != len(inspected_layers):
        raise GpuSpatialInspectionError(
            "Inspected GPU spatial layers contain a duplicate logical name"
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `revalidate_gpu_spatial_layer_sources`

**Purpose:** Verify an ordered collection of extracted GPU spatial-layer sources.

**Exact signature**

```python
def revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuValidatedSpatialLayerSource, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `inspected_layers` | positional-or-keyword | `tuple[GpuInspectedLayer, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_revalidate_gpu_spatial_layer_sources(<br>            planning_document, inspected_layers<br>        )`
- Explicit raise paths:
  - `re-raise`.
  - `GpuSpatialInspectionError(<br>            "GPU spatial-layer batch input or validation is malformed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- import: `landscout.stages.enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`
- direct call: `landscout.stages.enrich_planning_features::_normalized_catalogs` via `revalidate_gpu_spatial_layer_sources`
- value/type reference: `landscout.stages.enrich_planning_features::_normalized_catalogs` via `revalidate_gpu_spatial_layer_sources`
- import: `landscout.stages.enrich_planning_zoning::<module>` via `from landscout.sources.gpu_fr import (
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    revalidate_gpu_spatial_layer_sources,
)`
- direct call: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `revalidate_gpu_spatial_layer_sources`
- value/type reference: `landscout.stages.enrich_planning_zoning::validate_normalized_planning_zoning_inputs` via `revalidate_gpu_spatial_layer_sources`
- direct call: `tests.unit.test_enrich_planning_features::test_batch_gpu_revalidation_rejects_malformed_layer_items` via `gpu_source_module.revalidate_gpu_spatial_layer_sources`
- direct call: `tests.unit.test_enrich_planning_features::test_batch_gpu_revalidation_rejects_malformed_planning_document` via `gpu_source_module.revalidate_gpu_spatial_layer_sources`
- direct call: `tests.unit.test_enrich_planning_features::test_batch_gpu_revalidation_rejects_duplicate_logical_name` via `gpu_source_module.revalidate_gpu_spatial_layer_sources`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_revalidate_gpu_spatial_layer_sources` | `landscout.sources.gpu_fr._revalidate_gpu_spatial_layer_sources` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_crs_text`

**Purpose:** Implements `crs text` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _crs_text(frame: gpd.GeoDataFrame) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `"UNKNOWN"`
  - `f"{authority[0]}:{authority[1]}" if authority else frame.crs.to_string()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_summarize_layer` via `_crs_text`
- value/type reference: `landscout.sources.gpu_fr::_summarize_layer` via `_crs_text`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `CRS.from_user_input(frame.crs).to_authority` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `frame.crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _crs_text(frame: gpd.GeoDataFrame) -> str:
    if frame.crs is None:
        return "UNKNOWN"
    authority = CRS.from_user_input(frame.crs).to_authority()
    return f"{authority[0]}:{authority[1]}" if authority else frame.crs.to_string()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_summarize_layer`

**Purpose:** Implements `summarize layer` within the file role: Discovers and verifies GPU config identity, document/archive/extraction recovery, globally unique spatial roles, written files, and provenance.

**Exact signature**

```python
def _summarize_layer(
    frame: gpd.GeoDataFrame,
    reference: GpuSpatialLayerReference,
    extraction: GpuExtraction,
) -> GpuLayerSummary:
```

- Exact decorators: none.
- Declared return annotation: `GpuLayerSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `reference` | positional-or-keyword | `GpuSpatialLayerReference` | `required` |
| `extraction` | positional-or-keyword | `GpuExtraction` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuLayerSummary(<br>        source_document_id=extraction.archive.document.document_id,<br>        source_archive_sha256=extraction.archive.sha256,<br>        source_layer=reference.source_layer,<br>        crs=_crs_text(frame),<br>        feature_count=len(frame),<br>        columns=tuple(str(column) for column in frame.columns),<br>        dtypes=tuple(<br>            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()<br>        ),<br>        null_counts=tuple(<br>            (str(column), int(frame[column].isna().sum())) for column in frame.columns<br>        ),<br>        geometry_types=geometry_types,<br>        null_geometry_count=int((~non_null).sum()),<br>        empty_geometry_count=int((non_null & geometry.is_empty).sum()),<br>        invalid_geometry_count=int(invalid.sum()),<br>    )`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>            f"GPU layer has no active geometry: {reference.source_layer}"<br>        )` under lexical guard `frame.geometry.name not in frame.columns`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_summarize_layer`
- value/type reference: `landscout.sources.gpu_fr::_revalidate_gpu_spatial_layer_source` via `_summarize_layer`
- direct call: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_summarize_layer`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `_summarize_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `geometry.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[non_null]<br>        .geom_type.value_counts()<br>        .sort_index()<br>        .items` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[non_null]<br>        .geom_type.value_counts()<br>        .sort_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[non_null]<br>        .geom_type.value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuLayerSummary` | `landscout.sources.gpu_fr.GpuLayerSummary` |
| `_crs_text` | `landscout.sources.gpu_fr._crs_text` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `(~non_null).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_null & geometry.is_empty).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid.sum` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.notna`<br>`geometry[non_null]<br>        .geom_type.value_counts()<br>        .sort_index()<br>        .items`<br>`geometry[non_null]<br>        .geom_type.value_counts()<br>        .sort_index`<br>`geometry[non_null]<br>        .geom_type.value_counts`<br>`(non_null & geometry.is_empty).sum` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
        for key, value in geometry[non_null]
        .geom_type.value_counts()
        .sort_index()
        .items()
    )
    return GpuLayerSummary(
        source_document_id=extraction.archive.document.document_id,
        source_archive_sha256=extraction.archive.sha256,
        source_layer=reference.source_layer,
        crs=_crs_text(frame),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `inspect_gpu_planning_document`

**Purpose:** Discover and inspect zoning/prescription layers without interpretation.

**Exact signature**

```python
def inspect_gpu_planning_document(
    extraction: GpuExtraction, config: GpuSourceConfig
) -> GpuPlanningDocument:
```

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `GpuExtraction` | `required` |
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuPlanningDocument(<br>        source_config=validated_config,<br>        source_config_sha256=_source_config_sha256(validated_config),<br>        extraction=extraction,<br>        all_spatial_layers=references,<br>        zoning=zoning,<br>        related_layers=tuple(related),<br>    )`
- Explicit raise paths:
  - `GpuSpatialInspectionError(<br>            "GPU planning source/config validation failed before inspection"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `inspect_gpu_planning_document`
- value/type reference: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `inspect_gpu_planning_document`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `inspect_gpu_planning_document`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_build_physical_chain` via `inspect_gpu_planning_document`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
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
)`
- direct call: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `inspect_gpu_planning_document`
- value/type reference: `tests.unit.test_gpu_fr::test_spatial_inventory_and_inspection_preserve_source_quality` via `inspect_gpu_planning_document`
- direct call: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `inspect_gpu_planning_document`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `inspect_gpu_planning_document`
- direct call: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `inspect_gpu_planning_document`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `inspect_gpu_planning_document`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_one_physical_layer_for_two_logical_roles` via `inspect_gpu_planning_document`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_one_physical_layer_for_two_logical_roles` via `inspect_gpu_planning_document`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_mutated_config_before_layer_discovery` via `inspect_gpu_planning_document`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_mutated_config_before_layer_discovery` via `inspect_gpu_planning_document`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_archive_byte_mutation_before_layer_discovery` via `inspect_gpu_planning_document`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_archive_byte_mutation_before_layer_discovery` via `inspect_gpu_planning_document`
- direct call: `tests.unit.test_gpu_fr::test_inspection_rejects_document_lineage_not_matching_config` via `inspect_gpu_planning_document`
- value/type reference: `tests.unit.test_gpu_fr::test_inspection_rejects_document_lineage_not_matching_config` via `inspect_gpu_planning_document`
- direct call: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `inspect_gpu_planning_document`
- value/type reference: `tests.unit.test_gpu_fr::test_planning_document_records_and_revalidates_exact_config_identity` via `inspect_gpu_planning_document`
- direct call: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `inspect_gpu_planning_document`
- value/type reference: `tests.unit.test_gpu_fr::test_source_complete_revalidation_rejects_coordinated_spatial_omission` via `inspect_gpu_planning_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.gpu_fr._validated_source_config` |
| `_validate_gpu_extraction_for_config` | `landscout.sources.gpu_fr._validate_gpu_extraction_for_config` |
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `discover_gpu_spatial_layers` | `landscout.sources.gpu_fr.discover_gpu_spatial_layers` |
| `_configured_logical_references` | `landscout.sources.gpu_fr._configured_logical_references` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_load_reference` | `landscout.sources.gpu_fr._load_reference` |
| `GpuInspectedLayer` | `landscout.sources.gpu_fr.GpuInspectedLayer` |
| `_summarize_layer` | `landscout.sources.gpu_fr._summarize_layer` |
| `related.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuPlanningDocument` | `landscout.sources.gpu_fr.GpuPlanningDocument` |
| `_source_config_sha256` | `landscout.sources.gpu_fr._source_config_sha256` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_source_config_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `related.append(<br>            GpuInspectedLayer(<br>                logical_name=logical_name,<br>                reference=reference,<br>                data=data,<br>                summary=_summarize_layer(data, reference, extraction),<br>            )<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def inspect_gpu_planning_document(
    extraction: GpuExtraction, config: GpuSourceConfig
) -> GpuPlanningDocument:
    """Discover and inspect zoning/prescription layers without interpretation."""

    try:
        validated_config = _validated_source_config(config)
        _validate_gpu_extraction_for_config(extraction, validated_config)
    except (GpuConfigError, GpuSpatialInspectionError) as error:
        raise GpuSpatialInspectionError(
            "GPU planning source/config validation failed before inspection"
        ) from error
    references = discover_gpu_spatial_layers(extraction)
    configured = _configured_logical_references(references, validated_config)
    configured_by_name = dict(configured)
    zoning_reference = configured_by_name["zoning"]
    zoning_data = _load_reference(zoning_reference)
    zoning = GpuInspectedLayer(
        logical_name="zoning",
        reference=zoning_reference,
        data=zoning_data,
        summary=_summarize_layer(zoning_data, zoning_reference, extraction),
    )
    related: list[GpuInspectedLayer] = []
    for logical_name, reference in configured[1:]:
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
        source_config=validated_config,
        source_config_sha256=_source_config_sha256(validated_config),
        extraction=extraction,
        all_spatial_layers=references,
        zoning=zoning,
        related_layers=tuple(related),
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `ingest_gpu_planning_document`

**Purpose:** High-level official GPU discovery, acquisition, extraction and inspection.

**Exact signature**

```python
def ingest_gpu_planning_document(
    config: GpuSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> GpuPlanningDocument:
```

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `GpuSourceConfig` | `required` |
| `cache_dir` | positional-or-keyword | `Path` | `DEFAULT_CACHE_DIR` |
| `timeout` | positional-or-keyword | `float` | `120.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `inspect_gpu_planning_document(extraction, config)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
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
)`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `discover_current_gpu_document` | `landscout.sources.gpu_fr.discover_current_gpu_document` |
| `download_gpu_document` | `landscout.sources.gpu_fr.download_gpu_document` |
| `extract_gpu_document` | `landscout.sources.gpu_fr.extract_gpu_document` |
| `inspect_gpu_planning_document` | `landscout.sources.gpu_fr.inspect_gpu_planning_document` |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `finite_numeric_vocabulary`

**Purpose:** Return deterministic raw value counts for inspection-only reporting.

**Exact signature**

```python
def finite_numeric_vocabulary(
    frame: gpd.GeoDataFrame, column: str
) -> tuple[tuple[str, int], ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[str, int], ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(sorted(result, key=lambda item: item[0]))`
- Explicit raise paths:
  - `GpuSpatialInspectionError(f"Cannot inspect GPU attribute: {column}")` under lexical guard `column not in frame.columns or column == frame.geometry.name`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `GpuSpatialInspectionError` | `landscout.sources.gpu_fr.GpuSpatialInspectionError` |
| `frame[column].value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `counts.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isnan` | `math.isnan` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `result.append((label, int(count)))` |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `EXTRACTION_MANIFEST_SCHEMA_VERSION`.
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
"""Official Géoportail de l'Urbanisme document ingestion for France.

This source adapter discovers one currently effective planning document, caches
its official archive, extracts it safely, and reports the source schema.  It
deliberately does not interpret planning rules or classify parcel suitability.
"""

from __future__ import annotations

import json
import math
import re
import shutil
import stat
import sys
import unicodedata
import zipfile
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
from numbers import Integral
from pathlib import Path, PurePosixPath, PureWindowsPath
from shutil import copy2, copyfileobj
from typing import Annotated, Any, Literal
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urljoin, urlparse
from xml.etree import ElementTree

import geopandas as gpd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
)
from pyproj import CRS

from landscout.common.safe_http import open_safe_https
from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)
from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml

DEFAULT_CONFIG_PATH = Path("configs/sources/gpu_fr.yaml")
DEFAULT_CACHE_DIR = Path("data/cache/gpu")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
USER_AGENT = "LandScout-AI/0.1"
EXTRACTION_MANIFEST_NAME = ".landscout-gpu-extraction.json"
EXTRACTION_MANIFEST_SCHEMA_VERSION = 2

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
CommuneCode = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[0-9]{5}$"),
]
DownloadStrategy = Literal["partition"]
LogicalLayerName = Literal[
    "zoning",
    "prescription_surface",
    "prescription_line",
    "prescription_point",
    "information_surface",
    "information_line",
    "information_point",
]
FileCategory = Literal[
    "SPATIAL_DATA", "METADATA", "WRITTEN_REGULATION", "OTHER_ATTACHMENT"
]
GpuOfficialSourceIdentity = Literal["G\u00e9oportail de l'Urbanisme"]


class GpuApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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


class GpuDownloadConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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


class GpuCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    max_age_hours: float = Field(ge=0, allow_inf_nan=False)

    @field_validator("max_age_hours", mode="before")
    @classmethod
    def _strict_finite_number(cls, value: object) -> object:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or type(value) not in {int, float}
        ):
            raise ValueError("max_age_hours must be an exact finite number")
        if not math.isfinite(value):
            raise ValueError("max_age_hours must be finite")
        return value


class GpuPilotConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    commune_code: CommuneCode


class GpuLogicalLayerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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


class GpuSpatialLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    zoning: GpuLogicalLayerConfig
    prescription_surface: GpuLogicalLayerConfig
    prescription_line: GpuLogicalLayerConfig
    prescription_point: GpuLogicalLayerConfig
    information_surface: GpuLogicalLayerConfig
    information_line: GpuLogicalLayerConfig
    information_point: GpuLogicalLayerConfig


class GpuSourceConfig(BaseModel):
    """Strict configuration for official French GPU ingestion."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: GpuOfficialSourceIdentity
    portal: GpuOfficialSourceIdentity
    country: Literal["FR"]
    api: GpuApiConfig
    download: GpuDownloadConfig
    cache: GpuCacheConfig
    pilot: GpuPilotConfig
    spatial_layers: GpuSpatialLayersConfig


class GpuError(RuntimeError):
    """Base class for controlled GPU source failures."""


class GpuConfigError(GpuError):
    """Raised when GPU source configuration is invalid."""


class GpuDiscoveryError(GpuError):
    """Raised when the current planning document cannot be resolved safely."""


class GpuDownloadError(GpuError):
    """Raised when the GPU archive cannot be downloaded or cached safely."""


class GpuArchiveError(GpuError):
    """Raised when a GPU archive or extraction is corrupt or unsafe."""


class GpuSpatialInspectionError(GpuError):
    """Raised when required GPU spatial layers cannot be inspected safely."""


@dataclass(frozen=True)
class GpuWrittenFile:
    filename: str
    title: str | None
    document_path: str | None
    source_url: str | None


@dataclass(frozen=True)
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


@dataclass(frozen=True)
class GpuArchiveDownload:
    document: GpuDocumentMetadata
    download_timestamp: str
    filename: str
    archive_format: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool


@dataclass(frozen=True)
class GpuExtractedFile:
    relative_path: str
    file_type: str
    size_bytes: int
    sha256: str
    category: FileCategory


@dataclass(frozen=True)
class GpuExtraction:
    archive: GpuArchiveDownload
    extraction_root: Path
    files: tuple[GpuExtractedFile, ...]
    standard_models: tuple[str, ...]
    cache_hit: bool


@dataclass(frozen=True)
class GpuSpatialLayerReference:
    dataset_path: Path
    source_layer: str
    driver: str


@dataclass(frozen=True)
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


@dataclass(frozen=True)
class GpuInspectedLayer:
    logical_name: LogicalLayerName
    reference: GpuSpatialLayerReference
    data: gpd.GeoDataFrame
    summary: GpuLayerSummary


@dataclass(frozen=True)
class GpuSpatialSourceFileIntegrity:
    """One verified physical member of an extracted GPU spatial dataset."""

    relative_path: str
    file_type: str
    size_bytes: int
    sha256: str
    category: str


@dataclass(frozen=True)
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


@dataclass(frozen=True)
class GpuPlanningDocument:
    source_config: GpuSourceConfig
    source_config_sha256: str
    extraction: GpuExtraction
    all_spatial_layers: tuple[GpuSpatialLayerReference, ...]
    zoning: GpuInspectedLayer
    related_layers: tuple[GpuInspectedLayer, ...]


def _normalize_words(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_value = "".join(
        char for char in decomposed if not unicodedata.combining(char)
    )
    return "_".join(re.findall(r"[a-z0-9]+", ascii_value.casefold()))


def load_gpu_source_config(path: Path = DEFAULT_CONFIG_PATH) -> GpuSourceConfig:
    """Load and validate the strict GPU source configuration."""

    if not path.is_file():
        raise GpuConfigError(f"GPU source configuration does not exist: {path}")
    try:
        payload = loads_strict_yaml(path.read_bytes())
        if type(payload) is not dict:
            raise TypeError("GPU source configuration must be a mapping")
        return GpuSourceConfig.model_validate(payload)
    except (OSError, TypeError, StrictYamlError, ValidationError) as error:
        raise GpuConfigError(f"Invalid GPU source configuration: {path}") from error


def _validated_source_config(config: object) -> GpuSourceConfig:
    try:
        if type(config) is not GpuSourceConfig:
            raise TypeError("GPU source config type is invalid")
        return GpuSourceConfig.model_validate(config.model_dump(mode="python"))
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise GpuConfigError(
            "GPU source config no longer satisfies the official origin contract"
        ) from error


def _source_config_sha256(config: object) -> str:
    """Return the private canonical identity of one validated GPU config."""

    validated = _validated_source_config(config)
    try:
        payload = json.dumps(
            {
                "domain": "landscout.gpu.source_config",
                "config": validated.model_dump(mode="json"),
            },
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise GpuConfigError("GPU source config cannot be serialized safely") from error
    return sha256(payload).hexdigest()


def build_gpu_partition(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
    validated_config = _validated_source_config(config)
    code = commune_code or validated_config.pilot.commune_code
    if not isinstance(code, str) or re.fullmatch(r"[0-9]{5}", code) is None:
        raise GpuConfigError("GPU commune code must contain exactly five digits")
    return validated_config.download.partition_template.format(code_insee=code)


def _api_url(config: GpuSourceConfig, path: str) -> str:
    return urljoin(f"{str(config.api.base_url).rstrip('/')}/", path.lstrip("/"))


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


def build_gpu_partition_download_url(
    config: GpuSourceConfig, commune_code: str | None = None
) -> str:
    validated_config = _validated_source_config(config)
    partition = quote(build_gpu_partition(validated_config, commune_code), safe="")
    return _api_url(validated_config, f"document/download-by-partition/{partition}")


def _request_json(url: str, timeout: float) -> Any:
    try:
        with open_safe_https(
            url,
            timeout=timeout,
            headers={"Accept": "application/json", "User-Agent": USER_AGENT},
        ) as response:
            return loads_strict_json(response.read())
    except (HTTPError, URLError, OSError, StrictJsonError) as error:
        raise GpuDiscoveryError(f"GPU metadata request failed: {url}") from error


def _required_string(payload: dict[str, Any], key: str, label: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise GpuDiscoveryError(f"GPU {label} is missing or invalid")
    return value


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
            f"document/{quote(document_id, safe='')}/files/{quote(filename, safe='')}",
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
        raise GpuDiscoveryError(
            "GPU document details do not match the selected document"
        )
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
        effective_status=_required_string(
            details, "effectiveStatus", "effective status"
        ),
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


_WINDOWS_RESERVED_BASENAMES = {
    "con",
    "prn",
    "aux",
    "nul",
    *(f"com{index}" for index in range(1, 10)),
    *(f"lpt{index}" for index in range(1, 10)),
}


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


def _validate_gpu_document_for_config(
    document: GpuDocumentMetadata, config: GpuSourceConfig
) -> str:
    if type(document) is not GpuDocumentMetadata:
        raise GpuDownloadError("GPU document metadata object is invalid")
    if document.provider != config.provider or document.portal != config.portal:
        raise GpuDownloadError(
            "GPU document provider/portal does not match configuration"
        )
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
                ord(character) < 32 or ord(character) == 127 for character in filename
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
    if document.document_family != "DU" or (
        type(document.document_type) is not str
        or not document.document_type
        or document.document_type != document.document_type.strip()
        or any(
            ord(character) < 32 or ord(character) == 127
            for character in document.document_type
        )
    ):
        raise GpuDownloadError("GPU document family is not a planning document")
    if (
        document.status != "document.production"
        or document.legal_status != "APPROVED"
        or document.effective_status != "EN_VIGUEUR"
    ):
        raise GpuDownloadError("GPU document is not current, approved, and in force")
    if not isinstance(document.source_url, str) or document.source_url != expected_url:
        raise GpuDownloadError(
            "GPU document source URL is not the official partition URL"
        )
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


def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(DOWNLOAD_CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def _is_link_or_junction(path: Path) -> bool:
    return path.is_symlink() or path.is_junction()


def _validate_gpu_archive_download(
    download: GpuArchiveDownload,
) -> tuple[str, ...]:
    if type(download) is not GpuArchiveDownload:
        raise GpuArchiveError("GPU archive download object is invalid")
    if type(download.document) is not GpuDocumentMetadata:
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
            raise GpuArchiveError(
                f"Special files are not allowed in GPU archive: {raw_name}"
            )

        destination = PurePosixPath(raw_name.replace("\\", "/"))
        parts = tuple(part for part in destination.parts if part not in {"", "."})
        if not parts:
            raise GpuArchiveError(
                f"GPU ZIP member has no extraction target: {raw_name}"
            )
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
        sorted(
            (destination.as_posix() for _, destination in destinations),
            key=str.casefold,
        )
    )


def _document_identity(document: GpuDocumentMetadata) -> dict[str, Any]:
    result = asdict(document)
    result["written_files"] = [asdict(item) for item in document.written_files]
    return result


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


def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)


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
    recovery_paths = _cache_recovery_paths(archive_path, metadata_path)
    if any(path.exists() or _is_link_or_junction(path) for path in recovery_paths):
        raise GpuDownloadError(
            "GPU cache recovery backup already exists; manual recovery is required"
        )


def _prepare_temporary_cache_file(path: Path) -> None:
    try:
        if _is_link_or_junction(path):
            raise GpuDownloadError("GPU cache temporary path is a link or junction")
        if path.exists():
            if not path.is_file():
                raise GpuDownloadError("GPU cache temporary path is not a regular file")
            path.unlink()
    except GpuDownloadError:
        raise
    except OSError as error:
        raise GpuDownloadError(
            "GPU cache temporary path cannot be prepared safely"
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
        raise GpuDownloadError(
            "GPU cache temporary files could not be cleaned safely"
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


def _load_cached_archive(
    archive_path: Path,
    metadata_path: Path,
    document: GpuDocumentMetadata,
    max_age_hours: float,
) -> GpuArchiveDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        payload = loads_strict_json_object(metadata_path.read_bytes())
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
            and type(payload.get("file_size")) is int
            and payload["file_size"] == size
            and payload.get("sha256") == checksum
            and type(payload.get("member_count")) is int
            and payload["member_count"] == len(members)
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
        StrictJsonError,
        GpuArchiveError,
    ):
        return None


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
            temporary_archive.open("xb") as output,
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
        with temporary_metadata.open("x", encoding="utf-8") as output:
            output.write(
                json.dumps(lineage, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
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


def _inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    if _is_link_or_junction(root) or not root.is_dir():
        raise GpuArchiveError(f"GPU extraction root is not a regular directory: {root}")
    for path in root.rglob("*"):
        if _is_link_or_junction(path):
            raise GpuArchiveError(f"Extracted GPU symbolic link is forbidden: {path}")
        if not path.is_file() and not path.is_dir():
            raise GpuArchiveError(
                f"Extracted GPU special filesystem entry is forbidden: {path}"
            )
    files: list[GpuExtractedFile] = []
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=str):
        if path.parent == root and path.name == EXTRACTION_MANIFEST_NAME:
            continue
        resolved = path.resolve()
        try:
            relative = resolved.relative_to(root.resolve())
        except ValueError as error:
            raise GpuArchiveError(
                f"Extracted GPU file escapes cache: {path}"
            ) from error
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


def _validate_extraction_manifest(
    root: Path, download: GpuArchiveDownload
) -> tuple[GpuExtractedFile, ...]:
    marker = root / EXTRACTION_MANIFEST_NAME
    if _is_link_or_junction(marker) or not marker.is_file():
        raise GpuArchiveError("GPU extraction manifest is missing or unsafe")
    try:
        payload = loads_strict_json_object(marker.read_bytes())
    except (OSError, StrictJsonError) as error:
        raise GpuArchiveError("GPU extraction manifest is unreadable") from error
    if set(payload) != {
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


def _remove_extraction_path(path: Path) -> None:
    if path.is_junction():
        path.rmdir()
    elif path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.exists():
        shutil.rmtree(path)


def _cleanup_temporary_extraction_directory(
    path: Path,
    primary_error: BaseException | None,
) -> None:
    try:
        _remove_extraction_path(path)
    except OSError as error:
        if primary_error is None:
            raise GpuArchiveError(
                "GPU extraction temporary directory could not be cleaned safely"
            ) from error


def _require_no_extraction_recovery_material(root: Path) -> None:
    backup = root.with_name(f"{root.name}.bak")
    if backup.exists() or _is_link_or_junction(backup):
        raise GpuArchiveError(
            "GPU extraction recovery backup exists; manual recovery is required"
        )


def _prepare_temporary_extraction_directory(path: Path) -> None:
    try:
        if _is_link_or_junction(path):
            raise GpuArchiveError("GPU extraction temporary path is a link or junction")
        if path.exists():
            raise GpuArchiveError(
                "GPU extraction temporary path already exists; manual recovery is required"
            )
        path.mkdir()
    except GpuArchiveError:
        raise
    except OSError as error:
        raise GpuArchiveError(
            "GPU extraction temporary path cannot be prepared safely"
        ) from error


def _publish_extraction_directory(temporary_root: Path, root: Path) -> None:
    backup = root.with_name(f"{root.name}.bak")
    _require_no_extraction_recovery_material(root)
    old_moved = False
    if root.exists() or _is_link_or_junction(root):
        try:
            shutil.move(str(root), str(backup))
            old_moved = True
        except OSError as error:
            raise GpuArchiveError(
                "GPU extraction backup publication failed before replacement"
            ) from error
    try:
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


def extract_gpu_document(
    download: GpuArchiveDownload, cache_dir: Path = DEFAULT_CACHE_DIR
) -> GpuExtraction:
    """Safely extract a validated GPU ZIP into a content-addressed cache."""

    _validate_gpu_archive_download(download)
    root = cache_dir / "x" / download.sha256[:16]
    _require_no_extraction_recovery_material(root)
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
    _prepare_temporary_extraction_directory(temporary_root)
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
        with marker.open("x", encoding="utf-8") as output:
            output.write(
                json.dumps(_manifest_payload(download, files), indent=2, sort_keys=True)
                + "\n"
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
        _cleanup_temporary_extraction_directory(
            temporary_root,
            sys.exception(),
        )


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
                references.append(GpuSpatialLayerReference(path, raw_name, "GPKG"))
    for path in shp_paths:
        references.append(GpuSpatialLayerReference(path, path.stem, "ESRI Shapefile"))
    if not references:
        raise GpuSpatialInspectionError(
            "GPU document contains no supported spatial data"
        )
    unique = {(item.dataset_path.resolve(), item.source_layer) for item in references}
    if len(unique) != len(references):
        raise GpuSpatialInspectionError("GPU document exposes duplicate spatial layers")
    return tuple(
        sorted(references, key=lambda item: (str(item.dataset_path), item.source_layer))
    )


def _layer_config(
    config: GpuSourceConfig, logical_name: LogicalLayerName
) -> GpuLogicalLayerConfig:
    return getattr(config.spatial_layers, logical_name)


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


_GPU_LOGICAL_LAYER_NAMES: tuple[LogicalLayerName, ...] = (
    "zoning",
    "prescription_surface",
    "prescription_line",
    "prescription_point",
    "information_surface",
    "information_line",
    "information_point",
)


def _configured_logical_references(
    references: tuple[GpuSpatialLayerReference, ...],
    config: GpuSourceConfig,
) -> tuple[tuple[LogicalLayerName, GpuSpatialLayerReference], ...]:
    if type(references) is not tuple or any(
        type(reference) is not GpuSpatialLayerReference for reference in references
    ):
        raise GpuSpatialInspectionError(
            "GPU spatial-layer inventory must be an exact immutable tuple"
        )
    selected: list[tuple[LogicalLayerName, GpuSpatialLayerReference]] = []
    for logical_name in _GPU_LOGICAL_LAYER_NAMES:
        reference = _discover_logical_layer(
            references,
            config,
            logical_name,
            required=logical_name == "zoning",
        )
        if reference is not None:
            selected.append((logical_name, reference))
    physical_roles = [
        (reference.dataset_path.resolve(), reference.source_layer)
        for _, reference in selected
    ]
    if len(physical_roles) != len(set(physical_roles)):
        raise GpuSpatialInspectionError(
            "Two GPU logical roles resolve to the same physical layer"
        )
    return tuple(selected)


def _validate_gpu_extraction_for_config(
    extraction: object,
    config: GpuSourceConfig,
) -> None:
    try:
        if type(extraction) is not GpuExtraction:
            raise GpuSpatialInspectionError(
                "GPU extraction must be exactly a GpuExtraction"
            )
        if type(extraction.archive) is not GpuArchiveDownload:
            raise GpuSpatialInspectionError(
                "GPU extraction archive must be exactly a GpuArchiveDownload"
            )
        if type(extraction.archive.document) is not GpuDocumentMetadata:
            raise GpuSpatialInspectionError(
                "GPU extraction document must be exactly a GpuDocumentMetadata"
            )
        _validate_gpu_document_for_config(extraction.archive.document, config)
        _validate_gpu_archive_download(extraction.archive)
        root, _ = _validated_spatial_root(extraction)
        manifest_files = _validate_extraction_manifest(root, extraction.archive)
        if extraction.files != manifest_files:
            raise GpuSpatialInspectionError(
                "GPU extraction inventory differs from its verified manifest"
            )
        if type(extraction.standard_models) is not tuple or (
            extraction.standard_models != _discover_standard_models(root)
        ):
            raise GpuSpatialInspectionError(
                "GPU extraction standard-model inventory differs from source"
            )
        _validate_gpu_archive_download(extraction.archive)
    except GpuSpatialInspectionError:
        raise
    except (GpuArchiveError, GpuDownloadError) as error:
        raise GpuSpatialInspectionError(
            "GPU extraction does not match its configured physical source"
        ) from error
    except Exception as error:
        raise GpuSpatialInspectionError(
            "GPU extraction/config lineage cannot be validated safely"
        ) from error


def _validate_gpu_planning_document_config_identity(
    planning_document: object,
) -> GpuSourceConfig:
    try:
        if type(planning_document) is not GpuPlanningDocument:
            raise GpuSpatialInspectionError(
                "planning_document must be exactly a GpuPlanningDocument"
            )
        if (
            type(planning_document.extraction) is not GpuExtraction
            or type(planning_document.extraction.archive) is not GpuArchiveDownload
        ):
            raise GpuSpatialInspectionError(
                "GPU planning-document extraction lineage is malformed"
            )
        config = _validated_source_config(planning_document.source_config)
        checksum = planning_document.source_config_sha256
        if (
            type(checksum) is not str
            or re.fullmatch(r"[0-9a-f]{64}", checksum) is None
            or checksum != _source_config_sha256(config)
        ):
            raise GpuSpatialInspectionError(
                "GPU planning-document config SHA256 differs"
            )
        _validate_gpu_document_for_config(
            planning_document.extraction.archive.document,
            config,
        )
        root, _ = _validated_spatial_root(planning_document.extraction)
        manifest_files = _validate_extraction_manifest(
            root,
            planning_document.extraction.archive,
        )
        if planning_document.extraction.files != manifest_files:
            raise GpuSpatialInspectionError(
                "GPU extraction inventory differs from its verified manifest"
            )
        physical_references = discover_gpu_spatial_layers(planning_document.extraction)
        if planning_document.all_spatial_layers != physical_references:
            raise GpuSpatialInspectionError(
                "GPU planning-document spatial inventory differs from its "
                "physical extraction"
            )
        configured = _configured_logical_references(
            planning_document.all_spatial_layers,
            config,
        )
        inspected = (planning_document.zoning, *planning_document.related_layers)
        if type(planning_document.related_layers) is not tuple or any(
            type(layer) is not GpuInspectedLayer for layer in inspected
        ):
            raise GpuSpatialInspectionError(
                "GPU planning-document inspected layers are malformed"
            )
        actual = tuple((layer.logical_name, layer.reference) for layer in inspected)
        if actual != configured:
            raise GpuSpatialInspectionError(
                "GPU planning-document logical roles differ from its config"
            )
        return config
    except GpuSpatialInspectionError:
        raise
    except (GpuArchiveError, GpuConfigError, GpuDownloadError) as error:
        raise GpuSpatialInspectionError(
            "GPU planning-document source config is invalid"
        ) from error
    except Exception as error:
        raise GpuSpatialInspectionError(
            "GPU planning-document config identity cannot be validated safely"
        ) from error


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
                candidate.resolve(strict=True).relative_to(root_resolved).as_posix()
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


def _same_spatial_crs(left: object, right: object) -> bool:
    try:
        return bool(CRS.from_user_input(left).equals(CRS.from_user_input(right)))
    except Exception as error:
        raise GpuSpatialInspectionError(
            "GPU spatial source CRS cannot be validated"
        ) from error


def _compare_inspected_spatial_layer(
    inspected: GpuInspectedLayer,
    reread: gpd.GeoDataFrame,
) -> None:
    loaded = inspected.data
    try:
        if not isinstance(loaded, gpd.GeoDataFrame) or not isinstance(
            reread, gpd.GeoDataFrame
        ):
            raise GpuSpatialInspectionError("GPU spatial layer must be a GeoDataFrame")
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
        if (
            not loaded[attributes]
            .reset_index(drop=True)
            .equals(reread[attributes].reset_index(drop=True))
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


def _revalidate_gpu_spatial_layer_source(
    planning_document: GpuPlanningDocument,
    inspected_layer: GpuInspectedLayer,
    *,
    verify_extraction_manifest: bool,
) -> GpuValidatedSpatialLayerSource:
    """Verify and freshly reload one extracted GPU spatial-layer source."""

    try:
        if (
            type(planning_document) is not GpuPlanningDocument
            or type(inspected_layer) is not GpuInspectedLayer
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
            _validate_gpu_planning_document_config_identity(planning_document)
        reference = inspected_layer.reference
        relative, family = _spatial_source_family(
            reference, planning_document.extraction
        )
        with_fids = pyogrio.read_dataframe(
            reference.dataset_path,
            layer=reference.source_layer,
            fid_as_index=True,
        )
        if not with_fids.index.is_unique or any(
            isinstance(value, bool) or not isinstance(value, Integral) or int(value) < 0
            for value in with_fids.index
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


def _revalidate_gpu_spatial_layer_sources(
    planning_document: GpuPlanningDocument,
    inspected_layers: tuple[GpuInspectedLayer, ...],
) -> tuple[GpuValidatedSpatialLayerSource, ...]:
    _validate_gpu_planning_document_config_identity(planning_document)
    if type(inspected_layers) is not tuple:
        raise GpuSpatialInspectionError(
            "Inspected GPU spatial layers must be an immutable tuple"
        )
    if any(not isinstance(layer, GpuInspectedLayer) for layer in inspected_layers):
        raise GpuSpatialInspectionError(
            "Every inspected GPU spatial layer must be a GpuInspectedLayer"
        )
    if len({layer.logical_name for layer in inspected_layers}) != len(inspected_layers):
        raise GpuSpatialInspectionError(
            "Inspected GPU spatial layers contain a duplicate logical name"
        )
    return tuple(
        _revalidate_gpu_spatial_layer_source(
            planning_document,
            layer,
            verify_extraction_manifest=False,
        )
        for layer in inspected_layers
    )


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


def _crs_text(frame: gpd.GeoDataFrame) -> str:
    if frame.crs is None:
        return "UNKNOWN"
    authority = CRS.from_user_input(frame.crs).to_authority()
    return f"{authority[0]}:{authority[1]}" if authority else frame.crs.to_string()


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
        for key, value in geometry[non_null]
        .geom_type.value_counts()
        .sort_index()
        .items()
    )
    return GpuLayerSummary(
        source_document_id=extraction.archive.document.document_id,
        source_archive_sha256=extraction.archive.sha256,
        source_layer=reference.source_layer,
        crs=_crs_text(frame),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=geometry_types,
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int(invalid.sum()),
    )


def inspect_gpu_planning_document(
    extraction: GpuExtraction, config: GpuSourceConfig
) -> GpuPlanningDocument:
    """Discover and inspect zoning/prescription layers without interpretation."""

    try:
        validated_config = _validated_source_config(config)
        _validate_gpu_extraction_for_config(extraction, validated_config)
    except (GpuConfigError, GpuSpatialInspectionError) as error:
        raise GpuSpatialInspectionError(
            "GPU planning source/config validation failed before inspection"
        ) from error
    references = discover_gpu_spatial_layers(extraction)
    configured = _configured_logical_references(references, validated_config)
    configured_by_name = dict(configured)
    zoning_reference = configured_by_name["zoning"]
    zoning_data = _load_reference(zoning_reference)
    zoning = GpuInspectedLayer(
        logical_name="zoning",
        reference=zoning_reference,
        data=zoning_data,
        summary=_summarize_layer(zoning_data, zoning_reference, extraction),
    )
    related: list[GpuInspectedLayer] = []
    for logical_name, reference in configured[1:]:
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
        source_config=validated_config,
        source_config_sha256=_source_config_sha256(validated_config),
        extraction=extraction,
        all_spatial_layers=references,
        zoning=zoning,
        related_layers=tuple(related),
    )


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
