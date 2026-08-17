# `tests/unit/test_profile_shape.py`

## File identity

- Repository path: `tests/unit/test_profile_shape.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `profile_shape` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `c571ddbee0b9ae0676cd75a637e01c08c8f3b8562f75d4a7e104e9ec891b9086`

## 1. Purpose

Provides complete unit and regression coverage for the `profile_shape` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- None.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import Point` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.stages.profile_shape import ( PROFILE_METRICS, ShapeProfileError, profile_shape_distribution, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_with_error_row`

**Signature**

```python
def _with_error_row(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

**Purpose**

Implements with error row according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `mixed`.

**Algorithm**

1. Computes `mixed` from `parcels.copy()`.
2. Computes `mixed.loc[9, 'shape_status']` from `'ERROR'`.
3. Iterates `column` over `(*PROFILE_METRICS, 'centroid_lat', 'centroid_lon')`. For each value: Computes `mixed.loc[9, column]` from `None`.
4. Returns `mixed`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `parcels.copy`.

**Known repository callers**

- `tests/unit/test_profile_shape.py` — `test_error_rows_are_excluded_from_buckets`
- `tests/unit/test_profile_shape.py` — `test_error_rows_are_excluded_from_percentiles`
- `tests/unit/test_profile_shape.py` — `test_mixed_valid_and_error_rows_are_counted`
- `tests/unit/test_profile_shape.py` — `test_scenario_percentages_use_valid_count`

**Tests**

- `tests/unit/test_profile_shape.py::test_error_rows_are_excluded_from_buckets`
- `tests/unit/test_profile_shape.py::test_error_rows_are_excluded_from_percentiles`
- `tests/unit/test_profile_shape.py::test_mixed_valid_and_error_rows_are_counted`
- `tests/unit/test_profile_shape.py::test_scenario_percentages_use_valid_count`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `parcels`

**Signature**

```python
def parcels() -> gpd.GeoDataFrame:
```

**Purpose**

Implements parcels according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'parcel_id': [f'parcel-{index}' for index in range(count)], 'shape_status': ['VALID'] * count, 'area_m2': [100.0 * (index + 1) for index in range(count)], 'length_m': [4.0, 17.5, 42.0, 76.5, 132.0, 216.0, 420.0, 900.0, 1650.0, 300.0], 'width_m': [4.0, 7.0, 12.0, 17.0, 22.0, 27.0, 35.0, 45.0, 55.0, 60.0], 'length_width_ratio': [1.0, 2.5, 3.5, 4.5, 6.0, 8.0, 12.0, 20.0, 30.0, 5.0]…`.

**Algorithm**

1. Computes `count` from `10`.
2. Returns `gpd.GeoDataFrame({'parcel_id': [f'parcel-{index}' for index in range(count)], 'shape_status': ['VALID'] * count, 'area_m2': [100.0 * (index + 1) for index in range(count)], 'length_m': [4.0, 17.5, 42.0, 76.5, 132.0, 216.0, 420.0, 900.0, 1650.0, 300.0], 'width_m': [4.0, 7.0, 12.0, 17.0, 22.0, 27.0, 35.0, 45.0, 55.0, 60.0], 'length_width_ratio': [1.0, 2.5, 3.…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Point`, `gpd.GeoDataFrame`, `range`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_percentile_calculation`

**Signature**

```python
def test_percentile_calculation(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `percentile calculation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 2 explicit setup/context statement(s).
- Computes `profile` from `profile_shape_distribution(parcels)`.
- Computes `area` from `profile.distributions['area_m2']`.

**Action**

- Calls `profile_shape_distribution`.

**Expected result**

- Direct assertions: `assert area['min'] == pytest.approx(100.0)`; `assert area['p50'] == pytest.approx(550.0)`; `assert area['max'] == pytest.approx(1000.0)`; `assert set(area) == {'min', 'p01', 'p05', 'p10', 'p25', 'p50', 'p75', 'p90', 'p95', 'p99', 'max'}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `percentile calculation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `profile_shape_distribution`, `pytest.approx`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_bucket_counts_sum_to_input_count`

**Signature**

```python
def test_bucket_counts_sum_to_input_count(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `bucket counts sum to input count` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 1 explicit setup/context statement(s).
- Computes `profile` from `profile_shape_distribution(parcels)`.

**Action**

- Calls `profile.compactness_buckets.values`, `profile.ratio_buckets.values`, `profile.width_buckets.values`, `profile_shape_distribution`, `sum`.

**Expected result**

- Direct assertions: `assert sum(profile.width_buckets.values()) == len(parcels)`; `assert sum(profile.ratio_buckets.values()) == len(parcels)`; `assert sum(profile.compactness_buckets.values()) == len(parcels)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `bucket counts sum to input count` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `len`, `profile.compactness_buckets.values`, `profile.ratio_buckets.values`, `profile.width_buckets.values`, `profile_shape_distribution`, `sum`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_existing_all_valid_behavior_is_unchanged`

**Signature**

```python
def test_existing_all_valid_behavior_is_unchanged(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `existing all valid behavior is unchanged` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 1 explicit setup/context statement(s).
- Computes `profile` from `profile_shape_distribution(parcels)`.

**Action**

- Calls `profile_shape_distribution`.

**Expected result**

- Direct assertions: `assert profile.input_count == 10`; `assert profile.valid_count == 10`; `assert profile.error_count == 0`; `assert profile.distributions['area_m2']['max'] == pytest.approx(1000.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `existing all valid behavior is unchanged` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `profile_shape_distribution`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_diagnostic_scenario_counts`

**Signature**

```python
def test_diagnostic_scenario_counts(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `diagnostic scenario counts` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 1 explicit setup/context statement(s).
- Computes `profile` from `profile_shape_distribution(parcels)`.

**Action**

- Calls `profile_shape_distribution`.

**Expected result**

- Direct assertions: `assert profile.scenarios['A'].retained_count == 8`; `assert profile.scenarios['B'].retained_count == 7`; `assert profile.scenarios['C'].retained_count == 6`; `assert profile.scenarios['D'].retained_count == 4`; `assert profile.scenarios['E'].retained_count == 2`; `assert profile.scenarios['F'].retained_count == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `diagnostic scenario counts` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `profile_shape_distribution`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_input_is_not_mutated`

**Signature**

```python
def test_input_is_not_mutated(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `input is not mutated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 1 explicit setup/context statement(s).
- Computes `original` from `parcels.copy(deep=True)`.

**Action**

- Calls `parcels.copy`, `pd.testing.assert_frame_equal`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `input is not mutated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.copy`, `pd.testing.assert_frame_equal`, `profile_shape_distribution`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_metric_fails`

**Signature**

```python
def test_missing_metric_fails(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `missing metric fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 2 explicit setup/context statement(s).
- Computes `without_width` from `parcels.drop(columns=['width_m'])`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='width_m')` and executes: Calls `profile_shape_distribution(without_width)` for its validation or side effect.

**Action**

- Calls `parcels.drop`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='width_m'): profile_shape_distribution(without_width)`.

**Regression protected**

- Protects the exact `missing metric fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.drop`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_parcel_id_fails`

**Signature**

```python
def test_null_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `null parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 3 explicit setup/context statement(s).
- Computes `with_null` from `parcels.copy()`.
- Computes `with_null.loc[0, 'parcel_id']` from `None`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='null')` and executes: Calls `profile_shape_distribution(with_null)` for its validation or side effect.

**Action**

- Calls `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='null'): profile_shape_distribution(with_null)`.

**Regression protected**

- Protects the exact `null parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.copy`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_id_fails`

**Signature**

```python
def test_duplicate_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `duplicate parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 3 explicit setup/context statement(s).
- Computes `with_duplicate` from `parcels.copy()`.
- Computes `with_duplicate.loc[1, 'parcel_id']` from `with_duplicate.loc[0, 'parcel_id']`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='unique')` and executes: Calls `profile_shape_distribution(with_duplicate)` for its validation or side effect.

**Action**

- Calls `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='unique'): profile_shape_distribution(with_duplicate)`.

**Regression protected**

- Protects the exact `duplicate parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.copy`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_crs_fails`

**Signature**

```python
def test_missing_crs_fails(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `missing crs fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 2 explicit setup/context statement(s).
- Computes `without_crs` from `parcels.set_crs(None, allow_override=True)`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='CRS')` and executes: Calls `profile_shape_distribution(without_crs)` for its validation or side effect.

**Action**

- Calls `parcels.set_crs`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='CRS'): profile_shape_distribution(without_crs)`.

**Regression protected**

- Protects the exact `missing crs fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.set_crs`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_metric_on_valid_shape_fails`

**Signature**

```python
def test_null_metric_on_valid_shape_fails(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `null metric on valid shape fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 3 explicit setup/context statement(s).
- Computes `with_null_metric` from `parcels.copy()`.
- Computes `with_null_metric.loc[0, 'compactness']` from `None`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='complete')` and executes: Calls `profile_shape_distribution(with_null_metric)` for its validation or side effect.

**Action**

- Calls `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='complete'): profile_shape_distribution(with_null_metric)`.

**Regression protected**

- Protects the exact `null metric on valid shape fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.copy`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mixed_valid_and_error_rows_are_counted`

**Signature**

```python
def test_mixed_valid_and_error_rows_are_counted(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `mixed valid and error rows are counted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 1 explicit setup/context statement(s).
- Computes `profile` from `profile_shape_distribution(_with_error_row(parcels))`.

**Action**

- Calls `_with_error_row`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: `assert profile.input_count == 10`; `assert profile.valid_count == 9`; `assert profile.error_count == 1`; `assert profile.input_count == profile.valid_count + profile.error_count`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `mixed valid and error rows are counted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_with_error_row`, `profile_shape_distribution`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_error_rows_are_excluded_from_percentiles`

**Signature**

```python
def test_error_rows_are_excluded_from_percentiles(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `error rows are excluded from percentiles` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 1 explicit setup/context statement(s).
- Computes `profile` from `profile_shape_distribution(_with_error_row(parcels))`.

**Action**

- Calls `_with_error_row`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: `assert profile.distributions['area_m2']['max'] == pytest.approx(900.0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `error rows are excluded from percentiles` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_with_error_row`, `profile_shape_distribution`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_error_rows_are_excluded_from_buckets`

**Signature**

```python
def test_error_rows_are_excluded_from_buckets(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `error rows are excluded from buckets` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 1 explicit setup/context statement(s).
- Computes `profile` from `profile_shape_distribution(_with_error_row(parcels))`.

**Action**

- Calls `_with_error_row`, `profile.compactness_buckets.values`, `profile.ratio_buckets.values`, `profile.width_buckets.values`, `profile_shape_distribution`, `sum`.

**Expected result**

- Direct assertions: `assert sum(profile.width_buckets.values()) == profile.valid_count == 9`; `assert sum(profile.ratio_buckets.values()) == profile.valid_count`; `assert sum(profile.compactness_buckets.values()) == profile.valid_count`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `error rows are excluded from buckets` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_with_error_row`, `profile.compactness_buckets.values`, `profile.ratio_buckets.values`, `profile.width_buckets.values`, `profile_shape_distribution`, `sum`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_scenario_percentages_use_valid_count`

**Signature**

```python
def test_scenario_percentages_use_valid_count(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `scenario percentages use valid count` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 1 explicit setup/context statement(s).
- Computes `profile` from `profile_shape_distribution(_with_error_row(parcels))`.

**Action**

- Calls `_with_error_row`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: `assert profile.scenarios['A'].retained_count == 7`; `assert profile.scenarios['A'].retained_percentage == pytest.approx(7 / 9 * 100)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `scenario percentages use valid count` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_with_error_row`, `profile_shape_distribution`, `pytest.approx`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unexpected_shape_status_fails`

**Signature**

```python
def test_unexpected_shape_status_fails(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `unexpected shape status fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 3 explicit setup/context statement(s).
- Computes `unexpected` from `parcels.copy()`.
- Computes `unexpected.loc[0, 'shape_status']` from `'UNKNOWN'`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='Unexpected')` and executes: Calls `profile_shape_distribution(unexpected)` for its validation or side effect.

**Action**

- Calls `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='Unexpected'): profile_shape_distribution(unexpected)`.

**Regression protected**

- Protects the exact `unexpected shape status fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.copy`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_non_finite_metric_on_valid_row_fails`

**Signature**

```python
def test_non_finite_metric_on_valid_row_fails(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `non finite metric on valid row fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 3 explicit setup/context statement(s).
- Computes `non_finite` from `parcels.copy()`.
- Computes `non_finite.loc[0, 'length_m']` from `float('inf')`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='finite')` and executes: Calls `profile_shape_distribution(non_finite)` for its validation or side effect.

**Action**

- Calls `float`, `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='finite'): profile_shape_distribution(non_finite)`.

**Regression protected**

- Protects the exact `non finite metric on valid row fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `float`, `parcels.copy`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zero_valid_rows_fails_clearly`

**Signature**

```python
def test_zero_valid_rows_fails_clearly(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `zero valid rows fails clearly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 3 explicit setup/context statement(s).
- Computes `errors_only` from `parcels.copy()`.
- Computes `errors_only['shape_status']` from `'ERROR'`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='At least one VALID')` and executes: Calls `profile_shape_distribution(errors_only)` for its validation or side effect.

**Action**

- Calls `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='At least one VALID'): profile_shape_distribution(errors_only)`.

**Regression protected**

- Protects the exact `zero valid rows fails clearly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.copy`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_shape_metrics_require_physical_domains`

**Signature**

```python
def test_valid_shape_metrics_require_physical_domains(
    parcels: gpd.GeoDataFrame,
    column: str,
    value: float,
    message: str,
) -> None:
```

**Purpose**

Protects the `valid shape metrics require physical domains` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `column`, `value`, `message`.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[0, column]` from `value`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match=message)` and executes: Calls `profile_shape_distribution(invalid)` for its validation or side effect.

**Action**

- Calls `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match=message): profile_shape_distribution(invalid)`.

**Regression protected**

- Protects the exact `valid shape metrics require physical domains` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.copy`, `profile_shape_distribution`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_shape_length_must_not_be_less_than_width`

**Signature**

```python
def test_valid_shape_length_must_not_be_less_than_width(
    parcels: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Protects the `valid shape length must not be less than width` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[0, 'length_m']` from `3`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='length_m must be at least width_m')` and executes: Calls `profile_shape_distribution(invalid)` for its validation or side effect.

**Action**

- Calls `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='length_m must be at least width_m'): profile_shape_distribution(invalid)`.

**Regression protected**

- Protects the exact `valid shape length must not be less than width` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.copy`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_shape_ratio_must_match_length_divided_by_width`

**Signature**

```python
def test_valid_shape_ratio_must_match_length_divided_by_width(
    parcels: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Protects the `valid shape ratio must match length divided by width` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[0, 'length_width_ratio']` from `2`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='must equal length_m / width_m')` and executes: Calls `profile_shape_distribution(invalid)` for its validation or side effect.

**Action**

- Calls `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='must equal length_m / width_m'): profile_shape_distribution(invalid)`.

**Regression protected**

- Protects the exact `valid shape ratio must match length divided by width` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `parcels.copy`, `profile_shape_distribution`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_shape_metrics_reject_bool_and_numeric_strings`

**Signature**

```python
def test_valid_shape_metrics_reject_bool_and_numeric_strings(
    parcels: gpd.GeoDataFrame,
    value: object,
) -> None:
```

**Purpose**

Protects the `valid shape metrics reject bool and numeric strings` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid['area_m2']` from `invalid['area_m2'].astype(object)`.
- Computes `invalid.loc[0, 'area_m2']` from `value`.
- Enters managed context(s) `pytest.raises(ShapeProfileError, match='numeric and finite')` and executes: Calls `profile_shape_distribution(invalid)` for its validation or side effect.

**Action**

- Calls `invalid['area_m2'].astype`, `parcels.copy`, `profile_shape_distribution`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ShapeProfileError, match='numeric and finite'): profile_shape_distribution(invalid)`.

**Regression protected**

- Protects the exact `valid shape metrics reject bool and numeric strings` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `invalid['area_m2'].astype`, `parcels.copy`, `profile_shape_distribution`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `A` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `B` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `C` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `D` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `E` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `F` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `centroid_lat` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `centroid_lon` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `compactness` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `length_width_ratio` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `max` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `min` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `p50` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
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
