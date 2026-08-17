# `tests/unit/test_geometry.py`

## File identity

- Repository path: `tests/unit/test_geometry.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `geometry` contracts exercised in this file.
- Source SHA256: `50e59494276ba92023531f77811de11ae09a23445948c59109ff4ea02539242c`

## 1. Purpose

Provides complete unit and regression coverage for the `geometry` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

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

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `square` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])`.
- Tests requesting it by parameter injection: `test_valid_polygon_in_lambert93`, `test_area_in_square_metres`, `test_perimeter_in_metres`, `test_centroid`, `test_metric_calculation_in_wgs84_fails`, `test_square_shape_metrics`, `test_elongated_rectangle_is_less_compact_than_square`, `test_shape_metrics_reject_geographic_crs`, `test_centralized_shape_metrics_reject_geographic_crs`, `test_malformed_crs_inputs_raise_controlled_error`.

**Complete fixture implementation**

```python
def square() -> Polygon:
    return Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
```

### `test_valid_polygon_in_lambert93`

**Purpose**

Exercises `valid polygon in lambert93`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert area_m2(square, LAMBERT93) > 0
```

**Regression protected**

Locks `valid polygon in lambert93` through the exact asserted conditions: `area_m2(square, LAMBERT93) > 0`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_polygon_in_lambert93(square: Polygon) -> None:
    assert area_m2(square, LAMBERT93) > 0
```

### `test_area_in_square_metres`

**Purpose**

Exercises `area in square metres`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert area_m2(square, LAMBERT93) == pytest.approx(100.0)
```

**Regression protected**

Locks `area in square metres` through the exact asserted conditions: `area_m2(square, LAMBERT93) == pytest.approx(100.0)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_area_in_square_metres(square: Polygon) -> None:
    assert area_m2(square, LAMBERT93) == pytest.approx(100.0)
```

### `test_perimeter_in_metres`

**Purpose**

Exercises `perimeter in metres`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert perimeter_m(square, LAMBERT93) == pytest.approx(40.0)
```

**Regression protected**

Locks `perimeter in metres` through the exact asserted conditions: `perimeter_m(square, LAMBERT93) == pytest.approx(40.0)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_perimeter_in_metres(square: Polygon) -> None:
    assert perimeter_m(square, LAMBERT93) == pytest.approx(40.0)
```

### `test_centroid`

**Purpose**

Exercises `centroid`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
center = centroid(square)
```

**Expected result**

```python
assert center.x == pytest.approx(5.0)
assert center.y == pytest.approx(5.0)
```

**Regression protected**

Locks `centroid` through the exact asserted conditions: `center.x == pytest.approx(5.0)`; `center.y == pytest.approx(5.0)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_centroid(square: Polygon) -> None:
    center = centroid(square)

    assert center.x == pytest.approx(5.0)
    assert center.y == pytest.approx(5.0)
```

### `test_metric_calculation_in_wgs84_fails`

**Purpose**

Exercises `metric calculation in wgs84 fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `metric_function`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(MetricCrsError):
        metric_function(square, WGS84)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_metric_calculation_in_wgs84_fails(
    square: Polygon, metric_function: object
) -> None:
    with pytest.raises(MetricCrsError):
        metric_function(square, WGS84)
```

### `test_empty_geometry_fails`

**Purpose**

Exercises `empty geometry fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(EmptyGeometryError):
        area_m2(Polygon(), LAMBERT93)
```

**Regression protected**

Locks `empty geometry fails`: the reproduced adversarial input must raise `EmptyGeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_empty_geometry_fails() -> None:
    with pytest.raises(EmptyGeometryError):
        area_m2(Polygon(), LAMBERT93)
```

### `test_invalid_geometry_fails`

**Purpose**

Exercises `invalid geometry fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert not bow_tie.is_valid
with pytest.raises(InvalidGeometryError):
        area_m2(bow_tie, LAMBERT93)
