# `src/landscout/stages/enrich_road_proximity.py`

## File identity

- Repository path: `src/landscout/stages/enrich_road_proximity.py`
- File type: Python source
- Primary responsibility: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.
- Layer / domain: `stage` / `road`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `01bc54d789f3f3dca1d3e62c93aee4c686233b079025d1d96e01169523e56dfa`

## 1. Purpose

Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `road` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from numbers import Integral` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pandas.api.types import ( # type: ignore[import-untyped] is_bool_dtype, is_numeric_dtype, )` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.
- `from shapely import STRtree, force_2d` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoRoadData, IgnBdTopoSourceConfig, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.apply_road_vehicle_proxy_policy import ( IgnRoadVehicleProxyApplicationResult, apply_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.road_vehicle_proxy_policy import ( IgnRoadVehicleProxyPolicy, load_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `_PARCEL_STORAGE_CRS` | `"EPSG:4326"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_CALCULATION_CRS` | `"EPSG:2154"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_PROXIMITY_SCOPE` | `"WITHIN_VERIFIED_SOURCE_PACKAGE"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_PARCEL_GEOMETRY_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_ROAD_GEOMETRY_TYPES` | `frozenset({"LineString", "MultiLineString"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_ROAD_GEOMETRY_STATUSES` | `frozenset({"VALID", "NULL", "EMPTY", "INVALID"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_ROAD_MATCH_COLUMNS` | `( "road_feature_id", "source_feature_id", "road_proxy_primary_rule", "road_proxy_rule_trace_json", "road_proxy_unknown_fields_json", "road_proxy_toll_evidence", "nature_raw", "importance_raw", "asset_status_raw", "private_raw", "light_vehicle_access_raw", "carriageway_width_raw", "closure_period_raw", "restriction_nature_raw", "source_layer", "source_department_code", "source_edition", "source_archive_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_ROAD_REQUIRED_COLUMNS` | `frozenset( { *_ROAD_MATCH_COLUMNS, "geometry_status", "road_proxy_class", "road_proxy_policy_id", "road_proxy_policy_schema_version", "road_proxy_policy_config_sha256", "road_proxy_policy_scope", "road_proxy_heavy_vehicle_access", "geometry", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_MATCH_OUTPUT_MAPPING` | `{ "distance_m": "nearest_road_proxy_distance_m", "road_feature_id": "nearest_road_feature_id", "source_feature_id": "nearest_source_feature_id", "tie_count": "nearest_road_tie_count", "road_proxy_primary_rule": "nearest_road_primary_rule", "road_proxy_rule_trace_json": "nearest_road_rule_trace_json", "road_proxy_unknown_fields_json": "nearest_road_unknown_fields_json", "road_proxy_toll_evidence": "nearest_road_toll_evidence", "nature_raw": "nearest_nature_raw", "importance_raw": "nearest_importance_raw", "asset_status_raw": "nearest_asset_status_raw", "private_raw": "nearest_private_raw", "light_vehicle_access_raw": "nearest_light_vehicle_access_raw", "carriageway_width_raw": "nearest_carriageway_width_raw", "closure_period_raw": "nearest_closure_period_raw", "restriction_nature_raw": "nearest_restriction_nature_raw", "source_layer": "nearest_source_layer", "source_department_code": "nearest_source_department_code", "source_edition": "nearest_source_edition", "source_archive_sha256": "nearest_source_archive_sha256", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CLASS_PROXIMITY_COLUMNS` | `( "parcel_id", "road_proxy_class", "nearest_road_proxy_distance_m", "nearest_road_feature_id", "nearest_source_feature_id", "nearest_road_tie_count", "nearest_road_primary_rule", "nearest_road_rule_trace_json", "nearest_road_unknown_fields_json", "nearest_road_toll_evidence", "nearest_nature_raw", "nearest_importance_raw", "nearest_asset_status_raw", "nearest_private_raw", "nearest_light_vehicle_access_raw", "nearest_carriageway_width_raw", "nearest_closure_period_raw", "nearest_restriction_nature_raw", "nearest_source_layer", "nearest_source_department_code", "nearest_source_edition", "nearest_source_archive_sha256", "road_proxy_policy_id", "road_proxy_policy_schema_version", "road_proxy_policy_config_sha256", "road_proxy_heavy_vehicle_access", "proximity_scope", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `RoadProximityError`

**Purpose:** Raised when parcel-to-road proximity cannot be proven safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `RoadProxyClassCoverage`

**Purpose:** Source coverage and distance eligibility for one policy class.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `road_proxy_class` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_road_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `feature_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `distance_eligible` | `bool` | `required` | `bool` state used by `src/landscout/stages/enrich_road_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `ParcelRoadProximityResult`

**Purpose:** Unchanged parcels plus class-specific factual road proximity.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `class_proximity` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/enrich_road_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `class_coverage` | `tuple[RoadProxyClassCoverage, ...]` | `required` | `tuple[RoadProxyClassCoverage, ...]` state used by `src/landscout/stages/enrich_road_proximity.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

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

1. Checks `value is None`. When true: Raises `RoadProximityError(f'{label} CRS is required')`.
2. Runs guarded operation: Returns `CRS.from_user_input(value)`. Handles `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `value is None` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_user_input`, `RoadProximityError`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_require_crs`
- `src/landscout/stages/enrich_road_proximity.py` — `_validate_parcel_preservation`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_crs`

**Signature**

```python
def _require_crs(value: object, expected_epsg: int, label: str) -> None:
```

**Purpose**

Implements require crs according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected_epsg` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `actual` from `_validated_crs(value, label)`.
2. Computes `expected` from `CRS.from_epsg(expected_epsg)`.
3. Checks `not actual.equals(expected)`. When true: Raises `RoadProximityError(f'{label} must use EPSG:{expected_epsg}')`.

**Validation and invariants**

- Rejects or diverts the path when `not actual.equals(expected)` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `RoadProximityError`, `_validated_crs`, `actual.equals`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_validate_application_roads`
- `src/landscout/stages/enrich_road_proximity.py` — `_validate_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_exact_ids`

**Signature**

```python
def _validate_exact_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
```

**Purpose**

Validates and rejects malformed exact ids according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `require_unique` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `values.isna().any()`. When true: Raises `RoadProximityError(f'{label} values must not be null')`.
2. Computes `raw` from `values.tolist()`.
3. Checks `any((not isinstance(value, str) for value in raw))`. When true: Raises `RoadProximityError(f'{label} values must be exact strings')`.
4. Checks `any((not value.strip() for value in raw))`. When true: Raises `RoadProximityError(f'{label} values must not be empty')`.
5. Checks `any((value != value.strip() for value in raw))`. When true: Raises `RoadProximityError(f'{label} values must not have edge whitespace')`.
6. Checks `require_unique and values.duplicated().any()`. When true: Raises `RoadProximityError(f'{label} values must be unique')`.

**Validation and invariants**

- Rejects or diverts the path when `values.isna().any()` is true.
- Rejects or diverts the path when `any((not isinstance(value, str) for value in raw))` is true.
- Rejects or diverts the path when `any((not value.strip() for value in raw))` is true.
- Rejects or diverts the path when `any((value != value.strip() for value in raw))` is true.
- Rejects or diverts the path when `require_unique and values.duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityError`, `any`, `isinstance`, `value.strip`, `values.duplicated`, `values.duplicated().any`, `values.isna`, `values.isna().any`, `values.tolist`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_validate_application_roads`
- `src/landscout/stages/enrich_road_proximity.py` — `_validate_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_parcels`

**Signature**

```python
def _validate_parcels(parcels: object) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed parcels according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`object`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `parcels`.

**Algorithm**

1. Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `RoadProximityError('parcels must be a GeoDataFrame')`.
2. Checks `parcels.columns.duplicated().any()`. When true: Raises `RoadProximityError('Parcel columns must not contain duplicates')`.
3. Computes `missing` from `{'parcel_id', 'geometry'} - set(parcels.columns)`.
4. Checks `missing`. When true: Raises `RoadProximityError('Missing required parcel columns: ' + ', '.join(sorted(missing)))`.
5. Checks `parcels.active_geometry_name != 'geometry'`. When true: Raises `RoadProximityError('Parcel geometry column must be active')`.
6. Calls `_require_crs(parcels.crs, 4326, 'Parcel storage')` for its validation or side effect.
7. Calls `_validate_exact_ids(parcels['parcel_id'], 'parcel_id', require_unique=True)` for its validation or side effect.
8. Checks `parcels.geometry.isna().any()`. When true: Raises `RoadProximityError('Parcel geometries must not be null')`.
9. Checks `parcels.geometry.is_empty.any()`. When true: Raises `RoadProximityError('Parcel geometries must not be empty')`.
10. Checks `not parcels.geometry.is_valid.all()`. When true: Raises `RoadProximityError('Parcel geometries must be valid')`.
11. Computes `unsupported` from `sorted(set(parcels.geometry.geom_type.dropna()) - _PARCEL_GEOMETRY_TYPES)`.
12. Checks `unsupported`. When true: Raises `RoadProximityError('Parcel geometries must be Polygon or MultiPolygon; found: ' + ', '.join((str(value) for value in unsupported)))`.
13. Returns `parcels`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `parcels.columns.duplicated().any()` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `parcels.active_geometry_name != 'geometry'` is true.
- Rejects or diverts the path when `parcels.geometry.isna().any()` is true.
- Rejects or diverts the path when `parcels.geometry.is_empty.any()` is true.
- Rejects or diverts the path when `not parcels.geometry.is_valid.all()` is true.
- Rejects or diverts the path when `unsupported` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `RoadProximityError`, `_require_crs`, `_validate_exact_ids`, `isinstance`, `parcels.columns.duplicated`, `parcels.columns.duplicated().any`, `parcels.geometry.geom_type.dropna`, `parcels.geometry.is_empty.any`, `parcels.geometry.is_valid.all`, `parcels.geometry.isna`, `parcels.geometry.isna().any`, `set`, `sorted`, `str`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_enrich_parcel_road_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_policy_classes`

**Signature**

```python
def _policy_classes(
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
```

**Purpose**

Implements policy classes according to the exact implementation and guards in this file.

**Inputs**

- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[tuple[str, ...], tuple[str, ...]]`. Observed return expression(s): `(all_classes, eligible)`.

**Algorithm**

1. Computes `all_classes` from `policy.classes.values`.
2. Checks `len(all_classes) != 6 or len(set(all_classes)) != 6`. When true: Raises `RoadProximityError('Compiled road policy class domain is invalid')`.
3. Computes `non_distance` from `policy.classes.not_distance_proxy`.
4. Computes `eligible` from `tuple((value for value in all_classes if value != non_distance))`.
5. Checks `len(eligible) != 5 or non_distance not in all_classes`. When true: Raises `RoadProximityError('Compiled road distance eligibility is invalid')`.
6. Returns `(all_classes, eligible)`.

**Validation and invariants**

- Rejects or diverts the path when `len(all_classes) != 6 or len(set(all_classes)) != 6` is true.
- Rejects or diverts the path when `len(eligible) != 5 or non_distance not in all_classes` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityError`, `len`, `set`, `tuple`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_class_proximity_table`
- `src/landscout/stages/enrich_road_proximity.py` — `_coverage`
- `src/landscout/stages/enrich_road_proximity.py` — `_validate_application_roads`
- `src/landscout/stages/enrich_road_proximity.py` — `_validate_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_row_lineage`

**Signature**

```python
def _require_row_lineage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> None:
```

**Purpose**

Implements require row lineage according to the exact implementation and guards in this file.

**Inputs**

- `roads` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `expected` from `{'road_proxy_policy_id': policy.policy_id, 'road_proxy_policy_schema_version': policy.schema_version, 'road_proxy_policy_config_sha256': policy.config_sha256, 'road_proxy_policy_scope': policy.scope, 'road_proxy_heavy_vehicle_access': policy.heavy_vehicle_access}`.
2. Iterates `(column, value)` over `expected.items()`. For each value: Checks `roads[column].isna().any() or not roads[column].eq(value).all()`. When true: Raises `RoadProximityError(f'Road application policy lineage differs in {column}')`.

**Validation and invariants**

- Rejects or diverts the path when `roads[column].isna().any() or not roads[column].eq(value).all()` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityError`, `expected.items`, `roads[column].eq`, `roads[column].eq(value).all`, `roads[column].isna`, `roads[column].isna().any`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_validate_application_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_application_roads`

**Signature**

```python
def _validate_application_roads(
    application: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed application roads according to the exact implementation and guards in this file.

**Inputs**

- `application` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `roads`.

**Algorithm**

1. Checks `type(application) is not IgnRoadVehicleProxyApplicationResult`. When true: Raises `RoadProximityError('Road application result type is invalid')`.
2. Computes `roads` from `application.roads`.
3. Checks `not isinstance(roads, gpd.GeoDataFrame)`. When true: Raises `RoadProximityError('Road application roads must be a GeoDataFrame')`.
4. Checks `roads.columns.duplicated().any()`. When true: Raises `RoadProximityError('Road application columns must not be duplicated')`.
5. Computes `missing` from `_ROAD_REQUIRED_COLUMNS - set(roads.columns)`.
6. Checks `missing`. When true: Raises `RoadProximityError('Missing road application column or lineage: ' + ', '.join(sorted(missing)))`.
7. Checks `roads.active_geometry_name != 'geometry'`. When true: Raises `RoadProximityError('Road application geometry must be active')`.
8. Calls `_require_crs(roads.crs, 2154, 'Road application')` for its validation or side effect.
9. Calls `_validate_exact_ids(roads['road_feature_id'], 'road_feature_id', require_unique=True)` for its validation or side effect.
10. Calls `_validate_exact_ids(roads['source_feature_id'], 'source_feature_id', require_unique=False)` for its validation or side effect.
11. Computes `(all_classes, eligible_classes)` from `_policy_classes(policy)`.
12. Computes `classes` from `roads['road_proxy_class']`.
13. Checks `classes.isna().any() or not classes.isin(all_classes).all()`. When true: Raises `RoadProximityError('Road application has an unknown proxy class')`.
14. Calls `_require_row_lineage(roads, policy)` for its validation or side effect.
15. Computes `statuses` from `roads['geometry_status']`.
16. Checks `statuses.isna().any() or not statuses.isin(_ROAD_GEOMETRY_STATUSES).all()`. When true: Raises `RoadProximityError('Road application geometry status is invalid')`.
17. Computes `eligible` from `classes.isin(eligible_classes)`.
18. Checks `not statuses.loc[eligible].eq('VALID').all()`. When true: Raises `RoadProximityError('Distance-eligible roads must have VALID geometry status')`.
19. Computes `eligible_geometry` from `roads.loc[eligible, 'geometry']`.
20. Checks `eligible_geometry.isna().any()`. When true: Raises `RoadProximityError('Distance-eligible road geometry must not be null')`.
21. Checks `eligible_geometry.is_empty.any()`. When true: Raises `RoadProximityError('Distance-eligible road geometry must not be empty')`.
22. Checks `not eligible_geometry.is_valid.all()`. When true: Raises `RoadProximityError('Distance-eligible road geometry must be valid')`.
23. Computes `unsupported` from `sorted(set(eligible_geometry.geom_type.dropna()) - _ROAD_GEOMETRY_TYPES)`.
24. Checks `unsupported`. When true: Raises `RoadProximityError('Distance-eligible geometry must be LineString or MultiLineString; found: ' + ', '.join((str(value) for value in unsupported)))`.
25. Returns `roads`.

**Validation and invariants**

- Rejects or diverts the path when `type(application) is not IgnRoadVehicleProxyApplicationResult` is true.
- Rejects or diverts the path when `not isinstance(roads, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `roads.columns.duplicated().any()` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `roads.active_geometry_name != 'geometry'` is true.
- Rejects or diverts the path when `classes.isna().any() or not classes.isin(all_classes).all()` is true.
- Rejects or diverts the path when `statuses.isna().any() or not statuses.isin(_ROAD_GEOMETRY_STATUSES).all()` is true.
- Rejects or diverts the path when `not statuses.loc[eligible].eq('VALID').all()` is true.
- Rejects or diverts the path when `eligible_geometry.isna().any()` is true.
- Rejects or diverts the path when `eligible_geometry.is_empty.any()` is true.
- Rejects or diverts the path when `not eligible_geometry.is_valid.all()` is true.
- Rejects or diverts the path when `unsupported` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `RoadProximityError`, `_policy_classes`, `_require_crs`, `_require_row_lineage`, `_validate_exact_ids`, `classes.isin`, `classes.isin(all_classes).all`, `classes.isna`, `classes.isna().any`, `eligible_geometry.geom_type.dropna`, `eligible_geometry.is_empty.any`, `eligible_geometry.is_valid.all`, `eligible_geometry.isna`, `eligible_geometry.isna().any`, `isinstance`, `roads.columns.duplicated`, `roads.columns.duplicated().any`, `set`, `sorted`, `statuses.isin`, `statuses.isin(_ROAD_GEOMETRY_STATUSES).all`, `statuses.isna`, `statuses.isna().any`, `statuses.loc[eligible].eq`, `statuses.loc[eligible].eq('VALID').all`, `str`, `type`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_enrich_parcel_road_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

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

- `src/landscout/stages/enrich_road_proximity.py` — `_enrich_parcel_road_proximity`
- `src/landscout/stages/enrich_road_proximity.py` — `_nearest_class_rows`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_empty_nearest_rows`

**Signature**

```python
def _empty_nearest_rows(parcel_count: int) -> pd.DataFrame:
```

**Purpose**

Implements empty nearest rows according to the exact implementation and guards in this file.

**Inputs**

- `parcel_count` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `pd.DataFrame(index=pd.RangeIndex(parcel_count))`.
2. Computes `output['distance_m']` from `pd.Series(np.nan, index=output.index, dtype='float64')`.
3. Computes `output['tie_count']` from `pd.Series(pd.NA, index=output.index, dtype='Int64')`.
4. Iterates `column` over `_ROAD_MATCH_COLUMNS`. For each value: Checks `column == 'road_proxy_toll_evidence'`. When true: Computes `output[column]` from `pd.Series(pd.NA, index=output.index, dtype='boolean')`. Otherwise: Computes `output[column]` from `pd.Series(pd.NA, index=output.index, dtype='object')`.
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

- `src/landscout/stages/enrich_road_proximity.py` — `_nearest_class_rows`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_nearest_class_rows`

**Signature**

```python
def _nearest_class_rows(
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Implements nearest class rows according to the exact implementation and guards in this file.

**Inputs**

- `parcel_geometries` (`np.ndarray`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `roads` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`; `_empty_nearest_rows(parcel_count)`.

**Algorithm**

1. Computes `parcel_count` from `len(parcel_geometries)`.
2. Checks `roads.empty`. When true: Returns `_empty_nearest_rows(parcel_count)`.
3. Computes `tree` from `STRtree(_calculation_geometries(roads))`.
4. Computes `(indices, distances)` from `tree.query_nearest(parcel_geometries, all_matches=True, return_distance=True)`.
5. Computes `matches` from `pd.DataFrame({'parcel_position': indices[0], 'road_position': indices[1], 'distance_m': distances})`.
6. Computes `matches['road_feature_id']` from `roads.iloc[matches['road_position'].to_numpy()]['road_feature_id'].to_numpy()`.
7. Computes `matches` from `matches.sort_values(['parcel_position', 'distance_m', 'road_feature_id'], kind='mergesort')`.
8. Computes `ties` from `matches.groupby('parcel_position', sort=False).size()`.
9. Computes `selected` from `matches.drop_duplicates('parcel_position', keep='first').sort_values('parcel_position', kind='mergesort')`.
10. Checks `selected['parcel_position'].tolist() != list(range(parcel_count))`. When true: Raises `RoadProximityError('Nearest-road matching did not cover every parcel')`.
11. Computes `source_rows` from `roads.iloc[selected['road_position'].to_numpy()]`.
12. Computes `output` from `source_rows.loc[:, list(_ROAD_MATCH_COLUMNS)].reset_index(drop=True)`.
13. Calls `output.insert(0, 'tie_count', pd.Series(ties.reindex(range(parcel_count)).to_numpy(), dtype='Int64'))` for its validation or side effect.
14. Calls `output.insert(0, 'distance_m', selected['distance_m'].to_numpy(dtype='float64'))` for its validation or side effect.
15. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `selected['parcel_position'].tolist() != list(range(parcel_count))` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityError`, `STRtree`, `_calculation_geometries`, `_empty_nearest_rows`, `len`, `list`, `matches.drop_duplicates`, `matches.drop_duplicates('parcel_position', keep='first').sort_values`, `matches.groupby`, `matches.groupby('parcel_position', sort=False).size`, `matches.sort_values`, `matches['road_position'].to_numpy`, `output.insert`, `pd.DataFrame`, `pd.Series`, `range`, `roads.iloc[matches['road_position'].to_numpy()]['road_feature_id'].to_numpy`, `selected['distance_m'].to_numpy`, `selected['parcel_position'].tolist`, `selected['road_position'].to_numpy`, `source_rows.loc[:, list(_ROAD_MATCH_COLUMNS)].reset_index`, `ties.reindex`, `ties.reindex(range(parcel_count)).to_numpy`, `tree.query_nearest`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_class_proximity_table`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_coverage`

**Signature**

```python
def _coverage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[RoadProxyClassCoverage, ...]:
```

**Purpose**

Implements coverage according to the exact implementation and guards in this file.

**Inputs**

- `roads` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[RoadProxyClassCoverage, ...]`. Observed return expression(s): `tuple((RoadProxyClassCoverage(road_proxy_class=road_class, feature_count=int(counts.get(road_class, 0)), distance_eligible=road_class in eligible_classes) for road_class in all_classes))`.

**Algorithm**

1. Computes `(all_classes, eligible_classes)` from `_policy_classes(policy)`.
2. Computes `counts` from `roads['road_proxy_class'].value_counts()`.
3. Returns `tuple((RoadProxyClassCoverage(road_proxy_class=road_class, feature_count=int(counts.get(road_class, 0)), distance_eligible=road_class in eligible_classes) for road_class in all_classes))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProxyClassCoverage`, `_policy_classes`, `counts.get`, `int`, `roads['road_proxy_class'].value_counts`, `tuple`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_enrich_parcel_road_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_class_proximity_table`

**Signature**

```python
def _class_proximity_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> pd.DataFrame:
```

**Purpose**

Implements class proximity table according to the exact implementation and guards in this file.

**Inputs**

- `parcel_ids` (`pd.Series`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcel_geometries` (`np.ndarray`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `roads` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]`.

**Algorithm**

1. Computes `(_, eligible_classes)` from `_policy_classes(policy)`.
2. Defines `tables` with annotation `list[pd.DataFrame]` from `[]`.
3. Iterates `(class_position, road_class)` over `enumerate(eligible_classes)`. For each value: Computes `class_roads` from `roads.loc[roads['road_proxy_class'].eq(road_class)].reset_index(drop=True)`. Computes `nearest` from `_nearest_class_rows(parcel_geometries, class_roads)`. Calls `_validate_distance_and_ties(nearest.rename(columns={'distance_m': 'nearest_road_proxy_distance_m', 'tie_count': 'nearest_road_tie_count'}), expect_matches=not class_roads.empty)` for its validation or side effect. Executes 8 additional source-ordered statement(s).
4. Computes `output` from `pd.concat(tables, ignore_index=True)`.
5. Computes `output` from `output.sort_values(['_parcel_position', '_class_position'], kind='mergesort').reset_index(drop=True)`.
6. Computes `output` from `output.drop(columns=['_parcel_position', '_class_position'])`.
7. Computes `output['nearest_road_proxy_distance_m']` from `output['nearest_road_proxy_distance_m'].astype('float64')`.
8. Computes `output['nearest_road_tie_count']` from `output['nearest_road_tie_count'].astype('Int64')`.
9. Computes `output['nearest_road_toll_evidence']` from `output['nearest_road_toll_evidence'].astype('boolean')`.
10. Returns `output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_MATCH_OUTPUT_MAPPING.items`, `_nearest_class_rows`, `_policy_classes`, `_validate_distance_and_ties`, `enumerate`, `len`, `list`, `nearest.rename`, `nearest[source_column].reset_index`, `np.arange`, `output.drop`, `output.sort_values`, `output.sort_values(['_parcel_position', '_class_position'], kind='mergesort').reset_index`, `output['nearest_road_proxy_distance_m'].astype`, `output['nearest_road_tie_count'].astype`, `output['nearest_road_toll_evidence'].astype`, `parcel_ids.reset_index`, `pd.DataFrame`, `pd.concat`, `roads.loc[roads['road_proxy_class'].eq(road_class)].reset_index`, `roads['road_proxy_class'].eq`, `tables.append`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_enrich_parcel_road_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

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

- Declared return type: `bool`. Observed return expression(s): `True`; `bool(pd.isna(value))`; `False`.

**Algorithm**

1. Checks `value is None`. When true: Returns `True`.
2. Runs guarded operation: Returns `bool(pd.isna(value))`. Handles `(TypeError, ValueError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_validate_distance_and_ties`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_distance_and_ties`

**Signature**

```python
def _validate_distance_and_ties(
    rows: pd.DataFrame,
    *,
    expect_matches: bool,
) -> None:
```

**Purpose**

Validates and rejects malformed distance and ties according to the exact implementation and guards in this file.

**Inputs**

- `rows` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expect_matches` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `distances` from `rows['nearest_road_proxy_distance_m']`.
2. Computes `matched` from `distances.notna()`.
3. Checks `expect_matches and (not matched.all())`. When true: Raises `RoadProximityError('Non-empty road classes require parcel matches')`.
4. Checks `not expect_matches and matched.any()`. When true: Raises `RoadProximityError('Empty road classes must not contain matches')`.
5. Checks `matched.any()`. When true: Checks `not is_numeric_dtype(distances.dtype) or is_bool_dtype(distances.dtype)`. When true: Raises `RoadProximityError('Matched road distances must be numeric')`. Computes `numeric` from `distances.loc[matched].to_numpy(dtype='float64')`. Checks `not np.isfinite(numeric).all() or (numeric < 0).any()`. When true: Raises `RoadProximityError('Matched road distances must be finite and >= 0')`.
6. Computes `ties` from `rows['nearest_road_tie_count']`.
7. Iterates `(value, row_matched)` over `zip(ties.tolist(), matched.to_numpy(dtype=bool), strict=True)`. For each value: Computes `missing` from `_is_missing_scalar(value)`. Checks `not row_matched`. When true: Checks `not missing`. When true: Raises `RoadProximityError('Unmatched rows require null tie_count')`. Executes `continue` control flow. Checks `missing or not isinstance(value, Integral) or isinstance(value, (bool, np.bool_)) or (int(value) < 1)`. When true: Raises `RoadProximityError('Matched nearest_road_tie_count must be an integer >= 1')`.

**Validation and invariants**

- Rejects or diverts the path when `expect_matches and (not matched.all())` is true.
- Rejects or diverts the path when `not expect_matches and matched.any()` is true.
- Rejects or diverts the path when `matched.any()` is true.
- Rejects or diverts the path when `not is_numeric_dtype(distances.dtype) or is_bool_dtype(distances.dtype)` is true.
- Rejects or diverts the path when `not np.isfinite(numeric).all() or (numeric < 0).any()` is true.
- Rejects or diverts the path when `not row_matched` is true.
- Rejects or diverts the path when `missing or not isinstance(value, Integral) or isinstance(value, (bool, np.bool_)) or (int(value) < 1)` is true.
- Rejects or diverts the path when `not missing` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(numeric < 0).any`, `RoadProximityError`, `_is_missing_scalar`, `distances.loc[matched].to_numpy`, `distances.notna`, `int`, `is_bool_dtype`, `is_numeric_dtype`, `isinstance`, `matched.all`, `matched.any`, `matched.to_numpy`, `np.isfinite`, `np.isfinite(numeric).all`, `ties.tolist`, `zip`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_class_proximity_table`
- `src/landscout/stages/enrich_road_proximity.py` — `_validate_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_null_safe_equal`

**Signature**

```python
def _null_safe_equal(actual: pd.Series, expected: pd.Series) -> bool:
```

**Purpose**

Implements null safe equal according to the exact implementation and guards in this file.

**Inputs**

- `actual` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `bool((both_null | equal).all())`; `False`.

**Algorithm**

1. Computes `left` from `actual.reset_index(drop=True)`.
2. Computes `right` from `expected.reset_index(drop=True)`.
3. Checks `len(left) != len(right)`. When true: Returns `False`.
4. Computes `both_null` from `left.isna() & right.isna()`.
5. Runs guarded operation: Computes `equal` from `left.eq(right).fillna(False)`. Handles `(TypeError, ValueError)`.
6. Returns `bool((both_null | equal).all())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(both_null | equal).all`, `actual.reset_index`, `bool`, `expected.reset_index`, `left.eq`, `left.eq(right).fillna`, `left.isna`, `len`, `right.isna`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_validate_selected_evidence`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_selected_evidence`

**Signature**

```python
def _validate_selected_evidence(
    table: pd.DataFrame,
    roads: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Validates and rejects malformed selected evidence according to the exact implementation and guards in this file.

**Inputs**

- `table` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `roads` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `None`.

**Algorithm**

1. Computes `matched` from `table['nearest_road_feature_id'].notna()`.
2. Computes `selected` from `table.loc[matched].reset_index(drop=True)`.
3. Checks `selected.empty`. When true: Returns `None`.
4. Computes `lookup` from `roads.set_index('road_feature_id', drop=False)`.
5. Computes `positions` from `lookup.index.get_indexer(selected['nearest_road_feature_id'])`.
6. Checks `(positions < 0).any()`. When true: Raises `RoadProximityError('Selected nearest road ID is absent from source')`.
7. Computes `expected` from `lookup.iloc[positions].reset_index(drop=True)`.
8. Checks `not selected['road_proxy_class'].reset_index(drop=True).eq(expected['road_proxy_class']).all()`. When true: Raises `RoadProximityError('Selected nearest road has the wrong proxy class')`.
9. Iterates `(source_column, output_column)` over `_MATCH_OUTPUT_MAPPING.items()`. For each value: Checks `source_column in {'distance_m', 'tie_count'}`. When true: Executes `continue` control flow. Checks `not _null_safe_equal(selected[output_column], expected[source_column])`. When true: Raises `RoadProximityError(f'Selected nearest road evidence differs for {output_column}')`.

**Validation and invariants**

- Rejects or diverts the path when `(positions < 0).any()` is true.
- Rejects or diverts the path when `not selected['road_proxy_class'].reset_index(drop=True).eq(expected['road_proxy_class']).all()` is true.
- Rejects or diverts the path when `not _null_safe_equal(selected[output_column], expected[source_column])` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(positions < 0).any`, `RoadProximityError`, `_MATCH_OUTPUT_MAPPING.items`, `_null_safe_equal`, `lookup.iloc[positions].reset_index`, `lookup.index.get_indexer`, `roads.set_index`, `selected['road_proxy_class'].reset_index`, `selected['road_proxy_class'].reset_index(drop=True).eq`, `selected['road_proxy_class'].reset_index(drop=True).eq(expected['road_proxy_class']).all`, `table.loc[matched].reset_index`, `table['nearest_road_feature_id'].notna`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_validate_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_coverage`

**Signature**

```python
def _validate_coverage(
    coverage: tuple[RoadProxyClassCoverage, ...],
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
```

**Purpose**

Validates and rejects malformed coverage according to the exact implementation and guards in this file.

**Inputs**

- `coverage` (`tuple[RoadProxyClassCoverage, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `roads` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `eligible_classes`.

**Algorithm**

1. Computes `(all_classes, eligible_classes)` from `_policy_classes(policy)`.
2. Checks `type(coverage) is not tuple or len(coverage) != len(all_classes)`. When true: Raises `RoadProximityError('Road class coverage is incomplete')`.
3. Computes `counts` from `roads['road_proxy_class'].value_counts()`.
4. Computes `total` from `0`.
5. Iterates `(position, item)` over `enumerate(coverage)`. For each value: Checks `type(item) is not RoadProxyClassCoverage`. When true: Raises `RoadProximityError('Road class coverage entry type is invalid')`. Computes `road_class` from `all_classes[position]`. Checks `item.road_proxy_class != road_class`. When true: Raises `RoadProximityError('Road class coverage order is invalid')`. Executes 5 additional source-ordered statement(s).
6. Checks `total != len(roads)`. When true: Raises `RoadProximityError('Road class coverage does not sum to source rows')`.
7. Returns `eligible_classes`.

**Validation and invariants**

- Rejects or diverts the path when `type(coverage) is not tuple or len(coverage) != len(all_classes)` is true.
- Rejects or diverts the path when `total != len(roads)` is true.
- Rejects or diverts the path when `type(item) is not RoadProxyClassCoverage` is true.
- Rejects or diverts the path when `item.road_proxy_class != road_class` is true.
- Rejects or diverts the path when `type(item.feature_count) is not int or item.feature_count < 0` is true.
- Rejects or diverts the path when `type(item.distance_eligible) is not bool` is true.
- Rejects or diverts the path when `item.distance_eligible != (road_class in eligible_classes)` is true.
- Rejects or diverts the path when `item.feature_count != int(counts.get(road_class, 0))` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityError`, `_policy_classes`, `counts.get`, `enumerate`, `int`, `len`, `roads['road_proxy_class'].value_counts`, `type`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_validate_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_parcel_preservation`

**Signature**

```python
def _validate_parcel_preservation(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Validates and rejects malformed parcel preservation according to the exact implementation and guards in this file.

**Inputs**

- `source` (`gpd.GeoDataFrame`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `output` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `len(output) != len(source)`. When true: Raises `RoadProximityError('Road proximity changed parcel count')`.
2. Checks `list(output.columns) != list(source.columns)`. When true: Raises `RoadProximityError('Road proximity changed parcel columns')`.
3. Checks `not output.dtypes.equals(source.dtypes)`. When true: Raises `RoadProximityError('Road proximity changed parcel dtypes')`.
4. Checks `type(output.index) is not type(source.index) or output.index.names != source.index.names or str(output.index.dtype) != str(source.index.dtype) or (not output.index.equals(source.index))`. When true: Raises `RoadProximityError('Road proximity changed parcel index metadata')`.
5. Checks `not _validated_crs(output.crs, 'Output parcel').equals(_validated_crs(source.crs, 'Source parcel'))`. When true: Raises `RoadProximityError('Road proximity changed parcel CRS')`.
6. Checks `not output.geometry.to_wkb().equals(source.geometry.to_wkb())`. When true: Raises `RoadProximityError('Road proximity changed parcel geometry WKB')`.
7. Computes `geometry_column` from `source.active_geometry_name`.
8. Checks `geometry_column is None or not output.drop(columns=geometry_column).equals(source.drop(columns=geometry_column))`. When true: Raises `RoadProximityError('Road proximity changed parcel facts')`.

**Validation and invariants**

- Rejects or diverts the path when `len(output) != len(source)` is true.
- Rejects or diverts the path when `list(output.columns) != list(source.columns)` is true.
- Rejects or diverts the path when `not output.dtypes.equals(source.dtypes)` is true.
- Rejects or diverts the path when `type(output.index) is not type(source.index) or output.index.names != source.index.names or str(output.index.dtype) != str(source.index.dtype) or (not output.index.equals(source.index))` is true.
- Rejects or diverts the path when `not _validated_crs(output.crs, 'Output parcel').equals(_validated_crs(source.crs, 'Source parcel'))` is true.
- Rejects or diverts the path when `not output.geometry.to_wkb().equals(source.geometry.to_wkb())` is true.
- Rejects or diverts the path when `geometry_column is None or not output.drop(columns=geometry_column).equals(source.drop(columns=geometry_column))` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityError`, `_validated_crs`, `_validated_crs(output.crs, 'Output parcel').equals`, `len`, `list`, `output.drop`, `output.drop(columns=geometry_column).equals`, `output.dtypes.equals`, `output.geometry.to_wkb`, `output.geometry.to_wkb().equals`, `output.index.equals`, `source.drop`, `source.geometry.to_wkb`, `str`, `type`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_validate_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_result`

**Signature**

```python
def _validate_result(
    source_parcels: gpd.GeoDataFrame,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
    result: ParcelRoadProximityResult,
) -> None:
```

**Purpose**

Validates and rejects malformed result according to the exact implementation and guards in this file.

**Inputs**

- `source_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `roads` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`ParcelRoadProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `type(result) is not ParcelRoadProximityResult`. When true: Raises `RoadProximityError('Road proximity result type is invalid')`.
2. Checks `not isinstance(result.parcels, gpd.GeoDataFrame)`. When true: Raises `RoadProximityError('Road proximity parcels must be a GeoDataFrame')`.
3. Checks `type(result.class_proximity) is not pd.DataFrame`. When true: Raises `RoadProximityError('Class proximity must be a plain DataFrame')`.
4. Calls `_validate_parcel_preservation(source_parcels, result.parcels)` for its validation or side effect.
5. Computes `eligible_classes` from `_validate_coverage(result.class_coverage, roads, policy)`.
6. Computes `table` from `result.class_proximity`.
7. Checks `table.columns.duplicated().any() or list(table.columns) != list(CLASS_PROXIMITY_COLUMNS)`. When true: Raises `RoadProximityError('Class proximity schema is invalid')`.
8. Checks `len(table) != len(source_parcels) * len(eligible_classes)`. When true: Raises `RoadProximityError('Class proximity row count is invalid')`.
9. Computes `expected_ids` from `[parcel_id for parcel_id in source_parcels['parcel_id'].tolist() for _ in eligible_classes]`.
10. Computes `expected_classes` from `list(eligible_classes) * len(source_parcels)`.
11. Checks `table['parcel_id'].tolist() != expected_ids`. When true: Raises `RoadProximityError('Class proximity parcel order is invalid')`.
12. Checks `table['road_proxy_class'].tolist() != expected_classes`. When true: Raises `RoadProximityError('Class proximity class order is invalid')`.
13. Checks `policy.classes.not_distance_proxy in set(table['road_proxy_class'])`. When true: Raises `RoadProximityError('NOT_DISTANCE_PROXY cannot have distance rows')`.
14. Checks `table.duplicated(['parcel_id', 'road_proxy_class']).any()`. When true: Raises `RoadProximityError('Class proximity parcel/class pairs must be unique')`.
15. Computes `coverage` from `{item.road_proxy_class: item for item in result.class_coverage}`.
16. Computes `required_match_values` from `('nearest_road_feature_id', 'nearest_source_feature_id', 'nearest_road_primary_rule', 'nearest_road_rule_trace_json', 'nearest_road_unknown_fields_json', 'nearest_road_toll_evidence', 'nearest_source_layer', 'nearest_source_department_code', 'nearest_source_edition', 'nearest_source_archive_sha256')`.
17. Iterates `road_class` over `eligible_classes`. For each value: Computes `rows` from `table.loc[table['road_proxy_class'].eq(road_class)]`. Computes `expect_matches` from `coverage[road_class].feature_count > 0`. Calls `_validate_distance_and_ties(rows, expect_matches=expect_matches)` for its validation or side effect. Executes 1 additional source-ordered statement(s).
18. Computes `expected_lineage` from `{'road_proxy_policy_id': policy.policy_id, 'road_proxy_policy_schema_version': policy.schema_version, 'road_proxy_policy_config_sha256': policy.config_sha256, 'road_proxy_heavy_vehicle_access': policy.heavy_vehicle_access, 'proximity_scope': _PROXIMITY_SCOPE}`.
19. Iterates `(column, value)` over `expected_lineage.items()`. For each value: Checks `table[column].isna().any() or not table[column].eq(value).all()`. When true: Raises `RoadProximityError(f'Class proximity lineage differs in {column}')`.
20. Calls `_validate_selected_evidence(table, roads)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `type(result) is not ParcelRoadProximityResult` is true.
- Rejects or diverts the path when `not isinstance(result.parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `type(result.class_proximity) is not pd.DataFrame` is true.
- Rejects or diverts the path when `table.columns.duplicated().any() or list(table.columns) != list(CLASS_PROXIMITY_COLUMNS)` is true.
- Rejects or diverts the path when `len(table) != len(source_parcels) * len(eligible_classes)` is true.
- Rejects or diverts the path when `table['parcel_id'].tolist() != expected_ids` is true.
- Rejects or diverts the path when `table['road_proxy_class'].tolist() != expected_classes` is true.
- Rejects or diverts the path when `policy.classes.not_distance_proxy in set(table['road_proxy_class'])` is true.
- Rejects or diverts the path when `table.duplicated(['parcel_id', 'road_proxy_class']).any()` is true.
- Rejects or diverts the path when `expect_matches` is true.
- Rejects or diverts the path when `table[column].isna().any() or not table[column].eq(value).all()` is true.
- Rejects or diverts the path when `rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna().any().any()` is true.
- Rejects or diverts the path when `rows[column].isna().any()` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityError`, `_MATCH_OUTPUT_MAPPING.values`, `_validate_coverage`, `_validate_distance_and_ties`, `_validate_parcel_preservation`, `_validate_selected_evidence`, `expected_lineage.items`, `isinstance`, `len`, `list`, `rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna`, `rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna().any`, `rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna().any().any`, `rows[column].isna`, `rows[column].isna().any`, `set`, `source_parcels['parcel_id'].tolist`, `table.columns.duplicated`, `table.columns.duplicated().any`, `table.duplicated`, `table.duplicated(['parcel_id', 'road_proxy_class']).any`, `table['parcel_id'].tolist`, `table['road_proxy_class'].eq`, `table['road_proxy_class'].tolist`, `table[column].eq`, `table[column].eq(value).all`, `table[column].isna`, `table[column].isna().any`, `type`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_enrich_parcel_road_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_enrich_parcel_road_proximity`

**Signature**

```python
def _enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> ParcelRoadProximityResult:
```

**Purpose**

Enriches parcel road proximity according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_path` (`Path | None`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelRoadProximityResult`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `source_parcels` from `_validate_parcels(parcels)`.
2. Computes `policy` from `load_ign_road_vehicle_proxy_policy() if policy_path is None else load_ign_road_vehicle_proxy_policy(policy_path)`.
3. Computes `application` from `apply_ign_road_vehicle_proxy_policy(road_source, source_config, policy_path)`.
4. Computes `roads` from `_validate_application_roads(application, policy)`.
5. Computes `output_parcels` from `source_parcels.copy(deep=True)`.
6. Computes `calculation_parcels` from `source_parcels.to_crs(_CALCULATION_CRS)`.
7. Computes `parcel_geometries` from `_calculation_geometries(calculation_parcels)`.
8. Computes `class_proximity` from `_class_proximity_table(source_parcels['parcel_id'], parcel_geometries, roads, policy)`.
9. Computes `result` from `ParcelRoadProximityResult(parcels=output_parcels, class_proximity=class_proximity, class_coverage=_coverage(roads, policy))`.
10. Calls `_validate_result(source_parcels, roads, policy, result)` for its validation or side effect.
11. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_road_vehicle_proxy_policy`, `source_parcels.copy`, `source_parcels.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `ParcelRoadProximityResult`, `_calculation_geometries`, `_class_proximity_table`, `_coverage`, `_validate_application_roads`, `_validate_parcels`, `_validate_result`, `apply_ign_road_vehicle_proxy_policy`, `load_ign_road_vehicle_proxy_policy`, `source_parcels.copy`, `source_parcels.to_crs`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `enrich_parcel_road_proximity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `enrich_parcel_road_proximity`

**Signature**

```python
def enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
```

**Purpose**

Compute exact class-specific distance within the verified source package.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_path` (`Path | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelRoadProximityResult`. Observed return expression(s): `_enrich_parcel_road_proximity(parcels, road_source, source_config, policy_path)`.

**Algorithm**

1. Runs guarded operation: Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `RoadProximityError('parcels must be a GeoDataFrame with active geometry')`. Checks `type(road_source) is not IgnBdTopoRoadData`. When true: Raises `RoadProximityError('road_source must be an IgnBdTopoRoadData')`. Checks `type(source_config) is not IgnBdTopoSourceConfig`. When true: Raises `RoadProximityError('source_config must be an IgnBdTopoSourceConfig')`. Checks `policy_path is not None and (not isinstance(policy_path, Path))`. When true: Raises `RoadProximityError('policy_path must be a pathlib.Path or None')`. Executes 1 additional source-ordered statement(s). Handles `RoadProximityError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `type(road_source) is not IgnBdTopoRoadData` is true.
- Rejects or diverts the path when `type(source_config) is not IgnBdTopoSourceConfig` is true.
- Rejects or diverts the path when `policy_path is not None and (not isinstance(policy_path, Path))` is true.

**Exceptions**

- Explicitly raises: `RoadProximityError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityError`, `_enrich_parcel_road_proximity`, `isinstance`, `type`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`
- `tests/unit/test_enrich_road_proximity.py` — `_enrich`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_failure_stops_proximity`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_roads_must_be_geodataframe`
- `tests/unit/test_enrich_road_proximity.py` — `test_application_stage_is_invoked_exactly_once`
- `tests/unit/test_enrich_road_proximity.py` — `test_malformed_policy_stops_before_application`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_application_result_type_is_rejected`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_parcel_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_policy_path_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_road_source_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py` — `test_wrong_source_config_type_has_controlled_error`

**Tests**

- `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity`
- `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe`
- `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once`
- `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_road_source_type_has_controlled_error`
- `tests/unit/test_enrich_road_proximity.py::test_wrong_source_config_type_has_controlled_error`

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `_class_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `_parcel_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `carriageway_width_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `closure_period_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `drop` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `kind` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `light_vehicle_access_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_carriageway_width_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_closure_period_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_light_vehicle_access_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_private_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_restriction_nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_primary_rule` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_proxy_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_rule_trace_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_toll_evidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_road_unknown_fields_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `nearest_source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `private_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `proximity_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `road_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `road_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_class` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_heavy_vehicle_access` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_config_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_primary_rule` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_rule_trace_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_toll_evidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_unknown_fields_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `tie_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `road` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
