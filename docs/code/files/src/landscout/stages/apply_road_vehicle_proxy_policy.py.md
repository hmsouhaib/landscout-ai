# `src/landscout/stages/apply_road_vehicle_proxy_policy.py`

## File identity

- Repository path: `src/landscout/stages/apply_road_vehicle_proxy_policy.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: road
- Responsibility: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.
- Source SHA256: `b51c6465f7e2ae3ca455724ffaad0c6cd0472950cbca70d14c8e4cff5d50e076`

## 1. Purpose

Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **road** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import math`
- `from collections.abc import Callable, Mapping`
- `from dataclasses import dataclass`
- `from pathlib import Path`
- `from typing import Any, cast`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pandas.api.types import (  # type: ignore[import-untyped]
    is_bool_dtype,
    is_numeric_dtype,
)`

### Internal LandScout imports

- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`
- `from landscout.stages.normalize_access_ign import (
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`

## 4. Contract taxonomy

### A. Python constants

#### `_GEOMETRY_STATUSES`

```python
_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_validate_normalized_frame` (value argument/reference).

#### `_TECHNICAL_GEOMETRY_RULE`

```python
_TECHNICAL_GEOMETRY_RULE = "SOURCE_GEOMETRY_NOT_VALID"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_CRITICAL_FIELDS`

```python
_CRITICAL_FIELDS = (
    "fictitious_raw",
    "asset_status_raw",
    "nature_raw",
    "light_vehicle_access_raw",
    "private_raw",
    "importance_raw",
)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_UNKNOWN_FIELD_ORDER`

```python
_UNKNOWN_FIELD_ORDER = (
    *_CRITICAL_FIELDS,
    "carriageway_width_raw",
    "closure_period_raw",
    "restriction_nature_raw",
)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_REQUIRED_COLUMNS`

```python
_REQUIRED_COLUMNS = frozenset(
    {
        "geometry_status",
        "geometry",
        *_UNKNOWN_FIELD_ORDER,
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `_APPLICATION_COLUMNS`

```python
_APPLICATION_COLUMNS = (
    "road_proxy_primary_rule",
    "road_proxy_class",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_policy_scope",
    "road_proxy_policy_evidence_checked_on",
    "road_proxy_vehicle_scope",
    "road_proxy_heavy_vehicle_access",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "IgnRoadVehicleProxyApplicationError",
    "IgnRoadVehicleProxyApplicationResult",
    "apply_ign_road_vehicle_proxy_policy",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `IgnRoadVehicleProxyApplicationError`

**Purpose:** Raised when factual roads cannot receive the approved policy safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_validate_normalized_frame` via `IgnRoadVehicleProxyApplicationError`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `IgnRoadVehicleProxyApplicationError`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationError`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationError`.
- callback/function object: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error` via `pytest.raises(IgnRoadVehicleProxyApplicationError)`.
- callback/function object: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_config_type_has_controlled_error` via `pytest.raises(IgnRoadVehicleProxyApplicationError)`.
- callback/function object: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` via `pytest.raises(IgnRoadVehicleProxyApplicationError)`.
- callback/function object: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` via `pytest.raises(IgnRoadVehicleProxyApplicationError)`.
- callback/function object: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_geometry_status_is_rejected` via `pytest.raises(IgnRoadVehicleProxyApplicationError)`.
- callback/function object: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `pytest.raises(IgnRoadVehicleProxyApplicationError)`.
- callback/function object: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` via `pytest.raises(IgnRoadVehicleProxyApplicationError)`.
- callback/function object: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_config_is_exact_pydantic_type` via `pytest.raises(IgnRoadVehicleProxyApplicationError)`.
- import/re-export: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity` via `IgnRoadVehicleProxyApplicationError`.
- import/re-export: `tests/unit/test_enrich_road_proximity.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
)`.

**Exact class source**

```python
class IgnRoadVehicleProxyApplicationError(ValueError):
    """Raised when factual roads cannot receive the approved policy safely."""
```

### `IgnRoadVehicleProxyApplicationResult`

**Purpose:** Normalized factual roads plus deterministic general-car proxy evidence.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `roads` | `roads: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationResult`.
- import/re-export: `src/landscout/stages/enrich_road_proximity.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`.
- import/re-export: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_enrich` via `IgnRoadVehicleProxyApplicationResult`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once` via `IgnRoadVehicleProxyApplicationResult`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` via `IgnRoadVehicleProxyApplicationResult`.
- import/re-export: `tests/unit/test_enrich_road_proximity.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
)`.

