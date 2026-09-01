# `src/landscout/sources/ign_bdtopo_fr.py`

## File identity

- Repository path: `src/landscout/sources/ign_bdtopo_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: official source acquisition and physical authority
- Responsibility: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.
- Source SHA256: `598df901cd8dfe543595f22ff511b511a196f345474acd6355d7929a7a512101`

## 1. STEP 7F.1A.4 contract delta

- Binds four globally unique configured IGN roles, strict marker/inventory authority, Windows-compatible archive destinations, and fresh source-complete role objects; the internal extraction marker advances from schema 2 to 3.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

The file belongs to the **source adapter** layer and **official source acquisition and physical authority** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import os`
- `import re`
- `import shutil`
- `import sys`
- `import unicodedata`
- `from dataclasses import dataclass`
- `from datetime import UTC, date, datetime`
- `from hashlib import md5, sha256`
- `from pathlib import Path, PurePosixPath, PureWindowsPath`
- `from shutil import copy2, copyfileobj`
- `from typing import Annotated, Any, Literal, Self`
- `from urllib.error import HTTPError, URLError`
- `from urllib.parse import unquote, urlparse`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import py7zr`
- `import pyogrio`
- `from py7zr.exceptions import ArchiveError`
- `from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StrictBool,
    StringConstraints,
    ValidationError,
    field_validator,
    model_validator,
)`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.common.safe_http import open_safe_https`
- `from landscout.common.strict_json import loads_strict_json_object`
- `from landscout.common.strict_yaml import loads_strict_yaml`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `DEFAULT_CONFIG_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEFAULT_CONFIG_PATH = Path("configs/sources/ign_bdtopo_fr.yaml")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DEFAULT_CACHE_DIR`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEFAULT_CACHE_DIR = Path("data/cache/ign_bdtopo")
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

### `SPATIAL_ROLE`

- Category: module constant or closed domain.
- Exact declaration:

