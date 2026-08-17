# `tests/unit/test_geometry.py`

## File identity

- Repository path: `tests/unit/test_geometry.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `geometry` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `50e59494276ba92023531f77811de11ae09a23445948c59109ff4ea02539242c`

## 1. Purpose

Provides complete unit and regression coverage for the `geometry` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- None.

### Third-party

- `import pytest` — required by the implementation paths and symbols documented below.
- `from shapely.affinity import rotate` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import MultiPolygon, Point, Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.geo import ( LAMBERT93, WGS84, EmptyGeometryError, GeometryError, InvalidGeometryError, MetricCrsError, UnsupportedGeometryError, approximate_length_m, approximate_width_m, area_m2, centroid, compactness_score, length_width_ratio, parcel_shape_metrics_m, perimeter_m, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `square`

**Signature**

```python
def square() -> Polygon:
```

**Purpose**

Implements square according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `Polygon`. Observed return expression(s): `Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])`.

**Algorithm**

1. Returns `Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_polygon_in_lambert93`

**Signature**

```python
def test_valid_polygon_in_lambert93(square: Polygon) -> None:
```

**Purpose**

Protects the `valid polygon in lambert93` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `area_m2`.

**Expected result**

- Direct assertions: `assert area_m2(square, LAMBERT93) > 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid polygon in lambert93` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `area_m2`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_area_in_square_metres`

**Signature**

```python
def test_area_in_square_metres(square: Polygon) -> None:
```

**Purpose**

Protects the `area in square metres` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `area_m2`.

**Expected result**

- Direct assertions: `assert area_m2(square, LAMBERT93) == pytest.approx(100.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `area in square metres` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `area_m2`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_perimeter_in_metres`

**Signature**

```python
def test_perimeter_in_metres(square: Polygon) -> None:
```

**Purpose**

Protects the `perimeter in metres` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `perimeter_m`.

**Expected result**

- Direct assertions: `assert perimeter_m(square, LAMBERT93) == pytest.approx(40.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `perimeter in metres` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `perimeter_m`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_centroid`

**Signature**

```python
def test_centroid(square: Polygon) -> None:
```

**Purpose**

