# `tests/unit/test_crs.py`

## File identity

- Repository path: `tests/unit/test_crs.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `crs` contracts exercised in this file.
- Source SHA256: `c6b7a69a038e545413e3a5db8d6a636a5d2e51f411110dadfef8410e4a5860f4`

## 1. STEP 7F.1A.4 contract delta

- Ruff formatting only in STEP 7F.1A.4; executable contract, values, schemas, and test intent are unchanged. The companion is refreshed because its raw bytes and SHA changed.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `crs` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- None.

### Third-party packages

- `import pytest`
- `from shapely.geometry import Polygon`

### Internal LandScout imports

- `from landscout.geo import LAMBERT93, WGS84, MetricCrsError, centroid_to_latlon`
- `from landscout.geo.geometry import reproject_to_lambert93`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

No module-level constant, alias, schema, mapping, or meaningful dunder assignment is declared.

### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `test_crs_constants`

**Purpose:** Regression invariant: crs constants. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_crs_constants() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert WGS84.to_epsg() == 4326`
  - `assert LAMBERT93.to_epsg() == 2154`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `WGS84.to_epsg` | `landscout.geo.WGS84.to_epsg` |
| `LAMBERT93.to_epsg` | `landscout.geo.LAMBERT93.to_epsg` |

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
def test_crs_constants() -> None:
    assert WGS84.to_epsg() == 4326
    assert LAMBERT93.to_epsg() == 2154
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_reproject_to_lambert93_and_back_to_latlon`

**Purpose:** Regression invariant: reproject to lambert93 and back to latlon. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_reproject_to_lambert93_and_back_to_latlon() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert latitude == pytest.approx(48.005, abs=0.001)`
  - `assert longitude == pytest.approx(2.005, abs=0.001)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `reproject_to_lambert93` | `landscout.geo.geometry.reproject_to_lambert93` |
| `centroid_to_latlon` | `landscout.geo.centroid_to_latlon` |
| `pytest.approx` | `pytest.approx` |

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
def test_reproject_to_lambert93_and_back_to_latlon() -> None:
    polygon = Polygon([(2.0, 48.0), (2.01, 48.0), (2.01, 48.01), (2.0, 48.01)])

    projected = reproject_to_lambert93(polygon, WGS84)
    latitude, longitude = centroid_to_latlon(projected, LAMBERT93)

    assert latitude == pytest.approx(48.005, abs=0.001)
    assert longitude == pytest.approx(2.005, abs=0.001)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_reprojection_rejects_malformed_crs_with_controlled_error`

**Purpose:** Regression invariant: reprojection rejects malformed crs with controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_reprojection_rejects_malformed_crs_with_controlled_error(
    crs: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("crs", [None, object(), [], "invalid-crs"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `crs` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(MetricCrsError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `reproject_to_lambert93` | `landscout.geo.geometry.reproject_to_lambert93` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_reprojection_rejects_malformed_crs_with_controlled_error(
    crs: object,
) -> None:
    polygon = Polygon([(2, 48), (2.01, 48), (2.01, 48.01), (2, 48.01)])

    with pytest.raises(MetricCrsError):
        reproject_to_lambert93(polygon, crs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **3**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_crs_constants` | none | none | 2 | Proves crs constants using the exact source reproduced in section 7. |
| `test_reproject_to_lambert93_and_back_to_latlon` | none | none | 2 | Proves reproject to lambert93 and back to latlon using the exact source reproduced in section 7. |
| `test_reprojection_rejects_malformed_crs_with_controlled_error` | pytest.mark.parametrize("crs", [None, object(), [], "invalid-crs"]) | pytest.raises(MetricCrsError) | 0 | Proves reprojection rejects malformed crs with controlled error using the exact source reproduced in section 7. |

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
import pytest
from shapely.geometry import Polygon

from landscout.geo import LAMBERT93, WGS84, MetricCrsError, centroid_to_latlon
from landscout.geo.geometry import reproject_to_lambert93


def test_crs_constants() -> None:
    assert WGS84.to_epsg() == 4326
    assert LAMBERT93.to_epsg() == 2154


def test_reproject_to_lambert93_and_back_to_latlon() -> None:
    polygon = Polygon([(2.0, 48.0), (2.01, 48.0), (2.01, 48.01), (2.0, 48.01)])

    projected = reproject_to_lambert93(polygon, WGS84)
    latitude, longitude = centroid_to_latlon(projected, LAMBERT93)

    assert latitude == pytest.approx(48.005, abs=0.001)
    assert longitude == pytest.approx(2.005, abs=0.001)


@pytest.mark.parametrize("crs", [None, object(), [], "invalid-crs"])
def test_reprojection_rejects_malformed_crs_with_controlled_error(
    crs: object,
) -> None:
    polygon = Polygon([(2, 48), (2.01, 48), (2.01, 48.01), (2, 48.01)])

    with pytest.raises(MetricCrsError):
        reproject_to_lambert93(polygon, crs)  # type: ignore[arg-type]
```
