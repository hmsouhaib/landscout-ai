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
