# `tests/unit/test_filter_shape.py`

## File identity

- Repository path: `tests/unit/test_filter_shape.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `92d7ea6f3b6c3ae3c5edf33cfbab1db9ca6699840bafeba28fd1667bdbf9d81b`

## 1. Purpose

Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- None.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.config import ShapeCalibrationConfig, ShapeScreeningConfig` — required by the implementation paths and symbols documented below.
- `from landscout.stages.filter_parcels import ( ParcelFilterError, filter_parcels_by_shape, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_shape_config`

**Signature**

```python
def _shape_config(
    *,
    min_width_m: float = 15,
    max_length_width_ratio: float = 10,
    policy_version: str = "test_policy_v1",
) -> ShapeScreeningConfig:
```

**Purpose**

Implements shape config according to the exact implementation and guards in this file.

**Inputs**

- `min_width_m` (`float`; optional/default `15`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `max_length_width_ratio` (`float`; optional/default `10`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_version` (`str`; optional/default `'test_policy_v1'`) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ShapeScreeningConfig`. Observed return expression(s): `ShapeScreeningConfig(enabled=True, min_width_m=min_width_m, max_length_width_ratio=max_length_width_ratio, calibration=ShapeCalibrationConfig(policy_version=policy_version, method='unit_test', calibration_scope='test fixture', sample_size=10, calibrated_at='2026-08-11', target_retention_pct=90, observed_retention_pct=90))`.

**Algorithm**

1. Returns `ShapeScreeningConfig(enabled=True, min_width_m=min_width_m, max_length_width_ratio=max_length_width_ratio, calibration=ShapeCalibrationConfig(policy_version=policy_version, method='unit_test', calibration_scope='test fixture', sample_size=10, calibrated_at='2026-08-11', target_retention_pct=90, observed_retention_pct=90))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ShapeCalibrationConfig`, `ShapeScreeningConfig`.

**Known repository callers**

- `tests/unit/test_filter_shape.py` — `shape_config`
- `tests/unit/test_filter_shape.py` — `test_different_configs_change_results_for_same_parcels`

**Tests**

- `tests/unit/test_filter_shape.py::test_different_configs_change_results_for_same_parcels`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `shape_config`

**Signature**

```python
def shape_config() -> ShapeScreeningConfig:
```

**Purpose**

Implements shape config according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `ShapeScreeningConfig`. Observed return expression(s): `_shape_config()`.

**Algorithm**

1. Returns `_shape_config()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_shape_config`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

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

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'parcel_id': ['at-boundaries', 'passing', 'width-below', 'ratio-above', 'shape-error', 'width-unknown', 'ratio-unknown', 'both-unknown', 'ratio-unknown-width-below', 'both-thresholds-fail'], 'shape_status': ['VALID', 'VALID', 'VALID', 'VALID', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'VALID'], 'width_m': [15.0, 20.0, 14.9, 16.0, None, None, 20.0, None, 14.0, 14.0], 'length_w…`.

**Algorithm**

1. Computes `geometry` from `Polygon([(2.0, 43.0), (2.01, 43.0), (2.01, 43.01), (2.0, 43.0)])`.
2. Returns `gpd.GeoDataFrame({'parcel_id': ['at-boundaries', 'passing', 'width-below', 'ratio-above', 'shape-error', 'width-unknown', 'ratio-unknown', 'both-unknown', 'ratio-unknown-width-below', 'both-thresholds-fail'], 'shape_status': ['VALID', 'VALID', 'VALID', 'VALID', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'VALID'], 'width_m': [15.0, 20.0, 14.9, 16.0, None, …`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Polygon`, `gpd.GeoDataFrame`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_width_and_ratio_boundaries_are_retained`

**Signature**

```python
def test_exact_width_and_ratio_boundaries_are_retained(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `exact width and ratio boundaries are retained` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 1 explicit setup/context statement(s).
- Computes `(retained, _)` from `filter_parcels_by_shape(parcels, shape_config)`.

**Action**

- Calls `filter_parcels_by_shape`.

**Expected result**

- Direct assertions: `assert 'at-boundaries' in set(retained['parcel_id'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact width and ratio boundaries are retained` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rejected_parcel_has_expected_primary_reason`

**Signature**

```python
def test_rejected_parcel_has_expected_primary_reason(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
```

**Purpose**

Protects the `rejected parcel has expected primary reason` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`, `parcel_id`, `expected_reason`.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, rejected)` from `filter_parcels_by_shape(parcels, shape_config)`.
- Computes `row` from `rejected.loc[rejected['parcel_id'] == parcel_id].iloc[0]`.

**Action**

- Calls `filter_parcels_by_shape`.

**Expected result**

- Direct assertions: `assert row['shape_rejection_reason'] == expected_reason`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `rejected parcel has expected primary reason` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rejection_reason_precedence_is_deterministic`

**Signature**

```python
def test_rejection_reason_precedence_is_deterministic(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
```

**Purpose**

Protects the `rejection reason precedence is deterministic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`, `parcel_id`, `expected_reason`.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, rejected)` from `filter_parcels_by_shape(parcels, shape_config)`.
- Computes `reason` from `rejected.set_index('parcel_id').loc[parcel_id, 'shape_rejection_reason']`.

**Action**

- Calls `filter_parcels_by_shape`, `rejected.set_index`.

**Expected result**

- Direct assertions: `assert reason == expected_reason`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `rejection reason precedence is deterministic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `pytest.mark.parametrize`, `rejected.set_index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_error_precedence_does_not_inspect_metrics`

**Signature**

```python
def test_shape_error_precedence_does_not_inspect_metrics(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `shape error precedence does not inspect metrics` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 8 explicit setup/context statement(s).
- Computes `with_error_payload` from `parcels.copy()`.
- Computes `with_error_payload['width_m']` from `with_error_payload['width_m'].astype(object)`.
- Computes `with_error_payload['length_width_ratio']` from `with_error_payload['length_width_ratio'].astype(object)`.
- Computes `error_row` from `with_error_payload['parcel_id'] == 'shape-error'`.
- Computes `with_error_payload.loc[error_row, 'width_m']` from `'unavailable'`.
- Computes `with_error_payload.loc[error_row, 'length_width_ratio']` from `'unavailable'`.
- Computes `(_, rejected)` from `filter_parcels_by_shape(with_error_payload, shape_config)`.
- Computes `reason` from `rejected.set_index('parcel_id').loc['shape-error', 'shape_rejection_reason']`.

**Action**

- Calls `filter_parcels_by_shape`, `parcels.copy`, `rejected.set_index`, `with_error_payload['length_width_ratio'].astype`, `with_error_payload['width_m'].astype`.

**Expected result**

- Direct assertions: `assert reason == 'SHAPE_ERROR'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `shape error precedence does not inspect metrics` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `parcels.copy`, `rejected.set_index`, `with_error_payload['length_width_ratio'].astype`, `with_error_payload['width_m'].astype`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_enabled_outputs_record_active_policy_metadata`

**Signature**

```python
def test_enabled_outputs_record_active_policy_metadata(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `enabled outputs record active policy metadata` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 1 explicit setup/context statement(s).
- Computes `(retained, rejected)` from `filter_parcels_by_shape(parcels, shape_config)`.

**Action**

- Calls `filter_parcels_by_shape`.

**Expected result**

- Direct assertions: `assert 'shape_rejection_reason' not in retained.columns`; `assert set(output['shape_policy_version']) == {'test_policy_v1'}`; `assert set(output['shape_policy_min_width_m']) == {15.0}`; `assert set(output['shape_policy_max_ratio']) == {10.0}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `enabled outputs record active policy metadata` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_enabled_partition_preserves_exact_ids_and_crs`

**Signature**

```python
def test_enabled_partition_preserves_exact_ids_and_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `enabled partition preserves exact ids and crs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `(retained, rejected)` from `filter_parcels_by_shape(parcels, shape_config)`.
- Computes `retained_ids` from `set(retained['parcel_id'])`.
- Computes `rejected_ids` from `set(rejected['parcel_id'])`.

**Action**

- Calls `filter_parcels_by_shape`, `rejected['parcel_id'].duplicated`, `rejected['parcel_id'].duplicated().any`, `retained['parcel_id'].duplicated`, `retained['parcel_id'].duplicated().any`, `retained_ids.isdisjoint`.

**Expected result**

- Direct assertions: `assert len(parcels) == len(retained) + len(rejected)`; `assert retained_ids.isdisjoint(rejected_ids)`; `assert retained_ids | rejected_ids == set(parcels['parcel_id'])`; `assert not retained['parcel_id'].duplicated().any()`; `assert not rejected['parcel_id'].duplicated().any()`; `assert retained.crs == parcels.crs`; `assert rejected.crs == parcels.crs`; `assert 'compactness' in retained.columns`; `assert 'compactness' in rejected.columns`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `enabled partition preserves exact ids and crs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `len`, `rejected['parcel_id'].duplicated`, `rejected['parcel_id'].duplicated().any`, `retained['parcel_id'].duplicated`, `retained['parcel_id'].duplicated().any`, `retained_ids.isdisjoint`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_filter_does_not_mutate_input`

**Signature**

```python
def test_filter_does_not_mutate_input(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `filter does not mutate input` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 1 explicit setup/context statement(s).
- Computes `original` from `parcels.copy(deep=True)`.

**Action**

- Calls `filter_parcels_by_shape`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `filter does not mutate input` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `assert_geodataframe_equal`, `filter_parcels_by_shape`, `parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_required_column_fails`

**Signature**

```python
def test_missing_required_column_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
```

**Purpose**

Protects the `missing required column fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`, `column`.
- Contains 2 explicit setup/context statement(s).
- Computes `missing_column` from `parcels.drop(columns=[column])`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='Missing required shape columns')` and executes: Calls `filter_parcels_by_shape(missing_column, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `parcels.drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='Missing required shape columns'): filter_parcels_by_shape(missing_column, shape_config)`.

**Regression protected**

- Protects the exact `missing required column fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `parcels.drop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_parcel_id_fails`

**Signature**

```python
def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `null parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[0, 'parcel_id']` from `None`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='must not be null')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='must not be null'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `null parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `parcels.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_id_fails`

**Signature**

```python
def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `duplicate parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[1, 'parcel_id']` from `invalid.loc[0, 'parcel_id']`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='must be unique')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='must be unique'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `duplicate parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `parcels.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_crs_fails`

**Signature**

```python
def test_unknown_crs_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `unknown crs fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `invalid` from `parcels.set_crs(None, allow_override=True)`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='known CRS')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `parcels.set_crs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='known CRS'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `unknown crs fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `parcels.set_crs`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unexpected_or_null_shape_status_fails`

**Signature**

```python
def test_unexpected_or_null_shape_status_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    status: str | None,
) -> None:
```

**Purpose**

Protects the `unexpected or null shape status fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`, `status`.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[0, 'shape_status']` from `status`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='Unexpected shape_status')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='Unexpected shape_status'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `unexpected or null shape status fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_non_finite_known_metric_on_valid_row_fails`

**Signature**

```python
def test_non_finite_known_metric_on_valid_row_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
```

**Purpose**

Protects the `non finite known metric on valid row fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`, `column`.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[0, column]` from `float('inf')`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='numeric and finite')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `float`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='numeric and finite'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `non finite known metric on valid row fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `float`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_shape_requires_strict_positive_width`

**Signature**

```python
def test_valid_shape_requires_strict_positive_width(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: object,
) -> None:
```

**Purpose**

Protects the `valid shape requires strict positive width` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`, `width`.
- Contains 4 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid['width_m']` from `invalid['width_m'].astype(object)`.
- Computes `invalid.loc[0, 'width_m']` from `width`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='width_m must be (numeric and finite|greater than zero)')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `float`, `invalid['width_m'].astype`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='width_m must be (numeric and finite|greater than zero)'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `valid shape requires strict positive width` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `float`, `invalid['width_m'].astype`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_shape_requires_ratio_at_least_one`

**Signature**

```python
def test_valid_shape_requires_ratio_at_least_one(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    ratio: object,
) -> None:
```

**Purpose**

Protects the `valid shape requires ratio at least one` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`, `ratio`.
- Contains 4 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid['length_width_ratio']` from `invalid['length_width_ratio'].astype(object)`.
- Computes `invalid.loc[0, 'length_width_ratio']` from `ratio`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='length_width_ratio must be (numeric and finite|at least one)')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `float`, `invalid['length_width_ratio'].astype`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='length_width_ratio must be (numeric and finite|at least one)'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `valid shape requires ratio at least one` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `float`, `invalid['length_width_ratio'].astype`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_negative_ratio_cannot_pass_permissive_thresholds`

**Signature**

```python
def test_negative_ratio_cannot_pass_permissive_thresholds(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
) -> None:
```

**Purpose**

Protects the `negative ratio cannot pass permissive thresholds` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 4 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[0, 'width_m']` from `20`.
- Computes `invalid.loc[0, 'length_width_ratio']` from `-1`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='length_width_ratio must be at least one')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='length_width_ratio must be at least one'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `negative ratio cannot pass permissive thresholds` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `parcels.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_disabled_policy_is_an_exact_passthrough`

**Signature**

```python
def test_disabled_policy_is_an_exact_passthrough(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `disabled policy is an exact passthrough` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 2 explicit setup/context statement(s).
- Computes `disabled` from `ShapeScreeningConfig(enabled=False)`.
- Computes `(retained, rejected)` from `filter_parcels_by_shape(parcels, disabled)`.

**Action**

- Calls `ShapeScreeningConfig`, `filter_parcels_by_shape`.

**Expected result**

- Direct assertions: `assert column not in retained.columns`; `assert column not in rejected.columns`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `disabled policy is an exact passthrough` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `ShapeScreeningConfig`, `assert_geodataframe_equal`, `filter_parcels_by_shape`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_different_configs_change_results_for_same_parcels`

**Signature**

```python
def test_different_configs_change_results_for_same_parcels(
    parcels: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Protects the `different configs change results for same parcels` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 4 explicit setup/context statement(s).
- Computes `permissive` from `_shape_config(min_width_m=10, max_length_width_ratio=12, policy_version='permissive')`.
- Computes `restrictive` from `_shape_config(min_width_m=18, max_length_width_ratio=6, policy_version='restrictive')`.
- Computes `(permissive_retained, _)` from `filter_parcels_by_shape(parcels, permissive)`.
- Computes `(restrictive_retained, _)` from `filter_parcels_by_shape(parcels, restrictive)`.

**Action**

- Calls `_shape_config`, `filter_parcels_by_shape`.

**Expected result**

- Direct assertions: `assert set(permissive_retained['parcel_id']) == {'at-boundaries', 'passing', 'width-below', 'ratio-above', 'both-thresholds-fail'}`; `assert set(restrictive_retained['parcel_id']) == {'passing'}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `different configs change results for same parcels` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_shape_config`, `filter_parcels_by_shape`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_shape_requires_complete_metrics_even_when_screening_disabled`

**Signature**

```python
def test_valid_shape_requires_complete_metrics_even_when_screening_disabled(
    parcels: gpd.GeoDataFrame,
    column: str,
) -> None:
```

**Purpose**

Protects the `valid shape requires complete metrics even when screening disabled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `column`.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[0, column]` from `None`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='complete|must not be null')` and executes: Calls `filter_parcels_by_shape(invalid, ShapeScreeningConfig(enabled=False))` for its validation or side effect.

**Action**

- Calls `ShapeScreeningConfig`, `filter_parcels_by_shape`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='complete|must not be null'): filter_parcels_by_shape(invalid, ShapeScreeningConfig(enabled=False))`.

**Regression protected**

- Protects the exact `valid shape requires complete metrics even when screening disabled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `ShapeScreeningConfig`, `filter_parcels_by_shape`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_shape_rejects_every_incomplete_metric_form`

**Signature**

```python
def test_valid_shape_rejects_every_incomplete_metric_form(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: float | None,
    ratio: float | None,
) -> None:
```

**Purpose**

Protects the `valid shape rejects every incomplete metric form` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`, `width`, `ratio`.
- Contains 4 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.loc[0, 'width_m']` from `width`.
- Computes `invalid.loc[0, 'length_width_ratio']` from `ratio`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='complete')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `float`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='complete'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `valid shape rejects every incomplete metric form` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `float`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_filter_rejects_plain_dataframe`

**Signature**

```python
def test_shape_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `shape filter rejects plain dataframe` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='GeoDataFrame')` and executes: Calls `filter_parcels_by_shape(pd.DataFrame(parcels), shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='GeoDataFrame'): filter_parcels_by_shape(pd.DataFrame(parcels), shape_config)`.

**Regression protected**

- Protects the exact `shape filter rejects plain dataframe` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `pd.DataFrame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_filter_rejects_duplicate_columns`

**Signature**

```python
def test_shape_filter_rejects_duplicate_columns(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `shape filter rejects duplicate columns` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `duplicate` from `gpd.GeoDataFrame(pd.concat([parcels, parcels[['parcel_id']]], axis=1), geometry='geometry', crs=parcels.crs)`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='columns.*unique')` and executes: Calls `filter_parcels_by_shape(duplicate, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `gpd.GeoDataFrame`, `pd.concat`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='columns.*unique'): filter_parcels_by_shape(duplicate, shape_config)`.

**Regression protected**

- Protects the exact `shape filter rejects duplicate columns` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `gpd.GeoDataFrame`, `pd.concat`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_filter_rejects_unreadable_crs`

**Signature**

```python
def test_shape_filter_rejects_unreadable_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

**Purpose**

Protects the `shape filter rejects unreadable crs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `shape_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid.geometry.array._crs` from `'not-a-crs'`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='CRS')` and executes: Calls `filter_parcels_by_shape(invalid, shape_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_shape`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='CRS'): filter_parcels_by_shape(invalid, shape_config)`.

**Regression protected**

- Protects the exact `shape filter rejects unreadable crs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_shape`, `parcels.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `compactness` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `length_width_ratio` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `shape-error` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `shape_policy_max_ratio` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `shape_policy_min_width_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `shape_policy_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `shape_rejection_reason` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
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
