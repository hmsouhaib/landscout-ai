from __future__ import annotations

import pytest

from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)
from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml


def test_strict_yaml_rejects_nested_duplicate_mapping_keys() -> None:
    with pytest.raises(StrictYamlError, match="Duplicate YAML key"):
        loads_strict_yaml("source:\n  provider: IGN\n  provider: UNTRUSTED\n")


def test_strict_yaml_uses_safe_loader_semantics() -> None:
    assert loads_strict_yaml("enabled: true\nvalues: [1, 2]\n") == {
        "enabled": True,
        "values": [1, 2],
    }


def test_strict_json_rejects_nested_duplicate_object_keys() -> None:
    with pytest.raises(StrictJsonError, match="Duplicate JSON key"):
        loads_strict_json(b'{"source":{"sha256":"a","sha256":"b"}}')


@pytest.mark.parametrize(
    "value",
    ["NaN", "Infinity", "-Infinity", "1e999", "-1e999"],
)
def test_strict_json_rejects_every_nonfinite_number(value: str) -> None:
    with pytest.raises(StrictJsonError, match="finite"):
        loads_strict_json(f'{{"value":{value}}}')


def test_strict_json_rejects_malformed_utf8() -> None:
    with pytest.raises(StrictJsonError, match="UTF-8"):
        loads_strict_json(b'{"value":"\xff"}')


def test_strict_json_object_requires_an_object_top_level() -> None:
    with pytest.raises(StrictJsonError, match="object"):
        loads_strict_json_object("[]")


def test_strict_json_object_accepts_an_exact_object() -> None:
    assert loads_strict_json_object(b'{"schema_version":1}') == {"schema_version": 1}
