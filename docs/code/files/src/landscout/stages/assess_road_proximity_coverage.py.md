# `src/landscout/stages/assess_road_proximity_coverage.py`

## File identity

- Repository path: `src/landscout/stages/assess_road_proximity_coverage.py`
- File type: Python source
- Primary responsibility: Diagnoses road proxy proximity against the verified IGN department coverage boundary.
- Layer / domain: `stage` / `road`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `ff3fda58bfc1086082d8222ed099f1fae529ec45b05476c90d3177c42c114d2d`

## 1. Purpose

Diagnoses road proxy proximity against the verified IGN department coverage boundary.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `road` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import unicodedata` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.
- `from shapely import ( # type: ignore[import-untyped] boundary, covers, distance, force_2d, intersects, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoCoverageLayerSummary, IgnBdTopoDepartmentCoverage, IgnBdTopoRoadData, IgnBdTopoSourceConfig, _discover_department_coverage_layer, load_ign_bdtopo_department_coverage, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_road_proximity import ( CLASS_PROXIMITY_COLUMNS, ParcelRoadProximityResult, RoadProxyClassCoverage, enrich_parcel_road_proximity, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.road_vehicle_proxy_policy import ( IgnRoadVehicleProxyPolicy, load_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `_CALCULATION_CRS` | `"EPSG:2154"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_PROXIMITY_SCOPE` | `"WITHIN_VERIFIED_SOURCE_PACKAGE"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_COVERAGE_SPATIAL_ROLE` | `"SOURCE_COVERAGE_BOUNDARY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SOURCE_SPATIAL_ROLE` | `"PROXY_GEOMETRY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_POSITIONS` | `frozenset( {"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_STATUSES` | `frozenset( { "NO_MATCH", "NOT_BOUNDARY_LIMITED", "BOUNDARY_LIMITED", "OUTSIDE_OR_CROSSING_COVERAGE", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_PARCEL_GEOMETRY_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_COVERAGE_GEOMETRY_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SHA256_PATTERN` | `re.compile(r"^[0-9a-f]{64}$")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_IGN_PROVIDER_IDENTITIES` | `frozenset( { "ign", "institutnationaldelinformationgeographiqueetforestiereign", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_COVERAGE_LINEAGE_COLUMNS` | `( "road_source_coverage_provider", "road_source_coverage_product", "road_source_coverage_department_code", "road_source_coverage_edition", "road_source_coverage_product_version", "road_source_coverage_archive_sha256", "road_source_coverage_layer", "road_source_coverage_spatial_role", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_DIAGNOSTIC_COLUMNS` | `( "road_source_boundary_distance_m", "road_source_coverage_position", "road_proximity_coverage_status", *_COVERAGE_LINEAGE_COLUMNS, )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_COVERAGE_FRAME_LINEAGE` | `( "source_provider", "source_product", "source_department_code", "source_edition", "source_product_version", "source_archive_sha256", "source_layer", "spatial_role", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SELECTED_ROAD_COLUMNS` | `( "nearest_road_feature_id", "nearest_source_feature_id", "nearest_road_tie_count", "nearest_road_primary_rule", "nearest_road_rule_trace_json", "nearest_road_unknown_fields_json", "nearest_road_toll_evidence", "nearest_nature_raw", "nearest_importance_raw", "nearest_asset_status_raw", "nearest_private_raw", "nearest_light_vehicle_access_raw", "nearest_carriageway_width_raw", "nearest_closure_period_raw", "nearest_restriction_nature_raw", "nearest_source_layer", "nearest_source_department_code", "nearest_source_edition", "nearest_source_archive_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `RoadProximityCoverageError`

**Purpose:** Raised when road source-boundary diagnostics cannot be proven safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `RoadProximityCoverageAssessmentResult`

**Purpose:** Unchanged road proximity plus its source-package boundary diagnosis.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `class_proximity` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/assess_road_proximity_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `class_coverage` | `tuple[RoadProxyClassCoverage, ...]` | `required` | `tuple[RoadProxyClassCoverage, ...]` state used by `src/landscout/stages/assess_road_proximity_coverage.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_coverage` | `IgnBdTopoDepartmentCoverage` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_validated_crs`

**Signature**

```python
def _validated_crs(value: object, expected_epsg: int, label: str) -> CRS:
```

**Purpose**

Validates and returns canonical crs according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected_epsg` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `actual`.

**Algorithm**

1. Checks `value is None`. When true: Raises `RoadProximityCoverageError(f'{label} CRS is required')`.
2. Runs guarded operation: Computes `actual` from `CRS.from_user_input(value)`. Handles `Exception`.
3. Computes `expected` from `CRS.from_epsg(expected_epsg)`.
4. Checks `not actual.equals(expected)`. When true: Raises `RoadProximityCoverageError(f'{label} must use EPSG:{expected_epsg}')`.
5. Returns `actual`.

**Validation and invariants**

- Rejects or diverts the path when `value is None` is true.
- Rejects or diverts the path when `not actual.equals(expected)` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `CRS.from_user_input`, `RoadProximityCoverageError`, `actual.equals`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_require_same_parcels`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_coverage_summary`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_parcel_frame`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_source_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_normalized_identity`

**Signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

**Purpose**

Implements normalized identity according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `''.join((character for character in decomposed.casefold() if character.isalnum()))`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `RoadProximityCoverageError(f'{label} must be a non-empty exact string')`.
2. Computes `decomposed` from `unicodedata.normalize('NFKD', value)`.
3. Returns `''.join((character for character in decomposed.casefold() if character.isalnum()))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `''.join`, `RoadProximityCoverageError`, `character.isalnum`, `decomposed.casefold`, `isinstance`, `unicodedata.normalize`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_source_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_exact_string`

**Signature**

```python
def _exact_string(value: object, label: str) -> str:
```

**Purpose**

Implements exact string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `RoadProximityCoverageError(f'{label} must be a non-empty exact string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `isinstance`, `value.strip`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_null_safe_scalar_equal`

**Signature**

```python
def _null_safe_scalar_equal(actual: object, expected: object) -> bool:
```

**Purpose**

Implements null safe scalar equal according to the exact implementation and guards in this file.

**Inputs**

- `actual` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `bool(pd.isna(actual))`; `bool(actual == expected)`; `False`.

**Algorithm**

1. Checks `expected is None`. When true: Returns `bool(pd.isna(actual))`.
2. Runs guarded operation: Returns `bool(actual == expected)`. Handles `(TypeError, ValueError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_source_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_exact_ids`

**Signature**

```python
def _exact_ids(values: pd.Series, label: str) -> None:
```

**Purpose**

Implements exact ids according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `values.isna().any()`. When true: Raises `RoadProximityCoverageError(f'{label} values must not be null')`.
2. Computes `items` from `values.tolist()`.
3. Checks `any((not isinstance(item, str) for item in items))`. When true: Raises `RoadProximityCoverageError(f'{label} values must be exact strings')`.
4. Checks `any((not item or item != item.strip() for item in items))`. When true: Raises `RoadProximityCoverageError(f'{label} values must be non-empty without edge whitespace')`.
5. Checks `values.duplicated().any()`. When true: Raises `RoadProximityCoverageError(f'{label} values must be unique')`.

**Validation and invariants**

- Rejects or diverts the path when `values.isna().any()` is true.
- Rejects or diverts the path when `any((not isinstance(item, str) for item in items))` is true.
- Rejects or diverts the path when `any((not item or item != item.strip() for item in items))` is true.
- Rejects or diverts the path when `values.duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `any`, `isinstance`, `item.strip`, `values.duplicated`, `values.duplicated().any`, `values.isna`, `values.isna().any`, `values.tolist`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_parcel_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_parcel_frame`

**Signature**

```python
def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed parcel frame according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`object`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Checks `not isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `RoadProximityCoverageError(f'{label} must be a GeoDataFrame')`.
2. Checks `frame.columns.duplicated().any()`. When true: Raises `RoadProximityCoverageError(f'{label} columns must be unique')`.
3. Computes `missing` from `{'parcel_id', 'geometry'} - set(frame.columns)`.
4. Checks `missing`. When true: Raises `RoadProximityCoverageError(f'{label} is missing: ' + ', '.join(sorted(missing)))`.
5. Checks `frame.active_geometry_name != 'geometry'`. When true: Raises `RoadProximityCoverageError(f'{label} geometry must be active')`.
6. Calls `_validated_crs(frame.crs, 4326, label)` for its validation or side effect.
7. Calls `_exact_ids(frame['parcel_id'], f'{label} parcel_id')` for its validation or side effect.
8. Computes `geometry` from `frame.geometry`.
9. Checks `geometry.isna().any()`. When true: Raises `RoadProximityCoverageError(f'{label} geometry must not be null')`.
10. Checks `geometry.is_empty.any()`. When true: Raises `RoadProximityCoverageError(f'{label} geometry must not be empty')`.
11. Checks `not geometry.is_valid.all()`. When true: Raises `RoadProximityCoverageError(f'{label} geometry must be valid')`.
12. Checks `not set(geometry.geom_type.dropna()) <= _PARCEL_GEOMETRY_TYPES`. When true: Raises `RoadProximityCoverageError(f'{label} geometry must be Polygon or MultiPolygon')`.
13. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `frame.columns.duplicated().any()` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `frame.active_geometry_name != 'geometry'` is true.
- Rejects or diverts the path when `geometry.isna().any()` is true.
- Rejects or diverts the path when `geometry.is_empty.any()` is true.
- Rejects or diverts the path when `not geometry.is_valid.all()` is true.
- Rejects or diverts the path when `not set(geometry.geom_type.dropna()) <= _PARCEL_GEOMETRY_TYPES` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `RoadProximityCoverageError`, `_exact_ids`, `_validated_crs`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `geometry.geom_type.dropna`, `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`, `isinstance`, `set`, `sorted`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_assessment_result`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_upstream_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_same_index`

**Signature**

```python
def _same_index(left: pd.Index, right: pd.Index) -> bool:
```

**Purpose**

Returns whether `index` agrees under the implementation's exact comparison contract.

**Inputs**

- `left` (`pd.Index`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `right` (`pd.Index`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `bool(type(left) is type(right) and left.names == right.names and (str(left.dtype) == str(right.dtype)) and left.equals(right))`.

**Algorithm**

1. Returns `bool(type(left) is type(right) and left.names == right.names and (str(left.dtype) == str(right.dtype)) and left.equals(right))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `left.equals`, `str`, `type`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_require_same_parcels`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_same_parcels`

**Signature**

```python
def _require_same_parcels(
    expected: gpd.GeoDataFrame,
    actual: gpd.GeoDataFrame,
    label: str,
) -> None:
```

**Purpose**

Implements require same parcels according to the exact implementation and guards in this file.

**Inputs**

- `expected` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `actual` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `list(actual.columns) != list(expected.columns)`. When true: Raises `RoadProximityCoverageError(f'{label} parcel columns changed')`.
2. Checks `not actual.dtypes.equals(expected.dtypes)`. When true: Raises `RoadProximityCoverageError(f'{label} parcel dtypes changed')`.
3. Checks `not _same_index(actual.index, expected.index)`. When true: Raises `RoadProximityCoverageError(f'{label} parcel index changed')`.
4. Checks `not _validated_crs(actual.crs, 4326, label).equals(_validated_crs(expected.crs, 4326, label))`. When true: Raises `RoadProximityCoverageError(f'{label} parcel CRS changed')`.
5. Checks `not actual.geometry.to_wkb().equals(expected.geometry.to_wkb())`. When true: Raises `RoadProximityCoverageError(f'{label} parcel geometry changed')`.
6. Checks `not actual.drop(columns='geometry').equals(expected.drop(columns='geometry'))`. When true: Raises `RoadProximityCoverageError(f'{label} parcel facts changed')`.

**Validation and invariants**

- Rejects or diverts the path when `list(actual.columns) != list(expected.columns)` is true.
- Rejects or diverts the path when `not actual.dtypes.equals(expected.dtypes)` is true.
- Rejects or diverts the path when `not _same_index(actual.index, expected.index)` is true.
- Rejects or diverts the path when `not _validated_crs(actual.crs, 4326, label).equals(_validated_crs(expected.crs, 4326, label))` is true.
- Rejects or diverts the path when `not actual.geometry.to_wkb().equals(expected.geometry.to_wkb())` is true.
- Rejects or diverts the path when `not actual.drop(columns='geometry').equals(expected.drop(columns='geometry'))` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `_same_index`, `_validated_crs`, `_validated_crs(actual.crs, 4326, label).equals`, `actual.drop`, `actual.drop(columns='geometry').equals`, `actual.dtypes.equals`, `actual.geometry.to_wkb`, `actual.geometry.to_wkb().equals`, `expected.drop`, `expected.geometry.to_wkb`, `list`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_assessment_result`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_upstream_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_finite_nonnegative`

**Signature**

```python
def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
```

**Purpose**

Implements finite nonnegative according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `np.ndarray`. Observed return expression(s): `np.asarray(converted, dtype='float64')`.

**Algorithm**

1. Defines `converted` with annotation `list[float]` from `[]`.
2. Iterates `value` over `values.tolist()`. For each value: Checks `not isinstance(value, Real) or isinstance(value, (bool, np.bool_))`. When true: Raises `RoadProximityCoverageError(f'{label} must be numeric')`. Computes `numeric` from `float(value)`. Checks `not isfinite(numeric) or numeric < 0`. When true: Raises `RoadProximityCoverageError(f'{label} must be finite and non-negative')`. Executes 1 additional source-ordered statement(s).
3. Returns `np.asarray(converted, dtype='float64')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, Real) or isinstance(value, (bool, np.bool_))` is true.
- Rejects or diverts the path when `not isfinite(numeric) or numeric < 0` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `converted.append`, `float`, `isfinite`, `isinstance`, `np.asarray`, `values.tolist`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_assessment_result`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_match_rows`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_class_coverage`

**Signature**

```python
def _validate_class_coverage(
    coverage: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
```

**Purpose**

Validates and rejects malformed class coverage according to the exact implementation and guards in this file.

**Inputs**

- `coverage` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `eligible`.

**Algorithm**

1. Computes `classes` from `policy.classes.values`.
2. Computes `eligible` from `tuple((road_class for road_class in classes if road_class != policy.classes.not_distance_proxy))`.
3. Checks `type(coverage) is not tuple or len(coverage) != len(classes)`. When true: Raises `RoadProximityCoverageError('Road class coverage is invalid')`.
4. Iterates `(position, item)` over `enumerate(coverage)`. For each value: Checks `type(item) is not RoadProxyClassCoverage`. When true: Raises `RoadProximityCoverageError('Road class coverage type is invalid')`. Checks `item.road_proxy_class != classes[position]`. When true: Raises `RoadProximityCoverageError('Road class coverage order is invalid')`. Checks `type(item.feature_count) is not int or item.feature_count < 0`. When true: Raises `RoadProximityCoverageError('Road class coverage feature_count is invalid')`. Executes 1 additional source-ordered statement(s).
5. Returns `eligible`.

**Validation and invariants**

- Rejects or diverts the path when `type(coverage) is not tuple or len(coverage) != len(classes)` is true.
- Rejects or diverts the path when `type(item) is not RoadProxyClassCoverage` is true.
- Rejects or diverts the path when `item.road_proxy_class != classes[position]` is true.
- Rejects or diverts the path when `type(item.feature_count) is not int or item.feature_count < 0` is true.
- Rejects or diverts the path when `type(item.distance_eligible) is not bool or item.distance_eligible != (item.road_proxy_class in eligible)` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `enumerate`, `len`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_upstream_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_match_rows`

**Signature**

```python
def _validate_match_rows(
    table: pd.DataFrame,
    coverage: tuple[RoadProxyClassCoverage, ...],
) -> None:
```

**Purpose**

Validates and rejects malformed match rows according to the exact implementation and guards in this file.

**Inputs**

- `table` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coverage` (`tuple[RoadProxyClassCoverage, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `by_class` from `{item.road_proxy_class: item for item in coverage}`.
2. Iterates `(road_class, item)` over `by_class.items()`. For each value: Checks `not item.distance_eligible`. When true: Executes `continue` control flow. Computes `rows` from `table.loc[table['road_proxy_class'].eq(road_class)]`. Computes `matched` from `rows['nearest_road_proxy_distance_m'].notna()`. Executes 6 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `item.feature_count == 0` is true.
- Rejects or diverts the path when `not matched.all()` is true.
- Rejects or diverts the path when `rows.loc[:, list(required)].isna().any().any()` is true.
- Rejects or diverts the path when `matched.any() or rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any().any()` is true.
- Rejects or diverts the path when `not isinstance(value, Integral) or isinstance(value, (bool, np.bool_)) or int(value) < 1` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `_finite_nonnegative`, `by_class.items`, `int`, `isinstance`, `list`, `matched.all`, `matched.any`, `rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna`, `rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any`, `rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any().any`, `rows.loc[:, list(required)].isna`, `rows.loc[:, list(required)].isna().any`, `rows.loc[:, list(required)].isna().any().any`, `rows['nearest_road_proxy_distance_m'].notna`, `rows['nearest_road_tie_count'].tolist`, `table['road_proxy_class'].eq`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_upstream_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_upstream_result`

**Signature**

```python
def _validate_upstream_result(
    input_parcels: gpd.GeoDataFrame,
    result: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> ParcelRoadProximityResult:
```

**Purpose**

Validates and rejects malformed upstream result according to the exact implementation and guards in this file.

**Inputs**

- `input_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelRoadProximityResult`. Observed return expression(s): `result`.

**Algorithm**

1. Checks `type(result) is not ParcelRoadProximityResult`. When true: Raises `RoadProximityCoverageError('Road proximity result type is invalid')`.
2. Computes `parcels` from `_validate_parcel_frame(result.parcels, 'Road proximity parcels')`.
3. Calls `_require_same_parcels(input_parcels, parcels, 'Road proximity')` for its validation or side effect.
4. Computes `eligible` from `_validate_class_coverage(result.class_coverage, policy)`.
5. Computes `table` from `result.class_proximity`.
6. Checks `type(table) is not pd.DataFrame`. When true: Raises `RoadProximityCoverageError('Class proximity must be a plain DataFrame')`.
7. Checks `table.columns.duplicated().any() or tuple(table.columns) != CLASS_PROXIMITY_COLUMNS`. When true: Raises `RoadProximityCoverageError('Class proximity schema is invalid')`.
8. Checks `not isinstance(table.index, pd.RangeIndex) or (table.index.start != 0 or table.index.step != 1 or table.index.name is not None)`. When true: Raises `RoadProximityCoverageError('Class proximity index is invalid')`.
9. Checks `len(table) != len(parcels) * len(eligible)`. When true: Raises `RoadProximityCoverageError('Class proximity row count is invalid')`.
10. Computes `expected_ids` from `[parcel_id for parcel_id in parcels['parcel_id'].tolist() for _ in eligible]`.
11. Computes `expected_classes` from `list(eligible) * len(parcels)`.
12. Checks `table['parcel_id'].tolist() != expected_ids`. When true: Raises `RoadProximityCoverageError('Class proximity parcel order is invalid')`.
13. Checks `table['road_proxy_class'].tolist() != expected_classes`. When true: Raises `RoadProximityCoverageError('Class proximity class order is invalid')`.
14. Checks `table.duplicated(['parcel_id', 'road_proxy_class']).any()`. When true: Raises `RoadProximityCoverageError('Class proximity pairs are duplicated')`.
15. Computes `expected_lineage` from `{'road_proxy_policy_id': policy.policy_id, 'road_proxy_policy_schema_version': policy.schema_version, 'road_proxy_policy_config_sha256': policy.config_sha256, 'road_proxy_heavy_vehicle_access': policy.heavy_vehicle_access, 'proximity_scope': _PROXIMITY_SCOPE}`.
16. Iterates `(column, expected)` over `expected_lineage.items()`. For each value: Checks `table[column].isna().any() or not table[column].eq(expected).all()`. When true: Raises `RoadProximityCoverageError(f'Class proximity policy lineage is invalid: {column}')`.
17. Calls `_validate_match_rows(table, result.class_coverage)` for its validation or side effect.
18. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `type(result) is not ParcelRoadProximityResult` is true.
- Rejects or diverts the path when `type(table) is not pd.DataFrame` is true.
- Rejects or diverts the path when `table.columns.duplicated().any() or tuple(table.columns) != CLASS_PROXIMITY_COLUMNS` is true.
- Rejects or diverts the path when `not isinstance(table.index, pd.RangeIndex) or (table.index.start != 0 or table.index.step != 1 or table.index.name is not None)` is true.
- Rejects or diverts the path when `len(table) != len(parcels) * len(eligible)` is true.
- Rejects or diverts the path when `table['parcel_id'].tolist() != expected_ids` is true.
- Rejects or diverts the path when `table['road_proxy_class'].tolist() != expected_classes` is true.
- Rejects or diverts the path when `table.duplicated(['parcel_id', 'road_proxy_class']).any()` is true.
- Rejects or diverts the path when `table[column].isna().any() or not table[column].eq(expected).all()` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `_require_same_parcels`, `_validate_class_coverage`, `_validate_match_rows`, `_validate_parcel_frame`, `expected_lineage.items`, `isinstance`, `len`, `list`, `parcels['parcel_id'].tolist`, `table.columns.duplicated`, `table.columns.duplicated().any`, `table.duplicated`, `table.duplicated(['parcel_id', 'road_proxy_class']).any`, `table['parcel_id'].tolist`, `table['road_proxy_class'].tolist`, `table[column].eq`, `table[column].eq(expected).all`, `table[column].isna`, `table[column].isna().any`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_coverage_summary`

**Signature**

```python
def _validate_coverage_summary(
    coverage: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
    config: IgnBdTopoSourceConfig,
) -> None:
```

**Purpose**

Validates and rejects malformed coverage summary according to the exact implementation and guards in this file.

**Inputs**

- `coverage` (`IgnBdTopoDepartmentCoverage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `summary` from `coverage.summary`.
2. Checks `type(summary) is not IgnBdTopoCoverageLayerSummary`. When true: Raises `RoadProximityCoverageError('Coverage summary type is invalid')`.
3. Checks `summary.source_layer_name != coverage.source_layer`. When true: Raises `RoadProximityCoverageError('Coverage summary layer is invalid')`.
4. Calls `_validated_crs(summary.crs, 2154, 'Coverage summary')` for its validation or side effect.
5. Checks `type(summary.selected_feature_count) is not int or summary.selected_feature_count != len(frame)`. When true: Raises `RoadProximityCoverageError('Coverage selected feature count is invalid')`.
6. Checks `type(summary.source_feature_count) is not int or summary.source_feature_count < summary.selected_feature_count`. When true: Raises `RoadProximityCoverageError('Coverage source feature count is invalid')`.
7. Checks `type(summary.columns) is not tuple or not summary.columns or len(set(summary.columns)) != len(summary.columns) or any((not isinstance(column, str) or not column or column != column.strip() for column in summary.columns))`. When true: Raises `RoadProximityCoverageError('Coverage summary columns are invalid')`.
8. Checks `tuple(frame.columns) != (*summary.columns, *_COVERAGE_FRAME_LINEAGE)`. When true: Raises `RoadProximityCoverageError('Coverage frame schema is invalid')`.
9. Computes `expected_dtypes` from `tuple(((column, str(frame[column].dtype)) for column in summary.columns))`.
10. Checks `type(summary.dtypes) is not tuple or summary.dtypes != expected_dtypes`. When true: Raises `RoadProximityCoverageError('Coverage summary dtypes are invalid')`.
11. Computes `expected_field` from `config.coverage.department_layer.department_code_field`.
12. Checks `summary.department_code_field != expected_field`. When true: Raises `RoadProximityCoverageError('Coverage configured department field is invalid')`.
13. Checks `summary.selected_department_code != coverage.source_department_code`. When true: Raises `RoadProximityCoverageError('Coverage selected department is invalid')`.
14. Checks `not frame[expected_field].eq(coverage.source_department_code).all()`. When true: Raises `RoadProximityCoverageError('Coverage department identity is invalid')`.
15. Checks `summary.spatial_role != _COVERAGE_SPATIAL_ROLE`. When true: Raises `RoadProximityCoverageError('Coverage summary spatial role is invalid')`.

**Validation and invariants**

- Rejects or diverts the path when `type(summary) is not IgnBdTopoCoverageLayerSummary` is true.
- Rejects or diverts the path when `summary.source_layer_name != coverage.source_layer` is true.
- Rejects or diverts the path when `type(summary.selected_feature_count) is not int or summary.selected_feature_count != len(frame)` is true.
- Rejects or diverts the path when `type(summary.source_feature_count) is not int or summary.source_feature_count < summary.selected_feature_count` is true.
- Rejects or diverts the path when `type(summary.columns) is not tuple or not summary.columns or len(set(summary.columns)) != len(summary.columns) or any((not isinstance(column, str) or not column or column != column.strip() for column in summary.columns))` is true.
- Rejects or diverts the path when `tuple(frame.columns) != (*summary.columns, *_COVERAGE_FRAME_LINEAGE)` is true.
- Rejects or diverts the path when `type(summary.dtypes) is not tuple or summary.dtypes != expected_dtypes` is true.
- Rejects or diverts the path when `summary.department_code_field != expected_field` is true.
- Rejects or diverts the path when `summary.selected_department_code != coverage.source_department_code` is true.
- Rejects or diverts the path when `not frame[expected_field].eq(coverage.source_department_code).all()` is true.
- Rejects or diverts the path when `summary.spatial_role != _COVERAGE_SPATIAL_ROLE` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `_validated_crs`, `any`, `column.strip`, `frame[expected_field].eq`, `frame[expected_field].eq(coverage.source_department_code).all`, `isinstance`, `len`, `set`, `str`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_source_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_source_coverage`

**Signature**

```python
def _validate_source_coverage(
    source: object,
    road_source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> tuple[IgnBdTopoDepartmentCoverage, gpd.GeoDataFrame]:
```

**Purpose**

Validates and rejects malformed source coverage according to the exact implementation and guards in this file.

**Inputs**

- `source` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[IgnBdTopoDepartmentCoverage, gpd.GeoDataFrame]`. Observed return expression(s): `(source, frame)`.

**Algorithm**

1. Checks `type(source) is not IgnBdTopoDepartmentCoverage`. When true: Raises `RoadProximityCoverageError('Coverage source type is invalid')`.
2. Checks `source.extraction is not road_source.extraction`. When true: Raises `RoadProximityCoverageError('Coverage must retain the exact road extraction identity')`.
3. Computes `archive` from `road_source.extraction.archive`.
4. Checks `road_source.extraction.spatial_role != _SOURCE_SPATIAL_ROLE or archive.spatial_role != _SOURCE_SPATIAL_ROLE`. When true: Raises `RoadProximityCoverageError('Road package spatial role is invalid')`.
5. Calls `_validated_crs(archive.projection, 2154, 'Road package')` for its validation or side effect.
6. Computes `provider_identity` from `_normalized_identity(archive.provider, 'Road provider')`.
7. Computes `product_identity` from `_normalized_identity(archive.product, 'Road product')`.
8. Checks `provider_identity not in _IGN_PROVIDER_IDENTITIES`. When true: Raises `RoadProximityCoverageError('Road package provider is not IGN')`.
9. Checks `product_identity != 'bdtopo'`. When true: Raises `RoadProximityCoverageError('Road package product is not BD TOPO')`.
10. Checks `provider_identity != _normalized_identity(config.provider, 'Config provider')`. When true: Raises `RoadProximityCoverageError('Road package provider differs from config')`.
11. Checks `product_identity != _normalized_identity(config.product, 'Config product')`. When true: Raises `RoadProximityCoverageError('Road package product differs from config')`.
12. Checks `archive.department_code != config.department_code`. When true: Raises `RoadProximityCoverageError('Road package department differs from config')`.
13. Checks `_SHA256_PATTERN.fullmatch(archive.sha256) is None`. When true: Raises `RoadProximityCoverageError('Road package archive SHA256 is invalid')`.
14. Computes `expected_layer` from `_discover_department_coverage_layer(road_source.extraction.all_layer_names, config)`.
15. Checks `source.source_layer != expected_layer`. When true: Raises `RoadProximityCoverageError('Coverage does not use the configured physical layer')`.
16. Computes `expected_scalars` from `{'source_provider': archive.provider, 'source_product': archive.product, 'source_department_code': archive.department_code, 'source_edition': archive.edition, 'source_product_version': archive.product_version, 'source_archive_sha256': archive.sha256, 'source_layer': expected_layer, 'spatial_role': _COVERAGE_SPATIAL_RO…`.
17. Iterates `(name, expected)` over `expected_scalars.items()`. For each value: Checks `not _null_safe_scalar_equal(getattr(source, name), expected)`. When true: Raises `RoadProximityCoverageError(f'Coverage package lineage is invalid: {name}')`.
18. Checks `_normalized_identity(source.source_provider, 'Coverage provider') not in _IGN_PROVIDER_IDENTITIES`. When true: Raises `RoadProximityCoverageError('Coverage provider is not IGN')`.
19. Checks `_normalized_identity(source.source_product, 'Coverage product') != 'bdtopo'`. When true: Raises `RoadProximityCoverageError('Coverage product is not BD TOPO')`.
20. Checks `_SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None`. When true: Raises `RoadProximityCoverageError('Coverage archive SHA256 is invalid')`.
21. Computes `frame` from `source.coverage`.
22. Checks `not isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `RoadProximityCoverageError('Coverage must be a GeoDataFrame')`.
23. Checks `frame.columns.duplicated().any()`. When true: Raises `RoadProximityCoverageError('Coverage columns must be unique')`.
24. Checks `'geometry' not in frame.columns or frame.active_geometry_name != 'geometry'`. When true: Raises `RoadProximityCoverageError('Coverage geometry must exist and be active')`.
25. Calls `_validated_crs(frame.crs, 2154, 'Coverage')` for its validation or side effect.
26. Checks `len(frame) != 1`. When true: Raises `RoadProximityCoverageError('Coverage must contain exactly one selected feature')`.
27. Computes `geometry` from `frame.geometry`.
28. Checks `geometry.isna().any()`. When true: Raises `RoadProximityCoverageError('Coverage geometry must not be null')`.
29. Checks `geometry.is_empty.any()`. When true: Raises `RoadProximityCoverageError('Coverage geometry must not be empty')`.
30. Checks `not geometry.is_valid.all()`. When true: Raises `RoadProximityCoverageError('Coverage geometry must be valid')`.
31. Checks `not set(geometry.geom_type.dropna()) <= _COVERAGE_GEOMETRY_TYPES`. When true: Raises `RoadProximityCoverageError('Coverage geometry must be Polygon or MultiPolygon')`.
32. Calls `_validate_coverage_summary(source, frame, config)` for its validation or side effect.
33. Iterates `(column, expected)` over `expected_scalars.items()`. For each value: Computes `actual` from `frame.iloc[0][column]`. Checks `not _null_safe_scalar_equal(actual, expected)`. When true: Raises `RoadProximityCoverageError(f'Coverage row lineage is invalid: {column}')`.
34. Returns `(source, frame)`.

**Validation and invariants**

- Rejects or diverts the path when `type(source) is not IgnBdTopoDepartmentCoverage` is true.
- Rejects or diverts the path when `source.extraction is not road_source.extraction` is true.
- Rejects or diverts the path when `road_source.extraction.spatial_role != _SOURCE_SPATIAL_ROLE or archive.spatial_role != _SOURCE_SPATIAL_ROLE` is true.
- Rejects or diverts the path when `provider_identity not in _IGN_PROVIDER_IDENTITIES` is true.
- Rejects or diverts the path when `product_identity != 'bdtopo'` is true.
- Rejects or diverts the path when `provider_identity != _normalized_identity(config.provider, 'Config provider')` is true.
- Rejects or diverts the path when `product_identity != _normalized_identity(config.product, 'Config product')` is true.
- Rejects or diverts the path when `archive.department_code != config.department_code` is true.
- Rejects or diverts the path when `_SHA256_PATTERN.fullmatch(archive.sha256) is None` is true.
- Rejects or diverts the path when `source.source_layer != expected_layer` is true.
- Rejects or diverts the path when `_normalized_identity(source.source_provider, 'Coverage provider') not in _IGN_PROVIDER_IDENTITIES` is true.
- Rejects or diverts the path when `_normalized_identity(source.source_product, 'Coverage product') != 'bdtopo'` is true.
- Rejects or diverts the path when `_SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None` is true.
- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `frame.columns.duplicated().any()` is true.
- Rejects or diverts the path when `'geometry' not in frame.columns or frame.active_geometry_name != 'geometry'` is true.
- Rejects or diverts the path when `len(frame) != 1` is true.
- Rejects or diverts the path when `geometry.isna().any()` is true.
- Rejects or diverts the path when `geometry.is_empty.any()` is true.
- Rejects or diverts the path when `not geometry.is_valid.all()` is true.
- Rejects or diverts the path when `not set(geometry.geom_type.dropna()) <= _COVERAGE_GEOMETRY_TYPES` is true.
- Rejects or diverts the path when `not _null_safe_scalar_equal(getattr(source, name), expected)` is true.
- Rejects or diverts the path when `not _null_safe_scalar_equal(actual, expected)` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `_SHA256_PATTERN.fullmatch`, `_discover_department_coverage_layer`, `_normalized_identity`, `_null_safe_scalar_equal`, `_validate_coverage_summary`, `_validated_crs`, `expected_scalars.items`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `geometry.geom_type.dropna`, `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`, `getattr`, `isinstance`, `len`, `set`, `type`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_coverage_lineage`

**Signature**

```python
def _coverage_lineage(
    coverage: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
```

**Purpose**

Implements coverage lineage according to the exact implementation and guards in this file.

**Inputs**

- `coverage` (`IgnBdTopoDepartmentCoverage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'road_source_coverage_provider': coverage.source_provider, 'road_source_coverage_product': coverage.source_product, 'road_source_coverage_department_code': coverage.source_department_code, 'road_source_coverage_edition': coverage.source_edition, 'road_source_coverage_product_version': coverage.source_product_version, 'road_source_coverage_archive_sha256': coverage.source_archive_sha256, 'road_so…`.

**Algorithm**

1. Returns `{'road_source_coverage_provider': coverage.source_provider, 'road_source_coverage_product': coverage.source_product, 'road_source_coverage_department_code': coverage.source_department_code, 'road_source_coverage_edition': coverage.source_edition, 'road_source_coverage_product_version': coverage.source_product_version, 'road_source_coverage_archive_sha256': …`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_expected_diagnostics`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_parcel_coverage_diagnostics`

**Signature**

```python
def _parcel_coverage_diagnostics(
    parcels: gpd.GeoDataFrame,
    coverage_frame: gpd.GeoDataFrame,
) -> tuple[np.ndarray, np.ndarray]:
```

**Purpose**

Implements parcel coverage diagnostics according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coverage_frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[np.ndarray, np.ndarray]`. Observed return expression(s): `(boundary_distances, positions)`.

**Algorithm**

1. Computes `calculation` from `parcels.to_crs(_CALCULATION_CRS)`.
2. Computes `parcel_geometries` from `np.asarray(force_2d(np.asarray(calculation.geometry.array, dtype=object)), dtype=object)`.
3. Computes `coverage_geometry` from `force_2d(coverage_frame.geometry.iloc[0])`.
4. Computes `coverage_boundary` from `boundary(coverage_geometry)`.
5. Computes `covered` from `np.asarray(covers(coverage_geometry, parcel_geometries), dtype='bool')`.
6. Computes `boundary_contact` from `np.asarray(intersects(parcel_geometries, coverage_boundary), dtype='bool')`.
7. Computes `fully_covered` from `covered & ~boundary_contact`.
8. Computes `measured` from `np.asarray(distance(parcel_geometries, coverage_boundary), dtype='float64')`.
9. Checks `not np.isfinite(measured).all() or (measured < 0).any()`. When true: Raises `RoadProximityCoverageError('Calculated boundary distances must be finite and non-negative')`.
10. Computes `boundary_distances` from `np.where(fully_covered, measured, 0.0)`.
11. Computes `positions` from `np.where(fully_covered, 'FULLY_COVERED', 'OUTSIDE_OR_CROSSING_COVERAGE')`.
12. Returns `(boundary_distances, positions)`.

**Validation and invariants**

- Rejects or diverts the path when `not np.isfinite(measured).all() or (measured < 0).any()` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(measured < 0).any`, `RoadProximityCoverageError`, `boundary`, `covers`, `distance`, `force_2d`, `intersects`, `np.asarray`, `np.isfinite`, `np.isfinite(measured).all`, `np.where`, `parcels.to_crs`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_coverage_statuses`

**Signature**

```python
def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
) -> np.ndarray:
```

**Purpose**

Implements coverage statuses according to the exact implementation and guards in this file.

**Inputs**

- `distances` (`pd.Series`; required) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `boundary_distances` (`np.ndarray`; required) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `positions` (`np.ndarray`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `np.ndarray`. Observed return expression(s): `statuses`.

**Algorithm**

1. Computes `numeric` from `distances.to_numpy(dtype='float64', na_value=np.nan)`.
2. Computes `matched` from `~np.isnan(numeric)`.
3. Computes `fully_covered` from `positions == 'FULLY_COVERED'`.
4. Computes `statuses` from `np.full(len(distances), 'NO_MATCH', dtype=object)`.
5. Computes `outside` from `matched & ~fully_covered`.
6. Computes `statuses[outside]` from `'OUTSIDE_OR_CROSSING_COVERAGE'`.
7. Computes `internal` from `matched & fully_covered`.
8. Computes `statuses[internal & (numeric < boundary_distances)]` from `'NOT_BOUNDARY_LIMITED'`.
9. Computes `statuses[internal & (numeric >= boundary_distances)]` from `'BOUNDARY_LIMITED'`.
10. Returns `statuses`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `distances.to_numpy`, `len`, `np.full`, `np.isnan`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_expected_diagnostics`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_expected_diagnostics`

**Signature**

```python
def _expected_diagnostics(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
```

**Purpose**

Implements expected diagnostics according to the exact implementation and guards in this file.

**Inputs**

- `table` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `boundary_distances` (`np.ndarray`; required) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `positions` (`np.ndarray`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coverage` (`IgnBdTopoDepartmentCoverage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output.loc[:, list(_DIAGNOSTIC_COLUMNS)]`.

**Algorithm**

1. Computes `boundary_by_id` from `dict(zip(parcels['parcel_id'], boundary_distances, strict=True))`.
2. Computes `position_by_id` from `dict(zip(parcels['parcel_id'], positions, strict=True))`.
3. Computes `row_boundary` from `table['parcel_id'].map(boundary_by_id).astype('float64')`.
4. Computes `row_positions` from `table['parcel_id'].map(position_by_id)`.
5. Computes `output` from `pd.DataFrame(index=table.index.copy())`.
6. Computes `output['road_source_boundary_distance_m']` from `row_boundary`.
7. Computes `output['road_source_coverage_position']` from `row_positions`.
8. Computes `output['road_proximity_coverage_status']` from `_coverage_statuses(table['nearest_road_proxy_distance_m'], row_boundary.to_numpy(dtype='float64'), row_positions.to_numpy(dtype=object))`.
9. Iterates `(column, value)` over `_coverage_lineage(coverage).items()`. For each value: Computes `output[column]` from `value`.
10. Returns `output.loc[:, list(_DIAGNOSTIC_COLUMNS)]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `table.index.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_coverage_lineage`, `_coverage_lineage(coverage).items`, `_coverage_statuses`, `dict`, `list`, `pd.DataFrame`, `row_boundary.to_numpy`, `row_positions.to_numpy`, `table.index.copy`, `table['parcel_id'].map`, `table['parcel_id'].map(boundary_by_id).astype`, `zip`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_diagnosed_class_proximity`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_diagnosed_class_proximity`

**Signature**

```python
def _diagnosed_class_proximity(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
```

**Purpose**

Implements diagnosed class proximity according to the exact implementation and guards in this file.

**Inputs**

- `table` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `boundary_distances` (`np.ndarray`; required) — linear quantity, normally metres where the name ends in `_m`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `positions` (`np.ndarray`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coverage` (`IgnBdTopoDepartmentCoverage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `table.copy(deep=True)`.
2. Computes `diagnostics` from `_expected_diagnostics(table, parcels, boundary_distances, positions, coverage)`.
3. Iterates `column` over `_DIAGNOSTIC_COLUMNS`. For each value: Computes `output[column]` from `diagnostics[column]`.
4. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `table.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_expected_diagnostics`, `table.copy`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_selected_road_package`

**Signature**

```python
def _validate_selected_road_package(
    table: pd.DataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> None:
```

**Purpose**

Validates and rejects malformed selected road package according to the exact implementation and guards in this file.

**Inputs**

- `table` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coverage` (`IgnBdTopoDepartmentCoverage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `matched` from `table['nearest_road_proxy_distance_m'].notna()`.
2. Computes `expected` from `{'nearest_source_department_code': coverage.source_department_code, 'nearest_source_edition': coverage.source_edition, 'nearest_source_archive_sha256': coverage.source_archive_sha256}`.
3. Iterates `(column, value)` over `expected.items()`. For each value: Computes `selected` from `table.loc[matched, column]`. Checks `selected.isna().any() or not selected.eq(value).all()`. When true: Raises `RoadProximityCoverageError(f'Selected road package lineage differs from coverage: {column}')`.

**Validation and invariants**

- Rejects or diverts the path when `selected.isna().any() or not selected.eq(value).all()` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `expected.items`, `selected.eq`, `selected.eq(value).all`, `selected.isna`, `selected.isna().any`, `table['nearest_road_proxy_distance_m'].notna`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_validate_assessment_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_assessment_result`

**Signature**

```python
def _validate_assessment_result(
    input_parcels: gpd.GeoDataFrame,
    proximity: ParcelRoadProximityResult,
    road_source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
    loaded_coverage: IgnBdTopoDepartmentCoverage,
    result: object,
) -> None:
```

**Purpose**

Validates and rejects malformed assessment result according to the exact implementation and guards in this file.

**Inputs**

- `input_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `proximity` (`ParcelRoadProximityResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `loaded_coverage` (`IgnBdTopoDepartmentCoverage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `type(result) is not RoadProximityCoverageAssessmentResult`. When true: Raises `RoadProximityCoverageError('Coverage assessment result type is invalid')`.
2. Checks `result.source_coverage is not loaded_coverage`. When true: Raises `RoadProximityCoverageError('Coverage assessment source was not preserved')`.
3. Computes `(coverage, coverage_frame)` from `_validate_source_coverage(result.source_coverage, road_source, config)`.
4. Calls `_validate_parcel_frame(result.parcels, 'Coverage result parcels')` for its validation or side effect.
5. Calls `_require_same_parcels(input_parcels, result.parcels, 'Coverage result')` for its validation or side effect.
6. Calls `_require_same_parcels(proximity.parcels, result.parcels, 'Coverage result')` for its validation or side effect.
7. Checks `result.class_coverage is not proximity.class_coverage`. When true: Raises `RoadProximityCoverageError('Road class coverage was not preserved')`.
8. Computes `output` from `result.class_proximity`.
9. Computes `source` from `proximity.class_proximity`.
10. Checks `type(output) is not pd.DataFrame`. When true: Raises `RoadProximityCoverageError('Coverage class proximity is invalid')`.
11. Computes `expected_columns` from `(*CLASS_PROXIMITY_COLUMNS, *_DIAGNOSTIC_COLUMNS)`.
12. Checks `output.columns.duplicated().any() or tuple(output.columns) != expected_columns`. When true: Raises `RoadProximityCoverageError('Coverage class proximity schema is invalid')`.
13. Checks `not _same_index(output.index, source.index)`. When true: Raises `RoadProximityCoverageError('Coverage class proximity index changed')`.
14. Computes `prefix` from `output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]`.
15. Checks `not prefix.dtypes.equals(source.dtypes) or not prefix.equals(source)`. When true: Raises `RoadProximityCoverageError('Coverage assessment changed original class proximity facts')`.
16. Computes `(boundary_distances, positions)` from `_parcel_coverage_diagnostics(proximity.parcels, coverage_frame)`.
17. Computes `expected` from `_expected_diagnostics(source, proximity.parcels, boundary_distances, positions, coverage)`.
18. Computes `actual` from `output.loc[:, list(_DIAGNOSTIC_COLUMNS)]`.
19. Checks `not actual.dtypes.equals(expected.dtypes) or not actual.equals(expected)`. When true: Raises `RoadProximityCoverageError('Coverage diagnostics differ from geometric reconstruction')`.
20. Computes `numeric` from `_finite_nonnegative(output['road_source_boundary_distance_m'], 'Road source boundary distance')`.
21. Computes `position_values` from `output['road_source_coverage_position']`.
22. Checks `position_values.isna().any() or not set(position_values.unique()) <= _POSITIONS`. When true: Raises `RoadProximityCoverageError('Coverage position is invalid')`.
23. Computes `outside` from `position_values.eq('OUTSIDE_OR_CROSSING_COVERAGE').to_numpy(dtype='bool')`.
24. Checks `(numeric[outside] != 0.0).any()`. When true: Raises `RoadProximityCoverageError('Outside or crossing rows require zero boundary distance')`.
25. Computes `statuses` from `output['road_proximity_coverage_status']`.
26. Checks `statuses.isna().any() or not set(statuses.unique()) <= _STATUSES`. When true: Raises `RoadProximityCoverageError('Coverage status is invalid')`.
27. Calls `_validate_selected_road_package(output, coverage)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `type(result) is not RoadProximityCoverageAssessmentResult` is true.
- Rejects or diverts the path when `result.source_coverage is not loaded_coverage` is true.
- Rejects or diverts the path when `result.class_coverage is not proximity.class_coverage` is true.
- Rejects or diverts the path when `type(output) is not pd.DataFrame` is true.
- Rejects or diverts the path when `output.columns.duplicated().any() or tuple(output.columns) != expected_columns` is true.
- Rejects or diverts the path when `not _same_index(output.index, source.index)` is true.
- Rejects or diverts the path when `not prefix.dtypes.equals(source.dtypes) or not prefix.equals(source)` is true.
- Rejects or diverts the path when `not actual.dtypes.equals(expected.dtypes) or not actual.equals(expected)` is true.
- Rejects or diverts the path when `position_values.isna().any() or not set(position_values.unique()) <= _POSITIONS` is true.
- Rejects or diverts the path when `(numeric[outside] != 0.0).any()` is true.
- Rejects or diverts the path when `statuses.isna().any() or not set(statuses.unique()) <= _STATUSES` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(numeric[outside] != 0.0).any`, `RoadProximityCoverageError`, `_expected_diagnostics`, `_finite_nonnegative`, `_parcel_coverage_diagnostics`, `_require_same_parcels`, `_same_index`, `_validate_parcel_frame`, `_validate_selected_road_package`, `_validate_source_coverage`, `actual.dtypes.equals`, `actual.equals`, `list`, `output.columns.duplicated`, `output.columns.duplicated().any`, `position_values.eq`, `position_values.eq('OUTSIDE_OR_CROSSING_COVERAGE').to_numpy`, `position_values.isna`, `position_values.isna().any`, `position_values.unique`, `prefix.dtypes.equals`, `prefix.equals`, `set`, `statuses.isna`, `statuses.isna().any`, `statuses.unique`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_assess_road_proximity_coverage`

**Signature**

```python
def _assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> RoadProximityCoverageAssessmentResult:
```

**Purpose**

Assesses road proximity coverage according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_path` (`Path | None`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RoadProximityCoverageAssessmentResult`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `input_parcels` from `_validate_parcel_frame(parcels, 'Input parcels')`.
2. Computes `proximity` from `enrich_parcel_road_proximity(parcels, road_source, source_config, policy_path)`.
3. Computes `policy` from `load_ign_road_vehicle_proxy_policy() if policy_path is None else load_ign_road_vehicle_proxy_policy(policy_path)`.
4. Computes `validated_proximity` from `_validate_upstream_result(input_parcels, proximity, policy)`.
5. Computes `coverage` from `load_ign_bdtopo_department_coverage(road_source.extraction, source_config)`.
6. Computes `(validated_coverage, coverage_frame)` from `_validate_source_coverage(coverage, road_source, source_config)`.
7. Calls `_validate_selected_road_package(validated_proximity.class_proximity, validated_coverage)` for its validation or side effect.
8. Computes `(boundary_distances, positions)` from `_parcel_coverage_diagnostics(validated_proximity.parcels, coverage_frame)`.
9. Computes `output_table` from `_diagnosed_class_proximity(validated_proximity.class_proximity, validated_proximity.parcels, boundary_distances, positions, validated_coverage)`.
10. Computes `result` from `RoadProximityCoverageAssessmentResult(parcels=validated_proximity.parcels.copy(deep=True), class_proximity=output_table, class_coverage=validated_proximity.class_coverage, source_coverage=validated_coverage)`.
11. Calls `_validate_assessment_result(input_parcels, validated_proximity, road_source, source_config, validated_coverage, result)` for its validation or side effect.
12. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_bdtopo_department_coverage`, `load_ign_road_vehicle_proxy_policy`, `validated_proximity.parcels.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `RoadProximityCoverageAssessmentResult`, `_diagnosed_class_proximity`, `_parcel_coverage_diagnostics`, `_validate_assessment_result`, `_validate_parcel_frame`, `_validate_selected_road_package`, `_validate_source_coverage`, `_validate_upstream_result`, `enrich_parcel_road_proximity`, `load_ign_bdtopo_department_coverage`, `load_ign_road_vehicle_proxy_policy`, `validated_proximity.parcels.copy`.

**Known repository callers**

- `src/landscout/stages/assess_road_proximity_coverage.py` — `assess_road_proximity_coverage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `assess_road_proximity_coverage`

**Signature**

```python
def assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
```

**Purpose**

Diagnose source-bound road proximity using the verified package boundary.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `road_source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_path` (`Path | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RoadProximityCoverageAssessmentResult`. Observed return expression(s): `_assess_road_proximity_coverage(parcels, road_source, source_config, policy_path)`.

**Algorithm**

1. Runs guarded operation: Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `RoadProximityCoverageError('parcels must be a GeoDataFrame')`. Checks `type(road_source) is not IgnBdTopoRoadData`. When true: Raises `RoadProximityCoverageError('road_source must be an IgnBdTopoRoadData')`. Checks `type(source_config) is not IgnBdTopoSourceConfig`. When true: Raises `RoadProximityCoverageError('source_config must be an IgnBdTopoSourceConfig')`. Checks `policy_path is not None and (not isinstance(policy_path, Path))`. When true: Raises `RoadProximityCoverageError('policy_path must be a pathlib.Path or None')`. Executes 1 additional source-ordered statement(s). Handles `RoadProximityCoverageError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `type(road_source) is not IgnBdTopoRoadData` is true.
- Rejects or diverts the path when `type(source_config) is not IgnBdTopoSourceConfig` is true.
- Rejects or diverts the path when `policy_path is not None and (not isinstance(policy_path, Path))` is true.

**Exceptions**

- Explicitly raises: `RoadProximityCoverageError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `RoadProximityCoverageError`, `_assess_road_proximity_coverage`, `isinstance`, `type`.

**Known repository callers**

- `tests/unit/test_assess_road_proximity_coverage.py` — `_assess`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_loader_failure_is_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_malformed_upstream_result_fails_before_coverage_load`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_proximity_failure_stops_coverage_loading`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py` — `test_wrong_public_input_type_is_controlled_and_fast`

**Tests**

- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled`
- `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load`
- `tests/unit/test_assess_road_proximity_coverage.py::test_proximity_failure_stops_coverage_loading`
- `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once`
- `tests/unit/test_assess_road_proximity_coverage.py::test_wrong_public_input_type_is_controlled_and_fast`

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
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
| `road_proximity_coverage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_class` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_boundary_distance_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_product_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_source_coverage_spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |

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
