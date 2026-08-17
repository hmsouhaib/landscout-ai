# `tests/unit/test_enrich_shape.py`

## File identity

- Repository path: `tests/unit/test_enrich_shape.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `enrich_shape` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `ad4f6b2997ac30b29a5aaa182b882cc7aac0a50abf55b4d97126934b187af21b`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_shape` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- None.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from shapely.affinity import rotate` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import Point, Polygon` — required by the implementation paths and symbols documented below.
- `from shapely.geometry.base import BaseGeometry` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.geo import LAMBERT93, parcel_shape_metrics_m` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_shape import ( DERIVED_METRIC_COLUMNS, ShapeEnrichmentError, enrich_parcel_shapes, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_candidate_frame`

**Signature**

```python
def _candidate_frame(geometries: list[BaseGeometry]) -> gpd.GeoDataFrame:
```

**Purpose**

Implements candidate frame according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[BaseGeometry]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'parcel_id': [f'parcel-{index}' for index in range(len(geometries))], 'geometry_status': ['VALID'] * len(geometries), 'area_m2': list(projected.area)}, geometry=wgs84, crs='EPSG:4326')`.

**Algorithm**

1. Computes `projected` from `gpd.GeoSeries(geometries, crs='EPSG:2154')`.
2. Computes `wgs84` from `projected.to_crs('EPSG:4326')`.
3. Returns `gpd.GeoDataFrame({'parcel_id': [f'parcel-{index}' for index in range(len(geometries))], 'geometry_status': ['VALID'] * len(geometries), 'area_m2': list(projected.area)}, geometry=wgs84, crs='EPSG:4326')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `projected.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `gpd.GeoDataFrame`, `gpd.GeoSeries`, `len`, `list`, `projected.to_crs`, `range`.

**Known repository callers**

- `tests/unit/test_enrich_shape.py` — `test_centroid_coordinates`
- `tests/unit/test_enrich_shape.py` — `test_duplicate_parcel_id_fails`
- `tests/unit/test_enrich_shape.py` — `test_elongated_parcel`
- `tests/unit/test_enrich_shape.py` — `test_enrichment_matches_centralized_shape_metrics`
- `tests/unit/test_enrich_shape.py` — `test_enrichment_requires_exact_non_empty_parcel_ids`
- `tests/unit/test_enrich_shape.py` — `test_exact_parcel_ids_are_preserved`
- `tests/unit/test_enrich_shape.py` — `test_failed_geometry_does_not_remove_other_rows`
- `tests/unit/test_enrich_shape.py` — `test_missing_crs_fails`
- `tests/unit/test_enrich_shape.py` — `test_missing_parcel_id_fails`
- `tests/unit/test_enrich_shape.py` — `test_null_parcel_id_fails`
- `tests/unit/test_enrich_shape.py` — `test_output_geometry_remains_wgs84`
- `tests/unit/test_enrich_shape.py` — `test_rectangle_metrics`
- `tests/unit/test_enrich_shape.py` — `test_rotated_rectangle_metrics`
- `tests/unit/test_enrich_shape.py` — `test_shape_enrichment_rejects_noncanonical_geometry_status`
- `tests/unit/test_enrich_shape.py` — `test_square_metrics`
- `tests/unit/test_enrich_shape.py` — `test_valid_candidate_area_requires_strict_positive_finite_number`

**Tests**

- `tests/unit/test_enrich_shape.py::test_centroid_coordinates`
- `tests/unit/test_enrich_shape.py::test_duplicate_parcel_id_fails`
- `tests/unit/test_enrich_shape.py::test_elongated_parcel`
- `tests/unit/test_enrich_shape.py::test_enrichment_matches_centralized_shape_metrics`
- `tests/unit/test_enrich_shape.py::test_enrichment_requires_exact_non_empty_parcel_ids`
- `tests/unit/test_enrich_shape.py::test_exact_parcel_ids_are_preserved`
- `tests/unit/test_enrich_shape.py::test_failed_geometry_does_not_remove_other_rows`
- `tests/unit/test_enrich_shape.py::test_missing_crs_fails`
- `tests/unit/test_enrich_shape.py::test_missing_parcel_id_fails`
- `tests/unit/test_enrich_shape.py::test_null_parcel_id_fails`
- `tests/unit/test_enrich_shape.py::test_output_geometry_remains_wgs84`
- `tests/unit/test_enrich_shape.py::test_rectangle_metrics`
- `tests/unit/test_enrich_shape.py::test_rotated_rectangle_metrics`
- `tests/unit/test_enrich_shape.py::test_shape_enrichment_rejects_noncanonical_geometry_status`
- `tests/unit/test_enrich_shape.py::test_square_metrics`
- `tests/unit/test_enrich_shape.py::test_valid_candidate_area_requires_strict_positive_finite_number`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

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

- Declared return type: `Polygon`. Observed return expression(s): `Polygon([(600000, 6200000), (600010, 6200000), (600010, 6200010), (600000, 6200010)])`.

**Algorithm**

1. Returns `Polygon([(600000, 6200000), (600010, 6200000), (600010, 6200010), (600000, 6200010)])`.

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

### `test_square_metrics`

**Signature**

```python
def test_square_metrics(square: Polygon) -> None:
```

**Purpose**

Protects the `square metrics` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 2 explicit setup/context statement(s).
- Computes `enriched` from `enrich_parcel_shapes(_candidate_frame([square]))`.
- Computes `row` from `enriched.iloc[0]`.

**Action**

- Calls `_candidate_frame`, `enrich_parcel_shapes`.

**Expected result**

- Direct assertions: `assert row['shape_status'] == 'VALID'`; `assert row['length_m'] == pytest.approx(10.0, abs=0.01)`; `assert row['width_m'] == pytest.approx(10.0, abs=0.01)`; `assert row['length_width_ratio'] == pytest.approx(1.0, abs=0.001)`; `assert row['compactness'] == pytest.approx(0.785398)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `square metrics` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `enrich_parcel_shapes`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rectangle_metrics`

**Signature**

```python
def test_rectangle_metrics() -> None:
```

**Purpose**

Protects the `rectangle metrics` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `rectangle` from `Polygon([(600000, 6200000), (600020, 6200000), (600020, 6200010), (600000, 6200010)])`.
- Computes `row` from `enrich_parcel_shapes(_candidate_frame([rectangle])).iloc[0]`.

**Action**

- Calls `Polygon`, `_candidate_frame`, `enrich_parcel_shapes`.

**Expected result**

- Direct assertions: `assert row['length_m'] == pytest.approx(20.0, abs=0.01)`; `assert row['width_m'] == pytest.approx(10.0, abs=0.01)`; `assert row['length_width_ratio'] == pytest.approx(2.0, abs=0.001)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `rectangle metrics` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_candidate_frame`, `enrich_parcel_shapes`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rotated_rectangle_metrics`