Protects the `centroid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 1 explicit setup/context statement(s).
- Computes `center` from `centroid(square)`.

**Action**

- Calls `centroid`.

**Expected result**

- Direct assertions: `assert center.x == pytest.approx(5.0)`; `assert center.y == pytest.approx(5.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `centroid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `centroid`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metric_calculation_in_wgs84_fails`

**Signature**

```python
def test_metric_calculation_in_wgs84_fails(
    square: Polygon, metric_function: object
) -> None:
```

**Purpose**

Protects the `metric calculation in wgs84 fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`, `metric_function`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(MetricCrsError)` and executes: Calls `metric_function(square, WGS84)` for its validation or side effect.

**Action**

- Calls `metric_function`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(MetricCrsError): metric_function(square, WGS84)`.

**Regression protected**

- Protects the exact `metric calculation in wgs84 fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `metric_function`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_empty_geometry_fails`

**Signature**

```python
def test_empty_geometry_fails() -> None:
```

**Purpose**

Protects the `empty geometry fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(EmptyGeometryError)` and executes: Calls `area_m2(Polygon(), LAMBERT93)` for its validation or side effect.

**Action**

- Calls `Polygon`, `area_m2`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(EmptyGeometryError): area_m2(Polygon(), LAMBERT93)`.

**Regression protected**

- Protects the exact `empty geometry fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `area_m2`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_geometry_fails`

**Signature**

```python
def test_invalid_geometry_fails() -> None:
```

**Purpose**

Protects the `invalid geometry fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `bow_tie` from `Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])`.
- Enters managed context(s) `pytest.raises(InvalidGeometryError)` and executes: Calls `area_m2(bow_tie, LAMBERT93)` for its validation or side effect.

**Action**

- Calls `Polygon`, `area_m2`.

**Expected result**

- Direct assertions: `assert not bow_tie.is_valid`.
- Expected exception contexts: `with pytest.raises(InvalidGeometryError): area_m2(bow_tie, LAMBERT93)`.

**Regression protected**

- Protects the exact `invalid geometry fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `area_m2`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_multipolygon`

**Signature**

```python
def test_multipolygon() -> None:
```

**Purpose**

Protects the `multipolygon` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `first` from `Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])`.
- Computes `second` from `Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])`.
- Computes `geometry` from `MultiPolygon([first, second])`.

**Action**

- Calls `MultiPolygon`, `Polygon`, `area_m2`, `perimeter_m`.

**Expected result**

- Direct assertions: `assert area_m2(geometry, LAMBERT93) == pytest.approx(200.0)`; `assert perimeter_m(geometry, LAMBERT93) == pytest.approx(80.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `multipolygon` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `Polygon`, `area_m2`, `perimeter_m`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_square_shape_metrics`

**Signature**

```python
def test_square_shape_metrics(square: Polygon) -> None:
```

**Purpose**

Protects the `square shape metrics` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `approximate_length_m`, `approximate_width_m`, `compactness_score`.

**Expected result**

- Direct assertions: `assert approximate_length_m(square, LAMBERT93) == pytest.approx(10.0)`; `assert approximate_width_m(square, LAMBERT93) == pytest.approx(10.0)`; `assert length_width_ratio(square, LAMBERT93) == pytest.approx(1.0)`; `assert compactness_score(square, LAMBERT93) == pytest.approx(0.785398)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `square shape metrics` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `approximate_length_m`, `approximate_width_m`, `compactness_score`, `length_width_ratio`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_simple_rectangle_shape_metrics`

**Signature**

```python
def test_simple_rectangle_shape_metrics() -> None:
```

**Purpose**

Protects the `simple rectangle shape metrics` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `rectangle` from `Polygon([(0, 0), (20, 0), (20, 10), (0, 10)])`.

**Action**

- Calls `Polygon`, `approximate_length_m`, `approximate_width_m`.

**Expected result**

- Direct assertions: `assert approximate_length_m(rectangle, LAMBERT93) == pytest.approx(20.0)`; `assert approximate_width_m(rectangle, LAMBERT93) == pytest.approx(10.0)`; `assert length_width_ratio(rectangle, LAMBERT93) == pytest.approx(2.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `simple rectangle shape metrics` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `approximate_length_m`, `approximate_width_m`, `length_width_ratio`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rotated_rectangle_is_orientation_independent`

**Signature**

```python
def test_rotated_rectangle_is_orientation_independent() -> None:
```

**Purpose**

Protects the `rotated rectangle is orientation independent` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `rectangle` from `Polygon([(0, 0), (30, 0), (30, 10), (0, 10)])`.
- Computes `rotated` from `rotate(rectangle, 37)`.

**Action**

- Calls `Polygon`, `approximate_length_m`, `approximate_width_m`, `rotate`.

**Expected result**

- Direct assertions: `assert approximate_length_m(rotated, LAMBERT93) == pytest.approx(30.0)`; `assert approximate_width_m(rotated, LAMBERT93) == pytest.approx(10.0)`; `assert length_width_ratio(rotated, LAMBERT93) == pytest.approx(3.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `rotated rectangle is orientation independent` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `approximate_length_m`, `approximate_width_m`, `length_width_ratio`, `pytest.approx`, `rotate`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_elongated_rectangle_is_less_compact_than_square`

**Signature**

```python
def test_elongated_rectangle_is_less_compact_than_square(square: Polygon) -> None:
```

**Purpose**

Protects the `elongated rectangle is less compact than square` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 1 explicit setup/context statement(s).
- Computes `elongated` from `Polygon([(0, 0), (100, 0), (100, 2), (0, 2)])`.

**Action**

- Calls `Polygon`, `compactness_score`.

**Expected result**

- Direct assertions: `assert length_width_ratio(elongated, LAMBERT93) == pytest.approx(50.0)`; `assert compactness_score(square, LAMBERT93) > compactness_score(elongated, LAMBERT93)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `elongated rectangle is less compact than square` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `compactness_score`, `length_width_ratio`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_multipolygon_shape_metrics`

**Signature**

```python
def test_multipolygon_shape_metrics() -> None:
```

**Purpose**

Protects the `multipolygon shape metrics` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `first` from `Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])`.
- Computes `second` from `Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])`.
- Computes `geometry` from `MultiPolygon([first, second])`.

**Action**

- Calls `MultiPolygon`, `Polygon`, `approximate_length_m`, `approximate_width_m`, `compactness_score`.

**Expected result**

- Direct assertions: `assert approximate_length_m(geometry, LAMBERT93) == pytest.approx(30.0)`; `assert approximate_width_m(geometry, LAMBERT93) == pytest.approx(10.0)`; `assert 0 < compactness_score(geometry, LAMBERT93) <= 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `multipolygon shape metrics` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `Polygon`, `approximate_length_m`, `approximate_width_m`, `compactness_score`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_metrics_reject_geographic_crs`

**Signature**

```python
def test_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
```

**Purpose**

Protects the `shape metrics reject geographic crs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 4 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(MetricCrsError)` and executes: Calls `approximate_length_m(square, WGS84)` for its validation or side effect.
- Enters managed context(s) `pytest.raises(MetricCrsError)` and executes: Calls `approximate_width_m(square, WGS84)` for its validation or side effect.
- Enters managed context(s) `pytest.raises(MetricCrsError)` and executes: Calls `length_width_ratio(square, WGS84)` for its validation or side effect.
- Enters managed context(s) `pytest.raises(MetricCrsError)` and executes: Calls `compactness_score(square, WGS84)` for its validation or side effect.

**Action**

- Calls `approximate_length_m`, `approximate_width_m`, `compactness_score`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(MetricCrsError): approximate_length_m(square, WGS84)`; `with pytest.raises(MetricCrsError): approximate_width_m(square, WGS84)`; `with pytest.raises(MetricCrsError): length_width_ratio(square, WGS84)`; `with pytest.raises(MetricCrsError): compactness_score(square, WGS84)`.

**Regression protected**

- Protects the exact `shape metrics reject geographic crs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `approximate_length_m`, `approximate_width_m`, `compactness_score`, `length_width_ratio`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_metrics_reject_invalid_geometry`

**Signature**

```python
def test_shape_metrics_reject_invalid_geometry() -> None:
```

**Purpose**

Protects the `shape metrics reject invalid geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `bow_tie` from `Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])`.
- Enters managed context(s) `pytest.raises(InvalidGeometryError)` and executes: Calls `approximate_length_m(bow_tie, LAMBERT93)` for its validation or side effect.

**Action**

- Calls `Polygon`, `approximate_length_m`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InvalidGeometryError): approximate_length_m(bow_tie, LAMBERT93)`.

**Regression protected**

- Protects the exact `shape metrics reject invalid geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `approximate_length_m`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_metrics_reject_empty_geometry`

**Signature**

```python
def test_shape_metrics_reject_empty_geometry() -> None:
```

**Purpose**

Protects the `shape metrics reject empty geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(EmptyGeometryError)` and executes: Calls `compactness_score(Polygon(), LAMBERT93)` for its validation or side effect.

**Action**

- Calls `Polygon`, `compactness_score`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(EmptyGeometryError): compactness_score(Polygon(), LAMBERT93)`.

