# `tests/unit/test_strict_serialization.py`

## File identity

- Repository path: `tests/unit/test_strict_serialization.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Exercises nested duplicate YAML/JSON keys, ordinary YAML scalar/list decoding, five nonfinite/overflow JSON tokens, invalid UTF-8 and object-root rejection/acceptance entirely in memory.
- Source SHA256: `98f223391076f36ae48c679b2bfaefd73f075ea67c78918227865a2d6fa7aac3`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for strict serialization; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Exercises nested duplicate YAML/JSON keys, ordinary YAML scalar/list decoding, five nonfinite/overflow JSON tokens, invalid UTF-8 and object-root rejection/acceptance entirely in memory.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`

### Third-party packages

- `import pytest`

### Internal LandScout imports

- `from landscout.common.strict_json import (
    StrictJsonError,
    loads_strict_json,
    loads_strict_json_object,
)`
- `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

No module-level constant, alias, schema, mapping, or meaningful dunder assignment is declared.

### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `test_strict_yaml_rejects_nested_duplicate_mapping_keys`

**Assertion scope:** Parse nested source.provider declared twice with conflicting strings and require StrictYamlError matching Duplicate YAML key; this proves the nested duplicate hook, not just root-level rejection.

**Exact signature**

```python
def test_strict_yaml_rejects_nested_duplicate_mapping_keys() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(StrictYamlError, match="Duplicate YAML key")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |

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
def test_strict_yaml_rejects_nested_duplicate_mapping_keys() -> None:
    with pytest.raises(StrictYamlError, match="Duplicate YAML key"):
        loads_strict_yaml("source:\n  provider: IGN\n  provider: UNTRUSTED\n")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_yaml_uses_safe_loader_semantics`

**Assertion scope:** Assert ordinary YAML true and [1, 2] decode as builtin bool/list/int values. Despite its name this positive case does not attempt an unsafe Python-object tag.

**Exact signature**

```python
def test_strict_yaml_uses_safe_loader_semantics() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert loads_strict_yaml("enabled: true\nvalues: [1, 2]\n") == {<br>        "enabled": True,<br>        "values": [1, 2],<br>    }`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |

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
def test_strict_yaml_uses_safe_loader_semantics() -> None:
    assert loads_strict_yaml("enabled: true\nvalues: [1, 2]\n") == {
        "enabled": True,
        "values": [1, 2],
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_json_rejects_nested_duplicate_object_keys`

**Assertion scope:** Feed UTF-8 bytes with two nested source.sha256 entries and require StrictJsonError matching Duplicate JSON key; neither value may silently win.

**Exact signature**

```python
def test_strict_json_rejects_nested_duplicate_object_keys() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(StrictJsonError, match="Duplicate JSON key")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `loads_strict_json` | `landscout.common.strict_json.loads_strict_json` |

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
def test_strict_json_rejects_nested_duplicate_object_keys() -> None:
    with pytest.raises(StrictJsonError, match="Duplicate JSON key"):
        loads_strict_json(b'{"source":{"sha256":"a","sha256":"b"}}')
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_json_rejects_every_nonfinite_number`

**Assertion scope:** Place each of NaN, Infinity, -Infinity, 1e999 and -1e999 in an object value and require a finite-number error. Three constants and two finite-looking float-overflow spellings are checked.

**Exact signature**

```python
def test_strict_json_rejects_every_nonfinite_number(value: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    ["NaN", "Infinity", "-Infinity", "1e999", "-1e999"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(StrictJsonError, match="finite")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `loads_strict_json` | `landscout.common.strict_json.loads_strict_json` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_strict_json_rejects_every_nonfinite_number(value: str) -> None:
    with pytest.raises(StrictJsonError, match="finite"):
        loads_strict_json(f'{{"value":{value}}}')
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_json_rejects_malformed_utf8`

**Assertion scope:** Pass bytes containing 0xff inside a JSON string and require StrictJsonError matching UTF-8 before accepting decoded evidence.

**Exact signature**

```python
def test_strict_json_rejects_malformed_utf8() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(StrictJsonError, match="UTF-8")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `loads_strict_json` | `landscout.common.strict_json.loads_strict_json` |

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
def test_strict_json_rejects_malformed_utf8() -> None:
    with pytest.raises(StrictJsonError, match="UTF-8"):
        loads_strict_json(b'{"value":"\xff"}')
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_json_object_requires_an_object_top_level`

**Assertion scope:** Pass [] to the object-specific parser and require an object error. The general JSON parser's ability to return arrays is not prohibited.

**Exact signature**

```python
def test_strict_json_object_requires_an_object_top_level() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(StrictJsonError, match="object")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |

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
def test_strict_json_object_requires_an_object_top_level() -> None:
    with pytest.raises(StrictJsonError, match="object"):
        loads_strict_json_object("[]")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_json_object_accepts_an_exact_object`

**Assertion scope:** Pass a byte-encoded schema_version object and assert the exact builtin dictionary containing integer 1; no schema-specific model is involved.

**Exact signature**

```python
def test_strict_json_object_accepts_an_exact_object() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert loads_strict_json_object(b'{"schema_version":1}') == {"schema_version": 1}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |

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
def test_strict_json_object_accepts_an_exact_object() -> None:
    assert loads_strict_json_object(b'{"schema_version":1}') == {"schema_version": 1}
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **7**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_strict_yaml_rejects_nested_duplicate_mapping_keys` | none | pytest.raises(StrictYamlError, match="Duplicate YAML key") | 0 | Parse nested source.provider declared twice with conflicting strings and require StrictYamlError matching Duplicate YAML key; this proves the nested duplicate hook, not just root-level rejection. |
| `test_strict_yaml_uses_safe_loader_semantics` | none | none | 1 | Assert ordinary YAML true and [1, 2] decode as builtin bool/list/int values. Despite its name this positive case does not attempt an unsafe Python-object tag. |
| `test_strict_json_rejects_nested_duplicate_object_keys` | none | pytest.raises(StrictJsonError, match="Duplicate JSON key") | 0 | Feed UTF-8 bytes with two nested source.sha256 entries and require StrictJsonError matching Duplicate JSON key; neither value may silently win. |
| `test_strict_json_rejects_every_nonfinite_number` | pytest.mark.parametrize(<br>    "value",<br>    ["NaN", "Infinity", "-Infinity", "1e999", "-1e999"],<br>) | pytest.raises(StrictJsonError, match="finite") | 0 | Place each of NaN, Infinity, -Infinity, 1e999 and -1e999 in an object value and require a finite-number error. Three constants and two finite-looking float-overflow spellings are checked. |
| `test_strict_json_rejects_malformed_utf8` | none | pytest.raises(StrictJsonError, match="UTF-8") | 0 | Pass bytes containing 0xff inside a JSON string and require StrictJsonError matching UTF-8 before accepting decoded evidence. |
| `test_strict_json_object_requires_an_object_top_level` | none | pytest.raises(StrictJsonError, match="object") | 0 | Pass [] to the object-specific parser and require an object error. The general JSON parser's ability to return arrays is not prohibited. |
| `test_strict_json_object_accepts_an_exact_object` | none | none | 1 | Pass a byte-encoded schema_version object and assert the exact builtin dictionary containing integer 1; no schema-specific model is involved. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
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
```
