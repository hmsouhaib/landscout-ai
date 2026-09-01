# `src/landscout/common/strict_json.py`

## File identity

- Repository path: `src/landscout/common/strict_json.py`
- File type: Python source
- Layer: internal common contract
- Domain: shared validation and schema contracts
- Responsibility: Decodes trust-bearing JSON with strict UTF-8, duplicate-key, finite-number, overflow, and object-root enforcement.
- Source SHA256: `c214bbca0260bdfe035f056ad533c4198099b68c1970b6271657baa13ca23ecf`

## 1. STEP 7F.1A.4 contract delta

- Introduces the single strict trust-bearing JSON decoder: strict UTF-8, duplicate-key rejection, finite/representable numeric values, and optional exact object-root enforcement.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Decodes trust-bearing JSON with strict UTF-8, duplicate-key, finite-number, overflow, and object-root enforcement.

The file belongs to the **internal common contract** layer and **shared validation and schema contracts** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `from math import isfinite`
- `from typing import Any`

### Third-party packages

- None.

### Internal LandScout imports

- None.

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

No module-level constant, alias, schema, mapping, or meaningful dunder assignment is declared.

### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `StrictJsonError`

**Source purpose:** Raised when a trust-bearing JSON document is not deterministic.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- constructor call: `landscout.common.strict_json::_unique_object` via `StrictJsonError`
- value/type reference: `landscout.common.strict_json::_unique_object` via `StrictJsonError`
- constructor call: `landscout.common.strict_json::_finite_float` via `StrictJsonError`
- value/type reference: `landscout.common.strict_json::_finite_float` via `StrictJsonError`
- constructor call: `landscout.common.strict_json::_reject_constant` via `StrictJsonError`
- value/type reference: `landscout.common.strict_json::_reject_constant` via `StrictJsonError`
- constructor call: `landscout.common.strict_json::loads_strict_json` via `StrictJsonError`
- value/type reference: `landscout.common.strict_json::loads_strict_json` via `StrictJsonError`
- constructor call: `landscout.common.strict_json::loads_strict_json_object` via `StrictJsonError`
- value/type reference: `landscout.common.strict_json::loads_strict_json_object` via `StrictJsonError`
- import: `landscout.sources.gpu_fr::<module>` via `from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)`
- value/type reference: `landscout.sources.gpu_fr::_request_json` via `StrictJsonError`
- value/type reference: `landscout.sources.gpu_fr::_load_cached_archive` via `StrictJsonError`
- value/type reference: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `StrictJsonError`
- import: `landscout.sources.rte_odre_fr::<module>` via `from landscout.common.strict_json import StrictJsonError, loads_strict_json_object`
- value/type reference: `landscout.sources.rte_odre_fr::_read_response_json` via `StrictJsonError`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_geojson` via `StrictJsonError`
- import: `tests.unit.test_strict_serialization::<module>` via `from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_json_rejects_nested_duplicate_object_keys` via `StrictJsonError`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_json_rejects_every_nonfinite_number` via `StrictJsonError`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_json_rejects_malformed_utf8` via `StrictJsonError`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_json_object_requires_an_object_top_level` via `StrictJsonError`

**Exact class source**

```python
class StrictJsonError(ValueError):
    """Raised when a trust-bearing JSON document is not deterministic."""
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_unique_object`

**Purpose:** Implements `unique object` within the file role: Decodes trust-bearing JSON with strict UTF-8, duplicate-key, finite-number, overflow, and object-root enforcement.

**Exact signature**

```python
def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, Any]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `pairs` | positional-or-keyword | `list[tuple[str, Any]]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `StrictJsonError(f"Duplicate JSON key: {key}")` under lexical guard `key in result`.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `landscout.common.strict_json::loads_strict_json` via `_unique_object`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `StrictJsonError` | `landscout.common.strict_json.StrictJsonError` |

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
| In-memory mutation | `result[key] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJsonError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_finite_float`

**Purpose:** Implements `finite float` within the file role: Decodes trust-bearing JSON with strict UTF-8, duplicate-key, finite-number, overflow, and object-root enforcement.

**Exact signature**

```python
def _finite_float(value: str) -> float:
```

- Exact decorators: none.
- Declared return annotation: `float`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `parsed`
- Explicit raise paths:
  - `StrictJsonError("JSON number must be finite")` under lexical guard `not isfinite(parsed)`.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `landscout.common.strict_json::loads_strict_json` via `_finite_float`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |
