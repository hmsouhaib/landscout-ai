# `src/landscout/stages/apply_road_vehicle_proxy_policy.py`

## File identity

- Repository path: `src/landscout/stages/apply_road_vehicle_proxy_policy.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.
- Source SHA256: `09d3aee41ca6878faba39e2f3165dce174f22fa64014913edc281ce6c3458b4c`

## 1. STEP 7F.1A.4 contract delta

- Revalidates the immutable source/policy inputs at the public application boundary while preserving factual rows and policy precedence.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "IgnRoadVehicleProxyApplicationError",
    "IgnRoadVehicleProxyApplicationResult",
    "apply_ign_road_vehicle_proxy_policy",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `IgnRoadVehicleProxyApplicationError`
  - `IgnRoadVehicleProxyApplicationResult`
  - `apply_ign_road_vehicle_proxy_policy`

### `_GEOMETRY_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_TECHNICAL_GEOMETRY_RULE`

- Category: module constant or closed domain.
- Exact declaration:

```python
_TECHNICAL_GEOMETRY_RULE = "SOURCE_GEOMETRY_NOT_VALID"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_CRITICAL_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `fictitious_raw`
  - `asset_status_raw`
  - `nature_raw`
  - `light_vehicle_access_raw`
  - `private_raw`
  - `importance_raw`

### `_UNKNOWN_FIELD_ORDER`

- Category: module constant or closed domain.
- Exact declaration:

```python
_UNKNOWN_FIELD_ORDER = (
    *_CRITICAL_FIELDS,
    "carriageway_width_raw",
    "closure_period_raw",
    "restriction_nature_raw",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_REQUIRED_COLUMNS = frozenset(
    {
        "geometry_status",
        "geometry",
        *_UNKNOWN_FIELD_ORDER,
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_APPLICATION_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `road_proxy_primary_rule`
  - `road_proxy_class`
  - `road_proxy_rule_trace_json`
  - `road_proxy_unknown_fields_json`
  - `road_proxy_toll_evidence`
  - `road_proxy_policy_id`
  - `road_proxy_policy_schema_version`
  - `road_proxy_policy_config_sha256`
  - `road_proxy_policy_scope`
  - `road_proxy_policy_evidence_checked_on`
  - `road_proxy_vehicle_scope`
  - `road_proxy_heavy_vehicle_access`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `IgnRoadVehicleProxyApplicationError`

**Source purpose:** Raised when factual roads cannot receive the approved policy safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- constructor call: `landscout.stages.apply_road_vehicle_proxy_policy::_validate_normalized_frame` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_validate_normalized_frame` via `IgnRoadVehicleProxyApplicationError`
- constructor call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `IgnRoadVehicleProxyApplicationError`
- constructor call: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationError`
- constructor call: `landscout.stages.apply_road_vehicle_proxy_policy::apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationError`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_wrong_source_type_has_controlled_error` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_wrong_source_config_type_has_controlled_error` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_malformed_policy_path_has_controlled_error` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalization_failure_stops_policy_loading` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_generated_policy_column_collision_fails_before_policy_loading` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_unknown_geometry_status_is_rejected` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_path_must_be_path_or_none` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_config_is_exact_pydantic_type` via `IgnRoadVehicleProxyApplicationError`
- import: `tests.unit.test_enrich_road_proximity::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
)`
- constructor call: `tests.unit.test_enrich_road_proximity::test_application_failure_stops_proximity` via `IgnRoadVehicleProxyApplicationError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_failure_stops_proximity` via `IgnRoadVehicleProxyApplicationError`

**Exact class source**

```python
class IgnRoadVehicleProxyApplicationError(ValueError):
    """Raised when factual roads cannot receive the approved policy safely."""
