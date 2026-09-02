# `src/landscout/common/immutable_mapping.py`

## File identity

- Repository path: `src/landscout/common/immutable_mapping.py`
- File type: Python source
- Layer: production contract
- Responsibility: Provides a deeply immutable mapping value for frozen decision-input configuration and policy models.
- Source SHA256: `b79ebb5b81d466d262b12adcf7bf54816036f1a922345558cd9da54806b3e727`

## 1. STEP 7F.1A.4.2 contract delta

- Makes immutable artifact evidence fail closed on unsupported/non-canonical JSON leaves and makes FrozenDict copy/deep-copy preserve immutable identity.
- Unsupported leaves are rejected rather than retained or stringified; existing valid JSON shapes, schemas, hashes, and business boundaries remain unchanged.

## 2. Purpose and architectural position

Provides a deeply immutable mapping value for frozen decision-input configuration and policy models.

This companion is source-bound. The SHA and complete snapshot below are authoritative for this file; summaries do not replace the implementation.

## 3. Exact imports and dependencies

- `from __future__ import annotations`
- `import math`
- `from collections.abc import Iterator, Mapping`
- `from types import MappingProxyType`
- `from typing import Self, cast`

## 4. Module declarations

- None.

## 5. Classes and lexical ownership

### `FrozenDict`

- Bases: `Mapping[Key, Value]`
- Decorators: none
- Source purpose: An immutable, recursively copied mapping with no mutable backing alias.
- Direct field/assignment count: 10
  - `__slots__ = ("_data",)`
  - `_data: Mapping[Key, Value]`
  - `__setitem__ = _immutable`
  - `__delitem__ = _immutable`
  - `__ior__ = _immutable`
  - `clear = _immutable`
  - `pop = _immutable`
  - `popitem = _immutable`
  - `setdefault = _immutable`
  - `update = _immutable`

## 6. Functions, methods, validators, callbacks, fixtures, and tests

### `FrozenDict.__init__`

- Exact signature: `def __init__(self, value: Mapping[Key, Value]) -> None:`
- Decorators: none
- Purpose: create an immutable mapping whose backing dictionary is not aliased to the supplied mapping.
- Ordered algorithm:
  1. Iterate through `value.items()` and preserve every key.
  2. Recursively process every member through the generic `freeze_value` helper.
  3. Build a new ordinary dictionary, breaking the supplied mapping's backing alias.
  4. Wrap the copied dictionary in `MappingProxyType`.
  5. Install that private mapping exactly once through `object.__setattr__`.
- Return/mutation behavior: initialization returns `None`; it does not mutate the supplied mapping and retains no mutable backing alias to that mapping itself.
- Contract boundary: the constructor uses generic `freeze_value`; it does not itself enforce strict canonical-JSON leaf semantics. Contracts requiring exact JSON leaves, exact string keys, finite floats, and cycle rejection must enter through `freeze_json_value` or `freeze_json_mapping`.

### `FrozenDict.__getitem__`

- Exact signature: `def __getitem__(self, key: Key) -> Value:`
- Decorators: none
- Purpose: provide mapping-key lookup over retained immutable state.
- Algorithm: delegate the key lookup to the private retained mapping and return its already-frozen value.
- Return/mutation behavior: returns the retained value without copying it and performs no mutation.

### `FrozenDict.__iter__`

- Exact signature: `def __iter__(self) -> Iterator[Key]:`
- Decorators: none
- Purpose: expose standard mapping iteration over retained keys.
- Algorithm: return the private mapping's key iterator, preserving the copied mapping's iteration order.
- Return/mutation behavior: returns an iterator and performs no mutation.

### `FrozenDict.__len__`

- Exact signature: `def __len__(self) -> int:`
- Decorators: none
- Purpose: report the retained mapping's cardinality.
- Algorithm: delegate to `len(self._data)`.
- Return/mutation behavior: returns the number of retained keys and performs no mutation.

### `FrozenDict.__repr__`

