# `src/landscout/stages/enrich_grid_proximity.py`

## File identity

- Repository path: `src/landscout/stages/enrich_grid_proximity.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.
- Source SHA256: `7131d0b980dad7b5c73a4c7cf2d0bd6f9fe5572c089ad39c4a592c02098c9015`

## 1. STEP 7F.1A.4 contract delta

- Revalidates the source config at the public boundary before source-complete electricity enrichment.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from dataclasses import dataclass`
- `from math import isfinite`
- `from numbers import Integral, Real`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pandas.api.types import is_scalar`
- `from pyproj import CRS`
- `from shapely import STRtree, force_2d`

### Internal LandScout imports

- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
)`
- `from landscout.stages.normalize_grid_ign import (
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `CALCULATION_CRS`

- Category: module constant or closed domain.
- Exact declaration:

```python
CALCULATION_CRS = "EPSG:2154"
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

### `PARCEL_REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `LINE_REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
LINE_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "voltage_raw",
        "voltage_status",
        "voltage_kv",
        "voltage_upper_bound_kv",
        "manager_name",
        "asset_status_raw",
        "geometry",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POST_REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
POST_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "name",
        "importance_raw",
        "asset_status_raw",
        "geometry",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `GRID_GEOMETRY_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
GRID_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
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

### `POST_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
POST_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PARCEL_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `VOLTAGE_PROXIMITY_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
VOLTAGE_PROXIMITY_COLUMNS = (
    "parcel_id",
    "voltage_kv",
    "nearest_line_proxy_distance_m",
    "nearest_line_grid_feature_id",
    "nearest_line_source_feature_id",
    "tie_count",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

- Qualified consumers:
  - import: `tests.unit.test_enrich_grid_proximity::<module>` via `from landscout.stages.enrich_grid_proximity import (
    VOLTAGE_PROXIMITY_COLUMNS,
)`
  - value/type reference: `tests.unit.test_enrich_grid_proximity::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `VOLTAGE_PROXIMITY_COLUMNS`
  - value/type reference: `tests.unit.test_enrich_grid_proximity::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `VOLTAGE_PROXIMITY_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `parcel_id`
  - `voltage_kv`
  - `nearest_line_proxy_distance_m`
  - `nearest_line_grid_feature_id`
  - `nearest_line_source_feature_id`
  - `tie_count`
  - `manager_name`
  - `asset_status_raw`
  - `source_department_code`
  - `source_edition`
  - `source_archive_sha256`

### `_LINE_MATCH_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_LINE_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "voltage_raw",
    "voltage_status",
    "voltage_kv",
    "voltage_upper_bound_kv",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `grid_feature_id`
  - `source_feature_id`
  - `voltage_raw`
  - `voltage_status`
  - `voltage_kv`
  - `voltage_upper_bound_kv`
  - `manager_name`
  - `asset_status_raw`
  - `source_department_code`
  - `source_edition`
  - `source_archive_sha256`

### `_POST_MATCH_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_POST_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "name",
    "importance_raw",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `grid_feature_id`
  - `source_feature_id`
  - `name`
  - `importance_raw`
  - `asset_status_raw`
  - `source_department_code`
  - `source_edition`
  - `source_archive_sha256`

### `_LINE_OUTPUT_MAPPING`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_line_proxy_distance_m",
    "grid_feature_id": "nearest_line_grid_feature_id",
    "source_feature_id": "nearest_line_source_feature_id",
    "tie_count": "nearest_line_tie_count",
    "voltage_raw": "nearest_line_voltage_raw",
    "voltage_status": "nearest_line_voltage_status",
    "voltage_kv": "nearest_line_voltage_kv",
    "voltage_upper_bound_kv": "nearest_line_voltage_upper_bound_kv",
    "manager_name": "nearest_line_manager_name",
    "asset_status_raw": "nearest_line_asset_status_raw",
    "source_department_code": "nearest_line_source_department_code",
    "source_edition": "nearest_line_source_edition",
    "source_archive_sha256": "nearest_line_source_archive_sha256",
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `distance_m`
  - `grid_feature_id`
  - `source_feature_id`
  - `tie_count`
  - `voltage_raw`
  - `voltage_status`
  - `voltage_kv`
  - `voltage_upper_bound_kv`
  - `manager_name`
  - `asset_status_raw`
  - `source_department_code`
  - `source_edition`
  - `source_archive_sha256`

### `_EXACT_LINE_OUTPUT_MAPPING`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_EXACT_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_exact_line_proxy_distance_m",
    "grid_feature_id": "nearest_exact_line_grid_feature_id",
    "source_feature_id": "nearest_exact_line_source_feature_id",
    "tie_count": "nearest_exact_line_tie_count",
    "voltage_kv": "nearest_exact_line_voltage_kv",
    "manager_name": "nearest_exact_line_manager_name",
    "asset_status_raw": "nearest_exact_line_asset_status_raw",
    "source_department_code": "nearest_exact_line_source_department_code",
    "source_edition": "nearest_exact_line_source_edition",
    "source_archive_sha256": "nearest_exact_line_source_archive_sha256",
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `distance_m`
  - `grid_feature_id`
  - `source_feature_id`
  - `tie_count`
  - `voltage_kv`
  - `manager_name`
  - `asset_status_raw`
  - `source_department_code`
  - `source_edition`
  - `source_archive_sha256`

### `_POST_OUTPUT_MAPPING`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_POST_OUTPUT_MAPPING = {
    "distance_m": "nearest_post_proxy_distance_m",
    "grid_feature_id": "nearest_post_grid_feature_id",
    "source_feature_id": "nearest_post_source_feature_id",
    "tie_count": "nearest_post_tie_count",
    "name": "nearest_post_name",
    "importance_raw": "nearest_post_importance_raw",
    "asset_status_raw": "nearest_post_asset_status_raw",
    "source_department_code": "nearest_post_source_department_code",
    "source_edition": "nearest_post_source_edition",
    "source_archive_sha256": "nearest_post_source_archive_sha256",
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `distance_m`
  - `grid_feature_id`
  - `source_feature_id`
  - `tie_count`
  - `name`
  - `importance_raw`
  - `asset_status_raw`
  - `source_department_code`
  - `source_edition`
  - `source_archive_sha256`