**Exact class source**

```python
class IgnRoadVehicleProxyApplicationResult:
    """Normalized factual roads plus deterministic general-car proxy evidence."""

    roads: gpd.GeoDataFrame
```


## 6. Functions and methods

### `_false_mask`

**Exact signature**

```python
def _false_mask(index: pd.Index) -> pd.Series:
```

**Purpose**

Private `road` helper for false mask; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
pd.Series(False, index=index, dtype='bool')
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_strict_boolean_masks` via `_false_mask`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_strict_private_masks` via `_false_mask`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_exact_string_mask` via `_false_mask`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_width_masks` via `_false_mask`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_json_array_from_masks` via `_false_mask`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `_false_mask`.

**Complete source-ordered implementation**

```python
def _false_mask(index: pd.Index) -> pd.Series:
    return pd.Series(False, index=index, dtype="bool")
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_object_scalar_mask`

**Exact signature**

```python
def _object_scalar_mask(
    series: pd.Series,
    predicate: Callable[[object], bool],
) -> pd.Series:
```

**Purpose**

Apply a strict scalar type gate only for heterogeneous object fixtures.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
pd.Series(np.asarray(values, dtype=bool), index=series.index)
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_strict_boolean_masks` via `_object_scalar_mask`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_strict_private_masks` via `_object_scalar_mask`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_width_masks` via `_object_scalar_mask`.

**Complete source-ordered implementation**

```python
def _object_scalar_mask(
    series: pd.Series,
    predicate: Callable[[object], bool],
) -> pd.Series:
    """Apply a strict scalar type gate only for heterogeneous object fixtures."""

    function = np.frompyfunc(predicate, 1, 1)
    values = function(series.to_numpy(dtype=object))
    return pd.Series(np.asarray(values, dtype=bool), index=series.index)
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_is_strict_numeric_scalar`

**Exact signature**

```python
def _is_strict_numeric_scalar(value: object) -> bool:
```

**Purpose**

Tests whether strict numeric scalar; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
type(value) in {int, float} or (isinstance(value, (np.integer, np.floating)) and (not isinstance(value, np.bool_)))
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_is_strict_binary_numeric` via `_is_strict_numeric_scalar`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_is_strict_positive_numeric` via `_is_strict_numeric_scalar`.

**Complete source-ordered implementation**

```python
def _is_strict_numeric_scalar(value: object) -> bool:
    return type(value) in {int, float} or (
        isinstance(value, (np.integer, np.floating))
        and not isinstance(value, np.bool_)
    )
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_is_strict_binary_numeric`

**Exact signature**

```python
def _is_strict_binary_numeric(value: object) -> bool:
```

**Purpose**

Tests whether strict binary numeric; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
math.isfinite(numeric) and numeric in {0.0, 1.0}

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

- callback/function object: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_strict_private_masks` via `_object_scalar_mask(series, _is_strict_binary_numeric)`.

**Complete source-ordered implementation**

```python
def _is_strict_binary_numeric(value: object) -> bool:
    if not _is_strict_numeric_scalar(value):
        return False
    numeric = float(cast(Any, value))
    return math.isfinite(numeric) and numeric in {0.0, 1.0}
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_is_strict_positive_numeric`

**Exact signature**

```python
def _is_strict_positive_numeric(value: object) -> bool:
```

**Purpose**

Tests whether strict positive numeric; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
math.isfinite(numeric) and numeric > 0

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

- callback/function object: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_width_masks` via `_object_scalar_mask(series, _is_strict_positive_numeric)`.

**Complete source-ordered implementation**

```python
def _is_strict_positive_numeric(value: object) -> bool:
    if not _is_strict_numeric_scalar(value):
        return False
    numeric = float(cast(Any, value))
    return math.isfinite(numeric) and numeric > 0
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_strict_boolean_masks`

**Exact signature**

```python
def _strict_boolean_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
```

**Purpose**

Private `road` helper for strict boolean masks; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[pd.Series, pd.Series, pd.Series]`.
- Every observed return expression is reproduced without truncation:
```python
(known, known.copy(), known.copy())

(known, true, false)

(known, true, false)
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `_strict_boolean_masks`.

**Complete source-ordered implementation**