**Regression protected**

- Protects the exact `shape metrics reject empty geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `compactness_score`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zero_area_geometry_raises_controlled_error`

**Signature**

```python
def test_zero_area_geometry_raises_controlled_error() -> None:
```

**Purpose**

Protects the `zero area geometry raises controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `zero_area` from `Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])`.
- Enters managed context(s) `pytest.raises(GeometryError)` and executes: Calls `length_width_ratio(zero_area, LAMBERT93)` for its validation or side effect.

**Action**

- Calls `Polygon`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GeometryError): length_width_ratio(zero_area, LAMBERT93)`.

**Regression protected**

- Protects the exact `zero area geometry raises controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `length_width_ratio`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_length_is_always_at_least_width`

**Signature**

```python
def test_length_is_always_at_least_width(geometry: Polygon) -> None:
```

**Purpose**

Protects the `length is always at least width` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `Polygon`, `approximate_length_m`, `approximate_width_m`, `rotate`.

**Expected result**

- Direct assertions: `assert approximate_length_m(geometry, LAMBERT93) >= approximate_width_m(geometry, LAMBERT93)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `length is always at least width` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `approximate_length_m`, `approximate_width_m`, `pytest.mark.parametrize`, `rotate`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_compactness_range`

**Signature**

```python
def test_compactness_range(geometry: Polygon) -> None:
```

