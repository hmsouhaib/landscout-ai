# `tests/unit/test_normalize_cadastre.py`

## File identity

- Repository path: `tests/unit/test_normalize_cadastre.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `2ee56ea4fa80743a6834d5fc1449e92e5509b2e39071cc2035a80b11e50b3f86`

## 1. Purpose

Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from copy import deepcopy` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.stages.normalize_cadastre import ( CadastreNormalizationError, normalize_cadastre_parcels, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_source_parcels`

**Signature**

```python
def _source_parcels(
    geometries: list[object],
    ids: list[object] | None = None,
    crs: str | None = "EPSG:4326",
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements source parcels according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `ids` (`list[object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `crs` (`str | None`; optional/default `'EPSG:4326'`) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'id': parcel_ids, 'commune': ['31395'] * count, 'prefixe': ['000'] * count, 'section': ['A'] * count, 'numero': [str(index + 1) for index in range(count)], 'contenance': [1000.0] * count, 'arpente': [False] * count, 'created': ['2020-01-01'] * count, 'updated': ['2024-01-01'] * count}, geometry=geometries, crs=crs)`.

**Algorithm**

1. Computes `parcel_ids` from `ids or [f'parcel-{index}' for index in range(len(geometries))]`.
2. Computes `count` from `len(geometries)`.
3. Returns `gpd.GeoDataFrame({'id': parcel_ids, 'commune': ['31395'] * count, 'prefixe': ['000'] * count, 'section': ['A'] * count, 'numero': [str(index + 1) for index in range(count)], 'contenance': [1000.0] * count, 'arpente': [False] * count, 'created': ['2020-01-01'] * count, 'updated': ['2024-01-01'] * count}, geometry=geometries, crs=crs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `gpd.GeoDataFrame`, `len`, `range`, `str`.

**Known repository callers**

- `tests/unit/test_normalize_cadastre.py` — `test_commune_accepts_canonical_french_insee_identity`
- `tests/unit/test_normalize_cadastre.py` — `test_commune_requires_canonical_french_insee_identity`
- `tests/unit/test_normalize_cadastre.py` — `test_duplicate_columns_are_rejected`
- `tests/unit/test_normalize_cadastre.py` — `test_duplicate_parcel_id_fails`
- `tests/unit/test_normalize_cadastre.py` — `test_every_cadastral_identity_field_requires_an_exact_nonempty_string`
- `tests/unit/test_normalize_cadastre.py` — `test_field_normalization`
- `tests/unit/test_normalize_cadastre.py` — `test_invalid_geometry_is_preserved_with_null_area`
- `tests/unit/test_normalize_cadastre.py` — `test_lambert93_area_calculation`
- `tests/unit/test_normalize_cadastre.py` — `test_missing_crs_fails`
- `tests/unit/test_normalize_cadastre.py` — `test_non_polygonal_geometry_is_rejected`
- `tests/unit/test_normalize_cadastre.py` — `test_normalization_does_not_mutate_input`
- `tests/unit/test_normalize_cadastre.py` — `test_null_and_empty_geometry_are_preserved_as_invalid`
- `tests/unit/test_normalize_cadastre.py` — `test_output_geometry_stays_in_wgs84`
- `tests/unit/test_normalize_cadastre.py` — `test_parcel_id_must_be_an_exact_nonempty_string`
- `tests/unit/test_normalize_cadastre.py` — `test_projected_source_crs_is_rejected`
- `tests/unit/test_normalize_cadastre.py` — `test_valid_multipolygon_is_accepted`

**Tests**

- `tests/unit/test_normalize_cadastre.py::test_commune_accepts_canonical_french_insee_identity`
- `tests/unit/test_normalize_cadastre.py::test_commune_requires_canonical_french_insee_identity`
- `tests/unit/test_normalize_cadastre.py::test_duplicate_columns_are_rejected`
- `tests/unit/test_normalize_cadastre.py::test_duplicate_parcel_id_fails`
- `tests/unit/test_normalize_cadastre.py::test_every_cadastral_identity_field_requires_an_exact_nonempty_string`
- `tests/unit/test_normalize_cadastre.py::test_field_normalization`
- `tests/unit/test_normalize_cadastre.py::test_invalid_geometry_is_preserved_with_null_area`
- `tests/unit/test_normalize_cadastre.py::test_lambert93_area_calculation`
- `tests/unit/test_normalize_cadastre.py::test_missing_crs_fails`
- `tests/unit/test_normalize_cadastre.py::test_non_polygonal_geometry_is_rejected`
- `tests/unit/test_normalize_cadastre.py::test_normalization_does_not_mutate_input`
- `tests/unit/test_normalize_cadastre.py::test_null_and_empty_geometry_are_preserved_as_invalid`
- `tests/unit/test_normalize_cadastre.py::test_output_geometry_stays_in_wgs84`
- `tests/unit/test_normalize_cadastre.py::test_parcel_id_must_be_an_exact_nonempty_string`
- `tests/unit/test_normalize_cadastre.py::test_projected_source_crs_is_rejected`
- `tests/unit/test_normalize_cadastre.py::test_valid_multipolygon_is_accepted`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `valid_polygon`

**Signature**

```python
def valid_polygon() -> Polygon:
```

**Purpose**

Implements valid polygon according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `Polygon`. Observed return expression(s): `Polygon([(2.35, 43.45), (2.36, 43.45), (2.36, 43.46), (2.35, 43.45)])`.

**Algorithm**

1. Returns `Polygon([(2.35, 43.45), (2.36, 43.45), (2.36, 43.46), (2.35, 43.45)])`.

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

### `test_field_normalization`

**Signature**

```python
def test_field_normalization(valid_polygon: Polygon) -> None:
```

**Purpose**

Protects the `field normalization` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`.
- Contains 1 explicit setup/context statement(s).
- Computes `normalized` from `normalize_cadastre_parcels(_source_parcels([valid_polygon]))`.

**Action**

- Calls `_source_parcels`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: `assert list(normalized.columns) == ['parcel_id', 'commune_code', 'section_prefix', 'section', 'parcel_number', 'source_contenance', 'source_arpente', 'source_created_at', 'source_updated_at', 'geometry_status', 'area_m2', 'geometry']`; `assert normalized.iloc[0]['parcel_id'] == 'parcel-0'`; `assert normalized.iloc[0]['commune_code'] == '31395'`; `assert normalized.iloc[0]['geometry_status'] == 'VALID'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `field normalization` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `list`, `normalize_cadastre_parcels`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_lambert93_area_calculation`

**Signature**

```python
def test_lambert93_area_calculation(valid_polygon: Polygon) -> None:
```

**Purpose**

Protects the `lambert93 area calculation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon])`.
- Computes `expected_area` from `source.to_crs('EPSG:2154').geometry.area.iloc[0]`.
- Computes `normalized` from `normalize_cadastre_parcels(source)`.

**Action**

- Calls `_source_parcels`, `normalize_cadastre_parcels`, `source.to_crs`.

**Expected result**

- Direct assertions: `assert normalized.iloc[0]['area_m2'] == pytest.approx(expected_area)`; `assert normalized.iloc[0]['area_m2'] > 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `lambert93 area calculation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `normalize_cadastre_parcels`, `pytest.approx`, `source.to_crs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_output_geometry_stays_in_wgs84`

**Signature**

```python
def test_output_geometry_stays_in_wgs84(valid_polygon: Polygon) -> None:
```

**Purpose**

Protects the `output geometry stays in wgs84` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon])`.
- Computes `normalized` from `normalize_cadastre_parcels(source)`.

**Action**

- Calls `_source_parcels`, `normalize_cadastre_parcels`, `normalized.crs.to_epsg`, `normalized.geometry.iloc[0].equals_exact`.

**Expected result**

- Direct assertions: `assert normalized.crs is not None`; `assert normalized.crs.to_epsg() == 4326`; `assert normalized.geometry.iloc[0].equals_exact(valid_polygon, tolerance=0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `output geometry stays in wgs84` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `normalize_cadastre_parcels`, `normalized.crs.to_epsg`, `normalized.geometry.iloc[0].equals_exact`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_geometry_is_preserved_with_null_area`

**Signature**

```python
def test_invalid_geometry_is_preserved_with_null_area() -> None:
```

**Purpose**

Protects the `invalid geometry is preserved with null area` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `bow_tie` from `Polygon([(2.35, 43.45), (2.36, 43.46), (2.35, 43.46), (2.36, 43.45)])`.
- Computes `normalized` from `normalize_cadastre_parcels(_source_parcels([bow_tie]))`.

**Action**

- Calls `Polygon`, `_source_parcels`, `normalize_cadastre_parcels`, `normalized.geometry.iloc[0].equals_exact`, `normalized['area_m2'].isna`.

**Expected result**

- Direct assertions: `assert not bow_tie.is_valid`; `assert normalized.iloc[0]['geometry_status'] == 'INVALID'`; `assert normalized['area_m2'].isna().iloc[0]`; `assert normalized.geometry.iloc[0].equals_exact(bow_tie, tolerance=0)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `invalid geometry is preserved with null area` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_source_parcels`, `normalize_cadastre_parcels`, `normalized.geometry.iloc[0].equals_exact`, `normalized['area_m2'].isna`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_crs_fails`

**Signature**

```python
def test_missing_crs_fails(valid_polygon: Polygon) -> None:
```

**Purpose**

Protects the `missing crs fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon], crs=None)`.
- Enters managed context(s) `pytest.raises(CadastreNormalizationError, match='CRS')` and executes: Calls `normalize_cadastre_parcels(source)` for its validation or side effect.

**Action**

- Calls `_source_parcels`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreNormalizationError, match='CRS'): normalize_cadastre_parcels(source)`.

**Regression protected**

- Protects the exact `missing crs fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `normalize_cadastre_parcels`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_id_fails`

**Signature**

```python
def test_duplicate_parcel_id_fails(valid_polygon: Polygon) -> None:
```

**Purpose**

Protects the `duplicate parcel id fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon, valid_polygon], ids=['duplicate', 'duplicate'])`.
- Enters managed context(s) `pytest.raises(CadastreNormalizationError, match='unique')` and executes: Calls `normalize_cadastre_parcels(source)` for its validation or side effect.

**Action**

- Calls `_source_parcels`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreNormalizationError, match='unique'): normalize_cadastre_parcels(source)`.

