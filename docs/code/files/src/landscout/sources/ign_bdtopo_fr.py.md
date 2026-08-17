# `src/landscout/sources/ign_bdtopo_fr.py`

## File identity

- Repository path: `src/landscout/sources/ign_bdtopo_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: grid/source
- Responsibility: Acquires, verifies, extracts, inventories, selects, loads, and source-completely revalidates IGN BD TOPO layers.
- Source SHA256: `c9c43bb6568e7137ed6c9dd69e2605c419568bb95efbc0132800eb0915253ba5`

## 1. Purpose

Acquires, verifies, extracts, inventories, selects, loads, and source-completely revalidates IGN BD TOPO layers.

## 2. Position in LandScout architecture

This file belongs to the **source adapter** layer and the **grid/source** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
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
- `import yaml`
- `from py7zr.exceptions import ArchiveError`
- `from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
    model_validator,
)`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.common.safe_http import open_safe_https`

## 4. Contract taxonomy

### A. Python constants

#### `DEFAULT_CONFIG_PATH`

```python
DEFAULT_CONFIG_PATH = Path("configs/sources/ign_bdtopo_fr.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `DEFAULT_CACHE_DIR`

```python
DEFAULT_CACHE_DIR = Path("data/cache/ign_bdtopo")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `DOWNLOAD_CHUNK_SIZE`

```python
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/sources/ign_bdtopo_fr.py::_calculate_checksums` (value reference), `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` (value reference), `src/landscout/sources/ign_bdtopo_fr.py::_geopackage_integrity` (value reference).

#### `SPATIAL_ROLE`

```python
SPATIAL_ROLE = "PROXY_GEOMETRY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_download` (value reference), `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` (value reference), `src/landscout/sources/ign_bdtopo_fr.py::_validate_layer_summary_contract` (value reference), `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` (value reference), `src/landscout/sources/ign_bdtopo_fr.py::_validate_archive_config_lineage` (value reference), `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_electricity_data` (value reference).

#### `COVERAGE_SPATIAL_ROLE`

```python
COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/sources/ign_bdtopo_fr.py::_department_coverage_from_frame` (value reference), `src/landscout/sources/ign_bdtopo_fr.py::_validate_coverage_summary_contract` (value reference).


### B. Type aliases and closed domains

#### `SpatialRole`

```python
SpatialRole = Literal["PROXY_GEOMETRY"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoDownload` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoExtraction` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoLayerSummary` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoElectricityData` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::_CacheMetadata` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::_ExtractionMetadata` (type annotation).

#### `CoverageSpatialRole`

```python
CoverageSpatialRole = Literal["SOURCE_COVERAGE_BOUNDARY"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoCoverageLayerSummary` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoDepartmentCoverage` (type annotation).

#### `LogicalLayerName`

```python
LogicalLayerName = Literal[
    "electric_lines",
    "transformation_posts",
    "road_segments",
]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoLayerSummary` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::_loaded_layer_from_frame` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_layer` (type annotation).

#### `Projection`

```python
Projection = Literal["EPSG:2154"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` (type annotation).

#### `PackageFormat`

```python
PackageFormat = Literal["GPKG"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` (type annotation).

#### `ArchiveFormat`

```python
ArchiveFormat = Literal["7z"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` (type annotation).

#### `ChecksumAlgorithm`

```python
ChecksumAlgorithm = Literal["md5", "sha256"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoArchiveIntegrity` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoDownload` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::_CacheMetadata` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::_calculate_checksums` (type annotation).

#### `NonEmptyString`

```python
NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
```

String constrained non-empty after the exact StringConstraints behavior in the declaration. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoLogicalLayerConfig` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoDepartmentLayerConfig` (type annotation), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` (type annotation).

#### `DepartmentCode`

```python
DepartmentCode = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=r"^(?:[0-9]{2}|2A|2B|97[1-6])$",
    ),
]
```

Annotated validation alias whose strictness, regex/bounds, and callbacks are exactly those shown above. Enforced/consumed by `src/landscout/stages/normalize_access_ign.py::<module>` (import), `src/landscout/stages/normalize_grid_ign.py::<module>` (import), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` (type annotation), `src/landscout/stages/normalize_access_ign.py::<module>` (value reference), `src/landscout/stages/normalize_grid_ign.py::<module>` (value reference).

#### `EditionString`

```python
EditionString = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^\d{4}-\d{2}-\d{2}$"),
]
```

Annotated validation alias whose strictness, regex/bounds, and callbacks are exactly those shown above. Enforced/consumed by `src/landscout/stages/normalize_access_ign.py::<module>` (import), `src/landscout/stages/normalize_grid_ign.py::<module>` (import), `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` (type annotation), `src/landscout/stages/normalize_access_ign.py::<module>` (value reference), `src/landscout/stages/normalize_grid_ign.py::<module>` (value reference).

#### `HexChecksum`

```python
HexChecksum = Annotated[
    str,
    StringConstraints(strip_whitespace=True, to_lower=True, pattern=r"^[0-9a-fA-F]+$"),
]
```

Annotated validation alias whose strictness, regex/bounds, and callbacks are exactly those shown above. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` (type annotation).

#### `CanonicalSha256`

```python
CanonicalSha256 = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^[0-9a-f]{64}$"),
]
```

Strict lowercase 64-hex SHA256 string used by Pydantic/source-result validation. Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::_ExtractionMetadata` (type annotation).

#### `StrictPositiveInt`

```python
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
```

Strict integer greater than zero; Boolean and numeric coercions are rejected by Pydantic Field(strict=True, gt=0). Enforced/consumed by `src/landscout/sources/ign_bdtopo_fr.py::_ExtractionMetadata` (type annotation).


### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `IgnBdTopoLogicalLayerConfig`

**Purpose:** Catalogue class label and normalized tokens used for layer discovery.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `class_label` | `class_label: NonEmptyString` | `IgnBdTopoLogicalLayerConfig.class_label` represents the `class_label` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `match_tokens` | `match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)` | Structured `match tokens` collection owned by `IgnBdTopoLogicalLayerConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Validators (exact source)**

`_unique_tokens`:

```python
def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(token) for token in value)
        if any(not token for token in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(set(normalized)) != len(normalized):
            raise ValueError("Layer match tokens must be unique after normalization")
        return value
```

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoLogicalLayersConfig` via `IgnBdTopoLogicalLayerConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoAccessConfig` via `IgnBdTopoLogicalLayerConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_matching_layers` via `IgnBdTopoLogicalLayerConfig`.

**Exact class source**

```python
class IgnBdTopoLogicalLayerConfig(BaseModel):
    """Catalogue class label and normalized tokens used for layer discovery."""

    model_config = ConfigDict(extra="forbid")

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

**Purpose:** Validates the grid/source contract carried by `electric_lines`, `transformation_posts`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `electric_lines` | `electric_lines: IgnBdTopoLogicalLayerConfig` | Factual IGN electricity-line GeoDataFrame owned by this source/normalized result. |
| `transformation_posts` | `transformation_posts: IgnBdTopoLogicalLayerConfig` | `IgnBdTopoLogicalLayersConfig.transformation_posts` represents the `transformation_posts` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Validators (exact source)**

`_different_token_sets`:

```python
def _different_token_sets(self) -> Self:
        electric = {
            _normalize_words(token) for token in self.electric_lines.match_tokens
        }
        posts = {
            _normalize_words(token)
            for token in self.transformation_posts.match_tokens
        }
        if electric == posts:
            raise ValueError("Logical layers must use different match tokens")
        return self
```

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` via `IgnBdTopoLogicalLayersConfig`.

**Exact class source**

```python
class IgnBdTopoLogicalLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    electric_lines: IgnBdTopoLogicalLayerConfig
    transformation_posts: IgnBdTopoLogicalLayerConfig

    @model_validator(mode="after")
    def _different_token_sets(self) -> Self:
        electric = {
            _normalize_words(token) for token in self.electric_lines.match_tokens
        }
        posts = {
            _normalize_words(token)
            for token in self.transformation_posts.match_tokens
        }
        if electric == posts:
            raise ValueError("Logical layers must use different match tokens")
        return self
```

### `IgnBdTopoDepartmentLayerConfig`

**Purpose:** Configured department layer and its observed identity field.

**Kind:** class.

**Inheritance:** `IgnBdTopoLogicalLayerConfig`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `department_code_field` | `department_code_field: NonEmptyString` | Configured physical attribute containing the department code. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoCoverageConfig` via `IgnBdTopoDepartmentLayerConfig`.

**Exact class source**

```python
class IgnBdTopoDepartmentLayerConfig(IgnBdTopoLogicalLayerConfig):
    """Configured department layer and its observed identity field."""

    department_code_field: NonEmptyString
```

### `IgnBdTopoAccessConfig`

**Purpose:** Configured factual transport layers loaded outside extraction metadata.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `road_segments` | `road_segments: IgnBdTopoLogicalLayerConfig` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |

**Interface consumers**

- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` via `IgnBdTopoAccessConfig`.

**Exact class source**

```python
class IgnBdTopoAccessConfig(BaseModel):
    """Configured factual transport layers loaded outside extraction metadata."""

    model_config = ConfigDict(extra="forbid")

    road_segments: IgnBdTopoLogicalLayerConfig
```

### `IgnBdTopoCoverageConfig`

**Purpose:** Validates the grid/source contract carried by `department_layer`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `department_layer` | `department_layer: IgnBdTopoDepartmentLayerConfig` | Configured department-coverage physical-layer match rule. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoSourceConfig` via `IgnBdTopoCoverageConfig`.

**Exact class source**

```python
class IgnBdTopoCoverageConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    department_layer: IgnBdTopoDepartmentLayerConfig
```

### `IgnBdTopoSourceConfig`

**Purpose:** Strict, reproducible description of one official IGN package.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `provider` | `provider: NonEmptyString` | Source-provider identity carried by this configuration/result and checked against its owning source contract. |
| `product` | `product: NonEmptyString` | Source product identity validated by the owning adapter. |
| `department_code` | `department_code: DepartmentCode` | French department code bound to this source package or normalization context. |
| `edition` | `edition: EditionString` | Declared physical source edition bound to this package/result. |
| `product_version` | `product_version: NonEmptyString \| None = None` | Nullable source product version copied from the verified package lineage. |
| `projection` | `projection: Projection` | Declared source-package projection identity checked by the owning adapter. |
| `format` | `format: PackageFormat` | `IgnBdTopoSourceConfig.format` represents the `format` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `archive_format` | `archive_format: ArchiveFormat` | `IgnBdTopoSourceConfig.archive_format` represents the `archive_format` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `source_url` | `source_url: HttpUrl` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `checksum_url` | `checksum_url: HttpUrl \| None = None` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `official_checksum_algorithm` | `official_checksum_algorithm: ChecksumAlgorithm \| None = None` | Official checksum algorithm declared for the source archive; null only when the source publishes no official checksum. |
| `official_checksum` | `official_checksum: HexChecksum \| None = None` | Official archive checksum value validated under official_checksum_algorithm; distinct from LandScout's SHA256. |
| `expected_archive_size_bytes` | `expected_archive_size_bytes: int \| None = Field(default=None, gt=0)` | Strict positive configured physical archive-size pin in bytes. |
| `cache_max_age_hours` | `cache_max_age_hours: float = Field(ge=0, allow_inf_nan=False)` | Configured maximum IGN archive-cache age in hours. |
| `logical_layers` | `logical_layers: IgnBdTopoLogicalLayersConfig` | Nested IGN electricity logical-role selection configuration. |
| `access` | `access: IgnBdTopoAccessConfig` | Nested IGN road logical-role selection configuration. |
| `coverage` | `coverage: IgnBdTopoCoverageConfig` | Nested department coverage-boundary selection configuration or validated coverage result. |

**Validators (exact source)**

`_valid_edition_date`:

```python
def _valid_edition_date(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError as error:
            raise ValueError("edition must be a valid ISO calendar date") from error
        return value
```

`_consistent_package_and_checksum`:

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
        if self.official_checksum_algorithm == "md5" and len(
            self.official_checksum or ""
        ) != 32:
            raise ValueError("An official MD5 checksum must contain 32 hexadecimal digits")
        if self.official_checksum_algorithm == "sha256" and len(
            self.official_checksum or ""
        ) != 64:
            raise ValueError(
                "An official SHA256 checksum must contain 64 hexadecimal digits"
            )
        if self.checksum_url is not None and not has_checksum:
            raise ValueError(
                "checksum_url requires a pinned official checksum and algorithm"
            )
        return self
```

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`.
- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `src/landscout/stages/enrich_grid_proximity.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
)`.
- import: `src/landscout/stages/enrich_road_proximity.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`.
- import: `src/landscout/stages/normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`.
- import: `src/landscout/stages/normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`.
- import: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_source_config` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_archive_filename` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::validate_ign_bdtopo_archive` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_download` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::discover_ign_bdtopo_layers` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_discover_department_coverage_layer` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_discover_road_layer` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_validated_layer_source_config` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_validate_archive_config_lineage` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_department_coverage` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_electricity_data` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_road_data` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_department_coverage` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_validate_configured_coverage_identity` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::assess_grid_coverage` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_coverage_summary` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::assess_road_proximity_coverage` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::enrich_parcel_grid_proximity` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::enrich_parcel_road_proximity` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/normalize_access_ign.py::_normalize_ign_roads` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/normalize_access_ign.py::normalize_ign_roads` via `IgnBdTopoSourceConfig`.
- type annotation: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::_synthetic_config` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::_extracted_fixture` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::source_config` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_valid_source_config_loads` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_real_layer_names_are_listed_and_discovered` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_missing_electric_line_layer_fails` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_missing_transformation_post_layer_fails` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_electric_line_layers_fail` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_schema_v2_extraction_metadata_binds_physical_geopackage` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_same_size_geopackage_tamper_invalidates_extraction_cache` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_forged_extraction_metadata_never_returns_cache_hit` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_sha_is_not_trusted` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_size_is_not_trusted` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_road_physical_layer_cannot_collide_with_electricity_roles` via `IgnBdTopoSourceConfig`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely` via `IgnBdTopoSourceConfig`.

**Exact class source**

