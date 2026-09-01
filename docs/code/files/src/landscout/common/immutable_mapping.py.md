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
- `import json`
- `from collections.abc import Iterator, Mapping`
- `from types import MappingProxyType`
- `from typing import cast`

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
- Source purpose: No callable docstring; exact source below is authoritative.

### `FrozenDict.__getitem__`

- Exact signature: `def __getitem__(self, key: Key) -> Value:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `FrozenDict.__iter__`

- Exact signature: `def __iter__(self) -> Iterator[Key]:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `FrozenDict.__len__`

- Exact signature: `def __len__(self) -> int:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `FrozenDict.__repr__`

- Exact signature: `def __repr__(self) -> str:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `FrozenDict.__eq__`

- Exact signature: `def __eq__(self, other: object) -> bool:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `FrozenDict.__setattr__`

- Exact signature: `def __setattr__(self, name: str, value: object) -> None:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `FrozenDict.__delattr__`

- Exact signature: `def __delattr__(self, name: str) -> None:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `FrozenDict._immutable`

- Exact signature: `def _immutable(self, *args: object, **kwargs: object) -> None:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `freeze_value`

- Exact signature: `def freeze_value(value: object) -> object:`
- Decorators: none
- Source purpose: Recursively copy JSON-like collections into immutable equivalents.

### `freeze_mapping`

- Exact signature: `def freeze_mapping[Key, Value]( value: Mapping[Key, Value], ) -> FrozenDict[Key, Value]:`
- Decorators: none
- Source purpose: Recursively copy a mapping into an immutable mapping value.

### `to_plain_json_value`

- Exact signature: `def to_plain_json_value(value: object) -> object:`
- Decorators: none
- Source purpose: Return a fresh canonical JSON-compatible copy of an immutable value.

## 6B. STEP 7F.1A.4.2 authoritative changed contracts

This section supersedes older source excerpts for the named callables. The exact complete current file snapshot in section 11 remains authoritative for every declaration.

### `FrozenDict.__copy__`

```python
def __copy__(self) -> Self:
        return self
```

### `FrozenDict.__deepcopy__`

```python
def __deepcopy__(self, memo: dict[int, object]) -> Self:
        memo[id(self)] = self
        return self
```

### `freeze_json_value`

```python
def freeze_json_value(value: object) -> object:
    """Recursively validate and freeze one canonical JSON value."""

    return _freeze_json_value(value, active=set())
```

### `_freeze_json_value`

```python
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
```

### `freeze_json_mapping`

```python
def freeze_json_mapping[Key](
    value: Mapping[Key, object],
) -> FrozenDict[str, object]:
    """Copy a string-keyed canonical JSON mapping into an immutable value."""

    return _freeze_json_mapping(value, active=set())
```

### `_freeze_json_mapping`

```python
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
```

### `to_plain_json_value`

```python
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
