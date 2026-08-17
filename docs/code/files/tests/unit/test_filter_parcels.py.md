# `tests/unit/test_filter_parcels.py`

## File identity

- Repository path: `tests/unit/test_filter_parcels.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `filter_parcels` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `d2b7a4bd8e16d349973ac8c21c1609dada89ae0604c6723f72b997660c2eaf1a`

## 1. Purpose

Provides complete unit and regression coverage for the `filter_parcels` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- None.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.config import ParcelConfig` — required by the implementation paths and symbols documented below.
- `from landscout.stages.filter_parcels import ParcelFilterError, filter_parcels_by_area` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `area_config`

**Signature**

```python
def area_config() -> ParcelConfig:
```

**Purpose**

Implements area config according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `ParcelConfig`. Observed return expression(s): `ParcelConfig(min_area_m2=2000, max_area_m2=15000)`.

**Algorithm**

1. Returns `ParcelConfig(min_area_m2=2000, max_area_m2=15000)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ParcelConfig`.

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

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'parcel_id': ['at-minimum', 'at-maximum', 'below-minimum', 'above-maximum', 'invalid-geometry', 'unknown-area'], 'geometry_status': ['VALID', 'VALID', 'VALID', 'VALID', 'INVALID', 'INVALID'], 'area_m2': [2000.0, 15000.0, 1999.0, 15001.0, 5000.0, None], 'commune_code': ['31395'] * 6}, geometry=[geometry] * 6, crs='EPSG:4326')`.

**Algorithm**

1. Computes `geometry` from `Polygon([(2.0, 43.0), (2.1, 43.0), (2.1, 43.1), (2.0, 43.0)])`.
2. Returns `gpd.GeoDataFrame({'parcel_id': ['at-minimum', 'at-maximum', 'below-minimum', 'above-maximum', 'invalid-geometry', 'unknown-area'], 'geometry_status': ['VALID', 'VALID', 'VALID', 'VALID', 'INVALID', 'INVALID'], 'area_m2': [2000.0, 15000.0, 1999.0, 15001.0, 5000.0, None], 'commune_code': ['31395'] * 6}, geometry=[geometry] * 6, crs='EPSG:4326')`.

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

### `test_minimum_boundary_is_included`

**Signature**

```python
def test_minimum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `minimum boundary is included` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 1 explicit setup/context statement(s).
- Computes `(candidates, _)` from `filter_parcels_by_area(parcels, area_config)`.

**Action**

- Calls `filter_parcels_by_area`.

**Expected result**

- Direct assertions: `assert 'at-minimum' in set(candidates['parcel_id'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `minimum boundary is included` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_maximum_boundary_is_included`

**Signature**

