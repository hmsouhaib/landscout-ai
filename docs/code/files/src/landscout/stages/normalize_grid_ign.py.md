# `src/landscout/stages/normalize_grid_ign.py`

## File identity

- Repository path: `src/landscout/stages/normalize_grid_ign.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: grid/source
- Responsibility: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.
- Source SHA256: `f287bded75c93f0a451e5819c7edcd99bdeb8e7a161069dbf99cd019e35ae290`

## 1. Purpose

Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **grid/source** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import re`
- `import unicodedata`
- `from dataclasses import dataclass`
- `from datetime import date, datetime`
- `from math import isfinite`
- `from numbers import Real`
- `from typing import Literal`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `from pandas.api.types import is_scalar`
- `from pydantic import HttpUrl, TypeAdapter, ValidationError`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.sources.ign_bdtopo_fr import (
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

## 4. Contract taxonomy

### A. Python constants

#### `SOURCE_PROVIDER`

```python
SOURCE_PROVIDER = "IGN"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `SOURCE_PRODUCT`

```python
SOURCE_PRODUCT = "BD_TOPO"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `SPATIAL_ROLE`

```python
SPATIAL_ROLE = "PROXY_GEOMETRY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_validate_grid` (value argument/reference).

#### `PACKAGE_LINEAGE_COLUMNS`

```python
PACKAGE_LINEAGE_COLUMNS = (
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `LINE_OUTPUT_COLUMNS`

```python
LINE_OUTPUT_COLUMNS = (
    "grid_feature_id",
    "grid_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    *PACKAGE_LINEAGE_COLUMNS,
    "voltage_raw",
    "voltage_status",
    "voltage_kv",
    "voltage_upper_bound_kv",
    "manager_name",
    "manager_siren",
    "asset_status_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_m",
    "spatial_role",
    "geometry_status",
    "geometry",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_valid_line_has_stable_identity_lineage_and_range_index` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_line_normalization_does_not_mutate_input_and_has_stable_columns` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::<module>` (import/re-export).

#### `TRANSFORMATION_POST_OUTPUT_COLUMNS`

```python
TRANSFORMATION_POST_OUTPUT_COLUMNS = (
    "grid_feature_id",
    "grid_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    *PACKAGE_LINEAGE_COLUMNS,
    "name",
    "name_status_raw",
    "importance_raw",
    "asset_status_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_m",
    "voltage_status",
    "voltage_kv",
    "spatial_role",
    "geometry_status",
    "geometry",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_valid_post_has_stable_lineage_and_no_voltage_inference` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::<module>` (import/re-export).

#### `LINE_SOURCE_FIELDS`

```python
LINE_SOURCE_FIELDS = frozenset(
    {
        "cleabs",
        "voltage",
        "gestionnaire",
        "siren_gestionnaire",
        "etat_de_l_objet",
        "sources",
        "identifiants_sources",
        "date_creation",
        "date_modification",
        "date_de_confirmation",
        "methode_d_acquisition_planimetrique",
        "precision_planimetrique",
        "geometry",
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` (value argument/reference).

#### `TRANSFORMATION_POST_SOURCE_FIELDS`

```python
TRANSFORMATION_POST_SOURCE_FIELDS = frozenset(
    {
        "cleabs",
        "toponyme",
        "statut_du_toponyme",
        "importance",
        "etat_de_l_objet",
        "sources",
        "identifiants_sources",
        "date_creation",
        "date_modification",
        "date_de_confirmation",
        "methode_d_acquisition_planimetrique",
        "precision_planimetrique",
        "geometry",
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` (value argument/reference).

#### `LINE_GEOMETRY_TYPES`

```python
LINE_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value argument/reference), `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` (value argument/reference).

#### `TRANSFORMATION_POST_GEOMETRY_TYPES`

```python
TRANSFORMATION_POST_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` (value argument/reference).

#### `_EXACT_VOLTAGE_PATTERN`

```python
_EXACT_VOLTAGE_PATTERN = re.compile(
    r"^(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE
)
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.

#### `_BELOW_VOLTAGE_PATTERN`

```python
_BELOW_VOLTAGE_PATTERN = re.compile(
    r"^<\s*(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE
)
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.

#### `_UNKNOWN_VOLTAGE_TERMS`

```python
_UNKNOWN_VOLTAGE_TERMS = frozenset(
    {"inconnu", "inconnue", "unknown", "non renseigne", "non renseignee"}
)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_DEENERGIZED_VOLTAGE_TERMS`

```python
_DEENERGIZED_VOLTAGE_TERMS = frozenset({"hors tension"})
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_DEPARTMENT_CODE_VALIDATOR`

```python
_DEPARTMENT_CODE_VALIDATOR = TypeAdapter(DepartmentCode)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_EDITION_VALIDATOR`

```python
_EDITION_VALIDATOR = TypeAdapter(EditionString)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_HTTP_URL_VALIDATOR`

```python
_HTTP_URL_VALIDATOR = TypeAdapter(HttpUrl)
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes.

#### `_SHA256_PATTERN`

```python
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.

#### `_IGN_PROVIDER_IDENTITIES`

```python
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institut national de l information geographique et forestiere",
        "institut national de l information geographique et forestiere ign",
    }
)
```

Module-level technical/source/policy constant consumed by the exact references below.


### B. Type aliases and closed domains

#### `VoltageStatus`

```python
VoltageStatus = Literal["EXACT", "BELOW", "UNKNOWN", "DEENERGIZED", "UNPARSED"]
```

IGN voltage parser result: EXACT, BELOW, UNKNOWN, DEENERGIZED, or UNPARSED. It is consumed by annotations or Pydantic validation in this module.

#### `GeometryStatus`

```python
GeometryStatus = Literal["VALID", "NULL", "EMPTY", "INVALID"]
```

Factual source-geometry quality state: VALID, NULL, EMPTY, or INVALID. It is consumed by annotations or Pydantic validation in this module.


### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `IgnGridNormalizationError`

**Purpose:** Raised when IGN electricity data cannot be normalized safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validated_lambert93` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_required_exact_string` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_source_context` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_input` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_valid_geometry_types` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalized_precision` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validated_geodataframe` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_layer_summary` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalized_identity` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_archive_identity` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_source_bundle` via `IgnGridNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `IgnGridNormalizationError`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_uppercase_sha256` via `pytest.raises(IgnGridNormalizationError, match='archive_sha256')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_grid_summary_requires_strict_structural_types` via `pytest.raises(IgnGridNormalizationError)`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_grid_archive_sha256_requires_canonical_lowercase` via `pytest.raises(IgnGridNormalizationError)`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_invalid_lineage_values` via `pytest.raises(IgnGridNormalizationError)`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_null_or_empty_line_cleabs_fails` via `pytest.raises(IgnGridNormalizationError, match='cleabs|null|empty')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_unsafe_source_id_is_rejected_without_rewriting` via `pytest.raises(IgnGridNormalizationError, match='cleabs|whitespace|control|:')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_duplicate_line_cleabs_fails` via `pytest.raises(IgnGridNormalizationError, match='unique')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_line_missing_or_wrong_crs_fails` via `pytest.raises(IgnGridNormalizationError, match='CRS|2154')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_missing_required_line_field_fails` via `pytest.raises(IgnGridNormalizationError, match=column)`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_invalid_line_precision_fails` via `pytest.raises(IgnGridNormalizationError, match='precision_planimetrique')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_duplicate_post_cleabs_fails` via `pytest.raises(IgnGridNormalizationError, match='unique')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_invalid_post_precision_fails` via `pytest.raises(IgnGridNormalizationError, match='precision_planimetrique')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_valid_polygon_or_point_is_rejected_as_electric_line` via `pytest.raises(IgnGridNormalizationError, match='geometry types')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_valid_line_or_point_is_rejected_as_transformation_post` via `pytest.raises(IgnGridNormalizationError, match='geometry types')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `pytest.raises(IgnGridNormalizationError, match='physical|fresh|source')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_incompatible_archive_identity` via `pytest.raises(IgnGridNormalizationError, match=message)`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_row_count_mismatch` via `pytest.raises(IgnGridNormalizationError, match='row count')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_layer_name_mismatch` via `pytest.raises(IgnGridNormalizationError, match='summary layer')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_wrong_logical_name` via `pytest.raises(IgnGridNormalizationError, match='logical name')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_crs_mismatch` via `pytest.raises(IgnGridNormalizationError, match='CRS|2154')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_forged_ordered_summary_schema` via `pytest.raises(IgnGridNormalizationError, match='schema|columns|dtype')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `pytest.raises(IgnGridNormalizationError, match='inventory|duplicate')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `pytest.raises(IgnGridNormalizationError, match='inventory|selected')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_colliding_electricity_roles` via `pytest.raises(IgnGridNormalizationError, match='same layer|distinct|role')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_counts_after_frame_mutation` via `pytest.raises(IgnGridNormalizationError, match='geometry summary')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_types_after_frame_mutation` via `pytest.raises(IgnGridNormalizationError, match='geometry summary')`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_any_spatial_role_mismatch` via `pytest.raises(IgnGridNormalizationError, match='PROXY_GEOMETRY')`.
- import/re-export: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`.

**Exact class source**

```python
class IgnGridNormalizationError(ValueError):
    """Raised when IGN electricity data cannot be normalized safely."""
```

### `_IgnGridSourceContext`

**Purpose:** Immutable source-package context persisted on every normalized row.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `source_layer` | `source_layer: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `department_code` | `department_code: str` | Stores `_IgnGridSourceContext`'s `department code` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `edition` | `edition: str` | Stores `_IgnGridSourceContext`'s `edition` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `product_version` | `product_version: str \| None` | Stores `_IgnGridSourceContext`'s `product version` value under exact annotation `str | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `download_timestamp` | `download_timestamp: str` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `archive_sha256` | `archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_url` | `source_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_source_context` via `_IgnGridSourceContext`.
- import/re-export: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    _IgnGridSourceContext as IgnGridSourceContext,
)`.

**Exact class source**

```python
class _IgnGridSourceContext:
    """Immutable source-package context persisted on every normalized row."""

    source_layer: str
    department_code: str
    edition: str
    product_version: str | None
    download_timestamp: str
    archive_sha256: str
    source_url: str