**Purpose**

Protects the `compactness range` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `Polygon`, `compactness_score`.

**Expected result**

- Direct assertions: `assert 0 < compactness_score(geometry, LAMBERT93) <= 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `compactness range` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `compactness_score`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_centralized_shape_metrics`

**Signature**

```python
def test_centralized_shape_metrics(
    geometry: Polygon, expected_length: float, expected_width: float
) -> None:
```

**Purpose**

Protects the `centralized shape metrics` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`, `expected_length`, `expected_width`.
- Contains 1 explicit setup/context statement(s).
- Computes `metrics` from `parcel_shape_metrics_m(geometry, LAMBERT93)`.

**Action**

- Calls `Polygon`, `parcel_shape_metrics_m`, `rotate`.

**Expected result**

- Direct assertions: `assert metrics.length_m == pytest.approx(expected_length)`; `assert metrics.width_m == pytest.approx(expected_width)`; `assert metrics.length_m >= metrics.width_m`; `assert metrics.length_width_ratio == pytest.approx(expected_length / expected_width)`; `assert 0 < metrics.compactness <= 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `centralized shape metrics` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `parcel_shape_metrics_m`, `pytest.approx`, `pytest.mark.parametrize`, `rotate`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_centralized_shape_metrics_support_multipolygon`

**Signature**

```python
def test_centralized_shape_metrics_support_multipolygon() -> None:
```

**Purpose**

Protects the `centralized shape metrics support multipolygon` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `first` from `Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])`.
- Computes `second` from `Polygon([(20, 0), (30, 0), (30, 10), (20, 10)])`.
- Computes `metrics` from `parcel_shape_metrics_m(MultiPolygon([first, second]), LAMBERT93)`.

**Action**

- Calls `MultiPolygon`, `Polygon`, `parcel_shape_metrics_m`.

**Expected result**

- Direct assertions: `assert metrics.length_m == pytest.approx(30.0)`; `assert metrics.width_m == pytest.approx(10.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `centralized shape metrics support multipolygon` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `Polygon`, `parcel_shape_metrics_m`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_centralized_shape_metrics_reject_invalid_geometry`

**Signature**

```python
def test_centralized_shape_metrics_reject_invalid_geometry() -> None:
```

**Purpose**

Protects the `centralized shape metrics reject invalid geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `bow_tie` from `Polygon([(0, 0), (10, 10), (0, 10), (10, 0)])`.
- Enters managed context(s) `pytest.raises(InvalidGeometryError)` and executes: Calls `parcel_shape_metrics_m(bow_tie, LAMBERT93)` for its validation or side effect.

**Action**

- Calls `Polygon`, `parcel_shape_metrics_m`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InvalidGeometryError): parcel_shape_metrics_m(bow_tie, LAMBERT93)`.

**Regression protected**

- Protects the exact `centralized shape metrics reject invalid geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `parcel_shape_metrics_m`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_centralized_shape_metrics_reject_zero_area_geometry`

**Signature**

```python
def test_centralized_shape_metrics_reject_zero_area_geometry() -> None:
```

**Purpose**

Protects the `centralized shape metrics reject zero area geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `zero_area` from `Polygon([(0, 0), (1, 0), (2, 0), (0, 0)])`.
- Enters managed context(s) `pytest.raises(GeometryError)` and executes: Calls `parcel_shape_metrics_m(zero_area, LAMBERT93)` for its validation or side effect.