```python
def _strict_boolean_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
    if is_bool_dtype(series.dtype):
        known = series.notna()
        true = known & series.eq(True)
        false = known & series.eq(False)
        return known, true, false

    if series.dtype == "object":
        known = _object_scalar_mask(
            series,
            lambda value: type(value) is bool or isinstance(value, np.bool_),
        )
        true = known & series.eq(True)
        false = known & series.eq(False)
        return known, true, false

    known = _false_mask(series.index)
    return known, known.copy(), known.copy()
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_strict_private_masks`

**Exact signature**

```python
def _strict_private_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
```

**Purpose**

Private `road` helper for strict private masks; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[pd.Series, pd.Series, pd.Series]`.
- Every observed return expression is reproduced without truncation:
```python
(known, known.copy(), known.copy())

(known, known & series.eq(True), known & series.eq(False))

(known, known & series.eq(1), known & series.eq(0))

(known, true, false)
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `_strict_private_masks`.

**Complete source-ordered implementation**

```python
def _strict_private_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
    if is_bool_dtype(series.dtype):
        known = series.notna()
        return known, known & series.eq(True), known & series.eq(False)

    if is_numeric_dtype(series.dtype):
        numeric = pd.to_numeric(series, errors="raise")
        finite = pd.Series(
            np.isfinite(numeric.to_numpy(dtype="float64", na_value=np.nan)),
            index=series.index,
        )
        known = series.notna() & finite & (series.eq(0) | series.eq(1))
        return known, known & series.eq(1), known & series.eq(0)

    if series.dtype == "object":
        boolean = _object_scalar_mask(
            series,
            lambda value: type(value) is bool or isinstance(value, np.bool_),
        )
        numeric = _object_scalar_mask(
            series,
            _is_strict_binary_numeric,
        )
        known = boolean | numeric
        true = known & series.eq(1)
        false = known & series.eq(0)
        return known, true, false

    known = _false_mask(series.index)
    return known, known.copy(), known.copy()
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_exact_string_mask`

**Exact signature**

```python
def _exact_string_mask(series: pd.Series) -> pd.Series:
```

**Purpose**

Private `road` helper for exact string mask; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
series.notna() & stripped.notna() & stripped.ne('') & series.eq(stripped)

_false_mask(series.index)
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_known_string_masks` via `_exact_string_mask`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_optional_exact_string_masks` via `_exact_string_mask`.

**Complete source-ordered implementation**

```python
def _exact_string_mask(series: pd.Series) -> pd.Series:
    if not (isinstance(series.dtype, pd.StringDtype) or series.dtype == "object"):
        return _false_mask(series.index)
    stripped = series.str.strip()
    return series.notna() & stripped.notna() & stripped.ne("") & series.eq(stripped)
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_known_string_masks`

**Exact signature**

```python
def _known_string_masks(
    series: pd.Series,
    known_values: frozenset[str],
) -> tuple[pd.Series, pd.Series]:
```

**Purpose**

Private `road` helper for known string masks; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[pd.Series, pd.Series]`.
- Every observed return expression is reproduced without truncation:
```python
(known, ~known)
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `_known_string_masks`.

**Complete source-ordered implementation**

```python
def _known_string_masks(
    series: pd.Series,
    known_values: frozenset[str],
) -> tuple[pd.Series, pd.Series]:
    exact = _exact_string_mask(series)
    known = exact & series.isin(known_values)
    return known, ~known
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_optional_exact_string_masks`

**Exact signature**

```python
def _optional_exact_string_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series]:
```

**Purpose**

Private `road` helper for optional exact string masks; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[pd.Series, pd.Series]`.
- Every observed return expression is reproduced without truncation:
```python
(exact_present, invalid)
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `_optional_exact_string_masks`.

**Complete source-ordered implementation**

```python
def _optional_exact_string_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series]:
    missing = series.isna()
    exact_present = _exact_string_mask(series)
    invalid = ~missing & ~exact_present
    return exact_present, invalid
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_width_masks`

**Exact signature**

```python
def _width_masks(
    series: pd.Series,
    threshold: float,
) -> tuple[pd.Series, pd.Series]:
```

**Purpose**

Private `road` helper for width masks; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[pd.Series, pd.Series]`.
- Every observed return expression is reproduced without truncation:
```python
(_false_mask(series.index), ~missing)

(narrow, ~valid)

