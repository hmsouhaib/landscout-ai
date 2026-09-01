# `src/landscout/common/strict_yaml.py`

## File identity

- Repository path: `src/landscout/common/strict_yaml.py`
- File type: Python source
- Layer: internal common contract
- Domain: shared validation and schema contracts
- Responsibility: Decodes trust-bearing YAML with a SafeLoader subclass that rejects duplicate mapping keys at every depth.
- Source SHA256: `2affe2cb67de83b4c493d6df1567d4f6809464a86fd47b57fcff48da99a9acc5`

## 1. STEP 7F.1A.4 contract delta

- Introduces the single strict trust-bearing YAML decoder with nested duplicate-key rejection and controlled UTF-8/parse failures.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Decodes trust-bearing YAML with a SafeLoader subclass that rejects duplicate mapping keys at every depth.

The file belongs to the **internal common contract** layer and **shared validation and schema contracts** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from typing import Any`

### Third-party packages

- `import yaml`

### Internal LandScout imports

- None.

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

No module-level constant, alias, schema, mapping, or meaningful dunder assignment is declared.

### Executable module-import-time statements

### Module-import-time executable statement at line 37

- Category: executable import-time registration/guard/statement; it is not a constant or function-local side effect.
- Exact call expressions: `_DuplicateRejectingSafeLoader.add_constructor`.
- Exact statement:

```python
_DuplicateRejectingSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)
```


## 5. Classes, models, dataclasses, and fields

### `StrictYamlError`

**Source purpose:** Raised when a trust-bearing YAML document is not deterministic.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- constructor call: `landscout.common.strict_yaml::_construct_unique_mapping` via `StrictYamlError`
- value/type reference: `landscout.common.strict_yaml::_construct_unique_mapping` via `StrictYamlError`
- constructor call: `landscout.common.strict_yaml::loads_strict_yaml` via `StrictYamlError`
- value/type reference: `landscout.common.strict_yaml::loads_strict_yaml` via `StrictYamlError`
- import: `landscout.sources.gpu_fr::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- value/type reference: `landscout.sources.gpu_fr::load_gpu_source_config` via `StrictYamlError`
- import: `landscout.stages.bess_planning_feature_policy::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_config` via `StrictYamlError`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- value/type reference: `landscout.stages.interpret_bess_zoning::load_bess_zoning_policy_config` via `StrictYamlError`
- import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::load_cnig_feature_code_profile` via `StrictYamlError`
- import: `landscout.stages.road_vehicle_proxy_policy::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `StrictYamlError`
- import: `landscout.stages.structure_planning_regulation::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- value/type reference: `landscout.stages.structure_planning_regulation::load_planning_regulation_structure_config` via `StrictYamlError`
- import: `tests.unit.test_strict_serialization::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_yaml_rejects_nested_duplicate_mapping_keys` via `StrictYamlError`

**Exact class source**

```python
class StrictYamlError(ValueError):
    """Raised when a trust-bearing YAML document is not deterministic."""