**Action**

- Calls `Polygon`, `parcel_shape_metrics_m`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(GeometryError): parcel_shape_metrics_m(zero_area, LAMBERT93)`.

**Regression protected**

- Protects the exact `centralized shape metrics reject zero area geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `parcel_shape_metrics_m`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_centralized_shape_metrics_reject_geographic_crs`

**Signature**

```python
def test_centralized_shape_metrics_reject_geographic_crs(square: Polygon) -> None:
```

**Purpose**

Protects the `centralized shape metrics reject geographic crs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(MetricCrsError)` and executes: Calls `parcel_shape_metrics_m(square, WGS84)` for its validation or side effect.

**Action**

- Calls `parcel_shape_metrics_m`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(MetricCrsError): parcel_shape_metrics_m(square, WGS84)`.

**Regression protected**

- Protects the exact `centralized shape metrics reject geographic crs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcel_shape_metrics_m`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_non_geometry_inputs_raise_controlled_error`

**Signature**

```python
def test_non_geometry_inputs_raise_controlled_error(geometry: object) -> None:
```

**Purpose**

Protects the `non geometry inputs raise controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(UnsupportedGeometryError)` and executes: Calls `area_m2(geometry, LAMBERT93)` for its validation or side effect.

**Action**

- Calls `area_m2`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(UnsupportedGeometryError): area_m2(geometry, LAMBERT93)`.

**Regression protected**

- Protects the exact `non geometry inputs raise controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `area_m2`, `object`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsupported_geometry_family_raises_controlled_error`

**Signature**

```python
def test_unsupported_geometry_family_raises_controlled_error() -> None:
```

**Purpose**

Protects the `unsupported geometry family raises controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(UnsupportedGeometryError)` and executes: Calls `area_m2(Point(0, 0), LAMBERT93)` for its validation or side effect.

**Action**

- Calls `Point`, `area_m2`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(UnsupportedGeometryError): area_m2(Point(0, 0), LAMBERT93)`.

**Regression protected**

- Protects the exact `unsupported geometry family raises controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Point`, `area_m2`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_three_dimensional_parcel_is_rejected`

**Signature**

```python
def test_three_dimensional_parcel_is_rejected() -> None:
```

**Purpose**

Protects the `three dimensional parcel is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `polygon_z` from `Polygon([(0, 0, 1), (10, 0, 1), (10, 10, 1), (0, 10, 1)])`.
- Enters managed context(s) `pytest.raises(UnsupportedGeometryError, match='two-dimensional')` and executes: Calls `area_m2(polygon_z, LAMBERT93)` for its validation or side effect.

**Action**

- Calls `Polygon`, `area_m2`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(UnsupportedGeometryError, match='two-dimensional'): area_m2(polygon_z, LAMBERT93)`.

**Regression protected**

- Protects the exact `three dimensional parcel is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `area_m2`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_crs_inputs_raise_controlled_error`

**Signature**

```python
def test_malformed_crs_inputs_raise_controlled_error(
    square: Polygon,
    crs: object,
) -> None:
```

**Purpose**

Protects the `malformed crs inputs raise controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`, `crs`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(MetricCrsError)` and executes: Calls `area_m2(square, crs)` for its validation or side effect.

**Action**

- Calls `area_m2`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(MetricCrsError): area_m2(square, crs)`.

**Regression protected**

- Protects the exact `malformed crs inputs raise controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `area_m2`, `object`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

No DataFrame/GeoDataFrame column is referenced directly. Object and scalar contracts are documented through classes, parameters, returns, constants, and validators.

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `test` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