(narrow, ~missing & ~numeric)
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `_width_masks`.

**Complete source-ordered implementation**

```python
def _width_masks(
    series: pd.Series,
    threshold: float,
) -> tuple[pd.Series, pd.Series]:
    missing = series.isna()
    if is_numeric_dtype(series.dtype) and not is_bool_dtype(series.dtype):
        numeric = series.to_numpy(dtype="float64", na_value=np.nan)
        finite_positive = pd.Series(
            np.isfinite(numeric) & (numeric > 0),
            index=series.index,
        )
        valid = missing | finite_positive
        narrow = finite_positive & series.lt(threshold)
        return narrow, ~valid

    if series.dtype == "object":
        numeric = _object_scalar_mask(
            series,
            _is_strict_positive_numeric,
        )
        numeric_values = pd.to_numeric(series.where(numeric), errors="coerce")
        narrow = numeric & numeric_values.lt(threshold)
        return narrow, ~missing & ~numeric

    return _false_mask(series.index), ~missing
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_json_array_from_masks`

**Exact signature**

```python
def _json_array_from_masks(
    index: pd.Index,
    ordered_masks: tuple[tuple[str, pd.Series], ...],
) -> pd.Series:
```

**Purpose**

Private `road` helper for json array from masks; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
output + ']'
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `_json_array_from_masks`.

**Complete source-ordered implementation**

```python
def _json_array_from_masks(
    index: pd.Index,
    ordered_masks: tuple[tuple[str, pd.Series], ...],
) -> pd.Series:
    output = pd.Series("[", index=index, dtype="object")
    populated = _false_mask(index)
    for value, raw_mask in ordered_masks:
        mask = raw_mask.fillna(False).astype(bool)
        token = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        output.loc[mask & ~populated] += token
        output.loc[mask & populated] += f",{token}"
        populated |= mask
    return output + "]"
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_rule_outcomes`

**Exact signature**

```python
def _rule_outcomes(policy: IgnRoadVehicleProxyPolicy) -> Mapping[str, str]:
```

**Purpose**

Private `road` helper for rule outcomes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Mapping[str, str]`.
- Every observed return expression is reproduced without truncation:
```python
{'FICTITIOUS_GEOMETRY': outcomes.fictitious_geometry, 'PROJECT_GEOMETRY_NOT_SIGNIFICANT': outcomes.project_geometry_not_significant, 'NOT_IN_SERVICE': outcomes.not_in_service, 'PHYSICALLY_IMPOSSIBLE': outcomes.physically_impossible, 'NON_GENERAL_VEHICLE_NATURE': outcomes.non_general_vehicle_nature, 'RIGHTS_RESTRICTED': outcomes.rights_restricted, 'PRIVATE_ROAD': outcomes.private_road, 'TEMPORAL_CLOSURE': outcomes.temporal_closure, 'KNOWN_RESTRICTION': outcomes.known_restriction, 'OTHER_RECORDED_RESTRICTION': outcomes.other_recorded_restriction, 'SPECIAL_NATURE': outcomes.special_nature, 'LIMITED_NATURE': outcomes.limited_nature, 'IMPORTANCE_6': outcomes.importance_6, 'NARROW_CARRIAGEWAY': outcomes.narrow_carriageway, 'OPEN_OR_TOLL': outcomes.open_or_toll, 'UNKNOWN': outcomes.unknown}
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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `_rule_outcomes`.

**Complete source-ordered implementation**

```python
def _rule_outcomes(policy: IgnRoadVehicleProxyPolicy) -> Mapping[str, str]:
    outcomes = policy.decision_outcomes
    return {
        "FICTITIOUS_GEOMETRY": outcomes.fictitious_geometry,
        "PROJECT_GEOMETRY_NOT_SIGNIFICANT": (
            outcomes.project_geometry_not_significant
        ),
        "NOT_IN_SERVICE": outcomes.not_in_service,
        "PHYSICALLY_IMPOSSIBLE": outcomes.physically_impossible,
        "NON_GENERAL_VEHICLE_NATURE": outcomes.non_general_vehicle_nature,
        "RIGHTS_RESTRICTED": outcomes.rights_restricted,
        "PRIVATE_ROAD": outcomes.private_road,
        "TEMPORAL_CLOSURE": outcomes.temporal_closure,
        "KNOWN_RESTRICTION": outcomes.known_restriction,
        "OTHER_RECORDED_RESTRICTION": outcomes.other_recorded_restriction,
        "SPECIAL_NATURE": outcomes.special_nature,
        "LIMITED_NATURE": outcomes.limited_nature,
        "IMPORTANCE_6": outcomes.importance_6,
        "NARROW_CARRIAGEWAY": outcomes.narrow_carriageway,
        "OPEN_OR_TOLL": outcomes.open_or_toll,
        "UNKNOWN": outcomes.unknown,
    }
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_normalized_frame`

