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
