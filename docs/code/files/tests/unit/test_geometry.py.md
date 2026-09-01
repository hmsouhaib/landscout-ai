# `tests/unit/test_geometry.py`

## File identity

- Repository path: `tests/unit/test_geometry.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `geometry` contracts exercised in this file.
- Source SHA256: `50e59494276ba92023531f77811de11ae09a23445948c59109ff4ea02539242c`

## 1. STEP 7F.1A.4 contract delta

- Documentation-fidelity refresh only: the source/test bytes are unchanged, but the companion now reproduces every exact pytest parametrization decorator and the complete current test source after the final independent AST audit found a legacy omission.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `geometry` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- None.

### Third-party packages

- `import pytest`
- `from shapely.affinity import rotate`
- `from shapely.geometry import MultiPolygon, Point, Polygon`

### Internal LandScout imports

- `from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

No module-level constant, alias, schema, mapping, or meaningful dunder assignment is declared.

### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `square`

**Purpose:** Implements `square` within the file role: Provides complete unit and regression coverage for the `geometry` contracts exercised in this file.

**Exact signature**

```python
def square() -> Polygon:
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `Polygon`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_geometry::test_valid_polygon_in_lambert93` via `square`
- value/type reference: `tests.unit.test_geometry::test_area_in_square_metres` via `square`
- value/type reference: `tests.unit.test_geometry::test_perimeter_in_metres` via `square`
- value/type reference: `tests.unit.test_geometry::test_centroid` via `square`
- value/type reference: `tests.unit.test_geometry::test_metric_calculation_in_wgs84_fails` via `square`
- value/type reference: `tests.unit.test_geometry::test_square_shape_metrics` via `square`
- value/type reference: `tests.unit.test_geometry::test_elongated_rectangle_is_less_compact_than_square` via `square`
- value/type reference: `tests.unit.test_geometry::test_shape_metrics_reject_geographic_crs` via `square`
- value/type reference: `tests.unit.test_geometry::test_centralized_shape_metrics_reject_geographic_crs` via `square`
- value/type reference: `tests.unit.test_geometry::test_malformed_crs_inputs_raise_controlled_error` via `square`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |

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
def square() -> Polygon:
    return Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_polygon_in_lambert93`

**Purpose:** Regression invariant: valid polygon in lambert93. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_polygon_in_lambert93(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert area_m2(square, LAMBERT93) > 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `area_m2` | `landscout.geo.area_m2` |

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
def test_valid_polygon_in_lambert93(square: Polygon) -> None:
    assert area_m2(square, LAMBERT93) > 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_area_in_square_metres`