**Exact signature**

```python
def _validate_normalized_frame(frame: object) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent normalized frame; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `frame.columns.duplicated().any()`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `frame.active_geometry_name != 'geometry' or frame.crs is None`.
- Guard with a raise path: `not isinstance(frame.index, pd.RangeIndex)`.
- Guard with a raise path: `statuses.isna().any() or not set(statuses.unique()).issubset(_GEOMETRY_STATUSES)`.
- Explicit raise expressions: `IgnRoadVehicleProxyApplicationError('Normalized IGN road columns must not contain duplicates')`, `IgnRoadVehicleProxyApplicationError('Normalized IGN roads are missing policy input columns: ' + ', '.join(sorted(missing)))`, `IgnRoadVehicleProxyApplicationError('Normalized IGN roads contain an impossible geometry_status')`, `IgnRoadVehicleProxyApplicationError('Normalized IGN roads must be a GeoDataFrame')`, `IgnRoadVehicleProxyApplicationError('Normalized IGN roads must retain a RangeIndex')`, `IgnRoadVehicleProxyApplicationError('Normalized IGN roads require active geometry and CRS')`.

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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `_validate_normalized_frame`.

**Complete source-ordered implementation**

```python
def _validate_normalized_frame(frame: object) -> gpd.GeoDataFrame:
    if not isinstance(frame, gpd.GeoDataFrame):
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads must be a GeoDataFrame"
        )
    if frame.columns.duplicated().any():
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN road columns must not contain duplicates"
        )
    missing = _REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads are missing policy input columns: "
            + ", ".join(sorted(missing))
        )
    if frame.active_geometry_name != "geometry" or frame.crs is None:
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads require active geometry and CRS"
        )
    if not isinstance(frame.index, pd.RangeIndex):
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads must retain a RangeIndex"
        )
    statuses = frame["geometry_status"]
    if statuses.isna().any() or not set(statuses.unique()).issubset(
        _GEOMETRY_STATUSES
    ):
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads contain an impossible geometry_status"
        )
    return frame
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_classify_road_frame`

**Exact signature**

```python
def _classify_road_frame(
    normalized: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `road` helper for classify road frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `set(outcomes) != set(policy.decision_precedence)`.
- Guard with a raise path: `primary.isna().any() or proxy_class.isna().any()`.
- Guard with a raise path: `len(result) != len(source) or not result.index.equals(source.index)`.
- Explicit raise expressions: `IgnRoadVehicleProxyApplicationError('Compiled policy precedence and outcomes do not agree')`, `IgnRoadVehicleProxyApplicationError('Every normalized IGN road must receive one primary policy result')`, `IgnRoadVehicleProxyApplicationError('IGN road policy application changed row count or order')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `output['geometry_status'].eq`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output['road_proxy_class']`, `output['road_proxy_heavy_vehicle_access']`, `output['road_proxy_policy_config_sha256']`, `output['road_proxy_policy_evidence_checked_on']`, `output['road_proxy_policy_id']`, `output['road_proxy_policy_schema_version']`, `output['road_proxy_policy_scope']`, `output['road_proxy_primary_rule']`, `output['road_proxy_rule_trace_json']`, `output['road_proxy_toll_evidence']`, `output['road_proxy_unknown_fields_json']`, `output['road_proxy_vehicle_scope']`, `primary.loc[first]`, `primary.loc[technical_geometry]`, `proxy_class.loc[first]`, `proxy_class.loc[technical_geometry]`, `rule_masks['OPEN_OR_TOLL']`, `rule_masks['UNKNOWN']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_apply_ign_road_vehicle_proxy_policy` via `_classify_road_frame`.

**Complete source-ordered implementation**

```python
def _classify_road_frame(
    normalized: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
    source = _validate_normalized_frame(normalized)
    output = source.copy(deep=True)
    index = output.index
    valid_geometry = output["geometry_status"].eq("VALID")
    technical_geometry = ~valid_geometry

    fictitious_known, fictitious_true, _ = _strict_boolean_masks(
        output["fictitious_raw"]
    )
    private_known, private_true, private_false = _strict_private_masks(
        output["private_raw"]
    )

    asset_values = policy.asset_state
    asset_domain = frozenset(
        {
            *asset_values.in_service,
            *asset_values.project_geometry_not_significant,
            *asset_values.under_construction,
        }
    )
    asset_known, asset_unknown = _known_string_masks(
        output["asset_status_raw"], asset_domain
    )

    nature_values = policy.nature
    nature_domain = frozenset(
        {
            *nature_values.general_motor_road,
            *nature_values.limited_motor_proxy,
            *nature_values.non_general_vehicle,
            *nature_values.special_review,
        }
    )
    nature_known, nature_unknown = _known_string_masks(
        output["nature_raw"], nature_domain
    )

    access_values = policy.light_vehicle_access
    access_domain = frozenset(
        {
            *access_values.open,
            *access_values.toll,
            *access_values.rights_restricted,
            *access_values.physically_impossible,
        }
    )
    access_known, access_unknown = _known_string_masks(
        output["light_vehicle_access_raw"], access_domain
    )
    importance_known, importance_unknown = _known_string_masks(
        output["importance_raw"], policy.importance.known
    )

    closure_present, closure_unknown = _optional_exact_string_masks(
        output["closure_period_raw"]
    )
    restriction_present, restriction_unknown = _optional_exact_string_masks(
        output["restriction_nature_raw"]
    )
    restriction_known = restriction_present & output[
        "restriction_nature_raw"
    ].isin(policy.known_restriction_review)
    restriction_other = restriction_present & ~restriction_known
    narrow, width_unknown = _width_masks(
        output["carriageway_width_raw"], policy.width_below_m
    )

    unknown_masks = {
        "fictitious_raw": ~fictitious_known,
        "asset_status_raw": asset_unknown,
        "nature_raw": nature_unknown,
        "light_vehicle_access_raw": access_unknown,
        "private_raw": ~private_known,
        "importance_raw": importance_unknown,
        "carriageway_width_raw": width_unknown,
        "closure_period_raw": closure_unknown,
        "restriction_nature_raw": restriction_unknown,
    }
    unknown_any = _false_mask(index)
    for mask in unknown_masks.values():
        unknown_any |= mask.fillna(False)

    rule_masks: dict[str, pd.Series] = {
        "FICTITIOUS_GEOMETRY": fictitious_true,
        "PROJECT_GEOMETRY_NOT_SIGNIFICANT": output["asset_status_raw"].isin(
            asset_values.project_geometry_not_significant
        ),
        "NOT_IN_SERVICE": output["asset_status_raw"].isin(
            asset_values.under_construction
        ),
        "PHYSICALLY_IMPOSSIBLE": output["light_vehicle_access_raw"].isin(
            access_values.physically_impossible
        ),
        "NON_GENERAL_VEHICLE_NATURE": output["nature_raw"].isin(
            nature_values.non_general_vehicle
        ),
        "RIGHTS_RESTRICTED": output["light_vehicle_access_raw"].isin(
            access_values.rights_restricted
        ),
        "PRIVATE_ROAD": private_true,
        "TEMPORAL_CLOSURE": closure_present,
        "KNOWN_RESTRICTION": restriction_known,
        "OTHER_RECORDED_RESTRICTION": restriction_other,
        "SPECIAL_NATURE": output["nature_raw"].isin(nature_values.special_review),
        "LIMITED_NATURE": output["nature_raw"].isin(
            nature_values.limited_motor_proxy
        ),
        "IMPORTANCE_6": output["importance_raw"].isin(policy.importance.limited),
        "NARROW_CARRIAGEWAY": narrow,
    }
    higher_rule = _false_mask(index)
    for mask in rule_masks.values():
        higher_rule |= mask.fillna(False)

    open_or_toll = (
        fictitious_known
        & ~fictitious_true
        & asset_known
        & output["asset_status_raw"].isin(asset_values.in_service)
        & nature_known
        & output["nature_raw"].isin(nature_values.general_motor_road)
        & access_known
        & output["light_vehicle_access_raw"].isin(
            access_values.open | access_values.toll
        )
        & private_known
        & private_false
        & importance_known
        & ~unknown_any
        & ~higher_rule
    )
    rule_masks["OPEN_OR_TOLL"] = open_or_toll
    determined = higher_rule | open_or_toll
    rule_masks["UNKNOWN"] = unknown_any | ~determined
    rule_masks = {
        rule: valid_geometry & mask.fillna(False).astype(bool)
        for rule, mask in rule_masks.items()
    }

    outcomes = _rule_outcomes(policy)
    if set(outcomes) != set(policy.decision_precedence):
        raise IgnRoadVehicleProxyApplicationError(
            "Compiled policy precedence and outcomes do not agree"
        )

    primary = pd.Series(pd.NA, index=index, dtype="string")
    proxy_class = pd.Series(pd.NA, index=index, dtype="string")
    primary.loc[technical_geometry] = _TECHNICAL_GEOMETRY_RULE
    proxy_class.loc[technical_geometry] = policy.classes.not_distance_proxy
    for rule in policy.decision_precedence:
        first = rule_masks[rule] & primary.isna()
        primary.loc[first] = rule
        proxy_class.loc[first] = outcomes[rule]
    if primary.isna().any() or proxy_class.isna().any():
        raise IgnRoadVehicleProxyApplicationError(
            "Every normalized IGN road must receive one primary policy result"
        )

    policy_trace_masks = tuple(
        (rule, rule_masks[rule]) for rule in policy.decision_precedence
    )
    trace = _json_array_from_masks(
        index,
        ((_TECHNICAL_GEOMETRY_RULE, technical_geometry), *policy_trace_masks),
    )
    unknown_fields = _json_array_from_masks(
        index,
        tuple((field, unknown_masks[field]) for field in _UNKNOWN_FIELD_ORDER),
    )

    output["road_proxy_primary_rule"] = primary
    output["road_proxy_class"] = proxy_class
    output["road_proxy_rule_trace_json"] = trace
    output["road_proxy_unknown_fields_json"] = unknown_fields
    output["road_proxy_toll_evidence"] = output[
        "light_vehicle_access_raw"
    ].isin(access_values.toll)
    output["road_proxy_policy_id"] = policy.policy_id
    output["road_proxy_policy_schema_version"] = policy.schema_version
    output["road_proxy_policy_config_sha256"] = policy.config_sha256
    output["road_proxy_policy_scope"] = policy.scope
    output["road_proxy_policy_evidence_checked_on"] = policy.evidence_checked_on
    output["road_proxy_vehicle_scope"] = policy.vehicle_scope
    output["road_proxy_heavy_vehicle_access"] = policy.heavy_vehicle_access

    result = gpd.GeoDataFrame(
        output.loc[:, [*source.columns, *_APPLICATION_COLUMNS]],
        geometry=source.active_geometry_name,
        crs=source.crs,
    )
    if len(result) != len(source) or not result.index.equals(source.index):
        raise IgnRoadVehicleProxyApplicationError(
            "IGN road policy application changed row count or order"
        )
    return result
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_apply_ign_road_vehicle_proxy_policy`

**Exact signature**

```python
def _apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> IgnRoadVehicleProxyApplicationResult:
```

**Purpose**

Applies the configured policy to ign road vehicle proxy policy; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnRoadVehicleProxyApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
IgnRoadVehicleProxyApplicationResult(roads=_classify_road_frame(normalized.road_segments, policy))
```

**Validation and exceptions**

- Guard with a raise path: `type(normalized) is not NormalizedIgnRoadData`.
- Explicit raise expressions: `IgnRoadVehicleProxyApplicationError('IGN road normalization returned an invalid result type')`.

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

- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::apply_ign_road_vehicle_proxy_policy` via `_apply_ign_road_vehicle_proxy_policy`.

**Complete source-ordered implementation**

```python
def _apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> IgnRoadVehicleProxyApplicationResult:
    normalized = normalize_ign_roads(source, source_config)
    if type(normalized) is not NormalizedIgnRoadData:
        raise IgnRoadVehicleProxyApplicationError(
            "IGN road normalization returned an invalid result type"
        )
    policy = (
        load_ign_road_vehicle_proxy_policy()
        if policy_path is None
        else load_ign_road_vehicle_proxy_policy(policy_path)
    )
    return IgnRoadVehicleProxyApplicationResult(
        roads=_classify_road_frame(normalized.road_segments, policy)
    )
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `apply_ign_road_vehicle_proxy_policy`

**Exact signature**

```python
def apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
```

**Purpose**

Source-completely normalize roads and apply the exact policy bytes once.

**Return contract**

- Declared return annotation: `IgnRoadVehicleProxyApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
_apply_ign_road_vehicle_proxy_policy(source, source_config, policy_path)
```

**Validation and exceptions**

- Guard with a raise path: `type(source) is not IgnBdTopoRoadData`.
- Guard with a raise path: `type(source_config) is not IgnBdTopoSourceConfig`.
- Guard with a raise path: `policy_path is not None and (not isinstance(policy_path, Path))`.
- Explicit raise expressions: `IgnRoadVehicleProxyApplicationError('IGN road vehicle-proxy policy cannot be applied safely')`, `TypeError('policy_path must be a pathlib.Path or None')`, `TypeError('source must be an IgnBdTopoRoadData')`, `TypeError('source_config must be an IgnBdTopoSourceConfig')`, `re-raise`.

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

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `apply_ign_road_vehicle_proxy_policy`.
- import/re-export: `src/landscout/stages/enrich_road_proximity.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` via `apply_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error` via `apply_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_config_type_has_controlled_error` via `apply_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` via `apply_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` via `apply_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` via `apply_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` via `apply_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `apply_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` via `apply_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_config_is_exact_pydantic_type` via `apply_ign_road_vehicle_proxy_policy`.
- import/re-export: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`.

**Complete source-ordered implementation**

```python
def apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
    """Source-completely normalize roads and apply the exact policy bytes once."""

    try:
        if type(source) is not IgnBdTopoRoadData:
            raise TypeError("source must be an IgnBdTopoRoadData")
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise TypeError("source_config must be an IgnBdTopoSourceConfig")
        if policy_path is not None and not isinstance(policy_path, Path):
            raise TypeError("policy_path must be a pathlib.Path or None")
        return _apply_ign_road_vehicle_proxy_policy(
            source, source_config, policy_path
        )
    except IgnRoadVehicleProxyApplicationError:
        raise
    except Exception as error:
        raise IgnRoadVehicleProxyApplicationError(
            "IGN road vehicle-proxy policy cannot be applied safely"
        ) from error
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.


## 7. Data contracts

### Frame-preservation and semantic notes

- All normalized road columns pass through unchanged. Only `road_proxy_*` evidence columns are appended. Policy rule names and class values are values in those columns, not additional columns.
- `road_proxy_heavy_vehicle_access=NOT_PROVEN` is explicit unresolved evidence and never claims truck, legal, or BESS access.
- `OPEN_OR_TOLL` and `UNKNOWN` are keys in the internal policy-rule mask mapping and values in evidence traces; neither is a DataFrame column.

### `_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
_REQUIRED_COLUMNS = frozenset(
    {
        "geometry_status",
        "geometry",
        *_UNKNOWN_FIELD_ORDER,
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `carriageway_width_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `closure_period_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `fictitious_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 6 | `geometry_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 7 | `importance_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `light_vehicle_access_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `private_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `restriction_nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `_APPLICATION_COLUMNS` — canonical or derived frame-column schema

```python
_APPLICATION_COLUMNS = (
    "road_proxy_primary_rule",
    "road_proxy_class",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_policy_scope",
    "road_proxy_policy_evidence_checked_on",
    "road_proxy_vehicle_scope",
    "road_proxy_heavy_vehicle_access",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `road_proxy_primary_rule` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 2 | `road_proxy_class` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 3 | `road_proxy_rule_trace_json` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `road_proxy_unknown_fields_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `road_proxy_toll_evidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `road_proxy_policy_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 7 | `road_proxy_policy_schema_version` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `road_proxy_policy_config_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 9 | `road_proxy_policy_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `road_proxy_policy_evidence_checked_on` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `road_proxy_vehicle_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `road_proxy_heavy_vehicle_access` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `IgnRoadVehicleProxyApplicationError` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_road_vehicle_proxy_policy.py`` | yes |
| `IgnRoadVehicleProxyApplicationResult` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_road_vehicle_proxy_policy.py`` | yes |
| `apply_ign_road_vehicle_proxy_policy` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_road_vehicle_proxy_policy.py`` | yes |

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

The module contributes to the road flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