```

### `_DuplicateRejectingSafeLoader`

**Source purpose:** Defines `_DuplicateRejectingSafeLoader`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `yaml.SafeLoader`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- value/type reference: `landscout.common.strict_yaml::_construct_unique_mapping` via `_DuplicateRejectingSafeLoader`
- value/type reference: `landscout.common.strict_yaml::loads_strict_yaml` via `_DuplicateRejectingSafeLoader`

**Exact class source**

```python
class _DuplicateRejectingSafeLoader(yaml.SafeLoader):
    pass
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_construct_unique_mapping`

**Purpose:** Implements `construct unique mapping` within the file role: Decodes trust-bearing YAML with a SafeLoader subclass that rejects duplicate mapping keys at every depth.

**Exact signature**

```python
def _construct_unique_mapping(
    loader: _DuplicateRejectingSafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
```

- Exact decorators: none.
- Declared return annotation: `dict[Any, Any]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `loader` | positional-or-keyword | `_DuplicateRejectingSafeLoader` | `required` |
| `node` | positional-or-keyword | `yaml.MappingNode` | `required` |
| `deep` | positional-or-keyword | `bool` | `False` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `StrictYamlError("YAML mapping key must be hashable")`.
  - `StrictYamlError(f"Duplicate YAML key: {key!r}")` under lexical guard `duplicate`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loader.flatten_mapping` | `unresolved local/third-party receiver; no ownership inferred` |
| `loader.construct_object` | `unresolved local/third-party receiver; no ownership inferred` |
| `StrictYamlError` | `landscout.common.strict_yaml.StrictYamlError` |

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
| In-memory mutation | `result[key] = loader.construct_object(value_node, deep=deep)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `loads_strict_yaml`

**Purpose:** Parse safe YAML while rejecting duplicate mapping keys at every depth.

**Exact signature**

```python
def loads_strict_yaml(value: str | bytes) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str \| bytes` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `yaml.load(document, Loader=_DuplicateRejectingSafeLoader)`
- Explicit raise paths:
  - `StrictYamlError("YAML document is not valid UTF-8")` under lexical guard `type(value) is bytes`.
  - `StrictYamlError("YAML input must be an exact string or bytes")` under lexical guard `type(value) is bytes`.
  - `re-raise`.
  - `StrictYamlError("YAML document is invalid")`.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.config::<module>` via `from landscout.common.strict_yaml import loads_strict_yaml`
- direct call: `landscout.config::_load_yaml` via `loads_strict_yaml`
- value/type reference: `landscout.config::_load_yaml` via `loads_strict_yaml`
- import: `landscout.sources.gpu_fr::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- direct call: `landscout.sources.gpu_fr::load_gpu_source_config` via `loads_strict_yaml`
- value/type reference: `landscout.sources.gpu_fr::load_gpu_source_config` via `loads_strict_yaml`
- import: `landscout.sources.ign_bdtopo_fr::<module>` via `from landscout.common.strict_yaml import loads_strict_yaml`
- direct call: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_source_config` via `loads_strict_yaml`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_source_config` via `loads_strict_yaml`
- import: `landscout.sources.inpn_protected_areas_fr::<module>` via `from landscout.common.strict_yaml import loads_strict_yaml`
- direct call: `landscout.sources.inpn_protected_areas_fr::load_inpn_protected_areas_source_config` via `loads_strict_yaml`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::load_inpn_protected_areas_source_config` via `loads_strict_yaml`
- import: `landscout.sources.rte_odre_fr::<module>` via `from landscout.common.strict_yaml import loads_strict_yaml`
- direct call: `landscout.sources.rte_odre_fr::load_rte_odre_source_config` via `loads_strict_yaml`
- value/type reference: `landscout.sources.rte_odre_fr::load_rte_odre_source_config` via `loads_strict_yaml`
- import: `landscout.stages.bess_planning_feature_policy::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- direct call: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_config` via `loads_strict_yaml`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_config` via `loads_strict_yaml`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- direct call: `landscout.stages.interpret_bess_zoning::load_bess_zoning_policy_config` via `loads_strict_yaml`
- value/type reference: `landscout.stages.interpret_bess_zoning::load_bess_zoning_policy_config` via `loads_strict_yaml`
- import: `landscout.stages.resolve_planning_feature_codes::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- direct call: `landscout.stages.resolve_planning_feature_codes::load_cnig_feature_code_profile` via `loads_strict_yaml`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::load_cnig_feature_code_profile` via `loads_strict_yaml`
- import: `landscout.stages.road_vehicle_proxy_policy::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- direct call: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `loads_strict_yaml`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `loads_strict_yaml`
- import: `landscout.stages.structure_planning_regulation::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- direct call: `landscout.stages.structure_planning_regulation::load_planning_regulation_structure_config` via `loads_strict_yaml`
- value/type reference: `landscout.stages.structure_planning_regulation::load_planning_regulation_structure_config` via `loads_strict_yaml`
- import: `tests.unit.test_strict_serialization::<module>` via `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- direct call: `tests.unit.test_strict_serialization::test_strict_yaml_rejects_nested_duplicate_mapping_keys` via `loads_strict_yaml`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_yaml_rejects_nested_duplicate_mapping_keys` via `loads_strict_yaml`
- direct call: `tests.unit.test_strict_serialization::test_strict_yaml_uses_safe_loader_semantics` via `loads_strict_yaml`
- value/type reference: `tests.unit.test_strict_serialization::test_strict_yaml_uses_safe_loader_semantics` via `loads_strict_yaml`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.decode` | `unresolved local/third-party receiver; no ownership inferred` |
| `StrictYamlError` | `landscout.common.strict_yaml.StrictYamlError` |
| `yaml.load` | `yaml.load` |

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
```
