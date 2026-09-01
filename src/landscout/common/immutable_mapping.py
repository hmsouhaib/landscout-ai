"""Internal immutable mapping used by frozen decision-input models."""

from __future__ import annotations

import json
from collections.abc import Iterator, Mapping
from types import MappingProxyType
from typing import cast


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


def to_plain_json_value(value: object) -> object:
    """Return a fresh canonical JSON-compatible copy of an immutable value."""

    if isinstance(value, Mapping):
        return {key: to_plain_json_value(member) for key, member in value.items()}
    if isinstance(value, tuple):
        return [to_plain_json_value(member) for member in value]
    if isinstance(value, frozenset):
        members = [to_plain_json_value(member) for member in value]
        return sorted(
            members,
            key=lambda member: json.dumps(
                member,
                ensure_ascii=False,
                allow_nan=False,
                sort_keys=True,
                separators=(",", ":"),
            ),
        )
    return value