**Signature**

```python
def test_rotated_rectangle_metrics() -> None:
```

**Purpose**

Protects the `rotated rectangle metrics` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `rectangle` from `Polygon([(600000, 6200000), (600030, 6200000), (600030, 6200010), (600000, 6200010)])`.
- Computes `rotated` from `rotate(rectangle, 37)`.
- Computes `row` from `enrich_parcel_shapes(_candidate_frame([rotated])).iloc[0]`.

**Action**

- Calls `Polygon`, `_candidate_frame`, `enrich_parcel_shapes`, `rotate`.

**Expected result**

- Direct assertions: `assert row['length_m'] == pytest.approx(30.0, abs=0.01)`; `assert row['width_m'] == pytest.approx(10.0, abs=0.01)`; `assert row['length_width_ratio'] == pytest.approx(3.0, abs=0.001)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `rotated rectangle metrics` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_candidate_frame`, `enrich_parcel_shapes`, `pytest.approx`, `rotate`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_elongated_parcel`

**Signature**

```python
def test_elongated_parcel() -> None:
```

**Purpose**

Protects the `elongated parcel` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `elongated` from `Polygon([(600000, 6200000), (600100, 6200000), (600100, 6200002), (600000, 6200002)])`.
- Computes `row` from `enrich_parcel_shapes(_candidate_frame([elongated])).iloc[0]`.

**Action**

- Calls `Polygon`, `_candidate_frame`, `enrich_parcel_shapes`.

**Expected result**

- Direct assertions: `assert row['length_width_ratio'] == pytest.approx(50.0, abs=0.01)`; `assert row['length_m'] >= row['width_m']`; `assert 0 <= row['compactness'] <= 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `elongated parcel` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_candidate_frame`, `enrich_parcel_shapes`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_centroid_coordinates`

