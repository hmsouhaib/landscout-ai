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