```python
class IgnBdTopoSourceConfig(BaseModel):
    """Strict, reproducible description of one official IGN package."""

    model_config = ConfigDict(extra="forbid")

    provider: NonEmptyString
    product: NonEmptyString
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
    expected_archive_size_bytes: int | None = Field(default=None, gt=0)
    cache_max_age_hours: float = Field(ge=0, allow_inf_nan=False)
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
        if self.official_checksum_algorithm == "md5" and len(
            self.official_checksum or ""
        ) != 32:
            raise ValueError("An official MD5 checksum must contain 32 hexadecimal digits")
        if self.official_checksum_algorithm == "sha256" and len(
            self.official_checksum or ""
        ) != 64:
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

**Purpose:** Base error for controlled IGN BD TOPO source failures.

**Kind:** controlled exception.

**Inheritance:** `RuntimeError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.

**Exact class source**

```python
class IgnBdTopoError(RuntimeError):
    """Base error for controlled IGN BD TOPO source failures."""
```

### `IgnBdTopoDownloadError`

**Purpose:** Raised when an IGN archive cannot be downloaded or cached safely.

**Kind:** controlled exception.

**Inheritance:** `IgnBdTopoError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_source_config` via `IgnBdTopoDownloadError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_archive_filename` via `IgnBdTopoDownloadError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_require_no_cache_recovery_material` via `IgnBdTopoDownloadError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_prepare_temporary_cache_file` via `IgnBdTopoDownloadError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_cleanup_temporary_cache_files` via `IgnBdTopoDownloadError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_publish_cache_pair` via `IgnBdTopoDownloadError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `IgnBdTopoDownloadError`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `pytest.raises(IgnBdTopoDownloadError, match='backup|recovery|manual')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `pytest.raises(IgnBdTopoDownloadError)`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `pytest.raises(IgnBdTopoDownloadError)`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `pytest.raises(IgnBdTopoDownloadError, match='rollback')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `pytest.raises(IgnBdTopoDownloadError, match='rollback')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_stale_cache_recovery_backup_fails_closed_without_destroying_it` via `pytest.raises(IgnBdTopoDownloadError, match='backup|recovery|manual')`.

**Exact class source**

```python
class IgnBdTopoDownloadError(IgnBdTopoError):
    """Raised when an IGN archive cannot be downloaded or cached safely."""
```

### `IgnBdTopoArchiveError`

**Purpose:** Raised when an IGN archive or its extraction is unsafe or invalid.

**Kind:** controlled exception.

**Inheritance:** `IgnBdTopoError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_calculate_checksums` via `IgnBdTopoArchiveError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::validate_ign_bdtopo_archive` via `IgnBdTopoArchiveError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_archive_members` via `IgnBdTopoArchiveError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::discover_ign_bdtopo_geopackage` via `IgnBdTopoArchiveError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_safe_relative_path` via `IgnBdTopoArchiveError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_resolve_relative_path` via `IgnBdTopoArchiveError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_geopackage_integrity` via `IgnBdTopoArchiveError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_publish_extraction_directory` via `IgnBdTopoArchiveError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `IgnBdTopoArchiveError`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `pytest.raises(IgnBdTopoArchiveError)`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `pytest.raises(IgnBdTopoArchiveError)`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected` via `pytest.raises(IgnBdTopoArchiveError, match='checksum|SHA')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected` via `pytest.raises(IgnBdTopoArchiveError, match='unsafe|member|path')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_multiple_geopackages_are_rejected_as_ambiguous` via `pytest.raises(IgnBdTopoArchiveError, match='GeoPackage|exactly one|ambiguous')`.

**Exact class source**

```python
class IgnBdTopoArchiveError(IgnBdTopoError):
    """Raised when an IGN archive or its extraction is unsafe or invalid."""
```

### `IgnBdTopoLayerError`

**Purpose:** Raised when required GeoPackage layers cannot be discovered or loaded.

**Kind:** controlled exception.

**Inheritance:** `IgnBdTopoError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::list_ign_bdtopo_layers` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::discover_ign_bdtopo_layers` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_discover_department_coverage_layer` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_discover_road_layer` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_verify_unchanged_extraction` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_read_layer_frame` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_read_verified_layer_frames` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_layer_summary_contract` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_compare_layer_summary` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_compare_loaded_frame` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_lambert93` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_loaded_layer_from_frame` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_layer` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_validated_layer_source_config` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_archive_config_lineage` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_department_coverage_from_frame` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_department_coverage` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_electricity_data` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_road_data` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_coverage_summary_contract` via `IgnBdTopoLayerError`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_department_coverage` via `IgnBdTopoLayerError`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_missing_electric_line_layer_fails` via `pytest.raises(IgnBdTopoLayerError, match='electric|line|Ligne')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_missing_transformation_post_layer_fails` via `pytest.raises(IgnBdTopoLayerError, match='transformation|post|Poste')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_electric_line_layers_fail` via `pytest.raises(IgnBdTopoLayerError, match='unambiguous|found 2')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_geographic_crs_is_rejected` via `pytest.raises(IgnBdTopoLayerError, match='2154|Lambert|projected|CRS')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_road_physical_layer_cannot_collide_with_electricity_roles` via `pytest.raises(IgnBdTopoLayerError, match='same layer|collid|role')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely` via `pytest.raises(IgnBdTopoLayerError, match='road|route|found 0')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely` via `pytest.raises(IgnBdTopoLayerError, match='road|route|found 2')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department` via `pytest.raises(IgnBdTopoLayerError, match='department|archive|lineage')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory` via `pytest.raises(IgnBdTopoLayerError, match='inventory|changed')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs` via `pytest.raises(IgnBdTopoLayerError, match='2154|Lambert|projected|CRS')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature` via `pytest.raises(IgnBdTopoLayerError, match='exactly one|found')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field` via `pytest.raises(IgnBdTopoLayerError, match='identity field|missing_code')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails` via `pytest.raises(IgnBdTopoLayerError, match='department|found 0')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous` via `pytest.raises(IgnBdTopoLayerError, match='unambiguous|found 2')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering` via `pytest.raises(IgnBdTopoLayerError, match='integrity|SHA|physical|changed')`.
- expected exception type: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_source_change_after_physical_read` via `pytest.raises(IgnBdTopoLayerError, match='changed|integrity|SHA')`.

**Exact class source**

```python
class IgnBdTopoLayerError(IgnBdTopoError):
    """Raised when required GeoPackage layers cannot be discovered or loaded."""
```

### `IgnBdTopoArchiveIntegrity`

**Purpose:** Immutable result/value envelope carrying `file_size`, `sha256`, `official_checksum_algorithm`, `official_checksum`, `official_checksum_validated`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `file_size` | `file_size: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `official_checksum_algorithm` | `official_checksum_algorithm: ChecksumAlgorithm \| None` | Official checksum algorithm declared for the source archive; null only when the source publishes no official checksum. |
| `official_checksum` | `official_checksum: str \| None` | Official archive checksum value validated under official_checksum_algorithm; distinct from LandScout's SHA256. |
| `official_checksum_validated` | `official_checksum_validated: bool` | Boolean `official checksum validated` flag on `IgnBdTopoArchiveIntegrity`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::validate_ign_bdtopo_archive` via `IgnBdTopoArchiveIntegrity`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::validate_ign_bdtopo_archive` via `IgnBdTopoArchiveIntegrity`.

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

**Purpose:** Immutable result/value envelope carrying `provider`, `product`, `department_code`, `edition`, `product_version`, `projection`, `package_format`, `archive_format`, `source_url`, `checksum_url`, `download_timestamp`, `filename`, `file_size`, `sha256`, `official_checksum_algorithm`, `official_checksum`, `official_checksum_validated`, `path`, `cache_hit`, `spatial_role`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `provider` | `provider: str` | Source-provider identity carried by this configuration/result and checked against its owning source contract. |
| `product` | `product: str` | Source product identity validated by the owning adapter. |
| `department_code` | `department_code: str` | French department code bound to this source package or normalization context. |
| `edition` | `edition: str` | Declared physical source edition bound to this package/result. |
| `product_version` | `product_version: str \| None` | Nullable source product version copied from the verified package lineage. |
| `projection` | `projection: str` | Declared source-package projection identity checked by the owning adapter. |
| `package_format` | `package_format: str` | `IgnBdTopoDownload.package_format` represents the `package_format` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `archive_format` | `archive_format: str` | `IgnBdTopoDownload.archive_format` represents the `archive_format` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `source_url` | `source_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `checksum_url` | `checksum_url: str \| None` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `download_timestamp` | `download_timestamp: str` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `filename` | `filename: str` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `file_size` | `file_size: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `official_checksum_algorithm` | `official_checksum_algorithm: ChecksumAlgorithm \| None` | Official checksum algorithm declared for the source archive; null only when the source publishes no official checksum. |
| `official_checksum` | `official_checksum: str \| None` | Official archive checksum value validated under official_checksum_algorithm; distinct from LandScout's SHA256. |
| `official_checksum_validated` | `official_checksum_validated: bool` | Boolean `official checksum validated` flag on `IgnBdTopoDownload`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `path` | `path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `cache_hit` | `cache_hit: bool` | True only when already verified local cache state was reused. |
| `spatial_role` | `spatial_role: SpatialRole = "PROXY_GEOMETRY"` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `src/landscout/stages/normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`.
- import: `src/landscout/stages/normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`.
- import: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.sources import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoExtraction` via `IgnBdTopoDownload`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_cache_metadata_from_download` via `IgnBdTopoDownload`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_download_from_metadata` via `IgnBdTopoDownload`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_download_from_metadata` via `IgnBdTopoDownload`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_download` via `IgnBdTopoDownload`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `IgnBdTopoDownload`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `IgnBdTopoDownload`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `IgnBdTopoDownload`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `IgnBdTopoDownload`.
- constructor call: `tests/unit/test_assess_grid_coverage.py::_coverage` via `IgnBdTopoDownload`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_archive` via `IgnBdTopoDownload`.
- constructor call: `tests/unit/test_assess_road_proximity_coverage.py::_archive` via `IgnBdTopoDownload`.
- constructor call: `tests/unit/test_enrich_grid_proximity.py::_physical_electricity_source` via `IgnBdTopoDownload`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::_extracted_fixture` via `IgnBdTopoDownload`.
- constructor call: `tests/unit/test_normalize_access_ign.py::_source` via `IgnBdTopoDownload`.
- constructor call: `tests/unit/test_normalize_grid_ign.py::_source_bundle` via `IgnBdTopoDownload`.

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

**Purpose:** Immutable result/value envelope carrying `all_layer_names`, `electric_lines_layer`, `transformation_posts_layer`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `all_layer_names` | `all_layer_names: tuple[str, ...]` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |
| `electric_lines_layer` | `electric_lines_layer: str` | Physical GeoPackage layer selected for the configured electricity-line role. |
| `transformation_posts_layer` | `transformation_posts_layer: str` | `IgnBdTopoLayerSelection.transformation_posts_layer` represents the `transformation_posts_layer` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::discover_ign_bdtopo_layers` via `IgnBdTopoLayerSelection`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::discover_ign_bdtopo_layers` via `IgnBdTopoLayerSelection`.

**Exact class source**

```python
class IgnBdTopoLayerSelection:
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
```

### `IgnBdTopoExtraction`

**Purpose:** Immutable result/value envelope carrying `archive`, `extraction_path`, `geopackage_path`, `geopackage_filename`, `geopackage_size_bytes`, `geopackage_sha256`, `all_layer_names`, `electric_lines_layer`, `transformation_posts_layer`, `cache_hit`, `spatial_role`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `archive` | `archive: IgnBdTopoDownload` | Verified archive/download envelope from which this extraction or source object was built. |
| `extraction_path` | `extraction_path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `geopackage_path` | `geopackage_path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `geopackage_filename` | `geopackage_filename: str` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `geopackage_size_bytes` | `geopackage_size_bytes: int` | Measured physical byte size of the verified extracted GeoPackage. |
| `geopackage_sha256` | `geopackage_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `all_layer_names` | `all_layer_names: tuple[str, ...]` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |
| `electric_lines_layer` | `electric_lines_layer: str` | Physical GeoPackage layer selected for the configured electricity-line role. |
| `transformation_posts_layer` | `transformation_posts_layer: str` | `IgnBdTopoExtraction.transformation_posts_layer` represents the `transformation_posts_layer` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `cache_hit` | `cache_hit: bool` | True only when already verified local cache state was reused. |
| `spatial_role` | `spatial_role: SpatialRole = "PROXY_GEOMETRY"` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `src/landscout/stages/normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`.
- import: `src/landscout/stages/normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`.
- import: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.sources import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoElectricityData` via `IgnBdTopoExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoRoadData` via `IgnBdTopoExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoDepartmentCoverage` via `IgnBdTopoExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_VerifiedIgnExtraction` via `IgnBdTopoExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `IgnBdTopoExtraction`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `IgnBdTopoExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `IgnBdTopoExtraction`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `IgnBdTopoExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `IgnBdTopoExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `IgnBdTopoExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_department_coverage_from_frame` via `IgnBdTopoExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_department_coverage` via `IgnBdTopoExtraction`.
- constructor call: `tests/unit/test_assess_grid_coverage.py::_coverage` via `IgnBdTopoExtraction`.
- type annotation: `tests/unit/test_assess_grid_coverage.py::_electricity_source` via `IgnBdTopoExtraction`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_extraction` via `IgnBdTopoExtraction`.
- constructor call: `tests/unit/test_assess_road_proximity_coverage.py::_extraction` via `IgnBdTopoExtraction`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_road_source` via `IgnBdTopoExtraction`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_coverage` via `IgnBdTopoExtraction`.
- constructor call: `tests/unit/test_enrich_grid_proximity.py::_physical_electricity_source` via `IgnBdTopoExtraction`.
- type annotation: `tests/unit/test_ign_bdtopo_fr.py::_extracted_fixture` via `IgnBdTopoExtraction`.
- constructor call: `tests/unit/test_normalize_access_ign.py::_source` via `IgnBdTopoExtraction`.
- constructor call: `tests/unit/test_normalize_grid_ign.py::_source_bundle` via `IgnBdTopoExtraction`.

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
    cache_hit: bool
    spatial_role: SpatialRole = "PROXY_GEOMETRY"
```

### `IgnBdTopoLayerSummary`

