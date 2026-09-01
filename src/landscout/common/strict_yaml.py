"""Small safe YAML reader for trust-bearing repository inputs."""

from __future__ import annotations

from typing import Any

import yaml  # type: ignore[import-untyped]


class StrictYamlError(ValueError):
    """Raised when a trust-bearing YAML document is not deterministic."""


class _DuplicateRejectingSafeLoader(yaml.SafeLoader):
    pass


def _construct_unique_mapping(
    loader: _DuplicateRejectingSafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in result
        except TypeError as error:
            raise StrictYamlError("YAML mapping key must be hashable") from error
        if duplicate:
            raise StrictYamlError(f"Duplicate YAML key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


_DuplicateRejectingSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def loads_strict_yaml(value: str | bytes) -> object:
    """Parse safe YAML while rejecting duplicate mapping keys at every depth."""

    if type(value) is bytes:
        try:
            document = value.decode("utf-8")
        except UnicodeDecodeError as error:
            raise StrictYamlError("YAML document is not valid UTF-8") from error
    elif type(value) is str:
        document = value
    else:
        raise StrictYamlError("YAML input must be an exact string or bytes")
    try:
        return yaml.load(document, Loader=_DuplicateRejectingSafeLoader)
    except StrictYamlError:
        raise
    except (TypeError, ValueError, yaml.YAMLError) as error:
        raise StrictYamlError("YAML document is invalid") from error