**Signature**

```python
def test_centroid_coordinates(square: Polygon) -> None:
```

**Purpose**

Protects the `centroid coordinates` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 2 explicit setup/context statement(s).
- Computes `expected` from `gpd.GeoSeries([square.centroid], crs='EPSG:2154').to_crs('EPSG:4326').iloc[0]`.
- Computes `row` from `enrich_parcel_shapes(_candidate_frame([square])).iloc[0]`.

**Action**

- Calls `_candidate_frame`, `enrich_parcel_shapes`, `gpd.GeoSeries`, `gpd.GeoSeries([square.centroid], crs='EPSG:2154').to_crs`.

**Expected result**

- Direct assertions: `assert row['centroid_lat'] == pytest.approx(expected.y)`; `assert row['centroid_lon'] == pytest.approx(expected.x)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `centroid coordinates` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `enrich_parcel_shapes`, `gpd.GeoSeries`, `gpd.GeoSeries([square.centroid], crs='EPSG:2154').to_crs`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_output_geometry_remains_wgs84`

**Signature**

```python
def test_output_geometry_remains_wgs84(square: Polygon) -> None:
```

**Purpose**

Protects the `output geometry remains wgs84` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square])`.
- Computes `enriched` from `enrich_parcel_shapes(source)`.

**Action**

- Calls `_candidate_frame`, `enrich_parcel_shapes`, `enriched.crs.to_epsg`, `enriched.geometry.iloc[0].equals_exact`.

**Expected result**

- Direct assertions: `assert enriched.crs is not None`; `assert enriched.crs.to_epsg() == 4326`; `assert enriched.geometry.iloc[0].equals_exact(source.geometry.iloc[0], tolerance=0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `output geometry remains wgs84` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `enrich_parcel_shapes`, `enriched.crs.to_epsg`, `enriched.geometry.iloc[0].equals_exact`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_crs_fails`

**Signature**

```python
def test_missing_crs_fails(square: Polygon) -> None:
```

**Purpose**

Protects the `missing crs fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square]).set_crs(None, allow_override=True)`.
- Enters managed context(s) `pytest.raises(ShapeEnrichmentError, match='CRS')` and executes: Calls `enrich_parcel_shapes(source)` for its validation or side effect.

**Action**

- Calls `_candidate_frame`, `_candidate_frame([square]).set_crs`, `enrich_parcel_shapes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeEnrichmentError, match='CRS'): enrich_parcel_shapes(source)`.

**Regression protected**

- Protects the exact `missing crs fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `_candidate_frame([square]).set_crs`, `enrich_parcel_shapes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_parcel_id_fails`

**Signature**

```python
def test_missing_parcel_id_fails(square: Polygon) -> None:
```

**Purpose**

Protects the `missing parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square]).drop(columns=['parcel_id'])`.
- Enters managed context(s) `pytest.raises(ShapeEnrichmentError, match='parcel_id')` and executes: Calls `enrich_parcel_shapes(source)` for its validation or side effect.

**Action**

- Calls `_candidate_frame`, `_candidate_frame([square]).drop`, `enrich_parcel_shapes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeEnrichmentError, match='parcel_id'): enrich_parcel_shapes(source)`.