```python
def test_maximum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `maximum boundary is included` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 1 explicit setup/context statement(s).
- Computes `(candidates, _)` from `filter_parcels_by_area(parcels, area_config)`.

**Action**

- Calls `filter_parcels_by_area`.

**Expected result**

- Direct assertions: `assert 'at-maximum' in set(candidates['parcel_id'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `maximum boundary is included` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rejected_parcel_has_expected_reason`

**Signature**

```python
def test_rejected_parcel_has_expected_reason(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
```

**Purpose**

Protects the `rejected parcel has expected reason` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`, `parcel_id`, `expected_reason`.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, rejected)` from `filter_parcels_by_area(parcels, area_config)`.
- Computes `row` from `rejected.loc[rejected['parcel_id'] == parcel_id].iloc[0]`.

**Action**

- Calls `filter_parcels_by_area`.

**Expected result**

- Direct assertions: `assert row['rejection_reason'] == expected_reason`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `rejected parcel has expected reason` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_parcel_disappears`

**Signature**

```python
def test_no_parcel_disappears(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `no parcel disappears` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 1 explicit setup/context statement(s).
- Computes `(candidates, rejected)` from `filter_parcels_by_area(parcels, area_config)`.

**Action**

- Calls `filter_parcels_by_area`.

**Expected result**

- Direct assertions: `assert len(parcels) == len(candidates) + len(rejected)`; `assert set(parcels['parcel_id']) == set(candidates['parcel_id']) | set(rejected['parcel_id'])`; `assert candidates.crs == parcels.crs`; `assert rejected.crs == parcels.crs`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `no parcel disappears` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `len`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_thresholds_come_from_config`

**Signature**

```python
def test_thresholds_come_from_config(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Protects the `thresholds come from config` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`.
- Contains 2 explicit setup/context statement(s).
- Computes `custom_config` from `ParcelConfig(min_area_m2=1999, max_area_m2=2000)`.
- Computes `(candidates, _)` from `filter_parcels_by_area(parcels, custom_config)`.

**Action**

- Calls `ParcelConfig`, `filter_parcels_by_area`.

**Expected result**

- Direct assertions: `assert set(candidates['parcel_id']) == {'below-minimum', 'at-minimum'}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `thresholds come from config` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `ParcelConfig`, `filter_parcels_by_area`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_parcel_id_fails`

**Signature**

```python
def test_missing_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `missing parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `without_id` from `parcels.drop(columns=['parcel_id'])`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='parcel_id')` and executes: Calls `filter_parcels_by_area(without_id, area_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_area`, `parcels.drop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='parcel_id'): filter_parcels_by_area(without_id, area_config)`.

**Regression protected**

- Protects the exact `missing parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `parcels.drop`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_parcel_id_fails`

**Signature**

```python
def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `null parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `with_null` from `parcels.copy()`.
- Computes `with_null.loc[0, 'parcel_id']` from `None`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='null')` and executes: Calls `filter_parcels_by_area(with_null, area_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_area`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='null'): filter_parcels_by_area(with_null, area_config)`.

**Regression protected**

- Protects the exact `null parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `parcels.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_id_fails`

**Signature**

```python
def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `duplicate parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 3 explicit setup/context statement(s).
- Computes `with_duplicate` from `parcels.copy()`.
- Computes `with_duplicate.loc[1, 'parcel_id']` from `with_duplicate.loc[0, 'parcel_id']`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='unique')` and executes: Calls `filter_parcels_by_area(with_duplicate, area_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_area`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='unique'): filter_parcels_by_area(with_duplicate, area_config)`.

**Regression protected**

- Protects the exact `duplicate parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `parcels.copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_candidate_and_rejected_ids_do_not_overlap`

**Signature**

```python
def test_candidate_and_rejected_ids_do_not_overlap(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `candidate and rejected ids do not overlap` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 1 explicit setup/context statement(s).
- Computes `(candidates, rejected)` from `filter_parcels_by_area(parcels, area_config)`.

**Action**

- Calls `filter_parcels_by_area`.

**Expected result**

- Direct assertions: `assert set(candidates['parcel_id']).isdisjoint(set(rejected['parcel_id']))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `candidate and rejected ids do not overlap` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `set`, `set(candidates['parcel_id']).isdisjoint`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_parcel_ids_are_preserved`

**Signature**

```python
def test_exact_parcel_ids_are_preserved(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `exact parcel ids are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `(candidates, rejected)` from `filter_parcels_by_area(parcels, area_config)`.
- Computes `output_ids` from `list(candidates['parcel_id']) + list(rejected['parcel_id'])`.

**Action**

- Calls `filter_parcels_by_area`.

**Expected result**

- Direct assertions: `assert len(output_ids) == len(set(output_ids))`; `assert set(output_ids) == set(parcels['parcel_id'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact parcel ids are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `len`, `list`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_geometry_requires_strict_positive_finite_area`

**Signature**

```python
def test_valid_geometry_requires_strict_positive_finite_area(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    area: object,
) -> None:
```

**Purpose**

Protects the `valid geometry requires strict positive finite area` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`, `area`.
- Contains 4 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid['area_m2']` from `invalid['area_m2'].astype(object)`.
- Computes `invalid.loc[0, 'area_m2']` from `area`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='strict positive finite numeric')` and executes: Calls `filter_parcels_by_area(invalid, area_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_area`, `float`, `invalid['area_m2'].astype`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='strict positive finite numeric'): filter_parcels_by_area(invalid, area_config)`.

**Regression protected**

- Protects the exact `valid geometry requires strict positive finite area` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `float`, `invalid['area_m2'].astype`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_area_filter_requires_exact_non_empty_parcel_ids`

**Signature**

```python
def test_area_filter_requires_exact_non_empty_parcel_ids(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: object,
) -> None:
```

**Purpose**

Protects the `area filter requires exact non empty parcel ids` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`, `parcel_id`.
- Contains 4 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid['parcel_id']` from `invalid['parcel_id'].astype(object)`.
- Computes `invalid.loc[0, 'parcel_id']` from `parcel_id`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='exact non-empty strings')` and executes: Calls `filter_parcels_by_area(invalid, area_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_area`, `invalid['parcel_id'].astype`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='exact non-empty strings'): filter_parcels_by_area(invalid, area_config)`.

**Regression protected**

- Protects the exact `area filter requires exact non empty parcel ids` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `invalid['parcel_id'].astype`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_area_filter_rejects_plain_dataframe`

**Signature**

```python
def test_area_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `area filter rejects plain dataframe` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `plain` from `pd.DataFrame(parcels)`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='GeoDataFrame')` and executes: Calls `filter_parcels_by_area(plain, area_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_area`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='GeoDataFrame'): filter_parcels_by_area(plain, area_config)`.

**Regression protected**

- Protects the exact `area filter rejects plain dataframe` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `pd.DataFrame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_area_filter_rejects_duplicate_columns`

**Signature**

```python
def test_area_filter_rejects_duplicate_columns(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

**Purpose**

Protects the `area filter rejects duplicate columns` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`.
- Contains 2 explicit setup/context statement(s).
- Computes `duplicate` from `gpd.GeoDataFrame(pd.concat([parcels, parcels[['parcel_id']]], axis=1), geometry='geometry', crs=parcels.crs)`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='columns.*unique')` and executes: Calls `filter_parcels_by_area(duplicate, area_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_area`, `gpd.GeoDataFrame`, `pd.concat`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='columns.*unique'): filter_parcels_by_area(duplicate, area_config)`.

**Regression protected**

- Protects the exact `area filter rejects duplicate columns` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `gpd.GeoDataFrame`, `pd.concat`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_area_filter_rejects_malformed_spatial_envelope`