```

**Regression protected**

Locks `invalid geometry fails`: the reproduced adversarial input must raise `InvalidGeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_invalid_geometry_fails() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    assert not bow_tie.is_valid
    with pytest.raises(InvalidGeometryError):
        area_m2(bow_tie, LAMBERT93)
```

### `test_multipolygon`

**Purpose**

Exercises `multipolygon`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
geometry = MultiPolygon([first, second])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert area_m2(geometry, LAMBERT93) == pytest.approx(200.0)
assert perimeter_m(geometry, LAMBERT93) == pytest.approx(80.0)
```

**Regression protected**

Locks `multipolygon` through the exact asserted conditions: `area_m2(geometry, LAMBERT93) == pytest.approx(200.0)`; `perimeter_m(geometry, LAMBERT93) == pytest.approx(80.0)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_multipolygon() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
    geometry = MultiPolygon([first, second])

    assert area_m2(geometry, LAMBERT93) == pytest.approx(200.0)
    assert perimeter_m(geometry, LAMBERT93) == pytest.approx(80.0)
```

### `test_square_shape_metrics`

**Purpose**

Exercises `square shape metrics`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert approximate_length_m(square, LAMBERT93) == pytest.approx(10.0)
assert approximate_width_m(square, LAMBERT93) == pytest.approx(10.0)
assert length_width_ratio(square, LAMBERT93) == pytest.approx(1.0)
assert compactness_score(square, LAMBERT93) == pytest.approx(0.785398)
```

**Regression protected**

Locks `square shape metrics` through the exact asserted conditions: `approximate_length_m(square, LAMBERT93) == pytest.approx(10.0)`; `approximate_width_m(square, LAMBERT93) == pytest.approx(10.0)`; `length_width_ratio(square, LAMBERT93) == pytest.approx(1.0)`; `compactness_score(square, LAMBERT93) == pytest.approx(0.785398)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_square_shape_metrics(square: Polygon) -> None:
    assert approximate_length_m(square, LAMBERT93) == pytest.approx(10.0)
    assert approximate_width_m(square, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(square, LAMBERT93) == pytest.approx(1.0)
    assert compactness_score(square, LAMBERT93) == pytest.approx(0.785398)
```

### `test_simple_rectangle_shape_metrics`

**Purpose**

Exercises `simple rectangle shape metrics`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
rectangle = Polygon([(0, 0), (20, 0), (20, 10), (0, 10)])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert approximate_length_m(rectangle, LAMBERT93) == pytest.approx(20.0)
assert approximate_width_m(rectangle, LAMBERT93) == pytest.approx(10.0)
assert length_width_ratio(rectangle, LAMBERT93) == pytest.approx(2.0)
```

**Regression protected**

Locks `simple rectangle shape metrics` through the exact asserted conditions: `approximate_length_m(rectangle, LAMBERT93) == pytest.approx(20.0)`; `approximate_width_m(rectangle, LAMBERT93) == pytest.approx(10.0)`; `length_width_ratio(rectangle, LAMBERT93) == pytest.approx(2.0)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_simple_rectangle_shape_metrics() -> None:
    rectangle = Polygon([(0, 0), (20, 0), (20, 10), (0, 10)])

    assert approximate_length_m(rectangle, LAMBERT93) == pytest.approx(20.0)
    assert approximate_width_m(rectangle, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(rectangle, LAMBERT93) == pytest.approx(2.0)
```

### `test_rotated_rectangle_is_orientation_independent`

**Purpose**

Exercises `rotated rectangle is orientation independent`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
rectangle = Polygon([(0, 0), (30, 0), (30, 10), (0, 10)])
rotated = rotate(rectangle, 37)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert approximate_length_m(rotated, LAMBERT93) == pytest.approx(30.0)
assert approximate_width_m(rotated, LAMBERT93) == pytest.approx(10.0)
assert length_width_ratio(rotated, LAMBERT93) == pytest.approx(3.0)
```

**Regression protected**

Locks `rotated rectangle is orientation independent` through the exact asserted conditions: `approximate_length_m(rotated, LAMBERT93) == pytest.approx(30.0)`; `approximate_width_m(rotated, LAMBERT93) == pytest.approx(10.0)`; `length_width_ratio(rotated, LAMBERT93) == pytest.approx(3.0)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_rotated_rectangle_is_orientation_independent() -> None:
    rectangle = Polygon([(0, 0), (30, 0), (30, 10), (0, 10)])
    rotated = rotate(rectangle, 37)

    assert approximate_length_m(rotated, LAMBERT93) == pytest.approx(30.0)
    assert approximate_width_m(rotated, LAMBERT93) == pytest.approx(10.0)
    assert length_width_ratio(rotated, LAMBERT93) == pytest.approx(3.0)
```

### `test_elongated_rectangle_is_less_compact_than_square`

**Purpose**

Exercises `elongated rectangle is less compact than square`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
elongated = Polygon([(0, 0), (100, 0), (100, 2), (0, 2)])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert length_width_ratio(elongated, LAMBERT93) == pytest.approx(50.0)
assert compactness_score(square, LAMBERT93) > compactness_score(
        elongated, LAMBERT93
    )
```

**Regression protected**

Locks `elongated rectangle is less compact than square` through the exact asserted conditions: `length_width_ratio(elongated, LAMBERT93) == pytest.approx(50.0)`; `compactness_score(square, LAMBERT93) > compactness_score(elongated, LAMBERT93)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_elongated_rectangle_is_less_compact_than_square(square: Polygon) -> None:
    elongated = Polygon([(0, 0), (100, 0), (100, 2), (0, 2)])

    assert length_width_ratio(elongated, LAMBERT93) == pytest.approx(50.0)
    assert compactness_score(square, LAMBERT93) > compactness_score(
        elongated, LAMBERT93
    )
```

### `test_multipolygon_shape_metrics`

**Purpose**

Exercises `multipolygon shape metrics`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
geometry = MultiPolygon([first, second])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert approximate_length_m(geometry, LAMBERT93) == pytest.approx(30.0)
assert approximate_width_m(geometry, LAMBERT93) == pytest.approx(10.0)
assert 0 < compactness_score(geometry, LAMBERT93) <= 1
```

**Regression protected**

Locks `multipolygon shape metrics` through the exact asserted conditions: `approximate_length_m(geometry, LAMBERT93) == pytest.approx(30.0)`; `approximate_width_m(geometry, LAMBERT93) == pytest.approx(10.0)`; `0 < compactness_score(geometry, LAMBERT93) <= 1`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_multipolygon_shape_metrics() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
    geometry = MultiPolygon([first, second])

    assert approximate_length_m(geometry, LAMBERT93) == pytest.approx(30.0)
    assert approximate_width_m(geometry, LAMBERT93) == pytest.approx(10.0)
    assert 0 < compactness_score(geometry, LAMBERT93) <= 1
```

### `test_shape_metrics_reject_geographic_crs`

**Purpose**

Exercises `shape metrics reject geographic crs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(MetricCrsError):
        approximate_length_m(square, WGS84)
with pytest.raises(MetricCrsError):
        approximate_width_m(square, WGS84)
with pytest.raises(MetricCrsError):
        length_width_ratio(square, WGS84)
with pytest.raises(MetricCrsError):
        compactness_score(square, WGS84)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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

### `test_shape_metrics_reject_invalid_geometry`

**Purpose**

Exercises `shape metrics reject invalid geometry`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InvalidGeometryError):
        approximate_length_m(bow_tie, LAMBERT93)
```

**Regression protected**

Locks `shape metrics reject invalid geometry`: the reproduced adversarial input must raise `InvalidGeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_shape_metrics_reject_invalid_geometry() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    with pytest.raises(InvalidGeometryError):
        approximate_length_m(bow_tie, LAMBERT93)
```

### `test_shape_metrics_reject_empty_geometry`

**Purpose**

Exercises `shape metrics reject empty geometry`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(EmptyGeometryError):
        compactness_score(Polygon(), LAMBERT93)
```

**Regression protected**

Locks `shape metrics reject empty geometry`: the reproduced adversarial input must raise `EmptyGeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_shape_metrics_reject_empty_geometry() -> None:
    with pytest.raises(EmptyGeometryError):
        compactness_score(Polygon(), LAMBERT93)
```

### `test_zero_area_geometry_raises_controlled_error`

**Purpose**

Exercises `zero area geometry raises controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GeometryError):
        length_width_ratio(zero_area, LAMBERT93)