**Regression protected**

- Protects the exact `missing parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `_candidate_frame([square]).drop`, `enrich_parcel_shapes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_parcel_id_fails`

**Signature**

```python
def test_null_parcel_id_fails(square: Polygon) -> None:
```

**Purpose**

Protects the `null parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square])`.
- Computes `source.loc[0, 'parcel_id']` from `None`.
- Enters managed context(s) `pytest.raises(ShapeEnrichmentError, match='null')` and executes: Calls `enrich_parcel_shapes(source)` for its validation or side effect.

**Action**

- Calls `_candidate_frame`, `enrich_parcel_shapes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeEnrichmentError, match='null'): enrich_parcel_shapes(source)`.

**Regression protected**

- Protects the exact `null parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `enrich_parcel_shapes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_id_fails`

**Signature**

```python
def test_duplicate_parcel_id_fails(square: Polygon) -> None:
```

**Purpose**

Protects the `duplicate parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square, square])`.
- Computes `source.loc[1, 'parcel_id']` from `source.loc[0, 'parcel_id']`.
- Enters managed context(s) `pytest.raises(ShapeEnrichmentError, match='unique')` and executes: Calls `enrich_parcel_shapes(source)` for its validation or side effect.

**Action**

- Calls `_candidate_frame`, `enrich_parcel_shapes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeEnrichmentError, match='unique'): enrich_parcel_shapes(source)`.

**Regression protected**

- Protects the exact `duplicate parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `enrich_parcel_shapes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_enrichment_requires_exact_non_empty_parcel_ids`

**Signature**

```python
def test_enrichment_requires_exact_non_empty_parcel_ids(
    square: Polygon,
    parcel_id: object,
) -> None:
```

**Purpose**

Protects the `enrichment requires exact non empty parcel ids` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`, `parcel_id`.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square])`.
- Computes `source['parcel_id']` from `source['parcel_id'].astype(object)`.
- Computes `source.loc[0, 'parcel_id']` from `parcel_id`.
- Enters managed context(s) `pytest.raises(ShapeEnrichmentError, match='exact non-empty strings')` and executes: Calls `enrich_parcel_shapes(source)` for its validation or side effect.

**Action**

- Calls `_candidate_frame`, `enrich_parcel_shapes`, `source['parcel_id'].astype`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeEnrichmentError, match='exact non-empty strings'): enrich_parcel_shapes(source)`.

**Regression protected**

- Protects the exact `enrichment requires exact non empty parcel ids` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `enrich_parcel_shapes`, `pytest.mark.parametrize`, `pytest.raises`, `source['parcel_id'].astype`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_candidate_area_requires_strict_positive_finite_number`

**Signature**

```python
def test_valid_candidate_area_requires_strict_positive_finite_number(
    square: Polygon,
    area: object,
) -> None:
```

**Purpose**

Protects the `valid candidate area requires strict positive finite number` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`, `area`.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square])`.
- Computes `source['area_m2']` from `source['area_m2'].astype(object)`.
- Computes `source.loc[0, 'area_m2']` from `area`.
- Enters managed context(s) `pytest.raises(ShapeEnrichmentError, match='strict positive finite numeric')` and executes: Calls `enrich_parcel_shapes(source)` for its validation or side effect.

**Action**

- Calls `_candidate_frame`, `enrich_parcel_shapes`, `float`, `source['area_m2'].astype`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeEnrichmentError, match='strict positive finite numeric'): enrich_parcel_shapes(source)`.

**Regression protected**

- Protects the exact `valid candidate area requires strict positive finite number` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `enrich_parcel_shapes`, `float`, `pytest.mark.parametrize`, `pytest.raises`, `source['area_m2'].astype`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_failed_geometry_does_not_remove_other_rows`

**Signature**

```python
def test_failed_geometry_does_not_remove_other_rows(square: Polygon) -> None:
```

**Purpose**

Protects the `failed geometry does not remove other rows` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square, Point(600000, 6200000)])`.
- Computes `source.loc[1, 'geometry_status']` from `'INVALID'`.
- Computes `enriched` from `enrich_parcel_shapes(source)`.