```

### `IgnVoltageNormalization`

**Purpose:** One source voltage value and its explicit normalized semantics.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `raw` | `raw: str \| None` | Stores `IgnVoltageNormalization`'s `raw` value under exact annotation `str | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `status` | `status: VoltageStatus` | Closed or validated `status` classification on `IgnVoltageNormalization`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `voltage_kv` | `voltage_kv: float \| None` | Stores `IgnVoltageNormalization`'s `voltage kv` value under exact annotation `float | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `voltage_upper_bound_kv` | `voltage_upper_bound_kv: float \| None` | Stores `IgnVoltageNormalization`'s `voltage upper bound kv` value under exact annotation `float | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::parse_ign_voltage` via `IgnVoltageNormalization`.

**Exact class source**

```python
class IgnVoltageNormalization:
    """One source voltage value and its explicit normalized semantics."""

    raw: str | None
    status: VoltageStatus
    voltage_kv: float | None
    voltage_upper_bound_kv: float | None
```

### `NormalizedIgnElectricityData`

**Purpose:** Immutable result containing normalized IGN electricity-line and transformation-post GeoDataFrames.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `electric_lines` | `electric_lines: gpd.GeoDataFrame` | Stores `NormalizedIgnElectricityData`'s `electric lines` value under exact annotation `gpd.GeoDataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `transformation_posts` | `transformation_posts: gpd.GeoDataFrame` | Closed or validated `transformation posts` classification on `NormalizedIgnElectricityData`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`.
- import/re-export: `src/landscout/stages/enrich_grid_proximity.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
)`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `NormalizedIgnElectricityData`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `NormalizedIgnElectricityData`.
- import/re-export: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.stages.normalize_grid_ign import NormalizedIgnElectricityData`.
- import/re-export: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`.

**Exact class source**

```python
class NormalizedIgnElectricityData:
    electric_lines: gpd.GeoDataFrame
    transformation_posts: gpd.GeoDataFrame
```


## 6. Functions and methods

### `_normalized_term`

**Exact signature**

```python
def _normalized_term(value: str) -> str:
```

**Purpose**

Private `grid/source` helper for normalized term; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
' '.join(without_accents.split())
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

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::parse_ign_voltage` via `_normalized_term`.

**Complete source-ordered implementation**

```python
def _normalized_term(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.strip().casefold())
    without_accents = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    return " ".join(without_accents.split())
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_positive_voltage`

**Exact signature**

```python
def _positive_voltage(match: re.Match[str]) -> float | None:
```

**Purpose**

Private `grid/source` helper for positive voltage; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float | None`.
- Every observed return expression is reproduced without truncation:
```python
value if value > 0 and isfinite(value) else None
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

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::parse_ign_voltage` via `_positive_voltage`.

**Complete source-ordered implementation**

```python
def _positive_voltage(match: re.Match[str]) -> float | None:
    value = float(match.group("value").replace(",", "."))
    return value if value > 0 and isfinite(value) else None
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_is_missing_scalar`

**Exact signature**

```python
def _is_missing_scalar(value: object) -> bool:
```

**Purpose**

Tests whether missing scalar; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
bool(pd.isna(value))

True

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

- direct call or construction: `src/landscout/stages/enrich_grid_proximity.py::_validate_tie_counts` via `_is_missing_scalar`.
- direct call or construction: `src/landscout/stages/enrich_road_proximity.py::_validate_distance_and_ties` via `_is_missing_scalar`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::parse_ign_voltage` via `_is_missing_scalar`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalized_precision` via `_is_missing_scalar`.

**Complete source-ordered implementation**

```python
def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    if not is_scalar(value):
        return False
    return bool(pd.isna(value))
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `parse_ign_voltage`

**Exact signature**

```python
def parse_ign_voltage(value: object) -> IgnVoltageNormalization:
```

**Purpose**

Parse scalar IGN voltage vocabulary without inventing precision. Unsupported list-like or array-like inputs are preserved as text and classified ``UNPARSED`` rather than reaching Pandas' ambiguous truth-value handling.

**Return contract**

- Declared return annotation: `IgnVoltageNormalization`.
- Every observed return expression is reproduced without truncation:
```python
IgnVoltageNormalization(raw, 'UNPARSED', None, None)