**Purpose:** Immutable result/value envelope carrying `logical_name`, `source_layer_name`, `crs`, `feature_count`, `columns`, `dtypes`, `null_geometry_count`, `empty_geometry_count`, `invalid_geometry_count`, `geometry_types`, `spatial_role`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `logical_name` | `logical_name: LogicalLayerName` | LandScout logical dataset/layer role bound to the selected physical source. |
| `source_layer_name` | `source_layer_name: str` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `crs` | `crs: str` | Coordinate reference system identity; exact accepted/storage/calculation behavior is enforced by the owning CRS validator. |
| `feature_count` | `feature_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `columns` | `columns: tuple[str, ...]` | Structured `columns` collection owned by `IgnBdTopoLayerSummary`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `dtypes` | `dtypes: tuple[tuple[str, str], ...]` | `IgnBdTopoLayerSummary.dtypes` represents the `dtypes` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `null_geometry_count` | `null_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `empty_geometry_count` | `empty_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `invalid_geometry_count` | `invalid_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `geometry_types` | `geometry_types: tuple[str, ...]` | `IgnBdTopoLayerSummary.geometry_types` represents the `geometry_types` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `spatial_role` | `spatial_role: SpatialRole = "PROXY_GEOMETRY"` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `src/landscout/stages/normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`.
- import: `src/landscout/stages/normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.sources import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoLoadedLayer` via `IgnBdTopoLayerSummary`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoElectricityData` via `IgnBdTopoLayerSummary`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoRoadData` via `IgnBdTopoLayerSummary`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_validate_layer_summary_contract` via `IgnBdTopoLayerSummary`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_compare_layer_summary` via `IgnBdTopoLayerSummary`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_loaded_layer_from_frame` via `IgnBdTopoLayerSummary`.
- type annotation: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `IgnBdTopoLayerSummary`.
- type annotation: `src/landscout/stages/normalize_grid_ign.py::_validate_layer_summary` via `IgnBdTopoLayerSummary`.
- constructor call: `tests/unit/test_assess_road_proximity_coverage.py::_road_source` via `IgnBdTopoLayerSummary`.
- type annotation: `tests/unit/test_enrich_grid_proximity.py::_physical_summary` via `IgnBdTopoLayerSummary`.
- constructor call: `tests/unit/test_enrich_grid_proximity.py::_physical_summary` via `IgnBdTopoLayerSummary`.
- type annotation: `tests/unit/test_normalize_access_ign.py::_summary` via `IgnBdTopoLayerSummary`.
- constructor call: `tests/unit/test_normalize_access_ign.py::_summary` via `IgnBdTopoLayerSummary`.
- type annotation: `tests/unit/test_normalize_grid_ign.py::_summary` via `IgnBdTopoLayerSummary`.
- constructor call: `tests/unit/test_normalize_grid_ign.py::_summary` via `IgnBdTopoLayerSummary`.

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

**Purpose:** Immutable result/value envelope carrying `data`, `summary`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `data` | `data: gpd.GeoDataFrame` | GeoDataFrame loaded for this exact inspected logical/physical layer. |
| `summary` | `summary: IgnBdTopoLayerSummary` | Validated immutable summary of the owning physical frame/layer. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_loaded_layer_from_frame` via `IgnBdTopoLoadedLayer`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_loaded_layer_from_frame` via `IgnBdTopoLoadedLayer`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_layer` via `IgnBdTopoLoadedLayer`.

**Exact class source**

```python
class IgnBdTopoLoadedLayer:
    data: gpd.GeoDataFrame
    summary: IgnBdTopoLayerSummary
```

### `IgnBdTopoElectricityData`

**Purpose:** Immutable result/value envelope carrying `extraction`, `electric_lines`, `transformation_posts`, `electric_lines_summary`, `transformation_posts_summary`, `spatial_role`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `extraction` | `extraction: IgnBdTopoExtraction` | `IgnBdTopoElectricityData.extraction` carries the extraction used by the reproduced constructors and validators; its declared type is `IgnBdTopoExtraction` and no legal meaning is inferred beyond that owner. |
| `electric_lines` | `electric_lines: gpd.GeoDataFrame` | Factual IGN electricity-line GeoDataFrame owned by this source/normalized result. |
| `transformation_posts` | `transformation_posts: gpd.GeoDataFrame` | `IgnBdTopoElectricityData.transformation_posts` represents the `transformation_posts` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `electric_lines_summary` | `electric_lines_summary: IgnBdTopoLayerSummary` | Validated summary of the factual IGN electricity-line frame. |
| `transformation_posts_summary` | `transformation_posts_summary: IgnBdTopoLayerSummary` | `IgnBdTopoElectricityData.transformation_posts_summary` represents the `transformation_posts_summary` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `spatial_role` | `spatial_role: SpatialRole = "PROXY_GEOMETRY"` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `src/landscout/stages/enrich_grid_proximity.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
)`.
- import: `src/landscout/stages/normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`.
- import: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.sources import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `IgnBdTopoElectricityData`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `IgnBdTopoElectricityData`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_electricity_data` via `IgnBdTopoElectricityData`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::assess_grid_coverage` via `IgnBdTopoElectricityData`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::enrich_parcel_grid_proximity` via `IgnBdTopoElectricityData`.
- type annotation: `src/landscout/stages/normalize_grid_ign.py::_validate_archive_identity` via `IgnBdTopoElectricityData`.
- type annotation: `src/landscout/stages/normalize_grid_ign.py::_validate_source_bundle` via `IgnBdTopoElectricityData`.
- type annotation: `src/landscout/stages/normalize_grid_ign.py::_source_context` via `IgnBdTopoElectricityData`.
- type annotation: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `IgnBdTopoElectricityData`.
- type annotation: `tests/unit/test_assess_grid_coverage.py::_electricity_source` via `IgnBdTopoElectricityData`.
- constructor call: `tests/unit/test_assess_grid_coverage.py::_electricity_source` via `IgnBdTopoElectricityData`.
- type annotation: `tests/unit/test_enrich_grid_proximity.py::_electricity_source` via `IgnBdTopoElectricityData`.
- constructor call: `tests/unit/test_enrich_grid_proximity.py::_electricity_source` via `IgnBdTopoElectricityData`.
- type annotation: `tests/unit/test_enrich_grid_proximity.py::_physical_electricity_source` via `IgnBdTopoElectricityData`.
- constructor call: `tests/unit/test_enrich_grid_proximity.py::_physical_electricity_source` via `IgnBdTopoElectricityData`.
- type annotation: `tests/unit/test_enrich_grid_proximity.py::_alternate_role_electricity_source` via `IgnBdTopoElectricityData`.
- type annotation: `tests/unit/test_enrich_grid_proximity.py::_configured_role_electricity_source` via `IgnBdTopoElectricityData`.
- type annotation: `tests/unit/test_normalize_grid_ign.py::normalize_ign_electricity` via `IgnBdTopoElectricityData`.
- type annotation: `tests/unit/test_normalize_grid_ign.py::_source_bundle` via `IgnBdTopoElectricityData`.
- constructor call: `tests/unit/test_normalize_grid_ign.py::_source_bundle` via `IgnBdTopoElectricityData`.
- type annotation: `tests/unit/test_normalize_grid_ign.py::_source_bundle_with_archive` via `IgnBdTopoElectricityData`.

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

**Purpose:** Unfiltered factual road geometry from one verified IGN extraction.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `extraction` | `extraction: IgnBdTopoExtraction` | `IgnBdTopoRoadData.extraction` carries the extraction used by the reproduced constructors and validators; its declared type is `IgnBdTopoExtraction` and no legal meaning is inferred beyond that owner. |
| `road_segments` | `road_segments: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `road_segments_summary` | `road_segments_summary: IgnBdTopoLayerSummary` | Validated summary of the factual IGN road-segment frame. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `src/landscout/stages/enrich_road_proximity.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`.
- import: `src/landscout/stages/normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`.
- import: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_enrich_road_proximity.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `IgnBdTopoRoadData`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_road_data` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::assess_road_proximity_coverage` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::enrich_parcel_road_proximity` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/normalize_access_ign.py::_normalize_ign_roads` via `IgnBdTopoRoadData`.
- type annotation: `src/landscout/stages/normalize_access_ign.py::normalize_ign_roads` via `IgnBdTopoRoadData`.
- type annotation: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_source` via `IgnBdTopoRoadData`.
- constructor call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_source` via `IgnBdTopoRoadData`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_road_source` via `IgnBdTopoRoadData`.
- constructor call: `tests/unit/test_assess_road_proximity_coverage.py::_road_source` via `IgnBdTopoRoadData`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `IgnBdTopoRoadData`.
- type annotation: `tests/unit/test_enrich_road_proximity.py::_source` via `IgnBdTopoRoadData`.
- constructor call: `tests/unit/test_enrich_road_proximity.py::_source` via `IgnBdTopoRoadData`.
- type annotation: `tests/unit/test_normalize_access_ign.py::_source` via `IgnBdTopoRoadData`.
- constructor call: `tests/unit/test_normalize_access_ign.py::_source` via `IgnBdTopoRoadData`.
- type annotation: `tests/unit/test_normalize_access_ign.py::_with_alternate_road_layer` via `IgnBdTopoRoadData`.

**Exact class source**

```python
class IgnBdTopoRoadData:
    """Unfiltered factual road geometry from one verified IGN extraction."""

    extraction: IgnBdTopoExtraction
    road_segments: gpd.GeoDataFrame
    road_segments_summary: IgnBdTopoLayerSummary
```

### `IgnBdTopoCoverageLayerSummary`

**Purpose:** Observed source-layer schema plus the authoritative selected feature.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `source_layer_name` | `source_layer_name: str` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `crs` | `crs: str` | Coordinate reference system identity; exact accepted/storage/calculation behavior is enforced by the owning CRS validator. |
| `source_feature_count` | `source_feature_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `selected_feature_count` | `selected_feature_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `columns` | `columns: tuple[str, ...]` | Structured `columns` collection owned by `IgnBdTopoCoverageLayerSummary`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `dtypes` | `dtypes: tuple[tuple[str, str], ...]` | `IgnBdTopoCoverageLayerSummary.dtypes` represents the `dtypes` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `null_geometry_count` | `null_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `empty_geometry_count` | `empty_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `invalid_geometry_count` | `invalid_geometry_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `geometry_types` | `geometry_types: tuple[str, ...]` | `IgnBdTopoCoverageLayerSummary.geometry_types` represents the `geometry_types` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `department_code_field` | `department_code_field: str` | Configured physical attribute containing the department code. |
| `selected_department_code` | `selected_department_code: str` | Department code selected from the configured coverage layer; it must equal package/config lineage. |
| `spatial_role` | `spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoDepartmentCoverage` via `IgnBdTopoCoverageLayerSummary`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_department_coverage_from_frame` via `IgnBdTopoCoverageLayerSummary`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_validate_coverage_summary_contract` via `IgnBdTopoCoverageLayerSummary`.
- constructor call: `tests/unit/test_assess_grid_coverage.py::_coverage` via `IgnBdTopoCoverageLayerSummary`.
- constructor call: `tests/unit/test_assess_road_proximity_coverage.py::_coverage` via `IgnBdTopoCoverageLayerSummary`.

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

**Purpose:** Selected department coverage with package lineage and source schema.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `extraction` | `extraction: IgnBdTopoExtraction` | `IgnBdTopoDepartmentCoverage.extraction` carries the extraction used by the reproduced constructors and validators; its declared type is `IgnBdTopoExtraction` and no legal meaning is inferred beyond that owner. |
| `coverage` | `coverage: gpd.GeoDataFrame` | Nested department coverage-boundary selection configuration or validated coverage result. |
| `summary` | `summary: IgnBdTopoCoverageLayerSummary` | Validated immutable summary of the owning physical frame/layer. |
| `source_provider` | `source_provider: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_product` | `source_product: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_department_code` | `source_department_code: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_edition` | `source_edition: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_product_version` | `source_product_version: str \| None` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_layer` | `source_layer: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `spatial_role` | `spatial_role: CoverageSpatialRole = "SOURCE_COVERAGE_BOUNDARY"` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |

**Interface consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_department_coverage_from_frame` via `IgnBdTopoDepartmentCoverage`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_department_coverage_from_frame` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_department_coverage` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_department_coverage` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::GridCoverageAssessmentResult` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_validate_coverage_summary` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_validate_source_coverage` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_validate_configured_coverage_identity` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_coverage_lineage_values` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_validate_proximity_source_identity` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::RoadProximityCoverageAssessmentResult` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_coverage_summary` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_coverage_lineage` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_expected_diagnostics` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_diagnosed_class_proximity` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_selected_road_package` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `tests/unit/test_assess_grid_coverage.py::_coverage` via `IgnBdTopoDepartmentCoverage`.
- constructor call: `tests/unit/test_assess_grid_coverage.py::_coverage` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `tests/unit/test_assess_grid_coverage.py::_with_alternate_coverage_layer` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_coverage` via `IgnBdTopoDepartmentCoverage`.
- constructor call: `tests/unit/test_assess_road_proximity_coverage.py::_coverage` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_measured_boundary_distance` via `IgnBdTopoDepartmentCoverage`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `IgnBdTopoDepartmentCoverage`.

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

**Purpose:** Validates the grid/source contract carried by `schema_version`, `provider`, `product`, `department_code`, `edition`, `product_version`, `projection`, `package_format`, `archive_format`, `source_url`, `checksum_url`, `download_timestamp`, `filename`, `file_size`, `sha256`, `official_checksum_algorithm`, `official_checksum`, `official_checksum_validated`, `spatial_role`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: Literal[1]` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `provider` | `provider: str` | Source-provider identity carried by this configuration/result and checked against its owning source contract. |
| `product` | `product: str` | Source product identity validated by the owning adapter. |
| `department_code` | `department_code: str` | French department code bound to this source package or normalization context. |
| `edition` | `edition: str` | Declared physical source edition bound to this package/result. |
| `product_version` | `product_version: str \| None` | Nullable source product version copied from the verified package lineage. |
| `projection` | `projection: str` | Declared source-package projection identity checked by the owning adapter. |
| `package_format` | `package_format: str` | `_CacheMetadata.package_format` represents the `package_format` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `archive_format` | `archive_format: str` | `_CacheMetadata.archive_format` represents the `archive_format` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `source_url` | `source_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `checksum_url` | `checksum_url: str \| None` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `download_timestamp` | `download_timestamp: str` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `filename` | `filename: str` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `file_size` | `file_size: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `sha256` | `sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `official_checksum_algorithm` | `official_checksum_algorithm: ChecksumAlgorithm \| None` | Official checksum algorithm declared for the source archive; null only when the source publishes no official checksum. |
| `official_checksum` | `official_checksum: str \| None` | Official archive checksum value validated under official_checksum_algorithm; distinct from LandScout's SHA256. |
| `official_checksum_validated` | `official_checksum_validated: bool` | Boolean `official checksum validated` flag on `_CacheMetadata`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `spatial_role` | `spatial_role: SpatialRole` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |

