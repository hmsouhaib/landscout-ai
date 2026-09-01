# `src/landscout/stages/normalize_grid_ign.py`

## File identity

- Repository path: `src/landscout/stages/normalize_grid_ign.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.
- Source SHA256: `e89baab63d48517ce48f3fbdf03602673786ca33f1671f3abf9cb366d57948a0`

## 1. STEP 7F.1A.4 contract delta

- Consumes fresh config-bound electricity objects and rows returned by independent source-complete revalidation.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `SOURCE_PROVIDER`

- Category: module constant or closed domain.
- Exact declaration:

```python
SOURCE_PROVIDER = "IGN"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SOURCE_PRODUCT`

- Category: module constant or closed domain.
- Exact declaration:

```python
SOURCE_PRODUCT = "BD_TOPO"
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

### `VoltageStatus`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
VoltageStatus = Literal["EXACT", "BELOW", "UNKNOWN", "DEENERGIZED", "UNPARSED"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `GeometryStatus`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
GeometryStatus = Literal["VALID", "NULL", "EMPTY", "INVALID"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PACKAGE_LINEAGE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `source_department_code`
  - `source_edition`
  - `source_product_version`
  - `source_download_timestamp`
  - `source_archive_sha256`
  - `source_url`

### `LINE_OUTPUT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`
  - value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_line_has_stable_identity_lineage_and_range_index` via `LINE_OUTPUT_COLUMNS`
  - value/type reference: `tests.unit.test_normalize_grid_ign::test_line_normalization_does_not_mutate_input_and_has_stable_columns` via `LINE_OUTPUT_COLUMNS`

### `TRANSFORMATION_POST_OUTPUT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`
  - value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_post_has_stable_lineage_and_no_voltage_inference` via `TRANSFORMATION_POST_OUTPUT_COLUMNS`

### `LINE_SOURCE_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `TRANSFORMATION_POST_SOURCE_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `LINE_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
LINE_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `TRANSFORMATION_POST_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
TRANSFORMATION_POST_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_EXACT_VOLTAGE_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_EXACT_VOLTAGE_PATTERN = re.compile(r"^(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_BELOW_VOLTAGE_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_BELOW_VOLTAGE_PATTERN = re.compile(
    r"^<\s*(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_UNKNOWN_VOLTAGE_TERMS`

- Category: module constant or closed domain.
- Exact declaration:

```python
_UNKNOWN_VOLTAGE_TERMS = frozenset(
    {"inconnu", "inconnue", "unknown", "non renseigne", "non renseignee"}
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_DEENERGIZED_VOLTAGE_TERMS`

- Category: module constant or closed domain.
- Exact declaration:

```python
_DEENERGIZED_VOLTAGE_TERMS = frozenset({"hors tension"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_DEPARTMENT_CODE_VALIDATOR`

- Category: module constant or closed domain.
- Exact declaration:

```python
_DEPARTMENT_CODE_VALIDATOR = TypeAdapter(DepartmentCode)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_EDITION_VALIDATOR`

- Category: module constant or closed domain.
- Exact declaration:

```python
_EDITION_VALIDATOR = TypeAdapter(EditionString)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_HTTP_URL_VALIDATOR`

- Category: module constant or closed domain.
- Exact declaration:

```python
_HTTP_URL_VALIDATOR = TypeAdapter(HttpUrl)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SHA256_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_IGN_PROVIDER_IDENTITIES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institut national de l information geographique et forestiere",
        "institut national de l information geographique et forestiere ign",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `IgnGridNormalizationError`

**Source purpose:** Raised when IGN electricity data cannot be normalized safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`
- constructor call: `landscout.stages.normalize_grid_ign::_validated_lambert93` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_validated_lambert93` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_required_exact_string` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_required_exact_string` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_validate_source_context` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_context` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_validate_input` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_input` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_validate_valid_geometry_types` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_valid_geometry_types` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_normalized_precision` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalized_precision` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_validated_geodataframe` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_validated_geodataframe` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_validate_layer_summary` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_layer_summary` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_normalized_identity` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalized_identity` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_validate_archive_identity` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_archive_identity` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `IgnGridNormalizationError`
- constructor call: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `IgnGridNormalizationError`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `IgnGridNormalizationError`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_uppercase_sha256` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_grid_summary_requires_strict_structural_types` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_grid_archive_sha256_requires_canonical_lowercase` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_invalid_lineage_values` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_null_or_empty_line_cleabs_fails` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_unsafe_source_id_is_rejected_without_rewriting` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_duplicate_line_cleabs_fails` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_missing_or_wrong_crs_fails` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_missing_required_line_field_fails` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_invalid_line_precision_fails` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_duplicate_post_cleabs_fails` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_invalid_post_precision_fails` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_polygon_or_point_is_rejected_as_electric_line` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_line_or_point_is_rejected_as_transformation_post` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_incompatible_archive_identity` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_archive_identity_requires_exact_pinned_strings` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_row_count_mismatch` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_layer_name_mismatch` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_wrong_logical_name` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_crs_mismatch` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_forged_ordered_summary_schema` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_colliding_electricity_roles` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_counts_after_frame_mutation` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_types_after_frame_mutation` via `IgnGridNormalizationError`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_any_spatial_role_mismatch` via `IgnGridNormalizationError`

**Exact class source**

```python
class IgnGridNormalizationError(ValueError):
    """Raised when IGN electricity data cannot be normalized safely."""
```

### `_IgnGridSourceContext`

**Source purpose:** Immutable source-package context persisted on every normalized row.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `source_layer` | `str` | `required` | `source_layer: str` |
| `department_code` | `str` | `required` | `department_code: str` |
| `edition` | `str` | `required` | `edition: str` |
| `product_version` | `str \| None` | `required` | `product_version: str \| None` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `archive_sha256` | `str` | `required` | `archive_sha256: str` |
| `source_url` | `str` | `required` | `source_url: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_context` via `_IgnGridSourceContext`
- value/type reference: `landscout.stages.normalize_grid_ign::_base_output` via `_IgnGridSourceContext`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_IgnGridSourceContext`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_IgnGridSourceContext`
- constructor call: `landscout.stages.normalize_grid_ign::_source_context` via `_IgnGridSourceContext`
- value/type reference: `landscout.stages.normalize_grid_ign::_source_context` via `_IgnGridSourceContext`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.stages.normalize_grid_ign import (
    _IgnGridSourceContext as IgnGridSourceContext,
)`
- constructor call: `tests.unit.test_normalize_grid_ign::_context` via `IgnGridSourceContext`
- value/type reference: `tests.unit.test_normalize_grid_ign::_context` via `IgnGridSourceContext`

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

**Source purpose:** One source voltage value and its explicit normalized semantics.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `raw` | `str \| None` | `required` | `raw: str \| None` |
| `status` | `VoltageStatus` | `required` | `status: VoltageStatus` |
| `voltage_kv` | `float \| None` | `required` | `voltage_kv: float \| None` |
| `voltage_upper_bound_kv` | `float \| None` | `required` | `voltage_upper_bound_kv: float \| None` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`
- constructor call: `landscout.stages.normalize_grid_ign::parse_ign_voltage` via `IgnVoltageNormalization`
- value/type reference: `landscout.stages.normalize_grid_ign::parse_ign_voltage` via `IgnVoltageNormalization`

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

**Source purpose:** Defines `NormalizedIgnElectricityData`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `electric_lines` | `gpd.GeoDataFrame` | `required` | `electric_lines: gpd.GeoDataFrame` |
| `transformation_posts` | `gpd.GeoDataFrame` | `required` | `transformation_posts: gpd.GeoDataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`
- import: `landscout.stages.enrich_grid_proximity::<module>` via `from landscout.stages.normalize_grid_ign import (
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
)`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `NormalizedIgnElectricityData`
- constructor call: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `NormalizedIgnElectricityData`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `NormalizedIgnElectricityData`
- import: `tests.unit.test_enrich_grid_proximity::<module>` via `from landscout.stages.normalize_grid_ign import NormalizedIgnElectricityData`
- constructor call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `NormalizedIgnElectricityData`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `NormalizedIgnElectricityData`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`
- value/type reference: `tests.unit.test_normalize_grid_ign::normalize_ign_electricity` via `NormalizedIgnElectricityData`

**Exact class source**

```python
class NormalizedIgnElectricityData:
    electric_lines: gpd.GeoDataFrame
    transformation_posts: gpd.GeoDataFrame
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_normalized_term`

**Purpose:** Implements `normalized term` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _normalized_term(value: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `" ".join(without_accents.split())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::parse_ign_voltage` via `_normalized_term`
- value/type reference: `landscout.stages.normalize_grid_ign::parse_ign_voltage` via `_normalized_term`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `unicodedata.normalize` | `unicodedata.normalize` |
| `value.strip().casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `"".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `unicodedata.combining` | `unicodedata.combining` |
| `" ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `without_accents.split` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _normalized_term(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.strip().casefold())
    without_accents = "".join(
        character for character in decomposed if not unicodedata.combining(character)
    )
    return " ".join(without_accents.split())
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_positive_voltage`

**Purpose:** Implements `positive voltage` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _positive_voltage(match: re.Match[str]) -> float | None:
```

- Exact decorators: none.
- Declared return annotation: `float | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `match` | positional-or-keyword | `re.Match[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value if value > 0 and isfinite(value) else None`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::parse_ign_voltage` via `_positive_voltage`
- value/type reference: `landscout.stages.normalize_grid_ign::parse_ign_voltage` via `_positive_voltage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `match.group("value").replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `match.group` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `match.group("value").replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _positive_voltage(match: re.Match[str]) -> float | None:
    value = float(match.group("value").replace(",", "."))
    return value if value > 0 and isfinite(value) else None
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_missing_scalar`

**Purpose:** Implements `is missing scalar` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _is_missing_scalar(value: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `True`
  - `False`
  - `bool(pd.isna(value))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::parse_ign_voltage` via `_is_missing_scalar`
- value/type reference: `landscout.stages.normalize_grid_ign::parse_ign_voltage` via `_is_missing_scalar`
- direct call: `landscout.stages.normalize_grid_ign::_normalized_precision` via `_is_missing_scalar`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalized_precision` via `_is_missing_scalar`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `is_scalar` | `pandas.api.types.is_scalar` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |

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
def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    if not is_scalar(value):
        return False
    return bool(pd.isna(value))
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `parse_ign_voltage`

**Purpose:** Parse scalar IGN voltage vocabulary without inventing precision.

    Unsupported list-like or array-like inputs are preserved as text and
    classified ``UNPARSED`` rather than reaching Pandas' ambiguous truth-value
    handling.

**Exact signature**

```python
def parse_ign_voltage(value: object) -> IgnVoltageNormalization:
```

- Exact decorators: none.
- Declared return annotation: `IgnVoltageNormalization`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnVoltageNormalization(str(value), "UNPARSED", None, None)`
  - `IgnVoltageNormalization(None, "UNKNOWN", None, None)`
  - `IgnVoltageNormalization(raw, "UNKNOWN", None, None)`
  - `IgnVoltageNormalization(raw, "DEENERGIZED", None, None)`
  - `IgnVoltageNormalization(raw, "BELOW", None, upper_bound)`
  - `IgnVoltageNormalization(raw, "EXACT", exact, None)`
  - `IgnVoltageNormalization(raw, "UNPARSED", None, None)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `parse_ign_voltage`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `parse_ign_voltage`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`
- direct call: `tests.unit.test_normalize_grid_ign::test_exact_voltage_parser_is_generic_and_finite` via `parse_ign_voltage`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_exact_voltage_parser_is_generic_and_finite` via `parse_ign_voltage`
- direct call: `tests.unit.test_normalize_grid_ign::test_bounded_voltage_is_generic_finite_and_not_exact` via `parse_ign_voltage`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_bounded_voltage_is_generic_finite_and_not_exact` via `parse_ign_voltage`
- direct call: `tests.unit.test_normalize_grid_ign::test_unknown_voltage_parser` via `parse_ign_voltage`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_unknown_voltage_parser` via `parse_ign_voltage`
- direct call: `tests.unit.test_normalize_grid_ign::test_deenergized_voltage_parser` via `parse_ign_voltage`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_deenergized_voltage_parser` via `parse_ign_voltage`
- direct call: `tests.unit.test_normalize_grid_ign::test_unexpected_or_non_scalar_voltage_is_controlled_unparsed` via `parse_ign_voltage`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_unexpected_or_non_scalar_voltage_is_controlled_unparsed` via `parse_ign_voltage`
- direct call: `tests.unit.test_normalize_grid_ign::test_invalid_or_overflowing_numeric_voltage_is_unparsed` via `parse_ign_voltage`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_invalid_or_overflowing_numeric_voltage_is_unparsed` via `parse_ign_voltage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `is_scalar` | `pandas.api.types.is_scalar` |
| `IgnVoltageNormalization` | `landscout.stages.normalize_grid_ign.IgnVoltageNormalization` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_missing_scalar` | `landscout.stages.normalize_grid_ign._is_missing_scalar` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalized_term` | `landscout.stages.normalize_grid_ign._normalized_term` |
| `_BELOW_VOLTAGE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `_positive_voltage` | `landscout.stages.normalize_grid_ign._positive_voltage` |
| `_EXACT_VOLTAGE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_lambert93`

**Purpose:** Implements `validated lambert93` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _validated_lambert93(crs_value: object, label: str) -> CRS:
```

- Exact decorators: none.
- Declared return annotation: `CRS`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `crs_value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `source_crs`
- Explicit raise paths:
  - `IgnGridNormalizationError(f"{label} CRS is required")` under lexical guard `crs_value is None`.
  - `IgnGridNormalizationError(f"{label} CRS is unreadable")`.
  - `IgnGridNormalizationError(f"{label} must use EPSG:2154")` under lexical guard `not source_crs.is_projected or not source_crs.equals(expected_crs)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_validate_input` via `_validated_lambert93`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_input` via `_validated_lambert93`
- direct call: `landscout.stages.normalize_grid_ign::_validate_layer_summary` via `_validated_lambert93`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_layer_summary` via `_validated_lambert93`
- direct call: `landscout.stages.normalize_grid_ign::_validate_archive_identity` via `_validated_lambert93`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_archive_identity` via `_validated_lambert93`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `source_crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_required_exact_string`

**Purpose:** Implements `required exact string` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _required_exact_string(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `IgnGridNormalizationError(f"IGN source context {label} must be a string")` under lexical guard `not isinstance(value, str) or not value.strip()`.
  - `IgnGridNormalizationError(<br>            f"IGN source context {label} must not contain edge whitespace"<br>        )` under lexical guard `value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_validate_source_context` via `_required_exact_string`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_context` via `_required_exact_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_context`

**Purpose:** Implements `validate source context` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _validate_source_context(context: _IgnGridSourceContext) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `context` | positional-or-keyword | `_IgnGridSourceContext` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnGridNormalizationError(<br>            "IGN source context department_code is invalid"<br>        )`.
  - `IgnGridNormalizationError(<br>            "IGN source context department_code must not be rewritten"<br>        )` under lexical guard `validated_department != department_code`.
  - `IgnGridNormalizationError(<br>            "IGN source context edition must be a valid ISO calendar date"<br>        )`.
  - `IgnGridNormalizationError(<br>            "IGN source context edition must not be rewritten"<br>        )` under lexical guard `validated_edition != edition`.
  - `IgnGridNormalizationError(<br>            "IGN source context download_timestamp must be a valid ISO datetime"<br>        )`.
  - `IgnGridNormalizationError(<br>            "IGN source context download_timestamp must be timezone-aware"<br>        )` under lexical guard `timestamp.tzinfo is None or timestamp.utcoffset() is None`.
  - `IgnGridNormalizationError(<br>            "IGN source context archive_sha256 must contain 64 hexadecimal characters"<br>        )` under lexical guard `_SHA256_PATTERN.fullmatch(archive_sha256) is None`.
  - `IgnGridNormalizationError(<br>            "IGN source context source_url must be a valid HTTP(S) URL"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_validate_source_context`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_validate_source_context`
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_validate_source_context`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_validate_source_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_internal_source_context_accepts_supported_department_codes` via `grid_normalization._validate_source_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_invalid_lineage_values` via `grid_normalization._validate_source_context`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_required_exact_string` | `landscout.stages.normalize_grid_ign._required_exact_string` |
| `_DEPARTMENT_CODE_VALIDATOR.validate_python` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `_EDITION_VALIDATOR.validate_python` | `unresolved local/third-party receiver; no ownership inferred` |
| `date.fromisoformat` | `datetime.date.fromisoformat` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `timestamp.utcoffset` | `unresolved local/third-party receiver; no ownership inferred` |
| `_SHA256_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `_HTTP_URL_VALIDATOR.validate_python` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_SHA256_PATTERN.fullmatch` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_source_context(context: _IgnGridSourceContext) -> None:
    _required_exact_string(context.source_layer, "source_layer")
    department_code = _required_exact_string(context.department_code, "department_code")
    edition = _required_exact_string(context.edition, "edition")
    download_timestamp = _required_exact_string(
        context.download_timestamp, "download_timestamp"
    )
    archive_sha256 = _required_exact_string(context.archive_sha256, "archive_sha256")
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_input`

**Purpose:** Implements `validate input` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _validate_input(
    frame: gpd.GeoDataFrame,
    required_columns: frozenset[str],
    source_layer: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `required_columns` | positional-or-keyword | `frozenset[str]` | `required` |
| `source_layer` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnGridNormalizationError(<br>            f"Missing required IGN {source_layer} columns: {formatted}"<br>        )` under lexical guard `missing`.
  - `IgnGridNormalizationError(<br>            f"IGN {source_layer} requires an active geometry column"<br>        )` under lexical guard `frame.active_geometry_name != "geometry"`.
  - `IgnGridNormalizationError(<br>            f"IGN {source_layer} cleabs values must not be null"<br>        )` under lexical guard `identifiers.isna().any()`.
  - `IgnGridNormalizationError(<br>            f"IGN {source_layer} cleabs values must be strings"<br>        )` under lexical guard `any(not isinstance(identifier, str) for identifier in identifiers.tolist())`.
  - `IgnGridNormalizationError(<br>            f"IGN {source_layer} cleabs values must not be empty"<br>        )` under lexical guard `identifiers.str.strip().eq("").any()`.
  - `IgnGridNormalizationError(<br>            f"IGN {source_layer} cleabs values must not contain edge whitespace"<br>        )` under lexical guard `identifiers.map(lambda value: value != value.strip()).any()`.
  - `IgnGridNormalizationError(<br>            f"IGN {source_layer} cleabs values must not contain ':'"<br>        )` under lexical guard `identifiers.str.contains(":", regex=False).any()`.
  - `IgnGridNormalizationError(<br>            f"IGN {source_layer} cleabs values must not contain control characters"<br>        )` under lexical guard `identifiers.map(<br>        lambda value: any(<br>            unicodedata.category(character) == "Cc" for character in value<br>        )<br>    ).any()`.
  - `IgnGridNormalizationError(<br>            f"IGN {source_layer} cleabs values must be unique"<br>        )` under lexical guard `identifiers.duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_validate_input`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_validate_input`
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_validate_input`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_validate_input`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `_validated_lambert93` | `landscout.stages.normalize_grid_ign._validated_lambert93` |
| `identifiers.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.str.strip().eq("").any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.str.strip().eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.str.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.map(lambda value: value != value.strip()).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.map` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.str.contains(":", regex=False).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.str.contains` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.map(<br>        lambda value: any(<br>            unicodedata.category(character) == "Cc" for character in value<br>        )<br>    ).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

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
        lambda value: any(
            unicodedata.category(character) == "Cc" for character in value
        )
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_geometry_status`

**Purpose:** Implements `geometry status` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `gpd.GeoSeries` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `status`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_geometry_status`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_geometry_status`
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_geometry_status`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_geometry_status`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.Series` | `pandas.Series` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna` |
| External process/environment | None directly present. |
| In-memory mutation | `status.loc[null_mask] = "NULL"`<br>`status.loc[empty_mask] = "EMPTY"`<br>`status.loc[invalid_mask] = "INVALID"` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_geometry_summary`

**Purpose:** Implements `geometry summary` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[int, int, int, tuple[str, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>        int(null_mask.sum()),<br>        int(empty_mask.sum()),<br>        int(invalid_mask.sum()),<br>        geometry_types,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_validate_layer_summary` via `_geometry_summary`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_layer_summary` via `_geometry_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `null_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `empty_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna`<br>`geometry[~null_mask].geom_type.dropna().unique`<br>`geometry[~null_mask].geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_valid_geometry_types`

**Purpose:** Implements `validate valid geometry types` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _validate_valid_geometry_types(
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    allowed_types: frozenset[str],
    source_layer: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `status` | positional-or-keyword | `pd.Series` | `required` |
| `allowed_types` | positional-or-keyword | `frozenset[str]` | `required` |
| `source_layer` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnGridNormalizationError(<br>            f"IGN {source_layer} has unsupported VALID geometry types: "<br>            + ", ".join(unsupported)<br>        )` under lexical guard `unsupported`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_validate_valid_geometry_types`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_validate_valid_geometry_types`
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_validate_valid_geometry_types`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_validate_valid_geometry_types`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_types.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalized_precision`

**Purpose:** Implements `normalized precision` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _normalized_precision(
    source: pd.Series,
    source_layer: str,
) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `pd.Series` | `required` |
| `source_layer` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.Series(normalized, index=source.index, dtype="float64")`
- Explicit raise paths:
  - `IgnGridNormalizationError(<br>                f"IGN {source_layer} precision_planimetrique must be numeric or null"<br>            )` under lexical guard `isinstance(value, bool) or not isinstance(value, Real)`.
  - `IgnGridNormalizationError(<br>                f"IGN {source_layer} precision_planimetrique must be finite and >= 0"<br>            )` under lexical guard `not isfinite(numeric) or numeric < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_normalized_precision`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_normalized_precision`
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_normalized_precision`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_normalized_precision`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_missing_scalar` | `landscout.stages.normalize_grid_ign._is_missing_scalar` |
| `normalized.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `isfinite` | `math.isfinite` |
| `pd.Series` | `pandas.Series` |

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
| In-memory mutation | `normalized.append(float("nan"))`<br>`normalized.append(numeric)` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_base_output`

**Purpose:** Implements `base output` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _base_output(
    frame: gpd.GeoDataFrame,
    *,
    feature_type: str,
    context: _IgnGridSourceContext,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `feature_type` | keyword-only | `str` | `required` |
| `context` | keyword-only | `_IgnGridSourceContext` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_base_output`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_base_output`
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_base_output`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_base_output`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `frame["cleabs"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `frame.index.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_ids.map` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `output["grid_feature_id"] = source_ids.map(<br>        lambda identifier: f"IGN_BDTOPO:{feature_type}:{identifier}"<br>    )`<br>`output["grid_feature_type"] = feature_type`<br>`output["source_provider"] = SOURCE_PROVIDER`<br>`output["source_product"] = SOURCE_PRODUCT`<br>`output["source_layer"] = context.source_layer`<br>`output["source_feature_id"] = source_ids`<br>`output["source_department_code"] = context.department_code`<br>`output["source_edition"] = context.edition`<br>`output["source_product_version"] = context.product_version`<br>`output["source_download_timestamp"] = context.download_timestamp`<br>`output["source_archive_sha256"] = context.archive_sha256`<br>`output["source_url"] = context.source_url` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_geodataframe`

**Purpose:** Implements `validated geodataframe` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _validated_geodataframe(
    output: pd.DataFrame,
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    columns: tuple[str, ...],
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `output` | positional-or-keyword | `pd.DataFrame` | `required` |
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `status` | positional-or-keyword | `pd.Series` | `required` |
| `columns` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `normalized`
- Explicit raise paths:
  - `IgnGridNormalizationError(<br>            "Normalized IGN grid_feature_id values must be non-null and unique"<br>        )` under lexical guard `normalized_ids.isna().any() or normalized_ids.duplicated().any()`.
  - `IgnGridNormalizationError("IGN normalization changed the row count")` under lexical guard `len(normalized) != len(frame)`.
  - `IgnGridNormalizationError("IGN normalized output must use a RangeIndex")` under lexical guard `not isinstance(normalized.index, pd.RangeIndex)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_validated_geodataframe`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_electric_lines` via `_validated_geodataframe`
- direct call: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_validated_geodataframe`
- value/type reference: `landscout.stages.normalize_grid_ign::_normalize_ign_transformation_posts` via `_validated_geodataframe`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `frame.geometry.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_ids.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_ids.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_ids.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized_ids.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `frame.geometry.copy` |
| External process/environment | None directly present. |
| In-memory mutation | `output["spatial_role"] = SPATIAL_ROLE`<br>`output["geometry_status"] = status`<br>`output["geometry"] = frame.geometry.copy()` |
| Direct parameter mutation | `output["spatial_role"] = SPATIAL_ROLE`<br>`output["geometry_status"] = status`<br>`output["geometry"] = frame.geometry.copy()` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalize_ign_electric_lines`

**Purpose:** Normalize one discovered IGN electric-line layer.

**Exact signature**

```python
def _normalize_ign_electric_lines(
    lines: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `lines` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `context` | positional-or-keyword | `_IgnGridSourceContext` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_validated_geodataframe(output, working, status, LINE_OUTPUT_COLUMNS)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_normalize_ign_electric_lines`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_normalize_ign_electric_lines`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.stages.normalize_grid_ign import (
    _normalize_ign_electric_lines as normalize_ign_electric_lines,
)`
- direct call: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_uppercase_sha256` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_uppercase_sha256` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_line_has_stable_identity_lineage_and_range_index` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_line_has_stable_identity_lineage_and_range_index` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_deenergized_voltage_does_not_override_source_asset_status` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_deenergized_voltage_does_not_override_source_asset_status` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_null_or_empty_line_cleabs_fails` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_null_or_empty_line_cleabs_fails` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_unsafe_source_id_is_rejected_without_rewriting` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_unsafe_source_id_is_rejected_without_rewriting` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_duplicate_line_cleabs_fails` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_duplicate_line_cleabs_fails` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_line_missing_or_wrong_crs_fails` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_missing_or_wrong_crs_fails` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_line_geometry_quality_is_preserved_without_row_loss_or_repair` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_geometry_quality_is_preserved_without_row_loss_or_repair` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_z_coordinates_are_preserved` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_z_coordinates_are_preserved` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_unusual_duplicate_source_index_is_not_preserved_as_identity` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_unusual_duplicate_source_index_is_not_preserved_as_identity` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_line_normalization_does_not_mutate_input_and_has_stable_columns` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_normalization_does_not_mutate_input_and_has_stable_columns` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_missing_required_line_field_fails` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_missing_required_line_field_fails` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_or_null_line_precision_is_normalized_to_float` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_or_null_line_precision_is_normalized_to_float` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_invalid_line_precision_fails` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_invalid_line_precision_fails` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_normalized_voltage_never_emits_non_finite_numeric_values` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_normalized_voltage_never_emits_non_finite_numeric_values` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `normalize_ign_electric_lines`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_polygon_or_point_is_rejected_as_electric_line` via `normalize_ign_electric_lines`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_polygon_or_point_is_rejected_as_electric_line` via `normalize_ign_electric_lines`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_source_context` | `landscout.stages.normalize_grid_ign._validate_source_context` |
| `_validate_input` | `landscout.stages.normalize_grid_ign._validate_input` |
| `lines.reset_index(drop=True).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `lines.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_geometry_status` | `landscout.stages.normalize_grid_ign._geometry_status` |
| `_validate_valid_geometry_types` | `landscout.stages.normalize_grid_ign._validate_valid_geometry_types` |
| `_normalized_precision` | `landscout.stages.normalize_grid_ign._normalized_precision` |
| `_base_output` | `landscout.stages.normalize_grid_ign._base_output` |
| `parse_ign_voltage` | `landscout.stages.normalize_grid_ign.parse_ign_voltage` |
| `working["voltage"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["gestionnaire"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["siren_gestionnaire"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["etat_de_l_objet"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["sources"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["identifiants_sources"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["date_creation"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["date_modification"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["date_de_confirmation"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working[<br>        "methode_d_acquisition_planimetrique"<br>    ].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_geodataframe` | `landscout.stages.normalize_grid_ign._validated_geodataframe` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_geometry_status`<br>`_validate_valid_geometry_types` |
| External process/environment | None directly present. |
| In-memory mutation | `output["voltage_raw"] = [result.raw for result in parsed]`<br>`output["voltage_status"] = [result.status for result in parsed]`<br>`output["voltage_kv"] = [result.voltage_kv for result in parsed]`<br>`output["voltage_upper_bound_kv"] = [<br>        result.voltage_upper_bound_kv for result in parsed<br>    ]`<br>`output["manager_name"] = working["gestionnaire"].copy()`<br>`output["manager_siren"] = working["siren_gestionnaire"].copy()`<br>`output["asset_status_raw"] = working["etat_de_l_objet"].copy()`<br>`output["source_name_raw"] = working["sources"].copy()`<br>`output["source_identifiers_raw"] = working["identifiants_sources"].copy()`<br>`output["source_created_at"] = working["date_creation"].copy()`<br>`output["source_modified_at"] = working["date_modification"].copy()`<br>`output["source_confirmed_at"] = working["date_de_confirmation"].copy()`<br>`output["planimetric_acquisition_method"] = working[<br>        "methode_d_acquisition_planimetrique"<br>    ].copy()`<br>`output["planimetric_precision_m"] = precision` |
| Direct parameter mutation | None directly present. |

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
    return _validated_geodataframe(output, working, status, LINE_OUTPUT_COLUMNS)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalize_ign_transformation_posts`

**Purpose:** Normalize one discovered IGN transformation-post proxy layer.

**Exact signature**

```python
def _normalize_ign_transformation_posts(
    posts: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `posts` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `context` | positional-or-keyword | `_IgnGridSourceContext` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_validated_geodataframe(<br>        output,<br>        working,<br>        status,<br>        TRANSFORMATION_POST_OUTPUT_COLUMNS,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_normalize_ign_transformation_posts`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_normalize_ign_transformation_posts`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.stages.normalize_grid_ign import (
    _normalize_ign_transformation_posts as normalize_ign_transformation_posts,
)`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_post_has_stable_lineage_and_no_voltage_inference` via `normalize_ign_transformation_posts`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_post_has_stable_lineage_and_no_voltage_inference` via `normalize_ign_transformation_posts`
- direct call: `tests.unit.test_normalize_grid_ign::test_post_geometry_crs_and_input_are_preserved` via `normalize_ign_transformation_posts`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_post_geometry_crs_and_input_are_preserved` via `normalize_ign_transformation_posts`
- direct call: `tests.unit.test_normalize_grid_ign::test_duplicate_post_cleabs_fails` via `normalize_ign_transformation_posts`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_duplicate_post_cleabs_fails` via `normalize_ign_transformation_posts`
- direct call: `tests.unit.test_normalize_grid_ign::test_null_post_geometry_and_precision_are_preserved` via `normalize_ign_transformation_posts`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_null_post_geometry_and_precision_are_preserved` via `normalize_ign_transformation_posts`
- direct call: `tests.unit.test_normalize_grid_ign::test_invalid_post_precision_fails` via `normalize_ign_transformation_posts`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_invalid_post_precision_fails` via `normalize_ign_transformation_posts`
- direct call: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `normalize_ign_transformation_posts`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `normalize_ign_transformation_posts`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_line_or_point_is_rejected_as_transformation_post` via `normalize_ign_transformation_posts`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_line_or_point_is_rejected_as_transformation_post` via `normalize_ign_transformation_posts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_source_context` | `landscout.stages.normalize_grid_ign._validate_source_context` |
| `_validate_input` | `landscout.stages.normalize_grid_ign._validate_input` |
| `posts.reset_index(drop=True).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `posts.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_geometry_status` | `landscout.stages.normalize_grid_ign._geometry_status` |
| `_validate_valid_geometry_types` | `landscout.stages.normalize_grid_ign._validate_valid_geometry_types` |
| `_normalized_precision` | `landscout.stages.normalize_grid_ign._normalized_precision` |
| `_base_output` | `landscout.stages.normalize_grid_ign._base_output` |
| `working["toponyme"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["statut_du_toponyme"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["importance"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["etat_de_l_objet"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["sources"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["identifiants_sources"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["date_creation"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["date_modification"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["date_de_confirmation"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working[<br>        "methode_d_acquisition_planimetrique"<br>    ].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_geodataframe` | `landscout.stages.normalize_grid_ign._validated_geodataframe` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_geometry_status`<br>`_validate_valid_geometry_types` |
| External process/environment | None directly present. |
| In-memory mutation | `output["name"] = working["toponyme"].copy()`<br>`output["name_status_raw"] = working["statut_du_toponyme"].copy()`<br>`output["importance_raw"] = working["importance"].copy()`<br>`output["asset_status_raw"] = working["etat_de_l_objet"].copy()`<br>`output["source_name_raw"] = working["sources"].copy()`<br>`output["source_identifiers_raw"] = working["identifiants_sources"].copy()`<br>`output["source_created_at"] = working["date_creation"].copy()`<br>`output["source_modified_at"] = working["date_modification"].copy()`<br>`output["source_confirmed_at"] = working["date_de_confirmation"].copy()`<br>`output["planimetric_acquisition_method"] = working[<br>        "methode_d_acquisition_planimetrique"<br>    ].copy()`<br>`output["planimetric_precision_m"] = precision`<br>`output["voltage_status"] = "UNKNOWN"`<br>`output["voltage_kv"] = float("nan")` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_layer_summary`

**Purpose:** Implements `validate layer summary` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `summary` | positional-or-keyword | `IgnBdTopoLayerSummary` | `required` |
| `expected_layer` | keyword-only | `str` | `required` |
| `expected_logical_name` | keyword-only | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnGridNormalizationError(<br>            f"IGN {expected_logical_name} summary schema contract is invalid"<br>        )`.
  - `IgnGridNormalizationError(<br>            f"IGN {expected_logical_name} summary layer does not match extraction"<br>        )` under lexical guard `summary.source_layer_name != expected_layer`.
  - `IgnGridNormalizationError(<br>            f"IGN {expected_logical_name} summary has the wrong logical name"<br>        )` under lexical guard `summary.logical_name != expected_logical_name`.
  - `IgnGridNormalizationError(<br>            f"IGN {expected_logical_name} summary row count does not match frame"<br>        )` under lexical guard `summary.feature_count != len(frame)`.
  - `IgnGridNormalizationError(<br>            f"IGN {expected_logical_name} summary schema columns or dtypes "<br>            "do not match frame"<br>        )` under lexical guard `summary.columns != observed_columns or summary.dtypes != observed_dtypes`.
  - `IgnGridNormalizationError(<br>            f"IGN {expected_logical_name} requires an active geometry column"<br>        )` under lexical guard `frame.active_geometry_name != "geometry"`.
  - `IgnGridNormalizationError(<br>            f"IGN {expected_logical_name} summary CRS does not match frame"<br>        )` under lexical guard `not frame_crs.equals(summary_crs)`.
  - `IgnGridNormalizationError(<br>            f"IGN {expected_logical_name} geometry summary does not match frame"<br>        )` under lexical guard `observed_geometry != expected_geometry`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `_validate_layer_summary`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `_validate_layer_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_layer_summary_contract` | `landscout.sources.ign_bdtopo_fr._validate_layer_summary_contract` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_lambert93` | `landscout.stages.normalize_grid_ign._validated_lambert93` |
| `frame_crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_geometry_summary` | `landscout.stages.normalize_grid_ign._geometry_summary` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_geometry_summary` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalized_identity`

**Purpose:** Implements `normalized identity` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `" ".join(re.findall(r"[a-z0-9]+", without_accents))`
- Explicit raise paths:
  - `IgnGridNormalizationError(f"IGN archive {label} must be a string")` under lexical guard `not isinstance(value, str) or not value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_validate_archive_identity` via `_normalized_identity`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_archive_identity` via `_normalized_identity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
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
def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnGridNormalizationError(f"IGN archive {label} must be a string")
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    without_accents = "".join(
        character for character in decomposed if not unicodedata.combining(character)
    )
    return " ".join(re.findall(r"[a-z0-9]+", without_accents))
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_archive_identity`

**Purpose:** Implements `validate archive identity` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _validate_archive_identity(source: IgnBdTopoElectricityData) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoElectricityData` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnGridNormalizationError(<br>            "IGN archive provider is incompatible with the IGN normalizer"<br>        )` under lexical guard `provider not in _IGN_PROVIDER_IDENTITIES`.
  - `IgnGridNormalizationError(<br>            "IGN archive product is incompatible with the BD TOPO normalizer"<br>        )` under lexical guard `product.replace(" ", "") != "bdtopo"`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `_validate_archive_identity`
- value/type reference: `landscout.stages.normalize_grid_ign::_validate_source_bundle` via `_validate_archive_identity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_normalized_identity` | `landscout.stages.normalize_grid_ign._normalized_identity` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `product.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_lambert93` | `landscout.stages.normalize_grid_ign._validated_lambert93` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `product.replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_bundle`

**Purpose:** Implements `validate source bundle` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _validate_source_bundle(source: IgnBdTopoElectricityData) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoElectricityData` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnGridNormalizationError(<br>            "IGN electricity source must be IgnBdTopoElectricityData"<br>        )` under lexical guard `type(source) is not IgnBdTopoElectricityData`.
  - `IgnGridNormalizationError("IGN electricity extraction type is invalid")` under lexical guard `type(source.extraction) is not IgnBdTopoExtraction`.
  - `IgnGridNormalizationError("IGN electricity archive type is invalid")` under lexical guard `type(source.extraction.archive) is not IgnBdTopoDownload`.
  - `IgnGridNormalizationError("IGN electricity summary type is invalid")` under lexical guard `type(source.electric_lines_summary) is not IgnBdTopoLayerSummary<br>        or type(source.transformation_posts_summary) is not IgnBdTopoLayerSummary`.
  - `IgnGridNormalizationError("IGN electricity layers must be GeoDataFrames")` under lexical guard `not isinstance(source.electric_lines, gpd.GeoDataFrame) or not isinstance(<br>        source.transformation_posts, gpd.GeoDataFrame<br>    )`.
  - `IgnGridNormalizationError(<br>            "IGN electricity layer inventory must be a unique non-empty tuple"<br>        )` under lexical guard `type(layer_names) is not tuple<br>        or not layer_names<br>        or any(<br>            not isinstance(name, str) or not name or name != name.strip()<br>            for name in layer_names<br>        )<br>        or len(set(layer_names)) != len(layer_names)`.
  - `IgnGridNormalizationError(<br>            "IGN electricity selected layer is absent from the layer inventory"<br>        )` under lexical guard `any(layer not in layer_names for layer in selected_layers)`.
  - `IgnGridNormalizationError(<br>            "IGN electricity roles must use distinct layers, not the same layer"<br>        )` under lexical guard `selected_layers[0] == selected_layers[1]`.
  - `IgnGridNormalizationError(<br>            "IGN source bundle spatial roles must all be PROXY_GEOMETRY"<br>        )` under lexical guard `any(role != SPATIAL_ROLE for role in roles)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_validate_source_bundle`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_validate_source_bundle`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_archive_identity` | `landscout.stages.normalize_grid_ign._validate_archive_identity` |
| `_validate_layer_summary` | `landscout.stages.normalize_grid_ign._validate_layer_summary` |

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
def _validate_source_bundle(source: IgnBdTopoElectricityData) -> None:
    if type(source) is not IgnBdTopoElectricityData:
        raise IgnGridNormalizationError(
            "IGN electricity source must be IgnBdTopoElectricityData"
        )
    if type(source.extraction) is not IgnBdTopoExtraction:
        raise IgnGridNormalizationError("IGN electricity extraction type is invalid")
    if type(source.extraction.archive) is not IgnBdTopoDownload:
        raise IgnGridNormalizationError("IGN electricity archive type is invalid")
    if (
        type(source.electric_lines_summary) is not IgnBdTopoLayerSummary
        or type(source.transformation_posts_summary) is not IgnBdTopoLayerSummary
    ):
        raise IgnGridNormalizationError("IGN electricity summary type is invalid")
    if not isinstance(source.electric_lines, gpd.GeoDataFrame) or not isinstance(
        source.transformation_posts, gpd.GeoDataFrame
    ):
        raise IgnGridNormalizationError("IGN electricity layers must be GeoDataFrames")
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_source_context`

**Purpose:** Implements `source context` within the file role: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

**Exact signature**

```python
def _source_context(
    source: IgnBdTopoElectricityData,
    source_layer: str,
) -> _IgnGridSourceContext:
```

- Exact decorators: none.
- Declared return annotation: `_IgnGridSourceContext`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoElectricityData` | `required` |
| `source_layer` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_IgnGridSourceContext(<br>        source_layer=source_layer,<br>        department_code=archive.department_code,<br>        edition=archive.edition,<br>        product_version=archive.product_version,<br>        download_timestamp=archive.download_timestamp,<br>        archive_sha256=archive.sha256,<br>        source_url=archive.source_url,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_source_context`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `_source_context`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_IgnGridSourceContext` | `landscout.stages.normalize_grid_ign._IgnGridSourceContext` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `normalize_ign_electricity`

**Purpose:** Validate and normalize a complete already-loaded IGN source bundle.

**Exact signature**

```python
def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `NormalizedIgnElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoElectricityData` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `NormalizedIgnElectricityData(<br>            electric_lines=_normalize_ign_electric_lines(<br>                fresh.electric_lines, line_context<br>            ),<br>            transformation_posts=_normalize_ign_transformation_posts(<br>                fresh.transformation_posts, post_context<br>            ),<br>        )`
- Explicit raise paths:
  - `IgnGridNormalizationError(<br>                "IGN electricity source config type is invalid"<br>            )` under lexical guard `type(config) is not IgnBdTopoSourceConfig`.
  - `re-raise`.
  - `IgnGridNormalizationError(<br>            f"IGN electricity source cannot be normalized safely: {error}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`
- import: `landscout.stages.enrich_grid_proximity::<module>` via `from landscout.stages.normalize_grid_ign import (
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
)`
- direct call: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `normalize_ign_electricity`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `normalize_ign_electricity`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.stages.normalize_grid_ign import (
    normalize_ign_electricity as _normalize_ign_electricity,
)`
- direct call: `tests.unit.test_normalize_grid_ign::normalize_ign_electricity` via `_normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::normalize_ign_electricity` via `_normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_grid_normalization_uses_distinct_fresh_revalidated_frames` via `_normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_grid_normalization_uses_distinct_fresh_revalidated_frames` via `_normalize_ign_electricity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `_revalidate_ign_bdtopo_electricity_data` | `landscout.sources.ign_bdtopo_fr._revalidate_ign_bdtopo_electricity_data` |
| `_validate_source_bundle` | `landscout.stages.normalize_grid_ign._validate_source_bundle` |
| `_source_context` | `landscout.stages.normalize_grid_ign._source_context` |
| `NormalizedIgnElectricityData` | `landscout.stages.normalize_grid_ign.NormalizedIgnElectricityData` |
| `_normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_normalize_ign_transformation_posts` | `landscout.stages.normalize_grid_ign._normalize_ign_transformation_posts` |

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
        fresh = _revalidate_ign_bdtopo_electricity_data(source, config)
        _validate_source_bundle(fresh)
        line_context = _source_context(fresh, fresh.extraction.electric_lines_layer)
        post_context = _source_context(
            fresh, fresh.extraction.transformation_posts_layer
        )
        return NormalizedIgnElectricityData(
            electric_lines=_normalize_ign_electric_lines(
                fresh.electric_lines, line_context
            ),
            transformation_posts=_normalize_ign_transformation_posts(
                fresh.transformation_posts, post_context
            ),
        )
    except IgnGridNormalizationError:
        raise
    except Exception as error:
        raise IgnGridNormalizationError(
            f"IGN electricity source cannot be normalized safely: {error}"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `PACKAGE_LINEAGE_COLUMNS`, `LINE_OUTPUT_COLUMNS`, `TRANSFORMATION_POST_OUTPUT_COLUMNS`, `LINE_SOURCE_FIELDS`, `TRANSFORMATION_POST_SOURCE_FIELDS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Normalize IGN BD TOPO electricity layers into stable LandScout proxies."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime
from math import isfinite
from numbers import Real
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pandas.api.types import is_scalar  # type: ignore[import-untyped]
from pydantic import HttpUrl, TypeAdapter, ValidationError
from pyproj import CRS

from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)

SOURCE_PROVIDER = "IGN"
SOURCE_PRODUCT = "BD_TOPO"
SPATIAL_ROLE = "PROXY_GEOMETRY"

VoltageStatus = Literal["EXACT", "BELOW", "UNKNOWN", "DEENERGIZED", "UNPARSED"]
GeometryStatus = Literal["VALID", "NULL", "EMPTY", "INVALID"]

PACKAGE_LINEAGE_COLUMNS = (
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
)

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

LINE_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
TRANSFORMATION_POST_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})

_EXACT_VOLTAGE_PATTERN = re.compile(r"^(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE)
_BELOW_VOLTAGE_PATTERN = re.compile(
    r"^<\s*(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE
)
_UNKNOWN_VOLTAGE_TERMS = frozenset(
    {"inconnu", "inconnue", "unknown", "non renseigne", "non renseignee"}
)
_DEENERGIZED_VOLTAGE_TERMS = frozenset({"hors tension"})
_DEPARTMENT_CODE_VALIDATOR = TypeAdapter(DepartmentCode)
_EDITION_VALIDATOR = TypeAdapter(EditionString)
_HTTP_URL_VALIDATOR = TypeAdapter(HttpUrl)
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institut national de l information geographique et forestiere",
        "institut national de l information geographique et forestiere ign",
    }
)


class IgnGridNormalizationError(ValueError):
    """Raised when IGN electricity data cannot be normalized safely."""


@dataclass(frozen=True)
class _IgnGridSourceContext:
    """Immutable source-package context persisted on every normalized row."""

    source_layer: str
    department_code: str
    edition: str
    product_version: str | None
    download_timestamp: str
    archive_sha256: str
    source_url: str


@dataclass(frozen=True)
class IgnVoltageNormalization:
    """One source voltage value and its explicit normalized semantics."""

    raw: str | None
    status: VoltageStatus
    voltage_kv: float | None
    voltage_upper_bound_kv: float | None


@dataclass(frozen=True)
class NormalizedIgnElectricityData:
    electric_lines: gpd.GeoDataFrame
    transformation_posts: gpd.GeoDataFrame


def _normalized_term(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.strip().casefold())
    without_accents = "".join(
        character for character in decomposed if not unicodedata.combining(character)
    )
    return " ".join(without_accents.split())


def _positive_voltage(match: re.Match[str]) -> float | None:
    value = float(match.group("value").replace(",", "."))
    return value if value > 0 and isfinite(value) else None


def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    if not is_scalar(value):
        return False
    return bool(pd.isna(value))


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


def _required_exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnGridNormalizationError(f"IGN source context {label} must be a string")
    if value != value.strip():
        raise IgnGridNormalizationError(
            f"IGN source context {label} must not contain edge whitespace"
        )
    return value


def _validate_source_context(context: _IgnGridSourceContext) -> None:
    _required_exact_string(context.source_layer, "source_layer")
    department_code = _required_exact_string(context.department_code, "department_code")
    edition = _required_exact_string(context.edition, "edition")
    download_timestamp = _required_exact_string(
        context.download_timestamp, "download_timestamp"
    )
    archive_sha256 = _required_exact_string(context.archive_sha256, "archive_sha256")
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
        lambda value: any(
            unicodedata.category(character) == "Cc" for character in value
        )
    ).any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must not contain control characters"
        )
    if identifiers.duplicated().any():
        raise IgnGridNormalizationError(
            f"IGN {source_layer} cleabs values must be unique"
        )


def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
    status = pd.Series("VALID", index=geometry.index, dtype="object")
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    status.loc[null_mask] = "NULL"
    status.loc[empty_mask] = "EMPTY"
    status.loc[invalid_mask] = "INVALID"
    return status


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
    return _validated_geodataframe(output, working, status, LINE_OUTPUT_COLUMNS)


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


def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnGridNormalizationError(f"IGN archive {label} must be a string")
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    without_accents = "".join(
        character for character in decomposed if not unicodedata.combining(character)
    )
    return " ".join(re.findall(r"[a-z0-9]+", without_accents))


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


def _validate_source_bundle(source: IgnBdTopoElectricityData) -> None:
    if type(source) is not IgnBdTopoElectricityData:
        raise IgnGridNormalizationError(
            "IGN electricity source must be IgnBdTopoElectricityData"
        )
    if type(source.extraction) is not IgnBdTopoExtraction:
        raise IgnGridNormalizationError("IGN electricity extraction type is invalid")
    if type(source.extraction.archive) is not IgnBdTopoDownload:
        raise IgnGridNormalizationError("IGN electricity archive type is invalid")
    if (
        type(source.electric_lines_summary) is not IgnBdTopoLayerSummary
        or type(source.transformation_posts_summary) is not IgnBdTopoLayerSummary
    ):
        raise IgnGridNormalizationError("IGN electricity summary type is invalid")
    if not isinstance(source.electric_lines, gpd.GeoDataFrame) or not isinstance(
        source.transformation_posts, gpd.GeoDataFrame
    ):
        raise IgnGridNormalizationError("IGN electricity layers must be GeoDataFrames")
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
        fresh = _revalidate_ign_bdtopo_electricity_data(source, config)
        _validate_source_bundle(fresh)
        line_context = _source_context(fresh, fresh.extraction.electric_lines_layer)
        post_context = _source_context(
            fresh, fresh.extraction.transformation_posts_layer
        )
        return NormalizedIgnElectricityData(
            electric_lines=_normalize_ign_electric_lines(
                fresh.electric_lines, line_context
            ),
            transformation_posts=_normalize_ign_transformation_posts(
                fresh.transformation_posts, post_context
            ),
        )
    except IgnGridNormalizationError:
        raise
    except Exception as error:
        raise IgnGridNormalizationError(
            f"IGN electricity source cannot be normalized safely: {error}"
        ) from error
```