**Signature**

```python
def test_area_filter_rejects_malformed_spatial_envelope(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    mode: str,
) -> None:
```

**Purpose**

Protects the `area filter rejects malformed spatial envelope` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`, `mode`.
- Contains 2 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='geometry|CRS')` and executes: Calls `filter_parcels_by_area(invalid, area_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_area`, `invalid.drop`, `invalid.set_crs`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='geometry|CRS'): filter_parcels_by_area(invalid, area_config)`.

**Regression protected**

- Protects the exact `area filter rejects malformed spatial envelope` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `invalid.drop`, `invalid.set_crs`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_area_filter_rejects_noncanonical_geometry_status`

**Signature**

```python
def test_area_filter_rejects_noncanonical_geometry_status(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    geometry_status: object,
) -> None:
```

**Purpose**

Protects the `area filter rejects noncanonical geometry status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcels`, `area_config`, `geometry_status`.
- Contains 4 explicit setup/context statement(s).
- Computes `invalid` from `parcels.copy()`.
- Computes `invalid['geometry_status']` from `invalid['geometry_status'].astype(object)`.
- Computes `invalid.loc[0, 'geometry_status']` from `geometry_status`.
- Enters managed context(s) `pytest.raises(ParcelFilterError, match='geometry_status')` and executes: Calls `filter_parcels_by_area(invalid, area_config)` for its validation or side effect.

**Action**

- Calls `filter_parcels_by_area`, `invalid['geometry_status'].astype`, `parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ParcelFilterError, match='geometry_status'): filter_parcels_by_area(invalid, area_config)`.

**Regression protected**

- Protects the exact `area filter rejects noncanonical geometry status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `filter_parcels_by_area`, `invalid['geometry_status'].astype`, `parcels.copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `commune_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `rejection_reason` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