- Exact signature: `def __repr__(self) -> str:`
- Decorators: none
- Purpose: provide a diagnostic representation of the immutable mapping.
- Algorithm: create a temporary plain dictionary view of the retained mapping and format it inside `FrozenDict(...)` with `repr` conversion.
- Return/mutation behavior: returns a string; it neither returns nor exposes the private dictionary created during initialization and does not make the object mutable.

### `FrozenDict.__eq__`

- Exact signature: `def __eq__(self, other: object) -> bool:`
- Decorators: none
- Purpose: compare mapping content independently of the concrete mapping implementation.
- Algorithm: when `other` is a `Mapping`, materialize both item views as temporary ordinary dictionaries and compare them; otherwise return `False`.
- Return/mutation behavior: returns a boolean and mutates neither operand.

### `FrozenDict.__copy__`

- Exact signature: `def __copy__(self) -> Self:`
- Decorators: none
- Purpose: support shallow-copy operations without rebuilding immutable state.
- Algorithm: return `self` directly.
- Return/mutation behavior: returns the same instance and performs no mutation.
- Contract boundary: returning `self` is safe only after the owning contract has established that every retained value is recursively immutable.

### `FrozenDict.__deepcopy__`

- Exact signature: `def __deepcopy__(self, memo: dict[int, object]) -> Self:`
- Decorators: none
- Purpose: support deep-copy operations without attempting to pickle or rebuild the private mapping proxy.
- Algorithm: record `self` under its object identity in `memo`, then return `self`.
- Return/mutation behavior: mutates only the caller-supplied copy memo, returns the same instance, and does not mutate retained mapping state.
- Contract boundary: returning `self` is safe only after the owning contract has established that every retained value is recursively immutable.

### `FrozenDict.__setattr__`

- Exact signature: `def __setattr__(self, name: str, value: object) -> None:`
- Decorators: none
- Purpose: prevent attribute replacement after the one controlled initialization write.
- Algorithm: discard the attempted attribute name and value, then raise `TypeError("frozen mapping cannot be mutated")`.
- Return/mutation behavior: never returns normally and prevents replacement of `_data`.

### `FrozenDict.__delattr__`

- Exact signature: `def __delattr__(self, name: str) -> None:`
- Decorators: none
- Purpose: prevent deletion of retained attributes.
- Algorithm: discard the attempted attribute name, then raise `TypeError("frozen mapping cannot be mutated")`.
- Return/mutation behavior: never returns normally and prevents deletion of `_data`.

### `FrozenDict._immutable`

- Exact signature: `def _immutable(self, *args: object, **kwargs: object) -> None:`
- Decorators: none
- Purpose: provide one controlled failure implementation for item and mapping mutation operations.
- Algorithm: ignore all supplied positional and keyword arguments, then raise `TypeError("frozen mapping cannot be mutated")`.
- Bound operations: `__setitem__`, `__delitem__`, `__ior__`, `clear`, `pop`, `popitem`, `setdefault`, and `update` are assigned to this implementation.
- Return/mutation behavior: never returns normally and leaves retained state unchanged.

### `freeze_value`

- Exact signature: `def freeze_value(value: object) -> object:`
- Decorators: none
- Source purpose: Recursively copy JSON-like collections into immutable equivalents.
- Ordered algorithm: mappings delegate to `freeze_mapping`; lists and tuples recursively become tuples; sets and frozensets recursively become frozensets; every other leaf is returned unchanged.
- Contract boundary: this generic helper relies on the owning Pydantic/domain model to validate leaf semantics before freezing. It is not the strict canonical-JSON validator.

### `freeze_mapping`

- Exact signature: `def freeze_mapping[Key, Value]( value: Mapping[Key, Value], ) -> FrozenDict[Key, Value]:`
- Decorators: none
- Source purpose: Recursively copy a mapping into an immutable mapping value.
- Algorithm: construct `FrozenDict`, whose constructor copies every key/value pair and recursively freezes each value through `freeze_value` before sealing the new dictionary behind `MappingProxyType`.

### `freeze_json_value`