**Regression protected**

- Protects the exact `duplicate parcel id fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `normalize_cadastre_parcels`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_non_geodataframe_is_rejected_safely`

**Signature**

```python
def test_non_geodataframe_is_rejected_safely() -> None:
```

**Purpose**

Protects the `non geodataframe is rejected safely` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(CadastreNormalizationError, match='GeoDataFrame')` and executes: Calls `normalize_cadastre_parcels(pd.DataFrame({'id': ['parcel']}))` for its validation or side effect.

**Action**

- Calls `normalize_cadastre_parcels`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreNormalizationError, match='GeoDataFrame'): normalize_cadastre_parcels(pd.DataFrame({'id': ['parcel']}))`.

**Regression protected**

- Protects the exact `non geodataframe is rejected safely` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `normalize_cadastre_parcels`, `pd.DataFrame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_columns_are_rejected`

**Signature**

```python
def test_duplicate_columns_are_rejected(valid_polygon: Polygon) -> None:
```

**Purpose**

Protects the `duplicate columns are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon])`.
- Computes `duplicate` from `gpd.GeoDataFrame(pd.concat([source, source[['id']]], axis=1), geometry='geometry', crs=source.crs)`.
- Enters managed context(s) `pytest.raises(CadastreNormalizationError, match='columns.*unique')` and executes: Calls `normalize_cadastre_parcels(duplicate)` for its validation or side effect.