```

### `IgnRoadVehicleProxyApplicationResult`

**Source purpose:** Normalized factual roads plus deterministic general-car proxy evidence.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `roads` | `gpd.GeoDataFrame` | `required` | `roads: gpd.GeoDataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- constructor call: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationResult`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationResult`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::apply_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyApplicationResult`
- import: `landscout.stages.enrich_road_proximity::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `IgnRoadVehicleProxyApplicationResult`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::_apply` via `IgnRoadVehicleProxyApplicationResult`
- import: `tests.unit.test_enrich_road_proximity::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
)`
- constructor call: `tests.unit.test_enrich_road_proximity::_enrich` via `IgnRoadVehicleProxyApplicationResult`
- value/type reference: `tests.unit.test_enrich_road_proximity::_enrich` via `IgnRoadVehicleProxyApplicationResult`
- constructor call: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `IgnRoadVehicleProxyApplicationResult`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `IgnRoadVehicleProxyApplicationResult`
- constructor call: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `IgnRoadVehicleProxyApplicationResult`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `IgnRoadVehicleProxyApplicationResult`

**Exact class source**

```python
class IgnRoadVehicleProxyApplicationResult:
    """Normalized factual roads plus deterministic general-car proxy evidence."""

    roads: gpd.GeoDataFrame
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_false_mask`

**Purpose:** Implements `false mask` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _false_mask(index: pd.Index) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `pd.Index` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.Series(False, index=index, dtype="bool")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_strict_boolean_masks` via `_false_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_strict_boolean_masks` via `_false_mask`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_strict_private_masks` via `_false_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_strict_private_masks` via `_false_mask`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_exact_string_mask` via `_false_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_exact_string_mask` via `_false_mask`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_width_masks` via `_false_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_width_masks` via `_false_mask`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_json_array_from_masks` via `_false_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_json_array_from_masks` via `_false_mask`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_false_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_false_mask`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _false_mask(index: pd.Index) -> pd.Series:
    return pd.Series(False, index=index, dtype="bool")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_object_scalar_mask`

**Purpose:** Apply a strict scalar type gate only for heterogeneous object fixtures.

**Exact signature**