**Interface consumers**

- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_cache_metadata_from_download` via `_CacheMetadata`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_cache_metadata_from_download` via `_CacheMetadata`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_download_from_metadata` via `_CacheMetadata`.

**Exact class source**

```python
class _CacheMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

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
    file_size: int
    sha256: str
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: bool
    spatial_role: SpatialRole
```

### `_ExtractionMetadata`

**Purpose:** Validates the grid/source contract carried by `schema_version`, `archive_sha256`, `geopackage_relative_path`, `geopackage_size_bytes`, `geopackage_sha256`, `all_layer_names`, `electric_lines_layer`, `transformation_posts_layer`, `spatial_role`.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: Literal[2]` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `archive_sha256` | `archive_sha256: CanonicalSha256` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `geopackage_relative_path` | `geopackage_relative_path: str` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |
| `geopackage_size_bytes` | `geopackage_size_bytes: StrictPositiveInt` | Measured physical byte size of the verified extracted GeoPackage. |
| `geopackage_sha256` | `geopackage_sha256: CanonicalSha256` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `all_layer_names` | `all_layer_names: tuple[str, ...]` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |
| `electric_lines_layer` | `electric_lines_layer: str` | Physical GeoPackage layer selected for the configured electricity-line role. |
| `transformation_posts_layer` | `transformation_posts_layer: str` | `_ExtractionMetadata.transformation_posts_layer` represents the `transformation_posts_layer` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `spatial_role` | `spatial_role: SpatialRole` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |

**Interface consumers**

- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_VerifiedIgnExtraction` via `_ExtractionMetadata`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_ExtractionMetadata`.

**Exact class source**

```python
class _ExtractionMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[2]
    archive_sha256: CanonicalSha256
    geopackage_relative_path: str
    geopackage_size_bytes: StrictPositiveInt
    geopackage_sha256: CanonicalSha256
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    spatial_role: SpatialRole
```

### `_VerifiedIgnExtraction`

**Purpose:** Immutable result/value envelope carrying `extraction`, `metadata`, `geopackage_path`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `extraction` | `extraction: IgnBdTopoExtraction` | `_VerifiedIgnExtraction.extraction` carries the extraction used by the reproduced constructors and validators; its declared type is `IgnBdTopoExtraction` and no legal meaning is inferred beyond that owner. |
| `metadata` | `metadata: _ExtractionMetadata` | Strict parsed cache/extraction metadata bound to the verified physical source. |
| `geopackage_path` | `geopackage_path: Path` | Filesystem location for the artifact named by the field; containment, portability, link, existence, and recovery checks belong to the owning source/artifact validator. |

**Interface consumers**

- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `_VerifiedIgnExtraction`.
- constructor call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `_VerifiedIgnExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_verify_unchanged_extraction` via `_VerifiedIgnExtraction`.
- type annotation: `src/landscout/sources/ign_bdtopo_fr.py::_read_verified_layer_frames` via `_VerifiedIgnExtraction`.

**Exact class source**

```python
class _VerifiedIgnExtraction:
    extraction: IgnBdTopoExtraction
    metadata: _ExtractionMetadata
    geopackage_path: Path
```


## 6. Functions and methods

### `IgnBdTopoLogicalLayerConfig._unique_tokens`

**Exact signature**

```python
def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
```

**Purpose**