```

**Regression protected**

Locks `zero area geometry raises controlled error`: the reproduced adversarial input must raise `GeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_zero_area_geometry_raises_controlled_error() -> None:
    zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])

    with pytest.raises(GeometryError):
        length_width_ratio(zero_area, LAMBERT93)
```

### `test_length_is_always_at_least_width`

**Purpose**

Exercises `length is always at least width`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert approximate_length_m(geometry, LAMBERT93) >= approximate_width_m(
        geometry, LAMBERT93
    )
```

**Regression protected**

Locks `length is always at least width` through the exact asserted conditions: `approximate_length_m(geometry, LAMBERT93) >= approximate_width_m(geometry, LAMBERT93)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_length_is_always_at_least_width(geometry: Polygon) -> None:
    assert approximate_length_m(geometry, LAMBERT93) >= approximate_width_m(
        geometry, LAMBERT93
    )
```

### `test_compactness_range`

**Purpose**

Exercises `compactness range`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert 0 < compactness_score(geometry, LAMBERT93) <= 1
```

**Regression protected**

Locks `compactness range` through the exact asserted conditions: `0 < compactness_score(geometry, LAMBERT93) <= 1`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_compactness_range(geometry: Polygon) -> None:
    assert 0 < compactness_score(geometry, LAMBERT93) <= 1
```