```python
def _object_scalar_mask(
    series: pd.Series,
    predicate: Callable[[object], bool],
) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |
| `predicate` | positional-or-keyword | `Callable[[object], bool]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.Series(np.asarray(values, dtype=bool), index=series.index)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_strict_boolean_masks` via `_object_scalar_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_strict_boolean_masks` via `_object_scalar_mask`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_strict_private_masks` via `_object_scalar_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_strict_private_masks` via `_object_scalar_mask`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_width_masks` via `_object_scalar_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_width_masks` via `_object_scalar_mask`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `np.frompyfunc` | `numpy.frompyfunc` |
| `function` | `unresolved local/third-party receiver; no ownership inferred` |
| `series.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `np.asarray` | `numpy.asarray` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_strict_numeric_scalar`

**Purpose:** Implements `is strict numeric scalar` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _is_strict_numeric_scalar(value: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `type(value) in {int, float} or (<br>        isinstance(value, (np.integer, np.floating)) and not isinstance(value, np.bool_)<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_is_strict_binary_numeric` via `_is_strict_numeric_scalar`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_is_strict_binary_numeric` via `_is_strict_numeric_scalar`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_is_strict_positive_numeric` via `_is_strict_numeric_scalar`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_is_strict_positive_numeric` via `_is_strict_numeric_scalar`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _is_strict_numeric_scalar(value: object) -> bool:
    return type(value) in {int, float} or (
        isinstance(value, (np.integer, np.floating)) and not isinstance(value, np.bool_)
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_strict_binary_numeric`

**Purpose:** Implements `is strict binary numeric` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _is_strict_binary_numeric(value: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `False`
  - `math.isfinite(numeric) and numeric in {0.0, 1.0}`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_strict_private_masks` via `_is_strict_binary_numeric`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_strict_numeric_scalar` | `landscout.stages.apply_road_vehicle_proxy_policy._is_strict_numeric_scalar` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `cast` | `typing.cast` |
| `math.isfinite` | `math.isfinite` |

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
def _is_strict_binary_numeric(value: object) -> bool:
    if not _is_strict_numeric_scalar(value):
        return False
    numeric = float(cast(Any, value))
    return math.isfinite(numeric) and numeric in {0.0, 1.0}
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_strict_positive_numeric`

**Purpose:** Implements `is strict positive numeric` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _is_strict_positive_numeric(value: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `False`
  - `math.isfinite(numeric) and numeric > 0`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_width_masks` via `_is_strict_positive_numeric`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_strict_numeric_scalar` | `landscout.stages.apply_road_vehicle_proxy_policy._is_strict_numeric_scalar` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `cast` | `typing.cast` |
| `math.isfinite` | `math.isfinite` |

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
def _is_strict_positive_numeric(value: object) -> bool:
    if not _is_strict_numeric_scalar(value):
        return False
    numeric = float(cast(Any, value))
    return math.isfinite(numeric) and numeric > 0
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_boolean_masks`

**Purpose:** Implements `strict boolean masks` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _strict_boolean_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[pd.Series, pd.Series, pd.Series]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `known, true, false`
  - `known, known.copy(), known.copy()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_strict_boolean_masks`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_strict_boolean_masks`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `is_bool_dtype` | `pandas.api.types.is_bool_dtype` |
| `series.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `series.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_object_scalar_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._object_scalar_mask` |
| `_false_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._false_mask` |
| `known.copy` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_private_masks`

**Purpose:** Implements `strict private masks` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _strict_private_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series, pd.Series]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[pd.Series, pd.Series, pd.Series]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `known, known & series.eq(True), known & series.eq(False)`
  - `known, known & series.eq(1), known & series.eq(0)`
  - `known, true, false`
  - `known, known.copy(), known.copy()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_strict_private_masks`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_strict_private_masks`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `is_bool_dtype` | `pandas.api.types.is_bool_dtype` |
| `series.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `series.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `is_numeric_dtype` | `pandas.api.types.is_numeric_dtype` |
| `pd.to_numeric` | `pandas.to_numeric` |
| `pd.Series` | `pandas.Series` |
| `np.isfinite` | `numpy.isfinite` |
| `numeric.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_object_scalar_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._object_scalar_mask` |
| `_false_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._false_mask` |
| `known.copy` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_exact_string_mask`

**Purpose:** Implements `exact string mask` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _exact_string_mask(series: pd.Series) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_false_mask(series.index)`
  - `series.notna() & stripped.notna() & stripped.ne("") & series.eq(stripped)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_known_string_masks` via `_exact_string_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_known_string_masks` via `_exact_string_mask`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_optional_exact_string_masks` via `_exact_string_mask`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_optional_exact_string_masks` via `_exact_string_mask`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_false_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._false_mask` |
| `series.str.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `series.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `stripped.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `stripped.ne` | `unresolved local/third-party receiver; no ownership inferred` |
| `series.eq` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _exact_string_mask(series: pd.Series) -> pd.Series:
    if not (isinstance(series.dtype, pd.StringDtype) or series.dtype == "object"):
        return _false_mask(series.index)
    stripped = series.str.strip()
    return series.notna() & stripped.notna() & stripped.ne("") & series.eq(stripped)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_known_string_masks`

**Purpose:** Implements `known string masks` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _known_string_masks(
    series: pd.Series,
    known_values: frozenset[str],
) -> tuple[pd.Series, pd.Series]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[pd.Series, pd.Series]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |
| `known_values` | positional-or-keyword | `frozenset[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `known, ~known`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_known_string_masks`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_known_string_masks`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_exact_string_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._exact_string_mask` |
| `series.isin` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _known_string_masks(
    series: pd.Series,
    known_values: frozenset[str],
) -> tuple[pd.Series, pd.Series]:
    exact = _exact_string_mask(series)
    known = exact & series.isin(known_values)
    return known, ~known
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_optional_exact_string_masks`

**Purpose:** Implements `optional exact string masks` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _optional_exact_string_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[pd.Series, pd.Series]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `exact_present, invalid`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_optional_exact_string_masks`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_optional_exact_string_masks`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `series.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_string_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._exact_string_mask` |

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
def _optional_exact_string_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series]:
    missing = series.isna()
    exact_present = _exact_string_mask(series)
    invalid = ~missing & ~exact_present
    return exact_present, invalid
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_width_masks`

**Purpose:** Implements `width masks` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _width_masks(
    series: pd.Series,
    threshold: float,
) -> tuple[pd.Series, pd.Series]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[pd.Series, pd.Series]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |
| `threshold` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `narrow, ~valid`
  - `narrow, ~missing & ~numeric`
  - `_false_mask(series.index), ~missing`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_width_masks`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_width_masks`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `series.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `is_numeric_dtype` | `pandas.api.types.is_numeric_dtype` |
| `is_bool_dtype` | `pandas.api.types.is_bool_dtype` |
| `series.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `np.isfinite` | `numpy.isfinite` |
| `series.lt` | `unresolved local/third-party receiver; no ownership inferred` |
| `_object_scalar_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._object_scalar_mask` |
| `pd.to_numeric` | `pandas.to_numeric` |
| `series.where` | `unresolved local/third-party receiver; no ownership inferred` |
| `numeric_values.lt` | `unresolved local/third-party receiver; no ownership inferred` |
| `_false_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._false_mask` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_json_array_from_masks`

**Purpose:** Implements `json array from masks` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _json_array_from_masks(
    index: pd.Index,
    ordered_masks: tuple[tuple[str, pd.Series], ...],
) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `pd.Index` | `required` |
| `ordered_masks` | positional-or-keyword | `tuple[tuple[str, pd.Series], ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output + "]"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_json_array_from_masks`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_json_array_from_masks`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.Series` | `pandas.Series` |
| `_false_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._false_mask` |
| `raw_mask.fillna(False).astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_mask.fillna` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

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
| In-memory mutation | `output.loc[mask & ~populated] += token`<br>`output.loc[mask & populated] += f",{token}"` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_rule_outcomes`

**Purpose:** Implements `rule outcomes` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _rule_outcomes(policy: IgnRoadVehicleProxyPolicy) -> Mapping[str, str]:
```

- Exact decorators: none.
- Declared return annotation: `Mapping[str, str]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "FICTITIOUS_GEOMETRY": outcomes.fictitious_geometry,<br>        "PROJECT_GEOMETRY_NOT_SIGNIFICANT": (outcomes.project_geometry_not_significant),<br>        "NOT_IN_SERVICE": outcomes.not_in_service,<br>        "PHYSICALLY_IMPOSSIBLE": outcomes.physically_impossible,<br>        "NON_GENERAL_VEHICLE_NATURE": outcomes.non_general_vehicle_nature,<br>        "RIGHTS_RESTRICTED": outcomes.rights_restricted,<br>        "PRIVATE_ROAD": outcomes.private_road,<br>        "TEMPORAL_CLOSURE": outcomes.temporal_closure,<br>        "KNOWN_RESTRICTION": outcomes.known_restriction,<br>        "OTHER_RECORDED_RESTRICTION": outcomes.other_recorded_restriction,<br>        "SPECIAL_NATURE": outcomes.special_nature,<br>        "LIMITED_NATURE": outcomes.limited_nature,<br>        "IMPORTANCE_6": outcomes.importance_6,<br>        "NARROW_CARRIAGEWAY": outcomes.narrow_carriageway,<br>        "OPEN_OR_TOLL": outcomes.open_or_toll,<br>        "UNKNOWN": outcomes.unknown,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_rule_outcomes`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_rule_outcomes`

Outbound call expressions and conservative ownership:
- No calls.

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
def _rule_outcomes(policy: IgnRoadVehicleProxyPolicy) -> Mapping[str, str]:
    outcomes = policy.decision_outcomes
    return {
        "FICTITIOUS_GEOMETRY": outcomes.fictitious_geometry,
        "PROJECT_GEOMETRY_NOT_SIGNIFICANT": (outcomes.project_geometry_not_significant),
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_normalized_frame`

**Purpose:** Implements `validate normalized frame` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _validate_normalized_frame(frame: object) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `IgnRoadVehicleProxyApplicationError(<br>            "Normalized IGN roads must be a GeoDataFrame"<br>        )` under lexical guard `not isinstance(frame, gpd.GeoDataFrame)`.
  - `IgnRoadVehicleProxyApplicationError(<br>            "Normalized IGN road columns must not contain duplicates"<br>        )` under lexical guard `frame.columns.duplicated().any()`.
  - `IgnRoadVehicleProxyApplicationError(<br>            "Normalized IGN roads are missing policy input columns: "<br>            + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `IgnRoadVehicleProxyApplicationError(<br>            "Normalized IGN roads collide with generated policy columns: "<br>            + ", ".join(sorted(collisions))<br>        )` under lexical guard `collisions`.
  - `IgnRoadVehicleProxyApplicationError(<br>            "Normalized IGN roads require active geometry and CRS"<br>        )` under lexical guard `frame.active_geometry_name != "geometry" or frame.crs is None`.
  - `IgnRoadVehicleProxyApplicationError(<br>            "Normalized IGN roads must retain a RangeIndex"<br>        )` under lexical guard `not isinstance(frame.index, pd.RangeIndex)`.
  - `IgnRoadVehicleProxyApplicationError(<br>            "Normalized IGN roads contain an impossible geometry_status"<br>        )` under lexical guard `statuses.isna().any() or not set(statuses.unique()).issubset(_GEOMETRY_STATUSES)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_validate_normalized_frame`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `_validate_normalized_frame`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `_validate_normalized_frame`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `_validate_normalized_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadVehicleProxyApplicationError` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationError` |
| `frame.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(statuses.unique()).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.unique` | `unresolved local/third-party receiver; no ownership inferred` |

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
    collisions = set(_APPLICATION_COLUMNS) & set(frame.columns)
    if collisions:
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads collide with generated policy columns: "
            + ", ".join(sorted(collisions))
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
    if statuses.isna().any() or not set(statuses.unique()).issubset(_GEOMETRY_STATUSES):
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads contain an impossible geometry_status"
        )
    return frame
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_classify_road_frame`

**Purpose:** Implements `classify road frame` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _classify_road_frame(
    normalized: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `normalized` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `IgnRoadVehicleProxyApplicationError(<br>            "Compiled policy precedence and outcomes do not agree"<br>        )` under lexical guard `set(outcomes) != set(policy.decision_precedence)`.
  - `IgnRoadVehicleProxyApplicationError(<br>            "Every normalized IGN road must receive one primary policy result"<br>        )` under lexical guard `primary.isna().any() or proxy_class.isna().any()`.
  - `IgnRoadVehicleProxyApplicationError(<br>            "IGN road policy application changed row count or order"<br>        )` under lexical guard `len(result) != len(source) or not result.index.equals(source.index)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `_classify_road_frame`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `_classify_road_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_normalized_frame` | `landscout.stages.apply_road_vehicle_proxy_policy._validate_normalized_frame` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["geometry_status"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_boolean_masks` | `landscout.stages.apply_road_vehicle_proxy_policy._strict_boolean_masks` |
| `_strict_private_masks` | `landscout.stages.apply_road_vehicle_proxy_policy._strict_private_masks` |
| `frozenset` | `unresolved local/third-party receiver; no ownership inferred` |
| `_known_string_masks` | `landscout.stages.apply_road_vehicle_proxy_policy._known_string_masks` |
| `_optional_exact_string_masks` | `landscout.stages.apply_road_vehicle_proxy_policy._optional_exact_string_masks` |
| `output["restriction_nature_raw"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `_width_masks` | `landscout.stages.apply_road_vehicle_proxy_policy._width_masks` |
| `_false_mask` | `landscout.stages.apply_road_vehicle_proxy_policy._false_mask` |
| `unknown_masks.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `mask.fillna` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["asset_status_raw"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["light_vehicle_access_raw"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["nature_raw"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["importance_raw"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `rule_masks.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `mask.fillna(False).astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `rule_masks.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rule_outcomes` | `landscout.stages.apply_road_vehicle_proxy_policy._rule_outcomes` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadVehicleProxyApplicationError` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationError` |
| `pd.Series` | `pandas.Series` |
| `primary.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `primary.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `proxy_class.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `proxy_class.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_json_array_from_masks` | `landscout.stages.apply_road_vehicle_proxy_policy._json_array_from_masks` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `output["geometry_status"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `rule_masks["OPEN_OR_TOLL"] = open_or_toll`<br>`rule_masks["UNKNOWN"] = unknown_any \| ~determined`<br>`primary.loc[technical_geometry] = _TECHNICAL_GEOMETRY_RULE`<br>`proxy_class.loc[technical_geometry] = policy.classes.not_distance_proxy`<br>`primary.loc[first] = rule`<br>`proxy_class.loc[first] = outcomes[rule]`<br>`output["road_proxy_primary_rule"] = primary`<br>`output["road_proxy_class"] = proxy_class`<br>`output["road_proxy_rule_trace_json"] = trace`<br>`output["road_proxy_unknown_fields_json"] = unknown_fields`<br>`output["road_proxy_toll_evidence"] = output["light_vehicle_access_raw"].isin(<br>        access_values.toll<br>    )`<br>`output["road_proxy_policy_id"] = policy.policy_id`<br>`output["road_proxy_policy_schema_version"] = policy.schema_version`<br>`output["road_proxy_policy_config_sha256"] = policy.config_sha256`<br>`output["road_proxy_policy_scope"] = policy.scope`<br>`output["road_proxy_policy_evidence_checked_on"] = policy.evidence_checked_on`<br>`output["road_proxy_vehicle_scope"] = policy.vehicle_scope`<br>`output["road_proxy_heavy_vehicle_access"] = policy.heavy_vehicle_access` |
| Direct parameter mutation | None directly present. |

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
    restriction_known = restriction_present & output["restriction_nature_raw"].isin(
        policy.known_restriction_review
    )
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
        "LIMITED_NATURE": output["nature_raw"].isin(nature_values.limited_motor_proxy),
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
    output["road_proxy_toll_evidence"] = output["light_vehicle_access_raw"].isin(
        access_values.toll
    )
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_apply_ign_road_vehicle_proxy_policy`

**Purpose:** Implements `apply ign road vehicle proxy policy` within the file role: Applies the compiled IGN road evidence policy with strict scalar parsing, precedence, traces, and source preservation.

**Exact signature**

```python
def _apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> IgnRoadVehicleProxyApplicationResult:
```

- Exact decorators: none.
- Declared return annotation: `IgnRoadVehicleProxyApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `policy_path` | positional-or-keyword | `Path \| None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnRoadVehicleProxyApplicationResult(<br>        roads=_classify_road_frame(normalized_roads, policy)<br>    )`
- Explicit raise paths:
  - `IgnRoadVehicleProxyApplicationError(<br>            "IGN road normalization returned an invalid result type"<br>        )` under lexical guard `type(normalized) is not NormalizedIgnRoadData`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::apply_ign_road_vehicle_proxy_policy` via `_apply_ign_road_vehicle_proxy_policy`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::apply_ign_road_vehicle_proxy_policy` via `_apply_ign_road_vehicle_proxy_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadVehicleProxyApplicationError` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationError` |
| `_validate_normalized_frame` | `landscout.stages.apply_road_vehicle_proxy_policy._validate_normalized_frame` |
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `IgnRoadVehicleProxyApplicationResult` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationResult` |
| `_classify_road_frame` | `landscout.stages.apply_road_vehicle_proxy_policy._classify_road_frame` |

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
    normalized_roads = _validate_normalized_frame(normalized.road_segments)
    policy = (
        load_ign_road_vehicle_proxy_policy()
        if policy_path is None
        else load_ign_road_vehicle_proxy_policy(policy_path)
    )
    return IgnRoadVehicleProxyApplicationResult(
        roads=_classify_road_frame(normalized_roads, policy)
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `apply_ign_road_vehicle_proxy_policy`

**Purpose:** Source-completely normalize roads and apply the exact policy bytes once.

**Exact signature**

```python
def apply_ign_road_vehicle_proxy_policy(
    source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
```

- Exact decorators: none.
- Declared return annotation: `IgnRoadVehicleProxyApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `policy_path` | positional-or-keyword | `Path \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_apply_ign_road_vehicle_proxy_policy(source, source_config, policy_path)`
- Explicit raise paths:
  - `TypeError("source must be an IgnBdTopoRoadData")` under lexical guard `type(source) is not IgnBdTopoRoadData`.
  - `TypeError("source_config must be an IgnBdTopoSourceConfig")` under lexical guard `type(source_config) is not IgnBdTopoSourceConfig`.
  - `TypeError("policy_path must be a pathlib.Path or None")` under lexical guard `policy_path is not None and not isinstance(policy_path, Path)`.
  - `re-raise`.
  - `IgnRoadVehicleProxyApplicationError(<br>            "IGN road vehicle-proxy policy cannot be applied safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- import: `landscout.stages.enrich_road_proximity::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- direct call: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `apply_ign_road_vehicle_proxy_policy`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::_apply` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::_apply` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_wrong_source_type_has_controlled_error` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_wrong_source_type_has_controlled_error` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_wrong_source_config_type_has_controlled_error` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_wrong_source_config_type_has_controlled_error` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_malformed_policy_path_has_controlled_error` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_malformed_policy_path_has_controlled_error` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_complete_normalization_is_invoked_exactly_once` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_complete_normalization_is_invoked_exactly_once` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalization_failure_stops_policy_loading` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalization_failure_stops_policy_loading` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_generated_policy_column_collision_fails_before_policy_loading` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_generated_policy_column_collision_fails_before_policy_loading` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_object_is_not_mutated` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_object_is_not_mutated` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_path_must_be_path_or_none` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_path_must_be_path_or_none` via `apply_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_config_is_exact_pydantic_type` via `apply_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_config_is_exact_pydantic_type` via `apply_ign_road_vehicle_proxy_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy._apply_ign_road_vehicle_proxy_policy` |
| `IgnRoadVehicleProxyApplicationError` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationError` |

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
        return _apply_ign_road_vehicle_proxy_policy(source, source_config, policy_path)
    except IgnRoadVehicleProxyApplicationError:
        raise
    except Exception as error:
        raise IgnRoadVehicleProxyApplicationError(
            "IGN road vehicle-proxy policy cannot be applied safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `_CRITICAL_FIELDS`, `_REQUIRED_COLUMNS`, `_APPLICATION_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `IgnRoadVehicleProxyApplicationError` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationError` |
| `IgnRoadVehicleProxyApplicationResult` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationResult` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Apply the checked-in IGN general-vehicle proxy policy to factual roads."""

from __future__ import annotations

import json
import math
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pandas.api.types import (  # type: ignore[import-untyped]
    is_bool_dtype,
    is_numeric_dtype,
)

from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)
from landscout.stages.normalize_access_ign import (
    NormalizedIgnRoadData,
    normalize_ign_roads,
)
from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)

__all__ = [
    "IgnRoadVehicleProxyApplicationError",
    "IgnRoadVehicleProxyApplicationResult",
    "apply_ign_road_vehicle_proxy_policy",
]

_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
_TECHNICAL_GEOMETRY_RULE = "SOURCE_GEOMETRY_NOT_VALID"
_CRITICAL_FIELDS = (
    "fictitious_raw",
    "asset_status_raw",
    "nature_raw",
    "light_vehicle_access_raw",
    "private_raw",
    "importance_raw",
)
_UNKNOWN_FIELD_ORDER = (
    *_CRITICAL_FIELDS,
    "carriageway_width_raw",
    "closure_period_raw",
    "restriction_nature_raw",
)
_REQUIRED_COLUMNS = frozenset(
    {
        "geometry_status",
        "geometry",
        *_UNKNOWN_FIELD_ORDER,
    }
)
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


class IgnRoadVehicleProxyApplicationError(ValueError):
    """Raised when factual roads cannot receive the approved policy safely."""


@dataclass(frozen=True)
class IgnRoadVehicleProxyApplicationResult:
    """Normalized factual roads plus deterministic general-car proxy evidence."""

    roads: gpd.GeoDataFrame


def _false_mask(index: pd.Index) -> pd.Series:
    return pd.Series(False, index=index, dtype="bool")


def _object_scalar_mask(
    series: pd.Series,
    predicate: Callable[[object], bool],
) -> pd.Series:
    """Apply a strict scalar type gate only for heterogeneous object fixtures."""

    function = np.frompyfunc(predicate, 1, 1)
    values = function(series.to_numpy(dtype=object))
    return pd.Series(np.asarray(values, dtype=bool), index=series.index)


def _is_strict_numeric_scalar(value: object) -> bool:
    return type(value) in {int, float} or (
        isinstance(value, (np.integer, np.floating)) and not isinstance(value, np.bool_)
    )


def _is_strict_binary_numeric(value: object) -> bool:
    if not _is_strict_numeric_scalar(value):
        return False
    numeric = float(cast(Any, value))
    return math.isfinite(numeric) and numeric in {0.0, 1.0}


def _is_strict_positive_numeric(value: object) -> bool:
    if not _is_strict_numeric_scalar(value):
        return False
    numeric = float(cast(Any, value))
    return math.isfinite(numeric) and numeric > 0


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


def _exact_string_mask(series: pd.Series) -> pd.Series:
    if not (isinstance(series.dtype, pd.StringDtype) or series.dtype == "object"):
        return _false_mask(series.index)
    stripped = series.str.strip()
    return series.notna() & stripped.notna() & stripped.ne("") & series.eq(stripped)


def _known_string_masks(
    series: pd.Series,
    known_values: frozenset[str],
) -> tuple[pd.Series, pd.Series]:
    exact = _exact_string_mask(series)
    known = exact & series.isin(known_values)
    return known, ~known


def _optional_exact_string_masks(
    series: pd.Series,
) -> tuple[pd.Series, pd.Series]:
    missing = series.isna()
    exact_present = _exact_string_mask(series)
    invalid = ~missing & ~exact_present
    return exact_present, invalid


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


def _rule_outcomes(policy: IgnRoadVehicleProxyPolicy) -> Mapping[str, str]:
    outcomes = policy.decision_outcomes
    return {
        "FICTITIOUS_GEOMETRY": outcomes.fictitious_geometry,
        "PROJECT_GEOMETRY_NOT_SIGNIFICANT": (outcomes.project_geometry_not_significant),
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
    collisions = set(_APPLICATION_COLUMNS) & set(frame.columns)
    if collisions:
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads collide with generated policy columns: "
            + ", ".join(sorted(collisions))
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
    if statuses.isna().any() or not set(statuses.unique()).issubset(_GEOMETRY_STATUSES):
        raise IgnRoadVehicleProxyApplicationError(
            "Normalized IGN roads contain an impossible geometry_status"
        )
    return frame


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
    restriction_known = restriction_present & output["restriction_nature_raw"].isin(
        policy.known_restriction_review
    )
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
        "LIMITED_NATURE": output["nature_raw"].isin(nature_values.limited_motor_proxy),
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
    output["road_proxy_toll_evidence"] = output["light_vehicle_access_raw"].isin(
        access_values.toll
    )
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
    normalized_roads = _validate_normalized_frame(normalized.road_segments)
    policy = (
        load_ign_road_vehicle_proxy_policy()
        if policy_path is None
        else load_ign_road_vehicle_proxy_policy(policy_path)
    )
    return IgnRoadVehicleProxyApplicationResult(
        roads=_classify_road_frame(normalized_roads, policy)
    )


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
        return _apply_ign_road_vehicle_proxy_policy(source, source_config, policy_path)
    except IgnRoadVehicleProxyApplicationError:
        raise
    except Exception as error:
        raise IgnRoadVehicleProxyApplicationError(
            "IGN road vehicle-proxy policy cannot be applied safely"
        ) from error
```