Private `grid/source` helper for unique tokens; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `any((not token for token in normalized))`.
- Guard with a raise path: `len(set(normalized)) != len(normalized)`.
- Explicit raise expressions: `ValueError('Layer match tokens must be unique after normalization')`, `ValueError('Layer match tokens must contain letters or digits')`.

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
def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(token) for token in value)
        if any(not token for token in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(set(normalized)) != len(normalized):
            raise ValueError("Layer match tokens must be unique after normalization")
        return value
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `IgnBdTopoLogicalLayersConfig._different_token_sets`

**Exact signature**

```python
def _different_token_sets(self) -> Self:
```

**Purpose**

Private `grid/source` helper for different token sets; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `electric == posts`.
- Explicit raise expressions: `ValueError('Logical layers must use different match tokens')`.

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
def _different_token_sets(self) -> Self:
        electric = {
            _normalize_words(token) for token in self.electric_lines.match_tokens
        }
        posts = {
            _normalize_words(token)
            for token in self.transformation_posts.match_tokens
        }
        if electric == posts:
            raise ValueError("Logical layers must use different match tokens")
        return self
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `IgnBdTopoSourceConfig._valid_edition_date`

**Exact signature**

```python
def _valid_edition_date(cls, value: str) -> str:
```

**Purpose**

Private `grid/source` helper for valid edition date; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `ValueError('edition must be a valid ISO calendar date')`.

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
def _valid_edition_date(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError as error:
            raise ValueError("edition must be a valid ISO calendar date") from error
        return value
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `IgnBdTopoSourceConfig._consistent_package_and_checksum`

**Exact signature**

```python
def _consistent_package_and_checksum(self) -> Self:
```

**Purpose**

Private `grid/source` helper for consistent package and checksum; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `Path(path).suffix.casefold() != f'.{self.archive_format}'`.
- Guard with a raise path: `has_algorithm != has_checksum`.
- Guard with a raise path: `self.official_checksum_algorithm == 'md5' and len(self.official_checksum or '') != 32`.
- Guard with a raise path: `self.official_checksum_algorithm == 'sha256' and len(self.official_checksum or '') != 64`.
- Guard with a raise path: `self.checksum_url is not None and (not has_checksum)`.
- Explicit raise expressions: `ValueError('An official MD5 checksum must contain 32 hexadecimal digits')`, `ValueError('An official SHA256 checksum must contain 64 hexadecimal digits')`, `ValueError('checksum_url requires a pinned official checksum and algorithm')`, `ValueError('official_checksum_algorithm and official_checksum must be set together')`, `ValueError('source_url extension does not match archive_format')`.

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
        if self.official_checksum_algorithm == "md5" and len(
            self.official_checksum or ""
        ) != 32:
            raise ValueError("An official MD5 checksum must contain 32 hexadecimal digits")
        if self.official_checksum_algorithm == "sha256" and len(
            self.official_checksum or ""
        ) != 64:
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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
' '.join(re.findall('[a-z0-9]+', ascii_like))
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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoLogicalLayerConfig._unique_tokens` via `_normalize_words`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::IgnBdTopoLogicalLayersConfig._different_token_sets` via `_normalize_words`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_matching_layers` via `_normalize_words`.

**Complete source-ordered implementation**

```python
def _normalize_words(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    ascii_like = "".join(char for char in decomposed if not unicodedata.combining(char))
    return " ".join(re.findall(r"[a-z0-9]+", ascii_like))
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_source_config`

**Exact signature**

```python
def load_ign_bdtopo_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> IgnBdTopoSourceConfig:
```

**Purpose**

Load and strictly validate the pinned IGN source configuration.

**Return contract**

- Declared return annotation: `IgnBdTopoSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoSourceConfig.model_validate(content)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(content, dict)`.
- Explicit raise expressions: `IgnBdTopoDownloadError(f'Cannot read IGN source config: {path}')`, `TypeError(f'Expected a YAML mapping in {path}')`.

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

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.sources import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_enrich_road_proximity.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `load_ign_bdtopo_source_config`.
- direct call: `tests/unit/test_assess_grid_coverage.py::<module>` via `load_ign_bdtopo_source_config`.
- direct call: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `load_ign_bdtopo_source_config`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::<module>` via `load_ign_bdtopo_source_config`.
- direct call: `tests/unit/test_enrich_road_proximity.py::<module>` via `load_ign_bdtopo_source_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::source_config` via `load_ign_bdtopo_source_config`.
- direct call: `tests/unit/test_normalize_access_ign.py::<module>` via `load_ign_bdtopo_source_config`.
- direct call: `tests/unit/test_normalize_grid_ign.py::<module>` via `load_ign_bdtopo_source_config`.

**Complete source-ordered implementation**

```python
def load_ign_bdtopo_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> IgnBdTopoSourceConfig:
    """Load and strictly validate the pinned IGN source configuration."""

    try:
        with path.open(encoding="utf-8") as stream:
            content = yaml.safe_load(stream)
    except OSError as error:
        raise IgnBdTopoDownloadError(f"Cannot read IGN source config: {path}") from error
    if not isinstance(content, dict):
        raise TypeError(f"Expected a YAML mapping in {path}")
    return IgnBdTopoSourceConfig.model_validate(content)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_archive_filename`

**Exact signature**

```python
def _archive_filename(config: IgnBdTopoSourceConfig) -> str:
```

**Purpose**

Private `grid/source` helper for archive filename; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
filename
```

**Validation and exceptions**

- Guard with a raise path: `not filename or Path(filename).suffix.casefold() != '.7z'`.
- Explicit raise expressions: `IgnBdTopoDownloadError('IGN source URL does not identify a .7z archive')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_archive_filename`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_archive_config_lineage` via `_archive_filename`.

**Complete source-ordered implementation**

```python
def _archive_filename(config: IgnBdTopoSourceConfig) -> str:
    filename = Path(unquote(urlparse(str(config.source_url)).path)).name
    if not filename or Path(filename).suffix.casefold() != ".7z":
        raise IgnBdTopoDownloadError("IGN source URL does not identify a .7z archive")
    return filename
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_calculate_checksums`

**Exact signature**

```python
def _calculate_checksums(
    path: Path, official_algorithm: ChecksumAlgorithm | None
) -> tuple[str, str | None]:
```

**Purpose**

Private `grid/source` helper for calculate checksums; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, str | None]`.
- Every observed return expression is reproduced without truncation:
```python
(sha256_digest.hexdigest(), official_digest.hexdigest() if official_digest is not None else None)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `IgnBdTopoArchiveError(f'Cannot read IGN archive: {path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.open`, `stream.read`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `md5`, `official_digest.hexdigest`, `sha256`, `sha256_digest.hexdigest`.
- Environment/process effects: none.
- In-memory mutation: `official_digest`, `sha256_digest`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::validate_ign_bdtopo_archive` via `_calculate_checksums`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `validate_ign_bdtopo_archive`

**Exact signature**

```python
def validate_ign_bdtopo_archive(
    path: Path, config: IgnBdTopoSourceConfig
) -> IgnBdTopoArchiveIntegrity:
```

**Purpose**

Validate size, configured official checksum, and available 7z CRC data. Some official IGN archives omit container CRC metadata, for which py7zr returns ``None``. Such archives still require exact official size/checksum validation here and a successful full extraction before they are usable.

**Return contract**

- Declared return annotation: `IgnBdTopoArchiveIntegrity`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoArchiveIntegrity(file_size=file_size, sha256=local_sha256, official_checksum_algorithm=config.official_checksum_algorithm, official_checksum=config.official_checksum, official_checksum_validated=official_validated)
```

**Validation and exceptions**

- Guard with a raise path: `not path.is_file()`.
- Guard with a raise path: `file_size <= 0`.
- Guard with a raise path: `config.expected_archive_size_bytes is not None and file_size != config.expected_archive_size_bytes`.
- Guard with a raise path: `official_validated and calculated_official != config.official_checksum`.
- Guard with a raise path: `integrity_result is False`.
- Explicit raise expressions: `IgnBdTopoArchiveError(f'Cannot inspect IGN archive: {path}')`, `IgnBdTopoArchiveError(f'IGN archive does not exist: {path}')`, `IgnBdTopoArchiveError(f'IGN archive does not match the pinned official {config.official_checksum_algorithm} checksum')`, `IgnBdTopoArchiveError(f'IGN archive failed its 7z CRC integrity check: {path}')`, `IgnBdTopoArchiveError(f'IGN archive is empty: {path}')`, `IgnBdTopoArchiveError(f'IGN archive is not a readable 7z file: {path}')`, `IgnBdTopoArchiveError(f'IGN archive size does not match the official catalogue: {file_size} != {config.expected_archive_size_bytes}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.is_file`, `path.stat`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_download` via `validate_ign_bdtopo_archive`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `validate_ign_bdtopo_archive`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `validate_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `validate_ign_bdtopo_archive`.

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

    if not path.is_file():
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_cache_metadata_from_download`

**Exact signature**

```python
def _cache_metadata_from_download(download: IgnBdTopoDownload) -> _CacheMetadata:
```

**Purpose**

Private `grid/source` helper for cache metadata from download; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_CacheMetadata`.
- Every observed return expression is reproduced without truncation:
```python
_CacheMetadata(schema_version=1, provider=download.provider, product=download.product, department_code=download.department_code, edition=download.edition, product_version=download.product_version, projection=download.projection, package_format=download.package_format, archive_format=download.archive_format, source_url=download.source_url, checksum_url=download.checksum_url, download_timestamp=download.download_timestamp, filename=download.filename, file_size=download.file_size, sha256=download.sha256, official_checksum_algorithm=download.official_checksum_algorithm, official_checksum=download.official_checksum, official_checksum_validated=download.official_checksum_validated, spatial_role=download.spatial_role)
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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_cache_metadata_from_download`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_download_from_metadata`

**Exact signature**

```python
def _download_from_metadata(
    metadata: _CacheMetadata, archive_path: Path, *, cache_hit: bool
) -> IgnBdTopoDownload:
```

**Purpose**

Acquires, verifies, and records from metadata; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnBdTopoDownload`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoDownload(provider=metadata.provider, product=metadata.product, department_code=metadata.department_code, edition=metadata.edition, product_version=metadata.product_version, projection=metadata.projection, package_format=metadata.package_format, archive_format=metadata.archive_format, source_url=metadata.source_url, checksum_url=metadata.checksum_url, download_timestamp=metadata.download_timestamp, filename=metadata.filename, file_size=metadata.file_size, sha256=metadata.sha256, official_checksum_algorithm=metadata.official_checksum_algorithm, official_checksum=metadata.official_checksum, official_checksum_validated=metadata.official_checksum_validated, path=archive_path, cache_hit=cache_hit, spatial_role=metadata.spatial_role)
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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_download` via `_download_from_metadata`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_load_cached_download`

**Exact signature**

```python
def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDownload | None:
```

**Purpose**

Reads and validates cached download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnBdTopoDownload | None`.
- Every observed return expression is reproduced without truncation:
```python
None

_download_from_metadata(metadata, archive_path, cache_hit=True)

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

- Network I/O: `_download_from_metadata`.
- Filesystem read: `archive_path.is_file`, `metadata_path.is_file`, `metadata_path.read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_load_cached_download`.

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
        metadata = _CacheMetadata.model_validate_json(
            metadata_path.read_text(encoding="utf-8")
        )
        downloaded_at = datetime.fromisoformat(metadata.download_timestamp)
        if downloaded_at.tzinfo is None:
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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_publish_cache_pair` via `_replace_file`.

**Complete source-ordered implementation**

```python
def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)
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
(archive_path.with_name(f'{archive_path.name}.bak'), metadata_path.with_name(f'{metadata_path.name}.bak'))
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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_require_no_cache_recovery_material` via `_cache_recovery_paths`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_publish_cache_pair` via `_cache_recovery_paths`.

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

- Guard with a raise path: `any((path.exists() or path.is_symlink() or path.is_junction() for path in recovery_paths))`.
- Explicit raise expressions: `IgnBdTopoDownloadError('IGN cache recovery backup already exists; manual recovery is required')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_publish_cache_pair` via `_require_no_cache_recovery_material`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_require_no_cache_recovery_material`.

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

- Guard with a raise path: `path.is_symlink() or path.is_junction()`.
- Guard with a raise path: `path.exists()`.
- Guard with a raise path: `not path.is_file()`.
- Explicit raise expressions: `IgnBdTopoDownloadError('IGN cache temporary path cannot be prepared safely')`, `IgnBdTopoDownloadError('IGN cache temporary path is a link or junction')`, `IgnBdTopoDownloadError('IGN cache temporary path is not a regular file')`, `re-raise`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_prepare_temporary_cache_file`.

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
- Explicit raise expressions: `IgnBdTopoDownloadError('IGN cache temporary files could not be cleaned safely')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_cleanup_temporary_cache_files`.

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
- Explicit raise expressions: `IgnBdTopoDownloadError('IGN cache publication and rollback both failed')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `archive_path.is_file`, `metadata_path.is_file`.
- Filesystem write: `archive_backup.unlink`, `archive_path.unlink`, `metadata_backup.unlink`, `metadata_path.unlink`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `_publish_cache_pair`.

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
        except OSError as rollback_error:
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `download_ign_bdtopo_archive`

**Exact signature**

```python
def download_ign_bdtopo_archive(
    config: IgnBdTopoSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> IgnBdTopoDownload:
```

**Purpose**

Download or reuse the pinned IGN package with atomic cache publication.

**Return contract**

- Declared return annotation: `IgnBdTopoDownload`.
- Every observed return expression is reproduced without truncation:
```python
cached

result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `IgnBdTopoDownloadError(f'IGN download failed: {source_url}')`, `re-raise`.

**Side effects**

- Network I/O: `open_safe_https`.
- Filesystem read: `temporary_archive.open`.
- Filesystem write: `cache_dir.mkdir`, `copyfileobj`, `temporary_metadata.write_text`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::_extracted_fixture` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous` via `download_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering` via `download_ign_bdtopo_archive`.

**Complete source-ordered implementation**

```python
def download_ign_bdtopo_archive(
    config: IgnBdTopoSourceConfig,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    timeout: float = 120.0,
) -> IgnBdTopoDownload:
    """Download or reuse the pinned IGN package with atomic cache publication."""

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
            temporary_archive.open("wb") as output,
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
        temporary_metadata.write_text(
            metadata.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_archive_members`

**Exact signature**

```python
def _validate_archive_members(archive: py7zr.SevenZipFile) -> None:
```

**Purpose**

Rejects malformed or inconsistent archive members; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not infos`.
- Guard with a raise path: `not name or '\x00' in name`.
- Guard with a raise path: `posix_path.is_absolute() or windows_path.is_absolute() or bool(windows_path.drive) or ('..' in posix_path.parts)`.
- Guard with a raise path: `info.is_symlink or not (info.is_file or info.is_directory)`.
- Explicit raise expressions: `IgnBdTopoArchiveError('IGN archive contains an invalid member name')`, `IgnBdTopoArchiveError('IGN archive contains no members')`, `IgnBdTopoArchiveError(f'IGN archive contains an unsafe member path: {name}')`, `IgnBdTopoArchiveError(f'IGN archive contains an unsupported link or special member: {name}')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_validate_archive_members`.

**Complete source-ordered implementation**

```python
def _validate_archive_members(archive: py7zr.SevenZipFile) -> None:
    infos = archive.list()
    if not infos:
        raise IgnBdTopoArchiveError("IGN archive contains no members")
    for info in infos:
        name = info.filename
        if not name or "\x00" in name:
            raise IgnBdTopoArchiveError("IGN archive contains an invalid member name")
        normalized_name = name.replace("\\", "/")
        posix_path = PurePosixPath(normalized_name)
        windows_path = PureWindowsPath(name)
        if (
            posix_path.is_absolute()
            or windows_path.is_absolute()
            or bool(windows_path.drive)
            or ".." in posix_path.parts
        ):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsafe member path: {name}"
            )
        if info.is_symlink or not (
            info.is_file or info.is_directory
        ):
            raise IgnBdTopoArchiveError(
                f"IGN archive contains an unsupported link or special member: {name}"
            )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `discover_ign_bdtopo_geopackage`

**Exact signature**

```python
def discover_ign_bdtopo_geopackage(root: Path) -> Path:
```

**Purpose**

Return the sole GeoPackage below an extracted package root.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
geopackages[0]

root
```

**Validation and exceptions**

- Guard with a raise path: `root.is_file()`.
- Guard with a raise path: `not root.is_dir()`.
- Guard with a raise path: `len(geopackages) != 1`.
- Explicit raise expressions: `IgnBdTopoArchiveError(f'Expected a GeoPackage, got: {root}')`, `IgnBdTopoArchiveError(f'Expected exactly one GeoPackage in the IGN package, found {len(geopackages)}')`, `IgnBdTopoArchiveError(f'Extraction directory does not exist: {root}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.is_file`, `root.is_dir`, `root.is_file`, `root.rglob`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `discover_ign_bdtopo_geopackage`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `discover_ign_bdtopo_geopackage`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `discover_ign_bdtopo_geopackage`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_geopackage_is_discovered_recursively` via `discover_ign_bdtopo_geopackage`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_multiple_geopackages_are_rejected_as_ambiguous` via `discover_ign_bdtopo_geopackage`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `list_ign_bdtopo_layers`

**Exact signature**

```python
def list_ign_bdtopo_layers(geopackage_path: Path) -> tuple[str, ...]:
```

**Purpose**

List every real layer name exposed by an IGN GeoPackage.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
names
```

**Validation and exceptions**

- Guard with a raise path: `not geopackage_path.is_file()`.
- Guard with a raise path: `not names or any((not name.strip() for name in names))`.
- Guard with a raise path: `len(set(names)) != len(names)`.
- Explicit raise expressions: `IgnBdTopoLayerError('GeoPackage exposes duplicate layer names')`, `IgnBdTopoLayerError('GeoPackage exposes no valid layer names')`, `IgnBdTopoLayerError(f'Cannot list layers in GeoPackage: {geopackage_path}')`, `IgnBdTopoLayerError(f'GeoPackage does not exist: {geopackage_path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `geopackage_path.is_file`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::discover_ign_bdtopo_layers` via `list_ign_bdtopo_layers`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `list_ign_bdtopo_layers`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_verify_unchanged_extraction` via `list_ign_bdtopo_layers`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_real_layer_names_are_listed_and_discovered` via `list_ign_bdtopo_layers`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_matching_layers`

**Exact signature**

```python
def _matching_layers(
    layer_names: tuple[str, ...], logical_config: IgnBdTopoLogicalLayerConfig
) -> tuple[str, ...]:
```

**Purpose**

Private `grid/source` helper for matching layers; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(matches)
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
- In-memory mutation: `matches`, `token_words`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::discover_ign_bdtopo_layers` via `_matching_layers`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_discover_department_coverage_layer` via `_matching_layers`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_discover_road_layer` via `_matching_layers`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `discover_ign_bdtopo_layers`

**Exact signature**

```python
def discover_ign_bdtopo_layers(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoLayerSelection:
```

**Purpose**

Resolve both configured logical classes without assuming exact casing.

**Return contract**

- Declared return annotation: `IgnBdTopoLayerSelection`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoLayerSelection(all_layer_names=layer_names, electric_lines_layer=electric_matches[0], transformation_posts_layer=post_matches[0])
```

**Validation and exceptions**

- Guard with a raise path: `len(electric_matches) != 1`.
- Guard with a raise path: `len(post_matches) != 1`.
- Guard with a raise path: `electric_matches[0] == post_matches[0]`.
- Explicit raise expressions: `IgnBdTopoLayerError('Electric-line and transformation-post discovery selected the same layer')`, `IgnBdTopoLayerError(f"Expected one unambiguous electric-line layer for '{config.logical_layers.electric_lines.class_label}', found {len(electric_matches)}: {electric_matches}")`, `IgnBdTopoLayerError(f"Expected one unambiguous transformation-post layer for '{config.logical_layers.transformation_posts.class_label}', found {len(post_matches)}: {post_matches}")`.

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

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `discover_ign_bdtopo_layers`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `discover_ign_bdtopo_layers`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `discover_ign_bdtopo_layers`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_real_layer_names_are_listed_and_discovered` via `discover_ign_bdtopo_layers`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_electric_line_layer_fails` via `discover_ign_bdtopo_layers`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_transformation_post_layer_fails` via `discover_ign_bdtopo_layers`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_electric_line_layers_fail` via `discover_ign_bdtopo_layers`.

**Complete source-ordered implementation**

```python
def discover_ign_bdtopo_layers(
    geopackage_path: Path,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoLayerSelection:
    """Resolve both configured logical classes without assuming exact casing."""

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_discover_department_coverage_layer`

**Exact signature**

```python
def _discover_department_coverage_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
```

**Purpose**

Private `grid/source` helper for discover department coverage layer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
matches[0]
```

**Validation and exceptions**

- Guard with a raise path: `len(matches) != 1`.
- Explicit raise expressions: `IgnBdTopoLayerError(f"Expected one unambiguous department coverage layer for '{config.coverage.department_layer.class_label}', found {len(matches)}: {matches}")`.

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

- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_department_coverage` via `_discover_department_coverage_layer`.
- direct call: `src/landscout/stages/assess_grid_coverage.py::_validate_configured_coverage_identity` via `_discover_department_coverage_layer`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `_discover_department_coverage_layer`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_discover_road_layer`

**Exact signature**

```python
def _discover_road_layer(
    layer_names: tuple[str, ...],
    config: IgnBdTopoSourceConfig,
) -> str:
```

**Purpose**

Private `grid/source` helper for discover road layer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
matches[0]
```

**Validation and exceptions**

- Guard with a raise path: `len(matches) != 1`.
- Explicit raise expressions: `IgnBdTopoLayerError(f"Expected one unambiguous road-segment layer for '{config.access.road_segments.class_label}', found {len(matches)}: {matches}")`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `_discover_road_layer`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_safe_relative_path`

**Exact signature**

```python
def _safe_relative_path(path: Path, root: Path) -> str:
```

**Purpose**

Private `grid/source` helper for safe relative path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
path.resolve().relative_to(root.resolve()).as_posix()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `IgnBdTopoArchiveError(f'Extracted GeoPackage escapes its extraction root: {path}')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_safe_relative_path`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_resolve_relative_path`

**Exact signature**

```python
def _resolve_relative_path(root: Path, relative_path: str) -> Path:
```

**Purpose**

Resolves relative path; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
candidate
```

**Validation and exceptions**

- Guard with a raise path: `not relative_path or posix_path.is_absolute() or windows_path.is_absolute() or bool(windows_path.drive) or ('..' in posix_path.parts)`.
- Explicit raise expressions: `IgnBdTopoArchiveError('Cached GeoPackage path escapes its extraction root')`, `IgnBdTopoArchiveError('Cached extraction metadata contains an unsafe GeoPackage path')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `_resolve_relative_path`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `_resolve_relative_path`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_resolve_relative_path`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_geopackage_integrity`

**Exact signature**

```python
def _geopackage_integrity(path: Path) -> tuple[int, str]:
```

**Purpose**

Private `grid/source` helper for geopackage integrity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[int, str]`.
- Every observed return expression is reproduced without truncation:
```python
(size_bytes, digest.hexdigest())
```

**Validation and exceptions**

- Guard with a raise path: `not path.is_file()`.
- Guard with a raise path: `size_bytes <= 0`.
- Explicit raise expressions: `IgnBdTopoArchiveError(f'Cannot inspect IGN GeoPackage: {path}')`, `IgnBdTopoArchiveError(f'Cannot read IGN GeoPackage: {path}')`, `IgnBdTopoArchiveError(f'IGN GeoPackage does not exist: {path}')`, `IgnBdTopoArchiveError(f'IGN GeoPackage is empty: {path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.is_file`, `path.open`, `path.stat`, `stream.read`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `digest.hexdigest`, `sha256`.
- Environment/process effects: none.
- In-memory mutation: `digest`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `_geopackage_integrity`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_verify_unchanged_extraction` via `_geopackage_integrity`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `_geopackage_integrity`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_geopackage_integrity`.

**Complete source-ordered implementation**

```python
def _geopackage_integrity(path: Path) -> tuple[int, str]:
    if not path.is_file():
        raise IgnBdTopoArchiveError(f"IGN GeoPackage does not exist: {path}")
    try:
        size_bytes = path.stat().st_size
    except OSError as error:
        raise IgnBdTopoArchiveError(
            f"Cannot inspect IGN GeoPackage: {path}"
        ) from error
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_valid_layer_inventory`

**Exact signature**

```python
def _valid_layer_inventory(value: object) -> bool:
```

**Purpose**

Private `grid/source` helper for valid layer inventory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
type(value) is tuple and bool(value) and all((isinstance(name, str) and bool(name) and (name == name.strip()) for name in value)) and (len(set(value)) == len(value))
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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `_valid_layer_inventory`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_extraction_envelope`

**Exact signature**

```python
def _validate_extraction_envelope(
    extraction: object,
) -> _VerifiedIgnExtraction:
```

**Purpose**

Bind one extraction envelope to its schema-v2 marker and current GPKG.

**Return contract**

- Declared return annotation: `_VerifiedIgnExtraction`.
- Every observed return expression is reproduced without truncation:
```python
_VerifiedIgnExtraction(extraction=extraction, metadata=metadata, geopackage_path=discovered_path)
```

**Validation and exceptions**

- Guard with a raise path: `type(extraction) is not IgnBdTopoExtraction`.
- Guard with a raise path: `type(extraction.archive) is not IgnBdTopoDownload`.
- Guard with a raise path: `extraction.spatial_role != SPATIAL_ROLE or extraction.archive.spatial_role != SPATIAL_ROLE`.
- Guard with a raise path: `not isinstance(extraction.archive.sha256, str) or re.fullmatch('[0-9a-f]{64}', extraction.archive.sha256) is None`.
- Guard with a raise path: `type(extraction.geopackage_size_bytes) is not int or extraction.geopackage_size_bytes <= 0`.
- Guard with a raise path: `not isinstance(extraction.geopackage_sha256, str) or re.fullmatch('[0-9a-f]{64}', extraction.geopackage_sha256) is None`.
- Guard with a raise path: `not isinstance(extraction.extraction_path, Path) or not isinstance(extraction.geopackage_path, Path)`.
- Guard with a raise path: `not marker_path.is_file()`.
- Guard with a raise path: `expected_path.resolve() != discovered_path.resolve() or extraction.geopackage_path.resolve() != discovered_path.resolve() or extraction.geopackage_filename != discovered_path.name`.
- Guard with a raise path: `metadata.archive_sha256 != extraction.archive.sha256`.
- Guard with a raise path: `metadata.spatial_role != extraction.spatial_role`.
- Guard with a raise path: `not _valid_layer_inventory(extraction.all_layer_names)`.
- Guard with a raise path: `metadata.all_layer_names != extraction.all_layer_names`.
- Guard with a raise path: `selected_roles != (metadata.electric_lines_layer, metadata.transformation_posts_layer)`.
- Guard with a raise path: `selected_roles[0] == selected_roles[1] or any((role not in extraction.all_layer_names for role in selected_roles))`.
- Guard with a raise path: `metadata.geopackage_size_bytes != extraction.geopackage_size_bytes or metadata.geopackage_sha256 != extraction.geopackage_sha256`.
- Guard with a raise path: `current_size != extraction.geopackage_size_bytes or current_sha != extraction.geopackage_sha256`.
- Guard with a raise path: `current_layers != extraction.all_layer_names`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN extraction physical integrity changed or is invalid')`, `TypeError('IGN extraction archive type is invalid')`, `TypeError('IGN extraction must be an exact IgnBdTopoExtraction')`, `TypeError('IGN extraction paths are invalid')`, `ValueError('IGN archive SHA256 lineage is invalid')`, `ValueError('IGN extraction GeoPackage SHA256 is invalid')`, `ValueError('IGN extraction GeoPackage integrity differs from metadata')`, `ValueError('IGN extraction GeoPackage path is inconsistent')`, `ValueError('IGN extraction GeoPackage size is invalid')`, `ValueError('IGN extraction archive lineage differs from metadata')`, `ValueError('IGN extraction electricity roles are invalid')`, `ValueError('IGN extraction electricity roles differ from metadata')`, `ValueError('IGN extraction layer inventory differs from metadata')`, `ValueError('IGN extraction layer inventory is invalid')`, `ValueError('IGN extraction lineage must be PROXY_GEOMETRY')`, `ValueError('IGN extraction spatial role differs from metadata')`, `ValueError('IGN physical GeoPackage integrity changed')`, `ValueError('IGN physical GeoPackage layer inventory changed')`, `ValueError('IGN schema-v2 extraction metadata is missing')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `marker_path.is_file`, `marker_path.read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `_validate_extraction_envelope`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `_validate_extraction_envelope`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_department_coverage` via `_validate_extraction_envelope`.

**Complete source-ordered implementation**

```python
def _validate_extraction_envelope(
    extraction: object,
) -> _VerifiedIgnExtraction:
    """Bind one extraction envelope to its schema-v2 marker and current GPKG."""

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
        if not marker_path.is_file():
            raise ValueError("IGN schema-v2 extraction metadata is missing")
        metadata = _ExtractionMetadata.model_validate_json(
            marker_path.read_text(encoding="utf-8")
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
        )
        if selected_roles != (
            metadata.electric_lines_layer,
            metadata.transformation_posts_layer,
        ):
            raise ValueError("IGN extraction electricity roles differ from metadata")
        if selected_roles[0] == selected_roles[1] or any(
            role not in extraction.all_layer_names for role in selected_roles
        ):
            raise ValueError("IGN extraction electricity roles are invalid")
        if (
            metadata.geopackage_size_bytes != extraction.geopackage_size_bytes
            or metadata.geopackage_sha256 != extraction.geopackage_sha256
        ):
            raise ValueError("IGN extraction GeoPackage integrity differs from metadata")
        current_size, current_sha = _geopackage_integrity(discovered_path)
        if (
            current_size != extraction.geopackage_size_bytes
            or current_sha != extraction.geopackage_sha256
        ):
            raise ValueError("IGN physical GeoPackage integrity changed")
        current_layers = list_ign_bdtopo_layers(discovered_path)
        if current_layers != extraction.all_layer_names:
            raise ValueError("IGN physical GeoPackage layer inventory changed")
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_verify_unchanged_extraction`

**Exact signature**

```python
def _verify_unchanged_extraction(context: _VerifiedIgnExtraction) -> None:
```

**Purpose**

Private `grid/source` helper for verify unchanged extraction; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `size != context.extraction.geopackage_size_bytes or digest != context.extraction.geopackage_sha256 or list_ign_bdtopo_layers(context.geopackage_path) != context.extraction.all_layer_names`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN physical GeoPackage changed during source layer loading')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_read_verified_layer_frames` via `_verify_unchanged_extraction`.

**Complete source-ordered implementation**

```python
def _verify_unchanged_extraction(context: _VerifiedIgnExtraction) -> None:
    size, digest = _geopackage_integrity(context.geopackage_path)
    if (
        size != context.extraction.geopackage_size_bytes
        or digest != context.extraction.geopackage_sha256
        or list_ign_bdtopo_layers(context.geopackage_path)
        != context.extraction.all_layer_names
    ):
        raise IgnBdTopoLayerError(
            "IGN physical GeoPackage changed during source layer loading"
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_read_layer_frame`

**Exact signature**

```python
def _read_layer_frame(geopackage_path: Path, layer_name: str) -> gpd.GeoDataFrame:
```

**Purpose**

Reads layer frame; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(layer_name, str) or not layer_name or layer_name != layer_name.strip()`.
- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame)`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN source layer name must be an exact string')`, `IgnBdTopoLayerError(f'Cannot load IGN GeoPackage layer: {layer_name}')`, `IgnBdTopoLayerError(f'IGN layer is not spatial: {layer_name}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `gpd.read_file`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_read_verified_layer_frames` via `_read_layer_frame`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_layer` via `_read_layer_frame`.

**Complete source-ordered implementation**

```python
def _read_layer_frame(geopackage_path: Path, layer_name: str) -> gpd.GeoDataFrame:
    if not isinstance(layer_name, str) or not layer_name or layer_name != layer_name.strip():
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_read_verified_layer_frames`

**Exact signature**

```python
def _read_verified_layer_frames(
    context: _VerifiedIgnExtraction,
    layer_names: tuple[str, ...],
) -> tuple[gpd.GeoDataFrame, ...]:
```

**Purpose**

Reads verified layer frames; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[gpd.GeoDataFrame, ...]`.
- Every observed return expression is reproduced without truncation:
```python
frames
```

**Validation and exceptions**

- Guard with a raise path: `type(layer_names) is not tuple or not layer_names`.
- Guard with a raise path: `len(set(layer_names)) != len(layer_names) or any((layer not in context.extraction.all_layer_names for layer in layer_names))`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN verified layer batch is invalid')`, `IgnBdTopoLayerError('IGN verified layer batch must be a non-empty tuple')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `_read_verified_layer_frames`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `_read_verified_layer_frames`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_department_coverage` via `_read_verified_layer_frames`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_layer_summary_contract`

**Exact signature**

```python
def _validate_layer_summary_contract(summary: object) -> IgnBdTopoLayerSummary:
```

**Purpose**

Rejects malformed or inconsistent layer summary contract; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnBdTopoLayerSummary`.
- Every observed return expression is reproduced without truncation:
```python
summary
```

**Validation and exceptions**

- Guard with a raise path: `type(summary) is not IgnBdTopoLayerSummary`.
- Guard with a raise path: `type(summary.columns) is not tuple or not summary.columns or any((not isinstance(column, str) or not column or column != column.strip() for column in summary.columns)) or (len(set(summary.columns)) != len(summary.columns))`.
- Guard with a raise path: `type(summary.dtypes) is not tuple or len(summary.dtypes) != len(summary.columns) or any((type(item) is not tuple or len(item) != 2 or any((not isinstance(value, str) or not value for value in item)) for item in summary.dtypes)) or (tuple((column for column, _ in summary.dtypes)) != summary.columns)`.
- Guard with a raise path: `type(summary.geometry_types) is not tuple or any((not isinstance(value, str) or not value or value != value.strip() for value in summary.geometry_types)) or summary.geometry_types != tuple(sorted(set(summary.geometry_types)))`.
- Guard with a raise path: `summary.spatial_role != SPATIAL_ROLE`.
- Guard with a raise path: `any((getattr(summary, name) > summary.feature_count for name in ('null_geometry_count', 'empty_geometry_count', 'invalid_geometry_count')))`.
- Guard with a raise path: `type(value) is not int or value < 0`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN layer summary columns are invalid')`, `IgnBdTopoLayerError('IGN layer summary dtypes are invalid')`, `IgnBdTopoLayerError('IGN layer summary geometry count is impossible')`, `IgnBdTopoLayerError('IGN layer summary geometry types are invalid')`, `IgnBdTopoLayerError('IGN layer summary spatial role is invalid')`, `IgnBdTopoLayerError('IGN layer summary type is invalid')`, `IgnBdTopoLayerError(f'IGN layer summary {name} must be a strict non-negative integer')`.

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

- import: `src/landscout/stages/normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`.
- import: `src/landscout/stages/normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_compare_layer_summary` via `_validate_layer_summary_contract`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_loaded_layer_from_frame` via `_validate_layer_summary_contract`.
- direct call: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `_validate_layer_summary_contract`.
- direct call: `src/landscout/stages/normalize_grid_ign.py::_validate_layer_summary` via `_validate_layer_summary_contract`.

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
            not isinstance(column, str)
            or not column
            or column != column.strip()
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_compare_layer_summary`

**Exact signature**

```python
def _compare_layer_summary(
    supplied: object,
    expected: IgnBdTopoLayerSummary,
) -> None:
```

**Purpose**

Private `grid/source` helper for compare layer summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `validated != expected`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN supplied layer summary differs from physical source')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_electricity_data` via `_compare_layer_summary`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_road_data` via `_compare_layer_summary`.

**Complete source-ordered implementation**

```python
def _compare_layer_summary(
    supplied: object,
    expected: IgnBdTopoLayerSummary,
) -> None:
    validated = _validate_layer_summary_contract(supplied)
    if validated != expected:
        raise IgnBdTopoLayerError("IGN supplied layer summary differs from physical source")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_compare_loaded_frame`

**Exact signature**

```python
def _compare_loaded_frame(
    supplied: object,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
```

**Purpose**

Private `grid/source` helper for compare loaded frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(supplied, gpd.GeoDataFrame)`.
- Guard with a raise path: `tuple(supplied.columns) != tuple(expected.columns)`.
- Guard with a raise path: `tuple((str(dtype) for dtype in supplied.dtypes)) != tuple((str(dtype) for dtype in expected.dtypes))`.
- Guard with a raise path: `type(supplied.index) is not type(expected.index)`.
- Guard with a raise path: `supplied.index.names != expected.index.names or not supplied.index.equals(expected.index)`.
- Guard with a raise path: `supplied.active_geometry_name != expected.active_geometry_name`.
- Guard with a raise path: `not supplied_crs.equals(expected_crs)`.
- Guard with a raise path: `geometry_name is None`.
- Guard with a raise path: `supplied.geometry.to_wkb(hex=True).tolist() != expected.geometry.to_wkb(hex=True).tolist()`.
- Guard with a raise path: `supplied.attrs != expected.attrs`.
- Explicit raise expressions: `AssertionError('CRS differs')`, `AssertionError('active geometry differs')`, `AssertionError('columns differ')`, `AssertionError('dtypes differ')`, `AssertionError('frame attributes differ')`, `AssertionError('geometry WKB differs')`, `AssertionError('geometry is missing')`, `AssertionError('index differs')`, `AssertionError('index type differs')`, `IgnBdTopoLayerError(f'IGN supplied {label} differs from freshly read physical source')`, `TypeError('supplied layer is not a GeoDataFrame')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `expected.geometry.to_wkb`, `expected.geometry.to_wkb(hex=True).tolist`, `supplied.geometry.to_wkb`, `supplied.geometry.to_wkb(hex=True).tolist`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_electricity_data` via `_compare_loaded_frame`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_road_data` via `_compare_loaded_frame`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_department_coverage` via `_compare_loaded_frame`.

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
        if supplied.geometry.to_wkb(hex=True).tolist() != expected.geometry.to_wkb(
            hex=True
        ).tolist():
            raise AssertionError("geometry WKB differs")
        if supplied.attrs != expected.attrs:
            raise AssertionError("frame attributes differ")
    except Exception as error:
        raise IgnBdTopoLayerError(
            f"IGN supplied {label} differs from freshly read physical source"
        ) from error
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_load_cached_extraction`

**Exact signature**

```python
def _load_cached_extraction(
    extraction_path: Path,
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoExtraction | None:
```

**Purpose**

Reads and validates cached extraction; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnBdTopoExtraction | None`.
- Every observed return expression is reproduced without truncation:
```python
None

IgnBdTopoExtraction(archive=download, extraction_path=extraction_path, geopackage_path=geopackage_path, geopackage_filename=geopackage_path.name, geopackage_size_bytes=metadata.geopackage_size_bytes, geopackage_sha256=metadata.geopackage_sha256, all_layer_names=selection.all_layer_names, electric_lines_layer=selection.electric_lines_layer, transformation_posts_layer=selection.transformation_posts_layer, cache_hit=True)

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
- Filesystem read: `extraction_path.is_dir`, `metadata_path.is_file`, `metadata_path.read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_load_cached_extraction`.

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
        metadata = _ExtractionMetadata.model_validate_json(
            metadata_path.read_text(encoding="utf-8")
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
        geopackage_size, geopackage_sha256 = _geopackage_integrity(
            geopackage_path
        )
        if (
            geopackage_size != metadata.geopackage_size_bytes
            or geopackage_sha256 != metadata.geopackage_sha256
        ):
            return None
        selection = discover_ign_bdtopo_layers(geopackage_path, config)
        if (
            selection.all_layer_names != metadata.all_layer_names
            or selection.electric_lines_layer != metadata.electric_lines_layer
            or selection.transformation_posts_layer
            != metadata.transformation_posts_layer
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_replace_directory`

**Exact signature**

```python
def _replace_directory(source: Path, target: Path) -> None:
```

**Purpose**

Private `grid/source` helper for replace directory; its complete implementation below is the authoritative behavioral contract.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_publish_extraction_directory` via `_replace_directory`.

**Complete source-ordered implementation**

```python
def _replace_directory(source: Path, target: Path) -> None:
    source.replace(target)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_remove_tree`

**Exact signature**

```python
def _remove_tree(path: Path) -> None:
```

**Purpose**

Private `grid/source` helper for remove tree; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.exists`, `path.is_dir`.
- Filesystem write: `path.unlink`, `shutil.rmtree`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_publish_extraction_directory` via `_remove_tree`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_remove_tree`.

**Complete source-ordered implementation**

```python
def _remove_tree(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_publish_extraction_directory`

**Exact signature**

```python
def _publish_extraction_directory(
    temporary_path: Path, extraction_path: Path
) -> None:
```

**Purpose**

Private `grid/source` helper for publish extraction directory; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `IgnBdTopoArchiveError('IGN extraction publication and rollback both failed')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `extraction_path.exists`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::extract_ign_bdtopo_archive` via `_publish_extraction_directory`.

**Complete source-ordered implementation**

```python
def _publish_extraction_directory(
    temporary_path: Path, extraction_path: Path
) -> None:
    backup_path = extraction_path.with_name(f"{extraction_path.name}.bak")
    _remove_tree(backup_path)
    extraction_existed = extraction_path.exists()
    if extraction_existed:
        _replace_directory(extraction_path, backup_path)
    try:
        _replace_directory(temporary_path, extraction_path)
    except OSError:
        try:
            if extraction_existed:
                _replace_directory(backup_path, extraction_path)
        except OSError as rollback_error:
            raise IgnBdTopoArchiveError(
                "IGN extraction publication and rollback both failed"
            ) from rollback_error
        raise
    else:
        _remove_tree(backup_path)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `extract_ign_bdtopo_archive`

**Exact signature**

```python
def extract_ign_bdtopo_archive(
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
    extraction_dir: Path | None = None,
) -> IgnBdTopoExtraction:
```

**Purpose**

Safely extract the package and resolve its required electricity layers.

**Return contract**

- Declared return annotation: `IgnBdTopoExtraction`.
- Every observed return expression is reproduced without truncation:
```python
cached

IgnBdTopoExtraction(archive=download, extraction_path=extraction_path, geopackage_path=published_geopackage, geopackage_filename=published_geopackage.name, geopackage_size_bytes=metadata.geopackage_size_bytes, geopackage_sha256=metadata.geopackage_sha256, all_layer_names=selection.all_layer_names, electric_lines_layer=selection.electric_lines_layer, transformation_posts_layer=selection.transformation_posts_layer, cache_hit=False)
```

**Validation and exceptions**

- Guard with a raise path: `integrity.sha256 != download.sha256`.
- Guard with a raise path: `extraction_path.exists() and (not extraction_path.is_dir())`.
- Explicit raise expressions: `IgnBdTopoArchiveError('Downloaded IGN archive checksum changed before extraction')`, `IgnBdTopoArchiveError(f'IGN archive extraction failed: {download.path}')`, `IgnBdTopoArchiveError(f'IGN extraction target exists and is not a directory: {extraction_path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `extraction_path.exists`, `extraction_path.is_dir`.
- Filesystem write: `(temporary_path / '.landscout-extraction.json').write_text`, `extraction_path.parent.mkdir`, `temporary_path.mkdir`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::_extracted_fixture` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_schema_v2_extraction_metadata_binds_physical_geopackage` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_same_size_geopackage_tamper_invalidates_extraction_cache` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_forged_extraction_metadata_never_returns_cache_hit` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_sha_is_not_trusted` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_size_is_not_trusted` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous` via `extract_ign_bdtopo_archive`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering` via `extract_ign_bdtopo_archive`.

**Complete source-ordered implementation**

```python
def extract_ign_bdtopo_archive(
    download: IgnBdTopoDownload,
    config: IgnBdTopoSourceConfig,
    extraction_dir: Path | None = None,
) -> IgnBdTopoExtraction:
    """Safely extract the package and resolve its required electricity layers."""

    integrity = validate_ign_bdtopo_archive(download.path, config)
    if integrity.sha256 != download.sha256:
        raise IgnBdTopoArchiveError(
            "Downloaded IGN archive checksum changed before extraction"
        )
    extraction_path = extraction_dir or (
        download.path.parent / "x" / download.sha256[:16]
    )
    if extraction_path.exists() and not extraction_path.is_dir():
        raise IgnBdTopoArchiveError(
            f"IGN extraction target exists and is not a directory: {extraction_path}"
        )
    cached = _load_cached_extraction(extraction_path, download, config)
    if cached is not None:
        return cached

    extraction_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = extraction_path.with_name(f"{extraction_path.name}.part")
    _remove_tree(temporary_path)
    temporary_path.mkdir(parents=True)
    try:
        with py7zr.SevenZipFile(download.path, mode="r") as archive:
            _validate_archive_members(archive)
            archive.extractall(path=temporary_path)

        geopackage_path = discover_ign_bdtopo_geopackage(temporary_path)
        selection = discover_ign_bdtopo_layers(geopackage_path, config)
        relative_path = _safe_relative_path(geopackage_path, temporary_path)
        geopackage_size, geopackage_sha256 = _geopackage_integrity(
            geopackage_path
        )
        metadata = _ExtractionMetadata(
            schema_version=2,
            archive_sha256=download.sha256,
            geopackage_relative_path=relative_path,
            geopackage_size_bytes=geopackage_size,
            geopackage_sha256=geopackage_sha256,
            all_layer_names=selection.all_layer_names,
            electric_lines_layer=selection.electric_lines_layer,
            transformation_posts_layer=selection.transformation_posts_layer,
            spatial_role="PROXY_GEOMETRY",
        )
        (temporary_path / ".landscout-extraction.json").write_text(
            metadata.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
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
            cache_hit=False,
        )
    except (ArchiveError, EOFError, OSError, ValueError) as error:
        raise IgnBdTopoArchiveError(
            f"IGN archive extraction failed: {download.path}"
        ) from error
    finally:
        _remove_tree(temporary_path)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_lambert93`

**Exact signature**

```python
def _validate_lambert93(crs_value: Any, layer_name: str) -> CRS:
```

**Purpose**

Rejects malformed or inconsistent lambert93; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
crs
```

**Validation and exceptions**

- Guard with a raise path: `crs_value is None`.
- Guard with a raise path: `not crs.is_projected`.
- Guard with a raise path: `not crs.equals(expected)`.
- Explicit raise expressions: `IgnBdTopoLayerError(f'IGN layer CRS is not Lambert-93 / EPSG:2154 compatible: {layer_name} ({crs.to_string()})')`, `IgnBdTopoLayerError(f'IGN layer CRS must be projected: {layer_name} ({crs.to_string()})')`, `IgnBdTopoLayerError(f'IGN layer has an unreadable CRS: {layer_name}')`, `IgnBdTopoLayerError(f'IGN layer has no CRS: {layer_name}')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_compare_loaded_frame` via `_validate_lambert93`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_loaded_layer_from_frame` via `_validate_lambert93`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_department_coverage_from_frame` via `_validate_lambert93`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_loaded_layer_from_frame`

**Exact signature**

```python
def _loaded_layer_from_frame(
    frame: gpd.GeoDataFrame,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
```

**Purpose**

Private `grid/source` helper for loaded layer from frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoLoadedLayer`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoLoadedLayer(data=frame, summary=summary)
```

**Validation and exceptions**

- Guard with a raise path: `geometry_name not in frame.columns`.
- Guard with a raise path: `frame.empty`.
- Explicit raise expressions: `IgnBdTopoLayerError(f'IGN layer contains no features: {layer_name}')`, `IgnBdTopoLayerError(f'IGN layer geometry column is missing: {layer_name}')`, `IgnBdTopoLayerError(f'IGN layer has no active geometry column: {layer_name}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `geometry.isna`, `geometry[non_null_mask].geom_type.dropna`, `geometry[non_null_mask].geom_type.dropna().unique`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_layer` via `_loaded_layer_from_frame`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `_loaded_layer_from_frame`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `_loaded_layer_from_frame`.

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
        raise IgnBdTopoLayerError(
            f"IGN layer geometry column is missing: {layer_name}"
        )
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
        sorted(str(value) for value in geometry[non_null_mask].geom_type.dropna().unique())
    )
    summary = IgnBdTopoLayerSummary(
        logical_name=logical_name,
        source_layer_name=layer_name,
        crs=crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in frame.dtypes.items()),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
    )
    _validate_layer_summary_contract(summary)
    return IgnBdTopoLoadedLayer(data=frame, summary=summary)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_layer`

**Exact signature**

```python
def load_ign_bdtopo_layer(
    geopackage_path: Path,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
```

**Purpose**

Load and validate one selected IGN layer without repairing geometry.

**Return contract**

- Declared return annotation: `IgnBdTopoLoadedLayer`.
- Every observed return expression is reproduced without truncation:
```python
_loaded_layer_from_frame(frame, layer_name, logical_name)
```

**Validation and exceptions**

- Guard with a raise path: `not geopackage_path.is_file()`.
- Guard with a raise path: `not layer_name.strip()`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN source layer name must not be empty')`, `IgnBdTopoLayerError(f'GeoPackage does not exist: {geopackage_path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `geopackage_path.is_file`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_layer_loader_retains_crs_counts_and_null_geometries` via `load_ign_bdtopo_layer`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_invalid_geometry_is_preserved_without_repair` via `load_ign_bdtopo_layer`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_geographic_crs_is_rejected` via `load_ign_bdtopo_layer`.

**Complete source-ordered implementation**

```python
def load_ign_bdtopo_layer(
    geopackage_path: Path,
    layer_name: str,
    logical_name: LogicalLayerName,
) -> IgnBdTopoLoadedLayer:
    """Load and validate one selected IGN layer without repairing geometry."""

    if not geopackage_path.is_file():
        raise IgnBdTopoLayerError(f"GeoPackage does not exist: {geopackage_path}")
    if not layer_name.strip():
        raise IgnBdTopoLayerError("IGN source layer name must not be empty")
    frame = _read_layer_frame(geopackage_path, layer_name)
    return _loaded_layer_from_frame(frame, layer_name, logical_name)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validated_layer_source_config`

**Exact signature**

```python
def _validated_layer_source_config(config: object) -> IgnBdTopoSourceConfig:
```

**Purpose**

Checks and returns canonical layer source config; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnBdTopoSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoSourceConfig.model_validate(config.model_dump(mode='python'))
```

**Validation and exceptions**

- Guard with a raise path: `type(config) is not IgnBdTopoSourceConfig`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN electricity source config is invalid')`, `TypeError('IGN electricity source config type is invalid')`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `_validated_layer_source_config`.

**Complete source-ordered implementation**

```python
def _validated_layer_source_config(config: object) -> IgnBdTopoSourceConfig:
    try:
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("IGN electricity source config type is invalid")
        return IgnBdTopoSourceConfig.model_validate(
            config.model_dump(mode="python")
        )
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise IgnBdTopoLayerError(
            "IGN electricity source config is invalid"
        ) from error
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_archive_config_lineage`

**Exact signature**

```python
def _validate_archive_config_lineage(
    extraction: object,
    config: IgnBdTopoSourceConfig,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent archive config lineage; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(extraction) is not IgnBdTopoExtraction`.
- Guard with a raise path: `type(archive) is not IgnBdTopoDownload`.
- Guard with a raise path: `type(archive.file_size) is not int or archive.file_size <= 0`.
- Guard with a raise path: `type(archive.official_checksum_validated) is not bool`.
- Guard with a raise path: `any((actual != expected for actual, expected in expected_values))`.
- Guard with a raise path: `config.expected_archive_size_bytes is not None and archive.file_size != config.expected_archive_size_bytes`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN electricity archive lineage differs from source config')`, `TypeError('IGN electricity archive size is invalid')`, `TypeError('IGN electricity archive type is invalid')`, `TypeError('IGN electricity extraction type is invalid')`, `TypeError('IGN electricity official-checksum state is invalid')`, `ValueError('IGN electricity archive lineage differs from source config')`, `ValueError('IGN electricity archive size differs from source config')`, `re-raise`.

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

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `_validate_archive_config_lineage`.

**Complete source-ordered implementation**

```python
def _validate_archive_config_lineage(
    extraction: object,
    config: IgnBdTopoSourceConfig,
) -> None:
    try:
        if type(extraction) is not IgnBdTopoExtraction:
            raise TypeError("IGN electricity extraction type is invalid")
        archive = extraction.archive
        if type(archive) is not IgnBdTopoDownload:
            raise TypeError("IGN electricity archive type is invalid")
        if type(archive.file_size) is not int or archive.file_size <= 0:
            raise TypeError("IGN electricity archive size is invalid")
        if type(archive.official_checksum_validated) is not bool:
            raise TypeError(
                "IGN electricity official-checksum state is invalid"
            )
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
            raise ValueError(
                "IGN electricity archive lineage differs from source config"
            )
        if (
            config.expected_archive_size_bytes is not None
            and archive.file_size != config.expected_archive_size_bytes
        ):
            raise ValueError(
                "IGN electricity archive size differs from source config"
            )
    except IgnBdTopoLayerError:
        raise
    except Exception as error:
        raise IgnBdTopoLayerError(
            "IGN electricity archive lineage differs from source config"
        ) from error
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_electricity`

**Exact signature**

```python
def load_ign_bdtopo_electricity(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Load the two electricity layers reproduced from the source config.

**Return contract**

- Declared return annotation: `IgnBdTopoElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoElectricityData(extraction=extraction, electric_lines=electric_lines.data, transformation_posts=transformation_posts.data, electric_lines_summary=electric_lines.summary, transformation_posts_summary=transformation_posts.summary)
```

**Validation and exceptions**

- Guard with a raise path: `configured_selection.all_layer_names != extraction.all_layer_names or configured_selection.electric_lines_layer != extraction.electric_lines_layer or configured_selection.transformation_posts_layer != extraction.transformation_posts_layer`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN electricity roles differ from the configured physical layers')`.

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

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_electricity_data` via `load_ign_bdtopo_electricity`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts` via `load_ign_bdtopo_electricity`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `load_ign_bdtopo_electricity`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering` via `load_ign_bdtopo_electricity`.

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
    configured_selection = discover_ign_bdtopo_layers(
        context.geopackage_path,
        validated_config,
    )
    if (
        configured_selection.all_layer_names != extraction.all_layer_names
        or configured_selection.electric_lines_layer
        != extraction.electric_lines_layer
        or configured_selection.transformation_posts_layer
        != extraction.transformation_posts_layer
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_roads`

**Exact signature**

```python
def load_ign_bdtopo_roads(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
```

**Purpose**

Load the configured factual road layer without filtering or repair.

**Return contract**

- Declared return annotation: `IgnBdTopoRoadData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoRoadData(extraction=extraction, road_segments=loaded.data, road_segments_summary=loaded.summary)
```

**Validation and exceptions**

- Guard with a raise path: `config.department_code != extraction.archive.department_code`.
- Guard with a raise path: `layer_name in {extraction.electric_lines_layer, extraction.transformation_posts_layer}`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN road config department does not match archive lineage')`, `IgnBdTopoLayerError('Road, electric-line, and transformation-post roles must use distinct layers')`.

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

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_road_data` via `load_ign_bdtopo_roads`.
- direct call: `tests/unit/test_normalize_access_ign.py::_with_alternate_road_layer` via `load_ign_bdtopo_roads`.
- direct call: `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer` via `load_ign_bdtopo_roads`.

**Complete source-ordered implementation**

```python
def load_ign_bdtopo_roads(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
    """Load the configured factual road layer without filtering or repair."""

    context = _validate_extraction_envelope(extraction)
    if config.department_code != extraction.archive.department_code:
        raise IgnBdTopoLayerError(
            "IGN road config department does not match archive lineage"
        )
    layer_name = _discover_road_layer(extraction.all_layer_names, config)
    if layer_name in {
        extraction.electric_lines_layer,
        extraction.transformation_posts_layer,
    }:
        raise IgnBdTopoLayerError(
            "Road, electric-line, and transformation-post roles must use distinct layers"
        )
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_department_coverage_from_frame`

**Exact signature**

```python
def _department_coverage_from_frame(
    extraction: IgnBdTopoExtraction,
    frame: gpd.GeoDataFrame,
    layer_name: str,
    department_field: str,
) -> IgnBdTopoDepartmentCoverage:
```

**Purpose**

Private `grid/source` helper for department coverage from frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoDepartmentCoverage`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoDepartmentCoverage(extraction=extraction, coverage=selected, summary=summary, source_provider=archive.provider, source_product=archive.product, source_department_code=archive.department_code, source_edition=archive.edition, source_product_version=archive.product_version, source_archive_sha256=archive.sha256, source_layer=layer_name)
```

**Validation and exceptions**

- Guard with a raise path: `geometry_name not in frame.columns`.
- Guard with a raise path: `frame.empty`.
- Guard with a raise path: `department_field not in frame.columns`.
- Guard with a raise path: `selected_count != 1`.
- Guard with a raise path: `selected_geometry.isna().any()`.
- Guard with a raise path: `selected_geometry.is_empty.any()`.
- Guard with a raise path: `not selected_geometry.is_valid.all()`.
- Guard with a raise path: `not selected_types <= {'Polygon', 'MultiPolygon'}`.
- Guard with a raise path: `collisions`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN department coverage attributes collide with lineage columns: ' + ', '.join(sorted(collisions)))`, `IgnBdTopoLayerError('Selected department coverage geometry is empty')`, `IgnBdTopoLayerError('Selected department coverage geometry is invalid')`, `IgnBdTopoLayerError('Selected department coverage geometry is null')`, `IgnBdTopoLayerError('Selected department coverage geometry must be Polygon or MultiPolygon')`, `IgnBdTopoLayerError(f'Configured department identity field is missing from IGN coverage layer: {department_field}')`, `IgnBdTopoLayerError(f'Expected exactly one authoritative department coverage feature for {archive.department_code}, found {selected_count}')`, `IgnBdTopoLayerError(f'IGN department coverage geometry column is missing: {layer_name}')`, `IgnBdTopoLayerError(f'IGN department coverage layer contains no features: {layer_name}')`, `IgnBdTopoLayerError(f'IGN department coverage layer has no active geometry: {layer_name}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `geometry.isna`, `geometry[non_null_mask].geom_type.dropna`, `geometry[non_null_mask].geom_type.dropna().unique`, `selected_geometry.geom_type.dropna`, `selected_geometry.is_empty.any`, `selected_geometry.is_valid.all`, `selected_geometry.isna`, `selected_geometry.isna().any`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `selected[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_department_coverage` via `_department_coverage_from_frame`.

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
            str(value)
            for value in geometry[non_null_mask].geom_type.dropna().unique()
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
            (str(column), str(dtype))
            for column, dtype in frame.dtypes.items()
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `load_ign_bdtopo_department_coverage`

**Exact signature**

```python
def load_ign_bdtopo_department_coverage(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
```

**Purpose**

Load the one authoritative configured department coverage feature.

**Return contract**

- Declared return annotation: `IgnBdTopoDepartmentCoverage`.
- Every observed return expression is reproduced without truncation:
```python
_department_coverage_from_frame(extraction, frame, layer_name, config.coverage.department_layer.department_code_field)
```

**Validation and exceptions**

- Guard with a raise path: `config.department_code != archive.department_code`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN coverage config department does not match archive lineage')`.

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

- re-export: `src/landscout/sources/__init__.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`.
- import: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)`.
- import: `tests/unit/test_ign_bdtopo_fr.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
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
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`.
- direct call: `src/landscout/sources/ign_bdtopo_fr.py::_revalidate_ign_bdtopo_department_coverage` via `load_ign_bdtopo_department_coverage`.
- direct call: `src/landscout/stages/assess_grid_coverage.py::assess_grid_coverage` via `load_ign_bdtopo_department_coverage`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `load_ign_bdtopo_department_coverage`.
- direct call: `tests/unit/test_assess_grid_coverage.py::_with_alternate_coverage_layer` via `load_ign_bdtopo_department_coverage`.
- direct call: `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` via `load_ign_bdtopo_department_coverage`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity` via `load_ign_bdtopo_department_coverage`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature` via `load_ign_bdtopo_department_coverage`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field` via `load_ign_bdtopo_department_coverage`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails` via `load_ign_bdtopo_department_coverage`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous` via `load_ign_bdtopo_department_coverage`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering` via `load_ign_bdtopo_department_coverage`.

**Complete source-ordered implementation**

```python
def load_ign_bdtopo_department_coverage(
    extraction: IgnBdTopoExtraction,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
    """Load the one authoritative configured department coverage feature."""

    context = _validate_extraction_envelope(extraction)
    archive = extraction.archive
    if config.department_code != archive.department_code:
        raise IgnBdTopoLayerError(
            "IGN coverage config department does not match archive lineage"
        )
    layer_name = _discover_department_coverage_layer(
        extraction.all_layer_names, config
    )
    (frame,) = _read_verified_layer_frames(context, (layer_name,))
    return _department_coverage_from_frame(
        extraction,
        frame,
        layer_name,
        config.coverage.department_layer.department_code_field,
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_revalidate_ign_bdtopo_electricity_data`

**Exact signature**

```python
def _revalidate_ign_bdtopo_electricity_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Fresh-read and exact-compare one supplied electricity source bundle.

**Return contract**

- Declared return annotation: `IgnBdTopoElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
fresh
```

**Validation and exceptions**

- Guard with a raise path: `type(source) is not IgnBdTopoElectricityData`.
- Guard with a raise path: `type(config) is not IgnBdTopoSourceConfig`.
- Guard with a raise path: `source.spatial_role != SPATIAL_ROLE`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN electricity source-complete revalidation failed')`, `TypeError('IGN electricity source config type is invalid')`, `TypeError('IGN electricity source type is invalid')`, `ValueError('IGN electricity source spatial role is invalid')`, `re-raise`.

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

- import: `src/landscout/stages/normalize_grid_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`.
- direct call: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `_revalidate_ign_bdtopo_electricity_data`.

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
        _compare_loaded_frame(source.electric_lines, fresh.electric_lines, "electric lines")
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_revalidate_ign_bdtopo_road_data`

**Exact signature**

```python
def _revalidate_ign_bdtopo_road_data(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoRoadData:
```

**Purpose**

Fresh-read and exact-compare one supplied road source bundle.

**Return contract**

- Declared return annotation: `IgnBdTopoRoadData`.
- Every observed return expression is reproduced without truncation:
```python
fresh
```

**Validation and exceptions**

- Guard with a raise path: `type(source) is not IgnBdTopoRoadData`.
- Guard with a raise path: `type(config) is not IgnBdTopoSourceConfig`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN road source-complete revalidation failed')`, `TypeError('IGN road source config type is invalid')`, `TypeError('IGN road source type is invalid')`, `re-raise`.

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

- import: `src/landscout/stages/normalize_access_ign.py::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`.
- direct call: `src/landscout/stages/normalize_access_ign.py::_normalize_ign_roads` via `_revalidate_ign_bdtopo_road_data`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_coverage_summary_contract`

**Exact signature**

```python
def _validate_coverage_summary_contract(
    summary: object,
) -> IgnBdTopoCoverageLayerSummary:
```

**Purpose**

Rejects malformed or inconsistent coverage summary contract; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnBdTopoCoverageLayerSummary`.
- Every observed return expression is reproduced without truncation:
```python
summary
```

**Validation and exceptions**

- Guard with a raise path: `type(summary) is not IgnBdTopoCoverageLayerSummary`.
- Guard with a raise path: `summary.selected_feature_count > summary.source_feature_count`.
- Guard with a raise path: `type(summary.columns) is not tuple or not summary.columns or any((not isinstance(value, str) or not value or value != value.strip() for value in summary.columns)) or (len(set(summary.columns)) != len(summary.columns))`.
- Guard with a raise path: `type(summary.dtypes) is not tuple or len(summary.dtypes) != len(summary.columns) or any((type(item) is not tuple or len(item) != 2 or any((not isinstance(value, str) or not value for value in item)) for item in summary.dtypes)) or (tuple((name for name, _ in summary.dtypes)) != summary.columns)`.
- Guard with a raise path: `type(summary.geometry_types) is not tuple or summary.geometry_types != tuple(sorted(set(summary.geometry_types))) or any((not isinstance(value, str) or not value for value in summary.geometry_types))`.
- Guard with a raise path: `summary.spatial_role != COVERAGE_SPATIAL_ROLE`.
- Guard with a raise path: `type(value) is not int or value < 0`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN coverage summary columns are invalid')`, `IgnBdTopoLayerError('IGN coverage summary counts are inconsistent')`, `IgnBdTopoLayerError('IGN coverage summary dtypes are invalid')`, `IgnBdTopoLayerError('IGN coverage summary geometry types are invalid')`, `IgnBdTopoLayerError('IGN coverage summary spatial role is invalid')`, `IgnBdTopoLayerError('IGN coverage summary type is invalid')`, `IgnBdTopoLayerError(f'IGN coverage summary {name} must be a strict non-negative integer')`.

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
        or any(not isinstance(value, str) or not value for value in summary.geometry_types)
    ):
        raise IgnBdTopoLayerError("IGN coverage summary geometry types are invalid")
    if summary.spatial_role != COVERAGE_SPATIAL_ROLE:
        raise IgnBdTopoLayerError("IGN coverage summary spatial role is invalid")
    return summary
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_revalidate_ign_bdtopo_department_coverage`

**Exact signature**

```python
def _revalidate_ign_bdtopo_department_coverage(
    source: object,
    config: IgnBdTopoSourceConfig,
) -> IgnBdTopoDepartmentCoverage:
```

**Purpose**

Fresh-read and exact-compare selected coverage with its physical layer.

**Return contract**

- Declared return annotation: `IgnBdTopoDepartmentCoverage`.
- Every observed return expression is reproduced without truncation:
```python
fresh
```

**Validation and exceptions**

- Guard with a raise path: `type(source) is not IgnBdTopoDepartmentCoverage`.
- Guard with a raise path: `type(config) is not IgnBdTopoSourceConfig`.
- Guard with a raise path: `source.summary != fresh.summary`.
- Guard with a raise path: `any((getattr(source, name) != getattr(fresh, name) for name in scalar_names))`.
- Explicit raise expressions: `IgnBdTopoLayerError('IGN coverage source-complete revalidation failed')`, `TypeError('IGN coverage source config type is invalid')`, `TypeError('IGN department coverage type is invalid')`, `ValueError('IGN coverage lineage differs from physical source')`, `ValueError('IGN coverage summary differs from physical source')`, `re-raise`.

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

- Configured source identity: exact provider/product/department/edition/version/projection/formats/URLs/checksum/size plus logical layer match rules.
- URL/safe transport: the revalidated configured HTTPS archive URL uses open_safe_https.
- Physical bytes/cache/archive: cache sidecar and current archive size/checksum/SHA are checked; 7z extraction and GeoPackage inventory/marker bind physical bytes and logical selections.
- Physical layer selection: config-aware loaders reproduce unique electric-line, transformation-post, road, and department-coverage roles from actual inventory instead of trusting supplied summary names.
- Result/later revalidation: immutable source objects carry frames/summaries/extraction; grid/road normalizers fresh-load and exact-compare configured physical results.

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