```python
SPATIAL_ROLE = "PROXY_GEOMETRY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `COVERAGE_SPATIAL_ROLE`

- Category: module constant or closed domain.
- Exact declaration:

```python
COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SpatialRole`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
SpatialRole = Literal["PROXY_GEOMETRY"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CoverageSpatialRole`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
CoverageSpatialRole = Literal["SOURCE_COVERAGE_BOUNDARY"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `LogicalLayerName`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
LogicalLayerName = Literal[
    "electric_lines",
    "transformation_posts",
    "road_segments",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `Projection`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
Projection = Literal["EPSG:2154"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PackageFormat`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
PackageFormat = Literal["GPKG"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ArchiveFormat`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
ArchiveFormat = Literal["7z"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ChecksumAlgorithm`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
ChecksumAlgorithm = Literal["md5", "sha256"]
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

### `DepartmentCode`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
DepartmentCode = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=r"^(?:[0-9]{2}|2A|2B|97[1-6])$",
    ),
]
```

- Qualified consumers:
  - import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
  - import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`

### `EditionString`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
EditionString = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^\d{4}-\d{2}-\d{2}$"),
]
```

- Qualified consumers:
  - import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
  - import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`

### `HexChecksum`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
HexChecksum = Annotated[
    str,
    StringConstraints(strip_whitespace=True, to_lower=True, pattern=r"^[0-9a-fA-F]+$"),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CanonicalSha256`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
CanonicalSha256 = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^[0-9a-f]{64}$"),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `StrictPositiveInt`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `StrictNonNegativeFloat`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
StrictNonNegativeFloat = Annotated[
    float,
    Field(strict=True, ge=0, allow_inf_nan=False),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_WINDOWS_FORBIDDEN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_WINDOWS_FORBIDDEN = frozenset('<>:"/\\|?*')
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_WINDOWS_RESERVED`

- Category: module constant or closed domain.
- Exact declaration:

```python
_WINDOWS_RESERVED = frozenset(
    {
        "con",
        "prn",
        "aux",
        "nul",
        "clock$",
        *(f"com{index}" for index in range(1, 10)),
        *(f"lpt{index}" for index in range(1, 10)),
        "com¹",
        "com²",
        "com³",
        "lpt¹",
        "lpt²",
        "lpt³",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `IgnBdTopoLogicalLayerConfig`

**Source purpose:** Catalogue class label and normalized tokens used for layer discovery.

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

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_matching_layers` via `IgnBdTopoLogicalLayerConfig`

**Exact class source**

```python
class IgnBdTopoLogicalLayerConfig(BaseModel):
    """Catalogue class label and normalized tokens used for layer discovery."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    class_label: NonEmptyString
    match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)

    @field_validator("match_tokens")
    @classmethod
    def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(token) for token in value)
        if any(not token for token in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(set(normalized)) != len(normalized):
            raise ValueError("Layer match tokens must be unique after normalization")
        return value
```

### `IgnBdTopoLogicalLayersConfig`

**Source purpose:** Defines `IgnBdTopoLogicalLayersConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `electric_lines` | `IgnBdTopoLogicalLayerConfig` | `required` | `electric_lines: IgnBdTopoLogicalLayerConfig` |
| `transformation_posts` | `IgnBdTopoLogicalLayerConfig` | `required` | `transformation_posts: IgnBdTopoLogicalLayerConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`

**Exact class source**

```python
class IgnBdTopoLogicalLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    electric_lines: IgnBdTopoLogicalLayerConfig
    transformation_posts: IgnBdTopoLogicalLayerConfig

    @model_validator(mode="after")
    def _different_token_sets(self) -> Self:
        electric = {
            _normalize_words(token) for token in self.electric_lines.match_tokens
        }
        posts = {
            _normalize_words(token) for token in self.transformation_posts.match_tokens
        }
        if electric == posts:
            raise ValueError("Logical layers must use different match tokens")
        return self
```

### `IgnBdTopoDepartmentLayerConfig`

**Source purpose:** Configured department layer and its observed identity field.

- Exact decorators: none.
- Exact bases: `IgnBdTopoLogicalLayerConfig`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `department_code_field` | `NonEmptyString` | `required` | `department_code_field: NonEmptyString` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`

**Exact class source**

```python
class IgnBdTopoDepartmentLayerConfig(IgnBdTopoLogicalLayerConfig):
    """Configured department layer and its observed identity field."""

    department_code_field: NonEmptyString
```

### `IgnBdTopoAccessConfig`

**Source purpose:** Configured factual transport layers loaded outside extraction metadata.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `road_segments` | `IgnBdTopoLogicalLayerConfig` | `required` | `road_segments: IgnBdTopoLogicalLayerConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class IgnBdTopoAccessConfig(BaseModel):
    """Configured factual transport layers loaded outside extraction metadata."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    road_segments: IgnBdTopoLogicalLayerConfig
```

### `IgnBdTopoCoverageConfig`

**Source purpose:** Defines `IgnBdTopoCoverageConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `department_layer` | `IgnBdTopoDepartmentLayerConfig` | `required` | `department_layer: IgnBdTopoDepartmentLayerConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`

**Exact class source**

```python
class IgnBdTopoCoverageConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    department_layer: IgnBdTopoDepartmentLayerConfig
```

### `IgnBdTopoSourceConfig`

**Source purpose:** Strict, reproducible description of one official IGN package.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `provider` | `Literal["Institut national de l'information géographique et forestière (IGN)"]` | `required` | `provider: Literal[<br>        "Institut national de l'information géographique et forestière (IGN)"<br>    ]` |
| `product` | `Literal['BD TOPO']` | `required` | `product: Literal["BD TOPO"]` |
| `department_code` | `DepartmentCode` | `required` | `department_code: DepartmentCode` |
| `edition` | `EditionString` | `required` | `edition: EditionString` |
| `product_version` | `NonEmptyString \| None` | `None` | `product_version: NonEmptyString \| None = None` |
| `projection` | `Projection` | `required` | `projection: Projection` |
| `format` | `PackageFormat` | `required` | `format: PackageFormat` |
| `archive_format` | `ArchiveFormat` | `required` | `archive_format: ArchiveFormat` |
| `source_url` | `HttpUrl` | `required` | `source_url: HttpUrl` |
| `checksum_url` | `HttpUrl \| None` | `None` | `checksum_url: HttpUrl \| None = None` |
| `official_checksum_algorithm` | `ChecksumAlgorithm \| None` | `None` | `official_checksum_algorithm: ChecksumAlgorithm \| None = None` |
| `official_checksum` | `HexChecksum \| None` | `None` | `official_checksum: HexChecksum \| None = None` |
| `expected_archive_size_bytes` | `StrictPositiveInt \| None` | `None` | `expected_archive_size_bytes: StrictPositiveInt \| None = None` |
| `cache_max_age_hours` | `StrictNonNegativeFloat` | `required` | `cache_max_age_hours: StrictNonNegativeFloat` |
| `logical_layers` | `IgnBdTopoLogicalLayersConfig` | `required` | `logical_layers: IgnBdTopoLogicalLayersConfig` |
| `access` | `IgnBdTopoAccessConfig` | `required` | `access: IgnBdTopoAccessConfig` |
| `coverage` | `IgnBdTopoCoverageConfig` | `required` | `coverage: IgnBdTopoCoverageConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_source_config` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validated_source_config` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_archive_filename` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_department_coverage_layer` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_road_layer` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validated_layer_source_config` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_archive_config_lineage` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_department_coverage` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.apply_road_vehicle_proxy_policy::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_configured_coverage_identity` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_coverage_summary` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::assess_road_proximity_coverage` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.enrich_grid_proximity::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
)`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.enrich_road_proximity::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.enrich_road_proximity::enrich_parcel_road_proximity` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.normalize_access_ign::normalize_ign_roads` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `IgnBdTopoSourceConfig`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `IgnBdTopoSourceConfig`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_synthetic_config` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::source_config` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_valid_source_config_loads` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_loaded_ign_source_config_and_nested_models_are_frozen` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_revalidates_a_tampered_config_before_network` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_invalid_department_coverage_config_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_required_source_field_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_invalid_source_configuration_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unknown_source_config_field_is_rejected` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_real_layer_names_are_listed_and_discovered` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_electric_line_layer_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_transformation_post_layer_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_electric_line_layers_fail` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_schema_v3_extraction_metadata_binds_complete_physical_inventory` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_rejects_forged_download_lineage_before_archive_open` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_same_size_geopackage_tamper_invalidates_extraction_cache` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_forged_extraction_metadata_never_returns_cache_hit` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_sha_is_not_trusted` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_size_is_not_trusted` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_physical_layer_cannot_collide_with_electricity_roles` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_road_role` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_electricity_roles` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_physical_layers_must_be_distinct` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_extraction_backup_blocks_before_7z_open` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_source_change_after_physical_read` via `IgnBdTopoSourceConfig`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`

**Exact class source**

```python
class IgnBdTopoSourceConfig(BaseModel):
    """Strict, reproducible description of one official IGN package."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: Literal[
        "Institut national de l'information géographique et forestière (IGN)"
    ]
    product: Literal["BD TOPO"]
    department_code: DepartmentCode
    edition: EditionString
    product_version: NonEmptyString | None = None
    projection: Projection
    format: PackageFormat
    archive_format: ArchiveFormat
    source_url: HttpUrl
    checksum_url: HttpUrl | None = None
    official_checksum_algorithm: ChecksumAlgorithm | None = None
    official_checksum: HexChecksum | None = None
    expected_archive_size_bytes: StrictPositiveInt | None = None
    cache_max_age_hours: StrictNonNegativeFloat
    logical_layers: IgnBdTopoLogicalLayersConfig
    access: IgnBdTopoAccessConfig
    coverage: IgnBdTopoCoverageConfig

    @field_validator("edition")
    @classmethod
    def _valid_edition_date(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError as error:
            raise ValueError("edition must be a valid ISO calendar date") from error
        return value

    @model_validator(mode="after")
    def _consistent_package_and_checksum(self) -> Self:
        path = unquote(urlparse(str(self.source_url)).path)
        if Path(path).suffix.casefold() != f".{self.archive_format}":
            raise ValueError("source_url extension does not match archive_format")

        has_algorithm = self.official_checksum_algorithm is not None
        has_checksum = self.official_checksum is not None
        if has_algorithm != has_checksum:
            raise ValueError(
                "official_checksum_algorithm and official_checksum must be set together"
            )
        if (
            self.official_checksum_algorithm == "md5"
            and len(self.official_checksum or "") != 32
        ):
            raise ValueError(
                "An official MD5 checksum must contain 32 hexadecimal digits"
            )
        if (
            self.official_checksum_algorithm == "sha256"
            and len(self.official_checksum or "") != 64
        ):
            raise ValueError(
                "An official SHA256 checksum must contain 64 hexadecimal digits"
            )
        if self.checksum_url is not None and not has_checksum:
            raise ValueError(
                "checksum_url requires a pinned official checksum and algorithm"
            )
        return self
```

### `IgnBdTopoError`

**Source purpose:** Base error for controlled IGN BD TOPO source failures.

- Exact decorators: none.
- Exact bases: `RuntimeError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validated_source_config` via `IgnBdTopoError`

**Exact class source**

```python
class IgnBdTopoError(RuntimeError):
    """Base error for controlled IGN BD TOPO source failures."""
```

### `IgnBdTopoDownloadError`

**Source purpose:** Raised when an IGN archive cannot be downloaded or cached safely.

- Exact decorators: none.
- Exact bases: `IgnBdTopoError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_source_config` via `IgnBdTopoDownloadError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_source_config` via `IgnBdTopoDownloadError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validated_source_config` via `IgnBdTopoDownloadError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_archive_filename` via `IgnBdTopoDownloadError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_archive_filename` via `IgnBdTopoDownloadError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_require_no_cache_recovery_material` via `IgnBdTopoDownloadError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_require_no_cache_recovery_material` via `IgnBdTopoDownloadError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_prepare_temporary_cache_file` via `IgnBdTopoDownloadError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_prepare_temporary_cache_file` via `IgnBdTopoDownloadError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_cleanup_temporary_cache_files` via `IgnBdTopoDownloadError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_cleanup_temporary_cache_files` via `IgnBdTopoDownloadError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_publish_cache_pair` via `IgnBdTopoDownloadError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_cache_pair` via `IgnBdTopoDownloadError`
- constructor call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `IgnBdTopoDownloadError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `IgnBdTopoDownloadError`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_revalidates_a_tampered_config_before_network` via `IgnBdTopoDownloadError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `IgnBdTopoDownloadError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `IgnBdTopoDownloadError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `IgnBdTopoDownloadError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `IgnBdTopoDownloadError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `IgnBdTopoDownloadError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `IgnBdTopoDownloadError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_duplicate_ign_yaml_key_is_rejected` via `IgnBdTopoDownloadError`

**Exact class source**

```python
class IgnBdTopoDownloadError(IgnBdTopoError):
    """Raised when an IGN archive cannot be downloaded or cached safely."""
```

### `IgnBdTopoArchiveError`

**Source purpose:** Raised when an IGN archive or its extraction is unsafe or invalid.

- Exact decorators: none.
- Exact bases: `IgnBdTopoError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::_calculate_checksums` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_calculate_checksums` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_cache_pair` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_windows_component_key` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_windows_component_key` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_validate_archive_members` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_archive_members` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_geopackage` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_geopackage` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_safe_relative_path` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_safe_relative_path` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_resolve_relative_path` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_resolve_relative_path` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_geopackage_integrity` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_geopackage_integrity` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_regular_file_sha256` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_regular_file_sha256` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_inventory_extracted_tree` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_inventory_extracted_tree` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_validate_extracted_inventory` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extracted_inventory` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_remove_validated_extraction_directory` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_remove_validated_extraction_directory` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_require_no_extraction_backup` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_require_no_extraction_backup` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_require_safe_existing_extraction_marker` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_require_safe_existing_extraction_marker` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_prepare_temporary_extraction_directory` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_prepare_temporary_extraction_directory` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `IgnBdTopoArchiveError`
- constructor call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `IgnBdTopoArchiveError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `IgnBdTopoArchiveError`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_multiple_geopackages_are_rejected_as_ambiguous` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_rejects_forged_download_lineage_before_archive_open` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_windows_unsafe_member_names_fail_closed` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_casefold_and_nfkc_destination_collisions_fail` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_nfkc_separator_destinations_fail_closed` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_parent_file_conflict_fails_closed` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_7z_encrypted_archive_fails_closed` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extracted_inventory_mismatch_fails_closed` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_extraction_backup_blocks_before_7z_open` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_publication_double_failure_preserves_backup` via `IgnBdTopoArchiveError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via `IgnBdTopoArchiveError`

**Exact class source**

```python
class IgnBdTopoArchiveError(IgnBdTopoError):
    """Raised when an IGN archive or its extraction is unsafe or invalid."""
```

### `IgnBdTopoLayerError`

**Source purpose:** Raised when required GeoPackage layers cannot be discovered or loaded.

- Exact decorators: none.
- Exact bases: `IgnBdTopoError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::list_ign_bdtopo_layers` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::list_ign_bdtopo_layers` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_discover_department_coverage_layer` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_department_coverage_layer` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_discover_road_layer` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_road_layer` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_verify_unchanged_extraction` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_verify_unchanged_extraction` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_read_layer_frame` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_read_layer_frame` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_read_verified_layer_frames` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_read_verified_layer_frames` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_validate_layer_summary_contract` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_layer_summary_contract` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_compare_layer_summary` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_compare_layer_summary` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_compare_loaded_frame` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_compare_loaded_frame` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_validate_lambert93` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_lambert93` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_load_untrusted_ign_bdtopo_layer` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_untrusted_ign_bdtopo_layer` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validated_layer_source_config` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_validate_archive_config_lineage` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_archive_config_lineage` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_department_coverage_from_frame` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_department_coverage_from_frame` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_validate_coverage_summary_contract` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_coverage_summary_contract` via `IgnBdTopoLayerError`
- constructor call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_department_coverage` via `IgnBdTopoLayerError`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_department_coverage` via `IgnBdTopoLayerError`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_electric_line_layer_fails` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_transformation_post_layer_fails` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_electric_line_layers_fail` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_geographic_crs_is_rejected` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_physical_layer_cannot_collide_with_electricity_roles` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_road_role` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_electricity_roles` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_physical_layers_must_be_distinct` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `IgnBdTopoLayerError`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_source_change_after_physical_read` via `IgnBdTopoLayerError`

**Exact class source**

```python
class IgnBdTopoLayerError(IgnBdTopoError):
    """Raised when required GeoPackage layers cannot be discovered or loaded."""
```

### `IgnBdTopoArchiveIntegrity`

**Source purpose:** Defines `IgnBdTopoArchiveIntegrity`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `file_size` | `int` | `required` | `file_size: int` |
| `sha256` | `str` | `required` | `sha256: str` |
| `official_checksum_algorithm` | `ChecksumAlgorithm \| None` | `required` | `official_checksum_algorithm: ChecksumAlgorithm \| None` |
| `official_checksum` | `str \| None` | `required` | `official_checksum: str \| None` |
| `official_checksum_validated` | `bool` | `required` | `official_checksum_validated: bool` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `IgnBdTopoArchiveIntegrity`
- value/type reference: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `IgnBdTopoArchiveIntegrity`

**Exact class source**

```python
class IgnBdTopoArchiveIntegrity:
    file_size: int
    sha256: str
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: bool
```

### `IgnBdTopoDownload`

**Source purpose:** Defines `IgnBdTopoDownload`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `provider` | `str` | `required` | `provider: str` |
| `product` | `str` | `required` | `product: str` |
| `department_code` | `str` | `required` | `department_code: str` |
| `edition` | `str` | `required` | `edition: str` |
| `product_version` | `str \| None` | `required` | `product_version: str \| None` |
| `projection` | `str` | `required` | `projection: str` |
| `package_format` | `str` | `required` | `package_format: str` |
| `archive_format` | `str` | `required` | `archive_format: str` |
| `source_url` | `str` | `required` | `source_url: str` |
| `checksum_url` | `str \| None` | `required` | `checksum_url: str \| None` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `filename` | `str` | `required` | `filename: str` |
| `file_size` | `int` | `required` | `file_size: int` |
| `sha256` | `str` | `required` | `sha256: str` |
| `official_checksum_algorithm` | `ChecksumAlgorithm \| None` | `required` | `official_checksum_algorithm: ChecksumAlgorithm \| None` |
| `official_checksum` | `str \| None` | `required` | `official_checksum: str \| None` |
| `official_checksum_validated` | `bool` | `required` | `official_checksum_validated: bool` |
| `path` | `Path` | `required` | `path: Path` |
| `cache_hit` | `bool` | `required` | `cache_hit: bool` |
| `spatial_role` | `SpatialRole` | `"PROXY_GEOMETRY"` | `spatial_role: SpatialRole = "PROXY_GEOMETRY"` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_cache_metadata_from_download` via `IgnBdTopoDownload`
- constructor call: `landscout.sources.ign_bdtopo_fr::_download_from_metadata` via `IgnBdTopoDownload`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_download_from_metadata` via `IgnBdTopoDownload`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `IgnBdTopoDownload`
- constructor call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `IgnBdTopoDownload`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `IgnBdTopoDownload`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `IgnBdTopoDownload`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `IgnBdTopoDownload`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `IgnBdTopoDownload`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_archive_config_lineage` via `IgnBdTopoDownload`
- import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `IgnBdTopoDownload`
- import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `IgnBdTopoDownload`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_assess_road_proximity_coverage::_archive` via `IgnBdTopoDownload`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_archive` via `IgnBdTopoDownload`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `IgnBdTopoDownload`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_normalize_access_ign::_source` via `IgnBdTopoDownload`
- value/type reference: `tests.unit.test_normalize_access_ign::_source` via `IgnBdTopoDownload`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_normalize_grid_ign::_source_bundle` via `IgnBdTopoDownload`
- value/type reference: `tests.unit.test_normalize_grid_ign::_source_bundle` via `IgnBdTopoDownload`

**Exact class source**

```python
class IgnBdTopoDownload:
    provider: str
    product: str
    department_code: str
    edition: str
    product_version: str | None
    projection: str
    package_format: str
    archive_format: str
    source_url: str
    checksum_url: str | None
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: bool
    path: Path
    cache_hit: bool
    spatial_role: SpatialRole = "PROXY_GEOMETRY"
```

### `IgnBdTopoLayerSelection`

**Source purpose:** Defines `IgnBdTopoLayerSelection`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `all_layer_names` | `tuple[str, ...]` | `required` | `all_layer_names: tuple[str, ...]` |
| `electric_lines_layer` | `str` | `required` | `electric_lines_layer: str` |
| `transformation_posts_layer` | `str` | `required` | `transformation_posts_layer: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `IgnBdTopoLayerSelection`
- value/type reference: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `IgnBdTopoLayerSelection`

**Exact class source**

```python
class IgnBdTopoLayerSelection:
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
```

### `IgnBdTopoExtraction`

**Source purpose:** Defines `IgnBdTopoExtraction`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `archive` | `IgnBdTopoDownload` | `required` | `archive: IgnBdTopoDownload` |
| `extraction_path` | `Path` | `required` | `extraction_path: Path` |
| `geopackage_path` | `Path` | `required` | `geopackage_path: Path` |
| `geopackage_filename` | `str` | `required` | `geopackage_filename: str` |
| `geopackage_size_bytes` | `int` | `required` | `geopackage_size_bytes: int` |
| `geopackage_sha256` | `str` | `required` | `geopackage_sha256: str` |
| `all_layer_names` | `tuple[str, ...]` | `required` | `all_layer_names: tuple[str, ...]` |
| `electric_lines_layer` | `str` | `required` | `electric_lines_layer: str` |
| `transformation_posts_layer` | `str` | `required` | `transformation_posts_layer: str` |
| `road_segments_layer` | `str` | `required` | `road_segments_layer: str` |
| `department_layer` | `str` | `required` | `department_layer: str` |
| `cache_hit` | `bool` | `required` | `cache_hit: bool` |
| `spatial_role` | `SpatialRole` | `"PROXY_GEOMETRY"` | `spatial_role: SpatialRole = "PROXY_GEOMETRY"` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `IgnBdTopoExtraction`
- constructor call: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `IgnBdTopoExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `IgnBdTopoExtraction`
- constructor call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `IgnBdTopoExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `IgnBdTopoExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_archive_config_lineage` via `IgnBdTopoExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `IgnBdTopoExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `IgnBdTopoExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_department_coverage_from_frame` via `IgnBdTopoExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `IgnBdTopoExtraction`
- import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `IgnBdTopoExtraction`
- import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `IgnBdTopoExtraction`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_assess_road_proximity_coverage::_extraction` via `IgnBdTopoExtraction`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_extraction` via `IgnBdTopoExtraction`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_road_source` via `IgnBdTopoExtraction`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_coverage` via `IgnBdTopoExtraction`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `IgnBdTopoExtraction`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_normalize_access_ign::_source` via `IgnBdTopoExtraction`
- value/type reference: `tests.unit.test_normalize_access_ign::_source` via `IgnBdTopoExtraction`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_normalize_grid_ign::_source_bundle` via `IgnBdTopoExtraction`
- value/type reference: `tests.unit.test_normalize_grid_ign::_source_bundle` via `IgnBdTopoExtraction`

**Exact class source**

```python
class IgnBdTopoExtraction:
    archive: IgnBdTopoDownload
    extraction_path: Path
    geopackage_path: Path
    geopackage_filename: str
    geopackage_size_bytes: int
    geopackage_sha256: str
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    road_segments_layer: str
    department_layer: str
    cache_hit: bool
    spatial_role: SpatialRole = "PROXY_GEOMETRY"
```

### `IgnBdTopoLayerSummary`

**Source purpose:** Defines `IgnBdTopoLayerSummary`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `logical_name` | `LogicalLayerName` | `required` | `logical_name: LogicalLayerName` |
| `source_layer_name` | `str` | `required` | `source_layer_name: str` |
| `crs` | `str` | `required` | `crs: str` |
| `feature_count` | `int` | `required` | `feature_count: int` |
| `columns` | `tuple[str, ...]` | `required` | `columns: tuple[str, ...]` |
| `dtypes` | `tuple[tuple[str, str], ...]` | `required` | `dtypes: tuple[tuple[str, str], ...]` |
| `null_geometry_count` | `int` | `required` | `null_geometry_count: int` |
| `empty_geometry_count` | `int` | `required` | `empty_geometry_count: int` |
| `invalid_geometry_count` | `int` | `required` | `invalid_geometry_count: int` |
| `geometry_types` | `tuple[str, ...]` | `required` | `geometry_types: tuple[str, ...]` |
| `spatial_role` | `SpatialRole` | `"PROXY_GEOMETRY"` | `spatial_role: SpatialRole = "PROXY_GEOMETRY"` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_layer_summary_contract` via `IgnBdTopoLayerSummary`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_compare_layer_summary` via `IgnBdTopoLayerSummary`
- constructor call: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `IgnBdTopoLayerSummary`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `IgnBdTopoLayerSummary`
- import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `IgnBdTopoLayerSummary`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `IgnBdTopoLayerSummary`
- import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_layer_summary` via `IgnBdTopoLayerSummary`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `IgnBdTopoLayerSummary`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_assess_road_proximity_coverage::_road_source` via `IgnBdTopoLayerSummary`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_road_source` via `IgnBdTopoLayerSummary`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_normalize_access_ign::_summary` via `IgnBdTopoLayerSummary`
- value/type reference: `tests.unit.test_normalize_access_ign::_summary` via `IgnBdTopoLayerSummary`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_normalize_grid_ign::_summary` via `IgnBdTopoLayerSummary`
- value/type reference: `tests.unit.test_normalize_grid_ign::_summary` via `IgnBdTopoLayerSummary`

**Exact class source**

```python
class IgnBdTopoLayerSummary:
    logical_name: LogicalLayerName
    source_layer_name: str
    crs: str
    feature_count: int
    columns: tuple[str, ...]
    dtypes: tuple[tuple[str, str], ...]
    null_geometry_count: int
    empty_geometry_count: int
    invalid_geometry_count: int
    geometry_types: tuple[str, ...]
    spatial_role: SpatialRole = "PROXY_GEOMETRY"
```

### `IgnBdTopoLoadedLayer`

**Source purpose:** Defines `IgnBdTopoLoadedLayer`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `data` | `gpd.GeoDataFrame` | `required` | `data: gpd.GeoDataFrame` |
| `summary` | `IgnBdTopoLayerSummary` | `required` | `summary: IgnBdTopoLayerSummary` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `IgnBdTopoLoadedLayer`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `IgnBdTopoLoadedLayer`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_untrusted_ign_bdtopo_layer` via `IgnBdTopoLoadedLayer`

**Exact class source**

```python
class IgnBdTopoLoadedLayer:
    data: gpd.GeoDataFrame
    summary: IgnBdTopoLayerSummary
```

### `IgnBdTopoElectricityData`

**Source purpose:** Defines `IgnBdTopoElectricityData`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `extraction` | `IgnBdTopoExtraction` | `required` | `extraction: IgnBdTopoExtraction` |
| `electric_lines` | `gpd.GeoDataFrame` | `required` | `electric_lines: gpd.GeoDataFrame` |
| `transformation_posts` | `gpd.GeoDataFrame` | `required` | `transformation_posts: gpd.GeoDataFrame` |
| `electric_lines_summary` | `IgnBdTopoLayerSummary` | `required` | `electric_lines_summary: IgnBdTopoLayerSummary` |
| `transformation_posts_summary` | `IgnBdTopoLayerSummary` | `required` | `transformation_posts_summary: IgnBdTopoLayerSummary` |
| `spatial_role` | `SpatialRole` | `"PROXY_GEOMETRY"` | `spatial_role: SpatialRole = "PROXY_GEOMETRY"` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `IgnBdTopoElectricityData`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `IgnBdTopoElectricityData`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `IgnBdTopoElectricityData`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `IgnBdTopoElectricityData`
- import: `landscout.stages.enrich_grid_proximity::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
)`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `IgnBdTopoElectricityData`
- import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_archive_identity` via `IgnBdTopoElectricityData`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `IgnBdTopoElectricityData`
- value/type reference: `landscout.stages.normalize_grid_ign::_source_context` via `IgnBdTopoElectricityData`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `IgnBdTopoElectricityData`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- value/type reference: `tests.unit.test_normalize_grid_ign::normalize_ign_electricity` via `IgnBdTopoElectricityData`
- constructor call: `tests.unit.test_normalize_grid_ign::_source_bundle` via `IgnBdTopoElectricityData`
- value/type reference: `tests.unit.test_normalize_grid_ign::_source_bundle` via `IgnBdTopoElectricityData`
- value/type reference: `tests.unit.test_normalize_grid_ign::_source_bundle_with_archive` via `IgnBdTopoElectricityData`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_grid_normalization_uses_distinct_fresh_revalidated_frames.return_fresh_and_mutate_supplied` via `IgnBdTopoElectricityData`

**Exact class source**

```python
class IgnBdTopoElectricityData:
    extraction: IgnBdTopoExtraction
    electric_lines: gpd.GeoDataFrame
    transformation_posts: gpd.GeoDataFrame
    electric_lines_summary: IgnBdTopoLayerSummary
    transformation_posts_summary: IgnBdTopoLayerSummary
    spatial_role: SpatialRole = "PROXY_GEOMETRY"
```

### `IgnBdTopoRoadData`

**Source purpose:** Unfiltered factual road geometry from one verified IGN extraction.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `extraction` | `IgnBdTopoExtraction` | `required` | `extraction: IgnBdTopoExtraction` |
| `road_segments` | `gpd.GeoDataFrame` | `required` | `road_segments: gpd.GeoDataFrame` |
| `road_segments_summary` | `IgnBdTopoLayerSummary` | `required` | `road_segments_summary: IgnBdTopoLayerSummary` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `IgnBdTopoRoadData`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `IgnBdTopoRoadData`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `IgnBdTopoRoadData`
- import: `landscout.stages.apply_road_vehicle_proxy_policy::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoRoadData`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoRoadData`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `IgnBdTopoRoadData`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `IgnBdTopoRoadData`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `IgnBdTopoRoadData`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::assess_road_proximity_coverage` via `IgnBdTopoRoadData`
- import: `landscout.stages.enrich_road_proximity::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `IgnBdTopoRoadData`
- value/type reference: `landscout.stages.enrich_road_proximity::enrich_parcel_road_proximity` via `IgnBdTopoRoadData`
- import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `IgnBdTopoRoadData`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `IgnBdTopoRoadData`
- value/type reference: `landscout.stages.normalize_access_ign::normalize_ign_roads` via `IgnBdTopoRoadData`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_apply_road_vehicle_proxy_policy::_source` via `IgnBdTopoRoadData`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::_source` via `IgnBdTopoRoadData`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_assess_road_proximity_coverage::_road_source` via `IgnBdTopoRoadData`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_road_source` via `IgnBdTopoRoadData`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `IgnBdTopoRoadData`
- import: `tests.unit.test_enrich_road_proximity::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_enrich_road_proximity::_source` via `IgnBdTopoRoadData`
- value/type reference: `tests.unit.test_enrich_road_proximity::_source` via `IgnBdTopoRoadData`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_normalize_access_ign::_source` via `IgnBdTopoRoadData`
- value/type reference: `tests.unit.test_normalize_access_ign::_source` via `IgnBdTopoRoadData`
- constructor call: `tests.unit.test_normalize_access_ign::_with_alternate_road_layer` via `IgnBdTopoRoadData`
- value/type reference: `tests.unit.test_normalize_access_ign::_with_alternate_road_layer` via `IgnBdTopoRoadData`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_normalization_uses_distinct_fresh_revalidated_frame.return_fresh_and_mutate_supplied` via `IgnBdTopoRoadData`

**Exact class source**

```python
class IgnBdTopoRoadData:
    """Unfiltered factual road geometry from one verified IGN extraction."""

    extraction: IgnBdTopoExtraction
    road_segments: gpd.GeoDataFrame
    road_segments_summary: IgnBdTopoLayerSummary
```

### `IgnBdTopoCoverageLayerSummary`

**Source purpose:** Observed source-layer schema plus the authoritative selected feature.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `source_layer_name` | `str` | `required` | `source_layer_name: str` |
| `crs` | `str` | `required` | `crs: str` |
| `source_feature_count` | `int` | `required` | `source_feature_count: int` |
| `selected_feature_count` | `int` | `required` | `selected_feature_count: int` |
| `columns` | `tuple[str, ...]` | `required` | `columns: tuple[str, ...]` |
| `dtypes` | `tuple[tuple[str, str], ...]` | `required` | `dtypes: tuple[tuple[str, str], ...]` |
| `null_geometry_count` | `int` | `required` | `null_geometry_count: int` |
| `empty_geometry_count` | `int` | `required` | `empty_geometry_count: int` |
| `invalid_geometry_count` | `int` | `required` | `invalid_geometry_count: int` |
| `geometry_types` | `tuple[str, ...]` | `required` | `geometry_types: tuple[str, ...]` |
| `department_code_field` | `str` | `required` | `department_code_field: str` |
| `selected_department_code` | `str` | `required` | `selected_department_code: str` |
| `spatial_role` | `CoverageSpatialRole` | `"SOURCE_COVERAGE_BOUNDARY"` | `spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::_department_coverage_from_frame` via `IgnBdTopoCoverageLayerSummary`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_department_coverage_from_frame` via `IgnBdTopoCoverageLayerSummary`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_coverage_summary_contract` via `IgnBdTopoCoverageLayerSummary`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_coverage_summary` via `IgnBdTopoCoverageLayerSummary`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_coverage_summary` via `IgnBdTopoCoverageLayerSummary`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_assess_road_proximity_coverage::_coverage` via `IgnBdTopoCoverageLayerSummary`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_coverage` via `IgnBdTopoCoverageLayerSummary`

**Exact class source**

```python
class IgnBdTopoCoverageLayerSummary:
    """Observed source-layer schema plus the authoritative selected feature."""

    source_layer_name: str
    crs: str
    source_feature_count: int
    selected_feature_count: int
    columns: tuple[str, ...]
    dtypes: tuple[tuple[str, str], ...]
    null_geometry_count: int
    empty_geometry_count: int
    invalid_geometry_count: int
    geometry_types: tuple[str, ...]
    department_code_field: str
    selected_department_code: str
    spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"
```

### `IgnBdTopoDepartmentCoverage`

**Source purpose:** Selected department coverage with package lineage and source schema.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `extraction` | `IgnBdTopoExtraction` | `required` | `extraction: IgnBdTopoExtraction` |
| `coverage` | `gpd.GeoDataFrame` | `required` | `coverage: gpd.GeoDataFrame` |
| `summary` | `IgnBdTopoCoverageLayerSummary` | `required` | `summary: IgnBdTopoCoverageLayerSummary` |
| `source_provider` | `str` | `required` | `source_provider: str` |
| `source_product` | `str` | `required` | `source_product: str` |
| `source_department_code` | `str` | `required` | `source_department_code: str` |
| `source_edition` | `str` | `required` | `source_edition: str` |
| `source_product_version` | `str \| None` | `required` | `source_product_version: str \| None` |
| `source_archive_sha256` | `str` | `required` | `source_archive_sha256: str` |
| `source_layer` | `str` | `required` | `source_layer: str` |
| `spatial_role` | `CoverageSpatialRole` | `"SOURCE_COVERAGE_BOUNDARY"` | `spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- constructor call: `landscout.sources.ign_bdtopo_fr::_department_coverage_from_frame` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_department_coverage_from_frame` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_department_coverage` via `IgnBdTopoDepartmentCoverage`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_coverage_summary` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_source_coverage` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_configured_coverage_identity` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_grid_coverage::_coverage_lineage_values` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_proximity_source_identity` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `IgnBdTopoDepartmentCoverage`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_coverage_summary` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_coverage_lineage` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_expected_diagnostics` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_diagnosed_class_proximity` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_selected_road_package` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `IgnBdTopoDepartmentCoverage`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- constructor call: `tests.unit.test_assess_road_proximity_coverage::_coverage` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_coverage` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_measured_boundary_distance` via `IgnBdTopoDepartmentCoverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `IgnBdTopoDepartmentCoverage`

**Exact class source**

```python
class IgnBdTopoDepartmentCoverage:
    """Selected department coverage with package lineage and source schema."""

    extraction: IgnBdTopoExtraction
    coverage: gpd.GeoDataFrame
    summary: IgnBdTopoCoverageLayerSummary
    source_provider: str
    source_product: str
    source_department_code: str
    source_edition: str
    source_product_version: str | None
    source_archive_sha256: str
    source_layer: str
    spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"
```

### `_CacheMetadata`

**Source purpose:** Defines `_CacheMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `schema_version` | `Literal[1]` | `required` | `schema_version: Literal[1]` |
| `provider` | `str` | `required` | `provider: str` |
| `product` | `str` | `required` | `product: str` |
| `department_code` | `str` | `required` | `department_code: str` |
| `edition` | `str` | `required` | `edition: str` |
| `product_version` | `str \| None` | `required` | `product_version: str \| None` |
| `projection` | `str` | `required` | `projection: str` |
| `package_format` | `str` | `required` | `package_format: str` |
| `archive_format` | `str` | `required` | `archive_format: str` |
| `source_url` | `str` | `required` | `source_url: str` |
| `checksum_url` | `str \| None` | `required` | `checksum_url: str \| None` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `filename` | `str` | `required` | `filename: str` |
| `file_size` | `StrictPositiveInt` | `required` | `file_size: StrictPositiveInt` |
| `sha256` | `CanonicalSha256` | `required` | `sha256: CanonicalSha256` |
| `official_checksum_algorithm` | `ChecksumAlgorithm \| None` | `required` | `official_checksum_algorithm: ChecksumAlgorithm \| None` |
| `official_checksum` | `str \| None` | `required` | `official_checksum: str \| None` |
| `official_checksum_validated` | `StrictBool` | `required` | `official_checksum_validated: StrictBool` |
| `spatial_role` | `SpatialRole` | `required` | `spatial_role: SpatialRole` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.ign_bdtopo_fr::_cache_metadata_from_download` via `_CacheMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_cache_metadata_from_download` via `_CacheMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_download_from_metadata` via `_CacheMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `_CacheMetadata`

**Exact class source**

```python
class _CacheMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    provider: str
    product: str
    department_code: str
    edition: str
    product_version: str | None
    projection: str
    package_format: str
    archive_format: str
    source_url: str
    checksum_url: str | None
    download_timestamp: str
    filename: str
    file_size: StrictPositiveInt
    sha256: CanonicalSha256
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: StrictBool
    spatial_role: SpatialRole

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("IGN cache schema version must be an exact integer")
        return value
```

### `_ExtractedEntryMetadata`

**Source purpose:** Defines `_ExtractedEntryMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `relative_path` | `str` | `required` | `relative_path: str` |
| `kind` | `Literal['file', 'directory']` | `required` | `kind: Literal["file", "directory"]` |
| `size_bytes` | `int \| None` | `Field(default=None, strict=True, ge=0)` | `size_bytes: int \| None = Field(default=None, strict=True, ge=0)` |
| `sha256` | `CanonicalSha256 \| None` | `None` | `sha256: CanonicalSha256 \| None = None` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.ign_bdtopo_fr::_inventory_extracted_tree` via `_ExtractedEntryMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_inventory_extracted_tree` via `_ExtractedEntryMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extracted_inventory` via `_ExtractedEntryMetadata`

**Exact class source**

```python
class _ExtractedEntryMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    relative_path: str
    kind: Literal["file", "directory"]
    size_bytes: int | None = Field(default=None, strict=True, ge=0)
    sha256: CanonicalSha256 | None = None
```

### `_ExtractionMetadata`

**Source purpose:** Defines `_ExtractionMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `schema_version` | `Literal[3]` | `required` | `schema_version: Literal[3]` |
| `archive_sha256` | `CanonicalSha256` | `required` | `archive_sha256: CanonicalSha256` |
| `geopackage_relative_path` | `str` | `required` | `geopackage_relative_path: str` |
| `geopackage_size_bytes` | `StrictPositiveInt` | `required` | `geopackage_size_bytes: StrictPositiveInt` |
| `geopackage_sha256` | `CanonicalSha256` | `required` | `geopackage_sha256: CanonicalSha256` |
| `all_layer_names` | `tuple[str, ...]` | `required` | `all_layer_names: tuple[str, ...]` |
| `electric_lines_layer` | `str` | `required` | `electric_lines_layer: str` |
| `transformation_posts_layer` | `str` | `required` | `transformation_posts_layer: str` |
| `road_segments_layer` | `str` | `required` | `road_segments_layer: str` |
| `department_layer` | `str` | `required` | `department_layer: str` |
| `extracted_entries` | `tuple[_ExtractedEntryMetadata, ...]` | `required` | `extracted_entries: tuple[_ExtractedEntryMetadata, ...]` |
| `spatial_role` | `SpatialRole` | `required` | `spatial_role: SpatialRole` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_ExtractionMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_ExtractionMetadata`
- constructor call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_ExtractionMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_ExtractionMetadata`

**Exact class source**

```python
class _ExtractionMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[3]
    archive_sha256: CanonicalSha256
    geopackage_relative_path: str
    geopackage_size_bytes: StrictPositiveInt
    geopackage_sha256: CanonicalSha256
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    road_segments_layer: str
    department_layer: str
    extracted_entries: tuple[_ExtractedEntryMetadata, ...]
    spatial_role: SpatialRole

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("IGN extraction schema version must be an exact integer")
        return value
```

### `_ValidatedArchiveMember`

**Source purpose:** Defines `_ValidatedArchiveMember`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `relative_path` | `str` | `required` | `relative_path: str` |
| `kind` | `Literal['file', 'directory']` | `required` | `kind: Literal["file", "directory"]` |
| `size_bytes` | `int \| None` | `required` | `size_bytes: int \| None` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.ign_bdtopo_fr::_validate_archive_members` via `_ValidatedArchiveMember`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_archive_members` via `_ValidatedArchiveMember`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extracted_inventory` via `_ValidatedArchiveMember`
- constructor call: `tests.unit.test_ign_bdtopo_fr::test_extracted_inventory_mismatch_fails_closed` via `ign_bdtopo_fr._ValidatedArchiveMember`

**Exact class source**

```python
class _ValidatedArchiveMember:
    relative_path: str
    kind: Literal["file", "directory"]
    size_bytes: int | None
```

### `_ConfiguredPhysicalRoles`

**Source purpose:** Defines `_ConfiguredPhysicalRoles`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `all_layer_names` | `tuple[str, ...]` | `required` | `all_layer_names: tuple[str, ...]` |
| `electric_lines_layer` | `str` | `required` | `electric_lines_layer: str` |
| `transformation_posts_layer` | `str` | `required` | `transformation_posts_layer: str` |
| `road_segments_layer` | `str` | `required` | `road_segments_layer: str` |
| `department_layer` | `str` | `required` | `department_layer: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `_ConfiguredPhysicalRoles`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `_ConfiguredPhysicalRoles`

**Exact class source**

```python
class _ConfiguredPhysicalRoles:
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    road_segments_layer: str
    department_layer: str
```

### `_VerifiedIgnExtraction`

**Source purpose:** Defines `_VerifiedIgnExtraction`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `extraction` | `IgnBdTopoExtraction` | `required` | `extraction: IgnBdTopoExtraction` |
| `metadata` | `_ExtractionMetadata` | `required` | `metadata: _ExtractionMetadata` |
| `geopackage_path` | `Path` | `required` | `geopackage_path: Path` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_VerifiedIgnExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_VerifiedIgnExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_verify_unchanged_extraction` via `_VerifiedIgnExtraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_read_verified_layer_frames` via `_VerifiedIgnExtraction`

**Exact class source**

```python
class _VerifiedIgnExtraction:
    extraction: IgnBdTopoExtraction
    metadata: _ExtractionMetadata
    geopackage_path: Path
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `IgnBdTopoLogicalLayerConfig._unique_tokens`

**Purpose:** Implements `unique tokens` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
```

- Exact decorators: `field_validator("match_tokens")`, `classmethod`.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cls` | positional-or-keyword | `None` | `required` |
| `value` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError("Layer match tokens must contain letters or digits")` under lexical guard `any(not token for token in normalized)`.
  - `ValueError("Layer match tokens must be unique after normalization")` under lexical guard `len(set(normalized)) != len(normalized)`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_words` | `landscout.sources.ign_bdtopo_fr._normalize_words` |
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
def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(token) for token in value)
        if any(not token for token in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(set(normalized)) != len(normalized):
            raise ValueError("Layer match tokens must be unique after normalization")
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `IgnBdTopoLogicalLayersConfig._different_token_sets`

**Purpose:** Implements `different token sets` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _different_token_sets(self) -> Self:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("Logical layers must use different match tokens")` under lexical guard `electric == posts`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_normalize_words` | `landscout.sources.ign_bdtopo_fr._normalize_words` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
def _different_token_sets(self) -> Self:
        electric = {
            _normalize_words(token) for token in self.electric_lines.match_tokens
        }
        posts = {
            _normalize_words(token) for token in self.transformation_posts.match_tokens
        }
        if electric == posts:
            raise ValueError("Logical layers must use different match tokens")
        return self
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `IgnBdTopoSourceConfig._valid_edition_date`

**Purpose:** Implements `valid edition date` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _valid_edition_date(cls, value: str) -> str:
```

- Exact decorators: `field_validator("edition")`, `classmethod`.
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
  - `ValueError("edition must be a valid ISO calendar date")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `date.fromisoformat` | `datetime.date.fromisoformat` |
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
def _valid_edition_date(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError as error:
            raise ValueError("edition must be a valid ISO calendar date") from error
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `IgnBdTopoSourceConfig._consistent_package_and_checksum`

**Purpose:** Implements `consistent package and checksum` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _consistent_package_and_checksum(self) -> Self:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("source_url extension does not match archive_format")` under lexical guard `Path(path).suffix.casefold() != f".{self.archive_format}"`.
  - `ValueError(<br>                "official_checksum_algorithm and official_checksum must be set together"<br>            )` under lexical guard `has_algorithm != has_checksum`.
  - `ValueError(<br>                "An official MD5 checksum must contain 32 hexadecimal digits"<br>            )` under lexical guard `self.official_checksum_algorithm == "md5"<br>            and len(self.official_checksum or "") != 32`.
  - `ValueError(<br>                "An official SHA256 checksum must contain 64 hexadecimal digits"<br>            )` under lexical guard `self.official_checksum_algorithm == "sha256"<br>            and len(self.official_checksum or "") != 64`.
  - `ValueError(<br>                "checksum_url requires a pinned official checksum and algorithm"<br>            )` under lexical guard `self.checksum_url is not None and not has_checksum`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `unquote` | `urllib.parse.unquote` |
| `urlparse` | `urllib.parse.urlparse` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path(path).suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
def _consistent_package_and_checksum(self) -> Self:
        path = unquote(urlparse(str(self.source_url)).path)
        if Path(path).suffix.casefold() != f".{self.archive_format}":
            raise ValueError("source_url extension does not match archive_format")

        has_algorithm = self.official_checksum_algorithm is not None
        has_checksum = self.official_checksum is not None
        if has_algorithm != has_checksum:
            raise ValueError(
                "official_checksum_algorithm and official_checksum must be set together"
            )
        if (
            self.official_checksum_algorithm == "md5"
            and len(self.official_checksum or "") != 32
        ):
            raise ValueError(
                "An official MD5 checksum must contain 32 hexadecimal digits"
            )
        if (
            self.official_checksum_algorithm == "sha256"
            and len(self.official_checksum or "") != 64
        ):
            raise ValueError(
                "An official SHA256 checksum must contain 64 hexadecimal digits"
            )
        if self.checksum_url is not None and not has_checksum:
            raise ValueError(
                "checksum_url requires a pinned official checksum and algorithm"
            )
        return self
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_CacheMetadata._strict_schema_version`

**Purpose:** Implements `strict schema version` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _strict_schema_version(cls, value: object) -> object:
```

- Exact decorators: `field_validator("schema_version", mode="before")`, `classmethod`.
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
  - `ValueError("IGN cache schema version must be an exact integer")` under lexical guard `type(value) is not int`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("IGN cache schema version must be an exact integer")
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_ExtractionMetadata._strict_schema_version`

**Purpose:** Implements `strict schema version` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _strict_schema_version(cls, value: object) -> object:
```

- Exact decorators: `field_validator("schema_version", mode="before")`, `classmethod`.
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
  - `ValueError("IGN extraction schema version must be an exact integer")` under lexical guard `type(value) is not int`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("IGN extraction schema version must be an exact integer")
        return value
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_normalize_words`

**Purpose:** Implements `normalize words` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

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
  - `" ".join(re.findall(r"[a-z0-9]+", ascii_like))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::IgnBdTopoLogicalLayerConfig._unique_tokens` via `_normalize_words`
- value/type reference: `landscout.sources.ign_bdtopo_fr::IgnBdTopoLogicalLayerConfig._unique_tokens` via `_normalize_words`
- direct call: `landscout.sources.ign_bdtopo_fr::IgnBdTopoLogicalLayersConfig._different_token_sets` via `_normalize_words`
- value/type reference: `landscout.sources.ign_bdtopo_fr::IgnBdTopoLogicalLayersConfig._different_token_sets` via `_normalize_words`
- direct call: `landscout.sources.ign_bdtopo_fr::_matching_layers` via `_normalize_words`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_matching_layers` via `_normalize_words`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `unicodedata.normalize` | `unicodedata.normalize` |
| `value.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `"".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `unicodedata.combining` | `unicodedata.combining` |
| `" ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.findall` | `re.findall` |

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
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    ascii_like = "".join(char for char in decomposed if not unicodedata.combining(char))
    return " ".join(re.findall(r"[a-z0-9]+", ascii_like))
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `load_ign_bdtopo_source_config`

**Purpose:** Load and strictly validate the pinned IGN source configuration.

**Exact signature**

```python
def load_ign_bdtopo_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> IgnBdTopoSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `DEFAULT_CONFIG_PATH` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoSourceConfig.model_validate(content)`
- Explicit raise paths:
  - `IgnBdTopoDownloadError(<br>            f"Cannot read IGN source config: {path}"<br>        )`.
  - `IgnBdTopoDownloadError(f"Expected a YAML mapping in {path}")` under lexical guard `not isinstance(content, dict)`.
  - `IgnBdTopoDownloadError(f"IGN source config is invalid: {path}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- import: `tests.unit.test_enrich_road_proximity::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    load_ign_bdtopo_source_config,
)`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::source_config` via `load_ign_bdtopo_source_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::source_config` via `load_ign_bdtopo_source_config`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_duplicate_ign_yaml_key_is_rejected` via `load_ign_bdtopo_source_config`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_duplicate_ign_yaml_key_is_rejected` via `load_ign_bdtopo_source_config`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDownloadError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownloadError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoSourceConfig.model_validate` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig.model_validate` |

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
def load_ign_bdtopo_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> IgnBdTopoSourceConfig:
    """Load and strictly validate the pinned IGN source configuration."""

    try:
        content = loads_strict_yaml(path.read_bytes())
    except (OSError, TypeError, ValueError) as error:
        raise IgnBdTopoDownloadError(
            f"Cannot read IGN source config: {path}"
        ) from error
    if not isinstance(content, dict):
        raise IgnBdTopoDownloadError(f"Expected a YAML mapping in {path}")
    try:
        return IgnBdTopoSourceConfig.model_validate(content)
    except ValidationError as error:
        raise IgnBdTopoDownloadError(f"IGN source config is invalid: {path}") from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validated_source_config`

**Purpose:** Implements `validated source config` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _validated_source_config(
    config: object,
    *,
    error_type: type[IgnBdTopoError] = IgnBdTopoDownloadError,
) -> IgnBdTopoSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `object` | `required` |
| `error_type` | keyword-only | `type[IgnBdTopoError]` | `IgnBdTopoDownloadError` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoSourceConfig.model_validate(config.model_dump(mode="python"))`
- Explicit raise paths:
  - `TypeError("IGN source config type is invalid")` under lexical guard `type(config) is not IgnBdTopoSourceConfig`.
  - `error_type("IGN source config is invalid")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `_validated_source_config`
- value/type reference: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `_validated_source_config`
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_validated_source_config`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_validated_source_config`
- direct call: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `_validated_source_config`
- value/type reference: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `_validated_source_config`
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_validated_source_config`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_validated_source_config`
- direct call: `landscout.sources.ign_bdtopo_fr::_validated_layer_source_config` via `_validated_source_config`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validated_layer_source_config` via `_validated_source_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoSourceConfig.model_validate` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig.model_validate` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `error_type` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validated_source_config(
    config: object,
    *,
    error_type: type[IgnBdTopoError] = IgnBdTopoDownloadError,
) -> IgnBdTopoSourceConfig:
    try:
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("IGN source config type is invalid")
        return IgnBdTopoSourceConfig.model_validate(config.model_dump(mode="python"))
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise error_type("IGN source config is invalid") from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_archive_filename`

**Purpose:** Implements `archive filename` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _archive_filename(config: IgnBdTopoSourceConfig) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `filename`
- Explicit raise paths:
  - `IgnBdTopoDownloadError("IGN source URL does not identify a .7z archive")` under lexical guard `not filename or Path(filename).suffix.casefold() != ".7z"`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_archive_filename`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_archive_filename`
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_archive_config_lineage` via `_archive_filename`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_archive_config_lineage` via `_archive_filename`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path` | `pathlib.Path` |
| `unquote` | `urllib.parse.unquote` |
| `urlparse` | `urllib.parse.urlparse` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path(filename).suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDownloadError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownloadError` |

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
def _archive_filename(config: IgnBdTopoSourceConfig) -> str:
    filename = Path(unquote(urlparse(str(config.source_url)).path)).name
    if not filename or Path(filename).suffix.casefold() != ".7z":
        raise IgnBdTopoDownloadError("IGN source URL does not identify a .7z archive")
    return filename
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_calculate_checksums`

**Purpose:** Implements `calculate checksums` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _calculate_checksums(
    path: Path, official_algorithm: ChecksumAlgorithm | None
) -> tuple[str, str | None]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, str | None]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `official_algorithm` | positional-or-keyword | `ChecksumAlgorithm \| None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>        sha256_digest.hexdigest(),<br>        official_digest.hexdigest() if official_digest is not None else None,<br>    )`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(f"Cannot read IGN archive: {path}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `_calculate_checksums`
- value/type reference: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `_calculate_checksums`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sha256` | `hashlib.sha256` |
| `md5` | `hashlib.md5` |
| `path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `iter` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256_digest.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `official_digest.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `sha256_digest.hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `official_digest.hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256`<br>`sha256_digest.update`<br>`sha256_digest.hexdigest` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `sha256_digest.update(chunk)`<br>`official_digest.update(chunk)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _calculate_checksums(
    path: Path, official_algorithm: ChecksumAlgorithm | None
) -> tuple[str, str | None]:
    sha256_digest = sha256()
    official_digest = None
    if official_algorithm == "md5":
        official_digest = md5(usedforsecurity=False)
    elif official_algorithm == "sha256":
        official_digest = sha256()

    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
                sha256_digest.update(chunk)
                if official_digest is not None:
                    official_digest.update(chunk)
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot read IGN archive: {path}") from error
    return (
        sha256_digest.hexdigest(),
        official_digest.hexdigest() if official_digest is not None else None,
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `validate_ign_bdtopo_archive`

**Purpose:** Validate size, configured official checksum, and available 7z CRC data.

    Some official IGN archives omit container CRC metadata, for which py7zr
    returns ``None``.  Such archives still require exact official size/checksum
    validation here and a successful full extraction before they are usable.

**Exact signature**

```python
def validate_ign_bdtopo_archive(
    path: Path, config: IgnBdTopoSourceConfig
) -> IgnBdTopoArchiveIntegrity:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoArchiveIntegrity`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoArchiveIntegrity(<br>        file_size=file_size,<br>        sha256=local_sha256,<br>        official_checksum_algorithm=config.official_checksum_algorithm,<br>        official_checksum=config.official_checksum,<br>        official_checksum_validated=official_validated,<br>    )`
- Explicit raise paths:
  - `IgnBdTopoArchiveError("IGN archive path must be a pathlib.Path")` under lexical guard `not isinstance(path, Path)`.
  - `IgnBdTopoArchiveError(f"IGN archive does not exist: {path}")` under lexical guard `path.is_symlink() or path.is_junction() or not path.is_file()`.
  - `IgnBdTopoArchiveError(f"Cannot inspect IGN archive: {path}")`.
  - `IgnBdTopoArchiveError(f"IGN archive is empty: {path}")` under lexical guard `file_size <= 0`.
  - `IgnBdTopoArchiveError(<br>            "IGN archive size does not match the official catalogue: "<br>            f"{file_size} != {config.expected_archive_size_bytes}"<br>        )` under lexical guard `config.expected_archive_size_bytes is not None<br>        and file_size != config.expected_archive_size_bytes`.
  - `IgnBdTopoArchiveError(<br>            "IGN archive does not match the pinned official "<br>            f"{config.official_checksum_algorithm} checksum"<br>        )` under lexical guard `official_validated and calculated_official != config.official_checksum`.
  - `IgnBdTopoArchiveError(<br>            f"IGN archive is not a readable 7z file: {path}"<br>        )`.
  - `IgnBdTopoArchiveError(<br>            f"IGN archive failed its 7z CRC integrity check: {path}"<br>        )` under lexical guard `integrity_result is False`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `validate_ign_bdtopo_archive`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `validate_ign_bdtopo_archive`
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `validate_ign_bdtopo_archive`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `validate_ign_bdtopo_archive`
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `validate_ign_bdtopo_archive`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `validate_ign_bdtopo_archive`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `validate_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `validate_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via `validate_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via `validate_ign_bdtopo_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.ign_bdtopo_fr._validated_source_config` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_calculate_checksums` | `landscout.sources.ign_bdtopo_fr._calculate_checksums` |
| `py7zr.SevenZipFile` | `py7zr.SevenZipFile` |
| `archive.test` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveIntegrity` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveIntegrity` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file`<br>`path.stat`<br>`py7zr.SevenZipFile` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | `py7zr.SevenZipFile` |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def validate_ign_bdtopo_archive(
    path: Path, config: IgnBdTopoSourceConfig
) -> IgnBdTopoArchiveIntegrity:
    """Validate size, configured official checksum, and available 7z CRC data.

    Some official IGN archives omit container CRC metadata, for which py7zr
    returns ``None``.  Such archives still require exact official size/checksum
    validation here and a successful full extraction before they are usable.
    """

    config = _validated_source_config(config, error_type=IgnBdTopoArchiveError)
    if not isinstance(path, Path):
        raise IgnBdTopoArchiveError("IGN archive path must be a pathlib.Path")
    if path.is_symlink() or path.is_junction() or not path.is_file():
        raise IgnBdTopoArchiveError(f"IGN archive does not exist: {path}")
    try:
        file_size = path.stat().st_size
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot inspect IGN archive: {path}") from error
    if file_size <= 0:
        raise IgnBdTopoArchiveError(f"IGN archive is empty: {path}")
    if (
        config.expected_archive_size_bytes is not None
        and file_size != config.expected_archive_size_bytes
    ):
        raise IgnBdTopoArchiveError(
            "IGN archive size does not match the official catalogue: "
            f"{file_size} != {config.expected_archive_size_bytes}"
        )

    local_sha256, calculated_official = _calculate_checksums(
        path, config.official_checksum_algorithm
    )
    official_validated = config.official_checksum is not None
    if official_validated and calculated_official != config.official_checksum:
        raise IgnBdTopoArchiveError(
            "IGN archive does not match the pinned official "
            f"{config.official_checksum_algorithm} checksum"
        )

    try:
        with py7zr.SevenZipFile(path, mode="r") as archive:
            integrity_result = archive.test()
    except (ArchiveError, EOFError, OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"IGN archive is not a readable 7z file: {path}"
        ) from error
    if integrity_result is False:
        raise IgnBdTopoArchiveError(
            f"IGN archive failed its 7z CRC integrity check: {path}"
        )

    return IgnBdTopoArchiveIntegrity(
        file_size=file_size,
        sha256=local_sha256,
        official_checksum_algorithm=config.official_checksum_algorithm,
        official_checksum=config.official_checksum,
        official_checksum_validated=official_validated,
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_cache_metadata_from_download`

**Purpose:** Implements `cache metadata from download` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _cache_metadata_from_download(download: IgnBdTopoDownload) -> _CacheMetadata:
```

- Exact decorators: none.
- Declared return annotation: `_CacheMetadata`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `IgnBdTopoDownload` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_CacheMetadata(<br>        schema_version=1,<br>        provider=download.provider,<br>        product=download.product,<br>        department_code=download.department_code,<br>        edition=download.edition,<br>        product_version=download.product_version,<br>        projection=download.projection,<br>        package_format=download.package_format,<br>        archive_format=download.archive_format,<br>        source_url=download.source_url,<br>        checksum_url=download.checksum_url,<br>        download_timestamp=download.download_timestamp,<br>        filename=download.filename,<br>        file_size=download.file_size,<br>        sha256=download.sha256,<br>        official_checksum_algorithm=download.official_checksum_algorithm,<br>        official_checksum=download.official_checksum,<br>        official_checksum_validated=download.official_checksum_validated,<br>        spatial_role=download.spatial_role,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_cache_metadata_from_download`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_cache_metadata_from_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_CacheMetadata` | `landscout.sources.ign_bdtopo_fr._CacheMetadata` |

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
def _cache_metadata_from_download(download: IgnBdTopoDownload) -> _CacheMetadata:
    return _CacheMetadata(
        schema_version=1,
        provider=download.provider,
        product=download.product,
        department_code=download.department_code,
        edition=download.edition,
        product_version=download.product_version,
        projection=download.projection,
        package_format=download.package_format,
        archive_format=download.archive_format,
        source_url=download.source_url,
        checksum_url=download.checksum_url,
        download_timestamp=download.download_timestamp,
        filename=download.filename,
        file_size=download.file_size,
        sha256=download.sha256,
        official_checksum_algorithm=download.official_checksum_algorithm,
        official_checksum=download.official_checksum,
        official_checksum_validated=download.official_checksum_validated,
        spatial_role=download.spatial_role,
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_download_from_metadata`

**Purpose:** Implements `download from metadata` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _download_from_metadata(
    metadata: _CacheMetadata, archive_path: Path, *, cache_hit: bool
) -> IgnBdTopoDownload:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `metadata` | positional-or-keyword | `_CacheMetadata` | `required` |
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `cache_hit` | keyword-only | `bool` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoDownload(<br>        provider=metadata.provider,<br>        product=metadata.product,<br>        department_code=metadata.department_code,<br>        edition=metadata.edition,<br>        product_version=metadata.product_version,<br>        projection=metadata.projection,<br>        package_format=metadata.package_format,<br>        archive_format=metadata.archive_format,<br>        source_url=metadata.source_url,<br>        checksum_url=metadata.checksum_url,<br>        download_timestamp=metadata.download_timestamp,<br>        filename=metadata.filename,<br>        file_size=metadata.file_size,<br>        sha256=metadata.sha256,<br>        official_checksum_algorithm=metadata.official_checksum_algorithm,<br>        official_checksum=metadata.official_checksum,<br>        official_checksum_validated=metadata.official_checksum_validated,<br>        path=archive_path,<br>        cache_hit=cache_hit,<br>        spatial_role=metadata.spatial_role,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `_download_from_metadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `_download_from_metadata`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoDownload` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownload` |

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
def _download_from_metadata(
    metadata: _CacheMetadata, archive_path: Path, *, cache_hit: bool
) -> IgnBdTopoDownload:
    return IgnBdTopoDownload(
        provider=metadata.provider,
        product=metadata.product,
        department_code=metadata.department_code,
        edition=metadata.edition,
        product_version=metadata.product_version,
        projection=metadata.projection,
        package_format=metadata.package_format,
        archive_format=metadata.archive_format,
        source_url=metadata.source_url,
        checksum_url=metadata.checksum_url,
        download_timestamp=metadata.download_timestamp,
        filename=metadata.filename,
        file_size=metadata.file_size,
        sha256=metadata.sha256,
        official_checksum_algorithm=metadata.official_checksum_algorithm,
        official_checksum=metadata.official_checksum,
        official_checksum_validated=metadata.official_checksum_validated,
        path=archive_path,
        cache_hit=cache_hit,
        spatial_role=metadata.spatial_role,
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_load_cached_download`

**Purpose:** Implements `load cached download` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDownload | None:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoDownload | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive_path` | positional-or-keyword | `Path` | `required` |
| `metadata_path` | positional-or-keyword | `Path` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `_download_from_metadata(metadata, archive_path, cache_hit=True)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_load_cached_download`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_load_cached_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_CacheMetadata.model_validate` | `landscout.sources.ign_bdtopo_fr._CacheMetadata.model_validate` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `downloaded_at.utcoffset` | `unresolved local/third-party receiver; no ownership inferred` |
| `UTC.utcoffset` | `datetime.UTC.utcoffset` |
| `(<br>            datetime.now(UTC) - downloaded_at.astimezone(UTC)<br>        ).total_seconds` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `downloaded_at.astimezone` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `validate_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.validate_ign_bdtopo_archive` |
| `_download_from_metadata` | `landscout.sources.ign_bdtopo_fr._download_from_metadata` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_path.is_file`<br>`metadata_path.is_file`<br>`metadata_path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        metadata = _CacheMetadata.model_validate(
            loads_strict_json_object(metadata_path.read_bytes())
        )
        downloaded_at = datetime.fromisoformat(metadata.download_timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(
            None
        ):
            return None
        age_seconds = (
            datetime.now(UTC) - downloaded_at.astimezone(UTC)
        ).total_seconds()
        if age_seconds < 0 or age_seconds > config.cache_max_age_hours * 3600:
            return None

        expected_values: tuple[tuple[Any, Any], ...] = (
            (metadata.provider, config.provider),
            (metadata.product, config.product),
            (metadata.department_code, config.department_code),
            (metadata.edition, config.edition),
            (metadata.product_version, config.product_version),
            (metadata.projection, config.projection),
            (metadata.package_format, config.format),
            (metadata.archive_format, config.archive_format),
            (metadata.source_url, str(config.source_url)),
            (
                metadata.checksum_url,
                str(config.checksum_url) if config.checksum_url is not None else None,
            ),
            (metadata.filename, archive_path.name),
            (
                metadata.official_checksum_algorithm,
                config.official_checksum_algorithm,
            ),
            (metadata.official_checksum, config.official_checksum),
            (metadata.spatial_role, SPATIAL_ROLE),
        )
        if any(actual != expected for actual, expected in expected_values):
            return None

        integrity = validate_ign_bdtopo_archive(archive_path, config)
        if (
            metadata.file_size != integrity.file_size
            or metadata.sha256 != integrity.sha256
            or metadata.official_checksum_validated
            != integrity.official_checksum_validated
        ):
            return None
        return _download_from_metadata(metadata, archive_path, cache_hit=True)
    except (
        IgnBdTopoArchiveError,
        OSError,
        TypeError,
        ValueError,
        ValidationError,
    ):
        return None
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_replace_file`

**Purpose:** Implements `replace file` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

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
- direct call: `landscout.sources.ign_bdtopo_fr::_publish_cache_pair` via `_replace_file`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_cache_pair` via `_replace_file`

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

**Purpose:** Implements `cache recovery paths` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

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
  - `(<br>        archive_path.with_name(f"{archive_path.name}.bak"),<br>        metadata_path.with_name(f"{metadata_path.name}.bak"),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_require_no_cache_recovery_material` via `_cache_recovery_paths`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_require_no_cache_recovery_material` via `_cache_recovery_paths`
- direct call: `landscout.sources.ign_bdtopo_fr::_publish_cache_pair` via `_cache_recovery_paths`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_cache_pair` via `_cache_recovery_paths`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |

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
        archive_path.with_name(f"{archive_path.name}.bak"),
        metadata_path.with_name(f"{metadata_path.name}.bak"),
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_require_no_cache_recovery_material`

**Purpose:** Implements `require no cache recovery material` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

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
  - `IgnBdTopoDownloadError(<br>            "IGN cache recovery backup already exists; manual recovery is required"<br>        )` under lexical guard `any(<br>        path.exists() or path.is_symlink() or path.is_junction()<br>        for path in recovery_paths<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_publish_cache_pair` via `_require_no_cache_recovery_material`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_cache_pair` via `_require_no_cache_recovery_material`
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_require_no_cache_recovery_material`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_require_no_cache_recovery_material`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_cache_recovery_paths` | `landscout.sources.ign_bdtopo_fr._cache_recovery_paths` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDownloadError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownloadError` |

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
    if any(
        path.exists() or path.is_symlink() or path.is_junction()
        for path in recovery_paths
    ):
        raise IgnBdTopoDownloadError(
            "IGN cache recovery backup already exists; manual recovery is required"
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_prepare_temporary_cache_file`

**Purpose:** Implements `prepare temporary cache file` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

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
  - `IgnBdTopoDownloadError(<br>                "IGN cache temporary path is a link or junction"<br>            )` under lexical guard `path.is_symlink() or path.is_junction()`.
  - `IgnBdTopoDownloadError(<br>                    "IGN cache temporary path is not a regular file"<br>                )` under lexical guard `path.exists()`.
  - `re-raise`.
  - `IgnBdTopoDownloadError(<br>            "IGN cache temporary path cannot be prepared safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_prepare_temporary_cache_file`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_prepare_temporary_cache_file`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDownloadError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownloadError` |
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
        if path.is_symlink() or path.is_junction():
            raise IgnBdTopoDownloadError(
                "IGN cache temporary path is a link or junction"
            )
        if path.exists():
            if not path.is_file():
                raise IgnBdTopoDownloadError(
                    "IGN cache temporary path is not a regular file"
                )
            path.unlink()
    except IgnBdTopoDownloadError:
        raise
    except OSError as error:
        raise IgnBdTopoDownloadError(
            "IGN cache temporary path cannot be prepared safely"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_cleanup_temporary_cache_files`

**Purpose:** Implements `cleanup temporary cache files` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

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
  - `IgnBdTopoDownloadError(<br>            "IGN cache temporary files could not be cleaned safely"<br>        )` under lexical guard `cleanup_error is not None and primary_error is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_cleanup_temporary_cache_files`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_cleanup_temporary_cache_files`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDownloadError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownloadError` |

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
        raise IgnBdTopoDownloadError(
            "IGN cache temporary files could not be cleaned safely"
        ) from cleanup_error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_publish_cache_pair`

**Purpose:** Implements `publish cache pair` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

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
  - `IgnBdTopoDownloadError(<br>                "IGN cache publication and rollback both failed"<br>            )`.
  - `re-raise`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_publish_cache_pair`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `_publish_cache_pair`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `ign_bdtopo_fr._publish_cache_pair`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `ign_bdtopo_fr._publish_cache_pair`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_cache_recovery_paths` | `landscout.sources.ign_bdtopo_fr._cache_recovery_paths` |
| `archive_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_no_cache_recovery_material` | `landscout.sources.ign_bdtopo_fr._require_no_cache_recovery_material` |
| `copy2` | `shutil.copy2` |
| `archive_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_file` | `landscout.sources.ign_bdtopo_fr._replace_file` |
| `archive_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDownloadError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownloadError` |

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
            if not metadata_existed:
                metadata_path.unlink(missing_ok=True)
        except (IgnBdTopoArchiveError, OSError) as rollback_error:
            raise IgnBdTopoDownloadError(
                "IGN cache publication and rollback both failed"
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

### `download_ign_bdtopo_archive`

**Purpose:** Download or reuse the pinned IGN package with atomic cache publication.

**Exact signature**

```python
def download_ign_bdtopo_archive(
    config: IgnBdTopoSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> IgnBdTopoDownload:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `cache_dir` | positional-or-keyword | `Path` | `DEFAULT_CACHE_DIR` |
| `timeout` | positional-or-keyword | `float` | `120.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `cached`
  - `result`
- Explicit raise paths:
  - `re-raise`.
  - `IgnBdTopoDownloadError(f"IGN download failed: {source_url}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_download_revalidates_a_tampered_config_before_network` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_revalidates_a_tampered_config_before_network` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `download_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `download_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `download_ign_bdtopo_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.ign_bdtopo_fr._validated_source_config` |
| `_archive_filename` | `landscout.sources.ign_bdtopo_fr._archive_filename` |
| `_require_no_cache_recovery_material` | `landscout.sources.ign_bdtopo_fr._require_no_cache_recovery_material` |
| `_load_cached_download` | `landscout.sources.ign_bdtopo_fr._load_cached_download` |
| `cache_dir.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `_prepare_temporary_cache_file` | `landscout.sources.ign_bdtopo_fr._prepare_temporary_cache_file` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `temporary_archive.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `copyfileobj` | `shutil.copyfileobj` |
| `validate_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.validate_ign_bdtopo_archive` |
| `datetime.now(UTC).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `IgnBdTopoDownload` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownload` |
| `_cache_metadata_from_download` | `landscout.sources.ign_bdtopo_fr._cache_metadata_from_download` |
| `temporary_metadata.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata.model_dump_json` | `unresolved local/third-party receiver; no ownership inferred` |
| `_publish_cache_pair` | `landscout.sources.ign_bdtopo_fr._publish_cache_pair` |
| `IgnBdTopoDownloadError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownloadError` |
| `_cleanup_temporary_cache_files` | `landscout.sources.ign_bdtopo_fr._cleanup_temporary_cache_files` |
| `sys.exception` | `sys.exception` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | `temporary_archive.open`<br>`temporary_metadata.open` |
| Filesystem/archive write or publication | `cache_dir.mkdir`<br>`copyfileobj` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def download_ign_bdtopo_archive(
    config: IgnBdTopoSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> IgnBdTopoDownload:
    """Download or reuse the pinned IGN package with atomic cache publication."""

    config = _validated_source_config(config)
    filename = _archive_filename(config)
    archive_path = cache_dir / filename
    metadata_path = cache_dir / f"{filename}.metadata.json"
    _require_no_cache_recovery_material(archive_path, metadata_path)
    cached = _load_cached_download(archive_path, metadata_path, config)
    if cached is not None:
        return cached

    cache_dir.mkdir(parents=True, exist_ok=True)
    temporary_archive = archive_path.with_name(f"{archive_path.name}.part")
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    _prepare_temporary_cache_file(temporary_archive)
    _prepare_temporary_cache_file(temporary_metadata)
    source_url = str(config.source_url)
    try:
        with (
            open_safe_https(
                source_url,
                timeout=timeout,
                headers={"User-Agent": "LandScout-AI/0.1"},
            ) as response,
            temporary_archive.open("xb") as output,
        ):
            copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)

        integrity = validate_ign_bdtopo_archive(temporary_archive, config)
        download_timestamp = datetime.now(UTC).isoformat()
        result = IgnBdTopoDownload(
            provider=config.provider,
            product=config.product,
            department_code=config.department_code,
            edition=config.edition,
            product_version=config.product_version,
            projection=config.projection,
            package_format=config.format,
            archive_format=config.archive_format,
            source_url=source_url,
            checksum_url=(
                str(config.checksum_url) if config.checksum_url is not None else None
            ),
            download_timestamp=download_timestamp,
            filename=filename,
            file_size=integrity.file_size,
            sha256=integrity.sha256,
            official_checksum_algorithm=integrity.official_checksum_algorithm,
            official_checksum=integrity.official_checksum,
            official_checksum_validated=integrity.official_checksum_validated,
            path=archive_path,
            cache_hit=False,
        )
        metadata = _cache_metadata_from_download(result)
        with temporary_metadata.open("x", encoding="utf-8") as output:
            output.write(metadata.model_dump_json(indent=2) + "\n")
        _publish_cache_pair(
            temporary_archive, temporary_metadata, archive_path, metadata_path
        )
        return result
    except IgnBdTopoArchiveError:
        raise
    except (HTTPError, URLError, OSError) as error:
        raise IgnBdTopoDownloadError(f"IGN download failed: {source_url}") from error
    finally:
        _cleanup_temporary_cache_files(
            (temporary_archive, temporary_metadata),
            sys.exception(),
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_windows_component_key`

**Purpose:** Implements `windows component key` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _windows_component_key(component: str) -> str:
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
  - `IgnBdTopoArchiveError(<br>            "IGN archive contains a Windows-unsafe path component"<br>        )` under lexical guard `not normalized<br>        or normalized in {".", ".."}<br>        or normalized != normalized.strip()<br>        or normalized.endswith((".", " "))<br>        or any(ord(character) < 32 or ord(character) == 127 for character in normalized)<br>        or any(character in _WINDOWS_FORBIDDEN for character in normalized)`.
  - `IgnBdTopoArchiveError(<br>            "IGN archive contains a reserved Windows device name"<br>        )` under lexical guard `reserved_stem in _WINDOWS_RESERVED`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_archive_members` via `_windows_component_key`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_archive_members` via `_windows_component_key`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `unicodedata.normalize` | `unicodedata.normalize` |
| `normalized.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ord` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `normalized.split(".", maxsplit=1)[0].casefold` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _windows_component_key(component: str) -> str:
    normalized = unicodedata.normalize("NFKC", component)
    if (
        not normalized
        or normalized in {".", ".."}
        or normalized != normalized.strip()
        or normalized.endswith((".", " "))
        or any(ord(character) < 32 or ord(character) == 127 for character in normalized)
        or any(character in _WINDOWS_FORBIDDEN for character in normalized)
    ):
        raise IgnBdTopoArchiveError(
            "IGN archive contains a Windows-unsafe path component"
        )
    reserved_stem = normalized.split(".", maxsplit=1)[0].casefold()
    if reserved_stem in _WINDOWS_RESERVED:
        raise IgnBdTopoArchiveError(
            "IGN archive contains a reserved Windows device name"
        )
    return normalized.casefold()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_archive_members`

**Purpose:** Implements `validate archive members` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _validate_archive_members(
    archive: py7zr.SevenZipFile,
) -> tuple[_ValidatedArchiveMember, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[_ValidatedArchiveMember, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `archive` | positional-or-keyword | `py7zr.SevenZipFile` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(<br>        sorted(<br>            destinations.values(),<br>            key=lambda entry: (<br>                unicodedata.normalize("NFKC", entry.relative_path).casefold(),<br>                entry.relative_path,<br>            ),<br>        )<br>    )`
- Explicit raise paths:
  - `IgnBdTopoArchiveError("IGN archive must not be encrypted")` under lexical guard `archive.needs_password()`.
  - `re-raise`.
  - `IgnBdTopoArchiveError(<br>            "IGN archive member inventory is unreadable"<br>        )`.
  - `IgnBdTopoArchiveError("IGN archive contains no members")` under lexical guard `not infos`.
  - `IgnBdTopoArchiveError("IGN archive contains an invalid member name")` under lexical guard `type(name) is not str or not name or "\x00" in name`.
  - `IgnBdTopoArchiveError(<br>                "IGN archive contains a duplicate raw member name"<br>            )` under lexical guard `name in raw_names`.
  - `IgnBdTopoArchiveError(<br>                f"IGN archive contains an unsafe member path: {name}"<br>            )` under lexical guard `not normalized_name<br>            or any(part in {"", ".", ".."} for part in raw_parts)<br>            or posix_path.is_absolute()<br>            or windows_path.is_absolute()<br>            or bool(windows_path.drive)`.
  - `IgnBdTopoArchiveError(<br>                f"IGN archive contains an unsupported link or encrypted member: {name}"<br>            )` under lexical guard `bool(getattr(info, "is_symlink", False)) or bool(<br>            getattr(info, "encrypted", False)<br>        )`.
  - `IgnBdTopoArchiveError(<br>                f"IGN archive contains an unsupported special member: {name}"<br>            )` under lexical guard `not (is_file ^ is_directory)`.
  - `IgnBdTopoArchiveError(<br>                "IGN archive contains a case-insensitive or Unicode destination collision"<br>            )` under lexical guard `key in explicit_destinations`.
  - `IgnBdTopoArchiveError(<br>                    "IGN archive contains a parent-file destination conflict"<br>                )` under lexical guard `parent is not None and parent.kind == "file"`.
  - `IgnBdTopoArchiveError(<br>                "IGN archive contains a file/directory destination conflict"<br>            )` under lexical guard `existing is not None and existing.kind != kind`.
  - `IgnBdTopoArchiveError(<br>                "IGN archive contains a parent-file destination conflict"<br>            )` under lexical guard `kind == "file" and any(<br>            len(other_key) > len(key) and other_key[: len(key)] == key<br>            for other_key in destinations<br>        )`.
  - `IgnBdTopoArchiveError(<br>                "IGN archive contains an invalid file-size inventory"<br>            )` under lexical guard `kind == "file" and (type(raw_size) is not int or raw_size < 0)`.
  - `IgnBdTopoArchiveError(<br>            "Expected exactly one GeoPackage in the IGN archive inventory"<br>        )` under lexical guard `len(geopackages) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_validate_archive_members`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_validate_archive_members`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_windows_unsafe_member_names_fail_closed` via `ign_bdtopo_fr._validate_archive_members`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_casefold_and_nfkc_destination_collisions_fail` via `ign_bdtopo_fr._validate_archive_members`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_nfkc_separator_destinations_fail_closed` via `ign_bdtopo_fr._validate_archive_members`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_parent_file_conflict_fails_closed` via `ign_bdtopo_fr._validate_archive_members`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_7z_encrypted_archive_fails_closed` via `ign_bdtopo_fr._validate_archive_members`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive.needs_password` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `archive.list` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_names.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_name.rstrip` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_name.split` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `PureWindowsPath` | `pathlib.PureWindowsPath` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `posix_path.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `windows_path.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_windows_component_key` | `landscout.sources.ign_bdtopo_fr._windows_component_key` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `"/".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `destinations.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `destinations.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `_ValidatedArchiveMember` | `landscout.sources.ign_bdtopo_fr._ValidatedArchiveMember` |
| `destinations.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath(entry.relative_path).suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `raw_names.add(name)`<br>`explicit_destinations[key] = name`<br>`destinations.setdefault(<br>                parent_key,<br>                _ValidatedArchiveMember(parent_path, "directory", None),<br>            )`<br>`destinations[key] = _ValidatedArchiveMember(<br>            "/".join(raw_parts),<br>            kind,<br>            raw_size if kind == "file" else None,<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_archive_members(
    archive: py7zr.SevenZipFile,
) -> tuple[_ValidatedArchiveMember, ...]:
    try:
        if archive.needs_password():
            raise IgnBdTopoArchiveError("IGN archive must not be encrypted")
        infos = archive.list()
    except IgnBdTopoArchiveError:
        raise
    except Exception as error:
        raise IgnBdTopoArchiveError(
            "IGN archive member inventory is unreadable"
        ) from error
    if not infos:
        raise IgnBdTopoArchiveError("IGN archive contains no members")

    raw_names: set[str] = set()
    explicit_destinations: dict[tuple[str, ...], str] = {}
    destinations: dict[tuple[str, ...], _ValidatedArchiveMember] = {}
    for info in infos:
        name = info.filename
        if type(name) is not str or not name or "\x00" in name:
            raise IgnBdTopoArchiveError("IGN archive contains an invalid member name")
        if name in raw_names:
            raise IgnBdTopoArchiveError(
                "IGN archive contains a duplicate raw member name"
            )
        raw_names.add(name)
        normalized_name = name.replace("\\", "/")
        is_directory = bool(info.is_directory)
        if is_directory:
            normalized_name = normalized_name.rstrip("/")
        raw_parts = normalized_name.split("/")
        posix_path = PurePosixPath(normalized_name)
        windows_path = PureWindowsPath(name)
        if (
            not normalized_name
            or any(part in {"", ".", ".."} for part in raw_parts)
            or posix_path.is_absolute()
            or windows_path.is_absolute()
            or bool(windows_path.drive)
        ):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsafe member path: {name}"
            )
        if bool(getattr(info, "is_symlink", False)) or bool(
            getattr(info, "encrypted", False)
        ):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsupported link or encrypted member: {name}"
            )
        is_file = bool(info.is_file)
        if not (is_file ^ is_directory):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsupported special member: {name}"
            )

        key = tuple(_windows_component_key(part) for part in raw_parts)
        if key in explicit_destinations:
            raise IgnBdTopoArchiveError(
                "IGN archive contains a case-insensitive or Unicode destination collision"
            )
        explicit_destinations[key] = name
        kind: Literal["file", "directory"] = "directory" if is_directory else "file"
        for depth in range(1, len(key)):
            parent_key = key[:depth]
            parent_path = "/".join(raw_parts[:depth])
            parent = destinations.get(parent_key)
            if parent is not None and parent.kind == "file":
                raise IgnBdTopoArchiveError(
                    "IGN archive contains a parent-file destination conflict"
                )
            destinations.setdefault(
                parent_key,
                _ValidatedArchiveMember(parent_path, "directory", None),
            )
        existing = destinations.get(key)
        if existing is not None and existing.kind != kind:
            raise IgnBdTopoArchiveError(
                "IGN archive contains a file/directory destination conflict"
            )
        if kind == "file" and any(
            len(other_key) > len(key) and other_key[: len(key)] == key
            for other_key in destinations
        ):
            raise IgnBdTopoArchiveError(
                "IGN archive contains a parent-file destination conflict"
            )
        raw_size = getattr(info, "uncompressed", None)
        if kind == "file" and (type(raw_size) is not int or raw_size < 0):
            raise IgnBdTopoArchiveError(
                "IGN archive contains an invalid file-size inventory"
            )
        destinations[key] = _ValidatedArchiveMember(
            "/".join(raw_parts),
            kind,
            raw_size if kind == "file" else None,
        )

    files = [entry for entry in destinations.values() if entry.kind == "file"]
    geopackages = [
        entry
        for entry in files
        if PurePosixPath(entry.relative_path).suffix.casefold() == ".gpkg"
    ]
    if len(geopackages) != 1:
        raise IgnBdTopoArchiveError(
            "Expected exactly one GeoPackage in the IGN archive inventory"
        )
    return tuple(
        sorted(
            destinations.values(),
            key=lambda entry: (
                unicodedata.normalize("NFKC", entry.relative_path).casefold(),
                entry.relative_path,
            ),
        )
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `discover_ign_bdtopo_geopackage`

**Purpose:** Return the sole GeoPackage below an extracted package root.

**Exact signature**

```python
def discover_ign_bdtopo_geopackage(root: Path) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `root`
  - `geopackages[0]`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(f"Expected a GeoPackage, got: {root}")` under lexical guard `root.is_file()`.
  - `IgnBdTopoArchiveError(f"Extraction directory does not exist: {root}")` under lexical guard `not root.is_dir()`.
  - `IgnBdTopoArchiveError(<br>            "Expected exactly one GeoPackage in the IGN package, found "<br>            f"{len(geopackages)}"<br>        )` under lexical guard `len(geopackages) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `discover_ign_bdtopo_geopackage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `discover_ign_bdtopo_geopackage`
- direct call: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `discover_ign_bdtopo_geopackage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `discover_ign_bdtopo_geopackage`
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `discover_ign_bdtopo_geopackage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `discover_ign_bdtopo_geopackage`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_geopackage_is_discovered_recursively` via `discover_ign_bdtopo_geopackage`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_geopackage_is_discovered_recursively` via `discover_ign_bdtopo_geopackage`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_multiple_geopackages_are_rejected_as_ambiguous` via `discover_ign_bdtopo_geopackage`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_multiple_geopackages_are_rejected_as_ambiguous` via `discover_ign_bdtopo_geopackage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `root.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `root.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.is_file`<br>`root.is_dir`<br>`path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def discover_ign_bdtopo_geopackage(root: Path) -> Path:
    """Return the sole GeoPackage below an extracted package root."""

    if root.is_file():
        if root.suffix.casefold() == ".gpkg":
            return root
        raise IgnBdTopoArchiveError(f"Expected a GeoPackage, got: {root}")
    if not root.is_dir():
        raise IgnBdTopoArchiveError(f"Extraction directory does not exist: {root}")
    geopackages = sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix.casefold() == ".gpkg"
        ),
        key=lambda path: path.as_posix().casefold(),
    )
    if len(geopackages) != 1:
        raise IgnBdTopoArchiveError(
            "Expected exactly one GeoPackage in the IGN package, found "
            f"{len(geopackages)}"
        )
    return geopackages[0]
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `list_ign_bdtopo_layers`

**Purpose:** List every real layer name exposed by an IGN GeoPackage.

**Exact signature**

```python
def list_ign_bdtopo_layers(geopackage_path: Path) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geopackage_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `names`
- Explicit raise paths:
  - `IgnBdTopoLayerError(f"GeoPackage does not exist: {geopackage_path}")` under lexical guard `not geopackage_path.is_file()`.
  - `IgnBdTopoLayerError(<br>            f"Cannot list layers in GeoPackage: {geopackage_path}"<br>        )`.
  - `IgnBdTopoLayerError("GeoPackage exposes no valid layer names")` under lexical guard `not names or any(not name.strip() for name in names)`.
  - `IgnBdTopoLayerError("GeoPackage exposes duplicate layer names")` under lexical guard `len(set(names)) != len(names)`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `list_ign_bdtopo_layers`
- value/type reference: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `list_ign_bdtopo_layers`
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `list_ign_bdtopo_layers`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `list_ign_bdtopo_layers`
- direct call: `landscout.sources.ign_bdtopo_fr::_verify_unchanged_extraction` via `list_ign_bdtopo_layers`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_verify_unchanged_extraction` via `list_ign_bdtopo_layers`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_real_layer_names_are_listed_and_discovered` via `list_ign_bdtopo_layers`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_real_layer_names_are_listed_and_discovered` via `list_ign_bdtopo_layers`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geopackage_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `pyogrio.list_layers` | `pyogrio.list_layers` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `geopackage_path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def list_ign_bdtopo_layers(geopackage_path: Path) -> tuple[str, ...]:
    """List every real layer name exposed by an IGN GeoPackage."""

    if not geopackage_path.is_file():
        raise IgnBdTopoLayerError(f"GeoPackage does not exist: {geopackage_path}")
    try:
        listed = pyogrio.list_layers(geopackage_path)
        names = tuple(str(row[0]) for row in listed)
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"Cannot list layers in GeoPackage: {geopackage_path}"
        ) from error
    if not names or any(not name.strip() for name in names):
        raise IgnBdTopoLayerError("GeoPackage exposes no valid layer names")
    if len(set(names)) != len(names):
        raise IgnBdTopoLayerError("GeoPackage exposes duplicate layer names")
    return names
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_matching_layers`

**Purpose:** Implements `matching layers` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _matching_layers(
    layer_names: tuple[str, ...], logical_config: IgnBdTopoLogicalLayerConfig
) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `layer_names` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `logical_config` | positional-or-keyword | `IgnBdTopoLogicalLayerConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(matches)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `_matching_layers`
- value/type reference: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `_matching_layers`
- direct call: `landscout.sources.ign_bdtopo_fr::_discover_department_coverage_layer` via `_matching_layers`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_department_coverage_layer` via `_matching_layers`
- direct call: `landscout.sources.ign_bdtopo_fr::_discover_road_layer` via `_matching_layers`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_road_layer` via `_matching_layers`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `token_words.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_words(token).split` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_words` | `landscout.sources.ign_bdtopo_fr._normalize_words` |
| `_normalize_words(layer_name).split` | `unresolved local/third-party receiver; no ownership inferred` |
| `token_words.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.append` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `token_words.update(_normalize_words(token).split())`<br>`matches.append(layer_name)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _matching_layers(
    layer_names: tuple[str, ...], logical_config: IgnBdTopoLogicalLayerConfig
) -> tuple[str, ...]:
    token_words: set[str] = set()
    for token in logical_config.match_tokens:
        token_words.update(_normalize_words(token).split())
    matches = []
    for layer_name in layer_names:
        layer_words = set(_normalize_words(layer_name).split())
        if token_words.issubset(layer_words):
            matches.append(layer_name)
    return tuple(matches)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `discover_ign_bdtopo_layers`

**Purpose:** Resolve both configured logical classes without assuming exact casing.

**Exact signature**

```python
def discover_ign_bdtopo_layers(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoLayerSelection:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoLayerSelection`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geopackage_path` | positional-or-keyword | `Path` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoLayerSelection(<br>        all_layer_names=layer_names,<br>        electric_lines_layer=electric_matches[0],<br>        transformation_posts_layer=post_matches[0],<br>    )`
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            "Expected one unambiguous electric-line layer for "<br>            f"'{config.logical_layers.electric_lines.class_label}', found "<br>            f"{len(electric_matches)}: {electric_matches}"<br>        )` under lexical guard `len(electric_matches) != 1`.
  - `IgnBdTopoLayerError(<br>            "Expected one unambiguous transformation-post layer for "<br>            f"'{config.logical_layers.transformation_posts.class_label}', found "<br>            f"{len(post_matches)}: {post_matches}"<br>        )` under lexical guard `len(post_matches) != 1`.
  - `IgnBdTopoLayerError(<br>            "Electric-line and transformation-post discovery selected the same layer"<br>        )` under lexical guard `electric_matches[0] == post_matches[0]`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `discover_ign_bdtopo_layers`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `discover_ign_bdtopo_layers`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_real_layer_names_are_listed_and_discovered` via `discover_ign_bdtopo_layers`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_real_layer_names_are_listed_and_discovered` via `discover_ign_bdtopo_layers`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_electric_line_layer_fails` via `discover_ign_bdtopo_layers`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_electric_line_layer_fails` via `discover_ign_bdtopo_layers`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_transformation_post_layer_fails` via `discover_ign_bdtopo_layers`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_transformation_post_layer_fails` via `discover_ign_bdtopo_layers`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_electric_line_layers_fail` via `discover_ign_bdtopo_layers`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_electric_line_layers_fail` via `discover_ign_bdtopo_layers`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.ign_bdtopo_fr._validated_source_config` |
| `list_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.list_ign_bdtopo_layers` |
| `_matching_layers` | `landscout.sources.ign_bdtopo_fr._matching_layers` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `IgnBdTopoLayerSelection` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerSelection` |

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
def discover_ign_bdtopo_layers(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoLayerSelection:
    """Resolve both configured logical classes without assuming exact casing."""

    config = _validated_source_config(config, error_type=IgnBdTopoLayerError)
    layer_names = list_ign_bdtopo_layers(geopackage_path)
    electric_matches = _matching_layers(
        layer_names, config.logical_layers.electric_lines
    )
    post_matches = _matching_layers(
        layer_names, config.logical_layers.transformation_posts
    )
    if len(electric_matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous electric-line layer for "
            f"'{config.logical_layers.electric_lines.class_label}', found "
            f"{len(electric_matches)}: {electric_matches}"
        )
    if len(post_matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous transformation-post layer for "
            f"'{config.logical_layers.transformation_posts.class_label}', found "
            f"{len(post_matches)}: {post_matches}"
        )
    if electric_matches[0] == post_matches[0]:
        raise IgnBdTopoLayerError(
            "Electric-line and transformation-post discovery selected the same layer"
        )
    return IgnBdTopoLayerSelection(
        all_layer_names=layer_names,
        electric_lines_layer=electric_matches[0],
        transformation_posts_layer=post_matches[0],
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_discover_department_coverage_layer`

**Purpose:** Implements `discover department coverage layer` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _discover_department_coverage_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `layer_names` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `matches[0]`
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            "Expected one unambiguous department coverage layer for "<br>            f"'{config.coverage.department_layer.class_label}', found "<br>            f"{len(matches)}: {matches}"<br>        )` under lexical guard `len(matches) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `_discover_department_coverage_layer`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `_discover_department_coverage_layer`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- direct call: `landscout.stages.assess_grid_coverage::_validate_configured_coverage_identity` via `_discover_department_coverage_layer`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_configured_coverage_identity` via `_discover_department_coverage_layer`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_discover_department_coverage_layer`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_discover_department_coverage_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_matching_layers` | `landscout.sources.ign_bdtopo_fr._matching_layers` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

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
def _discover_department_coverage_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
    matches = _matching_layers(layer_names, config.coverage.department_layer)
    if len(matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous department coverage layer for "
            f"'{config.coverage.department_layer.class_label}', found "
            f"{len(matches)}: {matches}"
        )
    return matches[0]
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_discover_road_layer`

**Purpose:** Implements `discover road layer` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _discover_road_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `layer_names` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `matches[0]`
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            "Expected one unambiguous road-segment layer for "<br>            f"'{config.access.road_segments.class_label}', found "<br>            f"{len(matches)}: {matches}"<br>        )` under lexical guard `len(matches) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `_discover_road_layer`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `_discover_road_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_matching_layers` | `landscout.sources.ign_bdtopo_fr._matching_layers` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

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
def _discover_road_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
    matches = _matching_layers(layer_names, config.access.road_segments)
    if len(matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous road-segment layer for "
            f"'{config.access.road_segments.class_label}', found "
            f"{len(matches)}: {matches}"
        )
    return matches[0]
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_discover_configured_physical_roles`

**Purpose:** Implements `discover configured physical roles` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _discover_configured_physical_roles(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> _ConfiguredPhysicalRoles:
```

- Exact decorators: none.
- Declared return annotation: `_ConfiguredPhysicalRoles`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geopackage_path` | positional-or-keyword | `Path` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_ConfiguredPhysicalRoles(<br>        all_layer_names=electricity.all_layer_names,<br>        electric_lines_layer=electricity.electric_lines_layer,<br>        transformation_posts_layer=electricity.transformation_posts_layer,<br>        road_segments_layer=road,<br>        department_layer=department,<br>    )`
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            "IGN electric-line, transformation-post, road, and department roles "<br>            "must use four distinct physical layers"<br>        )` under lexical guard `len(set(selected)) != len(selected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_discover_configured_physical_roles`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_discover_configured_physical_roles`
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_discover_configured_physical_roles`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_discover_configured_physical_roles`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_discover_configured_physical_roles`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_discover_configured_physical_roles`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_discover_configured_physical_roles`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_discover_configured_physical_roles`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_discover_configured_physical_roles`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_discover_configured_physical_roles`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `discover_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_layers` |
| `_discover_road_layer` | `landscout.sources.ign_bdtopo_fr._discover_road_layer` |
| `_discover_department_coverage_layer` | `landscout.sources.ign_bdtopo_fr._discover_department_coverage_layer` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `_ConfiguredPhysicalRoles` | `landscout.sources.ign_bdtopo_fr._ConfiguredPhysicalRoles` |

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
def _discover_configured_physical_roles(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> _ConfiguredPhysicalRoles:
    electricity = discover_ign_bdtopo_layers(geopackage_path, config)
    road = _discover_road_layer(electricity.all_layer_names, config)
    department = _discover_department_coverage_layer(
        electricity.all_layer_names,
        config,
    )
    selected = (
        electricity.electric_lines_layer,
        electricity.transformation_posts_layer,
        road,
        department,
    )
    if len(set(selected)) != len(selected):
        raise IgnBdTopoLayerError(
            "IGN electric-line, transformation-post, road, and department roles "
            "must use four distinct physical layers"
        )
    return _ConfiguredPhysicalRoles(
        all_layer_names=electricity.all_layer_names,
        electric_lines_layer=electricity.electric_lines_layer,
        transformation_posts_layer=electricity.transformation_posts_layer,
        road_segments_layer=road,
        department_layer=department,
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_safe_relative_path`

**Purpose:** Implements `safe relative path` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _safe_relative_path(path: Path, root: Path) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path.resolve().relative_to(root.resolve()).as_posix()`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>            f"Extracted GeoPackage escapes its extraction root: {path}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_safe_relative_path`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_safe_relative_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.resolve().relative_to(root.resolve()).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.resolve().relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |

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
def _safe_relative_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except (OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"Extracted GeoPackage escapes its extraction root: {path}"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_resolve_relative_path`

**Purpose:** Implements `resolve relative path` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _resolve_relative_path(root: Path, relative_path: str) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `relative_path` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `candidate`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>            "Cached extraction metadata contains an unsafe GeoPackage path"<br>        )` under lexical guard `not relative_path<br>        or posix_path.is_absolute()<br>        or windows_path.is_absolute()<br>        or bool(windows_path.drive)<br>        or ".." in posix_path.parts`.
  - `IgnBdTopoArchiveError(<br>            "Cached GeoPackage path escapes its extraction root"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_resolve_relative_path`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_resolve_relative_path`
- direct call: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_resolve_relative_path`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_resolve_relative_path`
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_resolve_relative_path`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_resolve_relative_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `PureWindowsPath` | `pathlib.PureWindowsPath` |
| `posix_path.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `windows_path.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `root.joinpath` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidate.resolve().relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidate.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.resolve` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _resolve_relative_path(root: Path, relative_path: str) -> Path:
    posix_path = PurePosixPath(relative_path)
    windows_path = PureWindowsPath(relative_path)
    if (
        not relative_path
        or posix_path.is_absolute()
        or windows_path.is_absolute()
        or bool(windows_path.drive)
        or ".." in posix_path.parts
    ):
        raise IgnBdTopoArchiveError(
            "Cached extraction metadata contains an unsafe GeoPackage path"
        )
    candidate = root.joinpath(*posix_path.parts)
    try:
        candidate.resolve().relative_to(root.resolve())
    except (OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            "Cached GeoPackage path escapes its extraction root"
        ) from error
    return candidate
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_geopackage_integrity`

**Purpose:** Implements `geopackage integrity` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _geopackage_integrity(path: Path) -> tuple[int, str]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[int, str]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `size_bytes, digest.hexdigest()`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(f"IGN GeoPackage does not exist: {path}")` under lexical guard `not path.is_file()`.
  - `IgnBdTopoArchiveError(f"Cannot inspect IGN GeoPackage: {path}")`.
  - `IgnBdTopoArchiveError(f"IGN GeoPackage is empty: {path}")` under lexical guard `size_bytes <= 0`.
  - `IgnBdTopoArchiveError(f"Cannot read IGN GeoPackage: {path}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_geopackage_integrity`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_geopackage_integrity`
- direct call: `landscout.sources.ign_bdtopo_fr::_verify_unchanged_extraction` via `_geopackage_integrity`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_verify_unchanged_extraction` via `_geopackage_integrity`
- direct call: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_geopackage_integrity`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_geopackage_integrity`
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_geopackage_integrity`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_geopackage_integrity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
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
| Filesystem/archive read or metadata access | `path.is_file`<br>`path.stat`<br>`path.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `digest.update(chunk)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _geopackage_integrity(path: Path) -> tuple[int, str]:
    if not path.is_file():
        raise IgnBdTopoArchiveError(f"IGN GeoPackage does not exist: {path}")
    try:
        size_bytes = path.stat().st_size
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot inspect IGN GeoPackage: {path}") from error
    if size_bytes <= 0:
        raise IgnBdTopoArchiveError(f"IGN GeoPackage is empty: {path}")
    digest = sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
                digest.update(chunk)
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot read IGN GeoPackage: {path}") from error
    return size_bytes, digest.hexdigest()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_regular_file_sha256`

**Purpose:** Implements `regular file sha256` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _regular_file_sha256(path: Path) -> str:
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
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>            f"Cannot hash extracted IGN file: {path}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_inventory_extracted_tree` via `_regular_file_sha256`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_inventory_extracted_tree` via `_regular_file_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sha256` | `hashlib.sha256` |
| `path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `iter` | `unresolved local/third-party receiver; no ownership inferred` |
| `digest.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
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
def _regular_file_sha256(path: Path) -> str:
    digest = sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
                digest.update(chunk)
    except OSError as error:
        raise IgnBdTopoArchiveError(
            f"Cannot hash extracted IGN file: {path}"
        ) from error
    return digest.hexdigest()
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_inventory_extracted_tree`

**Purpose:** Implements `inventory extracted tree` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _inventory_extracted_tree(
    root: Path,
    *,
    exclude_relative_path: str | None = None,
) -> tuple[_ExtractedEntryMetadata, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[_ExtractedEntryMetadata, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `exclude_relative_path` | keyword-only | `str \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(<br>            sorted(<br>                entries,<br>                key=lambda entry: (<br>                    unicodedata.normalize("NFKC", entry.relative_path).casefold(),<br>                    entry.relative_path,<br>                ),<br>            )<br>        )`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>                "IGN extraction root must be a regular non-linked directory"<br>            )` under lexical guard `root.is_symlink() or root.is_junction() or not root.is_dir()`.
  - `IgnBdTopoArchiveError(<br>                        "IGN extraction contains a link, junction, or special directory"<br>                    )` under lexical guard `path.is_symlink() or path.is_junction() or not path.is_dir()`.
  - `IgnBdTopoArchiveError(<br>                        "IGN extraction contains a link, junction, or special file"<br>                    )` under lexical guard `path.is_symlink() or path.is_junction() or not path.is_file()`.
  - `re-raise`.
  - `IgnBdTopoArchiveError(<br>            "IGN extracted inventory cannot be inspected safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_extracted_inventory` via `_inventory_extracted_tree`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extracted_inventory` via `_inventory_extracted_tree`
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_inventory_extracted_tree`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_inventory_extracted_tree`
- direct call: `landscout.sources.ign_bdtopo_fr::_verify_unchanged_extraction` via `_inventory_extracted_tree`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_verify_unchanged_extraction` via `_inventory_extracted_tree`
- direct call: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_inventory_extracted_tree`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_inventory_extracted_tree`
- direct call: `landscout.sources.ign_bdtopo_fr::_remove_validated_extraction_directory` via `_inventory_extracted_tree`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_remove_validated_extraction_directory` via `_inventory_extracted_tree`
- direct call: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_inventory_extracted_tree`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_inventory_extracted_tree`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `root.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `os.walk` | `os.walk` |
| `Path` | `pathlib.Path` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to(root).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `entries.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_ExtractedEntryMetadata` | `landscout.sources.ign_bdtopo_fr._ExtractedEntryMetadata` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_regular_file_sha256` | `landscout.sources.ign_bdtopo_fr._regular_file_sha256` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.is_dir`<br>`path.is_dir`<br>`path.is_file`<br>`path.stat` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_regular_file_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `entries.append(<br>                    _ExtractedEntryMetadata(<br>                        relative_path=relative,<br>                        kind="directory",<br>                    )<br>                )`<br>`entries.append(<br>                    _ExtractedEntryMetadata(<br>                        relative_path=relative,<br>                        kind="file",<br>                        size_bytes=size,<br>                        sha256=_regular_file_sha256(path),<br>                    )<br>                )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _inventory_extracted_tree(
    root: Path,
    *,
    exclude_relative_path: str | None = None,
) -> tuple[_ExtractedEntryMetadata, ...]:
    try:
        if root.is_symlink() or root.is_junction() or not root.is_dir():
            raise IgnBdTopoArchiveError(
                "IGN extraction root must be a regular non-linked directory"
            )
        entries: list[_ExtractedEntryMetadata] = []
        for current_root, directory_names, file_names in os.walk(
            root,
            topdown=True,
            followlinks=False,
        ):
            current = Path(current_root)
            for name in sorted(directory_names):
                path = current / name
                if path.is_symlink() or path.is_junction() or not path.is_dir():
                    raise IgnBdTopoArchiveError(
                        "IGN extraction contains a link, junction, or special directory"
                    )
                relative = path.relative_to(root).as_posix()
                entries.append(
                    _ExtractedEntryMetadata(
                        relative_path=relative,
                        kind="directory",
                    )
                )
            for name in sorted(file_names):
                path = current / name
                relative = path.relative_to(root).as_posix()
                if relative == exclude_relative_path:
                    continue
                if path.is_symlink() or path.is_junction() or not path.is_file():
                    raise IgnBdTopoArchiveError(
                        "IGN extraction contains a link, junction, or special file"
                    )
                size = path.stat().st_size
                entries.append(
                    _ExtractedEntryMetadata(
                        relative_path=relative,
                        kind="file",
                        size_bytes=size,
                        sha256=_regular_file_sha256(path),
                    )
                )
        return tuple(
            sorted(
                entries,
                key=lambda entry: (
                    unicodedata.normalize("NFKC", entry.relative_path).casefold(),
                    entry.relative_path,
                ),
            )
        )
    except IgnBdTopoArchiveError:
        raise
    except OSError as error:
        raise IgnBdTopoArchiveError(
            "IGN extracted inventory cannot be inspected safely"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_extracted_inventory`

**Purpose:** Implements `validate extracted inventory` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _validate_extracted_inventory(
    root: Path,
    expected: tuple[_ValidatedArchiveMember, ...],
) -> tuple[_ExtractedEntryMetadata, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[_ExtractedEntryMetadata, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `expected` | positional-or-keyword | `tuple[_ValidatedArchiveMember, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `actual`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>            "IGN extracted destination inventory differs from the validated archive"<br>        )` under lexical guard `actual_facts != expected_facts`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_validate_extracted_inventory`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_validate_extracted_inventory`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extracted_inventory_mismatch_fails_closed` via `ign_bdtopo_fr._validate_extracted_inventory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inventory_extracted_tree` | `landscout.sources.ign_bdtopo_fr._inventory_extracted_tree` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |

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
def _validate_extracted_inventory(
    root: Path,
    expected: tuple[_ValidatedArchiveMember, ...],
) -> tuple[_ExtractedEntryMetadata, ...]:
    actual = _inventory_extracted_tree(root)
    actual_facts = {
        entry.relative_path: (entry.kind, entry.size_bytes) for entry in actual
    }
    expected_facts = {
        entry.relative_path: (entry.kind, entry.size_bytes) for entry in expected
    }
    if actual_facts != expected_facts:
        raise IgnBdTopoArchiveError(
            "IGN extracted destination inventory differs from the validated archive"
        )
    return actual
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_valid_layer_inventory`

**Purpose:** Implements `valid layer inventory` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _valid_layer_inventory(value: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `type(value) is tuple<br>        and bool(value)<br>        and all(<br>            isinstance(name, str) and bool(name) and name == name.strip()<br>            for name in value<br>        )<br>        and len(set(value)) == len(value)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_valid_layer_inventory`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_valid_layer_inventory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _valid_layer_inventory(value: object) -> bool:
    return (
        type(value) is tuple
        and bool(value)
        and all(
            isinstance(name, str) and bool(name) and name == name.strip()
            for name in value
        )
        and len(set(value)) == len(value)
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_extraction_envelope`

**Purpose:** Bind one extraction envelope to its schema-v3 marker and current GPKG.

**Exact signature**

```python
def _validate_extraction_envelope(
    extraction: object,
) -> _VerifiedIgnExtraction:
```

- Exact decorators: none.
- Declared return annotation: `_VerifiedIgnExtraction`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_VerifiedIgnExtraction(<br>            extraction=extraction,<br>            metadata=metadata,<br>            geopackage_path=discovered_path,<br>        )`
- Explicit raise paths:
  - `TypeError("IGN extraction must be an exact IgnBdTopoExtraction")` under lexical guard `type(extraction) is not IgnBdTopoExtraction`.
  - `TypeError("IGN extraction archive type is invalid")` under lexical guard `type(extraction.archive) is not IgnBdTopoDownload`.
  - `ValueError("IGN extraction lineage must be PROXY_GEOMETRY")` under lexical guard `extraction.spatial_role != SPATIAL_ROLE or (<br>            extraction.archive.spatial_role != SPATIAL_ROLE<br>        )`.
  - `ValueError("IGN archive SHA256 lineage is invalid")` under lexical guard `not isinstance(extraction.archive.sha256, str)<br>            or re.fullmatch(r"[0-9a-f]{64}", extraction.archive.sha256) is None`.
  - `ValueError("IGN extraction GeoPackage size is invalid")` under lexical guard `type(extraction.geopackage_size_bytes) is not int<br>            or extraction.geopackage_size_bytes <= 0`.
  - `ValueError("IGN extraction GeoPackage SHA256 is invalid")` under lexical guard `not isinstance(extraction.geopackage_sha256, str)<br>            or re.fullmatch(r"[0-9a-f]{64}", extraction.geopackage_sha256) is None`.
  - `TypeError("IGN extraction paths are invalid")` under lexical guard `not isinstance(extraction.extraction_path, Path) or not isinstance(<br>            extraction.geopackage_path, Path<br>        )`.
  - `ValueError("IGN schema-v3 extraction metadata is missing")` under lexical guard `marker_path.is_symlink()<br>            or marker_path.is_junction()<br>            or not marker_path.is_file()`.
  - `ValueError("IGN extraction GeoPackage path is inconsistent")` under lexical guard `expected_path.resolve() != discovered_path.resolve()<br>            or extraction.geopackage_path.resolve() != discovered_path.resolve()<br>            or extraction.geopackage_filename != discovered_path.name`.
  - `ValueError("IGN extraction archive lineage differs from metadata")` under lexical guard `metadata.archive_sha256 != extraction.archive.sha256`.
  - `ValueError("IGN extraction spatial role differs from metadata")` under lexical guard `metadata.spatial_role != extraction.spatial_role`.
  - `ValueError("IGN extraction layer inventory is invalid")` under lexical guard `not _valid_layer_inventory(extraction.all_layer_names)`.
  - `ValueError("IGN extraction layer inventory differs from metadata")` under lexical guard `metadata.all_layer_names != extraction.all_layer_names`.
  - `ValueError("IGN extraction physical roles differ from metadata")` under lexical guard `selected_roles != (<br>            metadata.electric_lines_layer,<br>            metadata.transformation_posts_layer,<br>            metadata.road_segments_layer,<br>            metadata.department_layer,<br>        )`.
  - `ValueError("IGN extraction physical roles are invalid")` under lexical guard `len(set(selected_roles)) != 4 or any(<br>            role not in extraction.all_layer_names for role in selected_roles<br>        )`.
  - `ValueError(<br>                "IGN extraction GeoPackage integrity differs from metadata"<br>            )` under lexical guard `metadata.geopackage_size_bytes != extraction.geopackage_size_bytes<br>            or metadata.geopackage_sha256 != extraction.geopackage_sha256`.
  - `ValueError("IGN physical GeoPackage integrity changed")` under lexical guard `current_size != extraction.geopackage_size_bytes<br>            or current_sha != extraction.geopackage_sha256`.
  - `ValueError("IGN physical GeoPackage layer inventory changed")` under lexical guard `current_layers != extraction.all_layer_names`.
  - `ValueError("IGN complete extracted-file inventory changed")` under lexical guard `current_entries != metadata.extracted_entries`.
  - `re-raise`.
  - `IgnBdTopoLayerError(<br>            "IGN extraction physical integrity changed or is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_validate_extraction_envelope`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_validate_extraction_envelope`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_validate_extraction_envelope`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_validate_extraction_envelope`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_validate_extraction_envelope`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_validate_extraction_envelope`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.fullmatch` | `re.fullmatch` |
| `marker_path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `marker_path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `marker_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `_ExtractionMetadata.model_validate` | `landscout.sources.ign_bdtopo_fr._ExtractionMetadata.model_validate` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `marker_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_resolve_relative_path` | `landscout.sources.ign_bdtopo_fr._resolve_relative_path` |
| `discover_ign_bdtopo_geopackage` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_geopackage` |
| `expected_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `discovered_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.geopackage_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `_valid_layer_inventory` | `landscout.sources.ign_bdtopo_fr._valid_layer_inventory` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `_geopackage_integrity` | `landscout.sources.ign_bdtopo_fr._geopackage_integrity` |
| `list_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.list_ign_bdtopo_layers` |
| `_inventory_extracted_tree` | `landscout.sources.ign_bdtopo_fr._inventory_extracted_tree` |
| `_VerifiedIgnExtraction` | `landscout.sources.ign_bdtopo_fr._VerifiedIgnExtraction` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `marker_path.is_file`<br>`marker_path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_extraction_envelope(
    extraction: object,
) -> _VerifiedIgnExtraction:
    """Bind one extraction envelope to its schema-v3 marker and current GPKG."""

    try:
        if type(extraction) is not IgnBdTopoExtraction:
            raise TypeError("IGN extraction must be an exact IgnBdTopoExtraction")
        if type(extraction.archive) is not IgnBdTopoDownload:
            raise TypeError("IGN extraction archive type is invalid")
        if extraction.spatial_role != SPATIAL_ROLE or (
            extraction.archive.spatial_role != SPATIAL_ROLE
        ):
            raise ValueError("IGN extraction lineage must be PROXY_GEOMETRY")
        if (
            not isinstance(extraction.archive.sha256, str)
            or re.fullmatch(r"[0-9a-f]{64}", extraction.archive.sha256) is None
        ):
            raise ValueError("IGN archive SHA256 lineage is invalid")
        if (
            type(extraction.geopackage_size_bytes) is not int
            or extraction.geopackage_size_bytes <= 0
        ):
            raise ValueError("IGN extraction GeoPackage size is invalid")
        if (
            not isinstance(extraction.geopackage_sha256, str)
            or re.fullmatch(r"[0-9a-f]{64}", extraction.geopackage_sha256) is None
        ):
            raise ValueError("IGN extraction GeoPackage SHA256 is invalid")
        if not isinstance(extraction.extraction_path, Path) or not isinstance(
            extraction.geopackage_path, Path
        ):
            raise TypeError("IGN extraction paths are invalid")
        marker_path = extraction.extraction_path / ".landscout-extraction.json"
        if (
            marker_path.is_symlink()
            or marker_path.is_junction()
            or not marker_path.is_file()
        ):
            raise ValueError("IGN schema-v3 extraction metadata is missing")
        metadata = _ExtractionMetadata.model_validate(
            loads_strict_json_object(marker_path.read_bytes())
        )
        expected_path = _resolve_relative_path(
            extraction.extraction_path,
            metadata.geopackage_relative_path,
        )
        discovered_path = discover_ign_bdtopo_geopackage(extraction.extraction_path)
        if (
            expected_path.resolve() != discovered_path.resolve()
            or extraction.geopackage_path.resolve() != discovered_path.resolve()
            or extraction.geopackage_filename != discovered_path.name
        ):
            raise ValueError("IGN extraction GeoPackage path is inconsistent")
        if metadata.archive_sha256 != extraction.archive.sha256:
            raise ValueError("IGN extraction archive lineage differs from metadata")
        if metadata.spatial_role != extraction.spatial_role:
            raise ValueError("IGN extraction spatial role differs from metadata")
        if not _valid_layer_inventory(extraction.all_layer_names):
            raise ValueError("IGN extraction layer inventory is invalid")
        if metadata.all_layer_names != extraction.all_layer_names:
            raise ValueError("IGN extraction layer inventory differs from metadata")
        selected_roles = (
            extraction.electric_lines_layer,
            extraction.transformation_posts_layer,
            extraction.road_segments_layer,
            extraction.department_layer,
        )
        if selected_roles != (
            metadata.electric_lines_layer,
            metadata.transformation_posts_layer,
            metadata.road_segments_layer,
            metadata.department_layer,
        ):
            raise ValueError("IGN extraction physical roles differ from metadata")
        if len(set(selected_roles)) != 4 or any(
            role not in extraction.all_layer_names for role in selected_roles
        ):
            raise ValueError("IGN extraction physical roles are invalid")
        if (
            metadata.geopackage_size_bytes != extraction.geopackage_size_bytes
            or metadata.geopackage_sha256 != extraction.geopackage_sha256
        ):
            raise ValueError(
                "IGN extraction GeoPackage integrity differs from metadata"
            )
        current_size, current_sha = _geopackage_integrity(discovered_path)
        if (
            current_size != extraction.geopackage_size_bytes
            or current_sha != extraction.geopackage_sha256
        ):
            raise ValueError("IGN physical GeoPackage integrity changed")
        current_layers = list_ign_bdtopo_layers(discovered_path)
        if current_layers != extraction.all_layer_names:
            raise ValueError("IGN physical GeoPackage layer inventory changed")
        current_entries = _inventory_extracted_tree(
            extraction.extraction_path,
            exclude_relative_path=".landscout-extraction.json",
        )
        if current_entries != metadata.extracted_entries:
            raise ValueError("IGN complete extracted-file inventory changed")
        return _VerifiedIgnExtraction(
            extraction=extraction,
            metadata=metadata,
            geopackage_path=discovered_path,
        )
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN extraction physical integrity changed or is invalid"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_verify_unchanged_extraction`

**Purpose:** Implements `verify unchanged extraction` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _verify_unchanged_extraction(context: _VerifiedIgnExtraction) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `context` | positional-or-keyword | `_VerifiedIgnExtraction` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            "IGN physical GeoPackage changed during source layer loading"<br>        )` under lexical guard `size != context.extraction.geopackage_size_bytes<br>        or digest != context.extraction.geopackage_sha256<br>        or list_ign_bdtopo_layers(context.geopackage_path)<br>        != context.extraction.all_layer_names<br>        or _inventory_extracted_tree(<br>            context.extraction.extraction_path,<br>            exclude_relative_path=".landscout-extraction.json",<br>        )<br>        != context.metadata.extracted_entries`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_read_verified_layer_frames` via `_verify_unchanged_extraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_read_verified_layer_frames` via `_verify_unchanged_extraction`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_geopackage_integrity` | `landscout.sources.ign_bdtopo_fr._geopackage_integrity` |
| `list_ign_bdtopo_layers` | `landscout.sources.ign_bdtopo_fr.list_ign_bdtopo_layers` |
| `_inventory_extracted_tree` | `landscout.sources.ign_bdtopo_fr._inventory_extracted_tree` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

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
def _verify_unchanged_extraction(context: _VerifiedIgnExtraction) -> None:
    size, digest = _geopackage_integrity(context.geopackage_path)
    if (
        size != context.extraction.geopackage_size_bytes
        or digest != context.extraction.geopackage_sha256
        or list_ign_bdtopo_layers(context.geopackage_path)
        != context.extraction.all_layer_names
        or _inventory_extracted_tree(
            context.extraction.extraction_path,
            exclude_relative_path=".landscout-extraction.json",
        )
        != context.metadata.extracted_entries
    ):
        raise IgnBdTopoLayerError(
            "IGN physical GeoPackage changed during source layer loading"
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_read_layer_frame`

**Purpose:** Implements `read layer frame` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _read_layer_frame(geopackage_path: Path, layer_name: str) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geopackage_path` | positional-or-keyword | `Path` | `required` |
| `layer_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `IgnBdTopoLayerError("IGN source layer name must be an exact string")` under lexical guard `not isinstance(layer_name, str)<br>        or not layer_name<br>        or layer_name != layer_name.strip()`.
  - `IgnBdTopoLayerError(<br>            f"Cannot load IGN GeoPackage layer: {layer_name}"<br>        )`.
  - `IgnBdTopoLayerError(f"IGN layer is not spatial: {layer_name}")` under lexical guard `not isinstance(frame, gpd.GeoDataFrame)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_read_verified_layer_frames` via `_read_layer_frame`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_read_verified_layer_frames` via `_read_layer_frame`
- direct call: `landscout.sources.ign_bdtopo_fr::_load_untrusted_ign_bdtopo_layer` via `_read_layer_frame`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_untrusted_ign_bdtopo_layer` via `_read_layer_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `layer_name.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `gpd.read_file` | `geopandas.read_file` |

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
def _read_layer_frame(geopackage_path: Path, layer_name: str) -> gpd.GeoDataFrame:
    if (
        not isinstance(layer_name, str)
        or not layer_name
        or layer_name != layer_name.strip()
    ):
        raise IgnBdTopoLayerError("IGN source layer name must be an exact string")
    try:
        frame = gpd.read_file(
            geopackage_path,
            layer=layer_name,
            engine="pyogrio",
        )
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"Cannot load IGN GeoPackage layer: {layer_name}"
        ) from error
    if not isinstance(frame, gpd.GeoDataFrame):
        raise IgnBdTopoLayerError(f"IGN layer is not spatial: {layer_name}")
    return frame
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_read_verified_layer_frames`

**Purpose:** Implements `read verified layer frames` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _read_verified_layer_frames(
    context: _VerifiedIgnExtraction,
    layer_names: tuple[str, ...],
) -> tuple[gpd.GeoDataFrame, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[gpd.GeoDataFrame, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `context` | positional-or-keyword | `_VerifiedIgnExtraction` | `required` |
| `layer_names` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frames`
- Explicit raise paths:
  - `IgnBdTopoLayerError("IGN verified layer batch must be a non-empty tuple")` under lexical guard `type(layer_names) is not tuple or not layer_names`.
  - `IgnBdTopoLayerError("IGN verified layer batch is invalid")` under lexical guard `len(set(layer_names)) != len(layer_names) or any(<br>        layer not in context.extraction.all_layer_names for layer in layer_names<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_read_verified_layer_frames`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_read_verified_layer_frames`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_read_verified_layer_frames`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_read_verified_layer_frames`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_read_verified_layer_frames`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_read_verified_layer_frames`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_read_layer_frame` | `landscout.sources.ign_bdtopo_fr._read_layer_frame` |
| `_verify_unchanged_extraction` | `landscout.sources.ign_bdtopo_fr._verify_unchanged_extraction` |

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
def _read_verified_layer_frames(
    context: _VerifiedIgnExtraction,
    layer_names: tuple[str, ...],
) -> tuple[gpd.GeoDataFrame, ...]:
    if type(layer_names) is not tuple or not layer_names:
        raise IgnBdTopoLayerError("IGN verified layer batch must be a non-empty tuple")
    if len(set(layer_names)) != len(layer_names) or any(
        layer not in context.extraction.all_layer_names for layer in layer_names
    ):
        raise IgnBdTopoLayerError("IGN verified layer batch is invalid")
    frames = tuple(
        _read_layer_frame(context.geopackage_path, layer_name)
        for layer_name in layer_names
    )
    _verify_unchanged_extraction(context)
    return frames
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_layer_summary_contract`

**Purpose:** Implements `validate layer summary contract` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _validate_layer_summary_contract(summary: object) -> IgnBdTopoLayerSummary:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoLayerSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `summary` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `summary`
- Explicit raise paths:
  - `IgnBdTopoLayerError("IGN layer summary type is invalid")` under lexical guard `type(summary) is not IgnBdTopoLayerSummary`.
  - `IgnBdTopoLayerError(<br>                f"IGN layer summary {name} must be a strict non-negative integer"<br>            )` under lexical guard `type(value) is not int or value < 0`.
  - `IgnBdTopoLayerError("IGN layer summary columns are invalid")` under lexical guard `type(summary.columns) is not tuple<br>        or not summary.columns<br>        or any(<br>            not isinstance(column, str) or not column or column != column.strip()<br>            for column in summary.columns<br>        )<br>        or len(set(summary.columns)) != len(summary.columns)`.
  - `IgnBdTopoLayerError("IGN layer summary dtypes are invalid")` under lexical guard `type(summary.dtypes) is not tuple<br>        or len(summary.dtypes) != len(summary.columns)<br>        or any(<br>            type(item) is not tuple<br>            or len(item) != 2<br>            or any(not isinstance(value, str) or not value for value in item)<br>            for item in summary.dtypes<br>        )<br>        or tuple(column for column, _ in summary.dtypes) != summary.columns`.
  - `IgnBdTopoLayerError("IGN layer summary geometry types are invalid")` under lexical guard `type(summary.geometry_types) is not tuple<br>        or any(<br>            not isinstance(value, str) or not value or value != value.strip()<br>            for value in summary.geometry_types<br>        )<br>        or summary.geometry_types != tuple(sorted(set(summary.geometry_types)))`.
  - `IgnBdTopoLayerError("IGN layer summary spatial role is invalid")` under lexical guard `summary.spatial_role != SPATIAL_ROLE`.
  - `IgnBdTopoLayerError("IGN layer summary geometry count is impossible")` under lexical guard `any(<br>        getattr(summary, name) > summary.feature_count<br>        for name in (<br>            "null_geometry_count",<br>            "empty_geometry_count",<br>            "invalid_geometry_count",<br>        )<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_compare_layer_summary` via `_validate_layer_summary_contract`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_compare_layer_summary` via `_validate_layer_summary_contract`
- direct call: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `_validate_layer_summary_contract`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `_validate_layer_summary_contract`
- import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
- direct call: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `_validate_layer_summary_contract`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `_validate_layer_summary_contract`
- import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`
- direct call: `landscout.stages.normalize_grid_ign::_validate_layer_summary` via `_validate_layer_summary_contract`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_layer_summary` via `_validate_layer_summary_contract`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `column.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_layer_summary_contract(summary: object) -> IgnBdTopoLayerSummary:
    if type(summary) is not IgnBdTopoLayerSummary:
        raise IgnBdTopoLayerError("IGN layer summary type is invalid")
    for name in (
        "feature_count",
        "null_geometry_count",
        "empty_geometry_count",
        "invalid_geometry_count",
    ):
        value = getattr(summary, name)
        if type(value) is not int or value < 0:
            raise IgnBdTopoLayerError(
                f"IGN layer summary {name} must be a strict non-negative integer"
            )
    if (
        type(summary.columns) is not tuple
        or not summary.columns
        or any(
            not isinstance(column, str) or not column or column != column.strip()
            for column in summary.columns
        )
        or len(set(summary.columns)) != len(summary.columns)
    ):
        raise IgnBdTopoLayerError("IGN layer summary columns are invalid")
    if (
        type(summary.dtypes) is not tuple
        or len(summary.dtypes) != len(summary.columns)
        or any(
            type(item) is not tuple
            or len(item) != 2
            or any(not isinstance(value, str) or not value for value in item)
            for item in summary.dtypes
        )
        or tuple(column for column, _ in summary.dtypes) != summary.columns
    ):
        raise IgnBdTopoLayerError("IGN layer summary dtypes are invalid")
    if (
        type(summary.geometry_types) is not tuple
        or any(
            not isinstance(value, str) or not value or value != value.strip()
            for value in summary.geometry_types
        )
        or summary.geometry_types != tuple(sorted(set(summary.geometry_types)))
    ):
        raise IgnBdTopoLayerError("IGN layer summary geometry types are invalid")
    if summary.spatial_role != SPATIAL_ROLE:
        raise IgnBdTopoLayerError("IGN layer summary spatial role is invalid")
    if any(
        getattr(summary, name) > summary.feature_count
        for name in (
            "null_geometry_count",
            "empty_geometry_count",
            "invalid_geometry_count",
        )
    ):
        raise IgnBdTopoLayerError("IGN layer summary geometry count is impossible")
    return summary
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_compare_layer_summary`

**Purpose:** Implements `compare layer summary` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _compare_layer_summary(
    supplied: object,
    expected: IgnBdTopoLayerSummary,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `supplied` | positional-or-keyword | `object` | `required` |
| `expected` | positional-or-keyword | `IgnBdTopoLayerSummary` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            "IGN supplied layer summary differs from physical source"<br>        )` under lexical guard `validated != expected`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `_compare_layer_summary`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `_compare_layer_summary`
- direct call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `_compare_layer_summary`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `_compare_layer_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_layer_summary_contract` | `landscout.sources.ign_bdtopo_fr._validate_layer_summary_contract` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

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
def _compare_layer_summary(
    supplied: object,
    expected: IgnBdTopoLayerSummary,
) -> None:
    validated = _validate_layer_summary_contract(supplied)
    if validated != expected:
        raise IgnBdTopoLayerError(
            "IGN supplied layer summary differs from physical source"
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_compare_loaded_frame`

**Purpose:** Implements `compare loaded frame` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _compare_loaded_frame(
    supplied: object,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `supplied` | positional-or-keyword | `object` | `required` |
| `expected` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `TypeError("supplied layer is not a GeoDataFrame")` under lexical guard `not isinstance(supplied, gpd.GeoDataFrame)`.
  - `AssertionError("columns differ")` under lexical guard `tuple(supplied.columns) != tuple(expected.columns)`.
  - `AssertionError("dtypes differ")` under lexical guard `tuple(str(dtype) for dtype in supplied.dtypes) != tuple(<br>            str(dtype) for dtype in expected.dtypes<br>        )`.
  - `AssertionError("index type differs")` under lexical guard `type(supplied.index) is not type(expected.index)`.
  - `AssertionError("index differs")` under lexical guard `supplied.index.names != expected.index.names or not supplied.index.equals(<br>            expected.index<br>        )`.
  - `AssertionError("active geometry differs")` under lexical guard `supplied.active_geometry_name != expected.active_geometry_name`.
  - `AssertionError("CRS differs")` under lexical guard `not supplied_crs.equals(expected_crs)`.
  - `AssertionError("geometry is missing")` under lexical guard `geometry_name is None`.
  - `AssertionError("geometry WKB differs")` under lexical guard `supplied.geometry.to_wkb(hex=True).tolist()<br>            != expected.geometry.to_wkb(hex=True).tolist()`.
  - `AssertionError("frame attributes differ")` under lexical guard `supplied.attrs != expected.attrs`.
  - `IgnBdTopoLayerError(<br>            f"IGN supplied {label} differs from freshly read physical source"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `_compare_loaded_frame`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `_compare_loaded_frame`
- direct call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `_compare_loaded_frame`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `_compare_loaded_frame`
- direct call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_department_coverage` via `_compare_loaded_frame`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_department_coverage` via `_compare_loaded_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_lambert93` | `landscout.sources.ign_bdtopo_fr._validate_lambert93` |
| `supplied_crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.testing.assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `supplied.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.geometry.to_wkb(hex=True).tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.geometry.to_wkb(hex=True).tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `supplied.geometry.to_wkb(hex=True).tolist`<br>`supplied.geometry.to_wkb`<br>`expected.geometry.to_wkb(hex=True).tolist`<br>`expected.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | `supplied.drop(columns=geometry_name)`<br>`expected.drop(columns=geometry_name)` |
| Direct parameter mutation | `supplied.drop(columns=geometry_name)`<br>`expected.drop(columns=geometry_name)` |

**Complete source-ordered implementation**

```python
def _compare_loaded_frame(
    supplied: object,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
    try:
        if not isinstance(supplied, gpd.GeoDataFrame):
            raise TypeError("supplied layer is not a GeoDataFrame")
        if tuple(supplied.columns) != tuple(expected.columns):
            raise AssertionError("columns differ")
        if tuple(str(dtype) for dtype in supplied.dtypes) != tuple(
            str(dtype) for dtype in expected.dtypes
        ):
            raise AssertionError("dtypes differ")
        if type(supplied.index) is not type(expected.index):
            raise AssertionError("index type differs")
        if supplied.index.names != expected.index.names or not supplied.index.equals(
            expected.index
        ):
            raise AssertionError("index differs")
        if supplied.active_geometry_name != expected.active_geometry_name:
            raise AssertionError("active geometry differs")
        supplied_crs = _validate_lambert93(supplied.crs, label)
        expected_crs = _validate_lambert93(expected.crs, label)
        if not supplied_crs.equals(expected_crs):
            raise AssertionError("CRS differs")
        geometry_name = expected.active_geometry_name
        if geometry_name is None:
            raise AssertionError("geometry is missing")
        pd.testing.assert_frame_equal(
            pd.DataFrame(supplied.drop(columns=geometry_name)),
            pd.DataFrame(expected.drop(columns=geometry_name)),
            check_dtype=True,
            check_index_type=True,
            check_column_type=True,
            check_names=True,
            check_exact=True,
        )
        if (
            supplied.geometry.to_wkb(hex=True).tolist()
            != expected.geometry.to_wkb(hex=True).tolist()
        ):
            raise AssertionError("geometry WKB differs")
        if supplied.attrs != expected.attrs:
            raise AssertionError("frame attributes differ")
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"IGN supplied {label} differs from freshly read physical source"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_load_cached_extraction`

**Purpose:** Implements `load cached extraction` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _load_cached_extraction(
    extraction_path: Path,
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoExtraction | None:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoExtraction | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction_path` | positional-or-keyword | `Path` | `required` |
| `download` | positional-or-keyword | `IgnBdTopoDownload` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `IgnBdTopoExtraction(<br>            archive=download,<br>            extraction_path=extraction_path,<br>            geopackage_path=geopackage_path,<br>            geopackage_filename=geopackage_path.name,<br>            geopackage_size_bytes=metadata.geopackage_size_bytes,<br>            geopackage_sha256=metadata.geopackage_sha256,<br>            all_layer_names=selection.all_layer_names,<br>            electric_lines_layer=selection.electric_lines_layer,<br>            transformation_posts_layer=selection.transformation_posts_layer,<br>            road_segments_layer=selection.road_segments_layer,<br>            department_layer=selection.department_layer,<br>            cache_hit=True,<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_load_cached_extraction`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_load_cached_extraction`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `extraction_path.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `_ExtractionMetadata.model_validate` | `landscout.sources.ign_bdtopo_fr._ExtractionMetadata.model_validate` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_resolve_relative_path` | `landscout.sources.ign_bdtopo_fr._resolve_relative_path` |
| `discover_ign_bdtopo_geopackage` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_geopackage` |
| `geopackage_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `discovered_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `_geopackage_integrity` | `landscout.sources.ign_bdtopo_fr._geopackage_integrity` |
| `_inventory_extracted_tree` | `landscout.sources.ign_bdtopo_fr._inventory_extracted_tree` |
| `_discover_configured_physical_roles` | `landscout.sources.ign_bdtopo_fr._discover_configured_physical_roles` |
| `IgnBdTopoExtraction` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoExtraction` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction_path.is_dir`<br>`metadata_path.is_file`<br>`metadata_path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _load_cached_extraction(
    extraction_path: Path,
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoExtraction | None:
    metadata_path = extraction_path / ".landscout-extraction.json"
    if not extraction_path.is_dir() or not metadata_path.is_file():
        return None
    try:
        if metadata_path.is_symlink() or metadata_path.is_junction():
            return None
        metadata = _ExtractionMetadata.model_validate(
            loads_strict_json_object(metadata_path.read_bytes())
        )
        if (
            metadata.archive_sha256 != download.sha256
            or metadata.spatial_role != SPATIAL_ROLE
        ):
            return None
        geopackage_path = _resolve_relative_path(
            extraction_path, metadata.geopackage_relative_path
        )
        discovered_path = discover_ign_bdtopo_geopackage(extraction_path)
        if geopackage_path.resolve() != discovered_path.resolve():
            return None
        geopackage_size, geopackage_sha256 = _geopackage_integrity(geopackage_path)
        if (
            geopackage_size != metadata.geopackage_size_bytes
            or geopackage_sha256 != metadata.geopackage_sha256
        ):
            return None
        if (
            _inventory_extracted_tree(
                extraction_path,
                exclude_relative_path=".landscout-extraction.json",
            )
            != metadata.extracted_entries
        ):
            return None
        selection = _discover_configured_physical_roles(geopackage_path, config)
        if (
            selection.all_layer_names != metadata.all_layer_names
            or selection.electric_lines_layer != metadata.electric_lines_layer
            or selection.transformation_posts_layer
            != metadata.transformation_posts_layer
            or selection.road_segments_layer != metadata.road_segments_layer
            or selection.department_layer != metadata.department_layer
        ):
            return None
        return IgnBdTopoExtraction(
            archive=download,
            extraction_path=extraction_path,
            geopackage_path=geopackage_path,
            geopackage_filename=geopackage_path.name,
            geopackage_size_bytes=metadata.geopackage_size_bytes,
            geopackage_sha256=metadata.geopackage_sha256,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            road_segments_layer=selection.road_segments_layer,
            department_layer=selection.department_layer,
            cache_hit=True,
        )
    except (
        IgnBdTopoArchiveError,
        IgnBdTopoLayerError,
        OSError,
        ValidationError,
        ValueError,
    ):
        return None
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_replace_directory`

**Purpose:** Implements `replace directory` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _replace_directory(source: Path, target: Path) -> None:
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
- direct call: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_replace_directory`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_replace_directory`

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
def _replace_directory(source: Path, target: Path) -> None:
    source.replace(target)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_path_exists_or_is_link`

**Purpose:** Implements `path exists or is link` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _path_exists_or_is_link(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path.exists() or path.is_symlink() or path.is_junction()`
  - `True`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_remove_validated_extraction_directory` via `_path_exists_or_is_link`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_remove_validated_extraction_directory` via `_path_exists_or_is_link`
- direct call: `landscout.sources.ign_bdtopo_fr::_require_no_extraction_backup` via `_path_exists_or_is_link`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_require_no_extraction_backup` via `_path_exists_or_is_link`
- direct call: `landscout.sources.ign_bdtopo_fr::_require_safe_existing_extraction_marker` via `_path_exists_or_is_link`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_require_safe_existing_extraction_marker` via `_path_exists_or_is_link`
- direct call: `landscout.sources.ign_bdtopo_fr::_prepare_temporary_extraction_directory` via `_path_exists_or_is_link`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_prepare_temporary_extraction_directory` via `_path_exists_or_is_link`
- direct call: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_path_exists_or_is_link`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_path_exists_or_is_link`
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_path_exists_or_is_link`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_path_exists_or_is_link`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _path_exists_or_is_link(path: Path) -> bool:
    try:
        return path.exists() or path.is_symlink() or path.is_junction()
    except OSError:
        return True
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_remove_validated_extraction_directory`

**Purpose:** Implements `remove validated extraction directory` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _remove_validated_extraction_directory(path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>            "IGN extraction transaction path is not a safe ordinary directory"<br>        )` under lexical guard `path.is_symlink() or path.is_junction() or not path.is_dir()`.
  - `IgnBdTopoArchiveError(<br>            "IGN extraction transaction directory could not be removed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_prepare_temporary_extraction_directory` via `_remove_validated_extraction_directory`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_prepare_temporary_extraction_directory` via `_remove_validated_extraction_directory`
- direct call: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_remove_validated_extraction_directory`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_remove_validated_extraction_directory`
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_remove_validated_extraction_directory`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_remove_validated_extraction_directory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_path_exists_or_is_link` | `landscout.sources.ign_bdtopo_fr._path_exists_or_is_link` |
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `_inventory_extracted_tree` | `landscout.sources.ign_bdtopo_fr._inventory_extracted_tree` |
| `shutil.rmtree` | `shutil.rmtree` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_dir` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _remove_validated_extraction_directory(path: Path) -> None:
    if not _path_exists_or_is_link(path):
        return
    if path.is_symlink() or path.is_junction() or not path.is_dir():
        raise IgnBdTopoArchiveError(
            "IGN extraction transaction path is not a safe ordinary directory"
        )
    _inventory_extracted_tree(path)
    try:
        shutil.rmtree(path)
    except OSError as error:
        raise IgnBdTopoArchiveError(
            "IGN extraction transaction directory could not be removed safely"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_require_no_extraction_backup`

**Purpose:** Implements `require no extraction backup` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _require_no_extraction_backup(extraction_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>            "IGN extraction recovery backup exists; manual recovery is required"<br>        )` under lexical guard `_path_exists_or_is_link(backup_path)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_require_no_extraction_backup`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_publish_extraction_directory` via `_require_no_extraction_backup`
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_require_no_extraction_backup`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_require_no_extraction_backup`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `extraction_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `_path_exists_or_is_link` | `landscout.sources.ign_bdtopo_fr._path_exists_or_is_link` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |

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
def _require_no_extraction_backup(extraction_path: Path) -> None:
    backup_path = extraction_path.with_name(f"{extraction_path.name}.bak")
    if _path_exists_or_is_link(backup_path):
        raise IgnBdTopoArchiveError(
            "IGN extraction recovery backup exists; manual recovery is required"
        )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_require_safe_existing_extraction_marker`

**Purpose:** Implements `require safe existing extraction marker` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _require_safe_existing_extraction_marker(extraction_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>                "IGN extraction integrity marker is not a regular non-linked file"<br>            )` under lexical guard `marker_path.is_symlink()<br>            or marker_path.is_junction()<br>            or not marker_path.is_file()`.
  - `re-raise`.
  - `IgnBdTopoArchiveError(<br>            "IGN extraction integrity marker cannot be inspected safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_require_safe_existing_extraction_marker`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_require_safe_existing_extraction_marker`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_path_exists_or_is_link` | `landscout.sources.ign_bdtopo_fr._path_exists_or_is_link` |
| `marker_path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `marker_path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `marker_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `marker_path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _require_safe_existing_extraction_marker(extraction_path: Path) -> None:
    marker_path = extraction_path / ".landscout-extraction.json"
    if not _path_exists_or_is_link(marker_path):
        return
    try:
        if (
            marker_path.is_symlink()
            or marker_path.is_junction()
            or not marker_path.is_file()
        ):
            raise IgnBdTopoArchiveError(
                "IGN extraction integrity marker is not a regular non-linked file"
            )
    except IgnBdTopoArchiveError:
        raise
    except OSError as error:
        raise IgnBdTopoArchiveError(
            "IGN extraction integrity marker cannot be inspected safely"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_prepare_temporary_extraction_directory`

**Purpose:** Implements `prepare temporary extraction directory` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

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
  - `IgnBdTopoArchiveError(<br>            "IGN temporary extraction directory cannot be created safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_prepare_temporary_extraction_directory`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_prepare_temporary_extraction_directory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_path_exists_or_is_link` | `landscout.sources.ign_bdtopo_fr._path_exists_or_is_link` |
| `_remove_validated_extraction_directory` | `landscout.sources.ign_bdtopo_fr._remove_validated_extraction_directory` |
| `path.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.mkdir` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _prepare_temporary_extraction_directory(path: Path) -> None:
    if _path_exists_or_is_link(path):
        _remove_validated_extraction_directory(path)
    try:
        path.mkdir(parents=False)
    except OSError as error:
        raise IgnBdTopoArchiveError(
            "IGN temporary extraction directory cannot be created safely"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_publish_extraction_directory`

**Purpose:** Implements `publish extraction directory` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _publish_extraction_directory(temporary_path: Path, extraction_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `temporary_path` | positional-or-keyword | `Path` | `required` |
| `extraction_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>                "IGN existing extraction target is not a safe ordinary directory"<br>            )` under lexical guard `extraction_existed`.
  - `IgnBdTopoArchiveError(<br>                "IGN extraction publication and rollback both failed"<br>            )`.
  - `re-raise`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_publish_extraction_directory`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_publish_extraction_directory`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extraction_publication_double_failure_preserves_backup` via `ign_bdtopo_fr._publish_extraction_directory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `extraction_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_no_extraction_backup` | `landscout.sources.ign_bdtopo_fr._require_no_extraction_backup` |
| `_path_exists_or_is_link` | `landscout.sources.ign_bdtopo_fr._path_exists_or_is_link` |
| `extraction_path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction_path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction_path.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `_inventory_extracted_tree` | `landscout.sources.ign_bdtopo_fr._inventory_extracted_tree` |
| `_replace_directory` | `landscout.sources.ign_bdtopo_fr._replace_directory` |
| `_remove_validated_extraction_directory` | `landscout.sources.ign_bdtopo_fr._remove_validated_extraction_directory` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction_path.is_dir` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _publish_extraction_directory(temporary_path: Path, extraction_path: Path) -> None:
    backup_path = extraction_path.with_name(f"{extraction_path.name}.bak")
    _require_no_extraction_backup(extraction_path)
    extraction_existed = _path_exists_or_is_link(extraction_path)
    if extraction_existed:
        if (
            extraction_path.is_symlink()
            or extraction_path.is_junction()
            or not extraction_path.is_dir()
        ):
            raise IgnBdTopoArchiveError(
                "IGN existing extraction target is not a safe ordinary directory"
            )
        _inventory_extracted_tree(extraction_path)
    if extraction_existed:
        _replace_directory(extraction_path, backup_path)
    try:
        _replace_directory(temporary_path, extraction_path)
    except OSError:
        try:
            if extraction_existed:
                if _path_exists_or_is_link(extraction_path):
                    _remove_validated_extraction_directory(extraction_path)
                _replace_directory(backup_path, extraction_path)
        except (IgnBdTopoArchiveError, OSError) as rollback_error:
            raise IgnBdTopoArchiveError(
                "IGN extraction publication and rollback both failed"
            ) from rollback_error
        raise
    else:
        if extraction_existed:
            _remove_validated_extraction_directory(backup_path)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `extract_ign_bdtopo_archive`

**Purpose:** Safely extract the package and resolve its required electricity layers.

**Exact signature**

```python
def extract_ign_bdtopo_archive(
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
    extraction_dir: Path | None = None,
) -> IgnBdTopoExtraction:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoExtraction`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `IgnBdTopoDownload` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `extraction_dir` | positional-or-keyword | `Path \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `cached`
  - `IgnBdTopoExtraction(<br>            archive=download,<br>            extraction_path=extraction_path,<br>            geopackage_path=published_geopackage,<br>            geopackage_filename=published_geopackage.name,<br>            geopackage_size_bytes=metadata.geopackage_size_bytes,<br>            geopackage_sha256=metadata.geopackage_sha256,<br>            all_layer_names=selection.all_layer_names,<br>            electric_lines_layer=selection.electric_lines_layer,<br>            transformation_posts_layer=selection.transformation_posts_layer,<br>            road_segments_layer=selection.road_segments_layer,<br>            department_layer=selection.department_layer,<br>            cache_hit=False,<br>        )`
- Explicit raise paths:
  - `IgnBdTopoArchiveError(<br>            "IGN download envelope differs from source config"<br>        )`.
  - `IgnBdTopoArchiveError("IGN extraction target must be a pathlib.Path")` under lexical guard `not isinstance(extraction_path, Path)`.
  - `IgnBdTopoArchiveError(<br>            f"IGN extraction target exists and is not a directory: {extraction_path}"<br>        )` under lexical guard `_path_exists_or_is_link(extraction_path) and (<br>        extraction_path.is_symlink()<br>        or extraction_path.is_junction()<br>        or not extraction_path.is_dir()<br>    )`.
  - `IgnBdTopoArchiveError(<br>            "Downloaded IGN archive integrity changed before extraction"<br>        )` under lexical guard `integrity.file_size != download.file_size<br>        or integrity.sha256 != download.sha256<br>        or integrity.official_checksum_algorithm != download.official_checksum_algorithm<br>        or integrity.official_checksum != download.official_checksum<br>        or integrity.official_checksum_validated != download.official_checksum_validated`.
  - `IgnBdTopoArchiveError(<br>            f"IGN archive extraction failed: {download.path}"<br>        )`.
  - `re-raise` under lexical guard `primary_error is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_schema_v3_extraction_metadata_binds_complete_physical_inventory` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_schema_v3_extraction_metadata_binds_complete_physical_inventory` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extraction_rejects_forged_download_lineage_before_archive_open` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_rejects_forged_download_lineage_before_archive_open` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_same_size_geopackage_tamper_invalidates_extraction_cache` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_same_size_geopackage_tamper_invalidates_extraction_cache` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_forged_extraction_metadata_never_returns_cache_hit` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_forged_extraction_metadata_never_returns_cache_hit` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_sha_is_not_trusted` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_sha_is_not_trusted` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_size_is_not_trusted` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_size_is_not_trusted` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_stale_extraction_backup_blocks_before_7z_open` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_extraction_backup_blocks_before_7z_open` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `extract_ign_bdtopo_archive`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `extract_ign_bdtopo_archive`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `extract_ign_bdtopo_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.ign_bdtopo_fr._validated_source_config` |
| `_validate_archive_config_lineage` | `landscout.sources.ign_bdtopo_fr._validate_archive_config_lineage` |
| `IgnBdTopoArchiveError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoArchiveError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_no_extraction_backup` | `landscout.sources.ign_bdtopo_fr._require_no_extraction_backup` |
| `_path_exists_or_is_link` | `landscout.sources.ign_bdtopo_fr._path_exists_or_is_link` |
| `extraction_path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction_path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction_path.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_safe_existing_extraction_marker` | `landscout.sources.ign_bdtopo_fr._require_safe_existing_extraction_marker` |
| `validate_ign_bdtopo_archive` | `landscout.sources.ign_bdtopo_fr.validate_ign_bdtopo_archive` |
| `_load_cached_extraction` | `landscout.sources.ign_bdtopo_fr._load_cached_extraction` |
| `extraction_path.parent.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `_prepare_temporary_extraction_directory` | `landscout.sources.ign_bdtopo_fr._prepare_temporary_extraction_directory` |
| `py7zr.SevenZipFile` | `py7zr.SevenZipFile` |
| `_validate_archive_members` | `landscout.sources.ign_bdtopo_fr._validate_archive_members` |
| `archive.extractall` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_extracted_inventory` | `landscout.sources.ign_bdtopo_fr._validate_extracted_inventory` |
| `discover_ign_bdtopo_geopackage` | `landscout.sources.ign_bdtopo_fr.discover_ign_bdtopo_geopackage` |
| `_discover_configured_physical_roles` | `landscout.sources.ign_bdtopo_fr._discover_configured_physical_roles` |
| `_safe_relative_path` | `landscout.sources.ign_bdtopo_fr._safe_relative_path` |
| `_geopackage_integrity` | `landscout.sources.ign_bdtopo_fr._geopackage_integrity` |
| `_ExtractionMetadata` | `landscout.sources.ign_bdtopo_fr._ExtractionMetadata` |
| `(temporary_path / ".landscout-extraction.json").open` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.write` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata.model_dump_json` | `unresolved local/third-party receiver; no ownership inferred` |
| `_publish_extraction_directory` | `landscout.sources.ign_bdtopo_fr._publish_extraction_directory` |
| `_resolve_relative_path` | `landscout.sources.ign_bdtopo_fr._resolve_relative_path` |
| `IgnBdTopoExtraction` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoExtraction` |
| `sys.exception` | `sys.exception` |
| `_remove_validated_extraction_directory` | `landscout.sources.ign_bdtopo_fr._remove_validated_extraction_directory` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction_path.is_dir`<br>`py7zr.SevenZipFile`<br>`(temporary_path / ".landscout-extraction.json").open` |
| Filesystem/archive write or publication | `extraction_path.parent.mkdir`<br>`archive.extractall` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | `py7zr.SevenZipFile` |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def extract_ign_bdtopo_archive(
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
    extraction_dir: Path | None = None,
) -> IgnBdTopoExtraction:
    """Safely extract the package and resolve its required electricity layers."""

    config = _validated_source_config(config, error_type=IgnBdTopoArchiveError)
    try:
        _validate_archive_config_lineage(download, config)
    except IgnBdTopoLayerError as error:
        raise IgnBdTopoArchiveError(
            "IGN download envelope differs from source config"
        ) from error
    extraction_path = extraction_dir or (
        download.path.parent / "x" / download.sha256[:16]
    )
    if not isinstance(extraction_path, Path):
        raise IgnBdTopoArchiveError("IGN extraction target must be a pathlib.Path")
    _require_no_extraction_backup(extraction_path)
    if _path_exists_or_is_link(extraction_path) and (
        extraction_path.is_symlink()
        or extraction_path.is_junction()
        or not extraction_path.is_dir()
    ):
        raise IgnBdTopoArchiveError(
            f"IGN extraction target exists and is not a directory: {extraction_path}"
        )
    _require_safe_existing_extraction_marker(extraction_path)
    integrity = validate_ign_bdtopo_archive(download.path, config)
    if (
        integrity.file_size != download.file_size
        or integrity.sha256 != download.sha256
        or integrity.official_checksum_algorithm != download.official_checksum_algorithm
        or integrity.official_checksum != download.official_checksum
        or integrity.official_checksum_validated != download.official_checksum_validated
    ):
        raise IgnBdTopoArchiveError(
            "Downloaded IGN archive integrity changed before extraction"
        )
    cached = _load_cached_extraction(extraction_path, download, config)
    if cached is not None:
        return cached

    extraction_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = extraction_path.with_name(f"{extraction_path.name}.part")
    _prepare_temporary_extraction_directory(temporary_path)
    try:
        with py7zr.SevenZipFile(download.path, mode="r") as archive:
            expected_entries = _validate_archive_members(archive)
            archive.extractall(path=temporary_path)

        extracted_entries = _validate_extracted_inventory(
            temporary_path,
            expected_entries,
        )
        geopackage_path = discover_ign_bdtopo_geopackage(temporary_path)
        selection = _discover_configured_physical_roles(geopackage_path, config)
        relative_path = _safe_relative_path(geopackage_path, temporary_path)
        geopackage_size, geopackage_sha256 = _geopackage_integrity(geopackage_path)
        metadata = _ExtractionMetadata(
            schema_version=3,
            archive_sha256=download.sha256,
            geopackage_relative_path=relative_path,
            geopackage_size_bytes=geopackage_size,
            geopackage_sha256=geopackage_sha256,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            road_segments_layer=selection.road_segments_layer,
            department_layer=selection.department_layer,
            extracted_entries=extracted_entries,
            spatial_role="PROXY_GEOMETRY",
        )
        with (temporary_path / ".landscout-extraction.json").open(
            "x", encoding="utf-8"
        ) as output:
            output.write(metadata.model_dump_json(indent=2) + "\n")
        _publish_extraction_directory(temporary_path, extraction_path)
        published_geopackage = _resolve_relative_path(extraction_path, relative_path)
        return IgnBdTopoExtraction(
            archive=download,
            extraction_path=extraction_path,
            geopackage_path=published_geopackage,
            geopackage_filename=published_geopackage.name,
            geopackage_size_bytes=metadata.geopackage_size_bytes,
            geopackage_sha256=metadata.geopackage_sha256,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            road_segments_layer=selection.road_segments_layer,
            department_layer=selection.department_layer,
            cache_hit=False,
        )
    except (ArchiveError, EOFError, OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"IGN archive extraction failed: {download.path}"
        ) from error
    finally:
        primary_error = sys.exception()
        try:
            _remove_validated_extraction_directory(temporary_path)
        except IgnBdTopoArchiveError:
            if primary_error is None:
                raise
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_lambert93`

**Purpose:** Implements `validate lambert93` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _validate_lambert93(crs_value: Any, layer_name: str) -> CRS:
```

- Exact decorators: none.
- Declared return annotation: `CRS`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `crs_value` | positional-or-keyword | `Any` | `required` |
| `layer_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `crs`
- Explicit raise paths:
  - `IgnBdTopoLayerError(f"IGN layer has no CRS: {layer_name}")` under lexical guard `crs_value is None`.
  - `IgnBdTopoLayerError(<br>            f"IGN layer has an unreadable CRS: {layer_name}"<br>        )`.
  - `IgnBdTopoLayerError(<br>            f"IGN layer CRS must be projected: {layer_name} ({crs.to_string()})"<br>        )` under lexical guard `not crs.is_projected`.
  - `IgnBdTopoLayerError(<br>            "IGN layer CRS is not Lambert-93 / EPSG:2154 compatible: "<br>            f"{layer_name} ({crs.to_string()})"<br>        )` under lexical guard `not crs.equals(expected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_compare_loaded_frame` via `_validate_lambert93`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_compare_loaded_frame` via `_validate_lambert93`
- direct call: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `_validate_lambert93`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_loaded_layer_from_frame` via `_validate_lambert93`
- direct call: `landscout.sources.ign_bdtopo_fr::_department_coverage_from_frame` via `_validate_lambert93`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_department_coverage_from_frame` via `_validate_lambert93`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_lambert93(crs_value: Any, layer_name: str) -> CRS:
    if crs_value is None:
        raise IgnBdTopoLayerError(f"IGN layer has no CRS: {layer_name}")
    try:
        crs = CRS.from_user_input(crs_value)
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"IGN layer has an unreadable CRS: {layer_name}"
        ) from error
    if not crs.is_projected:
        raise IgnBdTopoLayerError(
            f"IGN layer CRS must be projected: {layer_name} ({crs.to_string()})"
        )
    expected = CRS.from_epsg(2154)
    if not crs.equals(expected):
        raise IgnBdTopoLayerError(
            "IGN layer CRS is not Lambert-93 / EPSG:2154 compatible: "
            f"{layer_name} ({crs.to_string()})"
        )
    return crs
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_loaded_layer_from_frame`

**Purpose:** Implements `loaded layer from frame` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _loaded_layer_from_frame(
    frame: gpd.GeoDataFrame,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoLoadedLayer`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `layer_name` | positional-or-keyword | `str` | `required` |
| `logical_name` | positional-or-keyword | `LogicalLayerName` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoLoadedLayer(data=frame, summary=summary)`
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            f"IGN layer has no active geometry column: {layer_name}"<br>        )`.
  - `IgnBdTopoLayerError(f"IGN layer geometry column is missing: {layer_name}")` under lexical guard `geometry_name not in frame.columns`.
  - `IgnBdTopoLayerError(f"IGN layer contains no features: {layer_name}")` under lexical guard `frame.empty`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::_load_untrusted_ign_bdtopo_layer` via `_loaded_layer_from_frame`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_untrusted_ign_bdtopo_layer` via `_loaded_layer_from_frame`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_loaded_layer_from_frame`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_loaded_layer_from_frame`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_loaded_layer_from_frame`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_loaded_layer_from_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `_validate_lambert93` | `landscout.sources.ign_bdtopo_fr._validate_lambert93` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[non_null_mask].geom_type.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[non_null_mask].geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerSummary` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerSummary` |
| `crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `null_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `empty_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_layer_summary_contract` | `landscout.sources.ign_bdtopo_fr._validate_layer_summary_contract` |
| `IgnBdTopoLoadedLayer` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLoadedLayer` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna`<br>`geometry[non_null_mask].geom_type.dropna().unique`<br>`geometry[non_null_mask].geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _loaded_layer_from_frame(
    frame: gpd.GeoDataFrame,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
    try:
        geometry_name = frame.geometry.name
    except (AttributeError, ValueError) as error:
        raise IgnBdTopoLayerError(
            f"IGN layer has no active geometry column: {layer_name}"
        ) from error
    if geometry_name not in frame.columns:
        raise IgnBdTopoLayerError(f"IGN layer geometry column is missing: {layer_name}")
    crs = _validate_lambert93(frame.crs, layer_name)
    if frame.empty:
        raise IgnBdTopoLayerError(f"IGN layer contains no features: {layer_name}")

    geometry = frame.geometry
    null_mask = geometry.isna()
    non_null_mask = ~null_mask
    empty_mask = non_null_mask & geometry.is_empty
    measurable_mask = non_null_mask & ~geometry.is_empty
    invalid_mask = measurable_mask & ~geometry.is_valid
    geometry_types = tuple(
        sorted(
            str(value) for value in geometry[non_null_mask].geom_type.dropna().unique()
        )
    )
    summary = IgnBdTopoLayerSummary(
        logical_name=logical_name,
        source_layer_name=layer_name,
        crs=crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
    )
    _validate_layer_summary_contract(summary)
    return IgnBdTopoLoadedLayer(data=frame, summary=summary)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_load_untrusted_ign_bdtopo_layer`

**Purpose:** Inspect one raw layer without conferring config-bound source authority.

**Exact signature**

```python
def _load_untrusted_ign_bdtopo_layer(
    geopackage_path: Path,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoLoadedLayer`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geopackage_path` | positional-or-keyword | `Path` | `required` |
| `layer_name` | positional-or-keyword | `str` | `required` |
| `logical_name` | positional-or-keyword | `LogicalLayerName` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_loaded_layer_from_frame(frame, layer_name, logical_name)`
- Explicit raise paths:
  - `IgnBdTopoLayerError(f"GeoPackage does not exist: {geopackage_path}")` under lexical guard `not geopackage_path.is_file()`.
  - `IgnBdTopoLayerError("IGN source layer name must not be empty")` under lexical guard `not layer_name.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    _load_untrusted_ign_bdtopo_layer as load_untrusted_ign_bdtopo_layer,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_layer_loader_retains_crs_counts_and_null_geometries` via `load_untrusted_ign_bdtopo_layer`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_layer_loader_retains_crs_counts_and_null_geometries` via `load_untrusted_ign_bdtopo_layer`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_invalid_geometry_is_preserved_without_repair` via `load_untrusted_ign_bdtopo_layer`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_invalid_geometry_is_preserved_without_repair` via `load_untrusted_ign_bdtopo_layer`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_geographic_crs_is_rejected` via `load_untrusted_ign_bdtopo_layer`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_geographic_crs_is_rejected` via `load_untrusted_ign_bdtopo_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geopackage_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `layer_name.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_read_layer_frame` | `landscout.sources.ign_bdtopo_fr._read_layer_frame` |
| `_loaded_layer_from_frame` | `landscout.sources.ign_bdtopo_fr._loaded_layer_from_frame` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `geopackage_path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _load_untrusted_ign_bdtopo_layer(
    geopackage_path: Path,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
    """Inspect one raw layer without conferring config-bound source authority."""

    if not geopackage_path.is_file():
        raise IgnBdTopoLayerError(f"GeoPackage does not exist: {geopackage_path}")
    if not layer_name.strip():
        raise IgnBdTopoLayerError("IGN source layer name must not be empty")
    frame = _read_layer_frame(geopackage_path, layer_name)
    return _loaded_layer_from_frame(frame, layer_name, logical_name)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validated_layer_source_config`

**Purpose:** Implements `validated layer source config` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _validated_layer_source_config(config: object) -> IgnBdTopoSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_validated_source_config(config, error_type=IgnBdTopoLayerError)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_validated_layer_source_config`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_validated_layer_source_config`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_validated_layer_source_config`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_validated_layer_source_config`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_validated_layer_source_config`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_validated_layer_source_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_source_config` | `landscout.sources.ign_bdtopo_fr._validated_source_config` |

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
def _validated_layer_source_config(config: object) -> IgnBdTopoSourceConfig:
    return _validated_source_config(config, error_type=IgnBdTopoLayerError)
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_archive_config_lineage`

**Purpose:** Implements `validate archive config lineage` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _validate_archive_config_lineage(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `object` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `TypeError("IGN archive source type is invalid")` under lexical guard `type(source) is IgnBdTopoExtraction`.
  - `TypeError("IGN archive type is invalid")` under lexical guard `type(archive) is not IgnBdTopoDownload`.
  - `TypeError("IGN archive size is invalid")` under lexical guard `type(archive.file_size) is not int or archive.file_size <= 0`.
  - `TypeError("IGN official-checksum state is invalid")` under lexical guard `type(archive.official_checksum_validated) is not bool`.
  - `TypeError("IGN archive SHA256 is invalid")` under lexical guard `type(archive.sha256) is not str<br>            or re.fullmatch(r"[0-9a-f]{64}", archive.sha256) is None`.
  - `TypeError("IGN archive timestamp is invalid")` under lexical guard `type(archive.download_timestamp) is not str`.
  - `ValueError("IGN archive timestamp must be timezone-aware UTC")` under lexical guard `downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(<br>            None<br>        )`.
  - `TypeError("IGN archive path type is invalid")` under lexical guard `not isinstance(archive.path, Path)`.
  - `ValueError("IGN archive filename differs from its physical path")` under lexical guard `archive.path.name != archive.filename`.
  - `TypeError("IGN archive cache state is invalid")` under lexical guard `type(archive.cache_hit) is not bool`.
  - `ValueError("IGN archive lineage differs from source config")` under lexical guard `any(actual != expected for actual, expected in expected_values)`.
  - `ValueError("IGN archive size differs from source config")` under lexical guard `config.expected_archive_size_bytes is not None<br>            and archive.file_size != config.expected_archive_size_bytes`.
  - `re-raise`.
  - `IgnBdTopoLayerError(<br>            "IGN archive lineage differs from source config"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_validate_archive_config_lineage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_validate_archive_config_lineage`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_validate_archive_config_lineage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `_validate_archive_config_lineage`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_validate_archive_config_lineage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `_validate_archive_config_lineage`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_validate_archive_config_lineage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_validate_archive_config_lineage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.fullmatch` | `re.fullmatch` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `downloaded_at.utcoffset` | `unresolved local/third-party receiver; no ownership inferred` |
| `UTC.utcoffset` | `datetime.UTC.utcoffset` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_archive_filename` | `landscout.sources.ign_bdtopo_fr._archive_filename` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

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
def _validate_archive_config_lineage(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> None:
    try:
        if type(source) is IgnBdTopoExtraction:
            archive = source.archive
        elif type(source) is IgnBdTopoDownload:
            archive = source
        else:
            raise TypeError("IGN archive source type is invalid")
        if type(archive) is not IgnBdTopoDownload:
            raise TypeError("IGN archive type is invalid")
        if type(archive.file_size) is not int or archive.file_size <= 0:
            raise TypeError("IGN archive size is invalid")
        if type(archive.official_checksum_validated) is not bool:
            raise TypeError("IGN official-checksum state is invalid")
        if (
            type(archive.sha256) is not str
            or re.fullmatch(r"[0-9a-f]{64}", archive.sha256) is None
        ):
            raise TypeError("IGN archive SHA256 is invalid")
        if type(archive.download_timestamp) is not str:
            raise TypeError("IGN archive timestamp is invalid")
        downloaded_at = datetime.fromisoformat(archive.download_timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(
            None
        ):
            raise ValueError("IGN archive timestamp must be timezone-aware UTC")
        if not isinstance(archive.path, Path):
            raise TypeError("IGN archive path type is invalid")
        if archive.path.name != archive.filename:
            raise ValueError("IGN archive filename differs from its physical path")
        if type(archive.cache_hit) is not bool:
            raise TypeError("IGN archive cache state is invalid")
        expected_checksum_url = (
            str(config.checksum_url) if config.checksum_url is not None else None
        )
        expected_values: tuple[tuple[object, object], ...] = (
            (archive.provider, config.provider),
            (archive.product, config.product),
            (archive.department_code, config.department_code),
            (archive.edition, config.edition),
            (archive.product_version, config.product_version),
            (archive.projection, config.projection),
            (archive.package_format, config.format),
            (archive.archive_format, config.archive_format),
            (archive.source_url, str(config.source_url)),
            (archive.checksum_url, expected_checksum_url),
            (archive.filename, _archive_filename(config)),
            (
                archive.official_checksum_algorithm,
                config.official_checksum_algorithm,
            ),
            (archive.official_checksum, config.official_checksum),
            (
                archive.official_checksum_validated,
                config.official_checksum is not None,
            ),
            (archive.spatial_role, SPATIAL_ROLE),
        )
        if any(actual != expected for actual, expected in expected_values):
            raise ValueError("IGN archive lineage differs from source config")
        if (
            config.expected_archive_size_bytes is not None
            and archive.file_size != config.expected_archive_size_bytes
        ):
            raise ValueError("IGN archive size differs from source config")
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN archive lineage differs from source config"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `load_ign_bdtopo_electricity`

**Purpose:** Load the two electricity layers reproduced from the source config.

**Exact signature**

```python
def load_ign_bdtopo_electricity(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `IgnBdTopoExtraction` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoElectricityData(<br>        extraction=extraction,<br>        electric_lines=electric_lines.data,<br>        transformation_posts=transformation_posts.data,<br>        electric_lines_summary=electric_lines.summary,<br>        transformation_posts_summary=transformation_posts.summary,<br>    )`
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            "IGN electricity roles differ from the configured physical layers"<br>        )` under lexical guard `configured_selection.all_layer_names != extraction.all_layer_names<br>        or configured_selection.electric_lines_layer != extraction.electric_lines_layer<br>        or configured_selection.transformation_posts_layer<br>        != extraction.transformation_posts_layer<br>        or configured_selection.road_segments_layer != extraction.road_segments_layer<br>        or configured_selection.department_layer != extraction.department_layer`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `load_ign_bdtopo_electricity`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `load_ign_bdtopo_electricity`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `load_ign_bdtopo_electricity`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `load_ign_bdtopo_electricity`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_electricity_physical_layers_must_be_distinct` via `load_ign_bdtopo_electricity`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_physical_layers_must_be_distinct` via `load_ign_bdtopo_electricity`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `load_ign_bdtopo_electricity`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `load_ign_bdtopo_electricity`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `load_ign_bdtopo_electricity`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `load_ign_bdtopo_electricity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_layer_source_config` | `landscout.sources.ign_bdtopo_fr._validated_layer_source_config` |
| `_validate_archive_config_lineage` | `landscout.sources.ign_bdtopo_fr._validate_archive_config_lineage` |
| `_validate_extraction_envelope` | `landscout.sources.ign_bdtopo_fr._validate_extraction_envelope` |
| `_discover_configured_physical_roles` | `landscout.sources.ign_bdtopo_fr._discover_configured_physical_roles` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `_read_verified_layer_frames` | `landscout.sources.ign_bdtopo_fr._read_verified_layer_frames` |
| `_loaded_layer_from_frame` | `landscout.sources.ign_bdtopo_fr._loaded_layer_from_frame` |
| `IgnBdTopoElectricityData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoElectricityData` |

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
def load_ign_bdtopo_electricity(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
    """Load the two electricity layers reproduced from the source config."""

    validated_config = _validated_layer_source_config(config)
    _validate_archive_config_lineage(extraction, validated_config)
    context = _validate_extraction_envelope(extraction)
    configured_selection = _discover_configured_physical_roles(
        context.geopackage_path,
        validated_config,
    )
    if (
        configured_selection.all_layer_names != extraction.all_layer_names
        or configured_selection.electric_lines_layer != extraction.electric_lines_layer
        or configured_selection.transformation_posts_layer
        != extraction.transformation_posts_layer
        or configured_selection.road_segments_layer != extraction.road_segments_layer
        or configured_selection.department_layer != extraction.department_layer
    ):
        raise IgnBdTopoLayerError(
            "IGN electricity roles differ from the configured physical layers"
        )
    line_frame, post_frame = _read_verified_layer_frames(
        context,
        (
            configured_selection.electric_lines_layer,
            configured_selection.transformation_posts_layer,
        ),
    )
    electric_lines = _loaded_layer_from_frame(
        line_frame,
        configured_selection.electric_lines_layer,
        "electric_lines",
    )
    transformation_posts = _loaded_layer_from_frame(
        post_frame,
        configured_selection.transformation_posts_layer,
        "transformation_posts",
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=electric_lines.data,
        transformation_posts=transformation_posts.data,
        electric_lines_summary=electric_lines.summary,
        transformation_posts_summary=transformation_posts.summary,
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `load_ign_bdtopo_roads`

**Purpose:** Load the configured factual road layer without filtering or repair.

**Exact signature**

```python
def load_ign_bdtopo_roads(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoRoadData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `IgnBdTopoExtraction` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoRoadData(<br>        extraction=extraction,<br>        road_segments=loaded.data,<br>        road_segments_summary=loaded.summary,<br>    )`
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            "IGN road role differs from configured physical-layer inventory"<br>        )` under lexical guard `selection.all_layer_names != extraction.all_layer_names<br>        or selection.electric_lines_layer != extraction.electric_lines_layer<br>        or selection.transformation_posts_layer != extraction.transformation_posts_layer<br>        or selection.road_segments_layer != extraction.road_segments_layer<br>        or selection.department_layer != extraction.department_layer`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `load_ign_bdtopo_roads`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `load_ign_bdtopo_roads`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `ign_bdtopo_fr.load_ign_bdtopo_roads`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_physical_layer_cannot_collide_with_electricity_roles` via `ign_bdtopo_fr.load_ign_bdtopo_roads`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `ign_bdtopo_fr.load_ign_bdtopo_roads`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` via `ign_bdtopo_fr.load_ign_bdtopo_roads`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `ign_bdtopo_fr.load_ign_bdtopo_roads`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `ign_bdtopo_fr.load_ign_bdtopo_roads`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `ign_bdtopo_fr.load_ign_bdtopo_roads`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `ign_bdtopo_fr.load_ign_bdtopo_roads`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_source_change_after_physical_read` via `ign_bdtopo_fr.load_ign_bdtopo_roads`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- direct call: `tests.unit.test_normalize_access_ign::_with_alternate_road_layer` via `load_ign_bdtopo_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::_with_alternate_road_layer` via `load_ign_bdtopo_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_road_normalization_reproduces_configured_logical_layer` via `load_ign_bdtopo_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_normalization_reproduces_configured_logical_layer` via `load_ign_bdtopo_roads`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_layer_source_config` | `landscout.sources.ign_bdtopo_fr._validated_layer_source_config` |
| `_validate_archive_config_lineage` | `landscout.sources.ign_bdtopo_fr._validate_archive_config_lineage` |
| `_validate_extraction_envelope` | `landscout.sources.ign_bdtopo_fr._validate_extraction_envelope` |
| `_discover_configured_physical_roles` | `landscout.sources.ign_bdtopo_fr._discover_configured_physical_roles` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `_read_verified_layer_frames` | `landscout.sources.ign_bdtopo_fr._read_verified_layer_frames` |
| `_loaded_layer_from_frame` | `landscout.sources.ign_bdtopo_fr._loaded_layer_from_frame` |
| `IgnBdTopoRoadData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoRoadData` |

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
def load_ign_bdtopo_roads(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
    """Load the configured factual road layer without filtering or repair."""

    validated_config = _validated_layer_source_config(config)
    _validate_archive_config_lineage(extraction, validated_config)
    context = _validate_extraction_envelope(extraction)
    selection = _discover_configured_physical_roles(
        context.geopackage_path,
        validated_config,
    )
    if (
        selection.all_layer_names != extraction.all_layer_names
        or selection.electric_lines_layer != extraction.electric_lines_layer
        or selection.transformation_posts_layer != extraction.transformation_posts_layer
        or selection.road_segments_layer != extraction.road_segments_layer
        or selection.department_layer != extraction.department_layer
    ):
        raise IgnBdTopoLayerError(
            "IGN road role differs from configured physical-layer inventory"
        )
    layer_name = selection.road_segments_layer
    (road_frame,) = _read_verified_layer_frames(context, (layer_name,))
    loaded = _loaded_layer_from_frame(
        road_frame,
        layer_name,
        "road_segments",
    )
    return IgnBdTopoRoadData(
        extraction=extraction,
        road_segments=loaded.data,
        road_segments_summary=loaded.summary,
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_department_coverage_from_frame`

**Purpose:** Implements `department coverage from frame` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _department_coverage_from_frame(
    extraction: IgnBdTopoExtraction,
    frame: gpd.GeoDataFrame,
    layer_name: str,
    department_field: str,
) -> IgnBdTopoDepartmentCoverage:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoDepartmentCoverage`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `IgnBdTopoExtraction` | `required` |
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `layer_name` | positional-or-keyword | `str` | `required` |
| `department_field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoDepartmentCoverage(<br>        extraction=extraction,<br>        coverage=selected,<br>        summary=summary,<br>        source_provider=archive.provider,<br>        source_product=archive.product,<br>        source_department_code=archive.department_code,<br>        source_edition=archive.edition,<br>        source_product_version=archive.product_version,<br>        source_archive_sha256=archive.sha256,<br>        source_layer=layer_name,<br>    )`
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            f"IGN department coverage layer has no active geometry: {layer_name}"<br>        )`.
  - `IgnBdTopoLayerError(<br>            f"IGN department coverage geometry column is missing: {layer_name}"<br>        )` under lexical guard `geometry_name not in frame.columns`.
  - `IgnBdTopoLayerError(<br>            f"IGN department coverage layer contains no features: {layer_name}"<br>        )` under lexical guard `frame.empty`.
  - `IgnBdTopoLayerError(<br>            "Configured department identity field is missing from IGN coverage "<br>            f"layer: {department_field}"<br>        )` under lexical guard `department_field not in frame.columns`.
  - `IgnBdTopoLayerError(<br>            "Expected exactly one authoritative department coverage feature for "<br>            f"{archive.department_code}, found {selected_count}"<br>        )` under lexical guard `selected_count != 1`.
  - `IgnBdTopoLayerError("Selected department coverage geometry is null")` under lexical guard `selected_geometry.isna().any()`.
  - `IgnBdTopoLayerError("Selected department coverage geometry is empty")` under lexical guard `selected_geometry.is_empty.any()`.
  - `IgnBdTopoLayerError("Selected department coverage geometry is invalid")` under lexical guard `not selected_geometry.is_valid.all()`.
  - `IgnBdTopoLayerError(<br>            "Selected department coverage geometry must be Polygon or MultiPolygon"<br>        )` under lexical guard `not selected_types <= {"Polygon", "MultiPolygon"}`.
  - `IgnBdTopoLayerError(<br>            "IGN department coverage attributes collide with lineage columns: "<br>            + ", ".join(sorted(collisions))<br>        )` under lexical guard `collisions`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_department_coverage_from_frame`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `_department_coverage_from_frame`
- direct call: `tests.unit.test_assess_grid_coverage::_with_alternate_coverage_layer` via `ign_source._department_coverage_from_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `_validate_lambert93` | `landscout.sources.ign_bdtopo_fr._validate_lambert93` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[non_null_mask].geom_type.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[non_null_mask].geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[department_field].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.loc[selected_mask].reset_index(drop=True).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.loc[selected_mask].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_geometry.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_geometry.is_empty.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_geometry.is_valid.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `lineage.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoCoverageLayerSummary` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoCoverageLayerSummary` |
| `crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `null_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `empty_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDepartmentCoverage` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDepartmentCoverage` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna`<br>`geometry[non_null_mask].geom_type.dropna().unique`<br>`geometry[non_null_mask].geom_type.dropna`<br>`selected_geometry.isna().any`<br>`selected_geometry.isna`<br>`selected_geometry.is_empty.any`<br>`selected_geometry.is_valid.all`<br>`selected_geometry.geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | `selected[column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _department_coverage_from_frame(
    extraction: IgnBdTopoExtraction,
    frame: gpd.GeoDataFrame,
    layer_name: str,
    department_field: str,
) -> IgnBdTopoDepartmentCoverage:
    archive = extraction.archive
    try:
        geometry_name = frame.geometry.name
    except (AttributeError, ValueError) as error:
        raise IgnBdTopoLayerError(
            f"IGN department coverage layer has no active geometry: {layer_name}"
        ) from error
    if geometry_name not in frame.columns:
        raise IgnBdTopoLayerError(
            f"IGN department coverage geometry column is missing: {layer_name}"
        )
    crs = _validate_lambert93(frame.crs, layer_name)
    if frame.empty:
        raise IgnBdTopoLayerError(
            f"IGN department coverage layer contains no features: {layer_name}"
        )

    geometry = frame.geometry
    null_mask = geometry.isna()
    non_null_mask = ~null_mask
    empty_mask = non_null_mask & geometry.is_empty
    measurable_mask = non_null_mask & ~geometry.is_empty
    invalid_mask = measurable_mask & ~geometry.is_valid
    geometry_types = tuple(
        sorted(
            str(value) for value in geometry[non_null_mask].geom_type.dropna().unique()
        )
    )

    if department_field not in frame.columns:
        raise IgnBdTopoLayerError(
            "Configured department identity field is missing from IGN coverage "
            f"layer: {department_field}"
        )
    selected_mask = frame[department_field].eq(archive.department_code)
    selected_count = int(selected_mask.sum())
    if selected_count != 1:
        raise IgnBdTopoLayerError(
            "Expected exactly one authoritative department coverage feature for "
            f"{archive.department_code}, found {selected_count}"
        )
    selected = frame.loc[selected_mask].reset_index(drop=True).copy()
    selected_geometry = selected.geometry
    if selected_geometry.isna().any():
        raise IgnBdTopoLayerError("Selected department coverage geometry is null")
    if selected_geometry.is_empty.any():
        raise IgnBdTopoLayerError("Selected department coverage geometry is empty")
    if not selected_geometry.is_valid.all():
        raise IgnBdTopoLayerError("Selected department coverage geometry is invalid")
    selected_types = set(selected_geometry.geom_type.dropna())
    if not selected_types <= {"Polygon", "MultiPolygon"}:
        raise IgnBdTopoLayerError(
            "Selected department coverage geometry must be Polygon or MultiPolygon"
        )

    lineage = {
        "source_provider": archive.provider,
        "source_product": archive.product,
        "source_department_code": archive.department_code,
        "source_edition": archive.edition,
        "source_product_version": archive.product_version,
        "source_archive_sha256": archive.sha256,
        "source_layer": layer_name,
        "spatial_role": COVERAGE_SPATIAL_ROLE,
    }
    collisions = set(lineage) & set(selected.columns)
    if collisions:
        raise IgnBdTopoLayerError(
            "IGN department coverage attributes collide with lineage columns: "
            + ", ".join(sorted(collisions))
        )
    for column, value in lineage.items():
        selected[column] = value

    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name=layer_name,
        crs=crs.to_string(),
        source_feature_count=len(frame),
        selected_feature_count=selected_count,
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
        department_code_field=department_field,
        selected_department_code=archive.department_code,
    )
    return IgnBdTopoDepartmentCoverage(
        extraction=extraction,
        coverage=selected,
        summary=summary,
        source_provider=archive.provider,
        source_product=archive.product,
        source_department_code=archive.department_code,
        source_edition=archive.edition,
        source_product_version=archive.product_version,
        source_archive_sha256=archive.sha256,
        source_layer=layer_name,
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `load_ign_bdtopo_department_coverage`

**Purpose:** Load the one authoritative configured department coverage feature.

**Exact signature**

```python
def load_ign_bdtopo_department_coverage(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoDepartmentCoverage`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `IgnBdTopoExtraction` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_department_coverage_from_frame(<br>        extraction,<br>        frame,<br>        layer_name,<br>        validated_config.coverage.department_layer.department_code_field,<br>    )`
- Explicit raise paths:
  - `IgnBdTopoLayerError(<br>            "IGN coverage role differs from configured physical-layer inventory"<br>        )` under lexical guard `selection.all_layer_names != extraction.all_layer_names<br>        or selection.electric_lines_layer != extraction.electric_lines_layer<br>        or selection.transformation_posts_layer != extraction.transformation_posts_layer<br>        or selection.road_segments_layer != extraction.road_segments_layer<br>        or selection.department_layer != extraction.department_layer`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_department_coverage` via `load_ign_bdtopo_department_coverage`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_department_coverage` via `load_ign_bdtopo_department_coverage`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- direct call: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `load_ign_bdtopo_department_coverage`
- value/type reference: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `load_ign_bdtopo_department_coverage`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `load_ign_bdtopo_department_coverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `load_ign_bdtopo_department_coverage`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_road_role` via `load_ign_bdtopo_department_coverage`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_road_role` via `load_ign_bdtopo_department_coverage`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_electricity_roles` via `load_ign_bdtopo_department_coverage`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_electricity_roles` via `load_ign_bdtopo_department_coverage`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` via `load_ign_bdtopo_department_coverage`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` via `load_ign_bdtopo_department_coverage`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `load_ign_bdtopo_department_coverage`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `load_ign_bdtopo_department_coverage`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `load_ign_bdtopo_department_coverage`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `load_ign_bdtopo_department_coverage`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `load_ign_bdtopo_department_coverage`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `load_ign_bdtopo_department_coverage`
- direct call: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `load_ign_bdtopo_department_coverage`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `load_ign_bdtopo_department_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_layer_source_config` | `landscout.sources.ign_bdtopo_fr._validated_layer_source_config` |
| `_validate_archive_config_lineage` | `landscout.sources.ign_bdtopo_fr._validate_archive_config_lineage` |
| `_validate_extraction_envelope` | `landscout.sources.ign_bdtopo_fr._validate_extraction_envelope` |
| `_discover_configured_physical_roles` | `landscout.sources.ign_bdtopo_fr._discover_configured_physical_roles` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `_read_verified_layer_frames` | `landscout.sources.ign_bdtopo_fr._read_verified_layer_frames` |
| `_department_coverage_from_frame` | `landscout.sources.ign_bdtopo_fr._department_coverage_from_frame` |

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
def load_ign_bdtopo_department_coverage(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
    """Load the one authoritative configured department coverage feature."""

    validated_config = _validated_layer_source_config(config)
    _validate_archive_config_lineage(extraction, validated_config)
    context = _validate_extraction_envelope(extraction)
    selection = _discover_configured_physical_roles(
        context.geopackage_path,
        validated_config,
    )
    if (
        selection.all_layer_names != extraction.all_layer_names
        or selection.electric_lines_layer != extraction.electric_lines_layer
        or selection.transformation_posts_layer != extraction.transformation_posts_layer
        or selection.road_segments_layer != extraction.road_segments_layer
        or selection.department_layer != extraction.department_layer
    ):
        raise IgnBdTopoLayerError(
            "IGN coverage role differs from configured physical-layer inventory"
        )
    layer_name = selection.department_layer
    (frame,) = _read_verified_layer_frames(context, (layer_name,))
    return _department_coverage_from_frame(
        extraction,
        frame,
        layer_name,
        validated_config.coverage.department_layer.department_code_field,
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_revalidate_ign_bdtopo_electricity_data`

**Purpose:** Fresh-read and exact-compare one supplied electricity source bundle.

**Exact signature**

```python
def _revalidate_ign_bdtopo_electricity_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `object` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `fresh`
- Explicit raise paths:
  - `TypeError("IGN electricity source type is invalid")` under lexical guard `type(source) is not IgnBdTopoElectricityData`.
  - `TypeError("IGN electricity source config type is invalid")` under lexical guard `type(config) is not IgnBdTopoSourceConfig`.
  - `ValueError("IGN electricity source spatial role is invalid")` under lexical guard `source.spatial_role != SPATIAL_ROLE`.
  - `re-raise`.
  - `IgnBdTopoLayerError(<br>            "IGN electricity source-complete revalidation failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`
- direct call: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_revalidate_ign_bdtopo_electricity_data`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_revalidate_ign_bdtopo_electricity_data`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_ign_bdtopo_electricity` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_electricity` |
| `_compare_loaded_frame` | `landscout.sources.ign_bdtopo_fr._compare_loaded_frame` |
| `_compare_layer_summary` | `landscout.sources.ign_bdtopo_fr._compare_layer_summary` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

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
def _revalidate_ign_bdtopo_electricity_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
    """Fresh-read and exact-compare one supplied electricity source bundle."""

    try:
        if type(source) is not IgnBdTopoElectricityData:
            raise TypeError("IGN electricity source type is invalid")
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("IGN electricity source config type is invalid")
        fresh = load_ign_bdtopo_electricity(source.extraction, config)
        _compare_loaded_frame(
            source.electric_lines, fresh.electric_lines, "electric lines"
        )
        _compare_loaded_frame(
            source.transformation_posts,
            fresh.transformation_posts,
            "transformation posts",
        )
        _compare_layer_summary(
            source.electric_lines_summary, fresh.electric_lines_summary
        )
        _compare_layer_summary(
            source.transformation_posts_summary,
            fresh.transformation_posts_summary,
        )
        if source.spatial_role != SPATIAL_ROLE:
            raise ValueError("IGN electricity source spatial role is invalid")
        return fresh
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN electricity source-complete revalidation failed"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_revalidate_ign_bdtopo_road_data`

**Purpose:** Fresh-read and exact-compare one supplied road source bundle.

**Exact signature**

```python
def _revalidate_ign_bdtopo_road_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoRoadData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `object` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `fresh`
- Explicit raise paths:
  - `TypeError("IGN road source type is invalid")` under lexical guard `type(source) is not IgnBdTopoRoadData`.
  - `TypeError("IGN road source config type is invalid")` under lexical guard `type(config) is not IgnBdTopoSourceConfig`.
  - `re-raise`.
  - `IgnBdTopoLayerError(<br>            "IGN road source-complete revalidation failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
- direct call: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `_revalidate_ign_bdtopo_road_data`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `_revalidate_ign_bdtopo_road_data`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |
| `_compare_loaded_frame` | `landscout.sources.ign_bdtopo_fr._compare_loaded_frame` |
| `_compare_layer_summary` | `landscout.sources.ign_bdtopo_fr._compare_layer_summary` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

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
def _revalidate_ign_bdtopo_road_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
    """Fresh-read and exact-compare one supplied road source bundle."""

    try:
        if type(source) is not IgnBdTopoRoadData:
            raise TypeError("IGN road source type is invalid")
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("IGN road source config type is invalid")
        fresh = load_ign_bdtopo_roads(source.extraction, config)
        _compare_loaded_frame(
            source.road_segments,
            fresh.road_segments,
            "road segments",
        )
        _compare_layer_summary(
            source.road_segments_summary,
            fresh.road_segments_summary,
        )
        return fresh
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN road source-complete revalidation failed"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_coverage_summary_contract`

**Purpose:** Implements `validate coverage summary contract` within the file role: Acquires, verifies, safely extracts/inventories, selects globally unique configured roles, loads, and source-completely revalidates fresh IGN BD TOPO data.

**Exact signature**

```python
def _validate_coverage_summary_contract(
    summary: object,
) -> IgnBdTopoCoverageLayerSummary:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoCoverageLayerSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `summary` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `summary`
- Explicit raise paths:
  - `IgnBdTopoLayerError("IGN coverage summary type is invalid")` under lexical guard `type(summary) is not IgnBdTopoCoverageLayerSummary`.
  - `IgnBdTopoLayerError(<br>                f"IGN coverage summary {name} must be a strict non-negative integer"<br>            )` under lexical guard `type(value) is not int or value < 0`.
  - `IgnBdTopoLayerError("IGN coverage summary counts are inconsistent")` under lexical guard `summary.selected_feature_count > summary.source_feature_count`.
  - `IgnBdTopoLayerError("IGN coverage summary columns are invalid")` under lexical guard `type(summary.columns) is not tuple<br>        or not summary.columns<br>        or any(<br>            not isinstance(value, str) or not value or value != value.strip()<br>            for value in summary.columns<br>        )<br>        or len(set(summary.columns)) != len(summary.columns)`.
  - `IgnBdTopoLayerError("IGN coverage summary dtypes are invalid")` under lexical guard `type(summary.dtypes) is not tuple<br>        or len(summary.dtypes) != len(summary.columns)<br>        or any(<br>            type(item) is not tuple<br>            or len(item) != 2<br>            or any(not isinstance(value, str) or not value for value in item)<br>            for item in summary.dtypes<br>        )<br>        or tuple(name for name, _ in summary.dtypes) != summary.columns`.
  - `IgnBdTopoLayerError("IGN coverage summary geometry types are invalid")` under lexical guard `type(summary.geometry_types) is not tuple<br>        or summary.geometry_types != tuple(sorted(set(summary.geometry_types)))<br>        or any(<br>            not isinstance(value, str) or not value for value in summary.geometry_types<br>        )`.
  - `IgnBdTopoLayerError("IGN coverage summary spatial role is invalid")` under lexical guard `summary.spatial_role != COVERAGE_SPATIAL_ROLE`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_coverage_summary_contract(
    summary: object,
) -> IgnBdTopoCoverageLayerSummary:
    if type(summary) is not IgnBdTopoCoverageLayerSummary:
        raise IgnBdTopoLayerError("IGN coverage summary type is invalid")
    for name in (
        "source_feature_count",
        "selected_feature_count",
        "null_geometry_count",
        "empty_geometry_count",
        "invalid_geometry_count",
    ):
        value = getattr(summary, name)
        if type(value) is not int or value < 0:
            raise IgnBdTopoLayerError(
                f"IGN coverage summary {name} must be a strict non-negative integer"
            )
    if summary.selected_feature_count > summary.source_feature_count:
        raise IgnBdTopoLayerError("IGN coverage summary counts are inconsistent")
    if (
        type(summary.columns) is not tuple
        or not summary.columns
        or any(
            not isinstance(value, str) or not value or value != value.strip()
            for value in summary.columns
        )
        or len(set(summary.columns)) != len(summary.columns)
    ):
        raise IgnBdTopoLayerError("IGN coverage summary columns are invalid")
    if (
        type(summary.dtypes) is not tuple
        or len(summary.dtypes) != len(summary.columns)
        or any(
            type(item) is not tuple
            or len(item) != 2
            or any(not isinstance(value, str) or not value for value in item)
            for item in summary.dtypes
        )
        or tuple(name for name, _ in summary.dtypes) != summary.columns
    ):
        raise IgnBdTopoLayerError("IGN coverage summary dtypes are invalid")
    if (
        type(summary.geometry_types) is not tuple
        or summary.geometry_types != tuple(sorted(set(summary.geometry_types)))
        or any(
            not isinstance(value, str) or not value for value in summary.geometry_types
        )
    ):
        raise IgnBdTopoLayerError("IGN coverage summary geometry types are invalid")
    if summary.spatial_role != COVERAGE_SPATIAL_ROLE:
        raise IgnBdTopoLayerError("IGN coverage summary spatial role is invalid")
    return summary
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_revalidate_ign_bdtopo_department_coverage`

**Purpose:** Fresh-read and exact-compare selected coverage with its physical layer.

**Exact signature**

```python
def _revalidate_ign_bdtopo_department_coverage(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoDepartmentCoverage`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `object` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `fresh`
- Explicit raise paths:
  - `TypeError("IGN department coverage type is invalid")` under lexical guard `type(source) is not IgnBdTopoDepartmentCoverage`.
  - `TypeError("IGN coverage source config type is invalid")` under lexical guard `type(config) is not IgnBdTopoSourceConfig`.
  - `ValueError("IGN coverage summary differs from physical source")` under lexical guard `source.summary != fresh.summary`.
  - `ValueError("IGN coverage lineage differs from physical source")` under lexical guard `any(getattr(source, name) != getattr(fresh, name) for name in scalar_names)`.
  - `re-raise`.
  - `IgnBdTopoLayerError(<br>            "IGN coverage source-complete revalidation failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |
| `_compare_loaded_frame` | `landscout.sources.ign_bdtopo_fr._compare_loaded_frame` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerError` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerError` |

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
def _revalidate_ign_bdtopo_department_coverage(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
    """Fresh-read and exact-compare selected coverage with its physical layer."""

    try:
        if type(source) is not IgnBdTopoDepartmentCoverage:
            raise TypeError("IGN department coverage type is invalid")
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("IGN coverage source config type is invalid")
        fresh = load_ign_bdtopo_department_coverage(source.extraction, config)
        _compare_loaded_frame(source.coverage, fresh.coverage, "department coverage")
        if source.summary != fresh.summary:
            raise ValueError("IGN coverage summary differs from physical source")
        scalar_names = (
            "source_provider",
            "source_product",
            "source_department_code",
            "source_edition",
            "source_product_version",
            "source_archive_sha256",
            "source_layer",
            "spatial_role",
        )
        if any(getattr(source, name) != getattr(fresh, name) for name in scalar_names):
            raise ValueError("IGN coverage lineage differs from physical source")
        return fresh
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN coverage source-complete revalidation failed"
        ) from error
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
"""Official IGN BD TOPO archive ingestion for spatial screening sources.

This adapter deliberately stops at source acquisition, archive/layer discovery,
and source-layer loading. IGN geometries are screening proxies and are not
claimed to prove exact current grid assets, connection points, or legal access.
"""

from __future__ import annotations

import os
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass
from datetime import UTC, date, datetime
from hashlib import md5, sha256
from pathlib import Path, PurePosixPath, PureWindowsPath
from shutil import copy2, copyfileobj
from typing import Annotated, Any, Literal, Self
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
import py7zr
import pyogrio  # type: ignore[import-untyped]
from py7zr.exceptions import ArchiveError
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StrictBool,
    StringConstraints,
    ValidationError,
    field_validator,
    model_validator,
)
from pyproj import CRS

from landscout.common.safe_http import open_safe_https
from landscout.common.strict_json import loads_strict_json_object
from landscout.common.strict_yaml import loads_strict_yaml

DEFAULT_CONFIG_PATH = Path("configs/sources/ign_bdtopo_fr.yaml")
DEFAULT_CACHE_DIR = Path("data/cache/ign_bdtopo")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
SPATIAL_ROLE = "PROXY_GEOMETRY"
COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"

SpatialRole = Literal["PROXY_GEOMETRY"]
CoverageSpatialRole = Literal["SOURCE_COVERAGE_BOUNDARY"]
LogicalLayerName = Literal[
    "electric_lines",
    "transformation_posts",
    "road_segments",
]
Projection = Literal["EPSG:2154"]
PackageFormat = Literal["GPKG"]
ArchiveFormat = Literal["7z"]
ChecksumAlgorithm = Literal["md5", "sha256"]

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
DepartmentCode = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=r"^(?:[0-9]{2}|2A|2B|97[1-6])$",
    ),
]
EditionString = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^\d{4}-\d{2}-\d{2}$"),
]
HexChecksum = Annotated[
    str,
    StringConstraints(strip_whitespace=True, to_lower=True, pattern=r"^[0-9a-fA-F]+$"),
]
CanonicalSha256 = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^[0-9a-f]{64}$"),
]
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
StrictNonNegativeFloat = Annotated[
    float,
    Field(strict=True, ge=0, allow_inf_nan=False),
]


class IgnBdTopoLogicalLayerConfig(BaseModel):
    """Catalogue class label and normalized tokens used for layer discovery."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    class_label: NonEmptyString
    match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)

    @field_validator("match_tokens")
    @classmethod
    def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(token) for token in value)
        if any(not token for token in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(set(normalized)) != len(normalized):
            raise ValueError("Layer match tokens must be unique after normalization")
        return value


class IgnBdTopoLogicalLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    electric_lines: IgnBdTopoLogicalLayerConfig
    transformation_posts: IgnBdTopoLogicalLayerConfig

    @model_validator(mode="after")
    def _different_token_sets(self) -> Self:
        electric = {
            _normalize_words(token) for token in self.electric_lines.match_tokens
        }
        posts = {
            _normalize_words(token) for token in self.transformation_posts.match_tokens
        }
        if electric == posts:
            raise ValueError("Logical layers must use different match tokens")
        return self


class IgnBdTopoDepartmentLayerConfig(IgnBdTopoLogicalLayerConfig):
    """Configured department layer and its observed identity field."""

    department_code_field: NonEmptyString


class IgnBdTopoAccessConfig(BaseModel):
    """Configured factual transport layers loaded outside extraction metadata."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    road_segments: IgnBdTopoLogicalLayerConfig


class IgnBdTopoCoverageConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    department_layer: IgnBdTopoDepartmentLayerConfig


class IgnBdTopoSourceConfig(BaseModel):
    """Strict, reproducible description of one official IGN package."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: Literal[
        "Institut national de l'information géographique et forestière (IGN)"
    ]
    product: Literal["BD TOPO"]
    department_code: DepartmentCode
    edition: EditionString
    product_version: NonEmptyString | None = None
    projection: Projection
    format: PackageFormat
    archive_format: ArchiveFormat
    source_url: HttpUrl
    checksum_url: HttpUrl | None = None
    official_checksum_algorithm: ChecksumAlgorithm | None = None
    official_checksum: HexChecksum | None = None
    expected_archive_size_bytes: StrictPositiveInt | None = None
    cache_max_age_hours: StrictNonNegativeFloat
    logical_layers: IgnBdTopoLogicalLayersConfig
    access: IgnBdTopoAccessConfig
    coverage: IgnBdTopoCoverageConfig

    @field_validator("edition")
    @classmethod
    def _valid_edition_date(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError as error:
            raise ValueError("edition must be a valid ISO calendar date") from error
        return value

    @model_validator(mode="after")
    def _consistent_package_and_checksum(self) -> Self:
        path = unquote(urlparse(str(self.source_url)).path)
        if Path(path).suffix.casefold() != f".{self.archive_format}":
            raise ValueError("source_url extension does not match archive_format")

        has_algorithm = self.official_checksum_algorithm is not None
        has_checksum = self.official_checksum is not None
        if has_algorithm != has_checksum:
            raise ValueError(
                "official_checksum_algorithm and official_checksum must be set together"
            )
        if (
            self.official_checksum_algorithm == "md5"
            and len(self.official_checksum or "") != 32
        ):
            raise ValueError(
                "An official MD5 checksum must contain 32 hexadecimal digits"
            )
        if (
            self.official_checksum_algorithm == "sha256"
            and len(self.official_checksum or "") != 64
        ):
            raise ValueError(
                "An official SHA256 checksum must contain 64 hexadecimal digits"
            )
        if self.checksum_url is not None and not has_checksum:
            raise ValueError(
                "checksum_url requires a pinned official checksum and algorithm"
            )
        return self


class IgnBdTopoError(RuntimeError):
    """Base error for controlled IGN BD TOPO source failures."""


class IgnBdTopoDownloadError(IgnBdTopoError):
    """Raised when an IGN archive cannot be downloaded or cached safely."""


class IgnBdTopoArchiveError(IgnBdTopoError):
    """Raised when an IGN archive or its extraction is unsafe or invalid."""


class IgnBdTopoLayerError(IgnBdTopoError):
    """Raised when required GeoPackage layers cannot be discovered or loaded."""


@dataclass(frozen=True)
class IgnBdTopoArchiveIntegrity:
    file_size: int
    sha256: str
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: bool


@dataclass(frozen=True)
class IgnBdTopoDownload:
    provider: str
    product: str
    department_code: str
    edition: str
    product_version: str | None
    projection: str
    package_format: str
    archive_format: str
    source_url: str
    checksum_url: str | None
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: bool
    path: Path
    cache_hit: bool
    spatial_role: SpatialRole = "PROXY_GEOMETRY"


@dataclass(frozen=True)
class IgnBdTopoLayerSelection:
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str


@dataclass(frozen=True)
class IgnBdTopoExtraction:
    archive: IgnBdTopoDownload
    extraction_path: Path
    geopackage_path: Path
    geopackage_filename: str
    geopackage_size_bytes: int
    geopackage_sha256: str
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    road_segments_layer: str
    department_layer: str
    cache_hit: bool
    spatial_role: SpatialRole = "PROXY_GEOMETRY"


@dataclass(frozen=True)
class IgnBdTopoLayerSummary:
    logical_name: LogicalLayerName
    source_layer_name: str
    crs: str
    feature_count: int
    columns: tuple[str, ...]
    dtypes: tuple[tuple[str, str], ...]
    null_geometry_count: int
    empty_geometry_count: int
    invalid_geometry_count: int
    geometry_types: tuple[str, ...]
    spatial_role: SpatialRole = "PROXY_GEOMETRY"


@dataclass(frozen=True)
class IgnBdTopoLoadedLayer:
    data: gpd.GeoDataFrame
    summary: IgnBdTopoLayerSummary


@dataclass(frozen=True)
class IgnBdTopoElectricityData:
    extraction: IgnBdTopoExtraction
    electric_lines: gpd.GeoDataFrame
    transformation_posts: gpd.GeoDataFrame
    electric_lines_summary: IgnBdTopoLayerSummary
    transformation_posts_summary: IgnBdTopoLayerSummary
    spatial_role: SpatialRole = "PROXY_GEOMETRY"


@dataclass(frozen=True)
class IgnBdTopoRoadData:
    """Unfiltered factual road geometry from one verified IGN extraction."""

    extraction: IgnBdTopoExtraction
    road_segments: gpd.GeoDataFrame
    road_segments_summary: IgnBdTopoLayerSummary


@dataclass(frozen=True)
class IgnBdTopoCoverageLayerSummary:
    """Observed source-layer schema plus the authoritative selected feature."""

    source_layer_name: str
    crs: str
    source_feature_count: int
    selected_feature_count: int
    columns: tuple[str, ...]
    dtypes: tuple[tuple[str, str], ...]
    null_geometry_count: int
    empty_geometry_count: int
    invalid_geometry_count: int
    geometry_types: tuple[str, ...]
    department_code_field: str
    selected_department_code: str
    spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"


@dataclass(frozen=True)
class IgnBdTopoDepartmentCoverage:
    """Selected department coverage with package lineage and source schema."""

    extraction: IgnBdTopoExtraction
    coverage: gpd.GeoDataFrame
    summary: IgnBdTopoCoverageLayerSummary
    source_provider: str
    source_product: str
    source_department_code: str
    source_edition: str
    source_product_version: str | None
    source_archive_sha256: str
    source_layer: str
    spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"


class _CacheMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    provider: str
    product: str
    department_code: str
    edition: str
    product_version: str | None
    projection: str
    package_format: str
    archive_format: str
    source_url: str
    checksum_url: str | None
    download_timestamp: str
    filename: str
    file_size: StrictPositiveInt
    sha256: CanonicalSha256
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: StrictBool
    spatial_role: SpatialRole

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("IGN cache schema version must be an exact integer")
        return value


class _ExtractedEntryMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    relative_path: str
    kind: Literal["file", "directory"]
    size_bytes: int | None = Field(default=None, strict=True, ge=0)
    sha256: CanonicalSha256 | None = None


class _ExtractionMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[3]
    archive_sha256: CanonicalSha256
    geopackage_relative_path: str
    geopackage_size_bytes: StrictPositiveInt
    geopackage_sha256: CanonicalSha256
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    road_segments_layer: str
    department_layer: str
    extracted_entries: tuple[_ExtractedEntryMetadata, ...]
    spatial_role: SpatialRole

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("IGN extraction schema version must be an exact integer")
        return value


def _normalize_words(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    ascii_like = "".join(char for char in decomposed if not unicodedata.combining(char))
    return " ".join(re.findall(r"[a-z0-9]+", ascii_like))


def load_ign_bdtopo_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> IgnBdTopoSourceConfig:
    """Load and strictly validate the pinned IGN source configuration."""

    try:
        content = loads_strict_yaml(path.read_bytes())
    except (OSError, TypeError, ValueError) as error:
        raise IgnBdTopoDownloadError(
            f"Cannot read IGN source config: {path}"
        ) from error
    if not isinstance(content, dict):
        raise IgnBdTopoDownloadError(f"Expected a YAML mapping in {path}")
    try:
        return IgnBdTopoSourceConfig.model_validate(content)
    except ValidationError as error:
        raise IgnBdTopoDownloadError(f"IGN source config is invalid: {path}") from error


def _validated_source_config(
    config: object,
    *,
    error_type: type[IgnBdTopoError] = IgnBdTopoDownloadError,
) -> IgnBdTopoSourceConfig:
    try:
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("IGN source config type is invalid")
        return IgnBdTopoSourceConfig.model_validate(config.model_dump(mode="python"))
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise error_type("IGN source config is invalid") from error


def _archive_filename(config: IgnBdTopoSourceConfig) -> str:
    filename = Path(unquote(urlparse(str(config.source_url)).path)).name
    if not filename or Path(filename).suffix.casefold() != ".7z":
        raise IgnBdTopoDownloadError("IGN source URL does not identify a .7z archive")
    return filename


def _calculate_checksums(
    path: Path, official_algorithm: ChecksumAlgorithm | None
) -> tuple[str, str | None]:
    sha256_digest = sha256()
    official_digest = None
    if official_algorithm == "md5":
        official_digest = md5(usedforsecurity=False)
    elif official_algorithm == "sha256":
        official_digest = sha256()

    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
                sha256_digest.update(chunk)
                if official_digest is not None:
                    official_digest.update(chunk)
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot read IGN archive: {path}") from error
    return (
        sha256_digest.hexdigest(),
        official_digest.hexdigest() if official_digest is not None else None,
    )


def validate_ign_bdtopo_archive(
    path: Path, config: IgnBdTopoSourceConfig
) -> IgnBdTopoArchiveIntegrity:
    """Validate size, configured official checksum, and available 7z CRC data.

    Some official IGN archives omit container CRC metadata, for which py7zr
    returns ``None``.  Such archives still require exact official size/checksum
    validation here and a successful full extraction before they are usable.
    """

    config = _validated_source_config(config, error_type=IgnBdTopoArchiveError)
    if not isinstance(path, Path):
        raise IgnBdTopoArchiveError("IGN archive path must be a pathlib.Path")
    if path.is_symlink() or path.is_junction() or not path.is_file():
        raise IgnBdTopoArchiveError(f"IGN archive does not exist: {path}")
    try:
        file_size = path.stat().st_size
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot inspect IGN archive: {path}") from error
    if file_size <= 0:
        raise IgnBdTopoArchiveError(f"IGN archive is empty: {path}")
    if (
        config.expected_archive_size_bytes is not None
        and file_size != config.expected_archive_size_bytes
    ):
        raise IgnBdTopoArchiveError(
            "IGN archive size does not match the official catalogue: "
            f"{file_size} != {config.expected_archive_size_bytes}"
        )

    local_sha256, calculated_official = _calculate_checksums(
        path, config.official_checksum_algorithm
    )
    official_validated = config.official_checksum is not None
    if official_validated and calculated_official != config.official_checksum:
        raise IgnBdTopoArchiveError(
            "IGN archive does not match the pinned official "
            f"{config.official_checksum_algorithm} checksum"
        )

    try:
        with py7zr.SevenZipFile(path, mode="r") as archive:
            integrity_result = archive.test()
    except (ArchiveError, EOFError, OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"IGN archive is not a readable 7z file: {path}"
        ) from error
    if integrity_result is False:
        raise IgnBdTopoArchiveError(
            f"IGN archive failed its 7z CRC integrity check: {path}"
        )

    return IgnBdTopoArchiveIntegrity(
        file_size=file_size,
        sha256=local_sha256,
        official_checksum_algorithm=config.official_checksum_algorithm,
        official_checksum=config.official_checksum,
        official_checksum_validated=official_validated,
    )


def _cache_metadata_from_download(download: IgnBdTopoDownload) -> _CacheMetadata:
    return _CacheMetadata(
        schema_version=1,
        provider=download.provider,
        product=download.product,
        department_code=download.department_code,
        edition=download.edition,
        product_version=download.product_version,
        projection=download.projection,
        package_format=download.package_format,
        archive_format=download.archive_format,
        source_url=download.source_url,
        checksum_url=download.checksum_url,
        download_timestamp=download.download_timestamp,
        filename=download.filename,
        file_size=download.file_size,
        sha256=download.sha256,
        official_checksum_algorithm=download.official_checksum_algorithm,
        official_checksum=download.official_checksum,
        official_checksum_validated=download.official_checksum_validated,
        spatial_role=download.spatial_role,
    )


def _download_from_metadata(
    metadata: _CacheMetadata, archive_path: Path, *, cache_hit: bool
) -> IgnBdTopoDownload:
    return IgnBdTopoDownload(
        provider=metadata.provider,
        product=metadata.product,
        department_code=metadata.department_code,
        edition=metadata.edition,
        product_version=metadata.product_version,
        projection=metadata.projection,
        package_format=metadata.package_format,
        archive_format=metadata.archive_format,
        source_url=metadata.source_url,
        checksum_url=metadata.checksum_url,
        download_timestamp=metadata.download_timestamp,
        filename=metadata.filename,
        file_size=metadata.file_size,
        sha256=metadata.sha256,
        official_checksum_algorithm=metadata.official_checksum_algorithm,
        official_checksum=metadata.official_checksum,
        official_checksum_validated=metadata.official_checksum_validated,
        path=archive_path,
        cache_hit=cache_hit,
        spatial_role=metadata.spatial_role,
    )


def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDownload | None:
    if not archive_path.is_file() or not metadata_path.is_file():
        return None
    try:
        metadata = _CacheMetadata.model_validate(
            loads_strict_json_object(metadata_path.read_bytes())
        )
        downloaded_at = datetime.fromisoformat(metadata.download_timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(
            None
        ):
            return None
        age_seconds = (
            datetime.now(UTC) - downloaded_at.astimezone(UTC)
        ).total_seconds()
        if age_seconds < 0 or age_seconds > config.cache_max_age_hours * 3600:
            return None

        expected_values: tuple[tuple[Any, Any], ...] = (
            (metadata.provider, config.provider),
            (metadata.product, config.product),
            (metadata.department_code, config.department_code),
            (metadata.edition, config.edition),
            (metadata.product_version, config.product_version),
            (metadata.projection, config.projection),
            (metadata.package_format, config.format),
            (metadata.archive_format, config.archive_format),
            (metadata.source_url, str(config.source_url)),
            (
                metadata.checksum_url,
                str(config.checksum_url) if config.checksum_url is not None else None,
            ),
            (metadata.filename, archive_path.name),
            (
                metadata.official_checksum_algorithm,
                config.official_checksum_algorithm,
            ),
            (metadata.official_checksum, config.official_checksum),
            (metadata.spatial_role, SPATIAL_ROLE),
        )
        if any(actual != expected for actual, expected in expected_values):
            return None

        integrity = validate_ign_bdtopo_archive(archive_path, config)
        if (
            metadata.file_size != integrity.file_size
            or metadata.sha256 != integrity.sha256
            or metadata.official_checksum_validated
            != integrity.official_checksum_validated
        ):
            return None
        return _download_from_metadata(metadata, archive_path, cache_hit=True)
    except (
        IgnBdTopoArchiveError,
        OSError,
        TypeError,
        ValueError,
        ValidationError,
    ):
        return None


def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)


def _cache_recovery_paths(
    archive_path: Path,
    metadata_path: Path,
) -> tuple[Path, Path]:
    return (
        archive_path.with_name(f"{archive_path.name}.bak"),
        metadata_path.with_name(f"{metadata_path.name}.bak"),
    )


def _require_no_cache_recovery_material(
    archive_path: Path,
    metadata_path: Path,
) -> None:
    recovery_paths = _cache_recovery_paths(archive_path, metadata_path)
    if any(
        path.exists() or path.is_symlink() or path.is_junction()
        for path in recovery_paths
    ):
        raise IgnBdTopoDownloadError(
            "IGN cache recovery backup already exists; manual recovery is required"
        )


def _prepare_temporary_cache_file(path: Path) -> None:
    try:
        if path.is_symlink() or path.is_junction():
            raise IgnBdTopoDownloadError(
                "IGN cache temporary path is a link or junction"
            )
        if path.exists():
            if not path.is_file():
                raise IgnBdTopoDownloadError(
                    "IGN cache temporary path is not a regular file"
                )
            path.unlink()
    except IgnBdTopoDownloadError:
        raise
    except OSError as error:
        raise IgnBdTopoDownloadError(
            "IGN cache temporary path cannot be prepared safely"
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
        raise IgnBdTopoDownloadError(
            "IGN cache temporary files could not be cleaned safely"
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
            if not metadata_existed:
                metadata_path.unlink(missing_ok=True)
        except (IgnBdTopoArchiveError, OSError) as rollback_error:
            raise IgnBdTopoDownloadError(
                "IGN cache publication and rollback both failed"
            ) from rollback_error
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise
    else:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)


def download_ign_bdtopo_archive(
    config: IgnBdTopoSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> IgnBdTopoDownload:
    """Download or reuse the pinned IGN package with atomic cache publication."""

    config = _validated_source_config(config)
    filename = _archive_filename(config)
    archive_path = cache_dir / filename
    metadata_path = cache_dir / f"{filename}.metadata.json"
    _require_no_cache_recovery_material(archive_path, metadata_path)
    cached = _load_cached_download(archive_path, metadata_path, config)
    if cached is not None:
        return cached

    cache_dir.mkdir(parents=True, exist_ok=True)
    temporary_archive = archive_path.with_name(f"{archive_path.name}.part")
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    _prepare_temporary_cache_file(temporary_archive)
    _prepare_temporary_cache_file(temporary_metadata)
    source_url = str(config.source_url)
    try:
        with (
            open_safe_https(
                source_url,
                timeout=timeout,
                headers={"User-Agent": "LandScout-AI/0.1"},
            ) as response,
            temporary_archive.open("xb") as output,
        ):
            copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)

        integrity = validate_ign_bdtopo_archive(temporary_archive, config)
        download_timestamp = datetime.now(UTC).isoformat()
        result = IgnBdTopoDownload(
            provider=config.provider,
            product=config.product,
            department_code=config.department_code,
            edition=config.edition,
            product_version=config.product_version,
            projection=config.projection,
            package_format=config.format,
            archive_format=config.archive_format,
            source_url=source_url,
            checksum_url=(
                str(config.checksum_url) if config.checksum_url is not None else None
            ),
            download_timestamp=download_timestamp,
            filename=filename,
            file_size=integrity.file_size,
            sha256=integrity.sha256,
            official_checksum_algorithm=integrity.official_checksum_algorithm,
            official_checksum=integrity.official_checksum,
            official_checksum_validated=integrity.official_checksum_validated,
            path=archive_path,
            cache_hit=False,
        )
        metadata = _cache_metadata_from_download(result)
        with temporary_metadata.open("x", encoding="utf-8") as output:
            output.write(metadata.model_dump_json(indent=2) + "\n")
        _publish_cache_pair(
            temporary_archive, temporary_metadata, archive_path, metadata_path
        )
        return result
    except IgnBdTopoArchiveError:
        raise
    except (HTTPError, URLError, OSError) as error:
        raise IgnBdTopoDownloadError(f"IGN download failed: {source_url}") from error
    finally:
        _cleanup_temporary_cache_files(
            (temporary_archive, temporary_metadata),
            sys.exception(),
        )


_WINDOWS_FORBIDDEN = frozenset('<>:"/\\|?*')
_WINDOWS_RESERVED = frozenset(
    {
        "con",
        "prn",
        "aux",
        "nul",
        "clock$",
        *(f"com{index}" for index in range(1, 10)),
        *(f"lpt{index}" for index in range(1, 10)),
        "com¹",
        "com²",
        "com³",
        "lpt¹",
        "lpt²",
        "lpt³",
    }
)


@dataclass(frozen=True)
class _ValidatedArchiveMember:
    relative_path: str
    kind: Literal["file", "directory"]
    size_bytes: int | None


def _windows_component_key(component: str) -> str:
    normalized = unicodedata.normalize("NFKC", component)
    if (
        not normalized
        or normalized in {".", ".."}
        or normalized != normalized.strip()
        or normalized.endswith((".", " "))
        or any(ord(character) < 32 or ord(character) == 127 for character in normalized)
        or any(character in _WINDOWS_FORBIDDEN for character in normalized)
    ):
        raise IgnBdTopoArchiveError(
            "IGN archive contains a Windows-unsafe path component"
        )
    reserved_stem = normalized.split(".", maxsplit=1)[0].casefold()
    if reserved_stem in _WINDOWS_RESERVED:
        raise IgnBdTopoArchiveError(
            "IGN archive contains a reserved Windows device name"
        )
    return normalized.casefold()


def _validate_archive_members(
    archive: py7zr.SevenZipFile,
) -> tuple[_ValidatedArchiveMember, ...]:
    try:
        if archive.needs_password():
            raise IgnBdTopoArchiveError("IGN archive must not be encrypted")
        infos = archive.list()
    except IgnBdTopoArchiveError:
        raise
    except Exception as error:
        raise IgnBdTopoArchiveError(
            "IGN archive member inventory is unreadable"
        ) from error
    if not infos:
        raise IgnBdTopoArchiveError("IGN archive contains no members")

    raw_names: set[str] = set()
    explicit_destinations: dict[tuple[str, ...], str] = {}
    destinations: dict[tuple[str, ...], _ValidatedArchiveMember] = {}
    for info in infos:
        name = info.filename
        if type(name) is not str or not name or "\x00" in name:
            raise IgnBdTopoArchiveError("IGN archive contains an invalid member name")
        if name in raw_names:
            raise IgnBdTopoArchiveError(
                "IGN archive contains a duplicate raw member name"
            )
        raw_names.add(name)
        normalized_name = name.replace("\\", "/")
        is_directory = bool(info.is_directory)
        if is_directory:
            normalized_name = normalized_name.rstrip("/")
        raw_parts = normalized_name.split("/")
        posix_path = PurePosixPath(normalized_name)
        windows_path = PureWindowsPath(name)
        if (
            not normalized_name
            or any(part in {"", ".", ".."} for part in raw_parts)
            or posix_path.is_absolute()
            or windows_path.is_absolute()
            or bool(windows_path.drive)
        ):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsafe member path: {name}"
            )
        if bool(getattr(info, "is_symlink", False)) or bool(
            getattr(info, "encrypted", False)
        ):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsupported link or encrypted member: {name}"
            )
        is_file = bool(info.is_file)
        if not (is_file ^ is_directory):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsupported special member: {name}"
            )

        key = tuple(_windows_component_key(part) for part in raw_parts)
        if key in explicit_destinations:
            raise IgnBdTopoArchiveError(
                "IGN archive contains a case-insensitive or Unicode destination collision"
            )
        explicit_destinations[key] = name
        kind: Literal["file", "directory"] = "directory" if is_directory else "file"
        for depth in range(1, len(key)):
            parent_key = key[:depth]
            parent_path = "/".join(raw_parts[:depth])
            parent = destinations.get(parent_key)
            if parent is not None and parent.kind == "file":
                raise IgnBdTopoArchiveError(
                    "IGN archive contains a parent-file destination conflict"
                )
            destinations.setdefault(
                parent_key,
                _ValidatedArchiveMember(parent_path, "directory", None),
            )
        existing = destinations.get(key)
        if existing is not None and existing.kind != kind:
            raise IgnBdTopoArchiveError(
                "IGN archive contains a file/directory destination conflict"
            )
        if kind == "file" and any(
            len(other_key) > len(key) and other_key[: len(key)] == key
            for other_key in destinations
        ):
            raise IgnBdTopoArchiveError(
                "IGN archive contains a parent-file destination conflict"
            )
        raw_size = getattr(info, "uncompressed", None)
        if kind == "file" and (type(raw_size) is not int or raw_size < 0):
            raise IgnBdTopoArchiveError(
                "IGN archive contains an invalid file-size inventory"
            )
        destinations[key] = _ValidatedArchiveMember(
            "/".join(raw_parts),
            kind,
            raw_size if kind == "file" else None,
        )

    files = [entry for entry in destinations.values() if entry.kind == "file"]
    geopackages = [
        entry
        for entry in files
        if PurePosixPath(entry.relative_path).suffix.casefold() == ".gpkg"
    ]
    if len(geopackages) != 1:
        raise IgnBdTopoArchiveError(
            "Expected exactly one GeoPackage in the IGN archive inventory"
        )
    return tuple(
        sorted(
            destinations.values(),
            key=lambda entry: (
                unicodedata.normalize("NFKC", entry.relative_path).casefold(),
                entry.relative_path,
            ),
        )
    )


def discover_ign_bdtopo_geopackage(root: Path) -> Path:
    """Return the sole GeoPackage below an extracted package root."""

    if root.is_file():
        if root.suffix.casefold() == ".gpkg":
            return root
        raise IgnBdTopoArchiveError(f"Expected a GeoPackage, got: {root}")
    if not root.is_dir():
        raise IgnBdTopoArchiveError(f"Extraction directory does not exist: {root}")
    geopackages = sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix.casefold() == ".gpkg"
        ),
        key=lambda path: path.as_posix().casefold(),
    )
    if len(geopackages) != 1:
        raise IgnBdTopoArchiveError(
            "Expected exactly one GeoPackage in the IGN package, found "
            f"{len(geopackages)}"
        )
    return geopackages[0]


def list_ign_bdtopo_layers(geopackage_path: Path) -> tuple[str, ...]:
    """List every real layer name exposed by an IGN GeoPackage."""

    if not geopackage_path.is_file():
        raise IgnBdTopoLayerError(f"GeoPackage does not exist: {geopackage_path}")
    try:
        listed = pyogrio.list_layers(geopackage_path)
        names = tuple(str(row[0]) for row in listed)
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"Cannot list layers in GeoPackage: {geopackage_path}"
        ) from error
    if not names or any(not name.strip() for name in names):
        raise IgnBdTopoLayerError("GeoPackage exposes no valid layer names")
    if len(set(names)) != len(names):
        raise IgnBdTopoLayerError("GeoPackage exposes duplicate layer names")
    return names


def _matching_layers(
    layer_names: tuple[str, ...], logical_config: IgnBdTopoLogicalLayerConfig
) -> tuple[str, ...]:
    token_words: set[str] = set()
    for token in logical_config.match_tokens:
        token_words.update(_normalize_words(token).split())
    matches = []
    for layer_name in layer_names:
        layer_words = set(_normalize_words(layer_name).split())
        if token_words.issubset(layer_words):
            matches.append(layer_name)
    return tuple(matches)


def discover_ign_bdtopo_layers(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoLayerSelection:
    """Resolve both configured logical classes without assuming exact casing."""

    config = _validated_source_config(config, error_type=IgnBdTopoLayerError)
    layer_names = list_ign_bdtopo_layers(geopackage_path)
    electric_matches = _matching_layers(
        layer_names, config.logical_layers.electric_lines
    )
    post_matches = _matching_layers(
        layer_names, config.logical_layers.transformation_posts
    )
    if len(electric_matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous electric-line layer for "
            f"'{config.logical_layers.electric_lines.class_label}', found "
            f"{len(electric_matches)}: {electric_matches}"
        )
    if len(post_matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous transformation-post layer for "
            f"'{config.logical_layers.transformation_posts.class_label}', found "
            f"{len(post_matches)}: {post_matches}"
        )
    if electric_matches[0] == post_matches[0]:
        raise IgnBdTopoLayerError(
            "Electric-line and transformation-post discovery selected the same layer"
        )
    return IgnBdTopoLayerSelection(
        all_layer_names=layer_names,
        electric_lines_layer=electric_matches[0],
        transformation_posts_layer=post_matches[0],
    )


def _discover_department_coverage_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
    matches = _matching_layers(layer_names, config.coverage.department_layer)
    if len(matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous department coverage layer for "
            f"'{config.coverage.department_layer.class_label}', found "
            f"{len(matches)}: {matches}"
        )
    return matches[0]


def _discover_road_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
    matches = _matching_layers(layer_names, config.access.road_segments)
    if len(matches) != 1:
        raise IgnBdTopoLayerError(
            "Expected one unambiguous road-segment layer for "
            f"'{config.access.road_segments.class_label}', found "
            f"{len(matches)}: {matches}"
        )
    return matches[0]


@dataclass(frozen=True)
class _ConfiguredPhysicalRoles:
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    road_segments_layer: str
    department_layer: str


def _discover_configured_physical_roles(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> _ConfiguredPhysicalRoles:
    electricity = discover_ign_bdtopo_layers(geopackage_path, config)
    road = _discover_road_layer(electricity.all_layer_names, config)
    department = _discover_department_coverage_layer(
        electricity.all_layer_names,
        config,
    )
    selected = (
        electricity.electric_lines_layer,
        electricity.transformation_posts_layer,
        road,
        department,
    )
    if len(set(selected)) != len(selected):
        raise IgnBdTopoLayerError(
            "IGN electric-line, transformation-post, road, and department roles "
            "must use four distinct physical layers"
        )
    return _ConfiguredPhysicalRoles(
        all_layer_names=electricity.all_layer_names,
        electric_lines_layer=electricity.electric_lines_layer,
        transformation_posts_layer=electricity.transformation_posts_layer,
        road_segments_layer=road,
        department_layer=department,
    )


def _safe_relative_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except (OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"Extracted GeoPackage escapes its extraction root: {path}"
        ) from error


def _resolve_relative_path(root: Path, relative_path: str) -> Path:
    posix_path = PurePosixPath(relative_path)
    windows_path = PureWindowsPath(relative_path)
    if (
        not relative_path
        or posix_path.is_absolute()
        or windows_path.is_absolute()
        or bool(windows_path.drive)
        or ".." in posix_path.parts
    ):
        raise IgnBdTopoArchiveError(
            "Cached extraction metadata contains an unsafe GeoPackage path"
        )
    candidate = root.joinpath(*posix_path.parts)
    try:
        candidate.resolve().relative_to(root.resolve())
    except (OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            "Cached GeoPackage path escapes its extraction root"
        ) from error
    return candidate


def _geopackage_integrity(path: Path) -> tuple[int, str]:
    if not path.is_file():
        raise IgnBdTopoArchiveError(f"IGN GeoPackage does not exist: {path}")
    try:
        size_bytes = path.stat().st_size
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot inspect IGN GeoPackage: {path}") from error
    if size_bytes <= 0:
        raise IgnBdTopoArchiveError(f"IGN GeoPackage is empty: {path}")
    digest = sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
                digest.update(chunk)
    except OSError as error:
        raise IgnBdTopoArchiveError(f"Cannot read IGN GeoPackage: {path}") from error
    return size_bytes, digest.hexdigest()


def _regular_file_sha256(path: Path) -> str:
    digest = sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
                digest.update(chunk)
    except OSError as error:
        raise IgnBdTopoArchiveError(
            f"Cannot hash extracted IGN file: {path}"
        ) from error
    return digest.hexdigest()


def _inventory_extracted_tree(
    root: Path,
    *,
    exclude_relative_path: str | None = None,
) -> tuple[_ExtractedEntryMetadata, ...]:
    try:
        if root.is_symlink() or root.is_junction() or not root.is_dir():
            raise IgnBdTopoArchiveError(
                "IGN extraction root must be a regular non-linked directory"
            )
        entries: list[_ExtractedEntryMetadata] = []
        for current_root, directory_names, file_names in os.walk(
            root,
            topdown=True,
            followlinks=False,
        ):
            current = Path(current_root)
            for name in sorted(directory_names):
                path = current / name
                if path.is_symlink() or path.is_junction() or not path.is_dir():
                    raise IgnBdTopoArchiveError(
                        "IGN extraction contains a link, junction, or special directory"
                    )
                relative = path.relative_to(root).as_posix()
                entries.append(
                    _ExtractedEntryMetadata(
                        relative_path=relative,
                        kind="directory",
                    )
                )
            for name in sorted(file_names):
                path = current / name
                relative = path.relative_to(root).as_posix()
                if relative == exclude_relative_path:
                    continue
                if path.is_symlink() or path.is_junction() or not path.is_file():
                    raise IgnBdTopoArchiveError(
                        "IGN extraction contains a link, junction, or special file"
                    )
                size = path.stat().st_size
                entries.append(
                    _ExtractedEntryMetadata(
                        relative_path=relative,
                        kind="file",
                        size_bytes=size,
                        sha256=_regular_file_sha256(path),
                    )
                )
        return tuple(
            sorted(
                entries,
                key=lambda entry: (
                    unicodedata.normalize("NFKC", entry.relative_path).casefold(),
                    entry.relative_path,
                ),
            )
        )
    except IgnBdTopoArchiveError:
        raise
    except OSError as error:
        raise IgnBdTopoArchiveError(
            "IGN extracted inventory cannot be inspected safely"
        ) from error


def _validate_extracted_inventory(
    root: Path,
    expected: tuple[_ValidatedArchiveMember, ...],
) -> tuple[_ExtractedEntryMetadata, ...]:
    actual = _inventory_extracted_tree(root)
    actual_facts = {
        entry.relative_path: (entry.kind, entry.size_bytes) for entry in actual
    }
    expected_facts = {
        entry.relative_path: (entry.kind, entry.size_bytes) for entry in expected
    }
    if actual_facts != expected_facts:
        raise IgnBdTopoArchiveError(
            "IGN extracted destination inventory differs from the validated archive"
        )
    return actual


@dataclass(frozen=True)
class _VerifiedIgnExtraction:
    extraction: IgnBdTopoExtraction
    metadata: _ExtractionMetadata
    geopackage_path: Path


def _valid_layer_inventory(value: object) -> bool:
    return (
        type(value) is tuple
        and bool(value)
        and all(
            isinstance(name, str) and bool(name) and name == name.strip()
            for name in value
        )
        and len(set(value)) == len(value)
    )


def _validate_extraction_envelope(
    extraction: object,
) -> _VerifiedIgnExtraction:
    """Bind one extraction envelope to its schema-v3 marker and current GPKG."""

    try:
        if type(extraction) is not IgnBdTopoExtraction:
            raise TypeError("IGN extraction must be an exact IgnBdTopoExtraction")
        if type(extraction.archive) is not IgnBdTopoDownload:
            raise TypeError("IGN extraction archive type is invalid")
        if extraction.spatial_role != SPATIAL_ROLE or (
            extraction.archive.spatial_role != SPATIAL_ROLE
        ):
            raise ValueError("IGN extraction lineage must be PROXY_GEOMETRY")
        if (
            not isinstance(extraction.archive.sha256, str)
            or re.fullmatch(r"[0-9a-f]{64}", extraction.archive.sha256) is None
        ):
            raise ValueError("IGN archive SHA256 lineage is invalid")
        if (
            type(extraction.geopackage_size_bytes) is not int
            or extraction.geopackage_size_bytes <= 0
        ):
            raise ValueError("IGN extraction GeoPackage size is invalid")
        if (
            not isinstance(extraction.geopackage_sha256, str)
            or re.fullmatch(r"[0-9a-f]{64}", extraction.geopackage_sha256) is None
        ):
            raise ValueError("IGN extraction GeoPackage SHA256 is invalid")
        if not isinstance(extraction.extraction_path, Path) or not isinstance(
            extraction.geopackage_path, Path
        ):
            raise TypeError("IGN extraction paths are invalid")
        marker_path = extraction.extraction_path / ".landscout-extraction.json"
        if (
            marker_path.is_symlink()
            or marker_path.is_junction()
            or not marker_path.is_file()
        ):
            raise ValueError("IGN schema-v3 extraction metadata is missing")
        metadata = _ExtractionMetadata.model_validate(
            loads_strict_json_object(marker_path.read_bytes())
        )
        expected_path = _resolve_relative_path(
            extraction.extraction_path,
            metadata.geopackage_relative_path,
        )
        discovered_path = discover_ign_bdtopo_geopackage(extraction.extraction_path)
        if (
            expected_path.resolve() != discovered_path.resolve()
            or extraction.geopackage_path.resolve() != discovered_path.resolve()
            or extraction.geopackage_filename != discovered_path.name
        ):
            raise ValueError("IGN extraction GeoPackage path is inconsistent")
        if metadata.archive_sha256 != extraction.archive.sha256:
            raise ValueError("IGN extraction archive lineage differs from metadata")
        if metadata.spatial_role != extraction.spatial_role:
            raise ValueError("IGN extraction spatial role differs from metadata")
        if not _valid_layer_inventory(extraction.all_layer_names):
            raise ValueError("IGN extraction layer inventory is invalid")
        if metadata.all_layer_names != extraction.all_layer_names:
            raise ValueError("IGN extraction layer inventory differs from metadata")
        selected_roles = (
            extraction.electric_lines_layer,
            extraction.transformation_posts_layer,
            extraction.road_segments_layer,
            extraction.department_layer,
        )
        if selected_roles != (
            metadata.electric_lines_layer,
            metadata.transformation_posts_layer,
            metadata.road_segments_layer,
            metadata.department_layer,
        ):
            raise ValueError("IGN extraction physical roles differ from metadata")
        if len(set(selected_roles)) != 4 or any(
            role not in extraction.all_layer_names for role in selected_roles
        ):
            raise ValueError("IGN extraction physical roles are invalid")
        if (
            metadata.geopackage_size_bytes != extraction.geopackage_size_bytes
            or metadata.geopackage_sha256 != extraction.geopackage_sha256
        ):
            raise ValueError(
                "IGN extraction GeoPackage integrity differs from metadata"
            )
        current_size, current_sha = _geopackage_integrity(discovered_path)
        if (
            current_size != extraction.geopackage_size_bytes
            or current_sha != extraction.geopackage_sha256
        ):
            raise ValueError("IGN physical GeoPackage integrity changed")
        current_layers = list_ign_bdtopo_layers(discovered_path)
        if current_layers != extraction.all_layer_names:
            raise ValueError("IGN physical GeoPackage layer inventory changed")
        current_entries = _inventory_extracted_tree(
            extraction.extraction_path,
            exclude_relative_path=".landscout-extraction.json",
        )
        if current_entries != metadata.extracted_entries:
            raise ValueError("IGN complete extracted-file inventory changed")
        return _VerifiedIgnExtraction(
            extraction=extraction,
            metadata=metadata,
            geopackage_path=discovered_path,
        )
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN extraction physical integrity changed or is invalid"
        ) from error


def _verify_unchanged_extraction(context: _VerifiedIgnExtraction) -> None:
    size, digest = _geopackage_integrity(context.geopackage_path)
    if (
        size != context.extraction.geopackage_size_bytes
        or digest != context.extraction.geopackage_sha256
        or list_ign_bdtopo_layers(context.geopackage_path)
        != context.extraction.all_layer_names
        or _inventory_extracted_tree(
            context.extraction.extraction_path,
            exclude_relative_path=".landscout-extraction.json",
        )
        != context.metadata.extracted_entries
    ):
        raise IgnBdTopoLayerError(
            "IGN physical GeoPackage changed during source layer loading"
        )


def _read_layer_frame(geopackage_path: Path, layer_name: str) -> gpd.GeoDataFrame:
    if (
        not isinstance(layer_name, str)
        or not layer_name
        or layer_name != layer_name.strip()
    ):
        raise IgnBdTopoLayerError("IGN source layer name must be an exact string")
    try:
        frame = gpd.read_file(
            geopackage_path,
            layer=layer_name,
            engine="pyogrio",
        )
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"Cannot load IGN GeoPackage layer: {layer_name}"
        ) from error
    if not isinstance(frame, gpd.GeoDataFrame):
        raise IgnBdTopoLayerError(f"IGN layer is not spatial: {layer_name}")
    return frame


def _read_verified_layer_frames(
    context: _VerifiedIgnExtraction,
    layer_names: tuple[str, ...],
) -> tuple[gpd.GeoDataFrame, ...]:
    if type(layer_names) is not tuple or not layer_names:
        raise IgnBdTopoLayerError("IGN verified layer batch must be a non-empty tuple")
    if len(set(layer_names)) != len(layer_names) or any(
        layer not in context.extraction.all_layer_names for layer in layer_names
    ):
        raise IgnBdTopoLayerError("IGN verified layer batch is invalid")
    frames = tuple(
        _read_layer_frame(context.geopackage_path, layer_name)
        for layer_name in layer_names
    )
    _verify_unchanged_extraction(context)
    return frames


def _validate_layer_summary_contract(summary: object) -> IgnBdTopoLayerSummary:
    if type(summary) is not IgnBdTopoLayerSummary:
        raise IgnBdTopoLayerError("IGN layer summary type is invalid")
    for name in (
        "feature_count",
        "null_geometry_count",
        "empty_geometry_count",
        "invalid_geometry_count",
    ):
        value = getattr(summary, name)
        if type(value) is not int or value < 0:
            raise IgnBdTopoLayerError(
                f"IGN layer summary {name} must be a strict non-negative integer"
            )
    if (
        type(summary.columns) is not tuple
        or not summary.columns
        or any(
            not isinstance(column, str) or not column or column != column.strip()
            for column in summary.columns
        )
        or len(set(summary.columns)) != len(summary.columns)
    ):
        raise IgnBdTopoLayerError("IGN layer summary columns are invalid")
    if (
        type(summary.dtypes) is not tuple
        or len(summary.dtypes) != len(summary.columns)
        or any(
            type(item) is not tuple
            or len(item) != 2
            or any(not isinstance(value, str) or not value for value in item)
            for item in summary.dtypes
        )
        or tuple(column for column, _ in summary.dtypes) != summary.columns
    ):
        raise IgnBdTopoLayerError("IGN layer summary dtypes are invalid")
    if (
        type(summary.geometry_types) is not tuple
        or any(
            not isinstance(value, str) or not value or value != value.strip()
            for value in summary.geometry_types
        )
        or summary.geometry_types != tuple(sorted(set(summary.geometry_types)))
    ):
        raise IgnBdTopoLayerError("IGN layer summary geometry types are invalid")
    if summary.spatial_role != SPATIAL_ROLE:
        raise IgnBdTopoLayerError("IGN layer summary spatial role is invalid")
    if any(
        getattr(summary, name) > summary.feature_count
        for name in (
            "null_geometry_count",
            "empty_geometry_count",
            "invalid_geometry_count",
        )
    ):
        raise IgnBdTopoLayerError("IGN layer summary geometry count is impossible")
    return summary


def _compare_layer_summary(
    supplied: object,
    expected: IgnBdTopoLayerSummary,
) -> None:
    validated = _validate_layer_summary_contract(supplied)
    if validated != expected:
        raise IgnBdTopoLayerError(
            "IGN supplied layer summary differs from physical source"
        )


def _compare_loaded_frame(
    supplied: object,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
    try:
        if not isinstance(supplied, gpd.GeoDataFrame):
            raise TypeError("supplied layer is not a GeoDataFrame")
        if tuple(supplied.columns) != tuple(expected.columns):
            raise AssertionError("columns differ")
        if tuple(str(dtype) for dtype in supplied.dtypes) != tuple(
            str(dtype) for dtype in expected.dtypes
        ):
            raise AssertionError("dtypes differ")
        if type(supplied.index) is not type(expected.index):
            raise AssertionError("index type differs")
        if supplied.index.names != expected.index.names or not supplied.index.equals(
            expected.index
        ):
            raise AssertionError("index differs")
        if supplied.active_geometry_name != expected.active_geometry_name:
            raise AssertionError("active geometry differs")
        supplied_crs = _validate_lambert93(supplied.crs, label)
        expected_crs = _validate_lambert93(expected.crs, label)
        if not supplied_crs.equals(expected_crs):
            raise AssertionError("CRS differs")
        geometry_name = expected.active_geometry_name
        if geometry_name is None:
            raise AssertionError("geometry is missing")
        pd.testing.assert_frame_equal(
            pd.DataFrame(supplied.drop(columns=geometry_name)),
            pd.DataFrame(expected.drop(columns=geometry_name)),
            check_dtype=True,
            check_index_type=True,
            check_column_type=True,
            check_names=True,
            check_exact=True,
        )
        if (
            supplied.geometry.to_wkb(hex=True).tolist()
            != expected.geometry.to_wkb(hex=True).tolist()
        ):
            raise AssertionError("geometry WKB differs")
        if supplied.attrs != expected.attrs:
            raise AssertionError("frame attributes differ")
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"IGN supplied {label} differs from freshly read physical source"
        ) from error


def _load_cached_extraction(
    extraction_path: Path,
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoExtraction | None:
    metadata_path = extraction_path / ".landscout-extraction.json"
    if not extraction_path.is_dir() or not metadata_path.is_file():
        return None
    try:
        if metadata_path.is_symlink() or metadata_path.is_junction():
            return None
        metadata = _ExtractionMetadata.model_validate(
            loads_strict_json_object(metadata_path.read_bytes())
        )
        if (
            metadata.archive_sha256 != download.sha256
            or metadata.spatial_role != SPATIAL_ROLE
        ):
            return None
        geopackage_path = _resolve_relative_path(
            extraction_path, metadata.geopackage_relative_path
        )
        discovered_path = discover_ign_bdtopo_geopackage(extraction_path)
        if geopackage_path.resolve() != discovered_path.resolve():
            return None
        geopackage_size, geopackage_sha256 = _geopackage_integrity(geopackage_path)
        if (
            geopackage_size != metadata.geopackage_size_bytes
            or geopackage_sha256 != metadata.geopackage_sha256
        ):
            return None
        if (
            _inventory_extracted_tree(
                extraction_path,
                exclude_relative_path=".landscout-extraction.json",
            )
            != metadata.extracted_entries
        ):
            return None
        selection = _discover_configured_physical_roles(geopackage_path, config)
        if (
            selection.all_layer_names != metadata.all_layer_names
            or selection.electric_lines_layer != metadata.electric_lines_layer
            or selection.transformation_posts_layer
            != metadata.transformation_posts_layer
            or selection.road_segments_layer != metadata.road_segments_layer
            or selection.department_layer != metadata.department_layer
        ):
            return None
        return IgnBdTopoExtraction(
            archive=download,
            extraction_path=extraction_path,
            geopackage_path=geopackage_path,
            geopackage_filename=geopackage_path.name,
            geopackage_size_bytes=metadata.geopackage_size_bytes,
            geopackage_sha256=metadata.geopackage_sha256,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            road_segments_layer=selection.road_segments_layer,
            department_layer=selection.department_layer,
            cache_hit=True,
        )
    except (
        IgnBdTopoArchiveError,
        IgnBdTopoLayerError,
        OSError,
        ValidationError,
        ValueError,
    ):
        return None


def _replace_directory(source: Path, target: Path) -> None:
    source.replace(target)


def _path_exists_or_is_link(path: Path) -> bool:
    try:
        return path.exists() or path.is_symlink() or path.is_junction()
    except OSError:
        return True


def _remove_validated_extraction_directory(path: Path) -> None:
    if not _path_exists_or_is_link(path):
        return
    if path.is_symlink() or path.is_junction() or not path.is_dir():
        raise IgnBdTopoArchiveError(
            "IGN extraction transaction path is not a safe ordinary directory"
        )
    _inventory_extracted_tree(path)
    try:
        shutil.rmtree(path)
    except OSError as error:
        raise IgnBdTopoArchiveError(
            "IGN extraction transaction directory could not be removed safely"
        ) from error


def _require_no_extraction_backup(extraction_path: Path) -> None:
    backup_path = extraction_path.with_name(f"{extraction_path.name}.bak")
    if _path_exists_or_is_link(backup_path):
        raise IgnBdTopoArchiveError(
            "IGN extraction recovery backup exists; manual recovery is required"
        )


def _require_safe_existing_extraction_marker(extraction_path: Path) -> None:
    marker_path = extraction_path / ".landscout-extraction.json"
    if not _path_exists_or_is_link(marker_path):
        return
    try:
        if (
            marker_path.is_symlink()
            or marker_path.is_junction()
            or not marker_path.is_file()
        ):
            raise IgnBdTopoArchiveError(
                "IGN extraction integrity marker is not a regular non-linked file"
            )
    except IgnBdTopoArchiveError:
        raise
    except OSError as error:
        raise IgnBdTopoArchiveError(
            "IGN extraction integrity marker cannot be inspected safely"
        ) from error


def _prepare_temporary_extraction_directory(path: Path) -> None:
    if _path_exists_or_is_link(path):
        _remove_validated_extraction_directory(path)
    try:
        path.mkdir(parents=False)
    except OSError as error:
        raise IgnBdTopoArchiveError(
            "IGN temporary extraction directory cannot be created safely"
        ) from error


def _publish_extraction_directory(temporary_path: Path, extraction_path: Path) -> None:
    backup_path = extraction_path.with_name(f"{extraction_path.name}.bak")
    _require_no_extraction_backup(extraction_path)
    extraction_existed = _path_exists_or_is_link(extraction_path)
    if extraction_existed:
        if (
            extraction_path.is_symlink()
            or extraction_path.is_junction()
            or not extraction_path.is_dir()
        ):
            raise IgnBdTopoArchiveError(
                "IGN existing extraction target is not a safe ordinary directory"
            )
        _inventory_extracted_tree(extraction_path)
    if extraction_existed:
        _replace_directory(extraction_path, backup_path)
    try:
        _replace_directory(temporary_path, extraction_path)
    except OSError:
        try:
            if extraction_existed:
                if _path_exists_or_is_link(extraction_path):
                    _remove_validated_extraction_directory(extraction_path)
                _replace_directory(backup_path, extraction_path)
        except (IgnBdTopoArchiveError, OSError) as rollback_error:
            raise IgnBdTopoArchiveError(
                "IGN extraction publication and rollback both failed"
            ) from rollback_error
        raise
    else:
        if extraction_existed:
            _remove_validated_extraction_directory(backup_path)


def extract_ign_bdtopo_archive(
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
    extraction_dir: Path | None = None,
) -> IgnBdTopoExtraction:
    """Safely extract the package and resolve its required electricity layers."""

    config = _validated_source_config(config, error_type=IgnBdTopoArchiveError)
    try:
        _validate_archive_config_lineage(download, config)
    except IgnBdTopoLayerError as error:
        raise IgnBdTopoArchiveError(
            "IGN download envelope differs from source config"
        ) from error
    extraction_path = extraction_dir or (
        download.path.parent / "x" / download.sha256[:16]
    )
    if not isinstance(extraction_path, Path):
        raise IgnBdTopoArchiveError("IGN extraction target must be a pathlib.Path")
    _require_no_extraction_backup(extraction_path)
    if _path_exists_or_is_link(extraction_path) and (
        extraction_path.is_symlink()
        or extraction_path.is_junction()
        or not extraction_path.is_dir()
    ):
        raise IgnBdTopoArchiveError(
            f"IGN extraction target exists and is not a directory: {extraction_path}"
        )
    _require_safe_existing_extraction_marker(extraction_path)
    integrity = validate_ign_bdtopo_archive(download.path, config)
    if (
        integrity.file_size != download.file_size
        or integrity.sha256 != download.sha256
        or integrity.official_checksum_algorithm != download.official_checksum_algorithm
        or integrity.official_checksum != download.official_checksum
        or integrity.official_checksum_validated != download.official_checksum_validated
    ):
        raise IgnBdTopoArchiveError(
            "Downloaded IGN archive integrity changed before extraction"
        )
    cached = _load_cached_extraction(extraction_path, download, config)
    if cached is not None:
        return cached

    extraction_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = extraction_path.with_name(f"{extraction_path.name}.part")
    _prepare_temporary_extraction_directory(temporary_path)
    try:
        with py7zr.SevenZipFile(download.path, mode="r") as archive:
            expected_entries = _validate_archive_members(archive)
            archive.extractall(path=temporary_path)

        extracted_entries = _validate_extracted_inventory(
            temporary_path,
            expected_entries,
        )
        geopackage_path = discover_ign_bdtopo_geopackage(temporary_path)
        selection = _discover_configured_physical_roles(geopackage_path, config)
        relative_path = _safe_relative_path(geopackage_path, temporary_path)
        geopackage_size, geopackage_sha256 = _geopackage_integrity(geopackage_path)
        metadata = _ExtractionMetadata(
            schema_version=3,
            archive_sha256=download.sha256,
            geopackage_relative_path=relative_path,
            geopackage_size_bytes=geopackage_size,
            geopackage_sha256=geopackage_sha256,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            road_segments_layer=selection.road_segments_layer,
            department_layer=selection.department_layer,
            extracted_entries=extracted_entries,
            spatial_role="PROXY_GEOMETRY",
        )
        with (temporary_path / ".landscout-extraction.json").open(
            "x", encoding="utf-8"
        ) as output:
            output.write(metadata.model_dump_json(indent=2) + "\n")
        _publish_extraction_directory(temporary_path, extraction_path)
        published_geopackage = _resolve_relative_path(extraction_path, relative_path)
        return IgnBdTopoExtraction(
            archive=download,
            extraction_path=extraction_path,
            geopackage_path=published_geopackage,
            geopackage_filename=published_geopackage.name,
            geopackage_size_bytes=metadata.geopackage_size_bytes,
            geopackage_sha256=metadata.geopackage_sha256,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            road_segments_layer=selection.road_segments_layer,
            department_layer=selection.department_layer,
            cache_hit=False,
        )
    except (ArchiveError, EOFError, OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"IGN archive extraction failed: {download.path}"
        ) from error
    finally:
        primary_error = sys.exception()
        try:
            _remove_validated_extraction_directory(temporary_path)
        except IgnBdTopoArchiveError:
            if primary_error is None:
                raise


def _validate_lambert93(crs_value: Any, layer_name: str) -> CRS:
    if crs_value is None:
        raise IgnBdTopoLayerError(f"IGN layer has no CRS: {layer_name}")
    try:
        crs = CRS.from_user_input(crs_value)
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"IGN layer has an unreadable CRS: {layer_name}"
        ) from error
    if not crs.is_projected:
        raise IgnBdTopoLayerError(
            f"IGN layer CRS must be projected: {layer_name} ({crs.to_string()})"
        )
    expected = CRS.from_epsg(2154)
    if not crs.equals(expected):
        raise IgnBdTopoLayerError(
            "IGN layer CRS is not Lambert-93 / EPSG:2154 compatible: "
            f"{layer_name} ({crs.to_string()})"
        )
    return crs


def _loaded_layer_from_frame(
    frame: gpd.GeoDataFrame,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
    try:
        geometry_name = frame.geometry.name
    except (AttributeError, ValueError) as error:
        raise IgnBdTopoLayerError(
            f"IGN layer has no active geometry column: {layer_name}"
        ) from error
    if geometry_name not in frame.columns:
        raise IgnBdTopoLayerError(f"IGN layer geometry column is missing: {layer_name}")
    crs = _validate_lambert93(frame.crs, layer_name)
    if frame.empty:
        raise IgnBdTopoLayerError(f"IGN layer contains no features: {layer_name}")

    geometry = frame.geometry
    null_mask = geometry.isna()
    non_null_mask = ~null_mask
    empty_mask = non_null_mask & geometry.is_empty
    measurable_mask = non_null_mask & ~geometry.is_empty
    invalid_mask = measurable_mask & ~geometry.is_valid
    geometry_types = tuple(
        sorted(
            str(value) for value in geometry[non_null_mask].geom_type.dropna().unique()
        )
    )
    summary = IgnBdTopoLayerSummary(
        logical_name=logical_name,
        source_layer_name=layer_name,
        crs=crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
    )
    _validate_layer_summary_contract(summary)
    return IgnBdTopoLoadedLayer(data=frame, summary=summary)


def _load_untrusted_ign_bdtopo_layer(
    geopackage_path: Path,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
    """Inspect one raw layer without conferring config-bound source authority."""

    if not geopackage_path.is_file():
        raise IgnBdTopoLayerError(f"GeoPackage does not exist: {geopackage_path}")
    if not layer_name.strip():
        raise IgnBdTopoLayerError("IGN source layer name must not be empty")
    frame = _read_layer_frame(geopackage_path, layer_name)
    return _loaded_layer_from_frame(frame, layer_name, logical_name)


def _validated_layer_source_config(config: object) -> IgnBdTopoSourceConfig:
    return _validated_source_config(config, error_type=IgnBdTopoLayerError)


def _validate_archive_config_lineage(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> None:
    try:
        if type(source) is IgnBdTopoExtraction:
            archive = source.archive
        elif type(source) is IgnBdTopoDownload:
            archive = source
        else:
            raise TypeError("IGN archive source type is invalid")
        if type(archive) is not IgnBdTopoDownload:
            raise TypeError("IGN archive type is invalid")
        if type(archive.file_size) is not int or archive.file_size <= 0:
            raise TypeError("IGN archive size is invalid")
        if type(archive.official_checksum_validated) is not bool:
            raise TypeError("IGN official-checksum state is invalid")
        if (
            type(archive.sha256) is not str
            or re.fullmatch(r"[0-9a-f]{64}", archive.sha256) is None
        ):
            raise TypeError("IGN archive SHA256 is invalid")
        if type(archive.download_timestamp) is not str:
            raise TypeError("IGN archive timestamp is invalid")
        downloaded_at = datetime.fromisoformat(archive.download_timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(
            None
        ):
            raise ValueError("IGN archive timestamp must be timezone-aware UTC")
        if not isinstance(archive.path, Path):
            raise TypeError("IGN archive path type is invalid")
        if archive.path.name != archive.filename:
            raise ValueError("IGN archive filename differs from its physical path")
        if type(archive.cache_hit) is not bool:
            raise TypeError("IGN archive cache state is invalid")
        expected_checksum_url = (
            str(config.checksum_url) if config.checksum_url is not None else None
        )
        expected_values: tuple[tuple[object, object], ...] = (
            (archive.provider, config.provider),
            (archive.product, config.product),
            (archive.department_code, config.department_code),
            (archive.edition, config.edition),
            (archive.product_version, config.product_version),
            (archive.projection, config.projection),
            (archive.package_format, config.format),
            (archive.archive_format, config.archive_format),
            (archive.source_url, str(config.source_url)),
            (archive.checksum_url, expected_checksum_url),
            (archive.filename, _archive_filename(config)),
            (
                archive.official_checksum_algorithm,
                config.official_checksum_algorithm,
            ),
            (archive.official_checksum, config.official_checksum),
            (
                archive.official_checksum_validated,
                config.official_checksum is not None,
            ),
            (archive.spatial_role, SPATIAL_ROLE),
        )
        if any(actual != expected for actual, expected in expected_values):
            raise ValueError("IGN archive lineage differs from source config")
        if (
            config.expected_archive_size_bytes is not None
            and archive.file_size != config.expected_archive_size_bytes
        ):
            raise ValueError("IGN archive size differs from source config")
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN archive lineage differs from source config"
        ) from error


def load_ign_bdtopo_electricity(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
    """Load the two electricity layers reproduced from the source config."""

    validated_config = _validated_layer_source_config(config)
    _validate_archive_config_lineage(extraction, validated_config)
    context = _validate_extraction_envelope(extraction)
    configured_selection = _discover_configured_physical_roles(
        context.geopackage_path,
        validated_config,
    )
    if (
        configured_selection.all_layer_names != extraction.all_layer_names
        or configured_selection.electric_lines_layer != extraction.electric_lines_layer
        or configured_selection.transformation_posts_layer
        != extraction.transformation_posts_layer
        or configured_selection.road_segments_layer != extraction.road_segments_layer
        or configured_selection.department_layer != extraction.department_layer
    ):
        raise IgnBdTopoLayerError(
            "IGN electricity roles differ from the configured physical layers"
        )
    line_frame, post_frame = _read_verified_layer_frames(
        context,
        (
            configured_selection.electric_lines_layer,
            configured_selection.transformation_posts_layer,
        ),
    )
    electric_lines = _loaded_layer_from_frame(
        line_frame,
        configured_selection.electric_lines_layer,
        "electric_lines",
    )
    transformation_posts = _loaded_layer_from_frame(
        post_frame,
        configured_selection.transformation_posts_layer,
        "transformation_posts",
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=electric_lines.data,
        transformation_posts=transformation_posts.data,
        electric_lines_summary=electric_lines.summary,
        transformation_posts_summary=transformation_posts.summary,
    )


def load_ign_bdtopo_roads(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
    """Load the configured factual road layer without filtering or repair."""

    validated_config = _validated_layer_source_config(config)
    _validate_archive_config_lineage(extraction, validated_config)
    context = _validate_extraction_envelope(extraction)
    selection = _discover_configured_physical_roles(
        context.geopackage_path,
        validated_config,
    )
    if (
        selection.all_layer_names != extraction.all_layer_names
        or selection.electric_lines_layer != extraction.electric_lines_layer
        or selection.transformation_posts_layer != extraction.transformation_posts_layer
        or selection.road_segments_layer != extraction.road_segments_layer
        or selection.department_layer != extraction.department_layer
    ):
        raise IgnBdTopoLayerError(
            "IGN road role differs from configured physical-layer inventory"
        )
    layer_name = selection.road_segments_layer
    (road_frame,) = _read_verified_layer_frames(context, (layer_name,))
    loaded = _loaded_layer_from_frame(
        road_frame,
        layer_name,
        "road_segments",
    )
    return IgnBdTopoRoadData(
        extraction=extraction,
        road_segments=loaded.data,
        road_segments_summary=loaded.summary,
    )


def _department_coverage_from_frame(
    extraction: IgnBdTopoExtraction,
    frame: gpd.GeoDataFrame,
    layer_name: str,
    department_field: str,
) -> IgnBdTopoDepartmentCoverage:
    archive = extraction.archive
    try:
        geometry_name = frame.geometry.name
    except (AttributeError, ValueError) as error:
        raise IgnBdTopoLayerError(
            f"IGN department coverage layer has no active geometry: {layer_name}"
        ) from error
    if geometry_name not in frame.columns:
        raise IgnBdTopoLayerError(
            f"IGN department coverage geometry column is missing: {layer_name}"
        )
    crs = _validate_lambert93(frame.crs, layer_name)
    if frame.empty:
        raise IgnBdTopoLayerError(
            f"IGN department coverage layer contains no features: {layer_name}"
        )

    geometry = frame.geometry
    null_mask = geometry.isna()
    non_null_mask = ~null_mask
    empty_mask = non_null_mask & geometry.is_empty
    measurable_mask = non_null_mask & ~geometry.is_empty
    invalid_mask = measurable_mask & ~geometry.is_valid
    geometry_types = tuple(
        sorted(
            str(value) for value in geometry[non_null_mask].geom_type.dropna().unique()
        )
    )

    if department_field not in frame.columns:
        raise IgnBdTopoLayerError(
            "Configured department identity field is missing from IGN coverage "
            f"layer: {department_field}"
        )
    selected_mask = frame[department_field].eq(archive.department_code)
    selected_count = int(selected_mask.sum())
    if selected_count != 1:
        raise IgnBdTopoLayerError(
            "Expected exactly one authoritative department coverage feature for "
            f"{archive.department_code}, found {selected_count}"
        )
    selected = frame.loc[selected_mask].reset_index(drop=True).copy()
    selected_geometry = selected.geometry
    if selected_geometry.isna().any():
        raise IgnBdTopoLayerError("Selected department coverage geometry is null")
    if selected_geometry.is_empty.any():
        raise IgnBdTopoLayerError("Selected department coverage geometry is empty")
    if not selected_geometry.is_valid.all():
        raise IgnBdTopoLayerError("Selected department coverage geometry is invalid")
    selected_types = set(selected_geometry.geom_type.dropna())
    if not selected_types <= {"Polygon", "MultiPolygon"}:
        raise IgnBdTopoLayerError(
            "Selected department coverage geometry must be Polygon or MultiPolygon"
        )

    lineage = {
        "source_provider": archive.provider,
        "source_product": archive.product,
        "source_department_code": archive.department_code,
        "source_edition": archive.edition,
        "source_product_version": archive.product_version,
        "source_archive_sha256": archive.sha256,
        "source_layer": layer_name,
        "spatial_role": COVERAGE_SPATIAL_ROLE,
    }
    collisions = set(lineage) & set(selected.columns)
    if collisions:
        raise IgnBdTopoLayerError(
            "IGN department coverage attributes collide with lineage columns: "
            + ", ".join(sorted(collisions))
        )
    for column, value in lineage.items():
        selected[column] = value

    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name=layer_name,
        crs=crs.to_string(),
        source_feature_count=len(frame),
        selected_feature_count=selected_count,
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
        department_code_field=department_field,
        selected_department_code=archive.department_code,
    )
    return IgnBdTopoDepartmentCoverage(
        extraction=extraction,
        coverage=selected,
        summary=summary,
        source_provider=archive.provider,
        source_product=archive.product,
        source_department_code=archive.department_code,
        source_edition=archive.edition,
        source_product_version=archive.product_version,
        source_archive_sha256=archive.sha256,
        source_layer=layer_name,
    )


def load_ign_bdtopo_department_coverage(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
    """Load the one authoritative configured department coverage feature."""

    validated_config = _validated_layer_source_config(config)
    _validate_archive_config_lineage(extraction, validated_config)
    context = _validate_extraction_envelope(extraction)
    selection = _discover_configured_physical_roles(
        context.geopackage_path,
        validated_config,
    )
    if (
        selection.all_layer_names != extraction.all_layer_names
        or selection.electric_lines_layer != extraction.electric_lines_layer
        or selection.transformation_posts_layer != extraction.transformation_posts_layer
        or selection.road_segments_layer != extraction.road_segments_layer
        or selection.department_layer != extraction.department_layer
    ):
        raise IgnBdTopoLayerError(
            "IGN coverage role differs from configured physical-layer inventory"
        )
    layer_name = selection.department_layer
    (frame,) = _read_verified_layer_frames(context, (layer_name,))
    return _department_coverage_from_frame(
        extraction,
        frame,
        layer_name,
        validated_config.coverage.department_layer.department_code_field,
    )


def _revalidate_ign_bdtopo_electricity_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
    """Fresh-read and exact-compare one supplied electricity source bundle."""

    try:
        if type(source) is not IgnBdTopoElectricityData:
            raise TypeError("IGN electricity source type is invalid")
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("IGN electricity source config type is invalid")
        fresh = load_ign_bdtopo_electricity(source.extraction, config)
        _compare_loaded_frame(
            source.electric_lines, fresh.electric_lines, "electric lines"
        )
        _compare_loaded_frame(
            source.transformation_posts,
            fresh.transformation_posts,
            "transformation posts",
        )
        _compare_layer_summary(
            source.electric_lines_summary, fresh.electric_lines_summary
        )
        _compare_layer_summary(
            source.transformation_posts_summary,
            fresh.transformation_posts_summary,
        )
        if source.spatial_role != SPATIAL_ROLE:
            raise ValueError("IGN electricity source spatial role is invalid")
        return fresh
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN electricity source-complete revalidation failed"
        ) from error


def _revalidate_ign_bdtopo_road_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
    """Fresh-read and exact-compare one supplied road source bundle."""

    try:
        if type(source) is not IgnBdTopoRoadData:
            raise TypeError("IGN road source type is invalid")
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("IGN road source config type is invalid")
        fresh = load_ign_bdtopo_roads(source.extraction, config)
        _compare_loaded_frame(
            source.road_segments,
            fresh.road_segments,
            "road segments",
        )
        _compare_layer_summary(
            source.road_segments_summary,
            fresh.road_segments_summary,
        )
        return fresh
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN road source-complete revalidation failed"
        ) from error


def _validate_coverage_summary_contract(
    summary: object,
) -> IgnBdTopoCoverageLayerSummary:
    if type(summary) is not IgnBdTopoCoverageLayerSummary:
        raise IgnBdTopoLayerError("IGN coverage summary type is invalid")
    for name in (
        "source_feature_count",
        "selected_feature_count",
        "null_geometry_count",
        "empty_geometry_count",
        "invalid_geometry_count",
    ):
        value = getattr(summary, name)
        if type(value) is not int or value < 0:
            raise IgnBdTopoLayerError(
                f"IGN coverage summary {name} must be a strict non-negative integer"
            )
    if summary.selected_feature_count > summary.source_feature_count:
        raise IgnBdTopoLayerError("IGN coverage summary counts are inconsistent")
    if (
        type(summary.columns) is not tuple
        or not summary.columns
        or any(
            not isinstance(value, str) or not value or value != value.strip()
            for value in summary.columns
        )
        or len(set(summary.columns)) != len(summary.columns)
    ):
        raise IgnBdTopoLayerError("IGN coverage summary columns are invalid")
    if (
        type(summary.dtypes) is not tuple
        or len(summary.dtypes) != len(summary.columns)
        or any(
            type(item) is not tuple
            or len(item) != 2
            or any(not isinstance(value, str) or not value for value in item)
            for item in summary.dtypes
        )
        or tuple(name for name, _ in summary.dtypes) != summary.columns
    ):
        raise IgnBdTopoLayerError("IGN coverage summary dtypes are invalid")
    if (
        type(summary.geometry_types) is not tuple
        or summary.geometry_types != tuple(sorted(set(summary.geometry_types)))
        or any(
            not isinstance(value, str) or not value for value in summary.geometry_types
        )
    ):
        raise IgnBdTopoLayerError("IGN coverage summary geometry types are invalid")
    if summary.spatial_role != COVERAGE_SPATIAL_ROLE:
        raise IgnBdTopoLayerError("IGN coverage summary spatial role is invalid")
    return summary


def _revalidate_ign_bdtopo_department_coverage(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
    """Fresh-read and exact-compare selected coverage with its physical layer."""

    try:
        if type(source) is not IgnBdTopoDepartmentCoverage:
            raise TypeError("IGN department coverage type is invalid")
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("IGN coverage source config type is invalid")
        fresh = load_ign_bdtopo_department_coverage(source.extraction, config)
        _compare_loaded_frame(source.coverage, fresh.coverage, "department coverage")
        if source.summary != fresh.summary:
            raise ValueError("IGN coverage summary differs from physical source")
        scalar_names = (
            "source_provider",
            "source_product",
            "source_department_code",
            "source_edition",
            "source_product_version",
            "source_archive_sha256",
            "source_layer",
            "spatial_role",
        )
        if any(getattr(source, name) != getattr(fresh, name) for name in scalar_names):
            raise ValueError("IGN coverage lineage differs from physical source")
        return fresh
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN coverage source-complete revalidation failed"
        ) from error
```