**Action**

- Calls `_source_parcels`, `gpd.GeoDataFrame`, `normalize_cadastre_parcels`, `pd.concat`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreNormalizationError, match='columns.*unique'): normalize_cadastre_parcels(duplicate)`.

**Regression protected**

- Protects the exact `duplicate columns are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `gpd.GeoDataFrame`, `normalize_cadastre_parcels`, `pd.concat`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_projected_source_crs_is_rejected`

**Signature**

```python
def test_projected_source_crs_is_rejected(valid_polygon: Polygon) -> None:
```

**Purpose**

Protects the `projected source crs is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon]).to_crs('EPSG:2154')`.
- Enters managed context(s) `pytest.raises(CadastreNormalizationError, match='4326')` and executes: Calls `normalize_cadastre_parcels(source)` for its validation or side effect.

**Action**

- Calls `_source_parcels`, `_source_parcels([valid_polygon]).to_crs`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreNormalizationError, match='4326'): normalize_cadastre_parcels(source)`.

**Regression protected**

- Protects the exact `projected source crs is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `_source_parcels([valid_polygon]).to_crs`, `normalize_cadastre_parcels`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_id_must_be_an_exact_nonempty_string`

**Signature**

```python
def test_parcel_id_must_be_an_exact_nonempty_string(
    valid_polygon: Polygon,
    identifier: object,
) -> None:
```

**Purpose**

Protects the `parcel id must be an exact nonempty string` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`, `identifier`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon], ids=[identifier])`.
- Enters managed context(s) `pytest.raises(CadastreNormalizationError, match='parcel_id')` and executes: Calls `normalize_cadastre_parcels(source)` for its validation or side effect.

**Action**

- Calls `_source_parcels`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreNormalizationError, match='parcel_id'): normalize_cadastre_parcels(source)`.

**Regression protected**

- Protects the exact `parcel id must be an exact nonempty string` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `normalize_cadastre_parcels`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_non_polygonal_geometry_is_rejected`

**Signature**

```python
def test_non_polygonal_geometry_is_rejected(geometry: object) -> None:
```

**Purpose**