### `_PARCEL_OUTPUT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_PARCEL_OUTPUT_COLUMNS = frozenset(
    {
        *_LINE_OUTPUT_MAPPING.values(),
        *_EXACT_LINE_OUTPUT_MAPPING.values(),
        *_POST_OUTPUT_MAPPING.values(),
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `GridProximityError`

**Source purpose:** Raised when grid-proximity inputs or results are unsafe.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- constructor call: `landscout.stages.enrich_grid_proximity::_validated_crs` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validated_crs` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_require_lambert93` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_require_lambert93` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_active_geometry` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_active_geometry` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_id_values` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_id_values` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_parcels` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_parcels` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_reject_parcel_output_collisions` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_reject_parcel_output_collisions` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_grid` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_grid` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_nearest_feature_rows` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_nearest_feature_rows` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_distance_values` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_distance_values` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_tie_counts` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_tie_counts` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_match_integrity` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_match_integrity` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_voltage_coverage` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_voltage_coverage` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_exact_representation_consistency` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_exact_representation_consistency` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_validate_output_integrity` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_output_integrity` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `GridProximityError`
- constructor call: `landscout.stages.enrich_grid_proximity::_distance_profile` via `GridProximityError`
- value/type reference: `landscout.stages.enrich_grid_proximity::_distance_profile` via `GridProximityError`

**Exact class source**

```python
class GridProximityError(ValueError):
    """Raised when grid-proximity inputs or results are unsafe."""
```

### `VoltageLevelCoverage`

**Source purpose:** Source-line coverage for one dynamically observed exact voltage.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `voltage_kv` | `float` | `required` | `voltage_kv: float` |
| `line_feature_count` | `int` | `required` | `line_feature_count: int` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_voltage_coverage` via `VoltageLevelCoverage`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `VoltageLevelCoverage`
- constructor call: `landscout.stages.enrich_grid_proximity::_voltage_level_table` via `VoltageLevelCoverage`
- value/type reference: `landscout.stages.enrich_grid_proximity::_voltage_level_table` via `VoltageLevelCoverage`

**Exact class source**

```python
class VoltageLevelCoverage:
    """Source-line coverage for one dynamically observed exact voltage."""

    voltage_kv: float
    line_feature_count: int
```

### `GridProximityResult`

**Source purpose:** Parcel enrichment and dynamic exact-voltage proximity output.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | `parcels: gpd.GeoDataFrame` |
| `voltage_level_proximity` | `pd.DataFrame` | `required` | `voltage_level_proximity: pd.DataFrame` |
| `voltage_level_coverage` | `tuple[VoltageLevelCoverage, ...]` | `required` | `voltage_level_coverage: tuple[VoltageLevelCoverage, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_proximity_source_identity` via `GridProximityResult`
- constructor call: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `GridProximityResult`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `GridProximityResult`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `GridProximityResult`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `GridProximityResult`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_output_integrity` via `GridProximityResult`
- constructor call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `GridProximityResult`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `GridProximityResult`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `GridProximityResult`
- value/type reference: `landscout.stages.enrich_grid_proximity::profile_grid_proximity` via `GridProximityResult`

**Exact class source**

```python
class GridProximityResult:
    """Parcel enrichment and dynamic exact-voltage proximity output."""

    parcels: gpd.GeoDataFrame
    voltage_level_proximity: pd.DataFrame
    voltage_level_coverage: tuple[VoltageLevelCoverage, ...]
```

### `DistanceProfile`

**Source purpose:** Threshold-free distribution summary for one distance field.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `count` | `int` | `required` | `count: int` |
| `missing_count` | `int` | `required` | `missing_count: int` |
| `minimum` | `float \| None` | `required` | `minimum: float \| None` |
| `p01` | `float \| None` | `required` | `p01: float \| None` |
| `p05` | `float \| None` | `required` | `p05: float \| None` |
| `p10` | `float \| None` | `required` | `p10: float \| None` |
| `p25` | `float \| None` | `required` | `p25: float \| None` |
| `p50` | `float \| None` | `required` | `p50: float \| None` |
| `p75` | `float \| None` | `required` | `p75: float \| None` |
| `p90` | `float \| None` | `required` | `p90: float \| None` |
| `p95` | `float \| None` | `required` | `p95: float \| None` |
| `p99` | `float \| None` | `required` | `p99: float \| None` |
| `maximum` | `float \| None` | `required` | `maximum: float \| None` |
| `zero_distance_count` | `int` | `required` | `zero_distance_count: int` |
| `tie_count` | `int` | `required` | `tie_count: int` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- constructor call: `landscout.stages.enrich_grid_proximity::_distance_profile` via `DistanceProfile`
- value/type reference: `landscout.stages.enrich_grid_proximity::_distance_profile` via `DistanceProfile`

**Exact class source**

```python
class DistanceProfile:
    """Threshold-free distribution summary for one distance field."""

    count: int
    missing_count: int
    minimum: float | None
    p01: float | None
    p05: float | None
    p10: float | None
    p25: float | None
    p50: float | None
    p75: float | None
    p90: float | None
    p95: float | None
    p99: float | None
    maximum: float | None
    zero_distance_count: int
    tie_count: int
```

### `VoltageLevelDistanceProfile`

**Source purpose:** Distance distribution and source coverage for one exact voltage.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `voltage_kv` | `float` | `required` | `voltage_kv: float` |
| `line_feature_count` | `int` | `required` | `line_feature_count: int` |
| `parcel_proximity_count` | `int` | `required` | `parcel_proximity_count: int` |
| `distance` | `DistanceProfile` | `required` | `distance: DistanceProfile` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- constructor call: `landscout.stages.enrich_grid_proximity::profile_grid_proximity` via `VoltageLevelDistanceProfile`
- value/type reference: `landscout.stages.enrich_grid_proximity::profile_grid_proximity` via `VoltageLevelDistanceProfile`

**Exact class source**

```python
class VoltageLevelDistanceProfile:
    """Distance distribution and source coverage for one exact voltage."""

    voltage_kv: float
    line_feature_count: int
    parcel_proximity_count: int
    distance: DistanceProfile
```

### `GridProximityProfile`

**Source purpose:** Threshold-free parcel and voltage-level proximity profiles.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `parcel_count` | `int` | `required` | `parcel_count: int` |
| `nearest_line` | `DistanceProfile` | `required` | `nearest_line: DistanceProfile` |
| `nearest_exact_line` | `DistanceProfile` | `required` | `nearest_exact_line: DistanceProfile` |
| `nearest_post` | `DistanceProfile` | `required` | `nearest_post: DistanceProfile` |
| `voltage_levels` | `tuple[VoltageLevelDistanceProfile, ...]` | `required` | `voltage_levels: tuple[VoltageLevelDistanceProfile, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- constructor call: `landscout.stages.enrich_grid_proximity::profile_grid_proximity` via `GridProximityProfile`
- value/type reference: `landscout.stages.enrich_grid_proximity::profile_grid_proximity` via `GridProximityProfile`

**Exact class source**

```python
class GridProximityProfile:
    """Threshold-free parcel and voltage-level proximity profiles."""

    parcel_count: int
    nearest_line: DistanceProfile
    nearest_exact_line: DistanceProfile
    nearest_post: DistanceProfile
    voltage_levels: tuple[VoltageLevelDistanceProfile, ...]
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_validated_crs`

**Purpose:** Implements `validated crs` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validated_crs(value: object, label: str) -> CRS:
```

- Exact decorators: none.
- Declared return annotation: `CRS`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `CRS.from_user_input(value)`
- Explicit raise paths:
  - `GridProximityError(f"{label} CRS is required")` under lexical guard `value is None`.
  - `GridProximityError(f"{label} CRS is unreadable")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_require_lambert93` via `_validated_crs`
- value/type reference: `landscout.stages.enrich_grid_proximity::_require_lambert93` via `_validated_crs`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_parcels` via `_validated_crs`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_parcels` via `_validated_crs`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_output_integrity` via `_validated_crs`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_output_integrity` via `_validated_crs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |

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
def _validated_crs(value: object, label: str) -> CRS:
    if value is None:
        raise GridProximityError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise GridProximityError(f"{label} CRS is unreadable") from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_require_lambert93`

**Purpose:** Implements `require lambert93` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _require_lambert93(value: object, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridProximityError(f"{label} must use EPSG:2154")` under lexical guard `not actual.is_projected or not actual.equals(expected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_grid` via `_require_lambert93`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_grid` via `_require_lambert93`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_crs` | `landscout.stages.enrich_grid_proximity._validated_crs` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `actual.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |

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
def _require_lambert93(value: object, label: str) -> None:
    actual = _validated_crs(value, label)
    expected = CRS.from_epsg(2154)
    if not actual.is_projected or not actual.equals(expected):
        raise GridProximityError(f"{label} must use EPSG:2154")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_active_geometry`

**Purpose:** Implements `validate active geometry` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridProximityError(f"{label} geometry column is required")` under lexical guard `"geometry" not in frame.columns`.
  - `GridProximityError(f"{label} geometry column must be active")` under lexical guard `frame.active_geometry_name != "geometry"`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_parcels` via `_validate_active_geometry`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_parcels` via `_validate_active_geometry`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_grid` via `_validate_active_geometry`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_grid` via `_validate_active_geometry`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |

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
def _validate_active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise GridProximityError(f"{label} geometry column is required")
    if frame.active_geometry_name != "geometry":
        raise GridProximityError(f"{label} geometry column must be active")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_id_values`

**Purpose:** Implements `validate id values` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_id_values(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |
| `require_unique` | keyword-only | `bool` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridProximityError(f"{label} values must not be null")` under lexical guard `values.isna().any()`.
  - `GridProximityError(f"{label} values must be strings")` under lexical guard `any(not isinstance(value, str) for value in raw_values)`.
  - `GridProximityError(f"{label} values must not be empty")` under lexical guard `any(not value.strip() for value in raw_values)`.
  - `GridProximityError(<br>            f"{label} values must not contain leading or trailing whitespace"<br>        )` under lexical guard `any(value != value.strip() for value in raw_values)`.
  - `GridProximityError(f"{label} values must be unique")` under lexical guard `require_unique and values.duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_parcels` via `_validate_id_values`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_parcels` via `_validate_id_values`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `_validate_id_values`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `_validate_id_values`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_exact_representation_consistency` via `_validate_id_values`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_exact_representation_consistency` via `_validate_id_values`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `values.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `values.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_id_values(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise GridProximityError(f"{label} values must not be null")
    raw_values = values.tolist()
    if any(not isinstance(value, str) for value in raw_values):
        raise GridProximityError(f"{label} values must be strings")
    if any(not value.strip() for value in raw_values):
        raise GridProximityError(f"{label} values must not be empty")
    if any(value != value.strip() for value in raw_values):
        raise GridProximityError(
            f"{label} values must not contain leading or trailing whitespace"
        )
    if require_unique and values.duplicated().any():
        raise GridProximityError(f"{label} values must be unique")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_parcels`

**Purpose:** Implements `validate parcels` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
```

- Exact decorators: none.
- Declared return annotation: `CRS`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `source_crs`
- Explicit raise paths:
  - `GridProximityError(<br>            "Missing required parcel columns: " + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `GridProximityError("Parcel geometries must not be null")` under lexical guard `parcels.geometry.isna().any()`.
  - `GridProximityError("Parcel geometries must not be empty")` under lexical guard `parcels.geometry.is_empty.any()`.
  - `GridProximityError("Parcel geometries must be valid")` under lexical guard `not parcels.geometry.is_valid.all()`.
  - `GridProximityError(<br>            "Parcel geometries must be Polygon or MultiPolygon; found: "<br>            + ", ".join(unsupported)<br>        )` under lexical guard `unsupported`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_parcels`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_parcels`
- direct call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_validate_parcels`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_validate_parcels`
- direct call: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `_validate_parcels`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `_validate_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_active_geometry` | `landscout.stages.enrich_grid_proximity._validate_active_geometry` |
| `_validated_crs` | `landscout.stages.enrich_grid_proximity._validated_crs` |
| `_validate_id_values` | `landscout.stages.enrich_grid_proximity._validate_id_values` |
| `parcels.geometry.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.is_empty.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.is_valid.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_validate_active_geometry`<br>`parcels.geometry.isna().any`<br>`parcels.geometry.isna`<br>`parcels.geometry.is_empty.any`<br>`parcels.geometry.is_valid.all`<br>`parcels.geometry.geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
    missing = PARCEL_REQUIRED_COLUMNS - set(parcels.columns)
    if missing:
        raise GridProximityError(
            "Missing required parcel columns: " + ", ".join(sorted(missing))
        )
    _validate_active_geometry(parcels, "Parcel")
    source_crs = _validated_crs(parcels.crs, "Parcel")
    _validate_id_values(parcels["parcel_id"], "parcel_id", require_unique=True)
    if parcels.geometry.isna().any():
        raise GridProximityError("Parcel geometries must not be null")
    if parcels.geometry.is_empty.any():
        raise GridProximityError("Parcel geometries must not be empty")
    if not parcels.geometry.is_valid.all():
        raise GridProximityError("Parcel geometries must be valid")
    geometry_types = set(parcels.geometry.geom_type.dropna())
    unsupported = sorted(str(value) for value in geometry_types - PARCEL_GEOMETRY_TYPES)
    if unsupported:
        raise GridProximityError(
            "Parcel geometries must be Polygon or MultiPolygon; found: "
            + ", ".join(unsupported)
        )
    return source_crs
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_reject_parcel_output_collisions`

**Purpose:** Implements `reject parcel output collisions` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _reject_parcel_output_collisions(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridProximityError(<br>            "Parcel input collides with generated grid-proximity columns: "<br>            + ", ".join(sorted(collisions))<br>        )` under lexical guard `collisions`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_reject_parcel_output_collisions`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_reject_parcel_output_collisions`
- direct call: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `_reject_parcel_output_collisions`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `_reject_parcel_output_collisions`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _reject_parcel_output_collisions(parcels: gpd.GeoDataFrame) -> None:
    collisions = _PARCEL_OUTPUT_COLUMNS & set(parcels.columns)
    if collisions:
        raise GridProximityError(
            "Parcel input collides with generated grid-proximity columns: "
            + ", ".join(sorted(collisions))
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_observed_geometry_status`

**Purpose:** Implements `observed geometry status` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _observed_geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
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
- direct call: `landscout.stages.enrich_grid_proximity::_validate_grid` via `_observed_geometry_status`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_grid` via `_observed_geometry_status`

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
def _observed_geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
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

### `_validate_grid`

**Purpose:** Implements `validate grid` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_grid(
    frame: gpd.GeoDataFrame,
    *,
    label: str,
    required_columns: frozenset[str],
    feature_type: str,
    allowed_geometry_types: frozenset[str],
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `label` | keyword-only | `str` | `required` |
| `required_columns` | keyword-only | `frozenset[str]` | `required` |
| `feature_type` | keyword-only | `str` | `required` |
| `allowed_geometry_types` | keyword-only | `frozenset[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame.loc[valid_mask].reset_index(drop=True).copy()`
- Explicit raise paths:
  - `GridProximityError(<br>            f"Missing required {label} columns: " + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `GridProximityError(f"{label} grid_feature_id values must not be null")` under lexical guard `identifiers.isna().any()`.
  - `GridProximityError(<br>            f"{label} grid_feature_id values must be non-empty strings"<br>        )` under lexical guard `any(not isinstance(value, str) or not value for value in identifiers.tolist())`.
  - `GridProximityError(f"{label} grid_feature_id values must be unique")` under lexical guard `identifiers.duplicated().any()`.
  - `GridProximityError(f"{label} grid_feature_type must be {feature_type}")` under lexical guard `frame["grid_feature_type"].isna().any()<br>        or not frame["grid_feature_type"].eq(feature_type).all()`.
  - `GridProximityError(f"{label} spatial_role must be PROXY_GEOMETRY")` under lexical guard `frame["spatial_role"].isna().any()<br>        or not frame["spatial_role"].eq(SPATIAL_ROLE).all()`.
  - `GridProximityError(f"{label} has unexpected geometry_status values")` under lexical guard `declared_status.isna().any() or not declared_values <= GRID_GEOMETRY_STATUSES`.
  - `GridProximityError(<br>            f"{label} geometry_status does not match the source geometry"<br>        )` under lexical guard `not declared_status.astype("object").equals(observed_status)`.
  - `GridProximityError(<br>            f"{label} has unsupported VALID geometry types: " + ", ".join(unsupported)<br>        )` under lexical guard `unsupported`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_validate_grid`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_validate_grid`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_active_geometry` | `landscout.stages.enrich_grid_proximity._validate_active_geometry` |
| `_require_lambert93` | `landscout.stages.enrich_grid_proximity._require_lambert93` |
| `identifiers.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["grid_feature_type"].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["grid_feature_type"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["grid_feature_type"].eq(feature_type).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["grid_feature_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["spatial_role"].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["spatial_role"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["spatial_role"].eq(SPATIAL_ROLE).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["spatial_role"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_observed_geometry_status` | `landscout.stages.enrich_grid_proximity._observed_geometry_status` |
| `declared_status.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `declared_status.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `declared_status.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `declared_status.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `declared_status.astype("object").equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `declared_status.astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.loc[valid_mask, "geometry"].geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.loc[valid_mask].reset_index(drop=True).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.loc[valid_mask].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_validate_active_geometry`<br>`_observed_geometry_status`<br>`frame.loc[valid_mask, "geometry"].geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_grid(
    frame: gpd.GeoDataFrame,
    *,
    label: str,
    required_columns: frozenset[str],
    feature_type: str,
    allowed_geometry_types: frozenset[str],
) -> gpd.GeoDataFrame:
    missing = required_columns - set(frame.columns)
    if missing:
        raise GridProximityError(
            f"Missing required {label} columns: " + ", ".join(sorted(missing))
        )
    _validate_active_geometry(frame, label)
    _require_lambert93(frame.crs, label)

    identifiers = frame["grid_feature_id"]
    if identifiers.isna().any():
        raise GridProximityError(f"{label} grid_feature_id values must not be null")
    if any(not isinstance(value, str) or not value for value in identifiers.tolist()):
        raise GridProximityError(
            f"{label} grid_feature_id values must be non-empty strings"
        )
    if identifiers.duplicated().any():
        raise GridProximityError(f"{label} grid_feature_id values must be unique")
    if (
        frame["grid_feature_type"].isna().any()
        or not frame["grid_feature_type"].eq(feature_type).all()
    ):
        raise GridProximityError(f"{label} grid_feature_type must be {feature_type}")
    if (
        frame["spatial_role"].isna().any()
        or not frame["spatial_role"].eq(SPATIAL_ROLE).all()
    ):
        raise GridProximityError(f"{label} spatial_role must be PROXY_GEOMETRY")

    declared_status = frame["geometry_status"]
    observed_status = _observed_geometry_status(frame.geometry)
    declared_values = set(declared_status.dropna().unique())
    if declared_status.isna().any() or not declared_values <= GRID_GEOMETRY_STATUSES:
        raise GridProximityError(f"{label} has unexpected geometry_status values")
    if not declared_status.astype("object").equals(observed_status):
        raise GridProximityError(
            f"{label} geometry_status does not match the source geometry"
        )

    valid_mask = declared_status == "VALID"
    valid_types = set(frame.loc[valid_mask, "geometry"].geom_type.dropna())
    unsupported = sorted(str(value) for value in valid_types - allowed_geometry_types)
    if unsupported:
        raise GridProximityError(
            f"{label} has unsupported VALID geometry types: " + ", ".join(unsupported)
        )
    return frame.loc[valid_mask].reset_index(drop=True).copy()
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_finite_real_as_float`

**Purpose:** Implements `finite real as float` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _finite_real_as_float(value: object) -> float | None:
```

- Exact decorators: none.
- Declared return annotation: `float | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `numeric if isfinite(numeric) else None`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_is_positive_finite_number` via `_finite_real_as_float`
- value/type reference: `landscout.stages.enrich_grid_proximity::_is_positive_finite_number` via `_finite_real_as_float`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_distance_values` via `_finite_real_as_float`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_distance_values` via `_finite_real_as_float`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_tie_counts` via `_finite_real_as_float`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_tie_counts` via `_finite_real_as_float`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _finite_real_as_float(value: object) -> float | None:
    if not isinstance(value, Real) or isinstance(value, bool):
        return None
    try:
        numeric = float(value)
    except (OverflowError, TypeError, ValueError):
        return None
    return numeric if isfinite(numeric) else None
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_positive_finite_number`

**Purpose:** Implements `is positive finite number` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _is_positive_finite_number(value: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `numeric is not None and numeric > 0`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_match_integrity` via `_is_positive_finite_number`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_voltage_coverage` via `_is_positive_finite_number`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_voltage_coverage` via `_is_positive_finite_number`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `_is_positive_finite_number`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_is_positive_finite_number`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_finite_real_as_float` | `landscout.stages.enrich_grid_proximity._finite_real_as_float` |

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
def _is_positive_finite_number(value: object) -> bool:
    numeric = _finite_real_as_float(value)
    return numeric is not None and numeric > 0
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_calculation_geometries`

**Purpose:** Implements `calculation geometries` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
```

- Exact decorators: none.
- Declared return annotation: `np.ndarray`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `np.asarray(force_2d(values), dtype=object)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_nearest_feature_rows` via `_calculation_geometries`
- value/type reference: `landscout.stages.enrich_grid_proximity::_nearest_feature_rows` via `_calculation_geometries`
- direct call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_calculation_geometries`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_calculation_geometries`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `np.asarray` | `numpy.asarray` |
| `force_2d` | `shapely.force_2d` |

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
def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
    values = np.asarray(frame.geometry.array, dtype=object)
    return np.asarray(force_2d(values), dtype=object)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_empty_nearest_result`

**Purpose:** Implements `empty nearest result` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _empty_nearest_result(
    parcel_count: int,
    attribute_columns: tuple[str, ...],
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_count` | positional-or-keyword | `int` | `required` |
| `attribute_columns` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_nearest_feature_rows` via `_empty_nearest_result`
- value/type reference: `landscout.stages.enrich_grid_proximity::_nearest_feature_rows` via `_empty_nearest_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `pd.RangeIndex` | `pandas.RangeIndex` |
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
| In-memory mutation | `output["distance_m"] = pd.Series(np.nan, index=output.index, dtype="float64")`<br>`output["tie_count"] = pd.Series(pd.NA, index=output.index, dtype="Int64")`<br>`output[column] = pd.Series(np.nan, index=output.index, dtype="float64")`<br>`output[column] = pd.Series(pd.NA, index=output.index, dtype="object")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _empty_nearest_result(
    parcel_count: int,
    attribute_columns: tuple[str, ...],
) -> pd.DataFrame:
    output = pd.DataFrame(index=pd.RangeIndex(parcel_count))
    output["distance_m"] = pd.Series(np.nan, index=output.index, dtype="float64")
    output["tie_count"] = pd.Series(pd.NA, index=output.index, dtype="Int64")
    for column in attribute_columns:
        if column in {"voltage_kv", "voltage_upper_bound_kv"}:
            output[column] = pd.Series(np.nan, index=output.index, dtype="float64")
        else:
            output[column] = pd.Series(pd.NA, index=output.index, dtype="object")
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_nearest_feature_rows`

**Purpose:** Implements `nearest feature rows` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _nearest_feature_rows(
    parcel_geometries: np.ndarray,
    features: gpd.GeoDataFrame,
    attribute_columns: tuple[str, ...],
    *,
    allow_empty: bool = False,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_geometries` | positional-or-keyword | `np.ndarray` | `required` |
| `features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `attribute_columns` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `allow_empty` | keyword-only | `bool` | `False` |

**Return and exception contract**

- Exact observed return expressions:
  - `_empty_nearest_result(parcel_count, attribute_columns)`
  - `output`
- Explicit raise paths:
  - `GridProximityError("No VALID grid proxy feature is available")` under lexical guard `features.empty`.
  - `GridProximityError(<br>            "Nearest-neighbour matching did not cover every parcel"<br>        )` under lexical guard `selected["parcel_position"].tolist() != list(range(parcel_count))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_voltage_level_table` via `_nearest_feature_rows`
- value/type reference: `landscout.stages.enrich_grid_proximity::_voltage_level_table` via `_nearest_feature_rows`
- direct call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_nearest_feature_rows`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_nearest_feature_rows`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_empty_nearest_result` | `landscout.stages.enrich_grid_proximity._empty_nearest_result` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `_calculation_geometries` | `landscout.stages.enrich_grid_proximity._calculation_geometries` |
| `STRtree` | `shapely.STRtree` |
| `tree.query_nearest` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `features.iloc[matches["feature_position"].to_numpy()][<br>        "grid_feature_id"<br>    ].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches["feature_position"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.groupby("parcel_position", sort=False).size` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.drop_duplicates("parcel_position", keep="first").sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.drop_duplicates` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected["parcel_position"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected["feature_position"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `features.iloc[feature_positions].loc[:, list(attribute_columns)].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.insert` | `unresolved local/third-party receiver; no ownership inferred` |
| `ties.reindex(range(parcel_count)).to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `ties.reindex` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected["distance_m"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `selected["distance_m"].to_numpy` |
| External process/environment | None directly present. |
| In-memory mutation | `matches["grid_feature_id"] = features.iloc[matches["feature_position"].to_numpy()][<br>        "grid_feature_id"<br>    ].to_numpy()`<br>`output.insert(0, "tie_count", ties.reindex(range(parcel_count)).to_numpy())`<br>`output.insert(0, "distance_m", selected["distance_m"].to_numpy(dtype="float64"))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _nearest_feature_rows(
    parcel_geometries: np.ndarray,
    features: gpd.GeoDataFrame,
    attribute_columns: tuple[str, ...],
    *,
    allow_empty: bool = False,
) -> pd.DataFrame:
    parcel_count = len(parcel_geometries)
    if features.empty:
        if allow_empty:
            return _empty_nearest_result(parcel_count, attribute_columns)
        raise GridProximityError("No VALID grid proxy feature is available")

    feature_geometries = _calculation_geometries(features)
    tree = STRtree(feature_geometries)
    indices, distances = tree.query_nearest(
        parcel_geometries,
        all_matches=True,
        return_distance=True,
    )
    matches = pd.DataFrame(
        {
            "parcel_position": indices[0],
            "feature_position": indices[1],
            "distance_m": distances,
        }
    )
    matches["grid_feature_id"] = features.iloc[matches["feature_position"].to_numpy()][
        "grid_feature_id"
    ].to_numpy()
    matches = matches.sort_values(
        ["parcel_position", "distance_m", "grid_feature_id"],
        kind="mergesort",
    )
    ties = matches.groupby("parcel_position", sort=False).size()
    selected = matches.drop_duplicates("parcel_position", keep="first").sort_values(
        "parcel_position"
    )
    if selected["parcel_position"].tolist() != list(range(parcel_count)):
        raise GridProximityError(
            "Nearest-neighbour matching did not cover every parcel"
        )

    feature_positions = selected["feature_position"].to_numpy()
    output = features.iloc[feature_positions].loc[:, list(attribute_columns)].copy()
    output = output.reset_index(drop=True)
    output.insert(0, "tie_count", ties.reindex(range(parcel_count)).to_numpy())
    output.insert(0, "distance_m", selected["distance_m"].to_numpy(dtype="float64"))
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_attach_matches`

**Purpose:** Implements `attach matches` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _attach_matches(
    parcels: gpd.GeoDataFrame,
    matches: pd.DataFrame,
    mapping: dict[str, str],
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `matches` | positional-or-keyword | `pd.DataFrame` | `required` |
| `mapping` | positional-or-keyword | `dict[str, str]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_attach_matches`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_attach_matches`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `mapping.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches[source_column].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `parcels[output_column] = matches[source_column].reset_index(drop=True)` |
| Direct parameter mutation | `parcels[output_column] = matches[source_column].reset_index(drop=True)` |

**Complete source-ordered implementation**

```python
def _attach_matches(
    parcels: gpd.GeoDataFrame,
    matches: pd.DataFrame,
    mapping: dict[str, str],
) -> None:
    for source_column, output_column in mapping.items():
        parcels[output_column] = matches[source_column].reset_index(drop=True)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_distance_values`

**Purpose:** Implements `validate distance values` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_distance_values(values: pd.Series, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridProximityError(f"{label} distances must be numeric and finite")` under lexical guard `any(value is None for value in numeric_values)`.
  - `GridProximityError(f"{label} distances must be finite and >= 0")` under lexical guard `(numeric < 0).any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_match_integrity` via `_validate_distance_values`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_match_integrity` via `_validate_distance_values`
- direct call: `landscout.stages.enrich_grid_proximity::_distance_profile` via `_validate_distance_values`
- value/type reference: `landscout.stages.enrich_grid_proximity::_distance_profile` via `_validate_distance_values`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `values.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `_finite_real_as_float` | `landscout.stages.enrich_grid_proximity._finite_real_as_float` |
| `non_null.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `np.asarray` | `numpy.asarray` |
| `(numeric < 0).any` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_distance_values(values: pd.Series, label: str) -> None:
    non_null = values.dropna()
    numeric_values = [_finite_real_as_float(value) for value in non_null.tolist()]
    if any(value is None for value in numeric_values):
        raise GridProximityError(f"{label} distances must be numeric and finite")
    numeric = np.asarray(numeric_values, dtype="float64")
    if (numeric < 0).any():
        raise GridProximityError(f"{label} distances must be finite and >= 0")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_missing_scalar`

**Purpose:** Implements `is missing scalar` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

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
- direct call: `landscout.stages.enrich_grid_proximity::_validate_tie_counts` via `_is_missing_scalar`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_tie_counts` via `_is_missing_scalar`

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

### `_validate_tie_counts`

**Purpose:** Implements `validate tie counts` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_tie_counts(
    values: pd.Series,
    matched: pd.Series,
    label: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `pd.Series` | `required` |
| `matched` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridProximityError(f"{label} tie-count state is inconsistent")` under lexical guard `len(values) != len(matched)`.
  - `GridProximityError(<br>                    f"{label} unmatched rows must have null tie_count"<br>                )` under lexical guard `not row_is_matched`.
  - `GridProximityError(f"{label} matched rows require tie_count")` under lexical guard `missing`.
  - `GridProximityError(f"{label} tie_count must be a finite integer >= 1")` under lexical guard `numeric is None or not numeric.is_integer() or numeric < 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_match_integrity` via `_validate_tie_counts`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_match_integrity` via `_validate_tie_counts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `matched.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_missing_scalar` | `landscout.stages.enrich_grid_proximity._is_missing_scalar` |
| `_finite_real_as_float` | `landscout.stages.enrich_grid_proximity._finite_real_as_float` |
| `numeric.is_integer` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_tie_counts(
    values: pd.Series,
    matched: pd.Series,
    label: str,
) -> None:
    if len(values) != len(matched):
        raise GridProximityError(f"{label} tie-count state is inconsistent")
    for value, row_is_matched in zip(
        values.tolist(), matched.to_numpy(dtype="bool"), strict=True
    ):
        missing = _is_missing_scalar(value)
        if not row_is_matched:
            if not missing:
                raise GridProximityError(
                    f"{label} unmatched rows must have null tie_count"
                )
            continue
        if missing:
            raise GridProximityError(f"{label} matched rows require tie_count")
        numeric = _finite_real_as_float(value)
        if numeric is None or not numeric.is_integer() or numeric < 1:
            raise GridProximityError(f"{label} tie_count must be a finite integer >= 1")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_match_integrity`

**Purpose:** Implements `validate match integrity` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_match_integrity(
    frame: pd.DataFrame,
    *,
    label: str,
    distance_column: str,
    grid_id_column: str,
    source_id_column: str,
    tie_column: str,
    expect_matches: bool,
    voltage_column: str | None = None,
    unmatched_null_columns: tuple[str, ...] = (),
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `label` | keyword-only | `str` | `required` |
| `distance_column` | keyword-only | `str` | `required` |
| `grid_id_column` | keyword-only | `str` | `required` |
| `source_id_column` | keyword-only | `str` | `required` |
| `tie_column` | keyword-only | `str` | `required` |
| `expect_matches` | keyword-only | `bool` | `required` |
| `voltage_column` | keyword-only | `str \| None` | `None` |
| `unmatched_null_columns` | keyword-only | `tuple[str, ...]` | `()` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
- Explicit raise paths:
  - `GridProximityError(<br>            f"Missing {label} match columns: " + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `GridProximityError(f"{label} requires a match for every parcel")` under lexical guard `expect_matches and not matched.all()`.
  - `GridProximityError(f"{label} must be entirely unmatched")` under lexical guard `not expect_matches and matched.any()`.
  - `GridProximityError(f"{label} matched rows require {column}")` under lexical guard `expect_matches`.
  - `GridProximityError(<br>                f"{label} voltage must be numeric, finite, and > 0"<br>            )` under lexical guard `expect_matches`.
  - `GridProximityError(f"Missing {label} match column: {column}")` under lexical guard `column not in frame.columns`.
  - `GridProximityError(f"{label} unmatched rows must have null {column}")` under lexical guard `frame[column].notna().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `_validate_match_integrity`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `_validate_match_integrity`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_match_integrity`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_match_integrity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `required.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `distance.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `matched.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `matched.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_distance_values` | `landscout.stages.enrich_grid_proximity._validate_distance_values` |
| `_validate_tie_counts` | `landscout.stages.enrich_grid_proximity._validate_tie_counts` |
| `frame[column].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[voltage_column].map(_is_positive_finite_number).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[voltage_column].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `null_columns.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].notna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].notna` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `distance.notna`<br>`_validate_distance_values` |
| External process/environment | None directly present. |
| In-memory mutation | `required.add(voltage_column)`<br>`null_columns.add(voltage_column)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_match_integrity(
    frame: pd.DataFrame,
    *,
    label: str,
    distance_column: str,
    grid_id_column: str,
    source_id_column: str,
    tie_column: str,
    expect_matches: bool,
    voltage_column: str | None = None,
    unmatched_null_columns: tuple[str, ...] = (),
) -> None:
    required = {distance_column, grid_id_column, source_id_column, tie_column}
    if voltage_column is not None:
        required.add(voltage_column)
    missing = required - set(frame.columns)
    if missing:
        raise GridProximityError(
            f"Missing {label} match columns: " + ", ".join(sorted(missing))
        )

    distance = frame[distance_column]
    matched = distance.notna()
    if expect_matches and not matched.all():
        raise GridProximityError(f"{label} requires a match for every parcel")
    if not expect_matches and matched.any():
        raise GridProximityError(f"{label} must be entirely unmatched")
    _validate_distance_values(distance, label)
    _validate_tie_counts(frame[tie_column], matched, label)

    id_columns = (grid_id_column, source_id_column)
    if expect_matches:
        for column in id_columns:
            if frame[column].isna().any():
                raise GridProximityError(f"{label} matched rows require {column}")
        if (
            voltage_column is not None
            and not frame[voltage_column].map(_is_positive_finite_number).all()
        ):
            raise GridProximityError(
                f"{label} voltage must be numeric, finite, and > 0"
            )
        return

    null_columns = set(unmatched_null_columns) | set(id_columns)
    if voltage_column is not None:
        null_columns.add(voltage_column)
    for column in null_columns:
        if column not in frame.columns:
            raise GridProximityError(f"Missing {label} match column: {column}")
        if frame[column].notna().any():
            raise GridProximityError(f"{label} unmatched rows must have null {column}")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_voltage_coverage`

**Purpose:** Implements `validate voltage coverage` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_voltage_coverage(
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[float, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `coverage` | positional-or-keyword | `tuple[VoltageLevelCoverage, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(levels)`
- Explicit raise paths:
  - `GridProximityError("Voltage coverage entries are invalid")` under lexical guard `not isinstance(item, VoltageLevelCoverage)`.
  - `GridProximityError(<br>                "Voltage coverage levels must be numeric, finite, and > 0"<br>            )` under lexical guard `not _is_positive_finite_number(item.voltage_kv)`.
  - `GridProximityError(<br>                "Voltage coverage line_feature_count must be an integer > 0"<br>            )` under lexical guard `not isinstance(item.line_feature_count, Integral)<br>            or isinstance(item.line_feature_count, bool)<br>            or item.line_feature_count <= 0`.
  - `GridProximityError("Voltage coverage levels must be unique")` under lexical guard `len(set(levels)) != len(levels)`.
  - `GridProximityError("Voltage coverage levels must be ascending")` under lexical guard `levels != sorted(levels)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `_validate_voltage_coverage`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_voltage_table` via `_validate_voltage_coverage`
- direct call: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_voltage_coverage`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_voltage_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `_is_positive_finite_number` | `landscout.stages.enrich_grid_proximity._is_positive_finite_number` |
| `levels.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `levels.append(float(item.voltage_kv))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_voltage_coverage(
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
    levels: list[float] = []
    for item in coverage:
        if not isinstance(item, VoltageLevelCoverage):
            raise GridProximityError("Voltage coverage entries are invalid")
        if not _is_positive_finite_number(item.voltage_kv):
            raise GridProximityError(
                "Voltage coverage levels must be numeric, finite, and > 0"
            )
        if (
            not isinstance(item.line_feature_count, Integral)
            or isinstance(item.line_feature_count, bool)
            or item.line_feature_count <= 0
        ):
            raise GridProximityError(
                "Voltage coverage line_feature_count must be an integer > 0"
            )
        levels.append(float(item.voltage_kv))
    if len(set(levels)) != len(levels):
        raise GridProximityError("Voltage coverage levels must be unique")
    if levels != sorted(levels):
        raise GridProximityError("Voltage coverage levels must be ascending")
    return tuple(levels)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_voltage_table`

**Purpose:** Implements `validate voltage table` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_voltage_table(
    table: pd.DataFrame,
    parcel_ids: pd.Series,
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[float, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `table` | positional-or-keyword | `pd.DataFrame` | `required` |
| `parcel_ids` | positional-or-keyword | `pd.Series` | `required` |
| `coverage` | positional-or-keyword | `tuple[VoltageLevelCoverage, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `levels`
- Explicit raise paths:
  - `GridProximityError(<br>            "Missing voltage proximity columns: " + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `GridProximityError("Voltage proximity row count is inconsistent")` under lexical guard `len(table) != expected_rows`.
  - `GridProximityError(<br>            "Voltage proximity levels must be numeric, finite, and > 0"<br>        )` under lexical guard `not raw_voltage_values.map(_is_positive_finite_number).all()`.
  - `GridProximityError(<br>            "Voltage proximity parcel/voltage pairs must be unique"<br>        )` under lexical guard `table.duplicated(["parcel_id", "voltage_kv"]).any()`.
  - `GridProximityError(<br>            "Voltage proximity levels do not match source coverage"<br>        )` under lexical guard `table_levels != levels`.
  - `GridProximityError(<br>                f"Voltage proximity does not contain the exact parcel set for {voltage_kv:g} kV"<br>            )` under lexical guard `len(rows) != len(expected_ids) or rows["parcel_id"].tolist() != expected_ids`.
  - `GridProximityError(f"Voltage-level matched rows require {column}")` under lexical guard `table[column].isna().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_voltage_table`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_voltage_table`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_voltage_coverage` | `landscout.stages.enrich_grid_proximity._validate_voltage_coverage` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_id_values` | `landscout.stages.enrich_grid_proximity._validate_id_values` |
| `raw_voltage_values.map(_is_positive_finite_number).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_voltage_values.map` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.duplicated(["parcel_id", "voltage_kv"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_voltage_values.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_ids.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_match_integrity` | `landscout.stages.enrich_grid_proximity._validate_match_integrity` |
| `table[column].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_voltage_table(
    table: pd.DataFrame,
    parcel_ids: pd.Series,
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
    missing = set(VOLTAGE_PROXIMITY_COLUMNS) - set(table.columns)
    if missing:
        raise GridProximityError(
            "Missing voltage proximity columns: " + ", ".join(sorted(missing))
        )
    levels = _validate_voltage_coverage(coverage)
    expected_rows = len(parcel_ids) * len(levels)
    if len(table) != expected_rows:
        raise GridProximityError("Voltage proximity row count is inconsistent")
    if table.empty:
        return levels

    _validate_id_values(table["parcel_id"], "parcel_id", require_unique=False)
    raw_voltage_values = table["voltage_kv"]
    if not raw_voltage_values.map(_is_positive_finite_number).all():
        raise GridProximityError(
            "Voltage proximity levels must be numeric, finite, and > 0"
        )
    if table.duplicated(["parcel_id", "voltage_kv"]).any():
        raise GridProximityError(
            "Voltage proximity parcel/voltage pairs must be unique"
        )
    table_levels = tuple(
        sorted({float(value) for value in raw_voltage_values.tolist()})
    )
    if table_levels != levels:
        raise GridProximityError(
            "Voltage proximity levels do not match source coverage"
        )

    expected_ids = parcel_ids.tolist()
    for voltage_kv in levels:
        rows = table.loc[raw_voltage_values.map(float) == voltage_kv]
        if len(rows) != len(expected_ids) or rows["parcel_id"].tolist() != expected_ids:
            raise GridProximityError(
                f"Voltage proximity does not contain the exact parcel set for {voltage_kv:g} kV"
            )

    _validate_match_integrity(
        table,
        label="Voltage-level line proximity",
        distance_column="nearest_line_proxy_distance_m",
        grid_id_column="nearest_line_grid_feature_id",
        source_id_column="nearest_line_source_feature_id",
        tie_column="tie_count",
        expect_matches=True,
    )
    for column in (
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    ):
        if table[column].isna().any():
            raise GridProximityError(f"Voltage-level matched rows require {column}")
    return levels
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_null_safe_series_equal`

**Purpose:** Implements `null safe series equal` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _null_safe_series_equal(actual: pd.Series, expected: pd.Series) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `actual` | positional-or-keyword | `pd.Series` | `required` |
| `expected` | positional-or-keyword | `pd.Series` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `False`
  - `bool((both_null \| equal_values).all())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_exact_representation_consistency` via `_null_safe_series_equal`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_exact_representation_consistency` via `_null_safe_series_equal`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual_values.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_values.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual_values.eq(expected_values).fillna` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual_values.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `(both_null \| equal_values).all` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _null_safe_series_equal(actual: pd.Series, expected: pd.Series) -> bool:
    actual_values = actual.reset_index(drop=True)
    expected_values = expected.reset_index(drop=True)
    if len(actual_values) != len(expected_values):
        return False
    both_null = actual_values.isna() & expected_values.isna()
    try:
        equal_values = actual_values.eq(expected_values).fillna(False)
    except (TypeError, ValueError):
        return False
    return bool((both_null | equal_values).all())
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_exact_representation_consistency`

**Purpose:** Implements `validate exact representation consistency` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_exact_representation_consistency(
    parcels: gpd.GeoDataFrame,
    voltage_table: pd.DataFrame,
    levels: tuple[float, ...],
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `voltage_table` | positional-or-keyword | `pd.DataFrame` | `required` |
| `levels` | positional-or-keyword | `tuple[float, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
- Explicit raise paths:
  - `GridProximityError(<br>            "Voltage-level proximity contains an unexpected parcel ID"<br>        )` under lexical guard `candidates["_parcel_position"].isna().any()`.
  - `GridProximityError("Voltage-level proximity does not cover every parcel")` under lexical guard `expected["parcel_id"].isna().any()`.
  - `GridProximityError(<br>            "Global exact-line distance is inconsistent with voltage-level proximity"<br>        )` under lexical guard `not actual_distance.eq(expected["_distance"].reset_index(drop=True)).all()`.
  - `GridProximityError(<br>                f"Global exact-line {parcel_column} is inconsistent with "<br>                "voltage-level proximity"<br>            )` under lexical guard `not _null_safe_series_equal(actual[parcel_column], expected[table_column])`.
  - `GridProximityError(<br>            "Global exact-line tie count is inconsistent with voltage-level proximity"<br>        )` under lexical guard `not actual_ties.eq(expected_ties.reset_index(drop=True)).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_exact_representation_consistency`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_result_contract` via `_validate_exact_representation_consistency`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `voltage_table.loc[:, list(selected_columns)].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_id_values` | `landscout.stages.enrich_grid_proximity._validate_id_values` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates["parcel_id"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates["_parcel_position"].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates["_parcel_position"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `candidates[distance_column].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates["tie_count"].map(int).astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates["tie_count"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates.sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `ordered.drop_duplicates` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.set_index("_parcel_position").reindex` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected["parcel_id"].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected["parcel_id"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates.groupby("_parcel_position", sort=False)[<br>        "_distance"<br>    ].transform` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates.groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates["_distance"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `tied_level_winners.groupby("_parcel_position", sort=False)[<br>        "_tie_count"<br>    ].agg` | `unresolved local/third-party receiver; no ownership inferred` |
| `tied_level_winners.groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_ties.reindex` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual["nearest_exact_line_proxy_distance_m"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual_distance.eq(expected["_distance"].reset_index(drop=True)).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual_distance.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected["_distance"].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_null_safe_series_equal` | `landscout.stages.enrich_grid_proximity._null_safe_series_equal` |
| `actual["nearest_exact_line_tie_count"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual_ties.eq(expected_ties.reset_index(drop=True)).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual_ties.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_ties.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `candidates[distance_column].map`<br>`candidates.groupby("_parcel_position", sort=False)[<br>        "_distance"<br>    ].transform`<br>`candidates["_distance"].eq`<br>`actual["nearest_exact_line_proxy_distance_m"].map`<br>`actual_distance.eq(expected["_distance"].reset_index(drop=True)).all`<br>`actual_distance.eq`<br>`expected["_distance"].reset_index` |
| External process/environment | None directly present. |
| In-memory mutation | `candidates["_parcel_position"] = candidates["parcel_id"].map(parcel_positions)`<br>`candidates["_distance"] = candidates[distance_column].map(float)`<br>`candidates["_tie_count"] = candidates["tie_count"].map(int).astype("object")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_exact_representation_consistency(
    parcels: gpd.GeoDataFrame,
    voltage_table: pd.DataFrame,
    levels: tuple[float, ...],
) -> None:
    if not levels:
        return

    distance_column = "nearest_line_proxy_distance_m"
    grid_id_column = "nearest_line_grid_feature_id"
    selected_columns = (
        "parcel_id",
        distance_column,
        grid_id_column,
        "nearest_line_source_feature_id",
        "voltage_kv",
        "tie_count",
        "manager_name",
        "asset_status_raw",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    )
    candidates = voltage_table.loc[:, list(selected_columns)].copy()
    _validate_id_values(
        candidates[grid_id_column],
        "Voltage-level nearest grid_feature_id",
        require_unique=False,
    )
    parcel_positions = {
        parcel_id: position
        for position, parcel_id in enumerate(parcels["parcel_id"].tolist())
    }
    candidates["_parcel_position"] = candidates["parcel_id"].map(parcel_positions)
    if candidates["_parcel_position"].isna().any():
        raise GridProximityError(
            "Voltage-level proximity contains an unexpected parcel ID"
        )
    candidates["_distance"] = candidates[distance_column].map(float)
    candidates["_tie_count"] = candidates["tie_count"].map(int).astype("object")

    ordered = candidates.sort_values(
        ["_parcel_position", "_distance", grid_id_column],
        kind="mergesort",
    )
    expected = ordered.drop_duplicates("_parcel_position", keep="first")
    expected = expected.set_index("_parcel_position").reindex(range(len(parcels)))
    if expected["parcel_id"].isna().any():
        raise GridProximityError("Voltage-level proximity does not cover every parcel")

    minimum_distance = candidates.groupby("_parcel_position", sort=False)[
        "_distance"
    ].transform("min")
    tied_level_winners = candidates.loc[candidates["_distance"].eq(minimum_distance)]
    expected_ties = tied_level_winners.groupby("_parcel_position", sort=False)[
        "_tie_count"
    ].agg(lambda values: sum(values.tolist()))
    expected_ties = expected_ties.reindex(range(len(parcels)))

    actual = parcels.reset_index(drop=True)
    actual_distance = actual["nearest_exact_line_proxy_distance_m"].map(float)
    if not actual_distance.eq(expected["_distance"].reset_index(drop=True)).all():
        raise GridProximityError(
            "Global exact-line distance is inconsistent with voltage-level proximity"
        )

    field_mapping = (
        ("nearest_exact_line_grid_feature_id", grid_id_column),
        ("nearest_exact_line_source_feature_id", "nearest_line_source_feature_id"),
        ("nearest_exact_line_voltage_kv", "voltage_kv"),
        ("nearest_exact_line_manager_name", "manager_name"),
        ("nearest_exact_line_asset_status_raw", "asset_status_raw"),
        ("nearest_exact_line_source_department_code", "source_department_code"),
        ("nearest_exact_line_source_edition", "source_edition"),
        ("nearest_exact_line_source_archive_sha256", "source_archive_sha256"),
    )
    for parcel_column, table_column in field_mapping:
        if not _null_safe_series_equal(actual[parcel_column], expected[table_column]):
            raise GridProximityError(
                f"Global exact-line {parcel_column} is inconsistent with "
                "voltage-level proximity"
            )

    actual_ties = actual["nearest_exact_line_tie_count"].map(int)
    if not actual_ties.eq(expected_ties.reset_index(drop=True)).all():
        raise GridProximityError(
            "Global exact-line tie count is inconsistent with voltage-level proximity"
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_result_contract`

**Purpose:** Implements `validate result contract` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_result_contract(result: GridProximityResult) -> tuple[float, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[float, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `GridProximityResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `levels`
- Explicit raise paths:
  - `GridProximityError(<br>            "Missing proximity result columns: " + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `GridProximityError(<br>            "Nearest exact-line voltage does not match source coverage"<br>        )` under lexical guard `levels<br>        and not parcels["nearest_exact_line_voltage_kv"].map(float).isin(levels).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_validate_output_integrity` via `_validate_result_contract`
- value/type reference: `landscout.stages.enrich_grid_proximity::_validate_output_integrity` via `_validate_result_contract`
- direct call: `landscout.stages.enrich_grid_proximity::profile_grid_proximity` via `_validate_result_contract`
- value/type reference: `landscout.stages.enrich_grid_proximity::profile_grid_proximity` via `_validate_result_contract`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_parcels` | `landscout.stages.enrich_grid_proximity._validate_parcels` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_LINE_OUTPUT_MAPPING.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `_EXACT_LINE_OUTPUT_MAPPING.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `_POST_OUTPUT_MAPPING.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_voltage_coverage` | `landscout.stages.enrich_grid_proximity._validate_voltage_coverage` |
| `_validate_match_integrity` | `landscout.stages.enrich_grid_proximity._validate_match_integrity` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["nearest_exact_line_voltage_kv"].map(float).isin(levels).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["nearest_exact_line_voltage_kv"].map(float).isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["nearest_exact_line_voltage_kv"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_voltage_table` | `landscout.stages.enrich_grid_proximity._validate_voltage_table` |
| `_validate_exact_representation_consistency` | `landscout.stages.enrich_grid_proximity._validate_exact_representation_consistency` |

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
def _validate_result_contract(result: GridProximityResult) -> tuple[float, ...]:
    parcels = result.parcels
    _validate_parcels(parcels)
    required_proximity_columns = (
        set(_LINE_OUTPUT_MAPPING.values())
        | set(_EXACT_LINE_OUTPUT_MAPPING.values())
        | set(_POST_OUTPUT_MAPPING.values())
    )
    missing = required_proximity_columns - set(parcels.columns)
    if missing:
        raise GridProximityError(
            "Missing proximity result columns: " + ", ".join(sorted(missing))
        )
    levels = _validate_voltage_coverage(result.voltage_level_coverage)
    _validate_match_integrity(
        parcels,
        label="Nearest line proximity",
        distance_column="nearest_line_proxy_distance_m",
        grid_id_column="nearest_line_grid_feature_id",
        source_id_column="nearest_line_source_feature_id",
        tie_column="nearest_line_tie_count",
        expect_matches=True,
    )
    _validate_match_integrity(
        parcels,
        label="Nearest post proximity",
        distance_column="nearest_post_proxy_distance_m",
        grid_id_column="nearest_post_grid_feature_id",
        source_id_column="nearest_post_source_feature_id",
        tie_column="nearest_post_tie_count",
        expect_matches=True,
    )
    _validate_match_integrity(
        parcels,
        label="Nearest exact-line proximity",
        distance_column="nearest_exact_line_proxy_distance_m",
        grid_id_column="nearest_exact_line_grid_feature_id",
        source_id_column="nearest_exact_line_source_feature_id",
        tie_column="nearest_exact_line_tie_count",
        expect_matches=bool(levels),
        voltage_column="nearest_exact_line_voltage_kv",
        unmatched_null_columns=tuple(_EXACT_LINE_OUTPUT_MAPPING.values()),
    )
    if (
        levels
        and not parcels["nearest_exact_line_voltage_kv"].map(float).isin(levels).all()
    ):
        raise GridProximityError(
            "Nearest exact-line voltage does not match source coverage"
        )
    _validate_voltage_table(
        result.voltage_level_proximity,
        parcels["parcel_id"],
        result.voltage_level_coverage,
    )
    _validate_exact_representation_consistency(
        parcels,
        result.voltage_level_proximity,
        levels,
    )
    return levels
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_output_integrity`

**Purpose:** Implements `validate output integrity` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _validate_output_integrity(
    source_parcels: gpd.GeoDataFrame,
    result: GridProximityResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `result` | positional-or-keyword | `GridProximityResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridProximityError("Grid proximity enrichment changed parcel count")` under lexical guard `len(output) != len(source_parcels)`.
  - `GridProximityError(<br>            "Grid proximity enrichment changed parcel IDs or order"<br>        )` under lexical guard `not source_ids.equals(output_ids)`.
  - `GridProximityError("Enriched parcel CRS changed")` under lexical guard `not source_crs.equals(output_crs)`.
  - `GridProximityError("Enriched parcel geometry changed")` under lexical guard `not output.geometry.geom_equals_exact(<br>        source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False<br>    ).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_validate_output_integrity`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_validate_output_integrity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_result_contract` | `landscout.stages.enrich_grid_proximity._validate_result_contract` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `source_parcels["parcel_id"].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["parcel_id"].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_ids.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_crs` | `landscout.stages.enrich_grid_proximity._validated_crs` |
| `source_crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.geometry.geom_equals_exact(<br>        source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False<br>    ).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.geometry.geom_equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_parcels.geometry.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `output.geometry.geom_equals_exact(<br>        source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False<br>    ).all`<br>`output.geometry.geom_equals_exact`<br>`source_parcels.geometry.reset_index` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_output_integrity(
    source_parcels: gpd.GeoDataFrame,
    result: GridProximityResult,
) -> None:
    _validate_result_contract(result)
    output = result.parcels
    if len(output) != len(source_parcels):
        raise GridProximityError("Grid proximity enrichment changed parcel count")
    source_ids = source_parcels["parcel_id"].reset_index(drop=True)
    output_ids = output["parcel_id"].reset_index(drop=True)
    if not source_ids.equals(output_ids):
        raise GridProximityError(
            "Grid proximity enrichment changed parcel IDs or order"
        )
    source_crs = _validated_crs(source_parcels.crs, "Input parcel")
    output_crs = _validated_crs(output.crs, "Output parcel")
    if not source_crs.equals(output_crs):
        raise GridProximityError("Enriched parcel CRS changed")
    if not output.geometry.geom_equals_exact(
        source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False
    ).all():
        raise GridProximityError("Enriched parcel geometry changed")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_voltage_level_table`

**Purpose:** Implements `voltage level table` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _voltage_level_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    exact_lines: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_ids` | positional-or-keyword | `pd.Series` | `required` |
| `parcel_geometries` | positional-or-keyword | `np.ndarray` | `required` |
| `exact_lines` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `empty, ()`
  - `pd.concat(tables, ignore_index=True), tuple(coverage)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_voltage_level_table`
- value/type reference: `landscout.stages.enrich_grid_proximity::_enrich_parcel_grid_proximity_from_normalized` via `_voltage_level_table`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `exact_lines["voltage_kv"].unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `exact_lines.loc[exact_lines["voltage_kv"] == voltage_kv].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `coverage.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `VoltageLevelCoverage` | `landscout.stages.enrich_grid_proximity.VoltageLevelCoverage` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_nearest_feature_rows` | `landscout.stages.enrich_grid_proximity._nearest_feature_rows` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `parcel_ids.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `tables.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `empty["voltage_kv"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `empty[<br>            "nearest_line_proxy_distance_m"<br>        ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `empty["tie_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.concat` | `pandas.concat` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `empty[<br>            "nearest_line_proxy_distance_m"<br>        ].astype` |
| External process/environment | None directly present. |
| In-memory mutation | `coverage.append(<br>            VoltageLevelCoverage(<br>                voltage_kv=voltage_kv,<br>                line_feature_count=len(level_lines),<br>            )<br>        )`<br>`tables.append(table.loc[:, list(VOLTAGE_PROXIMITY_COLUMNS)])`<br>`empty["voltage_kv"] = empty["voltage_kv"].astype("float64")`<br>`empty["nearest_line_proxy_distance_m"] = empty[<br>            "nearest_line_proxy_distance_m"<br>        ].astype("float64")`<br>`empty["tie_count"] = empty["tie_count"].astype("Int64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _voltage_level_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    exact_lines: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]:
    levels = tuple(sorted(float(value) for value in exact_lines["voltage_kv"].unique()))
    tables: list[pd.DataFrame] = []
    coverage: list[VoltageLevelCoverage] = []
    for voltage_kv in levels:
        level_lines = exact_lines.loc[exact_lines["voltage_kv"] == voltage_kv].copy()
        coverage.append(
            VoltageLevelCoverage(
                voltage_kv=voltage_kv,
                line_feature_count=len(level_lines),
            )
        )
        nearest = _nearest_feature_rows(
            parcel_geometries,
            level_lines,
            (
                "grid_feature_id",
                "source_feature_id",
                "manager_name",
                "asset_status_raw",
                "source_department_code",
                "source_edition",
                "source_archive_sha256",
            ),
        )
        table = pd.DataFrame(
            {
                "parcel_id": parcel_ids.reset_index(drop=True),
                "voltage_kv": voltage_kv,
                "nearest_line_proxy_distance_m": nearest["distance_m"],
                "nearest_line_grid_feature_id": nearest["grid_feature_id"],
                "nearest_line_source_feature_id": nearest["source_feature_id"],
                "tie_count": nearest["tie_count"],
                "manager_name": nearest["manager_name"],
                "asset_status_raw": nearest["asset_status_raw"],
                "source_department_code": nearest["source_department_code"],
                "source_edition": nearest["source_edition"],
                "source_archive_sha256": nearest["source_archive_sha256"],
            }
        )
        tables.append(table.loc[:, list(VOLTAGE_PROXIMITY_COLUMNS)])

    if not tables:
        empty = pd.DataFrame(columns=list(VOLTAGE_PROXIMITY_COLUMNS))
        empty["voltage_kv"] = empty["voltage_kv"].astype("float64")
        empty["nearest_line_proxy_distance_m"] = empty[
            "nearest_line_proxy_distance_m"
        ].astype("float64")
        empty["tie_count"] = empty["tie_count"].astype("Int64")
        return empty, ()
    return pd.concat(tables, ignore_index=True), tuple(coverage)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_enrich_parcel_grid_proximity_from_normalized`

**Purpose:** Attach nearest IGN proxy matches using planar XY distance in EPSG:2154.

    IGN Z values are removed from calculation-only copies and do not affect
    horizontal proximity. Source parcel and normalized IGN geometries are not
    mutated. Distances describe only the nearest feature inside loaded proxy
    coverage and do not establish connection feasibility.

**Exact signature**

```python
def _enrich_parcel_grid_proximity_from_normalized(
    parcels: gpd.GeoDataFrame,
    electric_lines: gpd.GeoDataFrame,
    transformation_posts: gpd.GeoDataFrame,
) -> GridProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `GridProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `electric_lines` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `transformation_posts` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `GridProximityError("No VALID electric-line proxy is available")` under lexical guard `valid_lines.empty`.
  - `GridProximityError("No VALID transformation-post proxy is available")` under lexical guard `valid_posts.empty`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `_enrich_parcel_grid_proximity_from_normalized`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `_enrich_parcel_grid_proximity_from_normalized`
- import: `tests.unit.test_assess_grid_coverage::<module>` via `from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)`
- direct call: `tests.unit.test_assess_grid_coverage::_proximity` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::_proximity` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `enrich_parcel_grid_proximity`
- import: `tests.unit.test_enrich_grid_proximity::<module>` via `from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)`
- direct call: `tests.unit.test_enrich_grid_proximity::_two_parcel_two_voltage_result` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_two_parcel_two_voltage_result` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_separated_distance_uses_parcel_edge_not_centroid` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_separated_distance_uses_parcel_edge_not_centroid` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_touching_line_has_zero_distance` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_touching_line_has_zero_distance` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_post_distance_uses_parcel_and_post_polygons` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_post_distance_uses_parcel_and_post_polygons` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_epsg2154_parcel_input_remains_epsg2154` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_epsg2154_parcel_input_remains_epsg2154` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_valid_parcel_id_is_preserved_exactly` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_valid_parcel_id_is_preserved_exactly` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_invalid_parcel_id_hygiene_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_invalid_parcel_id_hygiene_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_supported_parcel_polygon_geometry_is_preserved` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_supported_parcel_polygon_geometry_is_preserved` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_semantically_wrong_parcel_geometry_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_semantically_wrong_parcel_geometry_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_missing_crs_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_missing_crs_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_crs_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_crs_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_z_line_has_same_horizontal_distance_as_xy_line` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_z_line_has_same_horizontal_distance_as_xy_line` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_line_tie_is_counted_and_lexical_feature_id_wins` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_line_tie_is_counted_and_lexical_feature_id_wins` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_cross_voltage_tie_uses_lexical_global_feature_id` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_cross_voltage_tie_uses_lexical_global_feature_id` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_feature_type_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_feature_type_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_duplicate_grid_feature_id_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_duplicate_grid_feature_id_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_spatial_role_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_spatial_role_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_unsupported_valid_grid_geometry_type_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_unsupported_valid_grid_geometry_type_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_supported_multi_geometries_are_accepted` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_supported_multi_geometries_are_accepted` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nearest_any_line_preserves_every_voltage_status` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nearest_any_line_preserves_every_voltage_status` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_invalid_exact_voltage_values_are_not_used_as_exact` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_invalid_exact_voltage_values_are_not_used_as_exact` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_missing_parcel_column_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_missing_parcel_column_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_null_parcel_id_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_null_parcel_id_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_duplicate_parcel_id_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_duplicate_parcel_id_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_bad_parcel_geometry_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_bad_parcel_geometry_is_rejected` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_distance_profile_is_threshold_free_and_tracks_ties` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_distance_profile_is_threshold_free_and_tracks_ties` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_allows_consistent_missing_manager_and_asset_status` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_allows_consistent_missing_manager_and_asset_status` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `enrich_parcel_grid_proximity`
- direct call: `tests.unit.test_enrich_grid_proximity::test_no_valid_required_grid_feature_is_rejected` via `enrich_parcel_grid_proximity`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_no_valid_required_grid_feature_is_rejected` via `enrich_parcel_grid_proximity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_parcels` | `landscout.stages.enrich_grid_proximity._validate_parcels` |
| `_reject_parcel_output_collisions` | `landscout.stages.enrich_grid_proximity._reject_parcel_output_collisions` |
| `_validate_grid` | `landscout.stages.enrich_grid_proximity._validate_grid` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `parcels.reset_index(drop=True).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_calculation_geometries` | `landscout.stages.enrich_grid_proximity._calculation_geometries` |
| `_nearest_feature_rows` | `landscout.stages.enrich_grid_proximity._nearest_feature_rows` |
| `_attach_matches` | `landscout.stages.enrich_grid_proximity._attach_matches` |
| `valid_lines[<br>        "voltage_kv"<br>    ].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_lines.loc[exact_mask].reset_index(drop=True).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_lines.loc[exact_mask].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `exact_lines["voltage_kv"].map(float).astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `exact_lines["voltage_kv"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `_voltage_level_table` | `landscout.stages.enrich_grid_proximity._voltage_level_table` |
| `GridProximityResult` | `landscout.stages.enrich_grid_proximity.GridProximityResult` |
| `_validate_output_integrity` | `landscout.stages.enrich_grid_proximity._validate_output_integrity` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `output.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `exact_lines["voltage_kv"] = exact_lines["voltage_kv"].map(float).astype("float64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _enrich_parcel_grid_proximity_from_normalized(
    parcels: gpd.GeoDataFrame,
    electric_lines: gpd.GeoDataFrame,
    transformation_posts: gpd.GeoDataFrame,
) -> GridProximityResult:
    """Attach nearest IGN proxy matches using planar XY distance in EPSG:2154.

    IGN Z values are removed from calculation-only copies and do not affect
    horizontal proximity. Source parcel and normalized IGN geometries are not
    mutated. Distances describe only the nearest feature inside loaded proxy
    coverage and do not establish connection feasibility.
    """

    _validate_parcels(parcels)
    _reject_parcel_output_collisions(parcels)
    valid_lines = _validate_grid(
        electric_lines,
        label="Electric-line grid",
        required_columns=LINE_REQUIRED_COLUMNS,
        feature_type="ELECTRIC_LINE",
        allowed_geometry_types=LINE_GEOMETRY_TYPES,
    )
    valid_posts = _validate_grid(
        transformation_posts,
        label="Transformation-post grid",
        required_columns=POST_REQUIRED_COLUMNS,
        feature_type="TRANSFORMATION_POST",
        allowed_geometry_types=POST_GEOMETRY_TYPES,
    )
    if valid_lines.empty:
        raise GridProximityError("No VALID electric-line proxy is available")
    if valid_posts.empty:
        raise GridProximityError("No VALID transformation-post proxy is available")

    output = parcels.reset_index(drop=True).copy()
    calculation_parcels = output.to_crs(CALCULATION_CRS)
    parcel_geometries = _calculation_geometries(calculation_parcels)

    nearest_line = _nearest_feature_rows(
        parcel_geometries,
        valid_lines,
        _LINE_MATCH_COLUMNS,
    )
    _attach_matches(output, nearest_line, _LINE_OUTPUT_MAPPING)

    exact_mask = (valid_lines["voltage_status"] == "EXACT") & valid_lines[
        "voltage_kv"
    ].map(_is_positive_finite_number)
    exact_lines = valid_lines.loc[exact_mask].reset_index(drop=True).copy()
    exact_lines["voltage_kv"] = exact_lines["voltage_kv"].map(float).astype("float64")
    nearest_exact = _nearest_feature_rows(
        parcel_geometries,
        exact_lines,
        _LINE_MATCH_COLUMNS,
        allow_empty=True,
    )
    _attach_matches(output, nearest_exact, _EXACT_LINE_OUTPUT_MAPPING)

    nearest_post = _nearest_feature_rows(
        parcel_geometries,
        valid_posts,
        _POST_MATCH_COLUMNS,
    )
    _attach_matches(output, nearest_post, _POST_OUTPUT_MAPPING)

    voltage_table, voltage_coverage = _voltage_level_table(
        output["parcel_id"], parcel_geometries, exact_lines
    )
    result = GridProximityResult(
        parcels=output,
        voltage_level_proximity=voltage_table,
        voltage_level_coverage=voltage_coverage,
    )
    _validate_output_integrity(parcels, result)
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `enrich_parcel_grid_proximity`

**Purpose:** Compute proximity from one physically revalidated IGN source bundle.

**Exact signature**

```python
def enrich_parcel_grid_proximity(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `GridProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `electricity_source` | positional-or-keyword | `IgnBdTopoElectricityData` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_enrich_parcel_grid_proximity_from_normalized(<br>            parcels,<br>            normalized.electric_lines,<br>            normalized.transformation_posts,<br>        )`
- Explicit raise paths:
  - `GridProximityError(<br>                "parcels must be a GeoDataFrame with active geometry"<br>            )` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `GridProximityError(<br>                "electricity source must be an IgnBdTopoElectricityData"<br>            )` under lexical guard `type(electricity_source) is not IgnBdTopoElectricityData`.
  - `GridProximityError("source_config must be an IgnBdTopoSourceConfig")` under lexical guard `type(source_config) is not IgnBdTopoSourceConfig`.
  - `GridProximityError(<br>                "IGN electricity normalization returned an invalid result"<br>            )` under lexical guard `type(normalized) is not NormalizedIgnElectricityData`.
  - `re-raise`.
  - `GridProximityError(<br>            "Parcel-to-grid proximity cannot be computed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- direct call: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `enrich_parcel_grid_proximity`
- value/type reference: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `enrich_parcel_grid_proximity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_parcels` | `landscout.stages.enrich_grid_proximity._validate_parcels` |
| `_reject_parcel_output_collisions` | `landscout.stages.enrich_grid_proximity._reject_parcel_output_collisions` |
| `normalize_ign_electricity` | `landscout.stages.normalize_grid_ign.normalize_ign_electricity` |
| `_enrich_parcel_grid_proximity_from_normalized` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |

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
def enrich_parcel_grid_proximity(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridProximityResult:
    """Compute proximity from one physically revalidated IGN source bundle."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise GridProximityError(
                "parcels must be a GeoDataFrame with active geometry"
            )
        if type(electricity_source) is not IgnBdTopoElectricityData:
            raise GridProximityError(
                "electricity source must be an IgnBdTopoElectricityData"
            )
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise GridProximityError("source_config must be an IgnBdTopoSourceConfig")
        _validate_parcels(parcels)
        _reject_parcel_output_collisions(parcels)
        normalized = normalize_ign_electricity(electricity_source, source_config)
        if type(normalized) is not NormalizedIgnElectricityData:
            raise GridProximityError(
                "IGN electricity normalization returned an invalid result"
            )
        return _enrich_parcel_grid_proximity_from_normalized(
            parcels,
            normalized.electric_lines,
            normalized.transformation_posts,
        )
    except GridProximityError:
        raise
    except Exception as error:
        raise GridProximityError(
            "Parcel-to-grid proximity cannot be computed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_distance_profile`

**Purpose:** Implements `distance profile` within the file role: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

**Exact signature**

```python
def _distance_profile(distances: pd.Series, ties: pd.Series) -> DistanceProfile:
```

- Exact decorators: none.
- Declared return annotation: `DistanceProfile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `distances` | positional-or-keyword | `pd.Series` | `required` |
| `ties` | positional-or-keyword | `pd.Series` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `DistanceProfile(<br>            count=0,<br>            missing_count=missing_count,<br>            minimum=None,<br>            p01=None,<br>            p05=None,<br>            p10=None,<br>            p25=None,<br>            p50=None,<br>            p75=None,<br>            p90=None,<br>            p95=None,<br>            p99=None,<br>            maximum=None,<br>            zero_distance_count=0,<br>            tie_count=0,<br>        )`
  - `DistanceProfile(<br>        count=len(values),<br>        missing_count=missing_count,<br>        minimum=float(values.min()),<br>        p01=float(values.quantile(0.01)),<br>        p05=float(values.quantile(0.05)),<br>        p10=float(values.quantile(0.10)),<br>        p25=float(values.quantile(0.25)),<br>        p50=float(values.quantile(0.50)),<br>        p75=float(values.quantile(0.75)),<br>        p90=float(values.quantile(0.90)),<br>        p95=float(values.quantile(0.95)),<br>        p99=float(values.quantile(0.99)),<br>        maximum=float(values.max()),<br>        zero_distance_count=int(values.eq(0).sum()),<br>        tie_count=sum(value > 1 for value in matched_ties.tolist()),<br>    )`
- Explicit raise paths:
  - `GridProximityError("Matched distance rows require tie counts")` under lexical guard `matched_ties.isna().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_grid_proximity::profile_grid_proximity` via `_distance_profile`
- value/type reference: `landscout.stages.enrich_grid_proximity::profile_grid_proximity` via `_distance_profile`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_distance_values` | `landscout.stages.enrich_grid_proximity._validate_distance_values` |
| `distances.dropna().astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `distances.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `distances.isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `distances.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `DistanceProfile` | `landscout.stages.enrich_grid_proximity.DistanceProfile` |
| `distances.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `matched_ties.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `matched_ties.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.min` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.quantile` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.max` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.eq(0).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `matched_ties.tolist` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_validate_distance_values`<br>`distances.dropna().astype`<br>`distances.dropna`<br>`distances.isna().sum`<br>`distances.isna`<br>`DistanceProfile`<br>`distances.notna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _distance_profile(distances: pd.Series, ties: pd.Series) -> DistanceProfile:
    _validate_distance_values(distances, "Profile")
    values = distances.dropna().astype("float64")
    missing_count = int(distances.isna().sum())
    if values.empty:
        return DistanceProfile(
            count=0,
            missing_count=missing_count,
            minimum=None,
            p01=None,
            p05=None,
            p10=None,
            p25=None,
            p50=None,
            p75=None,
            p90=None,
            p95=None,
            p99=None,
            maximum=None,
            zero_distance_count=0,
            tie_count=0,
        )
    matched_ties = ties.loc[distances.notna()]
    if matched_ties.isna().any():
        raise GridProximityError("Matched distance rows require tie counts")
    return DistanceProfile(
        count=len(values),
        missing_count=missing_count,
        minimum=float(values.min()),
        p01=float(values.quantile(0.01)),
        p05=float(values.quantile(0.05)),
        p10=float(values.quantile(0.10)),
        p25=float(values.quantile(0.25)),
        p50=float(values.quantile(0.50)),
        p75=float(values.quantile(0.75)),
        p90=float(values.quantile(0.90)),
        p95=float(values.quantile(0.95)),
        p99=float(values.quantile(0.99)),
        maximum=float(values.max()),
        zero_distance_count=int(values.eq(0).sum()),
        tie_count=sum(value > 1 for value in matched_ties.tolist()),
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `profile_grid_proximity`

**Purpose:** Profile proximity distances without thresholds or suitability labels.

**Exact signature**

```python
def profile_grid_proximity(result: GridProximityResult) -> GridProximityProfile:
```

- Exact decorators: none.
- Declared return annotation: `GridProximityProfile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `GridProximityResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GridProximityProfile(<br>        parcel_count=len(parcels),<br>        nearest_line=_distance_profile(<br>            parcels["nearest_line_proxy_distance_m"],<br>            parcels["nearest_line_tie_count"],<br>        ),<br>        nearest_exact_line=_distance_profile(<br>            parcels["nearest_exact_line_proxy_distance_m"],<br>            parcels["nearest_exact_line_tie_count"],<br>        ),<br>        nearest_post=_distance_profile(<br>            parcels["nearest_post_proxy_distance_m"],<br>            parcels["nearest_post_tie_count"],<br>        ),<br>        voltage_levels=tuple(voltage_profiles),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- direct call: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `profile_grid_proximity`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `profile_grid_proximity`
- direct call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `profile_grid_proximity`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `profile_grid_proximity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_result_contract` | `landscout.stages.enrich_grid_proximity._validate_result_contract` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_distance_profile` | `landscout.stages.enrich_grid_proximity._distance_profile` |
| `voltage_profiles.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `VoltageLevelDistanceProfile` | `landscout.stages.enrich_grid_proximity.VoltageLevelDistanceProfile` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridProximityProfile` | `landscout.stages.enrich_grid_proximity.GridProximityProfile` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_distance_profile`<br>`VoltageLevelDistanceProfile` |
| External process/environment | None directly present. |
| In-memory mutation | `voltage_profiles.append(<br>            VoltageLevelDistanceProfile(<br>                voltage_kv=voltage_kv,<br>                line_feature_count=coverage[voltage_kv],<br>                parcel_proximity_count=len(rows),<br>                distance=distance,<br>            )<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def profile_grid_proximity(result: GridProximityResult) -> GridProximityProfile:
    """Profile proximity distances without thresholds or suitability labels."""

    _validate_result_contract(result)
    parcels = result.parcels
    coverage = {
        float(item.voltage_kv): item.line_feature_count
        for item in result.voltage_level_coverage
    }
    voltage_profiles: list[VoltageLevelDistanceProfile] = []
    table = result.voltage_level_proximity
    observed_levels = tuple(coverage)
    for voltage_kv in observed_levels:
        rows = table.loc[table["voltage_kv"] == voltage_kv]
        distance = _distance_profile(
            rows["nearest_line_proxy_distance_m"], rows["tie_count"]
        )
        voltage_profiles.append(
            VoltageLevelDistanceProfile(
                voltage_kv=voltage_kv,
                line_feature_count=coverage[voltage_kv],
                parcel_proximity_count=len(rows),
                distance=distance,
            )
        )

    return GridProximityProfile(
        parcel_count=len(parcels),
        nearest_line=_distance_profile(
            parcels["nearest_line_proxy_distance_m"],
            parcels["nearest_line_tie_count"],
        ),
        nearest_exact_line=_distance_profile(
            parcels["nearest_exact_line_proxy_distance_m"],
            parcels["nearest_exact_line_tie_count"],
        ),
        nearest_post=_distance_profile(
            parcels["nearest_post_proxy_distance_m"],
            parcels["nearest_post_tie_count"],
        ),
        voltage_levels=tuple(voltage_profiles),
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `PARCEL_REQUIRED_COLUMNS`, `LINE_REQUIRED_COLUMNS`, `POST_REQUIRED_COLUMNS`, `VOLTAGE_PROXIMITY_COLUMNS`, `_LINE_MATCH_COLUMNS`, `_POST_MATCH_COLUMNS`, `_LINE_OUTPUT_MAPPING`, `_EXACT_LINE_OUTPUT_MAPPING`, `_POST_OUTPUT_MAPPING`, `_PARCEL_OUTPUT_COLUMNS`.
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
"""Compute diagnostic parcel proximity to normalized IGN electricity proxies."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from numbers import Integral, Real

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pandas.api.types import is_scalar  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import STRtree, force_2d  # type: ignore[import-untyped]

from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
)
from landscout.stages.normalize_grid_ign import (
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
)

CALCULATION_CRS = "EPSG:2154"
SPATIAL_ROLE = "PROXY_GEOMETRY"

PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
LINE_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "voltage_raw",
        "voltage_status",
        "voltage_kv",
        "voltage_upper_bound_kv",
        "manager_name",
        "asset_status_raw",
        "geometry",
    }
)
POST_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "name",
        "importance_raw",
        "asset_status_raw",
        "geometry",
    }
)
GRID_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
LINE_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
POST_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})

VOLTAGE_PROXIMITY_COLUMNS = (
    "parcel_id",
    "voltage_kv",
    "nearest_line_proxy_distance_m",
    "nearest_line_grid_feature_id",
    "nearest_line_source_feature_id",
    "tie_count",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)

_LINE_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "voltage_raw",
    "voltage_status",
    "voltage_kv",
    "voltage_upper_bound_kv",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
_POST_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "name",
    "importance_raw",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)

_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_line_proxy_distance_m",
    "grid_feature_id": "nearest_line_grid_feature_id",
    "source_feature_id": "nearest_line_source_feature_id",
    "tie_count": "nearest_line_tie_count",
    "voltage_raw": "nearest_line_voltage_raw",
    "voltage_status": "nearest_line_voltage_status",
    "voltage_kv": "nearest_line_voltage_kv",
    "voltage_upper_bound_kv": "nearest_line_voltage_upper_bound_kv",
    "manager_name": "nearest_line_manager_name",
    "asset_status_raw": "nearest_line_asset_status_raw",
    "source_department_code": "nearest_line_source_department_code",
    "source_edition": "nearest_line_source_edition",
    "source_archive_sha256": "nearest_line_source_archive_sha256",
}
_EXACT_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_exact_line_proxy_distance_m",
    "grid_feature_id": "nearest_exact_line_grid_feature_id",
    "source_feature_id": "nearest_exact_line_source_feature_id",
    "tie_count": "nearest_exact_line_tie_count",
    "voltage_kv": "nearest_exact_line_voltage_kv",
    "manager_name": "nearest_exact_line_manager_name",
    "asset_status_raw": "nearest_exact_line_asset_status_raw",
    "source_department_code": "nearest_exact_line_source_department_code",
    "source_edition": "nearest_exact_line_source_edition",
    "source_archive_sha256": "nearest_exact_line_source_archive_sha256",
}
_POST_OUTPUT_MAPPING = {
    "distance_m": "nearest_post_proxy_distance_m",
    "grid_feature_id": "nearest_post_grid_feature_id",
    "source_feature_id": "nearest_post_source_feature_id",
    "tie_count": "nearest_post_tie_count",
    "name": "nearest_post_name",
    "importance_raw": "nearest_post_importance_raw",
    "asset_status_raw": "nearest_post_asset_status_raw",
    "source_department_code": "nearest_post_source_department_code",
    "source_edition": "nearest_post_source_edition",
    "source_archive_sha256": "nearest_post_source_archive_sha256",
}
_PARCEL_OUTPUT_COLUMNS = frozenset(
    {
        *_LINE_OUTPUT_MAPPING.values(),
        *_EXACT_LINE_OUTPUT_MAPPING.values(),
        *_POST_OUTPUT_MAPPING.values(),
    }
)


class GridProximityError(ValueError):
    """Raised when grid-proximity inputs or results are unsafe."""


@dataclass(frozen=True)
class VoltageLevelCoverage:
    """Source-line coverage for one dynamically observed exact voltage."""

    voltage_kv: float
    line_feature_count: int


@dataclass(frozen=True)
class GridProximityResult:
    """Parcel enrichment and dynamic exact-voltage proximity output."""

    parcels: gpd.GeoDataFrame
    voltage_level_proximity: pd.DataFrame
    voltage_level_coverage: tuple[VoltageLevelCoverage, ...]


@dataclass(frozen=True)
class DistanceProfile:
    """Threshold-free distribution summary for one distance field."""

    count: int
    missing_count: int
    minimum: float | None
    p01: float | None
    p05: float | None
    p10: float | None
    p25: float | None
    p50: float | None
    p75: float | None
    p90: float | None
    p95: float | None
    p99: float | None
    maximum: float | None
    zero_distance_count: int
    tie_count: int


@dataclass(frozen=True)
class VoltageLevelDistanceProfile:
    """Distance distribution and source coverage for one exact voltage."""

    voltage_kv: float
    line_feature_count: int
    parcel_proximity_count: int
    distance: DistanceProfile


@dataclass(frozen=True)
class GridProximityProfile:
    """Threshold-free parcel and voltage-level proximity profiles."""

    parcel_count: int
    nearest_line: DistanceProfile
    nearest_exact_line: DistanceProfile
    nearest_post: DistanceProfile
    voltage_levels: tuple[VoltageLevelDistanceProfile, ...]


def _validated_crs(value: object, label: str) -> CRS:
    if value is None:
        raise GridProximityError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise GridProximityError(f"{label} CRS is unreadable") from error


def _require_lambert93(value: object, label: str) -> None:
    actual = _validated_crs(value, label)
    expected = CRS.from_epsg(2154)
    if not actual.is_projected or not actual.equals(expected):
        raise GridProximityError(f"{label} must use EPSG:2154")


def _validate_active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise GridProximityError(f"{label} geometry column is required")
    if frame.active_geometry_name != "geometry":
        raise GridProximityError(f"{label} geometry column must be active")


def _validate_id_values(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise GridProximityError(f"{label} values must not be null")
    raw_values = values.tolist()
    if any(not isinstance(value, str) for value in raw_values):
        raise GridProximityError(f"{label} values must be strings")
    if any(not value.strip() for value in raw_values):
        raise GridProximityError(f"{label} values must not be empty")
    if any(value != value.strip() for value in raw_values):
        raise GridProximityError(
            f"{label} values must not contain leading or trailing whitespace"
        )
    if require_unique and values.duplicated().any():
        raise GridProximityError(f"{label} values must be unique")


def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
    missing = PARCEL_REQUIRED_COLUMNS - set(parcels.columns)
    if missing:
        raise GridProximityError(
            "Missing required parcel columns: " + ", ".join(sorted(missing))
        )
    _validate_active_geometry(parcels, "Parcel")
    source_crs = _validated_crs(parcels.crs, "Parcel")
    _validate_id_values(parcels["parcel_id"], "parcel_id", require_unique=True)
    if parcels.geometry.isna().any():
        raise GridProximityError("Parcel geometries must not be null")
    if parcels.geometry.is_empty.any():
        raise GridProximityError("Parcel geometries must not be empty")
    if not parcels.geometry.is_valid.all():
        raise GridProximityError("Parcel geometries must be valid")
    geometry_types = set(parcels.geometry.geom_type.dropna())
    unsupported = sorted(str(value) for value in geometry_types - PARCEL_GEOMETRY_TYPES)
    if unsupported:
        raise GridProximityError(
            "Parcel geometries must be Polygon or MultiPolygon; found: "
            + ", ".join(unsupported)
        )
    return source_crs


def _reject_parcel_output_collisions(parcels: gpd.GeoDataFrame) -> None:
    collisions = _PARCEL_OUTPUT_COLUMNS & set(parcels.columns)
    if collisions:
        raise GridProximityError(
            "Parcel input collides with generated grid-proximity columns: "
            + ", ".join(sorted(collisions))
        )


def _observed_geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
    status = pd.Series("VALID", index=geometry.index, dtype="object")
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    status.loc[null_mask] = "NULL"
    status.loc[empty_mask] = "EMPTY"
    status.loc[invalid_mask] = "INVALID"
    return status


def _validate_grid(
    frame: gpd.GeoDataFrame,
    *,
    label: str,
    required_columns: frozenset[str],
    feature_type: str,
    allowed_geometry_types: frozenset[str],
) -> gpd.GeoDataFrame:
    missing = required_columns - set(frame.columns)
    if missing:
        raise GridProximityError(
            f"Missing required {label} columns: " + ", ".join(sorted(missing))
        )
    _validate_active_geometry(frame, label)
    _require_lambert93(frame.crs, label)

    identifiers = frame["grid_feature_id"]
    if identifiers.isna().any():
        raise GridProximityError(f"{label} grid_feature_id values must not be null")
    if any(not isinstance(value, str) or not value for value in identifiers.tolist()):
        raise GridProximityError(
            f"{label} grid_feature_id values must be non-empty strings"
        )
    if identifiers.duplicated().any():
        raise GridProximityError(f"{label} grid_feature_id values must be unique")
    if (
        frame["grid_feature_type"].isna().any()
        or not frame["grid_feature_type"].eq(feature_type).all()
    ):
        raise GridProximityError(f"{label} grid_feature_type must be {feature_type}")
    if (
        frame["spatial_role"].isna().any()
        or not frame["spatial_role"].eq(SPATIAL_ROLE).all()
    ):
        raise GridProximityError(f"{label} spatial_role must be PROXY_GEOMETRY")

    declared_status = frame["geometry_status"]
    observed_status = _observed_geometry_status(frame.geometry)
    declared_values = set(declared_status.dropna().unique())
    if declared_status.isna().any() or not declared_values <= GRID_GEOMETRY_STATUSES:
        raise GridProximityError(f"{label} has unexpected geometry_status values")
    if not declared_status.astype("object").equals(observed_status):
        raise GridProximityError(
            f"{label} geometry_status does not match the source geometry"
        )

    valid_mask = declared_status == "VALID"
    valid_types = set(frame.loc[valid_mask, "geometry"].geom_type.dropna())
    unsupported = sorted(str(value) for value in valid_types - allowed_geometry_types)
    if unsupported:
        raise GridProximityError(
            f"{label} has unsupported VALID geometry types: " + ", ".join(unsupported)
        )
    return frame.loc[valid_mask].reset_index(drop=True).copy()


def _finite_real_as_float(value: object) -> float | None:
    if not isinstance(value, Real) or isinstance(value, bool):
        return None
    try:
        numeric = float(value)
    except (OverflowError, TypeError, ValueError):
        return None
    return numeric if isfinite(numeric) else None


def _is_positive_finite_number(value: object) -> bool:
    numeric = _finite_real_as_float(value)
    return numeric is not None and numeric > 0


def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
    values = np.asarray(frame.geometry.array, dtype=object)
    return np.asarray(force_2d(values), dtype=object)


def _empty_nearest_result(
    parcel_count: int,
    attribute_columns: tuple[str, ...],
) -> pd.DataFrame:
    output = pd.DataFrame(index=pd.RangeIndex(parcel_count))
    output["distance_m"] = pd.Series(np.nan, index=output.index, dtype="float64")
    output["tie_count"] = pd.Series(pd.NA, index=output.index, dtype="Int64")
    for column in attribute_columns:
        if column in {"voltage_kv", "voltage_upper_bound_kv"}:
            output[column] = pd.Series(np.nan, index=output.index, dtype="float64")
        else:
            output[column] = pd.Series(pd.NA, index=output.index, dtype="object")
    return output


def _nearest_feature_rows(
    parcel_geometries: np.ndarray,
    features: gpd.GeoDataFrame,
    attribute_columns: tuple[str, ...],
    *,
    allow_empty: bool = False,
) -> pd.DataFrame:
    parcel_count = len(parcel_geometries)
    if features.empty:
        if allow_empty:
            return _empty_nearest_result(parcel_count, attribute_columns)
        raise GridProximityError("No VALID grid proxy feature is available")

    feature_geometries = _calculation_geometries(features)
    tree = STRtree(feature_geometries)
    indices, distances = tree.query_nearest(
        parcel_geometries,
        all_matches=True,
        return_distance=True,
    )
    matches = pd.DataFrame(
        {
            "parcel_position": indices[0],
            "feature_position": indices[1],
            "distance_m": distances,
        }
    )
    matches["grid_feature_id"] = features.iloc[matches["feature_position"].to_numpy()][
        "grid_feature_id"
    ].to_numpy()
    matches = matches.sort_values(
        ["parcel_position", "distance_m", "grid_feature_id"],
        kind="mergesort",
    )
    ties = matches.groupby("parcel_position", sort=False).size()
    selected = matches.drop_duplicates("parcel_position", keep="first").sort_values(
        "parcel_position"
    )
    if selected["parcel_position"].tolist() != list(range(parcel_count)):
        raise GridProximityError(
            "Nearest-neighbour matching did not cover every parcel"
        )

    feature_positions = selected["feature_position"].to_numpy()
    output = features.iloc[feature_positions].loc[:, list(attribute_columns)].copy()
    output = output.reset_index(drop=True)
    output.insert(0, "tie_count", ties.reindex(range(parcel_count)).to_numpy())
    output.insert(0, "distance_m", selected["distance_m"].to_numpy(dtype="float64"))
    return output


def _attach_matches(
    parcels: gpd.GeoDataFrame,
    matches: pd.DataFrame,
    mapping: dict[str, str],
) -> None:
    for source_column, output_column in mapping.items():
        parcels[output_column] = matches[source_column].reset_index(drop=True)


def _validate_distance_values(values: pd.Series, label: str) -> None:
    non_null = values.dropna()
    numeric_values = [_finite_real_as_float(value) for value in non_null.tolist()]
    if any(value is None for value in numeric_values):
        raise GridProximityError(f"{label} distances must be numeric and finite")
    numeric = np.asarray(numeric_values, dtype="float64")
    if (numeric < 0).any():
        raise GridProximityError(f"{label} distances must be finite and >= 0")


def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    if not is_scalar(value):
        return False
    return bool(pd.isna(value))


def _validate_tie_counts(
    values: pd.Series,
    matched: pd.Series,
    label: str,
) -> None:
    if len(values) != len(matched):
        raise GridProximityError(f"{label} tie-count state is inconsistent")
    for value, row_is_matched in zip(
        values.tolist(), matched.to_numpy(dtype="bool"), strict=True
    ):
        missing = _is_missing_scalar(value)
        if not row_is_matched:
            if not missing:
                raise GridProximityError(
                    f"{label} unmatched rows must have null tie_count"
                )
            continue
        if missing:
            raise GridProximityError(f"{label} matched rows require tie_count")
        numeric = _finite_real_as_float(value)
        if numeric is None or not numeric.is_integer() or numeric < 1:
            raise GridProximityError(f"{label} tie_count must be a finite integer >= 1")


def _validate_match_integrity(
    frame: pd.DataFrame,
    *,
    label: str,
    distance_column: str,
    grid_id_column: str,
    source_id_column: str,
    tie_column: str,
    expect_matches: bool,
    voltage_column: str | None = None,
    unmatched_null_columns: tuple[str, ...] = (),
) -> None:
    required = {distance_column, grid_id_column, source_id_column, tie_column}
    if voltage_column is not None:
        required.add(voltage_column)
    missing = required - set(frame.columns)
    if missing:
        raise GridProximityError(
            f"Missing {label} match columns: " + ", ".join(sorted(missing))
        )

    distance = frame[distance_column]
    matched = distance.notna()
    if expect_matches and not matched.all():
        raise GridProximityError(f"{label} requires a match for every parcel")
    if not expect_matches and matched.any():
        raise GridProximityError(f"{label} must be entirely unmatched")
    _validate_distance_values(distance, label)
    _validate_tie_counts(frame[tie_column], matched, label)

    id_columns = (grid_id_column, source_id_column)
    if expect_matches:
        for column in id_columns:
            if frame[column].isna().any():
                raise GridProximityError(f"{label} matched rows require {column}")
        if (
            voltage_column is not None
            and not frame[voltage_column].map(_is_positive_finite_number).all()
        ):
            raise GridProximityError(
                f"{label} voltage must be numeric, finite, and > 0"
            )
        return

    null_columns = set(unmatched_null_columns) | set(id_columns)
    if voltage_column is not None:
        null_columns.add(voltage_column)
    for column in null_columns:
        if column not in frame.columns:
            raise GridProximityError(f"Missing {label} match column: {column}")
        if frame[column].notna().any():
            raise GridProximityError(f"{label} unmatched rows must have null {column}")


def _validate_voltage_coverage(
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
    levels: list[float] = []
    for item in coverage:
        if not isinstance(item, VoltageLevelCoverage):
            raise GridProximityError("Voltage coverage entries are invalid")
        if not _is_positive_finite_number(item.voltage_kv):
            raise GridProximityError(
                "Voltage coverage levels must be numeric, finite, and > 0"
            )
        if (
            not isinstance(item.line_feature_count, Integral)
            or isinstance(item.line_feature_count, bool)
            or item.line_feature_count <= 0
        ):
            raise GridProximityError(
                "Voltage coverage line_feature_count must be an integer > 0"
            )
        levels.append(float(item.voltage_kv))
    if len(set(levels)) != len(levels):
        raise GridProximityError("Voltage coverage levels must be unique")
    if levels != sorted(levels):
        raise GridProximityError("Voltage coverage levels must be ascending")
    return tuple(levels)


def _validate_voltage_table(
    table: pd.DataFrame,
    parcel_ids: pd.Series,
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
    missing = set(VOLTAGE_PROXIMITY_COLUMNS) - set(table.columns)
    if missing:
        raise GridProximityError(
            "Missing voltage proximity columns: " + ", ".join(sorted(missing))
        )
    levels = _validate_voltage_coverage(coverage)
    expected_rows = len(parcel_ids) * len(levels)
    if len(table) != expected_rows:
        raise GridProximityError("Voltage proximity row count is inconsistent")
    if table.empty:
        return levels

    _validate_id_values(table["parcel_id"], "parcel_id", require_unique=False)
    raw_voltage_values = table["voltage_kv"]
    if not raw_voltage_values.map(_is_positive_finite_number).all():
        raise GridProximityError(
            "Voltage proximity levels must be numeric, finite, and > 0"
        )
    if table.duplicated(["parcel_id", "voltage_kv"]).any():
        raise GridProximityError(
            "Voltage proximity parcel/voltage pairs must be unique"
        )
    table_levels = tuple(
        sorted({float(value) for value in raw_voltage_values.tolist()})
    )
    if table_levels != levels:
        raise GridProximityError(
            "Voltage proximity levels do not match source coverage"
        )

    expected_ids = parcel_ids.tolist()
    for voltage_kv in levels:
        rows = table.loc[raw_voltage_values.map(float) == voltage_kv]
        if len(rows) != len(expected_ids) or rows["parcel_id"].tolist() != expected_ids:
            raise GridProximityError(
                f"Voltage proximity does not contain the exact parcel set for {voltage_kv:g} kV"
            )

    _validate_match_integrity(
        table,
        label="Voltage-level line proximity",
        distance_column="nearest_line_proxy_distance_m",
        grid_id_column="nearest_line_grid_feature_id",
        source_id_column="nearest_line_source_feature_id",
        tie_column="tie_count",
        expect_matches=True,
    )
    for column in (
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    ):
        if table[column].isna().any():
            raise GridProximityError(f"Voltage-level matched rows require {column}")
    return levels


def _null_safe_series_equal(actual: pd.Series, expected: pd.Series) -> bool:
    actual_values = actual.reset_index(drop=True)
    expected_values = expected.reset_index(drop=True)
    if len(actual_values) != len(expected_values):
        return False
    both_null = actual_values.isna() & expected_values.isna()
    try:
        equal_values = actual_values.eq(expected_values).fillna(False)
    except (TypeError, ValueError):
        return False
    return bool((both_null | equal_values).all())


def _validate_exact_representation_consistency(
    parcels: gpd.GeoDataFrame,
    voltage_table: pd.DataFrame,
    levels: tuple[float, ...],
) -> None:
    if not levels:
        return

    distance_column = "nearest_line_proxy_distance_m"
    grid_id_column = "nearest_line_grid_feature_id"
    selected_columns = (
        "parcel_id",
        distance_column,
        grid_id_column,
        "nearest_line_source_feature_id",
        "voltage_kv",
        "tie_count",
        "manager_name",
        "asset_status_raw",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    )
    candidates = voltage_table.loc[:, list(selected_columns)].copy()
    _validate_id_values(
        candidates[grid_id_column],
        "Voltage-level nearest grid_feature_id",
        require_unique=False,
    )
    parcel_positions = {
        parcel_id: position
        for position, parcel_id in enumerate(parcels["parcel_id"].tolist())
    }
    candidates["_parcel_position"] = candidates["parcel_id"].map(parcel_positions)
    if candidates["_parcel_position"].isna().any():
        raise GridProximityError(
            "Voltage-level proximity contains an unexpected parcel ID"
        )
    candidates["_distance"] = candidates[distance_column].map(float)
    candidates["_tie_count"] = candidates["tie_count"].map(int).astype("object")

    ordered = candidates.sort_values(
        ["_parcel_position", "_distance", grid_id_column],
        kind="mergesort",
    )
    expected = ordered.drop_duplicates("_parcel_position", keep="first")
    expected = expected.set_index("_parcel_position").reindex(range(len(parcels)))
    if expected["parcel_id"].isna().any():
        raise GridProximityError("Voltage-level proximity does not cover every parcel")

    minimum_distance = candidates.groupby("_parcel_position", sort=False)[
        "_distance"
    ].transform("min")
    tied_level_winners = candidates.loc[candidates["_distance"].eq(minimum_distance)]
    expected_ties = tied_level_winners.groupby("_parcel_position", sort=False)[
        "_tie_count"
    ].agg(lambda values: sum(values.tolist()))
    expected_ties = expected_ties.reindex(range(len(parcels)))

    actual = parcels.reset_index(drop=True)
    actual_distance = actual["nearest_exact_line_proxy_distance_m"].map(float)
    if not actual_distance.eq(expected["_distance"].reset_index(drop=True)).all():
        raise GridProximityError(
            "Global exact-line distance is inconsistent with voltage-level proximity"
        )

    field_mapping = (
        ("nearest_exact_line_grid_feature_id", grid_id_column),
        ("nearest_exact_line_source_feature_id", "nearest_line_source_feature_id"),
        ("nearest_exact_line_voltage_kv", "voltage_kv"),
        ("nearest_exact_line_manager_name", "manager_name"),
        ("nearest_exact_line_asset_status_raw", "asset_status_raw"),
        ("nearest_exact_line_source_department_code", "source_department_code"),
        ("nearest_exact_line_source_edition", "source_edition"),
        ("nearest_exact_line_source_archive_sha256", "source_archive_sha256"),
    )
    for parcel_column, table_column in field_mapping:
        if not _null_safe_series_equal(actual[parcel_column], expected[table_column]):
            raise GridProximityError(
                f"Global exact-line {parcel_column} is inconsistent with "
                "voltage-level proximity"
            )

    actual_ties = actual["nearest_exact_line_tie_count"].map(int)
    if not actual_ties.eq(expected_ties.reset_index(drop=True)).all():
        raise GridProximityError(
            "Global exact-line tie count is inconsistent with voltage-level proximity"
        )


def _validate_result_contract(result: GridProximityResult) -> tuple[float, ...]:
    parcels = result.parcels
    _validate_parcels(parcels)
    required_proximity_columns = (
        set(_LINE_OUTPUT_MAPPING.values())
        | set(_EXACT_LINE_OUTPUT_MAPPING.values())
        | set(_POST_OUTPUT_MAPPING.values())
    )
    missing = required_proximity_columns - set(parcels.columns)
    if missing:
        raise GridProximityError(
            "Missing proximity result columns: " + ", ".join(sorted(missing))
        )
    levels = _validate_voltage_coverage(result.voltage_level_coverage)
    _validate_match_integrity(
        parcels,
        label="Nearest line proximity",
        distance_column="nearest_line_proxy_distance_m",
        grid_id_column="nearest_line_grid_feature_id",
        source_id_column="nearest_line_source_feature_id",
        tie_column="nearest_line_tie_count",
        expect_matches=True,
    )
    _validate_match_integrity(
        parcels,
        label="Nearest post proximity",
        distance_column="nearest_post_proxy_distance_m",
        grid_id_column="nearest_post_grid_feature_id",
        source_id_column="nearest_post_source_feature_id",
        tie_column="nearest_post_tie_count",
        expect_matches=True,
    )
    _validate_match_integrity(
        parcels,
        label="Nearest exact-line proximity",
        distance_column="nearest_exact_line_proxy_distance_m",
        grid_id_column="nearest_exact_line_grid_feature_id",
        source_id_column="nearest_exact_line_source_feature_id",
        tie_column="nearest_exact_line_tie_count",
        expect_matches=bool(levels),
        voltage_column="nearest_exact_line_voltage_kv",
        unmatched_null_columns=tuple(_EXACT_LINE_OUTPUT_MAPPING.values()),
    )
    if (
        levels
        and not parcels["nearest_exact_line_voltage_kv"].map(float).isin(levels).all()
    ):
        raise GridProximityError(
            "Nearest exact-line voltage does not match source coverage"
        )
    _validate_voltage_table(
        result.voltage_level_proximity,
        parcels["parcel_id"],
        result.voltage_level_coverage,
    )
    _validate_exact_representation_consistency(
        parcels,
        result.voltage_level_proximity,
        levels,
    )
    return levels


def _validate_output_integrity(
    source_parcels: gpd.GeoDataFrame,
    result: GridProximityResult,
) -> None:
    _validate_result_contract(result)
    output = result.parcels
    if len(output) != len(source_parcels):
        raise GridProximityError("Grid proximity enrichment changed parcel count")
    source_ids = source_parcels["parcel_id"].reset_index(drop=True)
    output_ids = output["parcel_id"].reset_index(drop=True)
    if not source_ids.equals(output_ids):
        raise GridProximityError(
            "Grid proximity enrichment changed parcel IDs or order"
        )
    source_crs = _validated_crs(source_parcels.crs, "Input parcel")
    output_crs = _validated_crs(output.crs, "Output parcel")
    if not source_crs.equals(output_crs):
        raise GridProximityError("Enriched parcel CRS changed")
    if not output.geometry.geom_equals_exact(
        source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False
    ).all():
        raise GridProximityError("Enriched parcel geometry changed")


def _voltage_level_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    exact_lines: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]:
    levels = tuple(sorted(float(value) for value in exact_lines["voltage_kv"].unique()))
    tables: list[pd.DataFrame] = []
    coverage: list[VoltageLevelCoverage] = []
    for voltage_kv in levels:
        level_lines = exact_lines.loc[exact_lines["voltage_kv"] == voltage_kv].copy()
        coverage.append(
            VoltageLevelCoverage(
                voltage_kv=voltage_kv,
                line_feature_count=len(level_lines),
            )
        )
        nearest = _nearest_feature_rows(
            parcel_geometries,
            level_lines,
            (
                "grid_feature_id",
                "source_feature_id",
                "manager_name",
                "asset_status_raw",
                "source_department_code",
                "source_edition",
                "source_archive_sha256",
            ),
        )
        table = pd.DataFrame(
            {
                "parcel_id": parcel_ids.reset_index(drop=True),
                "voltage_kv": voltage_kv,
                "nearest_line_proxy_distance_m": nearest["distance_m"],
                "nearest_line_grid_feature_id": nearest["grid_feature_id"],
                "nearest_line_source_feature_id": nearest["source_feature_id"],
                "tie_count": nearest["tie_count"],
                "manager_name": nearest["manager_name"],
                "asset_status_raw": nearest["asset_status_raw"],
                "source_department_code": nearest["source_department_code"],
                "source_edition": nearest["source_edition"],
                "source_archive_sha256": nearest["source_archive_sha256"],
            }
        )
        tables.append(table.loc[:, list(VOLTAGE_PROXIMITY_COLUMNS)])

    if not tables:
        empty = pd.DataFrame(columns=list(VOLTAGE_PROXIMITY_COLUMNS))
        empty["voltage_kv"] = empty["voltage_kv"].astype("float64")
        empty["nearest_line_proxy_distance_m"] = empty[
            "nearest_line_proxy_distance_m"
        ].astype("float64")
        empty["tie_count"] = empty["tie_count"].astype("Int64")
        return empty, ()
    return pd.concat(tables, ignore_index=True), tuple(coverage)


def _enrich_parcel_grid_proximity_from_normalized(
    parcels: gpd.GeoDataFrame,
    electric_lines: gpd.GeoDataFrame,
    transformation_posts: gpd.GeoDataFrame,
) -> GridProximityResult:
    """Attach nearest IGN proxy matches using planar XY distance in EPSG:2154.

    IGN Z values are removed from calculation-only copies and do not affect
    horizontal proximity. Source parcel and normalized IGN geometries are not
    mutated. Distances describe only the nearest feature inside loaded proxy
    coverage and do not establish connection feasibility.
    """

    _validate_parcels(parcels)
    _reject_parcel_output_collisions(parcels)
    valid_lines = _validate_grid(
        electric_lines,
        label="Electric-line grid",
        required_columns=LINE_REQUIRED_COLUMNS,
        feature_type="ELECTRIC_LINE",
        allowed_geometry_types=LINE_GEOMETRY_TYPES,
    )
    valid_posts = _validate_grid(
        transformation_posts,
        label="Transformation-post grid",
        required_columns=POST_REQUIRED_COLUMNS,
        feature_type="TRANSFORMATION_POST",
        allowed_geometry_types=POST_GEOMETRY_TYPES,
    )
    if valid_lines.empty:
        raise GridProximityError("No VALID electric-line proxy is available")
    if valid_posts.empty:
        raise GridProximityError("No VALID transformation-post proxy is available")

    output = parcels.reset_index(drop=True).copy()
    calculation_parcels = output.to_crs(CALCULATION_CRS)
    parcel_geometries = _calculation_geometries(calculation_parcels)

    nearest_line = _nearest_feature_rows(
        parcel_geometries,
        valid_lines,
        _LINE_MATCH_COLUMNS,
    )
    _attach_matches(output, nearest_line, _LINE_OUTPUT_MAPPING)

    exact_mask = (valid_lines["voltage_status"] == "EXACT") & valid_lines[
        "voltage_kv"
    ].map(_is_positive_finite_number)
    exact_lines = valid_lines.loc[exact_mask].reset_index(drop=True).copy()
    exact_lines["voltage_kv"] = exact_lines["voltage_kv"].map(float).astype("float64")
    nearest_exact = _nearest_feature_rows(
        parcel_geometries,
        exact_lines,
        _LINE_MATCH_COLUMNS,
        allow_empty=True,
    )
    _attach_matches(output, nearest_exact, _EXACT_LINE_OUTPUT_MAPPING)

    nearest_post = _nearest_feature_rows(
        parcel_geometries,
        valid_posts,
        _POST_MATCH_COLUMNS,
    )
    _attach_matches(output, nearest_post, _POST_OUTPUT_MAPPING)

    voltage_table, voltage_coverage = _voltage_level_table(
        output["parcel_id"], parcel_geometries, exact_lines
    )
    result = GridProximityResult(
        parcels=output,
        voltage_level_proximity=voltage_table,
        voltage_level_coverage=voltage_coverage,
    )
    _validate_output_integrity(parcels, result)
    return result


def enrich_parcel_grid_proximity(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridProximityResult:
    """Compute proximity from one physically revalidated IGN source bundle."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise GridProximityError(
                "parcels must be a GeoDataFrame with active geometry"
            )
        if type(electricity_source) is not IgnBdTopoElectricityData:
            raise GridProximityError(
                "electricity source must be an IgnBdTopoElectricityData"
            )
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise GridProximityError("source_config must be an IgnBdTopoSourceConfig")
        _validate_parcels(parcels)
        _reject_parcel_output_collisions(parcels)
        normalized = normalize_ign_electricity(electricity_source, source_config)
        if type(normalized) is not NormalizedIgnElectricityData:
            raise GridProximityError(
                "IGN electricity normalization returned an invalid result"
            )
        return _enrich_parcel_grid_proximity_from_normalized(
            parcels,
            normalized.electric_lines,
            normalized.transformation_posts,
        )
    except GridProximityError:
        raise
    except Exception as error:
        raise GridProximityError(
            "Parcel-to-grid proximity cannot be computed safely"
        ) from error


def _distance_profile(distances: pd.Series, ties: pd.Series) -> DistanceProfile:
    _validate_distance_values(distances, "Profile")
    values = distances.dropna().astype("float64")
    missing_count = int(distances.isna().sum())
    if values.empty:
        return DistanceProfile(
            count=0,
            missing_count=missing_count,
            minimum=None,
            p01=None,
            p05=None,
            p10=None,
            p25=None,
            p50=None,
            p75=None,
            p90=None,
            p95=None,
            p99=None,
            maximum=None,
            zero_distance_count=0,
            tie_count=0,
        )
    matched_ties = ties.loc[distances.notna()]
    if matched_ties.isna().any():
        raise GridProximityError("Matched distance rows require tie counts")
    return DistanceProfile(
        count=len(values),
        missing_count=missing_count,
        minimum=float(values.min()),
        p01=float(values.quantile(0.01)),
        p05=float(values.quantile(0.05)),
        p10=float(values.quantile(0.10)),
        p25=float(values.quantile(0.25)),
        p50=float(values.quantile(0.50)),
        p75=float(values.quantile(0.75)),
        p90=float(values.quantile(0.90)),
        p95=float(values.quantile(0.95)),
        p99=float(values.quantile(0.99)),
        maximum=float(values.max()),
        zero_distance_count=int(values.eq(0).sum()),
        tie_count=sum(value > 1 for value in matched_ties.tolist()),
    )


def profile_grid_proximity(result: GridProximityResult) -> GridProximityProfile:
    """Profile proximity distances without thresholds or suitability labels."""

    _validate_result_contract(result)
    parcels = result.parcels
    coverage = {
        float(item.voltage_kv): item.line_feature_count
        for item in result.voltage_level_coverage
    }
    voltage_profiles: list[VoltageLevelDistanceProfile] = []
    table = result.voltage_level_proximity
    observed_levels = tuple(coverage)
    for voltage_kv in observed_levels:
        rows = table.loc[table["voltage_kv"] == voltage_kv]
        distance = _distance_profile(
            rows["nearest_line_proxy_distance_m"], rows["tie_count"]
        )
        voltage_profiles.append(
            VoltageLevelDistanceProfile(
                voltage_kv=voltage_kv,
                line_feature_count=coverage[voltage_kv],
                parcel_proximity_count=len(rows),
                distance=distance,
            )
        )

    return GridProximityProfile(
        parcel_count=len(parcels),
        nearest_line=_distance_profile(
            parcels["nearest_line_proxy_distance_m"],
            parcels["nearest_line_tie_count"],
        ),
        nearest_exact_line=_distance_profile(
            parcels["nearest_exact_line_proxy_distance_m"],
            parcels["nearest_exact_line_tie_count"],
        ),
        nearest_post=_distance_profile(
            parcels["nearest_post_proxy_distance_m"],
            parcels["nearest_post_tie_count"],
        ),
        voltage_levels=tuple(voltage_profiles),
    )
```