IgnVoltageNormalization(str(value), 'UNPARSED', None, None)

IgnVoltageNormalization(None, 'UNKNOWN', None, None)

IgnVoltageNormalization(raw, 'UNKNOWN', None, None)

IgnVoltageNormalization(raw, 'DEENERGIZED', None, None)

IgnVoltageNormalization(raw, 'BELOW', None, upper_bound)

IgnVoltageNormalization(raw, 'EXACT', exact, None)
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

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `parse_ign_voltage`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_exact_voltage_parser_is_generic_and_finite` via `parse_ign_voltage`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_bounded_voltage_is_generic_finite_and_not_exact` via `parse_ign_voltage`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_unknown_voltage_parser` via `parse_ign_voltage`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_deenergized_voltage_parser` via `parse_ign_voltage`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_unexpected_or_non_scalar_voltage_is_controlled_unparsed` via `parse_ign_voltage`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_invalid_or_overflowing_numeric_voltage_is_unparsed` via `parse_ign_voltage`.
- import/re-export: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`.

**Complete source-ordered implementation**

```python
def parse_ign_voltage(value: object) -> IgnVoltageNormalization:
    """Parse scalar IGN voltage vocabulary without inventing precision.

    Unsupported list-like or array-like inputs are preserved as text and
    classified ``UNPARSED`` rather than reaching Pandas' ambiguous truth-value
    handling.
    """

    if not is_scalar(value):
        return IgnVoltageNormalization(str(value), "UNPARSED", None, None)
    if _is_missing_scalar(value):
        return IgnVoltageNormalization(None, "UNKNOWN", None, None)

    raw = value if isinstance(value, str) else str(value)
    normalized = _normalized_term(raw)
    if normalized in _UNKNOWN_VOLTAGE_TERMS:
        return IgnVoltageNormalization(raw, "UNKNOWN", None, None)
    if normalized in _DEENERGIZED_VOLTAGE_TERMS:
        return IgnVoltageNormalization(raw, "DEENERGIZED", None, None)

    below_match = _BELOW_VOLTAGE_PATTERN.fullmatch(normalized)
    if below_match is not None:
        upper_bound = _positive_voltage(below_match)
        if upper_bound is not None:
            return IgnVoltageNormalization(raw, "BELOW", None, upper_bound)

    exact_match = _EXACT_VOLTAGE_PATTERN.fullmatch(normalized)
    if exact_match is not None:
        exact = _positive_voltage(exact_match)
        if exact is not None:
            return IgnVoltageNormalization(raw, "EXACT", exact, None)

    return IgnVoltageNormalization(raw, "UNPARSED", None, None)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validated_lambert93`

**Exact signature**

```python
def _validated_lambert93(crs_value: object, label: str) -> CRS:
```

**Purpose**

Checks and returns canonical lambert93; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
source_crs
```

**Validation and exceptions**

- Guard with a raise path: `crs_value is None`.
- Guard with a raise path: `not source_crs.is_projected or not source_crs.equals(expected_crs)`.
- Explicit raise expressions: `IgnGridNormalizationError(f'{label} CRS is required')`, `IgnGridNormalizationError(f'{label} CRS is unreadable')`, `IgnGridNormalizationError(f'{label} must use EPSG:2154')`.

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

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_coverage_summary` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_source_coverage` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_frame` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_input` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_layer_summary` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_archive_identity` via `_validated_lambert93`.

**Complete source-ordered implementation**

```python
def _validated_lambert93(crs_value: object, label: str) -> CRS:
    if crs_value is None:
        raise IgnGridNormalizationError(f"{label} CRS is required")
    try:
        source_crs = CRS.from_user_input(crs_value)
    except Exception as error:
        raise IgnGridNormalizationError(f"{label} CRS is unreadable") from error
    expected_crs = CRS.from_epsg(2154)
    if not source_crs.is_projected or not source_crs.equals(expected_crs):
        raise IgnGridNormalizationError(f"{label} must use EPSG:2154")
    return source_crs
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_required_exact_string`

**Exact signature**

```python
def _required_exact_string(value: object, label: str) -> str:
```

**Purpose**

Private `grid/source` helper for required exact string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value.strip()`.
- Guard with a raise path: `value != value.strip()`.
- Explicit raise expressions: `IgnGridNormalizationError(f'IGN source context {label} must be a string')`, `IgnGridNormalizationError(f'IGN source context {label} must not contain edge whitespace')`.

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

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_context` via `_required_exact_string`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `_required_exact_string`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_source_context` via `_required_exact_string`.

**Complete source-ordered implementation**

```python
def _required_exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnGridNormalizationError(f"IGN source context {label} must be a string")
    if value != value.strip():
        raise IgnGridNormalizationError(
            f"IGN source context {label} must not contain edge whitespace"
        )
    return value
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_source_context`

**Exact signature**

```python
def _validate_source_context(context: _IgnGridSourceContext) -> None:
```

**Purpose**

Rejects malformed or inconsistent source context; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `validated_department != department_code`.
- Guard with a raise path: `validated_edition != edition`.
- Guard with a raise path: `timestamp.tzinfo is None or timestamp.utcoffset() is None`.
- Guard with a raise path: `_SHA256_PATTERN.fullmatch(archive_sha256) is None`.
- Explicit raise expressions: `IgnGridNormalizationError('IGN source context archive_sha256 must contain 64 hexadecimal characters')`, `IgnGridNormalizationError('IGN source context department_code is invalid')`, `IgnGridNormalizationError('IGN source context department_code must not be rewritten')`, `IgnGridNormalizationError('IGN source context download_timestamp must be a valid ISO datetime')`, `IgnGridNormalizationError('IGN source context download_timestamp must be timezone-aware')`, `IgnGridNormalizationError('IGN source context edition must be a valid ISO calendar date')`, `IgnGridNormalizationError('IGN source context edition must not be rewritten')`, `IgnGridNormalizationError('IGN source context source_url must be a valid HTTP(S) URL')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_SHA256_PATTERN.fullmatch`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_road_frame` via `_validate_source_context`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_validate_source_context`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_validate_source_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_accepts_supported_department_codes` via `grid_normalization._validate_source_context`.
- property/attribute access: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_accepts_supported_department_codes` via `grid_normalization._validate_source_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_invalid_lineage_values` via `grid_normalization._validate_source_context`.
- property/attribute access: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_invalid_lineage_values` via `grid_normalization._validate_source_context`.

**Complete source-ordered implementation**