| `StrictJsonError` | `landscout.common.strict_json.StrictJsonError` |

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
def _finite_float(value: str) -> float:
    parsed = float(value)
    if not isfinite(parsed):
        raise StrictJsonError("JSON number must be finite")
    return parsed
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_reject_constant`

**Purpose:** Implements `reject constant` within the file role: Decodes trust-bearing JSON with strict UTF-8, duplicate-key, finite-number, overflow, and object-root enforcement.

**Exact signature**

```python
def _reject_constant(value: str) -> float:
```

- Exact decorators: none.
- Declared return annotation: `float`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `StrictJsonError(f"JSON number must be finite: {value}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `landscout.common.strict_json::loads_strict_json` via `_reject_constant`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `StrictJsonError` | `landscout.common.strict_json.StrictJsonError` |

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
def _reject_constant(value: str) -> float:
    raise StrictJsonError(f"JSON number must be finite: {value}")
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `loads_strict_json`

**Purpose:** Parse strict UTF-8 JSON without duplicate keys or non-finite numbers.

**Exact signature**

```python
def loads_strict_json(value: str | bytes) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str \| bytes` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `json.loads(<br>            document,<br>            object_pairs_hook=_unique_object,<br>            parse_constant=_reject_constant,<br>            parse_float=_finite_float,<br>        )`
- Explicit raise paths:
  - `StrictJsonError("JSON document is not valid UTF-8")` under lexical guard `type(value) is bytes`.
  - `StrictJsonError("JSON input must be an exact string or bytes")` under lexical guard `type(value) is bytes`.
  - `re-raise`.
  - `StrictJsonError("JSON document is invalid")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.strict_json::loads_strict_json_object` via `loads_strict_json`
- value/type reference: `landscout.common.strict_json::loads_strict_json_object` via `loads_strict_json`
- import: `landscout.sources.gpu_fr::<module>` via `from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)`
- direct call: `landscout.sources.gpu_fr::_request_json` via `loads_strict_json`
- value/type reference: `landscout.sources.gpu_fr::_request_json` via `loads_strict_json`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.common.strict_json import loads_strict_json, loads_strict_json_object`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_json_ids` via `loads_strict_json`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_json_ids` via `loads_strict_json`
- import: `tests.unit.test_strict_serialization::<module>` via `from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)`
- direct call: `tests.unit.test_strict_serialization::test_strict_json_rejects_nested_duplicate_object_keys` via `loads_strict_json`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_json_rejects_nested_duplicate_object_keys` via `loads_strict_json`
- direct call: `tests.unit.test_strict_serialization::test_strict_json_rejects_every_nonfinite_number` via `loads_strict_json`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_json_rejects_every_nonfinite_number` via `loads_strict_json`
- direct call: `tests.unit.test_strict_serialization::test_strict_json_rejects_malformed_utf8` via `loads_strict_json`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_json_rejects_malformed_utf8` via `loads_strict_json`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.decode` | `unresolved local/third-party receiver; no ownership inferred` |
| `StrictJsonError` | `landscout.common.strict_json.StrictJsonError` |
| `json.loads` | `json.loads` |

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
def loads_strict_json(value: str | bytes) -> object:
    """Parse strict UTF-8 JSON without duplicate keys or non-finite numbers."""

    if type(value) is bytes:
        try:
            document = value.decode("utf-8")
        except UnicodeDecodeError as error:
            raise StrictJsonError("JSON document is not valid UTF-8") from error
    elif type(value) is str:
        document = value
    else:
        raise StrictJsonError("JSON input must be an exact string or bytes")
    try:
        return json.loads(
            document,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except StrictJsonError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as error:
        raise StrictJsonError("JSON document is invalid") from error
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `loads_strict_json_object`

**Purpose:** Parse a strict JSON document whose top-level value must be an object.

**Exact signature**

```python
def loads_strict_json_object(value: str | bytes) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str \| bytes` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `payload`
- Explicit raise paths:
  - `StrictJsonError("JSON document must contain one top-level object")` under lexical guard `type(payload) is not dict`.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.sources.cadastre_fr::<module>` via `from landscout.common.strict_json import loads_strict_json_object`