### `test_centralized_shape_metrics`

**Purpose**

Exercises `centralized shape metrics`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_length`, `expected_width`, `geometry`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
metrics = parcel_shape_metrics_m(geometry, LAMBERT93)
```

**Expected result**

```python
assert metrics.length_m == pytest.approx(expected_length)
assert metrics.width_m == pytest.approx(expected_width)
assert metrics.length_m >= metrics.width_m
assert metrics.length_width_ratio == pytest.approx(expected_length / expected_width)
assert 0 < metrics.compactness <= 1
```

**Regression protected**

Locks `centralized shape metrics` through the exact asserted conditions: `metrics.length_m == pytest.approx(expected_length)`; `metrics.width_m == pytest.approx(expected_width)`; `metrics.length_m >= metrics.width_m`; `metrics.length_width_ratio == pytest.approx(expected_length / expected_width)`; plus 1 additional reproduced assertion(s).

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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

### `test_centralized_shape_metrics_support_multipolygon`

**Purpose**

Exercises `centralized shape metrics support multipolygon`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])
```

**Action**

```python
metrics = parcel_shape_metrics_m(MultiPolygon([first, second]), LAMBERT93)
```

**Expected result**

```python
assert metrics.length_m == pytest.approx(30.0)
assert metrics.width_m == pytest.approx(10.0)
```

**Regression protected**

Locks `centralized shape metrics support multipolygon` through the exact asserted conditions: `metrics.length_m == pytest.approx(30.0)`; `metrics.width_m == pytest.approx(10.0)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_centralized_shape_metrics_support_multipolygon() -> None:
    first = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    second = Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])

    metrics = parcel_shape_metrics_m(MultiPolygon([first, second]), LAMBERT93)

    assert metrics.length_m == pytest.approx(30.0)
    assert metrics.width_m == pytest.approx(10.0)