```python
def _validate_source_context(context: _IgnGridSourceContext) -> None:
    _required_exact_string(context.source_layer, "source_layer")
    department_code = _required_exact_string(
        context.department_code, "department_code"
    )
    edition = _required_exact_string(context.edition, "edition")
    download_timestamp = _required_exact_string(
        context.download_timestamp, "download_timestamp"
    )
    archive_sha256 = _required_exact_string(
        context.archive_sha256, "archive_sha256"
    )
    source_url = _required_exact_string(context.source_url, "source_url")

    try:
        validated_department = _DEPARTMENT_CODE_VALIDATOR.validate_python(
            department_code
        )
    except ValidationError as error:
        raise IgnGridNormalizationError(
            "IGN source context department_code is invalid"
        ) from error
    if validated_department != department_code:
        raise IgnGridNormalizationError(
            "IGN source context department_code must not be rewritten"
        )

    try:
        validated_edition = _EDITION_VALIDATOR.validate_python(edition)
        date.fromisoformat(validated_edition)
    except (ValidationError, ValueError) as error:
        raise IgnGridNormalizationError(
            "IGN source context edition must be a valid ISO calendar date"
        ) from error
    if validated_edition != edition:
        raise IgnGridNormalizationError(
            "IGN source context edition must not be rewritten"
        )

    try:
        timestamp = datetime.fromisoformat(download_timestamp)
    except ValueError as error:
        raise IgnGridNormalizationError(
            "IGN source context download_timestamp must be a valid ISO datetime"
        ) from error
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise IgnGridNormalizationError(
            "IGN source context download_timestamp must be timezone-aware"
        )

    if _SHA256_PATTERN.fullmatch(archive_sha256) is None:
        raise IgnGridNormalizationError(
            "IGN source context archive_sha256 must contain 64 hexadecimal characters"
        )

    try:
        _HTTP_URL_VALIDATOR.validate_python(source_url)
    except ValidationError as error:
        raise IgnGridNormalizationError(
            "IGN source context source_url must be a valid HTTP(S) URL"
        ) from error

    if context.product_version is not None:
        _required_exact_string(context.product_version, "product_version")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_input`

**Exact signature**

```python
def _validate_input(
    frame: gpd.GeoDataFrame,
    required_columns: frozenset[str],
    source_layer: str,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent input; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `missing`.
- Guard with a raise path: `frame.active_geometry_name != 'geometry'`.
- Guard with a raise path: `identifiers.isna().any()`.
- Guard with a raise path: `any((not isinstance(identifier, str) for identifier in identifiers.tolist()))`.
- Guard with a raise path: `identifiers.str.strip().eq('').any()`.
- Guard with a raise path: `identifiers.map(lambda value: value != value.strip()).any()`.
- Guard with a raise path: `identifiers.str.contains(':', regex=False).any()`.
- Guard with a raise path: `identifiers.map(lambda value: any((unicodedata.category(character) == 'Cc' for character in value))).any()`.
- Guard with a raise path: `identifiers.duplicated().any()`.
- Explicit raise expressions: `IgnGridNormalizationError(f"IGN {source_layer} cleabs values must not contain ':'")`, `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must be strings')`, `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must be unique')`, `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must not be empty')`, `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must not be null')`, `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must not contain control characters')`, `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must not contain edge whitespace')`, `IgnGridNormalizationError(f'IGN {source_layer} requires an active geometry column')`, `IgnGridNormalizationError(f'Missing required IGN {source_layer} columns: {formatted}')`.

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

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_validate_input`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_validate_input`.

**Complete source-ordered implementation**

```python
def _validate_input(
    frame: gpd.GeoDataFrame,
    required_columns: frozenset[str],
    source_layer: str,
) -> None:
    missing = required_columns - set(frame.columns)
    if missing:
        formatted = ", ".join(sorted(missing))
        raise IgnGridNormalizationError(
            f"Missing required IGN {source_layer} columns: {formatted}"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnGridNormalizationError(
            f"IGN {source_layer} requires an active geometry column"
        )
    _validated_lambert93(frame.crs, f"IGN {source_layer}")

    identifiers = frame["cleabs"]
    if identifiers.isna().any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not be null"
        )
    if any(not isinstance(identifier, str) for identifier in identifiers.tolist()):
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must be strings"
        )
    if identifiers.str.strip().eq("").any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not be empty"
        )
    if identifiers.map(lambda value: value != value.strip()).any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not contain edge whitespace"
        )
    if identifiers.str.contains(":", regex=False).any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not contain ':'"
        )
    if identifiers.map(
        lambda value: any(unicodedata.category(character) == "Cc" for character in value)
    ).any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not contain control characters"
        )
    if identifiers.duplicated().any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must be unique"
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_geometry_status`

**Exact signature**

```python
def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
```

**Purpose**

Private `grid/source` helper for geometry status; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
status
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `geometry.isna`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `status.loc[empty_mask]`, `status.loc[invalid_mask]`, `status.loc[null_mask]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_road_frame` via `_geometry_status`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_geometry_status`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_geometry_status`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_lines` via `_geometry_status`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_posts` via `_geometry_status`.

**Complete source-ordered implementation**

```python
def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
    status = pd.Series("VALID", index=geometry.index, dtype="object")
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    status.loc[null_mask] = "NULL"
    status.loc[empty_mask] = "EMPTY"
    status.loc[invalid_mask] = "INVALID"
    return status
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_geometry_summary`

**Exact signature**

```python
def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
```

**Purpose**

Private `grid/source` helper for geometry summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[int, int, int, tuple[str, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(int(null_mask.sum()), int(empty_mask.sum()), int(invalid_mask.sum()), geometry_types)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `geometry.isna`, `geometry[~null_mask].geom_type.dropna`, `geometry[~null_mask].geom_type.dropna().unique`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `_geometry_summary`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_layer_summary` via `_geometry_summary`.

**Complete source-ordered implementation**

```python
def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    geometry_types = tuple(
        sorted(str(value) for value in geometry[~null_mask].geom_type.dropna().unique())
    )
    return (
        int(null_mask.sum()),
        int(empty_mask.sum()),
        int(invalid_mask.sum()),
        geometry_types,
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_valid_geometry_types`

**Exact signature**