- direct call: `landscout.sources.cadastre_fr::_load_cached_download` via `loads_strict_json_object`
- value/type reference: `landscout.sources.cadastre_fr::_load_cached_download` via `loads_strict_json_object`
- import: `landscout.sources.gpu_fr::<module>` via `from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)`
- direct call: `landscout.sources.gpu_fr::_load_cached_archive` via `loads_strict_json_object`
- value/type reference: `landscout.sources.gpu_fr::_load_cached_archive` via `loads_strict_json_object`
- direct call: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `loads_strict_json_object`
- value/type reference: `landscout.sources.gpu_fr::_validate_extraction_manifest` via `loads_strict_json_object`
- import: `landscout.sources.ign_bdtopo_fr::<module>` via `from landscout.common.strict_json import loads_strict_json_object`
- direct call: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `loads_strict_json_object`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `loads_strict_json_object`
- direct call: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `loads_strict_json_object`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `loads_strict_json_object`
- direct call: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `loads_strict_json_object`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `loads_strict_json_object`
- import: `landscout.sources.inpn_protected_areas_fr::<module>` via `from landscout.common.strict_json import loads_strict_json_object`
- direct call: `landscout.sources.inpn_protected_areas_fr::_read_strict_json` via `loads_strict_json_object`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_read_strict_json` via `loads_strict_json_object`
- import: `landscout.sources.rte_odre_fr::<module>` via `from landscout.common.strict_json import StrictJsonError, loads_strict_json_object`
- direct call: `landscout.sources.rte_odre_fr::_read_response_json` via `loads_strict_json_object`
- value/type reference: `landscout.sources.rte_odre_fr::_read_response_json` via `loads_strict_json_object`
- direct call: `landscout.sources.rte_odre_fr::_validate_geojson` via `loads_strict_json_object`
- value/type reference: `landscout.sources.rte_odre_fr::_validate_geojson` via `loads_strict_json_object`
- direct call: `landscout.sources.rte_odre_fr::_load_cached_download` via `loads_strict_json_object`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `loads_strict_json_object`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.common.strict_json import loads_strict_json, loads_strict_json_object`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `loads_strict_json_object`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `loads_strict_json_object`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.common.strict_json import loads_strict_json_object`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `loads_strict_json_object`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `loads_strict_json_object`
- import: `landscout.stages.bess_planning_feature_policy::<module>` via `from landscout.common.strict_json import loads_strict_json_object`
- direct call: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_artifacts` via `loads_strict_json_object`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_artifacts` via `loads_strict_json_object`
- import: `tests.unit.test_aggregate_bess_planning_feature_policy::<module>` via `from landscout.common.strict_json import loads_strict_json_object`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_load_legacy_local_aggregation_artifacts` via `loads_strict_json_object`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_load_legacy_local_aggregation_artifacts` via `loads_strict_json_object`
- import: `tests.unit.test_strict_serialization::<module>` via `from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)`
- direct call: `tests.unit.test_strict_serialization::test_strict_json_object_requires_an_object_top_level` via `loads_strict_json_object`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_json_object_requires_an_object_top_level` via `loads_strict_json_object`
- direct call: `tests.unit.test_strict_serialization::test_strict_json_object_accepts_an_exact_object` via `loads_strict_json_object`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_json_object_accepts_an_exact_object` via `loads_strict_json_object`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_json` | `landscout.common.strict_json.loads_strict_json` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `StrictJsonError` | `landscout.common.strict_json.StrictJsonError` |

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
def loads_strict_json_object(value: str | bytes) -> dict[str, object]:
    """Parse a strict JSON document whose top-level value must be an object."""

    payload = loads_strict_json(value)
    if type(payload) is not dict:
        raise StrictJsonError("JSON document must contain one top-level object")
    return payload
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: none at module scope.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Small deterministic JSON reader for trust-bearing repository inputs."""

from __future__ import annotations

import json
from math import isfinite
from typing import Any


class StrictJsonError(ValueError):
    """Raised when a trust-bearing JSON document is not deterministic."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJsonError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not isfinite(parsed):
        raise StrictJsonError("JSON number must be finite")
    return parsed


def _reject_constant(value: str) -> float:
    raise StrictJsonError(f"JSON number must be finite: {value}")


def loads_strict_json(value: str | bytes) -> object:
    """Parse strict UTF-8 JSON without duplicate keys or non-finite numbers."""

    if type(value) is bytes:
        try:
            document = value.decode("utf-8")
        except UnicodeDecodeError as error:
            raise StrictJsonError("JSON document is not valid UTF-8") from error
    elif type(value) is str:
        document = value
    else:
        raise StrictJsonError("JSON input must be an exact string or bytes")
    try:
        return json.loads(
            document,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except StrictJsonError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as error:
        raise StrictJsonError("JSON document is invalid") from error


def loads_strict_json_object(value: str | bytes) -> dict[str, object]:
    """Parse a strict JSON document whose top-level value must be an object."""

    payload = loads_strict_json(value)
    if type(payload) is not dict:
        raise StrictJsonError("JSON document must contain one top-level object")
    return payload
```