```

### `test_centralized_shape_metrics_reject_invalid_geometry`

**Purpose**

Exercises `centralized shape metrics reject invalid geometry`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InvalidGeometryError):
        parcel_shape_metrics_m(bow_tie, LAMBERT93)
```

**Regression protected**

Locks `centralized shape metrics reject invalid geometry`: the reproduced adversarial input must raise `InvalidGeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_centralized_shape_metrics_reject_invalid_geometry() -> None:
    bow_tie = Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])

    with pytest.raises(InvalidGeometryError):
        parcel_shape_metrics_m(bow_tie, LAMBERT93)
```

### `test_centralized_shape_metrics_reject_zero_area_geometry`

**Purpose**

Exercises `centralized shape metrics reject zero area geometry`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(GeometryError):
        parcel_shape_metrics_m(zero_area, LAMBERT93)
```

**Regression protected**

Locks `centralized shape metrics reject zero area geometry`: the reproduced adversarial input must raise `GeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_centralized_shape_metrics_reject_zero_area_geometry() -> None:
    zero_area = Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])

    with pytest.raises(GeometryError):
        parcel_shape_metrics_m(zero_area, LAMBERT93)
```

### `test_centralized_shape_metrics_reject_geographic_crs`

**Purpose**

Exercises `centralized shape metrics reject geographic crs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(MetricCrsError):
        parcel_shape_metrics_m(square, WGS84)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_centralized_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
    with pytest.raises(MetricCrsError):
        parcel_shape_metrics_m(square, WGS84)
```

### `test_non_geometry_inputs_raise_controlled_error`

**Purpose**

Exercises `non geometry inputs raise controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(UnsupportedGeometryError):
        area_m2(geometry, LAMBERT93)
```

**Regression protected**

Locks `non geometry inputs raise controlled error`: the reproduced adversarial input must raise `UnsupportedGeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_non_geometry_inputs_raise_controlled_error(geometry: object) -> None:
    with pytest.raises(UnsupportedGeometryError):
        area_m2(geometry, LAMBERT93)
```

### `test_unsupported_geometry_family_raises_controlled_error`

**Purpose**

Exercises `unsupported geometry family raises controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(UnsupportedGeometryError):
        area_m2(Point(0, 0), LAMBERT93)
```

**Regression protected**

Locks `unsupported geometry family raises controlled error`: the reproduced adversarial input must raise `UnsupportedGeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unsupported_geometry_family_raises_controlled_error() -> None:
    with pytest.raises(UnsupportedGeometryError):
        area_m2(Point(0, 0), LAMBERT93)
```

### `test_three_dimensional_parcel_is_rejected`

**Purpose**

Exercises `three dimensional parcel is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
polygon_z = Polygon([(0, 0, 1), (10, 0, 1), (10, 10, 1), (0, 10, 1)])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(UnsupportedGeometryError, match="two-dimensional"):
        area_m2(polygon_z, LAMBERT93)
```

**Regression protected**

Locks `three dimensional parcel is rejected`: the reproduced adversarial input must raise `UnsupportedGeometryError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_three_dimensional_parcel_is_rejected() -> None:
    polygon_z = Polygon([(0, 0, 1), (10, 0, 1), (10, 10, 1), (0, 10, 1)])

    with pytest.raises(UnsupportedGeometryError, match="two-dimensional"):
        area_m2(polygon_z, LAMBERT93)
```

### `test_malformed_crs_inputs_raise_controlled_error`

**Purpose**

Exercises `malformed crs inputs raise controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `crs`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(MetricCrsError):
        area_m2(square, crs)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_malformed_crs_inputs_raise_controlled_error(
    square: Polygon,
    crs: object,
) -> None:
    with pytest.raises(MetricCrsError):
        area_m2(square, crs)
```


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.


## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the test flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
