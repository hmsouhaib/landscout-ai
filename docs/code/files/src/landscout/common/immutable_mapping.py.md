# `src/landscout/common/immutable_mapping.py`

## File identity

- Repository path: `src/landscout/common/immutable_mapping.py`
- File type: Python source
- Layer: internal common contract
- Domain: shared validation and schema contracts
- Responsibility: Provides a deeply immutable mapping value for frozen decision-input configuration and policy models.
- Source SHA256: `dec349f8988a25b4b2ddbbfc5a5699171d6204525cf57f944fd9777db5c1ed3d`

## 1. STEP 7F.1A.4 contract delta

- Introduces a recursively frozen mapping value used by validated decision/configuration models so nested policy inputs cannot be mutated after validation.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides a deeply immutable mapping value for frozen decision-input configuration and policy models.

The file belongs to the **internal common contract** layer and **shared validation and schema contracts** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`

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

### `FrozenDict`

**Source purpose:** A dict-compatible value whose mutation operations always fail.

- Exact decorators: none.
- Exact bases: `dict[Key, Value]`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `__setitem__` | `inferred from assignment` | `_immutable` | `__setitem__ = _immutable` |
| `__delitem__` | `inferred from assignment` | `_immutable` | `__delitem__ = _immutable` |
| `__ior__` | `inferred from assignment` | `_immutable` | `__ior__ = _immutable` |
| `clear` | `inferred from assignment` | `_immutable` | `clear = _immutable` |
| `pop` | `inferred from assignment` | `_immutable` | `pop = _immutable` |
| `popitem` | `inferred from assignment` | `_immutable` | `popitem = _immutable` |
| `setdefault` | `inferred from assignment` | `_immutable` | `setdefault = _immutable` |
| `update` | `inferred from assignment` | `_immutable` | `update = _immutable` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.common.immutable_mapping::freeze_mapping` via `FrozenDict`
- value/type reference: `landscout.common.immutable_mapping::freeze_mapping` via `FrozenDict`

**Exact class source**

```python
class FrozenDict[Key, Value](dict[Key, Value]):
    """A dict-compatible value whose mutation operations always fail."""

    def _immutable(self, *args: object, **kwargs: object) -> None:
        del args, kwargs
        raise TypeError("frozen mapping cannot be mutated")

    __setitem__ = _immutable
    __delitem__ = _immutable
    __ior__ = _immutable  # type: ignore[assignment]
    clear = _immutable
    pop = _immutable  # type: ignore[assignment]
    popitem = _immutable  # type: ignore[assignment]
    setdefault = _immutable  # type: ignore[assignment]
    update = _immutable
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `FrozenDict._immutable`

**Purpose:** Implements `immutable` within the file role: Provides a deeply immutable mapping value for frozen decision-input configuration and policy models.

**Exact signature**

```python
def _immutable(self, *args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `TypeError("frozen mapping cannot be mutated")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _immutable(self, *args: object, **kwargs: object) -> None:
        del args, kwargs
        raise TypeError("frozen mapping cannot be mutated")
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `freeze_mapping`

**Purpose:** Copy a validated dictionary into an immutable dict-compatible value.

**Exact signature**

```python
def freeze_mapping[Key, Value](
    value: dict[Key, Value],
) -> FrozenDict[Key, Value]:
```

- Exact decorators: none.
- Declared return annotation: `FrozenDict[Key, Value]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `dict[Key, Value]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.stages.bess_planning_feature_policy::<module>` via `from landscout.common.immutable_mapping import freeze_mapping`
- direct call: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `freeze_mapping`
- value/type reference: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `freeze_mapping`
- import: `landscout.stages.structure_planning_regulation::<module>` via `from landscout.common.immutable_mapping import freeze_mapping`
- direct call: `landscout.stages.structure_planning_regulation::PlanningRegulationStructureConfig._validate_grammar` via `freeze_mapping`
- value/type reference: `landscout.stages.structure_planning_regulation::PlanningRegulationStructureConfig._validate_grammar` via `freeze_mapping`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `FrozenDict` | `landscout.common.immutable_mapping.FrozenDict` |
| `dict.update` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `dict.update(result, value)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def freeze_mapping[Key, Value](
    value: dict[Key, Value],
) -> FrozenDict[Key, Value]:
    """Copy a validated dictionary into an immutable dict-compatible value."""

    result: FrozenDict[Key, Value] = FrozenDict()
    dict.update(result, value)
    return result
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
"""Internal immutable mapping used by frozen decision-input models."""

from __future__ import annotations


class FrozenDict[Key, Value](dict[Key, Value]):
    """A dict-compatible value whose mutation operations always fail."""

    def _immutable(self, *args: object, **kwargs: object) -> None:
        del args, kwargs
        raise TypeError("frozen mapping cannot be mutated")

    __setitem__ = _immutable
    __delitem__ = _immutable
    __ior__ = _immutable  # type: ignore[assignment]
    clear = _immutable
    pop = _immutable  # type: ignore[assignment]
    popitem = _immutable  # type: ignore[assignment]
    setdefault = _immutable  # type: ignore[assignment]
    update = _immutable


def freeze_mapping[Key, Value](
    value: dict[Key, Value],
) -> FrozenDict[Key, Value]:
    """Copy a validated dictionary into an immutable dict-compatible value."""

    result: FrozenDict[Key, Value] = FrozenDict()
    dict.update(result, value)
    return result
```