- Exact signature: `def freeze_json_value(value: object) -> object:`
- Decorators: none
- Source purpose: Recursively validate and freeze one canonical JSON value.
- Algorithm: start a new active-collection identity set and delegate to `_freeze_json_value`.

### `_freeze_json_value`

- Exact signature: `def _freeze_json_value(value: object, *, active: set[int]) -> object:`
- Decorators: none
- Source purpose: Validate one canonical JSON value while rejecting collection cycles.
- Ordered algorithm: accept `None` and exact `str`, `bool`, or `int`; accept an exact `float` only when finite; recursively freeze mappings through `_freeze_json_mapping`; convert lists/tuples to tuples while adding and removing their identity from `active`; reject a repeated active identity as a cycle; reject every unsupported leaf without stringification.

### `freeze_json_mapping`

- Exact signature: `def freeze_json_mapping[Key]( value: Mapping[Key, object], ) -> FrozenDict[str, object]:`
- Decorators: none
- Source purpose: Copy a string-keyed canonical JSON mapping into an immutable value.
- Algorithm: start a new active-collection identity set and delegate to `_freeze_json_mapping`.

### `_freeze_json_mapping`

- Exact signature: `def _freeze_json_mapping[Key]( value: Mapping[Key, object], *, active: set[int], ) -> FrozenDict[str, object]:`
- Decorators: none
- Source purpose: Validate one canonical JSON mapping while rejecting collection cycles.
- Ordered algorithm: reject an identity already active; mark the mapping active; require every key to have exact built-in `str` type; recursively validate/freeze every value; seal the copied dictionary as `FrozenDict`; always remove the identity from `active` on exit.

### `to_plain_json_value`

- Exact signature: `def to_plain_json_value(value: object) -> object:`
- Decorators: none
- Source purpose: Return a fresh canonical JSON-compatible copy of an immutable value.
- Ordered algorithm: recursively copy exact-string-keyed mappings to fresh dictionaries; recursively copy lists/tuples to fresh lists; pass through `None` and exact `str`, `bool`, or `int`; pass through exact finite floats; reject non-string keys, non-finite floats, and unsupported values. It never stringifies a value.
## 7. Test inventory

- Exact `test_*` count: 0
- Exact pytest fixture count: 0

## 8. Deep-immutability and canonical-data contract

- Ordered values remain source-ordered tuples; set domains remain frozensets; retained mappings are recursively copied immutable values.
- Explicit serializers preserve the established plain JSON/Python representation where this file participates in canonical hashing or artifact validation.
- Public source/config boundaries retain reconstruction and revalidation; immutability is not treated as source authority.
- No repr, class name, object identity, memory address, or mutable backing alias is included in canonical hashes.

## 9. Trust, side effects, and business boundary

- Exact filesystem, network, hashing, serialization, CRS/geometry, and in-memory operations are defined only by the complete current source below.
- This file does not by documentation implication create a parcel score, ranking, legal conclusion, access conclusion, grid-capacity conclusion, environmental conclusion, or planning authorization.

## 10. Change impact

