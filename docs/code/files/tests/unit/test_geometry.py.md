# `tests/unit/test_geometry.py`

## File identity

- Repository path: `tests/unit/test_geometry.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Checks real in-memory polygon/multipolygon area, perimeter, centroid and rotated-envelope shape metrics on explicit fixtures, plus empty/invalid/nonpolygon/XYZ and geographic/malformed-CRS rejection; no source files, network or repairs are involved.
- Source SHA256: `50e59494276ba92023531f77811de11ae09a23445948c59109ff4ea02539242c`

## 1. STEP 7F.1A.4 contract delta

- Documentation-fidelity refresh only: the source/test bytes are unchanged, but the companion now reproduces every exact pytest parametrization decorator and the complete current test source after the final independent AST audit found a legacy omission.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Checks real in-memory polygon/multipolygon area, perimeter, centroid and rotated-envelope shape metrics on explicit fixtures, plus empty/invalid/nonpolygon/XYZ and geographic/malformed-CRS rejection; no source files, network or repairs are involved.

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

**Assertion scope:** Return a new valid 10-by-10 coordinate-unit Polygon for pytest fixture injection. Tests supply Lambert-93 to interpret those units as metres; the fixture itself stores no CRS.

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
| CRS/geometry/spatial calculation | Real Shapely Polygon construction. |
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

**Assertion scope:** Use the real area helper on the square fixture with Lambert-93 and assert positive area; this smoke check is weaker than the exact 100 m² case below.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Assert the 10-by-10 square has approximately 100 m² using the real metric helper.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Assert the square's real perimeter is approximately 40 m.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Compute the real planar centroid of the square and assert x and y are both approximately 5.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Parametrize area_m2 and perimeter_m; both must reject the valid square when its declared CRS is geographic WGS84 with MetricCrsError. The dynamic metric_function receiver is exactly this two-function set.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Pass Polygon() to area_m2 with Lambert-93 and require EmptyGeometryError; no repair or substitute polygon is used.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Construct a self-crossing bow-tie, assert the fixture is actually invalid, then require InvalidGeometryError from area_m2.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Combine two separated 10-by-10 squares and assert aggregate area 200 m² and perimeter 80 m; both components remain present.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Call the four individual shape helpers on a square and check length/width 10 m, ratio 1 and compactness approximately 0.785398 (π/4).

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** For a 20-by-10 rectangle assert 20 m length, 10 m width and ratio 2 using the individual helpers.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Rotate a 30-by-10 rectangle and assert its minimum-rotated-rectangle dimensions remain 30 m and 10 m, ratio 3. This is one rotation regression, not a proof over all angles.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Check the 100-by-2 rectangle's ratio is 50 and its compactness is below the square's; no threshold or suitability policy is inferred.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** For two separated squares, assert the joint rotated envelope spans 30 m by 10 m and compactness lies in (0, 1]. The width/length describe the combined geometry envelope, not a single component.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Use four separate raises contexts to require MetricCrsError from length, width, ratio and compactness helpers on the square with WGS84. All four calls execute independently.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Pass a self-crossing polygon to approximate_length_m and require InvalidGeometryError; this case does not directly invoke the other three individual helpers.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Pass Polygon() to compactness_score and require EmptyGeometryError.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Pass a collinear polygon to length_width_ratio and require the GeometryError base class. The test does not pin a narrower subtype or prove which internal guard rejects first.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** For three explicit geometries (square, elongated rectangle and a 23-degree rotated rectangle), assert individual length is at least individual width. The name's always is limited to these sampled cases.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** For a square and a 100-by-2 rectangle, assert compactness in (0, 1]; no random or exhaustive geometric domain is sampled.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** For four declared rectangle cases, including one rotated 37 degrees, call parcel_shape_metrics_m once and assert expected dimensions, length≥width, expected ratio and compactness range on the returned ShapeMetrics.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Pass the two separated squares to the centralized helper and assert the returned joint envelope dimensions 30 m by 10 m.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Require InvalidGeometryError from the centralized helper for a self-crossing polygon.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Require the GeometryError base class from centralized shape computation on a collinear polygon; do not claim a specific positive-area branch was reached.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Require MetricCrsError when the centralized helper receives the square with WGS84.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Five exact inputs (None, polygon text, integer 123, empty list and object) must raise UnsupportedGeometryError from area_m2; no Shapely geometry parser is substituted.

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
| CRS/geometry/spatial calculation | Delegated type rejection in `area_m2`; no successful geometry calculation. |
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

**Assertion scope:** Pass a real Point to the polygon-only area helper and require UnsupportedGeometryError.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** Pass a real XYZ Polygon to area_m2 and require UnsupportedGeometryError matching two-dimensional. This test does not construct XYM or XYZM data.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

**Assertion scope:** For None, object, empty list and not-a-crs text, require MetricCrsError from area_m2 with a valid square. The malformed-CRS gate is exercised independently of malformed geometry.

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
| CRS/geometry/spatial calculation | Real Shapely fixtures and the explicitly listed geometry/CRS helper calls; rejected inputs fail at their delegated validation gates. |
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

- Test function definitions: **28**. Static decorator arithmetic gives **42** cases (28 + 1 + 2 + 1 + 3 + 4 + 3); this file-content audit did not rerun collection.
- Pytest fixtures (decorator-proven): **1**.

### Fixtures

- `square` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_valid_polygon_in_lambert93` | none | none | 1 | Use the real area helper on the square fixture with Lambert-93 and assert positive area; this smoke check is weaker than the exact 100 m² case below. |
| `test_area_in_square_metres` | none | none | 1 | Assert the 10-by-10 square has approximately 100 m² using the real metric helper. |
| `test_perimeter_in_metres` | none | none | 1 | Assert the square's real perimeter is approximately 40 m. |
| `test_centroid` | none | none | 2 | Compute the real planar centroid of the square and assert x and y are both approximately 5. |
| `test_metric_calculation_in_wgs84_fails` | pytest.mark.parametrize("metric_function", [area_m2, perimeter_m]) | pytest.raises(MetricCrsError) | 0 | Parametrize area_m2 and perimeter_m; both must reject the valid square when its declared CRS is geographic WGS84 with MetricCrsError. The dynamic metric_function receiver is exactly this two-function set. |
| `test_empty_geometry_fails` | none | pytest.raises(EmptyGeometryError) | 0 | Pass Polygon() to area_m2 with Lambert-93 and require EmptyGeometryError; no repair or substitute polygon is used. |
| `test_invalid_geometry_fails` | none | pytest.raises(InvalidGeometryError) | 1 | Construct a self-crossing bow-tie, assert the fixture is actually invalid, then require InvalidGeometryError from area_m2. |
| `test_multipolygon` | none | none | 2 | Combine two separated 10-by-10 squares and assert aggregate area 200 m² and perimeter 80 m; both components remain present. |
| `test_square_shape_metrics` | none | none | 4 | Call the four individual shape helpers on a square and check length/width 10 m, ratio 1 and compactness approximately 0.785398 (π/4). |
| `test_simple_rectangle_shape_metrics` | none | none | 3 | For a 20-by-10 rectangle assert 20 m length, 10 m width and ratio 2 using the individual helpers. |
| `test_rotated_rectangle_is_orientation_independent` | none | none | 3 | Rotate a 30-by-10 rectangle and assert its minimum-rotated-rectangle dimensions remain 30 m and 10 m, ratio 3. This is one rotation regression, not a proof over all angles. |
| `test_elongated_rectangle_is_less_compact_than_square` | none | none | 2 | Check the 100-by-2 rectangle's ratio is 50 and its compactness is below the square's; no threshold or suitability policy is inferred. |
| `test_multipolygon_shape_metrics` | none | none | 3 | For two separated squares, assert the joint rotated envelope spans 30 m by 10 m and compactness lies in (0, 1]. The width/length describe the combined geometry envelope, not a single component. |
| `test_shape_metrics_reject_geographic_crs` | none | pytest.raises(MetricCrsError); pytest.raises(MetricCrsError); pytest.raises(MetricCrsError); pytest.raises(MetricCrsError) | 0 | Use four separate raises contexts to require MetricCrsError from length, width, ratio and compactness helpers on the square with WGS84. All four calls execute independently. |
| `test_shape_metrics_reject_invalid_geometry` | none | pytest.raises(InvalidGeometryError) | 0 | Pass a self-crossing polygon to approximate_length_m and require InvalidGeometryError; this case does not directly invoke the other three individual helpers. |
| `test_shape_metrics_reject_empty_geometry` | none | pytest.raises(EmptyGeometryError) | 0 | Pass Polygon() to compactness_score and require EmptyGeometryError. |
| `test_zero_area_geometry_raises_controlled_error` | none | pytest.raises(GeometryError) | 0 | Pass a collinear polygon to length_width_ratio and require the GeometryError base class. The test does not pin a narrower subtype or prove which internal guard rejects first. |
| `test_length_is_always_at_least_width` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),<br>        Polygon([(0, 0), (40, 0), (40, 5), (0, 5)]),<br>        rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 23),<br>    ],<br>) | none | 1 | For three explicit geometries (square, elongated rectangle and a 23-degree rotated rectangle), assert individual length is at least individual width. The name's always is limited to these sampled cases. |
| `test_compactness_range` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]),<br>        Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]),<br>    ],<br>) | none | 1 | For a square and a 100-by-2 rectangle, assert compactness in (0, 1]; no random or exhaustive geometric domain is sampled. |
| `test_centralized_shape_metrics` | pytest.mark.parametrize(<br>    ("geometry", "expected_length", "expected_width"),<br>    [<br>        (Polygon([(0, 0), (10, 0), (10, 10), (0, 10)]), 10.0, 10.0),<br>        (Polygon([(0, 0), (20, 0), (20, 10), (0, 10)]), 20.0, 10.0),<br>        (<br>            rotate(Polygon([(0, 0), (30, 0), (30, 10), (0, 10)]), 37),<br>            30.0,<br>            10.0,<br>        ),<br>        (Polygon([(0, 0), (100, 0), (100, 2), (0, 2)]), 100.0, 2.0),<br>    ],<br>) | none | 5 | For four declared rectangle cases, including one rotated 37 degrees, call parcel_shape_metrics_m once and assert expected dimensions, length≥width, expected ratio and compactness range on the returned ShapeMetrics. |
| `test_centralized_shape_metrics_support_multipolygon` | none | none | 2 | Pass the two separated squares to the centralized helper and assert the returned joint envelope dimensions 30 m by 10 m. |
| `test_centralized_shape_metrics_reject_invalid_geometry` | none | pytest.raises(InvalidGeometryError) | 0 | Require InvalidGeometryError from the centralized helper for a self-crossing polygon. |
| `test_centralized_shape_metrics_reject_zero_area_geometry` | none | pytest.raises(GeometryError) | 0 | Require the GeometryError base class from centralized shape computation on a collinear polygon; do not claim a specific positive-area branch was reached. |
| `test_centralized_shape_metrics_reject_geographic_crs` | none | pytest.raises(MetricCrsError) | 0 | Require MetricCrsError when the centralized helper receives the square with WGS84. |
| `test_non_geometry_inputs_raise_controlled_error` | pytest.mark.parametrize("geometry", [None, "polygon", 123, [], object()]) | pytest.raises(UnsupportedGeometryError) | 0 | Five exact inputs (None, polygon text, integer 123, empty list and object) must raise UnsupportedGeometryError from area_m2; no Shapely geometry parser is substituted. |
| `test_unsupported_geometry_family_raises_controlled_error` | none | pytest.raises(UnsupportedGeometryError) | 0 | Pass a real Point to the polygon-only area helper and require UnsupportedGeometryError. |
| `test_three_dimensional_parcel_is_rejected` | none | pytest.raises(UnsupportedGeometryError, match="two-dimensional") | 0 | Pass a real XYZ Polygon to area_m2 and require UnsupportedGeometryError matching two-dimensional. This test does not construct XYM or XYZM data. |
| `test_malformed_crs_inputs_raise_controlled_error` | pytest.mark.parametrize("crs", [None, object(), [], "not-a-crs"]) | pytest.raises(MetricCrsError) | 0 | For None, object, empty list and not-a-crs text, require MetricCrsError from area_m2 with a valid square. The malformed-CRS gate is exercised independently of malformed geometry. |

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