Protects the `non polygonal geometry is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(CadastreNormalizationError, match='Polygon')` and executes: Calls `normalize_cadastre_parcels(_source_parcels([geometry]))` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `_source_parcels`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreNormalizationError, match='Polygon'): normalize_cadastre_parcels(_source_parcels([geometry]))`.

**Regression protected**

- Protects the exact `non polygonal geometry is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `_source_parcels`, `normalize_cadastre_parcels`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_multipolygon_is_accepted`

**Signature**

```python
def test_valid_multipolygon_is_accepted(valid_polygon: Polygon) -> None:
```

**Purpose**

Protects the `valid multipolygon is accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`.
- Contains 1 explicit setup/context statement(s).
- Computes `normalized` from `normalize_cadastre_parcels(_source_parcels([MultiPolygon([valid_polygon])]))`.

**Action**

- Calls `MultiPolygon`, `_source_parcels`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: `assert normalized.loc[0, 'geometry_status'] == 'VALID'`; `assert normalized.loc[0, 'area_m2'] > 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid multipolygon is accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `_source_parcels`, `normalize_cadastre_parcels`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_and_empty_geometry_are_preserved_as_invalid`

**Signature**

```python
def test_null_and_empty_geometry_are_preserved_as_invalid(geometry: object) -> None:
```

**Purpose**

Protects the `null and empty geometry are preserved as invalid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Computes `normalized` from `normalize_cadastre_parcels(_source_parcels([geometry]))`.

**Action**

- Calls `Polygon`, `_source_parcels`, `normalize_cadastre_parcels`, `normalized.geometry.isna`, `pd.isna`.

**Expected result**

- Direct assertions: `assert normalized.loc[0, 'geometry_status'] == 'INVALID'`; `assert pd.isna(normalized.loc[0, 'area_m2'])`; `assert normalized.geometry.isna().iloc[0]`; `assert normalized.geometry.is_empty.iloc[0]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `null and empty geometry are preserved as invalid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_source_parcels`, `normalize_cadastre_parcels`, `normalized.geometry.isna`, `pd.isna`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normalization_does_not_mutate_input`

**Signature**

```python
def test_normalization_does_not_mutate_input(valid_polygon: Polygon) -> None:
```

**Purpose**

Protects the `normalization does not mutate input` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`.
- Contains 2 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon])`.
- Computes `before` from `deepcopy(source)`.

**Action**

- Calls `_source_parcels`, `deepcopy`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `normalization does not mutate input` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `assert_geodataframe_equal`, `deepcopy`, `normalize_cadastre_parcels`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_cadastral_identity_field_requires_an_exact_nonempty_string`

**Signature**

```python
def test_every_cadastral_identity_field_requires_an_exact_nonempty_string(
    valid_polygon: Polygon,
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `every cadastral identity field requires an exact nonempty string` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`, `column`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon])`.
- Computes `source[column]` from `source[column].astype(object)`.
- Computes `source.loc[0, column]` from `value`.
- Enters managed context(s) `pytest.raises(CadastreNormalizationError, match=column)` and executes: Calls `normalize_cadastre_parcels(source)` for its validation or side effect.

**Action**

- Calls `_source_parcels`, `normalize_cadastre_parcels`, `source[column].astype`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreNormalizationError, match=column): normalize_cadastre_parcels(source)`.

**Regression protected**

- Protects the exact `every cadastral identity field requires an exact nonempty string` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `normalize_cadastre_parcels`, `pytest.mark.parametrize`, `pytest.raises`, `source[column].astype`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_commune_requires_canonical_french_insee_identity`

**Signature**

```python
def test_commune_requires_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
```

**Purpose**

Protects the `commune requires canonical french insee identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`, `commune`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon])`.
- Computes `source.loc[0, 'commune']` from `commune`.
- Enters managed context(s) `pytest.raises(CadastreNormalizationError, match='commune')` and executes: Calls `normalize_cadastre_parcels(source)` for its validation or side effect.

**Action**

- Calls `_source_parcels`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreNormalizationError, match='commune'): normalize_cadastre_parcels(source)`.

**Regression protected**

- Protects the exact `commune requires canonical french insee identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `normalize_cadastre_parcels`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_commune_accepts_canonical_french_insee_identity`

**Signature**

```python
def test_commune_accepts_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
```

**Purpose**

Protects the `commune accepts canonical french insee identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `valid_polygon`, `commune`.
- Contains 3 explicit setup/context statement(s).
- Computes `source` from `_source_parcels([valid_polygon])`.
- Computes `source.loc[0, 'commune']` from `commune`.
- Computes `result` from `normalize_cadastre_parcels(source)`.

**Action**

- Calls `_source_parcels`, `normalize_cadastre_parcels`.

**Expected result**

- Direct assertions: `assert result.loc[0, 'commune_code'] == commune`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `commune accepts canonical french insee identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source_parcels`, `normalize_cadastre_parcels`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `arpente` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `commune` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `commune_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `contenance` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `created` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `id` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `numero` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `prefixe` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `section` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `updated` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