A source-byte change invalidates this companion SHA and requires re-auditing model reachability, alias isolation, mutation operations, field serializers, canonical hashes, schema versions, retained public-boundary validation, and permanent regressions.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Internal immutable mapping used by frozen decision-input models."""

from __future__ import annotations

import math
from collections.abc import Iterator, Mapping
from types import MappingProxyType
from typing import Self, cast


class FrozenDict[Key, Value](Mapping[Key, Value]):
    """An immutable, recursively copied mapping with no mutable backing alias."""

    __slots__ = ("_data",)

    _data: Mapping[Key, Value]

    def __init__(self, value: Mapping[Key, Value]) -> None:
        copied = {
            key: cast(Value, freeze_value(member)) for key, member in value.items()
        }
        object.__setattr__(self, "_data", MappingProxyType(copied))

    def __getitem__(self, key: Key) -> Value:
        return self._data[key]

    def __iter__(self) -> Iterator[Key]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"FrozenDict({dict(self._data)!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Mapping):
            return dict(self.items()) == dict(other.items())
        return False

    def __copy__(self) -> Self:
        return self

    def __deepcopy__(self, memo: dict[int, object]) -> Self:
        memo[id(self)] = self
        return self

    def __setattr__(self, name: str, value: object) -> None:
        del name, value
        raise TypeError("frozen mapping cannot be mutated")

    def __delattr__(self, name: str) -> None:
        del name
        raise TypeError("frozen mapping cannot be mutated")

    def _immutable(self, *args: object, **kwargs: object) -> None:
        del args, kwargs
        raise TypeError("frozen mapping cannot be mutated")

    __setitem__ = _immutable
    __delitem__ = _immutable
    __ior__ = _immutable
    clear = _immutable
    pop = _immutable  # type: ignore[assignment]
    popitem = _immutable  # type: ignore[assignment]
    setdefault = _immutable  # type: ignore[assignment]
    update = _immutable


def freeze_value(value: object) -> object:
    """Recursively copy JSON-like collections into immutable equivalents."""

    if isinstance(value, Mapping):
        return freeze_mapping(value)
    if isinstance(value, (list, tuple)):
        return tuple(freeze_value(member) for member in value)
    if isinstance(value, (set, frozenset)):
        return frozenset(freeze_value(member) for member in value)
    return value


def freeze_mapping[Key, Value](
    value: Mapping[Key, Value],
) -> FrozenDict[Key, Value]:
    """Recursively copy a mapping into an immutable mapping value."""

    return FrozenDict(value)


def freeze_json_value(value: object) -> object:
    """Recursively validate and freeze one canonical JSON value."""

    return _freeze_json_value(value, active=set())


def _freeze_json_value(value: object, *, active: set[int]) -> object:
    """Validate one canonical JSON value while rejecting collection cycles."""

    if value is None or type(value) in (str, bool, int):
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise ValueError("canonical JSON numbers must be finite")
        return value
    if isinstance(value, Mapping):
        return _freeze_json_mapping(value, active=active)
    if isinstance(value, (list, tuple)):
        identity = id(value)
        if identity in active:
            raise ValueError("canonical JSON collections must not contain cycles")
        active.add(identity)
        try:
            return tuple(_freeze_json_value(member, active=active) for member in value)
        finally:
            active.remove(identity)
    raise ValueError(
        "canonical JSON values must be null, exact strings, booleans, integers, "
        "finite floats, string-keyed mappings, lists, or tuples"
    )


def freeze_json_mapping[Key](
    value: Mapping[Key, object],
) -> FrozenDict[str, object]:
    """Copy a string-keyed canonical JSON mapping into an immutable value."""

    return _freeze_json_mapping(value, active=set())


def _freeze_json_mapping[Key](
    value: Mapping[Key, object],
    *,
    active: set[int],
) -> FrozenDict[str, object]:
    """Validate one canonical JSON mapping while rejecting collection cycles."""

    identity = id(value)
    if identity in active:
        raise ValueError("canonical JSON collections must not contain cycles")
    active.add(identity)
    frozen: dict[str, object] = {}
    try:
        for key, member in value.items():
            if type(key) is not str:
                raise ValueError("canonical JSON mapping keys must be exact strings")
            frozen[cast(str, key)] = _freeze_json_value(member, active=active)
        return FrozenDict(frozen)
    finally:
        active.remove(identity)


def to_plain_json_value(value: object) -> object:
    """Return a fresh canonical JSON-compatible copy of an immutable value."""

    if isinstance(value, Mapping):
        result: dict[str, object] = {}
        for key, member in value.items():
            if type(key) is not str:
                raise ValueError("canonical JSON mapping keys must be exact strings")
            result[key] = to_plain_json_value(member)
        return result
    if isinstance(value, (list, tuple)):
        return [to_plain_json_value(member) for member in value]
    if value is None or type(value) in (str, bool, int):
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise ValueError("canonical JSON numbers must be finite")
        return value
    raise ValueError("unsupported canonical JSON value")
```