```python
def _validate_valid_geometry_types(
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    allowed_types: frozenset[str],
    source_layer: str,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent valid geometry types; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `unsupported`.
- Explicit raise expressions: `IgnGridNormalizationError(f'IGN {source_layer} has unsupported VALID geometry types: ' + ', '.join(unsupported))`.

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

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_validate_valid_geometry_types`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_validate_valid_geometry_types`.

**Complete source-ordered implementation**

```python
def _validate_valid_geometry_types(
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    allowed_types: frozenset[str],
    source_layer: str,
) -> None:
    valid_types = frame.loc[status == "VALID", "geometry"].geom_type
    unsupported = sorted(set(valid_types.dropna()) - allowed_types)
    if unsupported:
        raise IgnGridNormalizationError(
            f"IGN {source_layer} has unsupported VALID geometry types: "
            + ", ".join(unsupported)
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalized_precision`

**Exact signature**

```python
def _normalized_precision(
    source: pd.Series,
    source_layer: str,
) -> pd.Series:
```

**Purpose**

Private `grid/source` helper for normalized precision; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
pd.Series(normalized, index=source.index, dtype='float64')
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Real)`.
- Guard with a raise path: `not isfinite(numeric) or numeric < 0`.
- Explicit raise expressions: `IgnGridNormalizationError(f'IGN {source_layer} precision_planimetrique must be finite and >= 0')`, `IgnGridNormalizationError(f'IGN {source_layer} precision_planimetrique must be numeric or null')`.

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

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_normalized_precision`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_normalized_precision`.

**Complete source-ordered implementation**

```python
def _normalized_precision(
    source: pd.Series,
    source_layer: str,
) -> pd.Series:
    normalized: list[float] = []
    for value in source.tolist():
        if _is_missing_scalar(value):
            normalized.append(float("nan"))
            continue
        if isinstance(value, bool) or not isinstance(value, Real):
            raise IgnGridNormalizationError(
                f"IGN {source_layer} precision_planimetrique must be numeric or null"
            )
        numeric = float(value)
        if not isfinite(numeric) or numeric < 0:
            raise IgnGridNormalizationError(
                f"IGN {source_layer} precision_planimetrique must be finite and >= 0"
            )
        normalized.append(numeric)
    return pd.Series(normalized, index=source.index, dtype="float64")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_base_output`

**Exact signature**

```python
def _base_output(
    frame: gpd.GeoDataFrame,
    *,
    feature_type: str,
    context: _IgnGridSourceContext,
) -> pd.DataFrame:
```

**Purpose**

Private `grid/source` helper for base output; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
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
- In-memory mutation: `output['grid_feature_id']`, `output['grid_feature_type']`, `output['source_archive_sha256']`, `output['source_department_code']`, `output['source_download_timestamp']`, `output['source_edition']`, `output['source_feature_id']`, `output['source_layer']`, `output['source_product']`, `output['source_product_version']`, `output['source_provider']`, `output['source_url']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_base_output`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_base_output`.

**Complete source-ordered implementation**

```python
def _base_output(
    frame: gpd.GeoDataFrame,
    *,
    feature_type: str,
    context: _IgnGridSourceContext,
) -> pd.DataFrame:
    source_ids = frame["cleabs"].copy()
    output = pd.DataFrame(index=frame.index.copy())
    output["grid_feature_id"] = source_ids.map(
        lambda identifier: f"IGN_BDTOPO:{feature_type}:{identifier}"
    )
    output["grid_feature_type"] = feature_type
    output["source_provider"] = SOURCE_PROVIDER
    output["source_product"] = SOURCE_PRODUCT
    output["source_layer"] = context.source_layer
    output["source_feature_id"] = source_ids
    output["source_department_code"] = context.department_code
    output["source_edition"] = context.edition
    output["source_product_version"] = context.product_version
    output["source_download_timestamp"] = context.download_timestamp
    output["source_archive_sha256"] = context.archive_sha256
    output["source_url"] = context.source_url
    return output
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validated_geodataframe`

**Exact signature**

```python
def _validated_geodataframe(
    output: pd.DataFrame,
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    columns: tuple[str, ...],
) -> gpd.GeoDataFrame:
```

**Purpose**

Checks and returns canonical geodataframe; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
normalized
```

**Validation and exceptions**

- Guard with a raise path: `normalized_ids.isna().any() or normalized_ids.duplicated().any()`.
- Guard with a raise path: `len(normalized) != len(frame)`.
- Guard with a raise path: `not isinstance(normalized.index, pd.RangeIndex)`.
- Explicit raise expressions: `IgnGridNormalizationError('IGN normalization changed the row count')`, `IgnGridNormalizationError('IGN normalized output must use a RangeIndex')`, `IgnGridNormalizationError('Normalized IGN grid_feature_id values must be non-null and unique')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `frame.geometry.copy`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output['geometry']`, `output['geometry_status']`, `output['spatial_role']`.
- Input mutation: `output['geometry']`, `output['geometry_status']`, `output['spatial_role']`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_validated_geodataframe`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_validated_geodataframe`.

**Complete source-ordered implementation**

```python
def _validated_geodataframe(
    output: pd.DataFrame,
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    columns: tuple[str, ...],
) -> gpd.GeoDataFrame:
    output["spatial_role"] = SPATIAL_ROLE
    output["geometry_status"] = status
    output["geometry"] = frame.geometry.copy()
    normalized = gpd.GeoDataFrame(
        output.loc[:, list(columns)], geometry="geometry", crs=frame.crs
    )
    normalized_ids = normalized["grid_feature_id"]
    if normalized_ids.isna().any() or normalized_ids.duplicated().any():
        raise IgnGridNormalizationError(
            "Normalized IGN grid_feature_id values must be non-null and unique"
        )
    if len(normalized) != len(frame):
        raise IgnGridNormalizationError("IGN normalization changed the row count")
    if not isinstance(normalized.index, pd.RangeIndex):
        raise IgnGridNormalizationError("IGN normalized output must use a RangeIndex")
    return normalized
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalize_ign_electric_lines`

**Exact signature**

```python
def _normalize_ign_electric_lines(
    lines: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Normalize one discovered IGN electric-line layer.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_validated_geodataframe(output, working, status, LINE_OUTPUT_COLUMNS)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_geometry_status`, `_validate_valid_geometry_types`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output['asset_status_raw']`, `output['manager_name']`, `output['manager_siren']`, `output['planimetric_acquisition_method']`, `output['planimetric_precision_m']`, `output['source_confirmed_at']`, `output['source_created_at']`, `output['source_identifiers_raw']`, `output['source_modified_at']`, `output['source_name_raw']`, `output['voltage_kv']`, `output['voltage_raw']`, `output['voltage_status']`, `output['voltage_upper_bound_kv']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `_normalize_ign_electric_lines`.
- import/re-export: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    _normalize_ign_electric_lines as normalize_ign_electric_lines,
)`.

**Complete source-ordered implementation**

```python
def _normalize_ign_electric_lines(
    lines: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
    """Normalize one discovered IGN electric-line layer."""

    _validate_source_context(context)
    _validate_input(lines, LINE_SOURCE_FIELDS, context.source_layer)
    working = lines.reset_index(drop=True).copy()
    status = _geometry_status(working.geometry)
    _validate_valid_geometry_types(
        working, status, LINE_GEOMETRY_TYPES, context.source_layer
    )
    precision = _normalized_precision(
        working["precision_planimetrique"], context.source_layer
    )
    output = _base_output(
        working,
        feature_type="ELECTRIC_LINE",
        context=context,
    )
    parsed = [parse_ign_voltage(value) for value in working["voltage"].tolist()]
    output["voltage_raw"] = [result.raw for result in parsed]
    output["voltage_status"] = [result.status for result in parsed]
    output["voltage_kv"] = [result.voltage_kv for result in parsed]
    output["voltage_upper_bound_kv"] = [
        result.voltage_upper_bound_kv for result in parsed
    ]
    output["manager_name"] = working["gestionnaire"].copy()
    output["manager_siren"] = working["siren_gestionnaire"].copy()
    output["asset_status_raw"] = working["etat_de_l_objet"].copy()
    output["source_name_raw"] = working["sources"].copy()
    output["source_identifiers_raw"] = working["identifiants_sources"].copy()
    output["source_created_at"] = working["date_creation"].copy()
    output["source_modified_at"] = working["date_modification"].copy()
    output["source_confirmed_at"] = working["date_de_confirmation"].copy()
    output["planimetric_acquisition_method"] = working[
        "methode_d_acquisition_planimetrique"
    ].copy()
    output["planimetric_precision_m"] = precision
    return _validated_geodataframe(
        output, working, status, LINE_OUTPUT_COLUMNS
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalize_ign_transformation_posts`

**Exact signature**

```python
def _normalize_ign_transformation_posts(
    posts: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Normalize one discovered IGN transformation-post proxy layer.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_validated_geodataframe(output, working, status, TRANSFORMATION_POST_OUTPUT_COLUMNS)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_geometry_status`, `_validate_valid_geometry_types`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output['asset_status_raw']`, `output['importance_raw']`, `output['name']`, `output['name_status_raw']`, `output['planimetric_acquisition_method']`, `output['planimetric_precision_m']`, `output['source_confirmed_at']`, `output['source_created_at']`, `output['source_identifiers_raw']`, `output['source_modified_at']`, `output['source_name_raw']`, `output['voltage_kv']`, `output['voltage_status']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `_normalize_ign_transformation_posts`.
- import/re-export: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    _normalize_ign_transformation_posts as normalize_ign_transformation_posts,
)`.

**Complete source-ordered implementation**

```python
def _normalize_ign_transformation_posts(
    posts: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
    """Normalize one discovered IGN transformation-post proxy layer."""

    _validate_source_context(context)
    _validate_input(posts, TRANSFORMATION_POST_SOURCE_FIELDS, context.source_layer)
    working = posts.reset_index(drop=True).copy()
    status = _geometry_status(working.geometry)
    _validate_valid_geometry_types(
        working,
        status,
        TRANSFORMATION_POST_GEOMETRY_TYPES,
        context.source_layer,
    )
    precision = _normalized_precision(
        working["precision_planimetrique"], context.source_layer
    )
    output = _base_output(
        working,
        feature_type="TRANSFORMATION_POST",
        context=context,
    )
    output["name"] = working["toponyme"].copy()
    output["name_status_raw"] = working["statut_du_toponyme"].copy()
    output["importance_raw"] = working["importance"].copy()
    output["asset_status_raw"] = working["etat_de_l_objet"].copy()
    output["source_name_raw"] = working["sources"].copy()
    output["source_identifiers_raw"] = working["identifiants_sources"].copy()
    output["source_created_at"] = working["date_creation"].copy()
    output["source_modified_at"] = working["date_modification"].copy()
    output["source_confirmed_at"] = working["date_de_confirmation"].copy()
    output["planimetric_acquisition_method"] = working[
        "methode_d_acquisition_planimetrique"
    ].copy()
    output["planimetric_precision_m"] = precision
    output["voltage_status"] = "UNKNOWN"
    output["voltage_kv"] = float("nan")
    return _validated_geodataframe(
        output,
        working,
        status,
        TRANSFORMATION_POST_OUTPUT_COLUMNS,
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_layer_summary`

**Exact signature**

```python
def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    *,
    expected_layer: str,
    expected_logical_name: str,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent layer summary; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `summary.source_layer_name != expected_layer`.
- Guard with a raise path: `summary.logical_name != expected_logical_name`.
- Guard with a raise path: `summary.feature_count != len(frame)`.
- Guard with a raise path: `summary.columns != observed_columns or summary.dtypes != observed_dtypes`.
- Guard with a raise path: `frame.active_geometry_name != 'geometry'`.
- Guard with a raise path: `not frame_crs.equals(summary_crs)`.
- Guard with a raise path: `observed_geometry != expected_geometry`.
- Explicit raise expressions: `IgnGridNormalizationError(f'IGN {expected_logical_name} geometry summary does not match frame')`, `IgnGridNormalizationError(f'IGN {expected_logical_name} requires an active geometry column')`, `IgnGridNormalizationError(f'IGN {expected_logical_name} summary CRS does not match frame')`, `IgnGridNormalizationError(f'IGN {expected_logical_name} summary has the wrong logical name')`, `IgnGridNormalizationError(f'IGN {expected_logical_name} summary layer does not match extraction')`, `IgnGridNormalizationError(f'IGN {expected_logical_name} summary row count does not match frame')`, `IgnGridNormalizationError(f'IGN {expected_logical_name} summary schema columns or dtypes do not match frame')`, `IgnGridNormalizationError(f'IGN {expected_logical_name} summary schema contract is invalid')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_geometry_summary`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_validate_layer_summary`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_validate_layer_summary`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_source_bundle` via `_validate_layer_summary`.

**Complete source-ordered implementation**

```python
def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    *,
    expected_layer: str,
    expected_logical_name: str,
) -> None:
    try:
        _validate_layer_summary_contract(summary)
    except Exception as error:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary schema contract is invalid"
        ) from error
    if summary.source_layer_name != expected_layer:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary layer does not match extraction"
        )
    if summary.logical_name != expected_logical_name:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary has the wrong logical name"
        )
    if summary.feature_count != len(frame):
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary row count does not match frame"
        )
    observed_columns = tuple(str(column) for column in frame.columns)
    observed_dtypes = tuple(
        (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
    )
    if summary.columns != observed_columns or summary.dtypes != observed_dtypes:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary schema columns or dtypes "
            "do not match frame"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} requires an active geometry column"
        )
    frame_crs = _validated_lambert93(frame.crs, f"IGN {expected_logical_name}")
    summary_crs = _validated_lambert93(
        summary.crs, f"IGN {expected_logical_name} summary"
    )
    if not frame_crs.equals(summary_crs):
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} summary CRS does not match frame"
        )
    observed_geometry = _geometry_summary(frame)
    expected_geometry = (
        summary.null_geometry_count,
        summary.empty_geometry_count,
        summary.invalid_geometry_count,
        summary.geometry_types,
    )
    if observed_geometry != expected_geometry:
        raise IgnGridNormalizationError(
            f"IGN {expected_logical_name} geometry summary does not match frame"
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalized_identity`

**Exact signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

**Purpose**

Private `grid/source` helper for normalized identity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
' '.join(re.findall('[a-z0-9]+', without_accents))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value.strip()`.
- Explicit raise expressions: `IgnGridNormalizationError(f'IGN archive {label} must be a string')`.

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

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_source_coverage` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_configured_coverage_identity` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_archive_identity` via `_normalized_identity`.

**Complete source-ordered implementation**

```python
def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnGridNormalizationError(f"IGN archive {label} must be a string")
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    without_accents = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    return " ".join(re.findall(r"[a-z0-9]+", without_accents))
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_archive_identity`

**Exact signature**

```python
def _validate_archive_identity(source: IgnBdTopoElectricityData) -> None:
```

**Purpose**

Rejects malformed or inconsistent archive identity; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `provider not in _IGN_PROVIDER_IDENTITIES`.
- Guard with a raise path: `product.replace(' ', '') != 'bdtopo'`.
- Explicit raise expressions: `IgnGridNormalizationError('IGN archive product is incompatible with the BD TOPO normalizer')`, `IgnGridNormalizationError('IGN archive provider is incompatible with the IGN normalizer')`.

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

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_source_bundle` via `_validate_archive_identity`.

**Complete source-ordered implementation**

```python
def _validate_archive_identity(source: IgnBdTopoElectricityData) -> None:
    archive = source.extraction.archive
    provider = _normalized_identity(archive.provider, "provider")
    product = _normalized_identity(archive.product, "product")
    if provider not in _IGN_PROVIDER_IDENTITIES:
        raise IgnGridNormalizationError(
            "IGN archive provider is incompatible with the IGN normalizer"
        )
    if product.replace(" ", "") != "bdtopo":
        raise IgnGridNormalizationError(
            "IGN archive product is incompatible with the BD TOPO normalizer"
        )
    _validated_lambert93(archive.projection, "IGN archive projection")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_source_bundle`

**Exact signature**

```python
def _validate_source_bundle(source: IgnBdTopoElectricityData) -> None:
```

**Purpose**

Rejects malformed or inconsistent source bundle; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(source) is not IgnBdTopoElectricityData`.
- Guard with a raise path: `type(source.extraction) is not IgnBdTopoExtraction`.
- Guard with a raise path: `type(source.extraction.archive) is not IgnBdTopoDownload`.
- Guard with a raise path: `type(source.electric_lines_summary) is not IgnBdTopoLayerSummary or type(source.transformation_posts_summary) is not IgnBdTopoLayerSummary`.
- Guard with a raise path: `not isinstance(source.electric_lines, gpd.GeoDataFrame) or not isinstance(source.transformation_posts, gpd.GeoDataFrame)`.
- Guard with a raise path: `type(layer_names) is not tuple or not layer_names or any((not isinstance(name, str) or not name or name != name.strip() for name in layer_names)) or (len(set(layer_names)) != len(layer_names))`.
- Guard with a raise path: `any((layer not in layer_names for layer in selected_layers))`.
- Guard with a raise path: `selected_layers[0] == selected_layers[1]`.
- Guard with a raise path: `any((role != SPATIAL_ROLE for role in roles))`.
- Explicit raise expressions: `IgnGridNormalizationError('IGN electricity archive type is invalid')`, `IgnGridNormalizationError('IGN electricity extraction type is invalid')`, `IgnGridNormalizationError('IGN electricity layer inventory must be a unique non-empty tuple')`, `IgnGridNormalizationError('IGN electricity layers must be GeoDataFrames')`, `IgnGridNormalizationError('IGN electricity roles must use distinct layers, not the same layer')`, `IgnGridNormalizationError('IGN electricity selected layer is absent from the layer inventory')`, `IgnGridNormalizationError('IGN electricity source must be IgnBdTopoElectricityData')`, `IgnGridNormalizationError('IGN electricity summary type is invalid')`, `IgnGridNormalizationError('IGN source bundle spatial roles must all be PROXY_GEOMETRY')`.

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

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_ign_roads` via `_validate_source_bundle`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `_validate_source_bundle`.

**Complete source-ordered implementation**

```python
def _validate_source_bundle(source: IgnBdTopoElectricityData) -> None:
    if type(source) is not IgnBdTopoElectricityData:
        raise IgnGridNormalizationError(
            "IGN electricity source must be IgnBdTopoElectricityData"
        )
    if type(source.extraction) is not IgnBdTopoExtraction:
        raise IgnGridNormalizationError("IGN electricity extraction type is invalid")
    if type(source.extraction.archive) is not IgnBdTopoDownload:
        raise IgnGridNormalizationError("IGN electricity archive type is invalid")
    if type(source.electric_lines_summary) is not IgnBdTopoLayerSummary or type(
        source.transformation_posts_summary
    ) is not IgnBdTopoLayerSummary:
        raise IgnGridNormalizationError("IGN electricity summary type is invalid")
    if not isinstance(source.electric_lines, gpd.GeoDataFrame) or not isinstance(
        source.transformation_posts, gpd.GeoDataFrame
    ):
        raise IgnGridNormalizationError(
            "IGN electricity layers must be GeoDataFrames"
        )
    extraction = source.extraction
    layer_names = extraction.all_layer_names
    if (
        type(layer_names) is not tuple
        or not layer_names
        or any(
            not isinstance(name, str) or not name or name != name.strip()
            for name in layer_names
        )
        or len(set(layer_names)) != len(layer_names)
    ):
        raise IgnGridNormalizationError(
            "IGN electricity layer inventory must be a unique non-empty tuple"
        )
    selected_layers = (
        extraction.electric_lines_layer,
        extraction.transformation_posts_layer,
    )
    if any(layer not in layer_names for layer in selected_layers):
        raise IgnGridNormalizationError(
            "IGN electricity selected layer is absent from the layer inventory"
        )
    if selected_layers[0] == selected_layers[1]:
        raise IgnGridNormalizationError(
            "IGN electricity roles must use distinct layers, not the same layer"
        )
    _validate_archive_identity(source)
    roles = (
        source.spatial_role,
        source.extraction.spatial_role,
        source.extraction.archive.spatial_role,
        source.electric_lines_summary.spatial_role,
        source.transformation_posts_summary.spatial_role,
    )
    if any(role != SPATIAL_ROLE for role in roles):
        raise IgnGridNormalizationError(
            "IGN source bundle spatial roles must all be PROXY_GEOMETRY"
        )
    _validate_layer_summary(
        source.electric_lines,
        source.electric_lines_summary,
        expected_layer=source.extraction.electric_lines_layer,
        expected_logical_name="electric_lines",
    )
    _validate_layer_summary(
        source.transformation_posts,
        source.transformation_posts_summary,
        expected_layer=source.extraction.transformation_posts_layer,
        expected_logical_name="transformation_posts",
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_source_context`

**Exact signature**

```python
def _source_context(
    source: IgnBdTopoElectricityData,
    source_layer: str,
) -> _IgnGridSourceContext:
```

**Purpose**

Private `grid/source` helper for source context; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_IgnGridSourceContext`.
- Every observed return expression is reproduced without truncation:
```python
_IgnGridSourceContext(source_layer=source_layer, department_code=archive.department_code, edition=archive.edition, product_version=archive.product_version, download_timestamp=archive.download_timestamp, archive_sha256=archive.sha256, source_url=archive.source_url)
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

- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `_source_context`.

**Complete source-ordered implementation**

```python
def _source_context(
    source: IgnBdTopoElectricityData,
    source_layer: str,
) -> _IgnGridSourceContext:
    archive = source.extraction.archive
    return _IgnGridSourceContext(
        source_layer=source_layer,
        department_code=archive.department_code,
        edition=archive.edition,
        product_version=archive.product_version,
        download_timestamp=archive.download_timestamp,
        archive_sha256=archive.sha256,
        source_url=archive.source_url,
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `normalize_ign_electricity`

**Exact signature**

```python
def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnElectricityData:
```

**Purpose**

Validate and normalize a complete already-loaded IGN source bundle.

**Return contract**

- Declared return annotation: `NormalizedIgnElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
NormalizedIgnElectricityData(electric_lines=_normalize_ign_electric_lines(source.electric_lines, line_context), transformation_posts=_normalize_ign_transformation_posts(source.transformation_posts, post_context))
```

**Validation and exceptions**

- Guard with a raise path: `type(config) is not IgnBdTopoSourceConfig`.
- Explicit raise expressions: `IgnGridNormalizationError('IGN electricity source cannot be normalized safely')`, `IgnGridNormalizationError('IGN electricity source config type is invalid')`, `re-raise`.

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

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`.
- direct call or construction: `src/landscout/stages/enrich_grid_proximity.py::enrich_parcel_grid_proximity` via `normalize_ign_electricity`.
- import/re-export: `src/landscout/stages/enrich_grid_proximity.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
)`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_supported_package_api_keeps_high_level_normalization` via `stages.normalize_ign_electricity`.
- property/attribute access: `tests/unit/test_normalize_grid_ign.py::test_supported_package_api_keeps_high_level_normalization` via `stages.normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_grid_summary_requires_strict_structural_types` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_grid_archive_sha256_requires_canonical_lowercase` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_path_uses_discovered_layer_names_and_archive_lineage` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_source_complete_grid_validation_does_not_mutate_supplied_frames` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_incompatible_archive_identity` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_row_count_mismatch` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_layer_name_mismatch` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_wrong_logical_name` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_crs_mismatch` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_forged_ordered_summary_schema` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_colliding_electricity_roles` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_counts_after_frame_mutation` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_types_after_frame_mutation` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_any_spatial_role_mismatch` via `normalize_ign_electricity`.
- import/re-export: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    normalize_ign_electricity as _normalize_ign_electricity,
)`.

**Complete source-ordered implementation**

```python
def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnElectricityData:
    """Validate and normalize a complete already-loaded IGN source bundle."""

    try:
        if type(config) is not IgnBdTopoSourceConfig:
            raise IgnGridNormalizationError(
                "IGN electricity source config type is invalid"
            )
        _validate_source_bundle(source)
        _revalidate_ign_bdtopo_electricity_data(source, config)
        line_context = _source_context(
            source, source.extraction.electric_lines_layer
        )
        post_context = _source_context(
            source, source.extraction.transformation_posts_layer
        )
        return NormalizedIgnElectricityData(
            electric_lines=_normalize_ign_electric_lines(
                source.electric_lines, line_context
            ),
            transformation_posts=_normalize_ign_transformation_posts(
                source.transformation_posts, post_context
            ),
        )
    except IgnGridNormalizationError:
        raise
    except Exception as error:
        raise IgnGridNormalizationError(
            "IGN electricity source cannot be normalized safely"
        ) from error
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.


## 7. Data contracts

### Frame-preservation and semantic notes

- `VoltageStatus` values (`EXACT`, `BELOW`, `UNKNOWN`, `DEENERGIZED`, `UNPARSED`) and `GeometryStatus` values (`VALID`, `NULL`, `EMPTY`, `INVALID`) are closed vocabularies, never column names.
- `LINE_OUTPUT_COLUMNS` and `TRANSFORMATION_POST_OUTPUT_COLUMNS` below are the canonical ordered factual GeoDataFrame schemas. Raw source attributes are copied; voltage fields are derived factual parsing; `spatial_role` is proxy lineage, not capacity evidence.

### `PACKAGE_LINEAGE_COLUMNS` — canonical or derived frame-column schema

```python
PACKAGE_LINEAGE_COLUMNS = (
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `source_product_version` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_download_timestamp` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 6 | `source_url` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `LINE_OUTPUT_COLUMNS` — canonical or derived frame-column schema

```python
LINE_OUTPUT_COLUMNS = (
    "grid_feature_id",
    "grid_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    *PACKAGE_LINEAGE_COLUMNS,
    "voltage_raw",
    "voltage_status",
    "voltage_kv",
    "voltage_upper_bound_kv",
    "manager_name",
    "manager_siren",
    "asset_status_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_m",
    "spatial_role",
    "geometry_status",
    "geometry",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `grid_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `grid_feature_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `source_provider` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_product` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 7 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `source_product_version` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `source_download_timestamp` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 12 | `source_url` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `voltage_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `voltage_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 15 | `voltage_kv` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 16 | `voltage_upper_bound_kv` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 17 | `manager_name` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 18 | `manager_siren` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 19 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 20 | `source_name_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 21 | `source_identifiers_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 22 | `source_created_at` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 23 | `source_modified_at` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 24 | `source_confirmed_at` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 25 | `planimetric_acquisition_method` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 26 | `planimetric_precision_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 27 | `spatial_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 28 | `geometry_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 29 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |

### `TRANSFORMATION_POST_OUTPUT_COLUMNS` — canonical or derived frame-column schema

```python
TRANSFORMATION_POST_OUTPUT_COLUMNS = (
    "grid_feature_id",
    "grid_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    *PACKAGE_LINEAGE_COLUMNS,
    "name",
    "name_status_raw",
    "importance_raw",
    "asset_status_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_m",
    "voltage_status",
    "voltage_kv",
    "spatial_role",
    "geometry_status",
    "geometry",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `grid_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `grid_feature_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `source_provider` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_product` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 7 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `source_product_version` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `source_download_timestamp` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 12 | `source_url` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `name` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `name_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `importance_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `source_name_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 18 | `source_identifiers_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 19 | `source_created_at` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 20 | `source_modified_at` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 21 | `source_confirmed_at` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 22 | `planimetric_acquisition_method` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 23 | `planimetric_precision_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 24 | `voltage_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 25 | `voltage_kv` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 26 | `spatial_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 27 | `geometry_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 28 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |

### `LINE_SOURCE_FIELDS` — required input frame fields (unordered when stored as a set)

```python
LINE_SOURCE_FIELDS = frozenset(
    {
        "cleabs",
        "voltage",
        "gestionnaire",
        "siren_gestionnaire",
        "etat_de_l_objet",
        "sources",
        "identifiants_sources",
        "date_creation",
        "date_modification",
        "date_de_confirmation",
        "methode_d_acquisition_planimetrique",
        "precision_planimetrique",
        "geometry",
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `cleabs` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `date_creation` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `date_de_confirmation` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `date_modification` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `etat_de_l_objet` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 7 | `gestionnaire` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `identifiants_sources` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `methode_d_acquisition_planimetrique` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `precision_planimetrique` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `siren_gestionnaire` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `sources` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `voltage` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `TRANSFORMATION_POST_SOURCE_FIELDS` — required input frame fields (unordered when stored as a set)

```python
TRANSFORMATION_POST_SOURCE_FIELDS = frozenset(
    {
        "cleabs",
        "toponyme",
        "statut_du_toponyme",
        "importance",
        "etat_de_l_objet",
        "sources",
        "identifiants_sources",
        "date_creation",
        "date_modification",
        "date_de_confirmation",
        "methode_d_acquisition_planimetrique",
        "precision_planimetrique",
        "geometry",
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `cleabs` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `date_creation` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `date_de_confirmation` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `date_modification` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `etat_de_l_objet` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 7 | `identifiants_sources` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `importance` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `methode_d_acquisition_planimetrique` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `precision_planimetrique` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `sources` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `statut_du_toponyme` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `toponyme` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.


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