**Action**

- Calls `Point`, `_candidate_frame`, `enrich_parcel_shapes`, `enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna`, `enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all`.

**Expected result**

- Direct assertions: `assert list(enriched['shape_status']) == ['VALID', 'ERROR']`; `assert enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `failed geometry does not remove other rows` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Point`, `_candidate_frame`, `enrich_parcel_shapes`, `enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna`, `enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all`, `list`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_parcel_ids_are_preserved`

**Signature**

```python
def test_exact_parcel_ids_are_preserved(square: Polygon) -> None:
```

**Purpose**

Protects the `exact parcel ids are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square, Point(600000, 6200000)])`.
- Computes `source.loc[1, 'geometry_status']` from `'INVALID'`.
- Computes `enriched` from `enrich_parcel_shapes(source)`.

**Action**

- Calls `Point`, `_candidate_frame`, `enrich_parcel_shapes`.

**Expected result**

- Direct assertions: `assert len(enriched) == len(source)`; `assert set(enriched['parcel_id']) == set(source['parcel_id'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact parcel ids are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Point`, `_candidate_frame`, `enrich_parcel_shapes`, `len`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_enrichment_matches_centralized_shape_metrics`

**Signature**

```python
def test_enrichment_matches_centralized_shape_metrics(square: Polygon) -> None:
```

**Purpose**

Protects the `enrichment matches centralized shape metrics` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_candidate_frame([square])`.
- Computes `expected_geometry` from `source.to_crs(LAMBERT93).geometry.iloc[0]`.
- Computes `expected` from `parcel_shape_metrics_m(expected_geometry, LAMBERT93)`.
- Computes `row` from `enrich_parcel_shapes(source).iloc[0]`.

**Action**

- Calls `_candidate_frame`, `enrich_parcel_shapes`, `parcel_shape_metrics_m`, `source.to_crs`.

**Expected result**

- Direct assertions: `assert row['length_m'] == pytest.approx(expected.length_m)`; `assert row['width_m'] == pytest.approx(expected.width_m)`; `assert row['length_width_ratio'] == pytest.approx(expected.length_width_ratio)`; `assert row['compactness'] == pytest.approx(expected.compactness)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `enrichment matches centralized shape metrics` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `enrich_parcel_shapes`, `parcel_shape_metrics_m`, `pytest.approx`, `source.to_crs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_enrichment_rejects_noncanonical_geometry_status`

**Signature**

```python
def test_shape_enrichment_rejects_noncanonical_geometry_status(
    square: Polygon,
    geometry_status: object,
) -> None:
```

**Purpose**

Protects the `shape enrichment rejects noncanonical geometry status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `square`, `geometry_status`.
- Contains 4 explicit setup/context statement(s).
- Computes `invalid` from `_candidate_frame([square])`.
- Computes `invalid['geometry_status']` from `invalid['geometry_status'].astype(object)`.
- Computes `invalid.loc[0, 'geometry_status']` from `geometry_status`.
- Enters managed context(s) `pytest.raises(ShapeEnrichmentError, match='geometry_status')` and executes: Calls `enrich_parcel_shapes(invalid)` for its validation or side effect.

**Action**

- Calls `_candidate_frame`, `enrich_parcel_shapes`, `invalid['geometry_status'].astype`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeEnrichmentError, match='geometry_status'): enrich_parcel_shapes(invalid)`.

**Regression protected**

- Protects the exact `shape enrichment rejects noncanonical geometry status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_candidate_frame`, `enrich_parcel_shapes`, `invalid['geometry_status'].astype`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `centroid_lat` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `centroid_lon` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `compactness` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `length_width_ratio` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `shape_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `width_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |

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
