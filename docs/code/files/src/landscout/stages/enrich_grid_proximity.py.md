# `src/landscout/stages/enrich_grid_proximity.py`

## File identity

- Repository path: `src/landscout/stages/enrich_grid_proximity.py`
- File type: Python source
- Primary responsibility: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.
- Layer / domain: `stage` / `grid`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `b6b2f3c296b3fc933a542a33157b42f4260a7356a0da8e59710c2d482cf2d8c3`

## 1. Purpose

Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `grid` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pandas.api.types import is_scalar` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.
- `from shapely import STRtree, force_2d` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoElectricityData, IgnBdTopoSourceConfig, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_grid_ign import ( NormalizedIgnElectricityData, normalize_ign_electricity, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `CALCULATION_CRS` | `"EPSG:2154"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SPATIAL_ROLE` | `"PROXY_GEOMETRY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_REQUIRED_COLUMNS` | `frozenset({"parcel_id", "geometry"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LINE_REQUIRED_COLUMNS` | `frozenset( { "grid_feature_id", "grid_feature_type", "source_feature_id", "source_department_code", "source_edition", "source_archive_sha256", "source_layer", "spatial_role", "geometry_status", "voltage_raw", "voltage_status", "voltage_kv", "voltage_upper_bound_kv", "manager_name", "asset_status_raw", "geometry", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POST_REQUIRED_COLUMNS` | `frozenset( { "grid_feature_id", "grid_feature_type", "source_feature_id", "source_department_code", "source_edition", "source_archive_sha256", "source_layer", "spatial_role", "geometry_status", "name", "importance_raw", "asset_status_raw", "geometry", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `GRID_GEOMETRY_STATUSES` | `frozenset({"VALID", "NULL", "EMPTY", "INVALID"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LINE_GEOMETRY_TYPES` | `frozenset({"LineString", "MultiLineString"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POST_GEOMETRY_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_GEOMETRY_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `VOLTAGE_PROXIMITY_COLUMNS` | `( "parcel_id", "voltage_kv", "nearest_line_proxy_distance_m", "nearest_line_grid_feature_id", "nearest_line_source_feature_id", "tie_count", "manager_name", "asset_status_raw", "source_department_code", "source_edition", "source_archive_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_LINE_MATCH_COLUMNS` | `( "grid_feature_id", "source_feature_id", "voltage_raw", "voltage_status", "voltage_kv", "voltage_upper_bound_kv", "manager_name", "asset_status_raw", "source_department_code", "source_edition", "source_archive_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_POST_MATCH_COLUMNS` | `( "grid_feature_id", "source_feature_id", "name", "importance_raw", "asset_status_raw", "source_department_code", "source_edition", "source_archive_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_LINE_OUTPUT_MAPPING` | `{ "distance_m": "nearest_line_proxy_distance_m", "grid_feature_id": "nearest_line_grid_feature_id", "source_feature_id": "nearest_line_source_feature_id", "tie_count": "nearest_line_tie_count", "voltage_raw": "nearest_line_voltage_raw", "voltage_status": "nearest_line_voltage_status", "voltage_kv": "nearest_line_voltage_kv", "voltage_upper_bound_kv": "nearest_line_voltage_upper_bound_kv", "manager_name": "nearest_line_manager_name", "asset_status_raw": "nearest_line_asset_status_raw", "source_department_code": "nearest_line_source_department_code", "source_edition": "nearest_line_source_edition", "source_archive_sha256": "nearest_line_source_archive_sha256", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_EXACT_LINE_OUTPUT_MAPPING` | `{ "distance_m": "nearest_exact_line_proxy_distance_m", "grid_feature_id": "nearest_exact_line_grid_feature_id", "source_feature_id": "nearest_exact_line_source_feature_id", "tie_count": "nearest_exact_line_tie_count", "voltage_kv": "nearest_exact_line_voltage_kv", "manager_name": "nearest_exact_line_manager_name", "asset_status_raw": "nearest_exact_line_asset_status_raw", "source_department_code": "nearest_exact_line_source_department_code", "source_edition": "nearest_exact_line_source_edition", "source_archive_sha256": "nearest_exact_line_source_archive_sha256", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_POST_OUTPUT_MAPPING` | `{ "distance_m": "nearest_post_proxy_distance_m", "grid_feature_id": "nearest_post_grid_feature_id", "source_feature_id": "nearest_post_source_feature_id", "tie_count": "nearest_post_tie_count", "name": "nearest_post_name", "importance_raw": "nearest_post_importance_raw", "asset_status_raw": "nearest_post_asset_status_raw", "source_department_code": "nearest_post_source_department_code", "source_edition": "nearest_post_source_edition", "source_archive_sha256": "nearest_post_source_archive_sha256", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `GridProximityError`

**Purpose:** Raised when grid-proximity inputs or results are unsafe.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `VoltageLevelCoverage`

**Purpose:** Source-line coverage for one dynamically observed exact voltage.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `voltage_kv` | `float` | `required` | `float` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `line_feature_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |

**Validators and methods:**

- None.

### `GridProximityResult`

**Purpose:** Parcel enrichment and dynamic exact-voltage proximity output.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `voltage_level_proximity` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `voltage_level_coverage` | `tuple[VoltageLevelCoverage, ...]` | `required` | `tuple[VoltageLevelCoverage, ...]` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `DistanceProfile`

**Purpose:** Threshold-free distribution summary for one distance field.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `count` | `int` | `required` | `int` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `missing_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `minimum` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p01` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p05` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p10` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p25` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p50` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p75` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p90` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p95` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `p99` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `maximum` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `zero_distance_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `tie_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |

**Validators and methods:**

- None.

### `VoltageLevelDistanceProfile`

**Purpose:** Distance distribution and source coverage for one exact voltage.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `voltage_kv` | `float` | `required` | `float` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `line_feature_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `parcel_proximity_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `distance` | `DistanceProfile` | `required` | `DistanceProfile` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `GridProximityProfile`

**Purpose:** Threshold-free parcel and voltage-level proximity profiles.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `parcel_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `nearest_line` | `DistanceProfile` | `required` | `DistanceProfile` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `nearest_exact_line` | `DistanceProfile` | `required` | `DistanceProfile` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `nearest_post` | `DistanceProfile` | `required` | `DistanceProfile` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `voltage_levels` | `tuple[VoltageLevelDistanceProfile, ...]` | `required` | `tuple[VoltageLevelDistanceProfile, ...]` state used by `src/landscout/stages/enrich_grid_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_validated_crs`

**Signature**

```python
def _validated_crs(value: object, label: str) -> CRS:
```

**Purpose**

Validates and returns canonical crs according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `CRS.from_user_input(value)`.

**Algorithm**

1. Checks `value is None`. When true: Raises `GridProximityError(f'{label} CRS is required')`.
2. Runs guarded operation: Returns `CRS.from_user_input(value)`. Handles `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `value is None` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_user_input`, `GridProximityError`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_require_lambert93`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_output_integrity`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_require_lambert93`

**Signature**

```python
def _require_lambert93(value: object, label: str) -> None:
```

**Purpose**

Implements require lambert93 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `actual` from `_validated_crs(value, label)`.
2. Computes `expected` from `CRS.from_epsg(2154)`.
3. Checks `not actual.is_projected or not actual.equals(expected)`. When true: Raises `GridProximityError(f'{label} must use EPSG:2154')`.

**Validation and invariants**

- Rejects or diverts the path when `not actual.is_projected or not actual.equals(expected)` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `GridProximityError`, `_validated_crs`, `actual.equals`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_grid`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_active_geometry`

**Signature**

```python
def _validate_active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

**Purpose**

Validates and rejects malformed active geometry according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `'geometry' not in frame.columns`. When true: Raises `GridProximityError(f'{label} geometry column is required')`.
2. Checks `frame.active_geometry_name != 'geometry'`. When true: Raises `GridProximityError(f'{label} geometry column must be active')`.

**Validation and invariants**

- Rejects or diverts the path when `'geometry' not in frame.columns` is true.
- Rejects or diverts the path when `frame.active_geometry_name != 'geometry'` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridProximityError`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_grid`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_id_values`

**Signature**

```python
def _validate_id_values(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
```

**Purpose**

Validates and rejects malformed id values according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `require_unique` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `values.isna().any()`. When true: Raises `GridProximityError(f'{label} values must not be null')`.
2. Computes `raw_values` from `values.tolist()`.
3. Checks `any((not isinstance(value, str) for value in raw_values))`. When true: Raises `GridProximityError(f'{label} values must be strings')`.
4. Checks `any((not value.strip() for value in raw_values))`. When true: Raises `GridProximityError(f'{label} values must not be empty')`.
5. Checks `any((value != value.strip() for value in raw_values))`. When true: Raises `GridProximityError(f'{label} values must not contain leading or trailing whitespace')`.
6. Checks `require_unique and values.duplicated().any()`. When true: Raises `GridProximityError(f'{label} values must be unique')`.

**Validation and invariants**

- Rejects or diverts the path when `values.isna().any()` is true.
- Rejects or diverts the path when `any((not isinstance(value, str) for value in raw_values))` is true.
- Rejects or diverts the path when `any((not value.strip() for value in raw_values))` is true.
- Rejects or diverts the path when `any((value != value.strip() for value in raw_values))` is true.
- Rejects or diverts the path when `require_unique and values.duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridProximityError`, `any`, `isinstance`, `value.strip`, `values.duplicated`, `values.duplicated().any`, `values.isna`, `values.isna().any`, `values.tolist`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_exact_representation_consistency`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_parcels`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_voltage_table`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_parcels`

**Signature**

```python
def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
```

**Purpose**

Validates and rejects malformed parcels according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `source_crs`.

**Algorithm**

1. Computes `missing` from `PARCEL_REQUIRED_COLUMNS - set(parcels.columns)`.
2. Checks `missing`. When true: Raises `GridProximityError('Missing required parcel columns: ' + ', '.join(sorted(missing)))`.
3. Calls `_validate_active_geometry(parcels, 'Parcel')` for its validation or side effect.
4. Computes `source_crs` from `_validated_crs(parcels.crs, 'Parcel')`.
5. Calls `_validate_id_values(parcels['parcel_id'], 'parcel_id', require_unique=True)` for its validation or side effect.
6. Checks `parcels.geometry.isna().any()`. When true: Raises `GridProximityError('Parcel geometries must not be null')`.
7. Checks `parcels.geometry.is_empty.any()`. When true: Raises `GridProximityError('Parcel geometries must not be empty')`.
8. Checks `not parcels.geometry.is_valid.all()`. When true: Raises `GridProximityError('Parcel geometries must be valid')`.
9. Computes `geometry_types` from `set(parcels.geometry.geom_type.dropna())`.
10. Computes `unsupported` from `sorted((str(value) for value in geometry_types - PARCEL_GEOMETRY_TYPES))`.
11. Checks `unsupported`. When true: Raises `GridProximityError('Parcel geometries must be Polygon or MultiPolygon; found: ' + ', '.join(unsupported))`.
12. Returns `source_crs`.

**Validation and invariants**

- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `parcels.geometry.isna().any()` is true.
- Rejects or diverts the path when `parcels.geometry.is_empty.any()` is true.
- Rejects or diverts the path when `not parcels.geometry.is_valid.all()` is true.
- Rejects or diverts the path when `unsupported` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `GridProximityError`, `_validate_active_geometry`, `_validate_id_values`, `_validated_crs`, `parcels.geometry.geom_type.dropna`, `parcels.geometry.is_empty.any`, `parcels.geometry.is_valid.all`, `parcels.geometry.isna`, `parcels.geometry.isna().any`, `set`, `sorted`, `str`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_enrich_parcel_grid_proximity_from_normalized`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_result_contract`
- `src/landscout/stages/enrich_grid_proximity.py` — `enrich_parcel_grid_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_observed_geometry_status`

**Signature**

```python
def _observed_geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
```

**Purpose**

Implements observed geometry status according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`gpd.GeoSeries`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `status`.

**Algorithm**

1. Computes `status` from `pd.Series('VALID', index=geometry.index, dtype='object')`.
2. Computes `null_mask` from `geometry.isna()`.
3. Computes `empty_mask` from `~null_mask & geometry.is_empty`.
4. Computes `invalid_mask` from `~null_mask & ~geometry.is_empty & ~geometry.is_valid`.
5. Computes `status.loc[null_mask]` from `'NULL'`.
6. Computes `status.loc[empty_mask]` from `'EMPTY'`.
7. Computes `status.loc[invalid_mask]` from `'INVALID'`.
8. Returns `status`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `geometry.isna`, `pd.Series`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_grid`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_grid`

**Signature**

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

**Purpose**

Validates and rejects malformed grid according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `required_columns` (`frozenset[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `feature_type` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `allowed_geometry_types` (`frozenset[str]`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame.loc[valid_mask].reset_index(drop=True).copy()`.

**Algorithm**

1. Computes `missing` from `required_columns - set(frame.columns)`.
2. Checks `missing`. When true: Raises `GridProximityError(f'Missing required {label} columns: ' + ', '.join(sorted(missing)))`.
3. Calls `_validate_active_geometry(frame, label)` for its validation or side effect.
4. Calls `_require_lambert93(frame.crs, label)` for its validation or side effect.
5. Computes `identifiers` from `frame['grid_feature_id']`.
6. Checks `identifiers.isna().any()`. When true: Raises `GridProximityError(f'{label} grid_feature_id values must not be null')`.
7. Checks `any((not isinstance(value, str) or not value for value in identifiers.tolist()))`. When true: Raises `GridProximityError(f'{label} grid_feature_id values must be non-empty strings')`.
8. Checks `identifiers.duplicated().any()`. When true: Raises `GridProximityError(f'{label} grid_feature_id values must be unique')`.
9. Checks `frame['grid_feature_type'].isna().any() or not frame['grid_feature_type'].eq(feature_type).all()`. When true: Raises `GridProximityError(f'{label} grid_feature_type must be {feature_type}')`.
10. Checks `frame['spatial_role'].isna().any() or not frame['spatial_role'].eq(SPATIAL_ROLE).all()`. When true: Raises `GridProximityError(f'{label} spatial_role must be PROXY_GEOMETRY')`.
11. Computes `declared_status` from `frame['geometry_status']`.
12. Computes `observed_status` from `_observed_geometry_status(frame.geometry)`.
13. Computes `declared_values` from `set(declared_status.dropna().unique())`.
14. Checks `declared_status.isna().any() or not declared_values <= GRID_GEOMETRY_STATUSES`. When true: Raises `GridProximityError(f'{label} has unexpected geometry_status values')`.
15. Checks `not declared_status.astype('object').equals(observed_status)`. When true: Raises `GridProximityError(f'{label} geometry_status does not match the source geometry')`.
16. Computes `valid_mask` from `declared_status == 'VALID'`.
17. Computes `valid_types` from `set(frame.loc[valid_mask, 'geometry'].geom_type.dropna())`.
18. Computes `unsupported` from `sorted((str(value) for value in valid_types - allowed_geometry_types))`.
19. Checks `unsupported`. When true: Raises `GridProximityError(f'{label} has unsupported VALID geometry types: ' + ', '.join(unsupported))`.
20. Returns `frame.loc[valid_mask].reset_index(drop=True).copy()`.

**Validation and invariants**

- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `identifiers.isna().any()` is true.
- Rejects or diverts the path when `any((not isinstance(value, str) or not value for value in identifiers.tolist()))` is true.
- Rejects or diverts the path when `identifiers.duplicated().any()` is true.
- Rejects or diverts the path when `frame['grid_feature_type'].isna().any() or not frame['grid_feature_type'].eq(feature_type).all()` is true.
- Rejects or diverts the path when `frame['spatial_role'].isna().any() or not frame['spatial_role'].eq(SPATIAL_ROLE).all()` is true.
- Rejects or diverts the path when `declared_status.isna().any() or not declared_values <= GRID_GEOMETRY_STATUSES` is true.
- Rejects or diverts the path when `not declared_status.astype('object').equals(observed_status)` is true.
- Rejects or diverts the path when `unsupported` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.loc[valid_mask].reset_index(drop=True).copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `', '.join`, `GridProximityError`, `_observed_geometry_status`, `_require_lambert93`, `_validate_active_geometry`, `any`, `declared_status.astype`, `declared_status.astype('object').equals`, `declared_status.dropna`, `declared_status.dropna().unique`, `declared_status.isna`, `declared_status.isna().any`, `frame.loc[valid_mask, 'geometry'].geom_type.dropna`, `frame.loc[valid_mask].reset_index`, `frame.loc[valid_mask].reset_index(drop=True).copy`, `frame['grid_feature_type'].eq`, `frame['grid_feature_type'].eq(feature_type).all`, `frame['grid_feature_type'].isna`, `frame['grid_feature_type'].isna().any`, `frame['spatial_role'].eq`, `frame['spatial_role'].eq(SPATIAL_ROLE).all`, `frame['spatial_role'].isna`, `frame['spatial_role'].isna().any`, `identifiers.duplicated`, `identifiers.duplicated().any`, `identifiers.isna`, `identifiers.isna().any`, `identifiers.tolist`, `isinstance`, `set`, `sorted`, `str`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_enrich_parcel_grid_proximity_from_normalized`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_finite_real_as_float`

**Signature**

```python
def _finite_real_as_float(value: object) -> float | None:
```

**Purpose**

Implements finite real as float according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float | None`. Observed return expression(s): `numeric if isfinite(numeric) else None`; `None`.

**Algorithm**

1. Checks `not isinstance(value, Real) or isinstance(value, bool)`. When true: Returns `None`.
2. Runs guarded operation: Computes `numeric` from `float(value)`. Handles `(OverflowError, TypeError, ValueError)`.
3. Returns `numeric if isfinite(numeric) else None`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `float`, `isfinite`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_is_positive_finite_number`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_distance_values`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_tie_counts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_is_positive_finite_number`

**Signature**

```python
def _is_positive_finite_number(value: object) -> bool:
```

**Purpose**

Returns whether `positive finite number` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `numeric is not None and numeric > 0`.

**Algorithm**

1. Computes `numeric` from `_finite_real_as_float(value)`.
2. Returns `numeric is not None and numeric > 0`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_finite_real_as_float`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_voltage_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_calculation_geometries`

**Signature**

```python
def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
```

**Purpose**

Implements calculation geometries according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `np.ndarray`. Observed return expression(s): `np.asarray(force_2d(values), dtype=object)`.

**Algorithm**

1. Computes `values` from `np.asarray(frame.geometry.array, dtype=object)`.
2. Returns `np.asarray(force_2d(values), dtype=object)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `force_2d`, `np.asarray`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_enrich_parcel_grid_proximity_from_normalized`
- `src/landscout/stages/enrich_grid_proximity.py` — `_nearest_feature_rows`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_empty_nearest_result`

**Signature**

```python
def _empty_nearest_result(
    parcel_count: int,
    attribute_columns: tuple[str, ...],
) -> pd.DataFrame:
```

**Purpose**

Implements empty nearest result according to the exact implementation and guards in this file.

**Inputs**

- `parcel_count` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `attribute_columns` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `pd.DataFrame(index=pd.RangeIndex(parcel_count))`.
2. Computes `output['distance_m']` from `pd.Series(np.nan, index=output.index, dtype='float64')`.
3. Computes `output['tie_count']` from `pd.Series(pd.NA, index=output.index, dtype='Int64')`.
4. Iterates `column` over `attribute_columns`. For each value: Checks `column in {'voltage_kv', 'voltage_upper_bound_kv'}`. When true: Computes `output[column]` from `pd.Series(np.nan, index=output.index, dtype='float64')`. Otherwise: Computes `output[column]` from `pd.Series(pd.NA, index=output.index, dtype='object')`.
5. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.DataFrame`, `pd.RangeIndex`, `pd.Series`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_nearest_feature_rows`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_nearest_feature_rows`

**Signature**

```python
def _nearest_feature_rows(
    parcel_geometries: np.ndarray,
    features: gpd.GeoDataFrame,
    attribute_columns: tuple[str, ...],
    *,
    allow_empty: bool = False,
) -> pd.DataFrame:
```

**Purpose**

Implements nearest feature rows according to the exact implementation and guards in this file.

**Inputs**

- `parcel_geometries` (`np.ndarray`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `attribute_columns` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `allow_empty` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`; `_empty_nearest_result(parcel_count, attribute_columns)`.

**Algorithm**

1. Computes `parcel_count` from `len(parcel_geometries)`.
2. Checks `features.empty`. When true: Checks `allow_empty`. When true: Returns `_empty_nearest_result(parcel_count, attribute_columns)`. Raises `GridProximityError('No VALID grid proxy feature is available')`.
3. Computes `feature_geometries` from `_calculation_geometries(features)`.
4. Computes `tree` from `STRtree(feature_geometries)`.
5. Computes `(indices, distances)` from `tree.query_nearest(parcel_geometries, all_matches=True, return_distance=True)`.
6. Computes `matches` from `pd.DataFrame({'parcel_position': indices[0], 'feature_position': indices[1], 'distance_m': distances})`.
7. Computes `matches['grid_feature_id']` from `features.iloc[matches['feature_position'].to_numpy()]['grid_feature_id'].to_numpy()`.
8. Computes `matches` from `matches.sort_values(['parcel_position', 'distance_m', 'grid_feature_id'], kind='mergesort')`.
9. Computes `ties` from `matches.groupby('parcel_position', sort=False).size()`.
10. Computes `selected` from `matches.drop_duplicates('parcel_position', keep='first').sort_values('parcel_position')`.
11. Checks `selected['parcel_position'].tolist() != list(range(parcel_count))`. When true: Raises `GridProximityError('Nearest-neighbour matching did not cover every parcel')`.
12. Computes `feature_positions` from `selected['feature_position'].to_numpy()`.
13. Computes `output` from `features.iloc[feature_positions].loc[:, list(attribute_columns)].copy()`.
14. Computes `output` from `output.reset_index(drop=True)`.
15. Calls `output.insert(0, 'tie_count', ties.reindex(range(parcel_count)).to_numpy())` for its validation or side effect.
16. Calls `output.insert(0, 'distance_m', selected['distance_m'].to_numpy(dtype='float64'))` for its validation or side effect.
17. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `features.empty` is true.
- Rejects or diverts the path when `selected['parcel_position'].tolist() != list(range(parcel_count))` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `features.iloc[feature_positions].loc[:, list(attribute_columns)].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GridProximityError`, `STRtree`, `_calculation_geometries`, `_empty_nearest_result`, `features.iloc[feature_positions].loc[:, list(attribute_columns)].copy`, `features.iloc[matches['feature_position'].to_numpy()]['grid_feature_id'].to_numpy`, `len`, `list`, `matches.drop_duplicates`, `matches.drop_duplicates('parcel_position', keep='first').sort_values`, `matches.groupby`, `matches.groupby('parcel_position', sort=False).size`, `matches.sort_values`, `matches['feature_position'].to_numpy`, `output.insert`, `output.reset_index`, `pd.DataFrame`, `range`, `selected['distance_m'].to_numpy`, `selected['feature_position'].to_numpy`, `selected['parcel_position'].tolist`, `ties.reindex`, `ties.reindex(range(parcel_count)).to_numpy`, `tree.query_nearest`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_enrich_parcel_grid_proximity_from_normalized`
- `src/landscout/stages/enrich_grid_proximity.py` — `_voltage_level_table`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_attach_matches`

**Signature**

```python
def _attach_matches(
    parcels: gpd.GeoDataFrame,
    matches: pd.DataFrame,
    mapping: dict[str, str],
) -> None:
```

**Purpose**

Implements attach matches according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `matches` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `mapping` (`dict[str, str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `(source_column, output_column)` over `mapping.items()`. For each value: Computes `parcels[output_column]` from `matches[source_column].reset_index(drop=True)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `mapping.items`, `matches[source_column].reset_index`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_enrich_parcel_grid_proximity_from_normalized`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_distance_values`

**Signature**

```python
def _validate_distance_values(values: pd.Series, label: str) -> None:
```

**Purpose**

Validates and rejects malformed distance values according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `non_null` from `values.dropna()`.
2. Computes `numeric_values` from `[_finite_real_as_float(value) for value in non_null.tolist()]`.
3. Checks `any((value is None for value in numeric_values))`. When true: Raises `GridProximityError(f'{label} distances must be numeric and finite')`.
4. Computes `numeric` from `np.asarray(numeric_values, dtype='float64')`.
5. Checks `(numeric < 0).any()`. When true: Raises `GridProximityError(f'{label} distances must be finite and >= 0')`.

**Validation and invariants**

- Rejects or diverts the path when `any((value is None for value in numeric_values))` is true.
- Rejects or diverts the path when `(numeric < 0).any()` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(numeric < 0).any`, `GridProximityError`, `_finite_real_as_float`, `any`, `non_null.tolist`, `np.asarray`, `values.dropna`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_distance_profile`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_match_integrity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_is_missing_scalar`

**Signature**

```python
def _is_missing_scalar(value: object) -> bool:
```

**Purpose**

Returns whether `missing scalar` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `bool(pd.isna(value))`; `True`; `False`.

**Algorithm**

1. Checks `value is None`. When true: Returns `True`.
2. Checks `not is_scalar(value)`. When true: Returns `False`.
3. Returns `bool(pd.isna(value))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `is_scalar`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_tie_counts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_tie_counts`

**Signature**

```python
def _validate_tie_counts(
    values: pd.Series,
    matched: pd.Series,
    label: str,
) -> None:
```

**Purpose**

Validates and rejects malformed tie counts according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `matched` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `len(values) != len(matched)`. When true: Raises `GridProximityError(f'{label} tie-count state is inconsistent')`.
2. Iterates `(value, row_is_matched)` over `zip(values.tolist(), matched.to_numpy(dtype='bool'), strict=True)`. For each value: Computes `missing` from `_is_missing_scalar(value)`. Checks `not row_is_matched`. When true: Checks `not missing`. When true: Raises `GridProximityError(f'{label} unmatched rows must have null tie_count')`. Executes `continue` control flow. Checks `missing`. When true: Raises `GridProximityError(f'{label} matched rows require tie_count')`. Executes 2 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `len(values) != len(matched)` is true.
- Rejects or diverts the path when `not row_is_matched` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `numeric is None or not numeric.is_integer() or numeric < 1` is true.
- Rejects or diverts the path when `not missing` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridProximityError`, `_finite_real_as_float`, `_is_missing_scalar`, `len`, `matched.to_numpy`, `numeric.is_integer`, `values.tolist`, `zip`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_match_integrity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_match_integrity`

**Signature**

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

**Purpose**

Validates and rejects malformed match integrity according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `distance_column` (`str`; required) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `grid_id_column` (`str`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_id_column` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `tie_column` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expect_matches` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `voltage_column` (`str | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `unmatched_null_columns` (`tuple[str, ...]`; optional/default `()`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `None`.

**Algorithm**

1. Computes `required` from `{distance_column, grid_id_column, source_id_column, tie_column}`.
2. Checks `voltage_column is not None`. When true: Calls `required.add(voltage_column)` for its validation or side effect.
3. Computes `missing` from `required - set(frame.columns)`.
4. Checks `missing`. When true: Raises `GridProximityError(f'Missing {label} match columns: ' + ', '.join(sorted(missing)))`.
5. Computes `distance` from `frame[distance_column]`.
6. Computes `matched` from `distance.notna()`.
7. Checks `expect_matches and (not matched.all())`. When true: Raises `GridProximityError(f'{label} requires a match for every parcel')`.
8. Checks `not expect_matches and matched.any()`. When true: Raises `GridProximityError(f'{label} must be entirely unmatched')`.
9. Calls `_validate_distance_values(distance, label)` for its validation or side effect.
10. Calls `_validate_tie_counts(frame[tie_column], matched, label)` for its validation or side effect.
11. Computes `id_columns` from `(grid_id_column, source_id_column)`.
12. Checks `expect_matches`. When true: Iterates `column` over `id_columns`. For each value: Checks `frame[column].isna().any()`. When true: Raises `GridProximityError(f'{label} matched rows require {column}')`. Checks `voltage_column is not None and (not frame[voltage_column].map(_is_positive_finite_number).all())`. When true: Raises `GridProximityError(f'{label} voltage must be numeric, finite, and > 0')`. Returns `None`.
13. Computes `null_columns` from `set(unmatched_null_columns) | set(id_columns)`.
14. Checks `voltage_column is not None`. When true: Calls `null_columns.add(voltage_column)` for its validation or side effect.
15. Iterates `column` over `null_columns`. For each value: Checks `column not in frame.columns`. When true: Raises `GridProximityError(f'Missing {label} match column: {column}')`. Checks `frame[column].notna().any()`. When true: Raises `GridProximityError(f'{label} unmatched rows must have null {column}')`.

**Validation and invariants**

- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `expect_matches and (not matched.all())` is true.
- Rejects or diverts the path when `not expect_matches and matched.any()` is true.
- Rejects or diverts the path when `expect_matches` is true.
- Rejects or diverts the path when `voltage_column is not None and (not frame[voltage_column].map(_is_positive_finite_number).all())` is true.
- Rejects or diverts the path when `column not in frame.columns` is true.
- Rejects or diverts the path when `frame[column].notna().any()` is true.
- Rejects or diverts the path when `frame[column].isna().any()` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `GridProximityError`, `_validate_distance_values`, `_validate_tie_counts`, `distance.notna`, `frame[column].isna`, `frame[column].isna().any`, `frame[column].notna`, `frame[column].notna().any`, `frame[voltage_column].map`, `frame[voltage_column].map(_is_positive_finite_number).all`, `matched.all`, `matched.any`, `null_columns.add`, `required.add`, `set`, `sorted`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_result_contract`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_voltage_table`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_voltage_coverage`

**Signature**

```python
def _validate_voltage_coverage(
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
```

**Purpose**

Validates and rejects malformed voltage coverage according to the exact implementation and guards in this file.

**Inputs**

- `coverage` (`tuple[VoltageLevelCoverage, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[float, ...]`. Observed return expression(s): `tuple(levels)`.

**Algorithm**

1. Defines `levels` with annotation `list[float]` from `[]`.
2. Iterates `item` over `coverage`. For each value: Checks `not isinstance(item, VoltageLevelCoverage)`. When true: Raises `GridProximityError('Voltage coverage entries are invalid')`. Checks `not _is_positive_finite_number(item.voltage_kv)`. When true: Raises `GridProximityError('Voltage coverage levels must be numeric, finite, and > 0')`. Checks `not isinstance(item.line_feature_count, Integral) or isinstance(item.line_feature_count, bool) or item.line_feature_count <= 0`. When true: Raises `GridProximityError('Voltage coverage line_feature_count must be an integer > 0')`. Executes 1 additional source-ordered statement(s).
3. Checks `len(set(levels)) != len(levels)`. When true: Raises `GridProximityError('Voltage coverage levels must be unique')`.
4. Checks `levels != sorted(levels)`. When true: Raises `GridProximityError('Voltage coverage levels must be ascending')`.
5. Returns `tuple(levels)`.

**Validation and invariants**

- Rejects or diverts the path when `len(set(levels)) != len(levels)` is true.
- Rejects or diverts the path when `levels != sorted(levels)` is true.
- Rejects or diverts the path when `not isinstance(item, VoltageLevelCoverage)` is true.
- Rejects or diverts the path when `not _is_positive_finite_number(item.voltage_kv)` is true.
- Rejects or diverts the path when `not isinstance(item.line_feature_count, Integral) or isinstance(item.line_feature_count, bool) or item.line_feature_count <= 0` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridProximityError`, `_is_positive_finite_number`, `float`, `isinstance`, `len`, `levels.append`, `set`, `sorted`, `tuple`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_result_contract`
- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_voltage_table`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_voltage_table`

**Signature**

```python
def _validate_voltage_table(
    table: pd.DataFrame,
    parcel_ids: pd.Series,
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
```

**Purpose**

Validates and rejects malformed voltage table according to the exact implementation and guards in this file.

**Inputs**

- `table` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcel_ids` (`pd.Series`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coverage` (`tuple[VoltageLevelCoverage, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[float, ...]`. Observed return expression(s): `levels`.

**Algorithm**

1. Computes `missing` from `set(VOLTAGE_PROXIMITY_COLUMNS) - set(table.columns)`.
2. Checks `missing`. When true: Raises `GridProximityError('Missing voltage proximity columns: ' + ', '.join(sorted(missing)))`.
3. Computes `levels` from `_validate_voltage_coverage(coverage)`.
4. Computes `expected_rows` from `len(parcel_ids) * len(levels)`.
5. Checks `len(table) != expected_rows`. When true: Raises `GridProximityError('Voltage proximity row count is inconsistent')`.
6. Checks `table.empty`. When true: Returns `levels`.
7. Calls `_validate_id_values(table['parcel_id'], 'parcel_id', require_unique=False)` for its validation or side effect.
8. Computes `raw_voltage_values` from `table['voltage_kv']`.
9. Checks `not raw_voltage_values.map(_is_positive_finite_number).all()`. When true: Raises `GridProximityError('Voltage proximity levels must be numeric, finite, and > 0')`.
10. Checks `table.duplicated(['parcel_id', 'voltage_kv']).any()`. When true: Raises `GridProximityError('Voltage proximity parcel/voltage pairs must be unique')`.
11. Computes `table_levels` from `tuple(sorted({float(value) for value in raw_voltage_values.tolist()}))`.
12. Checks `table_levels != levels`. When true: Raises `GridProximityError('Voltage proximity levels do not match source coverage')`.
13. Computes `expected_ids` from `parcel_ids.tolist()`.
14. Iterates `voltage_kv` over `levels`. For each value: Computes `rows` from `table.loc[raw_voltage_values.map(float) == voltage_kv]`. Checks `len(rows) != len(expected_ids) or rows['parcel_id'].tolist() != expected_ids`. When true: Raises `GridProximityError(f'Voltage proximity does not contain the exact parcel set for {voltage_kv:g} kV')`.
15. Calls `_validate_match_integrity(table, label='Voltage-level line proximity', distance_column='nearest_line_proxy_distance_m', grid_id_column='nearest_line_grid_feature_id', source_id_column='nearest_line_source_feature_id', tie_column='tie_count', expect_matches=True)` for its validation or side effect.
16. Iterates `column` over `('source_department_code', 'source_edition', 'source_archive_sha256')`. For each value: Checks `table[column].isna().any()`. When true: Raises `GridProximityError(f'Voltage-level matched rows require {column}')`.
17. Returns `levels`.

**Validation and invariants**

- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `len(table) != expected_rows` is true.
- Rejects or diverts the path when `not raw_voltage_values.map(_is_positive_finite_number).all()` is true.
- Rejects or diverts the path when `table.duplicated(['parcel_id', 'voltage_kv']).any()` is true.
- Rejects or diverts the path when `table_levels != levels` is true.
- Rejects or diverts the path when `len(rows) != len(expected_ids) or rows['parcel_id'].tolist() != expected_ids` is true.
- Rejects or diverts the path when `table[column].isna().any()` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `GridProximityError`, `_validate_id_values`, `_validate_match_integrity`, `_validate_voltage_coverage`, `float`, `len`, `parcel_ids.tolist`, `raw_voltage_values.map`, `raw_voltage_values.map(_is_positive_finite_number).all`, `raw_voltage_values.tolist`, `rows['parcel_id'].tolist`, `set`, `sorted`, `table.duplicated`, `table.duplicated(['parcel_id', 'voltage_kv']).any`, `table[column].isna`, `table[column].isna().any`, `tuple`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_result_contract`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_null_safe_series_equal`

**Signature**

```python
def _null_safe_series_equal(actual: pd.Series, expected: pd.Series) -> bool:
```

**Purpose**

Implements null safe series equal according to the exact implementation and guards in this file.

**Inputs**

- `actual` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `bool((both_null | equal_values).all())`; `False`.

**Algorithm**

1. Computes `actual_values` from `actual.reset_index(drop=True)`.
2. Computes `expected_values` from `expected.reset_index(drop=True)`.
3. Checks `len(actual_values) != len(expected_values)`. When true: Returns `False`.
4. Computes `both_null` from `actual_values.isna() & expected_values.isna()`.
5. Runs guarded operation: Computes `equal_values` from `actual_values.eq(expected_values).fillna(False)`. Handles `(TypeError, ValueError)`.
6. Returns `bool((both_null | equal_values).all())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(both_null | equal_values).all`, `actual.reset_index`, `actual_values.eq`, `actual_values.eq(expected_values).fillna`, `actual_values.isna`, `bool`, `expected.reset_index`, `expected_values.isna`, `len`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_exact_representation_consistency`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_exact_representation_consistency`

**Signature**

```python
def _validate_exact_representation_consistency(
    parcels: gpd.GeoDataFrame,
    voltage_table: pd.DataFrame,
    levels: tuple[float, ...],
) -> None:
```

**Purpose**

Validates and rejects malformed exact representation consistency according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `voltage_table` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `levels` (`tuple[float, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `None`.

**Algorithm**

1. Checks `not levels`. When true: Returns `None`.
2. Computes `distance_column` from `'nearest_line_proxy_distance_m'`.
3. Computes `grid_id_column` from `'nearest_line_grid_feature_id'`.
4. Computes `selected_columns` from `('parcel_id', distance_column, grid_id_column, 'nearest_line_source_feature_id', 'voltage_kv', 'tie_count', 'manager_name', 'asset_status_raw', 'source_department_code', 'source_edition', 'source_archive_sha256')`.
5. Computes `candidates` from `voltage_table.loc[:, list(selected_columns)].copy()`.
6. Calls `_validate_id_values(candidates[grid_id_column], 'Voltage-level nearest grid_feature_id', require_unique=False)` for its validation or side effect.
7. Computes `parcel_positions` from `{parcel_id: position for position, parcel_id in enumerate(parcels['parcel_id'].tolist())}`.
8. Computes `candidates['_parcel_position']` from `candidates['parcel_id'].map(parcel_positions)`.
9. Checks `candidates['_parcel_position'].isna().any()`. When true: Raises `GridProximityError('Voltage-level proximity contains an unexpected parcel ID')`.
10. Computes `candidates['_distance']` from `candidates[distance_column].map(float)`.
11. Computes `candidates['_tie_count']` from `candidates['tie_count'].map(int).astype('object')`.
12. Computes `ordered` from `candidates.sort_values(['_parcel_position', '_distance', grid_id_column], kind='mergesort')`.
13. Computes `expected` from `ordered.drop_duplicates('_parcel_position', keep='first')`.
14. Computes `expected` from `expected.set_index('_parcel_position').reindex(range(len(parcels)))`.
15. Checks `expected['parcel_id'].isna().any()`. When true: Raises `GridProximityError('Voltage-level proximity does not cover every parcel')`.
16. Computes `minimum_distance` from `candidates.groupby('_parcel_position', sort=False)['_distance'].transform('min')`.
17. Computes `tied_level_winners` from `candidates.loc[candidates['_distance'].eq(minimum_distance)]`.
18. Computes `expected_ties` from `tied_level_winners.groupby('_parcel_position', sort=False)['_tie_count'].agg(lambda values: sum(values.tolist()))`.
19. Computes `expected_ties` from `expected_ties.reindex(range(len(parcels)))`.
20. Computes `actual` from `parcels.reset_index(drop=True)`.
21. Computes `actual_distance` from `actual['nearest_exact_line_proxy_distance_m'].map(float)`.
22. Checks `not actual_distance.eq(expected['_distance'].reset_index(drop=True)).all()`. When true: Raises `GridProximityError('Global exact-line distance is inconsistent with voltage-level proximity')`.
23. Computes `field_mapping` from `(('nearest_exact_line_grid_feature_id', grid_id_column), ('nearest_exact_line_source_feature_id', 'nearest_line_source_feature_id'), ('nearest_exact_line_voltage_kv', 'voltage_kv'), ('nearest_exact_line_manager_name', 'manager_name'), ('nearest_exact_line_asset_status_raw', 'asset_status_raw'), ('nearest_exact_line_so…`.
24. Iterates `(parcel_column, table_column)` over `field_mapping`. For each value: Checks `not _null_safe_series_equal(actual[parcel_column], expected[table_column])`. When true: Raises `GridProximityError(f'Global exact-line {parcel_column} is inconsistent with voltage-level proximity')`.
25. Computes `actual_ties` from `actual['nearest_exact_line_tie_count'].map(int)`.
26. Checks `not actual_ties.eq(expected_ties.reset_index(drop=True)).all()`. When true: Raises `GridProximityError('Global exact-line tie count is inconsistent with voltage-level proximity')`.

**Validation and invariants**

- Rejects or diverts the path when `candidates['_parcel_position'].isna().any()` is true.
- Rejects or diverts the path when `expected['parcel_id'].isna().any()` is true.
- Rejects or diverts the path when `not actual_distance.eq(expected['_distance'].reset_index(drop=True)).all()` is true.
- Rejects or diverts the path when `not actual_ties.eq(expected_ties.reset_index(drop=True)).all()` is true.
- Rejects or diverts the path when `not _null_safe_series_equal(actual[parcel_column], expected[table_column])` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `voltage_table.loc[:, list(selected_columns)].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GridProximityError`, `_null_safe_series_equal`, `_validate_id_values`, `actual['nearest_exact_line_proxy_distance_m'].map`, `actual['nearest_exact_line_tie_count'].map`, `actual_distance.eq`, `actual_distance.eq(expected['_distance'].reset_index(drop=True)).all`, `actual_ties.eq`, `actual_ties.eq(expected_ties.reset_index(drop=True)).all`, `candidates.groupby`, `candidates.groupby('_parcel_position', sort=False)['_distance'].transform`, `candidates.sort_values`, `candidates['_distance'].eq`, `candidates['_parcel_position'].isna`, `candidates['_parcel_position'].isna().any`, `candidates['parcel_id'].map`, `candidates['tie_count'].map`, `candidates['tie_count'].map(int).astype`, `candidates[distance_column].map`, `enumerate`, `expected.set_index`, `expected.set_index('_parcel_position').reindex`, `expected['_distance'].reset_index`, `expected['parcel_id'].isna`, `expected['parcel_id'].isna().any`, `expected_ties.reindex`, `expected_ties.reset_index`, `len`, `list`, `ordered.drop_duplicates`, `parcels.reset_index`, `parcels['parcel_id'].tolist`, `range`, `sum`, `tied_level_winners.groupby`, `tied_level_winners.groupby('_parcel_position', sort=False)['_tie_count'].agg`, `values.tolist`, `voltage_table.loc[:, list(selected_columns)].copy`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_result_contract`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_result_contract`

**Signature**

```python
def _validate_result_contract(result: GridProximityResult) -> tuple[float, ...]:
```

**Purpose**

Validates and rejects malformed result contract according to the exact implementation and guards in this file.

**Inputs**

- `result` (`GridProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[float, ...]`. Observed return expression(s): `levels`.

**Algorithm**

1. Computes `parcels` from `result.parcels`.
2. Calls `_validate_parcels(parcels)` for its validation or side effect.
3. Computes `required_proximity_columns` from `set(_LINE_OUTPUT_MAPPING.values()) | set(_EXACT_LINE_OUTPUT_MAPPING.values()) | set(_POST_OUTPUT_MAPPING.values())`.
4. Computes `missing` from `required_proximity_columns - set(parcels.columns)`.
5. Checks `missing`. When true: Raises `GridProximityError('Missing proximity result columns: ' + ', '.join(sorted(missing)))`.
6. Computes `levels` from `_validate_voltage_coverage(result.voltage_level_coverage)`.
7. Calls `_validate_match_integrity(parcels, label='Nearest line proximity', distance_column='nearest_line_proxy_distance_m', grid_id_column='nearest_line_grid_feature_id', source_id_column='nearest_line_source_feature_id', tie_column='nearest_line_tie_count', expect_matches=True)` for its validation or side effect.
8. Calls `_validate_match_integrity(parcels, label='Nearest post proximity', distance_column='nearest_post_proxy_distance_m', grid_id_column='nearest_post_grid_feature_id', source_id_column='nearest_post_source_feature_id', tie_column='nearest_post_tie_count', expect_matches=True)` for its validation or side effect.
9. Calls `_validate_match_integrity(parcels, label='Nearest exact-line proximity', distance_column='nearest_exact_line_proxy_distance_m', grid_id_column='nearest_exact_line_grid_feature_id', source_id_column='nearest_exact_line_source_feature_id', tie_column='nearest_exact_line_tie_count', expect_matches=bool(levels), voltage_column='nearest_exact_line_voltage_kv', u…` for its validation or side effect.
10. Checks `levels and (not parcels['nearest_exact_line_voltage_kv'].map(float).isin(levels).all())`. When true: Raises `GridProximityError('Nearest exact-line voltage does not match source coverage')`.
11. Calls `_validate_voltage_table(result.voltage_level_proximity, parcels['parcel_id'], result.voltage_level_coverage)` for its validation or side effect.
12. Calls `_validate_exact_representation_consistency(parcels, result.voltage_level_proximity, levels)` for its validation or side effect.
13. Returns `levels`.

**Validation and invariants**

- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `levels and (not parcels['nearest_exact_line_voltage_kv'].map(float).isin(levels).all())` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `GridProximityError`, `_EXACT_LINE_OUTPUT_MAPPING.values`, `_LINE_OUTPUT_MAPPING.values`, `_POST_OUTPUT_MAPPING.values`, `_validate_exact_representation_consistency`, `_validate_match_integrity`, `_validate_parcels`, `_validate_voltage_coverage`, `_validate_voltage_table`, `bool`, `parcels['nearest_exact_line_voltage_kv'].map`, `parcels['nearest_exact_line_voltage_kv'].map(float).isin`, `parcels['nearest_exact_line_voltage_kv'].map(float).isin(levels).all`, `set`, `sorted`, `tuple`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_validate_output_integrity`
- `src/landscout/stages/enrich_grid_proximity.py` — `profile_grid_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_output_integrity`

**Signature**

```python
def _validate_output_integrity(
    source_parcels: gpd.GeoDataFrame,
    result: GridProximityResult,
) -> None:
```

**Purpose**

Validates and rejects malformed output integrity according to the exact implementation and guards in this file.

**Inputs**

- `source_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`GridProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `_validate_result_contract(result)` for its validation or side effect.
2. Computes `output` from `result.parcels`.
3. Checks `len(output) != len(source_parcels)`. When true: Raises `GridProximityError('Grid proximity enrichment changed parcel count')`.
4. Computes `source_ids` from `source_parcels['parcel_id'].reset_index(drop=True)`.
5. Computes `output_ids` from `output['parcel_id'].reset_index(drop=True)`.
6. Checks `not source_ids.equals(output_ids)`. When true: Raises `GridProximityError('Grid proximity enrichment changed parcel IDs or order')`.
7. Computes `source_crs` from `_validated_crs(source_parcels.crs, 'Input parcel')`.
8. Computes `output_crs` from `_validated_crs(output.crs, 'Output parcel')`.
9. Checks `not source_crs.equals(output_crs)`. When true: Raises `GridProximityError('Enriched parcel CRS changed')`.
10. Checks `not output.geometry.geom_equals_exact(source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False).all()`. When true: Raises `GridProximityError('Enriched parcel geometry changed')`.

**Validation and invariants**

- Rejects or diverts the path when `len(output) != len(source_parcels)` is true.
- Rejects or diverts the path when `not source_ids.equals(output_ids)` is true.
- Rejects or diverts the path when `not source_crs.equals(output_crs)` is true.
- Rejects or diverts the path when `not output.geometry.geom_equals_exact(source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False).all()` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridProximityError`, `_validate_result_contract`, `_validated_crs`, `len`, `output.geometry.geom_equals_exact`, `output.geometry.geom_equals_exact(source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False).all`, `output['parcel_id'].reset_index`, `source_crs.equals`, `source_ids.equals`, `source_parcels.geometry.reset_index`, `source_parcels['parcel_id'].reset_index`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_enrich_parcel_grid_proximity_from_normalized`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_voltage_level_table`

**Signature**

```python
def _voltage_level_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    exact_lines: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]:
```

**Purpose**

Implements voltage level table according to the exact implementation and guards in this file.

**Inputs**

- `parcel_ids` (`pd.Series`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcel_geometries` (`np.ndarray`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `exact_lines` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]`. Observed return expression(s): `(pd.concat(tables, ignore_index=True), tuple(coverage))`; `(empty, ())`.

**Algorithm**

1. Computes `levels` from `tuple(sorted((float(value) for value in exact_lines['voltage_kv'].unique())))`.
2. Defines `tables` with annotation `list[pd.DataFrame]` from `[]`.
3. Defines `coverage` with annotation `list[VoltageLevelCoverage]` from `[]`.
4. Iterates `voltage_kv` over `levels`. For each value: Computes `level_lines` from `exact_lines.loc[exact_lines['voltage_kv'] == voltage_kv].copy()`. Calls `coverage.append(VoltageLevelCoverage(voltage_kv=voltage_kv, line_feature_count=len(level_lines)))` for its validation or side effect. Computes `nearest` from `_nearest_feature_rows(parcel_geometries, level_lines, ('grid_feature_id', 'source_feature_id', 'manager_name', 'asset_status_raw', 'source_department_code', 'source_edition', 'source_archive_sha256'))`. Executes 2 additional source-ordered statement(s).
5. Checks `not tables`. When true: Computes `empty` from `pd.DataFrame(columns=list(VOLTAGE_PROXIMITY_COLUMNS))`. Computes `empty['voltage_kv']` from `empty['voltage_kv'].astype('float64')`. Computes `empty['nearest_line_proxy_distance_m']` from `empty['nearest_line_proxy_distance_m'].astype('float64')`. Executes 2 additional source-ordered statement(s).
6. Returns `(pd.concat(tables, ignore_index=True), tuple(coverage))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `exact_lines.loc[exact_lines['voltage_kv'] == voltage_kv].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `VoltageLevelCoverage`, `_nearest_feature_rows`, `coverage.append`, `empty['nearest_line_proxy_distance_m'].astype`, `empty['tie_count'].astype`, `empty['voltage_kv'].astype`, `exact_lines.loc[exact_lines['voltage_kv'] == voltage_kv].copy`, `exact_lines['voltage_kv'].unique`, `float`, `len`, `list`, `parcel_ids.reset_index`, `pd.DataFrame`, `pd.concat`, `sorted`, `tables.append`, `tuple`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `_enrich_parcel_grid_proximity_from_normalized`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_enrich_parcel_grid_proximity_from_normalized`

**Signature**

```python
def _enrich_parcel_grid_proximity_from_normalized(
    parcels: gpd.GeoDataFrame,
    electric_lines: gpd.GeoDataFrame,
    transformation_posts: gpd.GeoDataFrame,
) -> GridProximityResult:
```

**Purpose**

Attach nearest IGN proxy matches using planar XY distance in EPSG:2154. IGN Z values are removed from calculation-only copies and do not affect horizontal proximity. Source parcel and normalized IGN geometries are not mutated. Distances describe only the nearest feature inside loaded proxy coverage and do not establish connection feasibility.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `electric_lines` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `transformation_posts` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GridProximityResult`. Observed return expression(s): `result`.

**Algorithm**

1. Calls `_validate_parcels(parcels)` for its validation or side effect.
2. Computes `valid_lines` from `_validate_grid(electric_lines, label='Electric-line grid', required_columns=LINE_REQUIRED_COLUMNS, feature_type='ELECTRIC_LINE', allowed_geometry_types=LINE_GEOMETRY_TYPES)`.
3. Computes `valid_posts` from `_validate_grid(transformation_posts, label='Transformation-post grid', required_columns=POST_REQUIRED_COLUMNS, feature_type='TRANSFORMATION_POST', allowed_geometry_types=POST_GEOMETRY_TYPES)`.
4. Checks `valid_lines.empty`. When true: Raises `GridProximityError('No VALID electric-line proxy is available')`.
5. Checks `valid_posts.empty`. When true: Raises `GridProximityError('No VALID transformation-post proxy is available')`.
6. Computes `output` from `parcels.reset_index(drop=True).copy()`.
7. Computes `calculation_parcels` from `output.to_crs(CALCULATION_CRS)`.
8. Computes `parcel_geometries` from `_calculation_geometries(calculation_parcels)`.
9. Computes `nearest_line` from `_nearest_feature_rows(parcel_geometries, valid_lines, _LINE_MATCH_COLUMNS)`.
10. Calls `_attach_matches(output, nearest_line, _LINE_OUTPUT_MAPPING)` for its validation or side effect.
11. Computes `exact_mask` from `(valid_lines['voltage_status'] == 'EXACT') & valid_lines['voltage_kv'].map(_is_positive_finite_number)`.
12. Computes `exact_lines` from `valid_lines.loc[exact_mask].reset_index(drop=True).copy()`.
13. Computes `exact_lines['voltage_kv']` from `exact_lines['voltage_kv'].map(float).astype('float64')`.
14. Computes `nearest_exact` from `_nearest_feature_rows(parcel_geometries, exact_lines, _LINE_MATCH_COLUMNS, allow_empty=True)`.
15. Calls `_attach_matches(output, nearest_exact, _EXACT_LINE_OUTPUT_MAPPING)` for its validation or side effect.
16. Computes `nearest_post` from `_nearest_feature_rows(parcel_geometries, valid_posts, _POST_MATCH_COLUMNS)`.
17. Calls `_attach_matches(output, nearest_post, _POST_OUTPUT_MAPPING)` for its validation or side effect.
18. Computes `(voltage_table, voltage_coverage)` from `_voltage_level_table(output['parcel_id'], parcel_geometries, exact_lines)`.
19. Computes `result` from `GridProximityResult(parcels=output, voltage_level_proximity=voltage_table, voltage_level_coverage=voltage_coverage)`.
20. Calls `_validate_output_integrity(parcels, result)` for its validation or side effect.
21. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `valid_lines.empty` is true.
- Rejects or diverts the path when `valid_posts.empty` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `output.to_crs`, `parcels.reset_index(drop=True).copy`, `valid_lines.loc[exact_mask].reset_index(drop=True).copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `GridProximityError`, `GridProximityResult`, `_attach_matches`, `_calculation_geometries`, `_nearest_feature_rows`, `_validate_grid`, `_validate_output_integrity`, `_validate_parcels`, `_voltage_level_table`, `exact_lines['voltage_kv'].map`, `exact_lines['voltage_kv'].map(float).astype`, `output.to_crs`, `parcels.reset_index`, `parcels.reset_index(drop=True).copy`, `valid_lines.loc[exact_mask].reset_index`, `valid_lines.loc[exact_mask].reset_index(drop=True).copy`, `valid_lines['voltage_kv'].map`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `enrich_parcel_grid_proximity`
- `tests/unit/test_assess_grid_coverage.py` — `_proximity`
- `tests/unit/test_assess_grid_coverage.py` — `test_geographic_parcel_storage_crs_and_geometry_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `_two_parcel_two_voltage_result`
- `tests/unit/test_enrich_grid_proximity.py` — `test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_cross_voltage_tie_uses_lexical_global_feature_id`
- `tests/unit/test_enrich_grid_proximity.py` — `test_distance_profile_is_threshold_free_and_tracks_ties`
- `tests/unit/test_enrich_grid_proximity.py` — `test_duplicate_grid_feature_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_epsg2154_parcel_input_remains_epsg2154`
- `tests/unit/test_enrich_grid_proximity.py` — `test_epsg4326_input_is_calculated_in_lambert93_and_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_invalid_exact_voltage_values_are_not_used_as_exact`
- `tests/unit/test_enrich_grid_proximity.py` — `test_invalid_parcel_id_hygiene_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_line_tie_is_counted_and_lexical_feature_id_wins`
- `tests/unit/test_enrich_grid_proximity.py` — `test_missing_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_missing_parcel_column_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nearest_any_line_preserves_every_voltage_status`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nearest_exact_and_voltage_table_exclude_nonexact_lines`
- `tests/unit/test_enrich_grid_proximity.py` — `test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`
- `tests/unit/test_enrich_grid_proximity.py` — `test_no_valid_required_grid_feature_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_nonvalid_grid_geometries_are_excluded_without_row_loss`
- `tests/unit/test_enrich_grid_proximity.py` — `test_null_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_post_distance_uses_parcel_and_post_polygons`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_allows_consistent_missing_manager_and_asset_status`
- `tests/unit/test_enrich_grid_proximity.py` — `test_profile_rejects_nonnull_exact_field_without_exact_coverage`
- `tests/unit/test_enrich_grid_proximity.py` — `test_semantically_wrong_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_separated_distance_uses_parcel_edge_not_centroid`
- `tests/unit/test_enrich_grid_proximity.py` — `test_supported_multi_geometries_are_accepted`
- `tests/unit/test_enrich_grid_proximity.py` — `test_supported_parcel_polygon_geometry_is_preserved`
- `tests/unit/test_enrich_grid_proximity.py` — `test_touching_line_has_zero_distance`
- `tests/unit/test_enrich_grid_proximity.py` — `test_unsupported_valid_grid_geometry_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_valid_parcel_id_is_preserved_exactly`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_grid_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_grid_feature_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_wrong_spatial_role_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py` — `test_z_line_has_same_horizontal_distance_as_xy_line`

**Tests**

- `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id`
- `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties`
- `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154`
- `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact`
- `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins`
- `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status`
- `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines`
- `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`
- `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss`
- `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status`
- `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage`
- `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid`
- `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted`
- `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved`
- `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance`
- `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected`
- `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `enrich_parcel_grid_proximity`

**Signature**

```python
def enrich_parcel_grid_proximity(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridProximityResult:
```

**Purpose**

Compute proximity from one physically revalidated IGN source bundle.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `electricity_source` (`IgnBdTopoElectricityData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GridProximityResult`. Observed return expression(s): `_enrich_parcel_grid_proximity_from_normalized(parcels, normalized.electric_lines, normalized.transformation_posts)`.

**Algorithm**

1. Runs guarded operation: Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `GridProximityError('parcels must be a GeoDataFrame with active geometry')`. Checks `type(electricity_source) is not IgnBdTopoElectricityData`. When true: Raises `GridProximityError('electricity source must be an IgnBdTopoElectricityData')`. Checks `type(source_config) is not IgnBdTopoSourceConfig`. When true: Raises `GridProximityError('source_config must be an IgnBdTopoSourceConfig')`. Calls `_validate_parcels(parcels)` for its validation or side effect. Executes 3 additional source-ordered statement(s). Handles `GridProximityError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `type(electricity_source) is not IgnBdTopoElectricityData` is true.
- Rejects or diverts the path when `type(source_config) is not IgnBdTopoSourceConfig` is true.
- Rejects or diverts the path when `type(normalized) is not NormalizedIgnElectricityData` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridProximityError`, `_enrich_parcel_grid_proximity_from_normalized`, `_validate_parcels`, `isinstance`, `normalize_ign_electricity`, `type`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `assess_grid_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_distance_profile`

**Signature**

```python
def _distance_profile(distances: pd.Series, ties: pd.Series) -> DistanceProfile:
```

**Purpose**

Implements distance profile according to the exact implementation and guards in this file.

**Inputs**

- `distances` (`pd.Series`; required) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `ties` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `DistanceProfile`. Observed return expression(s): `DistanceProfile(count=len(values), missing_count=missing_count, minimum=float(values.min()), p01=float(values.quantile(0.01)), p05=float(values.quantile(0.05)), p10=float(values.quantile(0.1)), p25=float(values.quantile(0.25)), p50=float(values.quantile(0.5)), p75=float(values.quantile(0.75)), p90=float(values.quantile(0.9)), p95=float(values.quantile(0.95)), p99=float(values.quantile(0.99)), max…`; `DistanceProfile(count=0, missing_count=missing_count, minimum=None, p01=None, p05=None, p10=None, p25=None, p50=None, p75=None, p90=None, p95=None, p99=None, maximum=None, zero_distance_count=0, tie_count=0)`.

**Algorithm**

1. Calls `_validate_distance_values(distances, 'Profile')` for its validation or side effect.
2. Computes `values` from `distances.dropna().astype('float64')`.
3. Computes `missing_count` from `int(distances.isna().sum())`.
4. Checks `values.empty`. When true: Returns `DistanceProfile(count=0, missing_count=missing_count, minimum=None, p01=None, p05=None, p10=None, p25=None, p50=None, p75=None, p90=None, p95=None, p99=None, maximum=None, zero_distance_count=0, tie_count=0)`.
5. Computes `matched_ties` from `ties.loc[distances.notna()]`.
6. Checks `matched_ties.isna().any()`. When true: Raises `GridProximityError('Matched distance rows require tie counts')`.
7. Returns `DistanceProfile(count=len(values), missing_count=missing_count, minimum=float(values.min()), p01=float(values.quantile(0.01)), p05=float(values.quantile(0.05)), p10=float(values.quantile(0.1)), p25=float(values.quantile(0.25)), p50=float(values.quantile(0.5)), p75=float(values.quantile(0.75)), p90=float(values.quantile(0.9)), p95=float(values.quantile(0.95)…`.

**Validation and invariants**

- Rejects or diverts the path when `matched_ties.isna().any()` is true.

**Exceptions**

- Explicitly raises: `GridProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `DistanceProfile`, `GridProximityError`, `_validate_distance_values`, `distances.dropna`, `distances.dropna().astype`, `distances.isna`, `distances.isna().sum`, `distances.notna`, `float`, `int`, `len`, `matched_ties.isna`, `matched_ties.isna().any`, `matched_ties.tolist`, `sum`, `values.eq`, `values.eq(0).sum`, `values.max`, `values.min`, `values.quantile`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `profile_grid_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `profile_grid_proximity`

**Signature**

```python
def profile_grid_proximity(result: GridProximityResult) -> GridProximityProfile:
```

**Purpose**

Profile proximity distances without thresholds or suitability labels.

**Inputs**

- `result` (`GridProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `GridProximityProfile`. Observed return expression(s): `GridProximityProfile(parcel_count=len(parcels), nearest_line=_distance_profile(parcels['nearest_line_proxy_distance_m'], parcels['nearest_line_tie_count']), nearest_exact_line=_distance_profile(parcels['nearest_exact_line_proxy_distance_m'], parcels['nearest_exact_line_tie_count']), nearest_post=_distance_profile(parcels['nearest_post_proxy_distance_m'], parcels['nearest_post_tie_count']), voltag…`.

**Algorithm**

1. Calls `_validate_result_contract(result)` for its validation or side effect.
2. Computes `parcels` from `result.parcels`.
3. Computes `coverage` from `{float(item.voltage_kv): item.line_feature_count for item in result.voltage_level_coverage}`.
4. Defines `voltage_profiles` with annotation `list[VoltageLevelDistanceProfile]` from `[]`.
5. Computes `table` from `result.voltage_level_proximity`.
6. Computes `observed_levels` from `tuple(coverage)`.
7. Iterates `voltage_kv` over `observed_levels`. For each value: Computes `rows` from `table.loc[table['voltage_kv'] == voltage_kv]`. Computes `distance` from `_distance_profile(rows['nearest_line_proxy_distance_m'], rows['tie_count'])`. Calls `voltage_profiles.append(VoltageLevelDistanceProfile(voltage_kv=voltage_kv, line_feature_count=coverage[voltage_kv], parcel_proximity_count=len(rows), distance=distance))` for its validation or side effect.
8. Returns `GridProximityProfile(parcel_count=len(parcels), nearest_line=_distance_profile(parcels['nearest_line_proxy_distance_m'], parcels['nearest_line_tie_count']), nearest_exact_line=_distance_profile(parcels['nearest_exact_line_proxy_distance_m'], parcels['nearest_exact_line_tie_count']), nearest_post=_distance_profile(parcels['nearest_post_proxy_distance_m'], pa…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `GridProximityProfile`, `VoltageLevelDistanceProfile`, `_distance_profile`, `_validate_result_contract`, `float`, `len`, `tuple`, `voltage_profiles.append`.

**Known repository callers**

- `src/landscout/stages/assess_grid_coverage.py` — `_assess_grid_coverage_from_proximity`
- `src/landscout/stages/assess_grid_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `_distance` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `_parcel_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `feature_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `grid_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `grid_feature_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `kind` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `manager_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_exact_line_voltage_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_grid_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_line_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_post_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_post_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_upper_bound_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
