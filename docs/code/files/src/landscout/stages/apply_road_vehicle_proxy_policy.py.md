# `src/landscout/stages/apply_road_vehicle_proxy_policy.py`

## File identity

- Repository path: `src/landscout/stages/apply_road_vehicle_proxy_policy.py`
- File type: Python source
- Primary responsibility: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.
- Layer / domain: `stage` / `road`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `b51c6465f7e2ae3ca455724ffaad0c6cd0472950cbca70d14c8e4cff5d50e076`

## 1. Purpose

Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `road` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import math` — required by the implementation paths and symbols documented below.
- `from collections.abc import Callable, Mapping` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any, cast` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pandas.api.types import ( # type: ignore[import-untyped] is_bool_dtype, is_numeric_dtype, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoRoadData, IgnBdTopoSourceConfig, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_access_ign import ( NormalizedIgnRoadData, normalize_ign_roads, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.road_vehicle_proxy_policy import ( IgnRoadVehicleProxyPolicy, load_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `_GEOMETRY_STATUSES` | `frozenset({"VALID", "NULL", "EMPTY", "INVALID"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_TECHNICAL_GEOMETRY_RULE` | `"SOURCE_GEOMETRY_NOT_VALID"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_CRITICAL_FIELDS` | `( "fictitious_raw", "asset_status_raw", "nature_raw", "light_vehicle_access_raw", "private_raw", "importance_raw", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_UNKNOWN_FIELD_ORDER` | `( *_CRITICAL_FIELDS, "carriageway_width_raw", "closure_period_raw", "restriction_nature_raw", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_REQUIRED_COLUMNS` | `frozenset( { "geometry_status", "geometry", *_UNKNOWN_FIELD_ORDER, } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_APPLICATION_COLUMNS` | `( "road_proxy_primary_rule", "road_proxy_class", "road_proxy_rule_trace_json", "road_proxy_unknown_fields_json", "road_proxy_toll_evidence", "road_proxy_policy_id", "road_proxy_policy_schema_version", "road_proxy_policy_config_sha256", "road_proxy_policy_scope", "road_proxy_policy_evidence_checked_on", "road_proxy_vehicle_scope", "road_proxy_heavy_vehicle_access", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `IgnRoadVehicleProxyApplicationError`

**Purpose:** Raised when factual roads cannot receive the approved policy safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `IgnRoadVehicleProxyApplicationResult`

**Purpose:** Normalized factual roads plus deterministic general-car proxy evidence.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `roads` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_false_mask`

**Signature**

```python
def _false_mask(index: pd.Index) -> pd.Series:
```

**Purpose**

Implements false mask according to the exact implementation and guards in this file.

**Inputs**

- `index` (`pd.Index`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `pd.Series(False, index=index, dtype='bool')`.

**Algorithm**

1. Returns `pd.Series(False, index=index, dtype='bool')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.Series`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_classify_road_frame`
- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_exact_string_mask`
- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_json_array_from_masks`
- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_strict_boolean_masks`
- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_strict_private_masks`
- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_width_masks`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_object_scalar_mask`

**Signature**

```python
def _object_scalar_mask(
    series: pd.Series,
    predicate: Callable[[object], bool],
) -> pd.Series:
```

**Purpose**

Apply a strict scalar type gate only for heterogeneous object fixtures.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `predicate` (`Callable[[object], bool]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `pd.Series(np.asarray(values, dtype=bool), index=series.index)`.

**Algorithm**

1. Computes `function` from `np.frompyfunc(predicate, 1, 1)`.
2. Computes `values` from `function(series.to_numpy(dtype=object))`.
3. Returns `pd.Series(np.asarray(values, dtype=bool), index=series.index)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `function`, `np.asarray`, `np.frompyfunc`, `pd.Series`, `series.to_numpy`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_strict_boolean_masks`
- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_strict_private_masks`
- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_width_masks`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_is_strict_numeric_scalar`

**Signature**

```python
def _is_strict_numeric_scalar(value: object) -> bool:
```

**Purpose**

Returns whether `strict numeric scalar` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `type(value) in {int, float} or (isinstance(value, (np.integer, np.floating)) and (not isinstance(value, np.bool_)))`.

**Algorithm**

1. Returns `type(value) in {int, float} or (isinstance(value, (np.integer, np.floating)) and (not isinstance(value, np.bool_)))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `isinstance`, `type`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_is_strict_binary_numeric`
- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_is_strict_positive_numeric`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_is_strict_binary_numeric`

**Signature**

```python
def _is_strict_binary_numeric(value: object) -> bool:
```

**Purpose**

Returns whether `strict binary numeric` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `math.isfinite(numeric) and numeric in {0.0, 1.0}`; `False`.

**Algorithm**

1. Checks `not _is_strict_numeric_scalar(value)`. When true: Returns `False`.
2. Computes `numeric` from `float(cast(Any, value))`.
3. Returns `math.isfinite(numeric) and numeric in {0.0, 1.0}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_is_strict_numeric_scalar`, `cast`, `float`, `math.isfinite`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_is_strict_positive_numeric`

**Signature**

```python
def _is_strict_positive_numeric(value: object) -> bool:
```

**Purpose**

Returns whether `strict positive numeric` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `math.isfinite(numeric) and numeric > 0`; `False`.

**Algorithm**

1. Checks `not _is_strict_numeric_scalar(value)`. When true: Returns `False`.
2. Computes `numeric` from `float(cast(Any, value))`.
3. Returns `math.isfinite(numeric) and numeric > 0`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_is_strict_numeric_scalar`, `cast`, `float`, `math.isfinite`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_strict_boolean_masks`

**Signature**

```python
def _strict_boolean_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
```

**Purpose**

Implements strict boolean masks according to the exact implementation and guards in this file.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.Series, pd.Series, pd.Series]`. Observed return expression(s): `(known, known.copy(), known.copy())`; `(known, true, false)`.

**Algorithm**

1. Checks `is_bool_dtype(series.dtype)`. When true: Computes `known` from `series.notna()`. Computes `true` from `known & series.eq(True)`. Computes `false` from `known & series.eq(False)`. Executes 1 additional source-ordered statement(s).
2. Checks `series.dtype == 'object'`. When true: Computes `known` from `_object_scalar_mask(series, lambda value: type(value) is bool or isinstance(value, np.bool_))`. Computes `true` from `known & series.eq(True)`. Computes `false` from `known & series.eq(False)`. Executes 1 additional source-ordered statement(s).
3. Computes `known` from `_false_mask(series.index)`.
4. Returns `(known, known.copy(), known.copy())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `known.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_false_mask`, `_object_scalar_mask`, `is_bool_dtype`, `isinstance`, `known.copy`, `series.eq`, `series.notna`, `type`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_classify_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_strict_private_masks`

**Signature**

```python
def _strict_private_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
```

**Purpose**

Implements strict private masks according to the exact implementation and guards in this file.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.Series, pd.Series, pd.Series]`. Observed return expression(s): `(known, known.copy(), known.copy())`; `(known, known & series.eq(True), known & series.eq(False))`; `(known, known & series.eq(1), known & series.eq(0))`; `(known, true, false)`.

**Algorithm**

1. Checks `is_bool_dtype(series.dtype)`. When true: Computes `known` from `series.notna()`. Returns `(known, known & series.eq(True), known & series.eq(False))`.
2. Checks `is_numeric_dtype(series.dtype)`. When true: Computes `numeric` from `pd.to_numeric(series, errors='raise')`. Computes `finite` from `pd.Series(np.isfinite(numeric.to_numpy(dtype='float64', na_value=np.nan)), index=series.index)`. Computes `known` from `series.notna() & finite & (series.eq(0) | series.eq(1))`. Executes 1 additional source-ordered statement(s).
3. Checks `series.dtype == 'object'`. When true: Computes `boolean` from `_object_scalar_mask(series, lambda value: type(value) is bool or isinstance(value, np.bool_))`. Computes `numeric` from `_object_scalar_mask(series, _is_strict_binary_numeric)`. Computes `known` from `boolean | numeric`. Executes 3 additional source-ordered statement(s).
4. Computes `known` from `_false_mask(series.index)`.
5. Returns `(known, known.copy(), known.copy())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `known.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_false_mask`, `_object_scalar_mask`, `is_bool_dtype`, `is_numeric_dtype`, `isinstance`, `known.copy`, `np.isfinite`, `numeric.to_numpy`, `pd.Series`, `pd.to_numeric`, `series.eq`, `series.notna`, `type`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_classify_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_exact_string_mask`

**Signature**

```python
def _exact_string_mask(series: pd.Series) -> pd.Series:
```

**Purpose**

Implements exact string mask according to the exact implementation and guards in this file.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `series.notna() & stripped.notna() & stripped.ne('') & series.eq(stripped)`; `_false_mask(series.index)`.

**Algorithm**

1. Checks `not (isinstance(series.dtype, pd.StringDtype) or series.dtype == 'object')`. When true: Returns `_false_mask(series.index)`.
2. Computes `stripped` from `series.str.strip()`.
3. Returns `series.notna() & stripped.notna() & stripped.ne('') & series.eq(stripped)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_false_mask`, `isinstance`, `series.eq`, `series.notna`, `series.str.strip`, `stripped.ne`, `stripped.notna`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_known_string_masks`
- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_optional_exact_string_masks`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_known_string_masks`

**Signature**

```python
def _known_string_masks(
    series: pd.Series,
    known_values: frozenset[str],
) -> tuple[pd.Series, pd.Series]:
```

**Purpose**

Implements known string masks according to the exact implementation and guards in this file.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `known_values` (`frozenset[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.Series, pd.Series]`. Observed return expression(s): `(known, ~known)`.

**Algorithm**

1. Computes `exact` from `_exact_string_mask(series)`.
2. Computes `known` from `exact & series.isin(known_values)`.
3. Returns `(known, ~known)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_exact_string_mask`, `series.isin`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_classify_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_optional_exact_string_masks`

**Signature**

```python
def _optional_exact_string_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series]:
```

**Purpose**

Implements optional exact string masks according to the exact implementation and guards in this file.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.Series, pd.Series]`. Observed return expression(s): `(exact_present, invalid)`.

**Algorithm**

1. Computes `missing` from `series.isna()`.
2. Computes `exact_present` from `_exact_string_mask(series)`.
3. Computes `invalid` from `~missing & ~exact_present`.
4. Returns `(exact_present, invalid)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_exact_string_mask`, `series.isna`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_classify_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_width_masks`

**Signature**

```python
def _width_masks(
    series: pd.Series,
    threshold: float,
) -> tuple[pd.Series, pd.Series]:
```

**Purpose**

Implements width masks according to the exact implementation and guards in this file.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `threshold` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.Series, pd.Series]`. Observed return expression(s): `(_false_mask(series.index), ~missing)`; `(narrow, ~valid)`; `(narrow, ~missing & ~numeric)`.

**Algorithm**

1. Computes `missing` from `series.isna()`.
2. Checks `is_numeric_dtype(series.dtype) and (not is_bool_dtype(series.dtype))`. When true: Computes `numeric` from `series.to_numpy(dtype='float64', na_value=np.nan)`. Computes `finite_positive` from `pd.Series(np.isfinite(numeric) & (numeric > 0), index=series.index)`. Computes `valid` from `missing | finite_positive`. Executes 2 additional source-ordered statement(s).
3. Checks `series.dtype == 'object'`. When true: Computes `numeric` from `_object_scalar_mask(series, _is_strict_positive_numeric)`. Computes `numeric_values` from `pd.to_numeric(series.where(numeric), errors='coerce')`. Computes `narrow` from `numeric & numeric_values.lt(threshold)`. Executes 1 additional source-ordered statement(s).
4. Returns `(_false_mask(series.index), ~missing)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_false_mask`, `_object_scalar_mask`, `is_bool_dtype`, `is_numeric_dtype`, `np.isfinite`, `numeric_values.lt`, `pd.Series`, `pd.to_numeric`, `series.isna`, `series.lt`, `series.to_numpy`, `series.where`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_classify_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_json_array_from_masks`

**Signature**

```python
def _json_array_from_masks(
    index: pd.Index,
    ordered_masks: tuple[tuple[str, pd.Series], ...],
) -> pd.Series:
```

**Purpose**

Implements json array from masks according to the exact implementation and guards in this file.

**Inputs**

- `index` (`pd.Index`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `ordered_masks` (`tuple[tuple[str, pd.Series], ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `output + ']'`.

**Algorithm**

1. Computes `output` from `pd.Series('[', index=index, dtype='object')`.
2. Computes `populated` from `_false_mask(index)`.
3. Iterates `(value, raw_mask)` over `ordered_masks`. For each value: Computes `mask` from `raw_mask.fillna(False).astype(bool)`. Computes `token` from `json.dumps(value, ensure_ascii=False, separators=(',', ':'))`. Updates `output.loc[mask & ~populated]` using `` and `token`. Executes 2 additional source-ordered statement(s).
4. Returns `output + ']'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_false_mask`, `json.dumps`, `pd.Series`, `raw_mask.fillna`, `raw_mask.fillna(False).astype`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_classify_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_rule_outcomes`

**Signature**

```python
def _rule_outcomes(policy: IgnRoadVehicleProxyPolicy) -> Mapping[str, str]:
```

**Purpose**

Implements rule outcomes according to the exact implementation and guards in this file.

**Inputs**

- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Mapping[str, str]`. Observed return expression(s): `{'FICTITIOUS_GEOMETRY': outcomes.fictitious_geometry, 'PROJECT_GEOMETRY_NOT_SIGNIFICANT': outcomes.project_geometry_not_significant, 'NOT_IN_SERVICE': outcomes.not_in_service, 'PHYSICALLY_IMPOSSIBLE': outcomes.physically_impossible, 'NON_GENERAL_VEHICLE_NATURE': outcomes.non_general_vehicle_nature, 'RIGHTS_RESTRICTED': outcomes.rights_restricted, 'PRIVATE_ROAD': outcomes.private_road, 'TEMPORAL_C…`.

**Algorithm**

1. Computes `outcomes` from `policy.decision_outcomes`.
2. Returns `{'FICTITIOUS_GEOMETRY': outcomes.fictitious_geometry, 'PROJECT_GEOMETRY_NOT_SIGNIFICANT': outcomes.project_geometry_not_significant, 'NOT_IN_SERVICE': outcomes.not_in_service, 'PHYSICALLY_IMPOSSIBLE': outcomes.physically_impossible, 'NON_GENERAL_VEHICLE_NATURE': outcomes.non_general_vehicle_nature, 'RIGHTS_RESTRICTED': outcomes.rights_restricted, 'PRIVATE_R…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_classify_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_normalized_frame`

**Signature**

```python
def _validate_normalized_frame(frame: object) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed normalized frame according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`object`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Checks `not isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `IgnRoadVehicleProxyApplicationError('Normalized IGN roads must be a GeoDataFrame')`.
2. Checks `frame.columns.duplicated().any()`. When true: Raises `IgnRoadVehicleProxyApplicationError('Normalized IGN road columns must not contain duplicates')`.
3. Computes `missing` from `_REQUIRED_COLUMNS - set(frame.columns)`.
4. Checks `missing`. When true: Raises `IgnRoadVehicleProxyApplicationError('Normalized IGN roads are missing policy input columns: ' + ', '.join(sorted(missing)))`.
5. Checks `frame.active_geometry_name != 'geometry' or frame.crs is None`. When true: Raises `IgnRoadVehicleProxyApplicationError('Normalized IGN roads require active geometry and CRS')`.
6. Checks `not isinstance(frame.index, pd.RangeIndex)`. When true: Raises `IgnRoadVehicleProxyApplicationError('Normalized IGN roads must retain a RangeIndex')`.
7. Computes `statuses` from `frame['geometry_status']`.
8. Checks `statuses.isna().any() or not set(statuses.unique()).issubset(_GEOMETRY_STATUSES)`. When true: Raises `IgnRoadVehicleProxyApplicationError('Normalized IGN roads contain an impossible geometry_status')`.
9. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `frame.columns.duplicated().any()` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `frame.active_geometry_name != 'geometry' or frame.crs is None` is true.
- Rejects or diverts the path when `not isinstance(frame.index, pd.RangeIndex)` is true.
- Rejects or diverts the path when `statuses.isna().any() or not set(statuses.unique()).issubset(_GEOMETRY_STATUSES)` is true.

**Exceptions**

- Explicitly raises: `IgnRoadVehicleProxyApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `IgnRoadVehicleProxyApplicationError`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `isinstance`, `set`, `set(statuses.unique()).issubset`, `sorted`, `statuses.isna`, `statuses.isna().any`, `statuses.unique`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_classify_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_classify_road_frame`

**Signature**

```python
def _classify_road_frame(
    normalized: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements classify road frame according to the exact implementation and guards in this file.

**Inputs**

- `normalized` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`IgnRoadVehicleProxyPolicy`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `source` from `_validate_normalized_frame(normalized)`.
2. Computes `output` from `source.copy(deep=True)`.
3. Computes `index` from `output.index`.
4. Computes `valid_geometry` from `output['geometry_status'].eq('VALID')`.
5. Computes `technical_geometry` from `~valid_geometry`.
6. Computes `(fictitious_known, fictitious_true, _)` from `_strict_boolean_masks(output['fictitious_raw'])`.
7. Computes `(private_known, private_true, private_false)` from `_strict_private_masks(output['private_raw'])`.
8. Computes `asset_values` from `policy.asset_state`.
9. Computes `asset_domain` from `frozenset({*asset_values.in_service, *asset_values.project_geometry_not_significant, *asset_values.under_construction})`.
10. Computes `(asset_known, asset_unknown)` from `_known_string_masks(output['asset_status_raw'], asset_domain)`.
11. Computes `nature_values` from `policy.nature`.
12. Computes `nature_domain` from `frozenset({*nature_values.general_motor_road, *nature_values.limited_motor_proxy, *nature_values.non_general_vehicle, *nature_values.special_review})`.
13. Computes `(nature_known, nature_unknown)` from `_known_string_masks(output['nature_raw'], nature_domain)`.
14. Computes `access_values` from `policy.light_vehicle_access`.
15. Computes `access_domain` from `frozenset({*access_values.open, *access_values.toll, *access_values.rights_restricted, *access_values.physically_impossible})`.
16. Computes `(access_known, access_unknown)` from `_known_string_masks(output['light_vehicle_access_raw'], access_domain)`.
17. Computes `(importance_known, importance_unknown)` from `_known_string_masks(output['importance_raw'], policy.importance.known)`.
18. Computes `(closure_present, closure_unknown)` from `_optional_exact_string_masks(output['closure_period_raw'])`.
19. Computes `(restriction_present, restriction_unknown)` from `_optional_exact_string_masks(output['restriction_nature_raw'])`.
20. Computes `restriction_known` from `restriction_present & output['restriction_nature_raw'].isin(policy.known_restriction_review)`.
21. Computes `restriction_other` from `restriction_present & ~restriction_known`.
22. Computes `(narrow, width_unknown)` from `_width_masks(output['carriageway_width_raw'], policy.width_below_m)`.
23. Computes `unknown_masks` from `{'fictitious_raw': ~fictitious_known, 'asset_status_raw': asset_unknown, 'nature_raw': nature_unknown, 'light_vehicle_access_raw': access_unknown, 'private_raw': ~private_known, 'importance_raw': importance_unknown, 'carriageway_width_raw': width_unknown, 'closure_period_raw': closure_unknown, 'restriction_nature_raw'…`.
24. Computes `unknown_any` from `_false_mask(index)`.
25. Iterates `mask` over `unknown_masks.values()`. For each value: Updates `unknown_any` using `` and `mask.fillna(False)`.
26. Defines `rule_masks` with annotation `dict[str, pd.Series]` from `{'FICTITIOUS_GEOMETRY': fictitious_true, 'PROJECT_GEOMETRY_NOT_SIGNIFICANT': output['asset_status_raw'].isin(asset_values.project_geometry_not_significant), 'NOT_IN_SERVICE': output['asset_status_raw'].isin(asset_values.under_construction), 'PHYSICALLY_IMPOSSIBLE': output['light_vehicle_access_raw'].isin(access_values…`.
27. Computes `higher_rule` from `_false_mask(index)`.
28. Iterates `mask` over `rule_masks.values()`. For each value: Updates `higher_rule` using `` and `mask.fillna(False)`.
29. Computes `open_or_toll` from `fictitious_known & ~fictitious_true & asset_known & output['asset_status_raw'].isin(asset_values.in_service) & nature_known & output['nature_raw'].isin(nature_values.general_motor_road) & access_known & output['light_vehicle_access_raw'].isin(access_values.open | access_values.toll) & private_known & private_false & i…`.
30. Computes `rule_masks['OPEN_OR_TOLL']` from `open_or_toll`.
31. Computes `determined` from `higher_rule | open_or_toll`.
32. Computes `rule_masks['UNKNOWN']` from `unknown_any | ~determined`.
33. Computes `rule_masks` from `{rule: valid_geometry & mask.fillna(False).astype(bool) for rule, mask in rule_masks.items()}`.
34. Computes `outcomes` from `_rule_outcomes(policy)`.
35. Checks `set(outcomes) != set(policy.decision_precedence)`. When true: Raises `IgnRoadVehicleProxyApplicationError('Compiled policy precedence and outcomes do not agree')`.
36. Computes `primary` from `pd.Series(pd.NA, index=index, dtype='string')`.
37. Computes `proxy_class` from `pd.Series(pd.NA, index=index, dtype='string')`.
38. Computes `primary.loc[technical_geometry]` from `_TECHNICAL_GEOMETRY_RULE`.
39. Computes `proxy_class.loc[technical_geometry]` from `policy.classes.not_distance_proxy`.
40. Iterates `rule` over `policy.decision_precedence`. For each value: Computes `first` from `rule_masks[rule] & primary.isna()`. Computes `primary.loc[first]` from `rule`. Computes `proxy_class.loc[first]` from `outcomes[rule]`.
41. Checks `primary.isna().any() or proxy_class.isna().any()`. When true: Raises `IgnRoadVehicleProxyApplicationError('Every normalized IGN road must receive one primary policy result')`.
42. Computes `policy_trace_masks` from `tuple(((rule, rule_masks[rule]) for rule in policy.decision_precedence))`.
43. Computes `trace` from `_json_array_from_masks(index, ((_TECHNICAL_GEOMETRY_RULE, technical_geometry), *policy_trace_masks))`.
44. Computes `unknown_fields` from `_json_array_from_masks(index, tuple(((field, unknown_masks[field]) for field in _UNKNOWN_FIELD_ORDER)))`.
45. Computes `output['road_proxy_primary_rule']` from `primary`.
46. Computes `output['road_proxy_class']` from `proxy_class`.
47. Computes `output['road_proxy_rule_trace_json']` from `trace`.
48. Computes `output['road_proxy_unknown_fields_json']` from `unknown_fields`.
49. Computes `output['road_proxy_toll_evidence']` from `output['light_vehicle_access_raw'].isin(access_values.toll)`.
50. Computes `output['road_proxy_policy_id']` from `policy.policy_id`.
51. Computes `output['road_proxy_policy_schema_version']` from `policy.schema_version`.
52. Computes `output['road_proxy_policy_config_sha256']` from `policy.config_sha256`.
53. Computes `output['road_proxy_policy_scope']` from `policy.scope`.
54. Computes `output['road_proxy_policy_evidence_checked_on']` from `policy.evidence_checked_on`.
55. Computes `output['road_proxy_vehicle_scope']` from `policy.vehicle_scope`.
56. Computes `output['road_proxy_heavy_vehicle_access']` from `policy.heavy_vehicle_access`.
57. Computes `result` from `gpd.GeoDataFrame(output.loc[:, [*source.columns, *_APPLICATION_COLUMNS]], geometry=source.active_geometry_name, crs=source.crs)`.
58. Checks `len(result) != len(source) or not result.index.equals(source.index)`. When true: Raises `IgnRoadVehicleProxyApplicationError('IGN road policy application changed row count or order')`.
59. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `set(outcomes) != set(policy.decision_precedence)` is true.
- Rejects or diverts the path when `primary.isna().any() or proxy_class.isna().any()` is true.
- Rejects or diverts the path when `len(result) != len(source) or not result.index.equals(source.index)` is true.

**Exceptions**

- Explicitly raises: `IgnRoadVehicleProxyApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `source.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnRoadVehicleProxyApplicationError`, `_false_mask`, `_json_array_from_masks`, `_known_string_masks`, `_optional_exact_string_masks`, `_rule_outcomes`, `_strict_boolean_masks`, `_strict_private_masks`, `_validate_normalized_frame`, `_width_masks`, `frozenset`, `gpd.GeoDataFrame`, `len`, `mask.fillna`, `mask.fillna(False).astype`, `output['asset_status_raw'].isin`, `output['geometry_status'].eq`, `output['importance_raw'].isin`, `output['light_vehicle_access_raw'].isin`, `output['nature_raw'].isin`, `output['restriction_nature_raw'].isin`, `pd.Series`, `primary.isna`, `primary.isna().any`, `proxy_class.isna`, `proxy_class.isna().any`, `result.index.equals`, `rule_masks.items`, `rule_masks.values`, `set`, `source.copy`, `tuple`, `unknown_masks.values`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_apply_ign_road_vehicle_proxy_policy`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_apply_ign_road_vehicle_proxy_policy`

**Signature**

```python
def _apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> IgnRoadVehicleProxyApplicationResult:
```

**Purpose**

Applies ign road vehicle proxy policy according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_path` (`Path | None`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnRoadVehicleProxyApplicationResult`. Observed return expression(s): `IgnRoadVehicleProxyApplicationResult(roads=_classify_road_frame(normalized.road_segments, policy))`.

**Algorithm**

1. Computes `normalized` from `normalize_ign_roads(source, source_config)`.
2. Checks `type(normalized) is not NormalizedIgnRoadData`. When true: Raises `IgnRoadVehicleProxyApplicationError('IGN road normalization returned an invalid result type')`.
3. Computes `policy` from `load_ign_road_vehicle_proxy_policy() if policy_path is None else load_ign_road_vehicle_proxy_policy(policy_path)`.
4. Returns `IgnRoadVehicleProxyApplicationResult(roads=_classify_road_frame(normalized.road_segments, policy))`.

**Validation and invariants**

- Rejects or diverts the path when `type(normalized) is not NormalizedIgnRoadData` is true.

**Exceptions**

- Explicitly raises: `IgnRoadVehicleProxyApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_ign_road_vehicle_proxy_policy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnRoadVehicleProxyApplicationError`, `IgnRoadVehicleProxyApplicationResult`, `_classify_road_frame`, `load_ign_road_vehicle_proxy_policy`, `normalize_ign_roads`, `type`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `apply_ign_road_vehicle_proxy_policy`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `apply_ign_road_vehicle_proxy_policy`

**Signature**

```python
def apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
```

**Purpose**

Source-completely normalize roads and apply the exact policy bytes once.

**Inputs**

- `source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_path` (`Path | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnRoadVehicleProxyApplicationResult`. Observed return expression(s): `_apply_ign_road_vehicle_proxy_policy(source, source_config, policy_path)`.

**Algorithm**

1. Runs guarded operation: Checks `type(source) is not IgnBdTopoRoadData`. When true: Raises `TypeError('source must be an IgnBdTopoRoadData')`. Checks `type(source_config) is not IgnBdTopoSourceConfig`. When true: Raises `TypeError('source_config must be an IgnBdTopoSourceConfig')`. Checks `policy_path is not None and (not isinstance(policy_path, Path))`. When true: Raises `TypeError('policy_path must be a pathlib.Path or None')`. Returns `_apply_ign_road_vehicle_proxy_policy(source, source_config, policy_path)`. Handles `IgnRoadVehicleProxyApplicationError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(source) is not IgnBdTopoRoadData` is true.
- Rejects or diverts the path when `type(source_config) is not IgnBdTopoSourceConfig` is true.
- Rejects or diverts the path when `policy_path is not None and (not isinstance(policy_path, Path))` is true.

**Exceptions**

- Explicitly raises: `IgnRoadVehicleProxyApplicationError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnRoadVehicleProxyApplicationError`, `TypeError`, `_apply_ign_road_vehicle_proxy_policy`, `isinstance`, `type`.

**Known repository callers**

- `src/landscout/stages/enrich_road_proximity.py` — `_enrich_parcel_road_proximity`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `_apply`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_malformed_policy_path_has_controlled_error`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_normalization_failure_stops_policy_loading`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_policy_path_must_be_path_or_none`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_source_complete_normalization_is_invoked_exactly_once`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_source_config_is_exact_pydantic_type`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_source_object_is_not_mutated`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_valid_geometry_status_with_unsupported_geometry_is_not_repaired`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_wrong_source_config_type_has_controlled_error`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_wrong_source_type_has_controlled_error`

**Tests**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_config_is_exact_pydantic_type`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_config_type_has_controlled_error`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error`

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `OPEN_OR_TOLL` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNKNOWN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `carriageway_width_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `closure_period_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `fictitious_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `light_vehicle_access_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `private_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_class` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_heavy_vehicle_access` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_config_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_evidence_checked_on` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_primary_rule` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_rule_trace_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_toll_evidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_unknown_fields_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_vehicle_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