**Purpose:** Regression invariant: area in square metres. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_area_in_square_metres(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert area_m2(square, LAMBERT93) == pytest.approx(100.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `area_m2` | `landscout.geo.area_m2` |
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
def test_area_in_square_metres(square: Polygon) -> None:
    assert area_m2(square, LAMBERT93) == pytest.approx(100.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_perimeter_in_metres`

**Purpose:** Regression invariant: perimeter in metres. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_perimeter_in_metres(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert perimeter_m(square, LAMBERT93) == pytest.approx(40.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `perimeter_m` | `landscout.geo.perimeter_m` |
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
def test_perimeter_in_metres(square: Polygon) -> None:
    assert perimeter_m(square, LAMBERT93) == pytest.approx(40.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_centroid`

**Purpose:** Regression invariant: centroid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_centroid(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert center.x == pytest.approx(5.0)`
  - `assert center.y == pytest.approx(5.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `centroid` | `landscout.geo.centroid` |
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
def test_centroid(square: Polygon) -> None:
    center = centroid(square)

    assert center.x == pytest.approx(5.0)
    assert center.y == pytest.approx(5.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metric_calculation_in_wgs84_fails`

**Purpose:** Regression invariant: metric calculation in wgs84 fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_metric_calculation_in_wgs84_fails(
    square: Polygon, metric_function: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("metric_function", [area_m2, perimeter_m])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |
| `metric_function` | positional-or-keyword | `object` | `required` |

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
| `pytest.raises` | `pytest.raises` |
| `metric_function` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_metric_calculation_in_wgs84_fails(
    square: Polygon, metric_function: object
) -> None:
    with pytest.raises(MetricCrsError):
        metric_function(square, WGS84)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_empty_geometry_fails`

**Purpose:** Regression invariant: empty geometry fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_empty_geometry_fails() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(EmptyGeometryError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `area_m2` | `landscout.geo.area_m2` |
| `Polygon` | `shapely.geometry.Polygon` |

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
def test_empty_geometry_fails() -> None:
    with pytest.raises(EmptyGeometryError):
        area_m2(Polygon(), LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_geometry_fails`

**Purpose:** Regression invariant: invalid geometry fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_geometry_fails() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InvalidGeometryError)`
- Exact assertions:
  - `assert not bow_tie.is_valid`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `area_m2` | `landscout.geo.area_m2` |

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
def test_invalid_geometry_fails() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    assert not bow_tie.is_valid
    with pytest.raises(InvalidGeometryError):
        area_m2(bow_tie, LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_multipolygon`

**Purpose:** Regression invariant: multipolygon. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_multipolygon() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert area_m2(geometry, LAMBERT93) == pytest.approx(200.0)`
  - `assert perimeter_m(geometry, LAMBERT93) == pytest.approx(80.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |
| `area_m2` | `landscout.geo.area_m2` |
| `pytest.approx` | `pytest.approx` |
| `perimeter_m` | `landscout.geo.perimeter_m` |

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
def test_multipolygon() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
    geometry = MultiPolygon([first, second])

    assert area_m2(geometry, LAMBERT93) == pytest.approx(200.0)
    assert perimeter_m(geometry, LAMBERT93) == pytest.approx(80.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_square_shape_metrics`

**Purpose:** Regression invariant: square shape metrics. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_square_shape_metrics(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert approximate_length_m(square, LAMBERT93) == pytest.approx(10.0)`
  - `assert approximate_width_m(square, LAMBERT93) == pytest.approx(10.0)`
  - `assert length_width_ratio(square, LAMBERT93) == pytest.approx(1.0)`
  - `assert compactness_score(square, LAMBERT93) == pytest.approx(0.785398)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `approximate_length_m` | `landscout.geo.approximate_length_m` |
| `pytest.approx` | `pytest.approx` |
| `approximate_width_m` | `landscout.geo.approximate_width_m` |
| `length_width_ratio` | `landscout.geo.length_width_ratio` |
| `compactness_score` | `landscout.geo.compactness_score` |

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
def test_square_shape_metrics(square: Polygon) -> None:
    assert approximate_length_m(square, LAMBERT93) == pytest.approx(10.0)
    assert approximate_width_m(square, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(square, LAMBERT93) == pytest.approx(1.0)
    assert compactness_score(square, LAMBERT93) == pytest.approx(0.785398)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_simple_rectangle_shape_metrics`

**Purpose:** Regression invariant: simple rectangle shape metrics. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_simple_rectangle_shape_metrics() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert approximate_length_m(rectangle, LAMBERT93) == pytest.approx(20.0)`
  - `assert approximate_width_m(rectangle, LAMBERT93) == pytest.approx(10.0)`
  - `assert length_width_ratio(rectangle, LAMBERT93) == pytest.approx(2.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `approximate_length_m` | `landscout.geo.approximate_length_m` |
| `pytest.approx` | `pytest.approx` |
| `approximate_width_m` | `landscout.geo.approximate_width_m` |
| `length_width_ratio` | `landscout.geo.length_width_ratio` |

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
def test_simple_rectangle_shape_metrics() -> None:
    rectangle = Polygon([(0, 0), (20, 0), (20, 10), (0, 10)])

    assert approximate_length_m(rectangle, LAMBERT93) == pytest.approx(20.0)
    assert approximate_width_m(rectangle, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(rectangle, LAMBERT93) == pytest.approx(2.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rotated_rectangle_is_orientation_independent`

**Purpose:** Regression invariant: rotated rectangle is orientation independent. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_rotated_rectangle_is_orientation_independent() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert approximate_length_m(rotated, LAMBERT93) == pytest.approx(30.0)`
  - `assert approximate_width_m(rotated, LAMBERT93) == pytest.approx(10.0)`
  - `assert length_width_ratio(rotated, LAMBERT93) == pytest.approx(3.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `rotate` | `shapely.affinity.rotate` |
| `approximate_length_m` | `landscout.geo.approximate_length_m` |
| `pytest.approx` | `pytest.approx` |
| `approximate_width_m` | `landscout.geo.approximate_width_m` |
| `length_width_ratio` | `landscout.geo.length_width_ratio` |

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
def test_rotated_rectangle_is_orientation_independent() -> None:
    rectangle = Polygon([(0, 0), (30, 0), (30, 10), (0, 10)])
    rotated = rotate(rectangle, 37)

    assert approximate_length_m(rotated, LAMBERT93) == pytest.approx(30.0)
    assert approximate_width_m(rotated, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(rotated, LAMBERT93) == pytest.approx(3.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_elongated_rectangle_is_less_compact_than_square`

**Purpose:** Regression invariant: elongated rectangle is less compact than square. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_elongated_rectangle_is_less_compact_than_square(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert length_width_ratio(elongated, LAMBERT93) == pytest.approx(50.0)`
  - `assert compactness_score(square, LAMBERT93) > compactness_score(<br>        elongated, LAMBERT93<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `length_width_ratio` | `landscout.geo.length_width_ratio` |
| `pytest.approx` | `pytest.approx` |
| `compactness_score` | `landscout.geo.compactness_score` |

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
def test_elongated_rectangle_is_less_compact_than_square(square: Polygon) -> None:
    elongated = Polygon([(0, 0), (100, 0), (100, 2), (0, 2)])

    assert length_width_ratio(elongated, LAMBERT93) == pytest.approx(50.0)
    assert compactness_score(square, LAMBERT93) > compactness_score(
        elongated, LAMBERT93
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_multipolygon_shape_metrics`

**Purpose:** Regression invariant: multipolygon shape metrics. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_multipolygon_shape_metrics() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert approximate_length_m(geometry, LAMBERT93) == pytest.approx(30.0)`
  - `assert approximate_width_m(geometry, LAMBERT93) == pytest.approx(10.0)`
  - `assert 0 < compactness_score(geometry, LAMBERT93) <= 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |
| `approximate_length_m` | `landscout.geo.approximate_length_m` |
| `pytest.approx` | `pytest.approx` |
| `approximate_width_m` | `landscout.geo.approximate_width_m` |
| `compactness_score` | `landscout.geo.compactness_score` |

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
def test_multipolygon_shape_metrics() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
    geometry = MultiPolygon([first, second])

    assert approximate_length_m(geometry, LAMBERT93) == pytest.approx(30.0)
    assert approximate_width_m(geometry, LAMBERT93) == pytest.approx(10.0)
    assert 0 < compactness_score(geometry, LAMBERT93) <= 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_metrics_reject_geographic_crs`

**Purpose:** Regression invariant: shape metrics reject geographic crs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

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
| `pytest.raises` | `pytest.raises` |
| `approximate_length_m` | `landscout.geo.approximate_length_m` |
| `approximate_width_m` | `landscout.geo.approximate_width_m` |
| `length_width_ratio` | `landscout.geo.length_width_ratio` |
| `compactness_score` | `landscout.geo.compactness_score` |

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
def test_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
    with pytest.raises(MetricCrsError):
        approximate_length_m(square, WGS84)
    with pytest.raises(MetricCrsError):
        approximate_width_m(square, WGS84)
    with pytest.raises(MetricCrsError):
        length_width_ratio(square, WGS84)
    with pytest.raises(MetricCrsError):
        compactness_score(square, WGS84)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_metrics_reject_invalid_geometry`

**Purpose:** Regression invariant: shape metrics reject invalid geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_metrics_reject_invalid_geometry() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InvalidGeometryError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `approximate_length_m` | `landscout.geo.approximate_length_m` |

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
def test_shape_metrics_reject_invalid_geometry() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    with pytest.raises(InvalidGeometryError):
        approximate_length_m(bow_tie, LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_metrics_reject_empty_geometry`

**Purpose:** Regression invariant: shape metrics reject empty geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_metrics_reject_empty_geometry() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(EmptyGeometryError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `compactness_score` | `landscout.geo.compactness_score` |
| `Polygon` | `shapely.geometry.Polygon` |

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
def test_shape_metrics_reject_empty_geometry() -> None:
    with pytest.raises(EmptyGeometryError):
        compactness_score(Polygon(), LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zero_area_geometry_raises_controlled_error`

**Purpose:** Regression invariant: zero area geometry raises controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_zero_area_geometry_raises_controlled_error() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GeometryError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `length_width_ratio` | `landscout.geo.length_width_ratio` |

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
def test_zero_area_geometry_raises_controlled_error() -> None:
    zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])

    with pytest.raises(GeometryError):
        length_width_ratio(zero_area, LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_length_is_always_at_least_width`

**Purpose:** Regression invariant: length is always at least width. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_length_is_always_at_least_width(geometry: Polygon) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),
        Polygon([(0, 0), (40, 0), (40, 5), (0, 5)]),
        rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 23),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert approximate_length_m(geometry, LAMBERT93) >= approximate_width_m(<br>        geometry, LAMBERT93<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `approximate_length_m` | `landscout.geo.approximate_length_m` |
| `approximate_width_m` | `landscout.geo.approximate_width_m` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `rotate` | `shapely.affinity.rotate` |

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
def test_length_is_always_at_least_width(geometry: Polygon) -> None:
    assert approximate_length_m(geometry, LAMBERT93) >= approximate_width_m(
        geometry, LAMBERT93
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_compactness_range`

**Purpose:** Regression invariant: compactness range. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_compactness_range(geometry: Polygon) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),
        Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert 0 < compactness_score(geometry, LAMBERT93) <= 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `compactness_score` | `landscout.geo.compactness_score` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |

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
def test_compactness_range(geometry: Polygon) -> None:
    assert 0 < compactness_score(geometry, LAMBERT93) <= 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_centralized_shape_metrics`

**Purpose:** Regression invariant: centralized shape metrics. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_centralized_shape_metrics(
    geometry: Polygon, expected_length: float, expected_width: float
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometry", "expected_length", "expected_width"),
    [
        (Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]), 10.0, 10.0),
        (Polygon([(0, 0), (20, 0), (20, 10), (0, 10)]), 20.0, 10.0),
        (
            rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 37),
            30.0,
            10.0,
        ),
        (Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]), 100.0, 2.0),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `Polygon` | `required` |
| `expected_length` | positional-or-keyword | `float` | `required` |
| `expected_width` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert metrics.length_m == pytest.approx(expected_length)`
  - `assert metrics.width_m == pytest.approx(expected_width)`
  - `assert metrics.length_m >= metrics.width_m`
  - `assert metrics.length_width_ratio == pytest.approx(expected_length / expected_width)`
  - `assert 0 < metrics.compactness <= 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcel_shape_metrics_m` | `landscout.geo.parcel_shape_metrics_m` |
| `pytest.approx` | `pytest.approx` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `rotate` | `shapely.affinity.rotate` |

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
def test_centralized_shape_metrics(
    geometry: Polygon, expected_length: float, expected_width: float
) -> None:
    metrics = parcel_shape_metrics_m(geometry, LAMBERT93)

    assert metrics.length_m == pytest.approx(expected_length)
    assert metrics.width_m == pytest.approx(expected_width)
    assert metrics.length_m >= metrics.width_m
    assert metrics.length_width_ratio == pytest.approx(expected_length / expected_width)
    assert 0 < metrics.compactness <= 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_centralized_shape_metrics_support_multipolygon`

**Purpose:** Regression invariant: centralized shape metrics support multipolygon. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_centralized_shape_metrics_support_multipolygon() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert metrics.length_m == pytest.approx(30.0)`
  - `assert metrics.width_m == pytest.approx(10.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `parcel_shape_metrics_m` | `landscout.geo.parcel_shape_metrics_m` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |
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
def test_centralized_shape_metrics_support_multipolygon() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])

    metrics = parcel_shape_metrics_m(MultiPolygon([first, second]), LAMBERT93)

    assert metrics.length_m == pytest.approx(30.0)
    assert metrics.width_m == pytest.approx(10.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_centralized_shape_metrics_reject_invalid_geometry`

**Purpose:** Regression invariant: centralized shape metrics reject invalid geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_centralized_shape_metrics_reject_invalid_geometry() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InvalidGeometryError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `parcel_shape_metrics_m` | `landscout.geo.parcel_shape_metrics_m` |

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
def test_centralized_shape_metrics_reject_invalid_geometry() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    with pytest.raises(InvalidGeometryError):
        parcel_shape_metrics_m(bow_tie, LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_centralized_shape_metrics_reject_zero_area_geometry`

**Purpose:** Regression invariant: centralized shape metrics reject zero area geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_centralized_shape_metrics_reject_zero_area_geometry() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GeometryError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `parcel_shape_metrics_m` | `landscout.geo.parcel_shape_metrics_m` |

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
def test_centralized_shape_metrics_reject_zero_area_geometry() -> None:
    zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])

    with pytest.raises(GeometryError):
        parcel_shape_metrics_m(zero_area, LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_centralized_shape_metrics_reject_geographic_crs`

**Purpose:** Regression invariant: centralized shape metrics reject geographic crs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_centralized_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

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
| `pytest.raises` | `pytest.raises` |
| `parcel_shape_metrics_m` | `landscout.geo.parcel_shape_metrics_m` |

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
def test_centralized_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
    with pytest.raises(MetricCrsError):
        parcel_shape_metrics_m(square, WGS84)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_non_geometry_inputs_raise_controlled_error`

**Purpose:** Regression invariant: non geometry inputs raise controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_non_geometry_inputs_raise_controlled_error(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("geometry", [None, "polygon", 123, [], object()])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(UnsupportedGeometryError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `area_m2` | `landscout.geo.area_m2` |
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
def test_non_geometry_inputs_raise_controlled_error(geometry: object) -> None:
    with pytest.raises(UnsupportedGeometryError):
        area_m2(geometry, LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsupported_geometry_family_raises_controlled_error`

**Purpose:** Regression invariant: unsupported geometry family raises controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsupported_geometry_family_raises_controlled_error() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(UnsupportedGeometryError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `area_m2` | `landscout.geo.area_m2` |
| `Point` | `shapely.geometry.Point` |

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
def test_unsupported_geometry_family_raises_controlled_error() -> None:
    with pytest.raises(UnsupportedGeometryError):
        area_m2(Point(0, 0), LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_three_dimensional_parcel_is_rejected`

**Purpose:** Regression invariant: three dimensional parcel is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_three_dimensional_parcel_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(UnsupportedGeometryError, match="two-dimensional")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `area_m2` | `landscout.geo.area_m2` |

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
def test_three_dimensional_parcel_is_rejected() -> None:
    polygon_z = Polygon([(0, 0, 1), (10, 0, 1), (10, 10, 1), (0, 10, 1)])

    with pytest.raises(UnsupportedGeometryError, match="two-dimensional"):
        area_m2(polygon_z, LAMBERT93)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_crs_inputs_raise_controlled_error`

**Purpose:** Regression invariant: malformed crs inputs raise controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_crs_inputs_raise_controlled_error(
    square: Polygon,
    crs: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("crs", [None, object(), [], "not-a-crs"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |
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
| `pytest.raises` | `pytest.raises` |
| `area_m2` | `landscout.geo.area_m2` |
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
def test_malformed_crs_inputs_raise_controlled_error(
    square: Polygon,
    crs: object,
) -> None:
    with pytest.raises(MetricCrsError):
        area_m2(square, crs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **28**.
- Pytest fixtures (decorator-proven): **1**.

### Fixtures

- `square` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_valid_polygon_in_lambert93` | none | none | 1 | Proves valid polygon in lambert93 using the exact source reproduced in section 7. |
| `test_area_in_square_metres` | none | none | 1 | Proves area in square metres using the exact source reproduced in section 7. |
| `test_perimeter_in_metres` | none | none | 1 | Proves perimeter in metres using the exact source reproduced in section 7. |
| `test_centroid` | none | none | 2 | Proves centroid using the exact source reproduced in section 7. |
| `test_metric_calculation_in_wgs84_fails` | pytest.mark.parametrize("metric_function", [area_m2, perimeter_m]) | pytest.raises(MetricCrsError) | 0 | Proves metric calculation in wgs84 fails using the exact source reproduced in section 7. |
| `test_empty_geometry_fails` | none | pytest.raises(EmptyGeometryError) | 0 | Proves empty geometry fails using the exact source reproduced in section 7. |
| `test_invalid_geometry_fails` | none | pytest.raises(InvalidGeometryError) | 1 | Proves invalid geometry fails using the exact source reproduced in section 7. |
| `test_multipolygon` | none | none | 2 | Proves multipolygon using the exact source reproduced in section 7. |
| `test_square_shape_metrics` | none | none | 4 | Proves square shape metrics using the exact source reproduced in section 7. |
| `test_simple_rectangle_shape_metrics` | none | none | 3 | Proves simple rectangle shape metrics using the exact source reproduced in section 7. |
| `test_rotated_rectangle_is_orientation_independent` | none | none | 3 | Proves rotated rectangle is orientation independent using the exact source reproduced in section 7. |
| `test_elongated_rectangle_is_less_compact_than_square` | none | none | 2 | Proves elongated rectangle is less compact than square using the exact source reproduced in section 7. |
| `test_multipolygon_shape_metrics` | none | none | 3 | Proves multipolygon shape metrics using the exact source reproduced in section 7. |
| `test_shape_metrics_reject_geographic_crs` | none | pytest.raises(MetricCrsError); pytest.raises(MetricCrsError); pytest.raises(MetricCrsError); pytest.raises(MetricCrsError) | 0 | Proves shape metrics reject geographic crs using the exact source reproduced in section 7. |
| `test_shape_metrics_reject_invalid_geometry` | none | pytest.raises(InvalidGeometryError) | 0 | Proves shape metrics reject invalid geometry using the exact source reproduced in section 7. |
| `test_shape_metrics_reject_empty_geometry` | none | pytest.raises(EmptyGeometryError) | 0 | Proves shape metrics reject empty geometry using the exact source reproduced in section 7. |
| `test_zero_area_geometry_raises_controlled_error` | none | pytest.raises(GeometryError) | 0 | Proves zero area geometry raises controlled error using the exact source reproduced in section 7. |
| `test_length_is_always_at_least_width` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),<br>        Polygon([(0, 0), (40, 0), (40, 5), (0, 5)]),<br>        rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 23),<br>    ],<br>) | none | 1 | Proves length is always at least width using the exact source reproduced in section 7. |
| `test_compactness_range` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),<br>        Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]),<br>    ],<br>) | none | 1 | Proves compactness range using the exact source reproduced in section 7. |
| `test_centralized_shape_metrics` | pytest.mark.parametrize(<br>    ("geometry", "expected_length", "expected_width"),<br>    [<br>        (Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]), 10.0, 10.0),<br>        (Polygon([(0, 0), (20, 0), (20, 10), (0, 10)]), 20.0, 10.0),<br>        (<br>            rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 37),<br>            30.0,<br>            10.0,<br>        ),<br>        (Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]), 100.0, 2.0),<br>    ],<br>) | none | 5 | Proves centralized shape metrics using the exact source reproduced in section 7. |
| `test_centralized_shape_metrics_support_multipolygon` | none | none | 2 | Proves centralized shape metrics support multipolygon using the exact source reproduced in section 7. |
| `test_centralized_shape_metrics_reject_invalid_geometry` | none | pytest.raises(InvalidGeometryError) | 0 | Proves centralized shape metrics reject invalid geometry using the exact source reproduced in section 7. |
| `test_centralized_shape_metrics_reject_zero_area_geometry` | none | pytest.raises(GeometryError) | 0 | Proves centralized shape metrics reject zero area geometry using the exact source reproduced in section 7. |
| `test_centralized_shape_metrics_reject_geographic_crs` | none | pytest.raises(MetricCrsError) | 0 | Proves centralized shape metrics reject geographic crs using the exact source reproduced in section 7. |
| `test_non_geometry_inputs_raise_controlled_error` | pytest.mark.parametrize("geometry", [None, "polygon", 123, [], object()]) | pytest.raises(UnsupportedGeometryError) | 0 | Proves non geometry inputs raise controlled error using the exact source reproduced in section 7. |
| `test_unsupported_geometry_family_raises_controlled_error` | none | pytest.raises(UnsupportedGeometryError) | 0 | Proves unsupported geometry family raises controlled error using the exact source reproduced in section 7. |
| `test_three_dimensional_parcel_is_rejected` | none | pytest.raises(UnsupportedGeometryError, match="two-dimensional") | 0 | Proves three dimensional parcel is rejected using the exact source reproduced in section 7. |
| `test_malformed_crs_inputs_raise_controlled_error` | pytest.mark.parametrize("crs", [None, object(), [], "not-a-crs"]) | pytest.raises(MetricCrsError) | 0 | Proves malformed crs inputs raise controlled error using the exact source reproduced in section 7. |

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
from shapely.affinity import rotate
from shapely.geometry import MultiPolygon, Point, Polygon

from landscout.geo import (
    LAMBERT93,
    WGS84,
    EmptyGeometryError,
    GeometryError,
    InvalidGeometryError,
    MetricCrsError,
    UnsupportedGeometryError,
    approximate_length_m,
    approximate_width_m,
    area_m2,
    centroid,
    compactness_score,
    length_width_ratio,
    parcel_shape_metrics_m,
    perimeter_m,
)


@pytest.fixture
def square() -> Polygon:
    return Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])


def test_valid_polygon_in_lambert93(square: Polygon) -> None:
    assert area_m2(square, LAMBERT93) > 0


def test_area_in_square_metres(square: Polygon) -> None:
    assert area_m2(square, LAMBERT93) == pytest.approx(100.0)


def test_perimeter_in_metres(square: Polygon) -> None:
    assert perimeter_m(square, LAMBERT93) == pytest.approx(40.0)


def test_centroid(square: Polygon) -> None:
    center = centroid(square)

    assert center.x == pytest.approx(5.0)
    assert center.y == pytest.approx(5.0)


@pytest.mark.parametrize("metric_function", [area_m2, perimeter_m])
def test_metric_calculation_in_wgs84_fails(
    square: Polygon, metric_function: object
) -> None:
    with pytest.raises(MetricCrsError):
        metric_function(square, WGS84)  # type: ignore[operator]


def test_empty_geometry_fails() -> None:
    with pytest.raises(EmptyGeometryError):
        area_m2(Polygon(), LAMBERT93)


def test_invalid_geometry_fails() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    assert not bow_tie.is_valid
    with pytest.raises(InvalidGeometryError):
        area_m2(bow_tie, LAMBERT93)


def test_multipolygon() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
    geometry = MultiPolygon([first, second])

    assert area_m2(geometry, LAMBERT93) == pytest.approx(200.0)
    assert perimeter_m(geometry, LAMBERT93) == pytest.approx(80.0)


def test_square_shape_metrics(square: Polygon) -> None:
    assert approximate_length_m(square, LAMBERT93) == pytest.approx(10.0)
    assert approximate_width_m(square, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(square, LAMBERT93) == pytest.approx(1.0)
    assert compactness_score(square, LAMBERT93) == pytest.approx(0.785398)


def test_simple_rectangle_shape_metrics() -> None:
    rectangle = Polygon([(0, 0), (20, 0), (20, 10), (0, 10)])

    assert approximate_length_m(rectangle, LAMBERT93) == pytest.approx(20.0)
    assert approximate_width_m(rectangle, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(rectangle, LAMBERT93) == pytest.approx(2.0)


def test_rotated_rectangle_is_orientation_independent() -> None:
    rectangle = Polygon([(0, 0), (30, 0), (30, 10), (0, 10)])
    rotated = rotate(rectangle, 37)

    assert approximate_length_m(rotated, LAMBERT93) == pytest.approx(30.0)
    assert approximate_width_m(rotated, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(rotated, LAMBERT93) == pytest.approx(3.0)


def test_elongated_rectangle_is_less_compact_than_square(square: Polygon) -> None:
    elongated = Polygon([(0, 0), (100, 0), (100, 2), (0, 2)])

    assert length_width_ratio(elongated, LAMBERT93) == pytest.approx(50.0)
    assert compactness_score(square, LAMBERT93) > compactness_score(
        elongated, LAMBERT93
    )


def test_multipolygon_shape_metrics() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
    geometry = MultiPolygon([first, second])

    assert approximate_length_m(geometry, LAMBERT93) == pytest.approx(30.0)
    assert approximate_width_m(geometry, LAMBERT93) == pytest.approx(10.0)
    assert 0 < compactness_score(geometry, LAMBERT93) <= 1


def test_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
    with pytest.raises(MetricCrsError):
        approximate_length_m(square, WGS84)
    with pytest.raises(MetricCrsError):
        approximate_width_m(square, WGS84)
    with pytest.raises(MetricCrsError):
        length_width_ratio(square, WGS84)
    with pytest.raises(MetricCrsError):
        compactness_score(square, WGS84)


def test_shape_metrics_reject_invalid_geometry() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    with pytest.raises(InvalidGeometryError):
        approximate_length_m(bow_tie, LAMBERT93)


def test_shape_metrics_reject_empty_geometry() -> None:
    with pytest.raises(EmptyGeometryError):
        compactness_score(Polygon(), LAMBERT93)


def test_zero_area_geometry_raises_controlled_error() -> None:
    zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])

    with pytest.raises(GeometryError):
        length_width_ratio(zero_area, LAMBERT93)


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),
        Polygon([(0, 0), (40, 0), (40, 5), (0, 5)]),
        rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 23),
    ],
)
def test_length_is_always_at_least_width(geometry: Polygon) -> None:
    assert approximate_length_m(geometry, LAMBERT93) >= approximate_width_m(
        geometry, LAMBERT93
    )


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),
        Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]),
    ],
)
def test_compactness_range(geometry: Polygon) -> None:
    assert 0 < compactness_score(geometry, LAMBERT93) <= 1


@pytest.mark.parametrize(
    ("geometry", "expected_length", "expected_width"),
    [
        (Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]), 10.0, 10.0),
        (Polygon([(0, 0), (20, 0), (20, 10), (0, 10)]), 20.0, 10.0),
        (
            rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 37),
            30.0,
            10.0,
        ),
        (Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]), 100.0, 2.0),
    ],
)
def test_centralized_shape_metrics(
    geometry: Polygon, expected_length: float, expected_width: float
) -> None:
    metrics = parcel_shape_metrics_m(geometry, LAMBERT93)

    assert metrics.length_m == pytest.approx(expected_length)
    assert metrics.width_m == pytest.approx(expected_width)
    assert metrics.length_m >= metrics.width_m
    assert metrics.length_width_ratio == pytest.approx(expected_length / expected_width)
    assert 0 < metrics.compactness <= 1


def test_centralized_shape_metrics_support_multipolygon() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])

    metrics = parcel_shape_metrics_m(MultiPolygon([first, second]), LAMBERT93)

    assert metrics.length_m == pytest.approx(30.0)
    assert metrics.width_m == pytest.approx(10.0)


def test_centralized_shape_metrics_reject_invalid_geometry() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    with pytest.raises(InvalidGeometryError):
        parcel_shape_metrics_m(bow_tie, LAMBERT93)


def test_centralized_shape_metrics_reject_zero_area_geometry() -> None:
    zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])

    with pytest.raises(GeometryError):
        parcel_shape_metrics_m(zero_area, LAMBERT93)


def test_centralized_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
    with pytest.raises(MetricCrsError):
        parcel_shape_metrics_m(square, WGS84)


@pytest.mark.parametrize("geometry", [None, "polygon", 123, [], object()])
def test_non_geometry_inputs_raise_controlled_error(geometry: object) -> None:
    with pytest.raises(UnsupportedGeometryError):
        area_m2(geometry, LAMBERT93)  # type: ignore[arg-type]


def test_unsupported_geometry_family_raises_controlled_error() -> None:
    with pytest.raises(UnsupportedGeometryError):
        area_m2(Point(0, 0), LAMBERT93)


def test_three_dimensional_parcel_is_rejected() -> None:
    polygon_z = Polygon([(0, 0, 1), (10, 0, 1), (10, 10, 1), (0, 10, 1)])

    with pytest.raises(UnsupportedGeometryError, match="two-dimensional"):
        area_m2(polygon_z, LAMBERT93)


@pytest.mark.parametrize("crs", [None, object(), [], "not-a-crs"])
def test_malformed_crs_inputs_raise_controlled_error(
    square: Polygon,
    crs: object,
) -> None:
    with pytest.raises(MetricCrsError):
        area_m2(square, crs)  # type: ignore[arg-type]
```
