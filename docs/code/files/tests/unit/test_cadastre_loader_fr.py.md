# `tests/unit/test_cadastre_loader_fr.py`

## File identity

- Repository path: `tests/unit/test_cadastre_loader_fr.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `cadastre_loader_fr` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `e724a7ac10433602f93022270b72ad077cec1f8fc679b99eed6e954446f25959`

## 1. Purpose

Provides complete unit and regression coverage for the `cadastre_loader_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `import gzip` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `from unittest.mock import patch` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.cadastre_fr import CadastreDownload` — required by the implementation paths and symbols documented below.
- `from landscout.sources.cadastre_loader_fr import ( CadastreLoadError, EmptyCadastreDatasetError, MissingGeometryColumnError, UnsupportedGeometryTypeError, load_cadastre_parcels, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_write_geojson`

**Signature**

```python
def _write_geojson(path: Path, features: list[dict]) -> None:
```

**Purpose**

Writes geojson according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `features` (`list[dict]`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `content` from `{'type': 'FeatureCollection', 'features': features}`.
2. Calls `path.write_text(json.dumps(content), encoding='utf-8')` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `json.dumps`, `path.write_text`.

**Known repository callers**

- `tests/unit/test_cadastre_loader_fr.py` — `test_load_valid_gzipped_geojson`

**Tests**

- `tests/unit/test_cadastre_loader_fr.py::test_load_valid_gzipped_geojson`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_gzipped_geojson`

**Signature**

```python
def _write_gzipped_geojson(path: Path, features: list[dict]) -> None:
```

**Purpose**

Writes gzipped geojson according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `features` (`list[dict]`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `content` from `json.dumps({'type': 'FeatureCollection', 'features': features}).encode()`.
2. Calls `path.write_bytes(gzip.compress(content))` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.write_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `gzip.compress`, `json.dumps`, `json.dumps({'type': 'FeatureCollection', 'features': features}).encode`, `path.write_bytes`.

**Known repository callers**

- `tests/unit/test_cadastre_loader_fr.py` — `test_empty_dataset_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_load_valid_geojson_preserves_attributes`
- `tests/unit/test_cadastre_loader_fr.py` — `test_malformed_verified_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py` — `test_physical_change_during_read_is_rejected_by_post_read_verification`
- `tests/unit/test_cadastre_loader_fr.py` — `test_physical_mutation_after_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py` — `test_unsupported_geometry_type_fails`

**Tests**

- `tests/unit/test_cadastre_loader_fr.py::test_empty_dataset_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_load_valid_geojson_preserves_attributes`
- `tests/unit/test_cadastre_loader_fr.py::test_malformed_verified_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification`
- `tests/unit/test_cadastre_loader_fr.py::test_physical_mutation_after_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py::test_unsupported_geometry_type_fails`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download`

**Signature**

```python
def _download(path: Path, **changes: object) -> CadastreDownload:
```

**Purpose**

Downloads and validates download according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**changes` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CadastreDownload`. Observed return expression(s): `CadastreDownload(**values)`.

**Algorithm**

1. Computes `content` from `path.read_bytes() if path.is_file() else b'missing'`.
2. Defines `values` with annotation `dict[str, object]` from `{'source_url': 'https://cadastre.data.gouv.fr/test/parcels.json.gz', 'download_timestamp': '2026-08-16T10:00:00+00:00', 'filename': path.name, 'file_size': len(content), 'sha256': sha256(content).hexdigest(), 'path': path, 'cache_hit': True}`.
3. Calls `values.update(changes)` for its validation or side effect.
4. Returns `CadastreDownload(**values)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `CadastreDownload`, `path.read_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CadastreDownload`, `len`, `path.is_file`, `path.read_bytes`, `sha256`, `sha256(content).hexdigest`, `values.update`.

**Known repository callers**

- `tests/unit/test_cadastre_loader_fr.py` — `test_empty_dataset_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_invalid_file_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_load_valid_geojson_preserves_attributes`
- `tests/unit/test_cadastre_loader_fr.py` — `test_load_valid_gzipped_geojson`
- `tests/unit/test_cadastre_loader_fr.py` — `test_malformed_verified_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py` — `test_missing_file_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_missing_geometry_column_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_physical_change_during_read_is_rejected_by_post_read_verification`
- `tests/unit/test_cadastre_loader_fr.py` — `test_physical_mutation_after_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py` — `test_unsupported_geometry_type_fails`

**Tests**

- `tests/unit/test_cadastre_loader_fr.py::test_empty_dataset_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_invalid_file_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_load_valid_geojson_preserves_attributes`
- `tests/unit/test_cadastre_loader_fr.py::test_load_valid_gzipped_geojson`
- `tests/unit/test_cadastre_loader_fr.py::test_malformed_verified_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py::test_missing_file_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_missing_geometry_column_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification`
- `tests/unit/test_cadastre_loader_fr.py::test_physical_mutation_after_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py::test_unsupported_geometry_type_fails`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_physical_change_during_read_is_rejected_by_post_read_verification.mutate_after_read`

**Signature**

```python
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
```

**Purpose**

Implements mutate after read according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `frame` from `original_read(*args, **kwargs)`.
2. Calls `path.write_bytes(gzip.compress(b'{"type":"FeatureCollection","features":[]}'))` for its validation or side effect.
3. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.write_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `gzip.compress`, `original_read`, `path.write_bytes`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_load_valid_geojson_preserves_attributes`

**Signature**

```python
def test_load_valid_geojson_preserves_attributes(tmp_path: Path) -> None:
```

**Purpose**

Protects the `load valid geojson preserves attributes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'parcels.json.gz'`.
- Computes `parcels` from `load_cadastre_parcels(_download(path))`.

**Action**

- Calls `_download`, `_write_gzipped_geojson`, `load_cadastre_parcels`.

**Expected result**

- Direct assertions: `assert len(parcels) == 2`; `assert list(parcels.columns) == ['id', 'section', 'numero', 'geometry']`; `assert set(parcels.geometry.geom_type) == {'Polygon', 'MultiPolygon'}`; `assert parcels.crs is not None`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `load valid geojson preserves attributes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_write_gzipped_geojson`, `len`, `list`, `load_cadastre_parcels`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_load_valid_gzipped_geojson`

**Signature**

```python
def test_load_valid_gzipped_geojson(tmp_path: Path) -> None:
```

**Purpose**

Protects the `load valid gzipped geojson` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `plain_path` from `tmp_path / 'parcels.geojson'`.
- Computes `gzip_path` from `tmp_path / 'parcels.json.gz'`.
- Computes `parcels` from `load_cadastre_parcels(_download(gzip_path))`.

**Action**

- Calls `_download`, `_write_geojson`, `gzip.compress`, `gzip_path.write_bytes`, `load_cadastre_parcels`, `plain_path.read_bytes`.

**Expected result**

- Direct assertions: `assert len(parcels) == 1`; `assert parcels.iloc[0]['id'] == 'parcel-1'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `load valid gzipped geojson` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_write_geojson`, `gzip.compress`, `gzip_path.write_bytes`, `len`, `load_cadastre_parcels`, `plain_path.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_empty_dataset_fails`

**Signature**

```python
def test_empty_dataset_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `empty dataset fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'empty.json.gz'`.
- Enters managed context(s) `pytest.raises(EmptyCadastreDatasetError)` and executes: Calls `load_cadastre_parcels(_download(path))` for its validation or side effect.

**Action**

- Calls `_download`, `_write_gzipped_geojson`, `load_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(EmptyCadastreDatasetError): load_cadastre_parcels(_download(path))`.

**Regression protected**

- Protects the exact `empty dataset fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_write_gzipped_geojson`, `load_cadastre_parcels`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_file_fails`

**Signature**

```python
def test_missing_file_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `missing file fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(CadastreLoadError, match='exist')` and executes: Calls `load_cadastre_parcels(_download(tmp_path / 'missing.json.gz'))` for its validation or side effect.

**Action**

- Calls `_download`, `load_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreLoadError, match='exist'): load_cadastre_parcels(_download(tmp_path / 'missing.json.gz'))`.

**Regression protected**

- Protects the exact `missing file fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `load_cadastre_parcels`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_file_fails`

**Signature**

```python
def test_invalid_file_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `invalid file fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'invalid.json.gz'`.
- Enters managed context(s) `pytest.raises(CadastreLoadError)` and executes: Calls `load_cadastre_parcels(_download(path))` for its validation or side effect.

**Action**

- Calls `_download`, `gzip.compress`, `load_cadastre_parcels`, `path.write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreLoadError): load_cadastre_parcels(_download(path))`.

**Regression protected**

- Protects the exact `invalid file fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `gzip.compress`, `load_cadastre_parcels`, `path.write_bytes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_geometry_column_fails`

**Signature**

```python
def test_missing_geometry_column_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `missing geometry column fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'parcels.json.gz'`.
- Computes `frame_without_geometry` from `gpd.GeoDataFrame({'id': ['parcel-1']})`.
- Enters managed context(s) `patch('landscout.sources.cadastre_loader_fr.gpd.read_file', return_value=frame_without_geometry), pytest.raises(MissingGeometryColumnError)` and executes: Calls `load_cadastre_parcels(_download(path))` for its validation or side effect.

**Action**

- Calls `_download`, `gpd.GeoDataFrame`, `gzip.compress`, `load_cadastre_parcels`, `path.write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.sources.cadastre_loader_fr.gpd.read_file', return_value=frame_without_geometry), pytest.raises(MissingGeometryColumnError): load_cadastre_parcels(_download(path))`.

**Regression protected**

- Protects the exact `missing geometry column fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `gpd.GeoDataFrame`, `gzip.compress`, `load_cadastre_parcels`, `patch`, `path.write_bytes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsupported_geometry_type_fails`

**Signature**

```python
def test_unsupported_geometry_type_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `unsupported geometry type fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'points.json.gz'`.
- Enters managed context(s) `pytest.raises(UnsupportedGeometryTypeError, match='Point')` and executes: Calls `load_cadastre_parcels(_download(path))` for its validation or side effect.

**Action**

- Calls `_download`, `_write_gzipped_geojson`, `load_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(UnsupportedGeometryTypeError, match='Point'): load_cadastre_parcels(_download(path))`.

**Regression protected**

- Protects the exact `unsupported geometry type fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_write_gzipped_geojson`, `load_cadastre_parcels`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_verified_download_is_rejected_before_parsing`

**Signature**

```python
def test_malformed_verified_download_is_rejected_before_parsing(
    tmp_path: Path,
    changes: dict[str, object],
    message: str,
) -> None:
```

**Purpose**

Protects the `malformed verified download is rejected before parsing` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `changes`, `message`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'parcels.json.gz'`.
- Enters managed context(s) `patch('landscout.sources.cadastre_loader_fr.gpd.read_file', side_effect=AssertionError('parser must not run')), pytest.raises(CadastreLoadError, match=message)` and executes: Calls `load_cadastre_parcels(_download(path, **changes))` for its validation or side effect.

**Action**

- Calls `AssertionError`, `_download`, `_write_gzipped_geojson`, `load_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.sources.cadastre_loader_fr.gpd.read_file', side_effect=AssertionError('parser must not run')), pytest.raises(CadastreLoadError, match=message): load_cadastre_parcels(_download(path, **changes))`.

**Regression protected**

- Protects the exact `malformed verified download is rejected before parsing` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_download`, `_write_gzipped_geojson`, `load_cadastre_parcels`, `patch`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_public_input_type_is_controlled`

**Signature**

```python
def test_wrong_public_input_type_is_controlled() -> None:
```

**Purpose**

Protects the `wrong public input type is controlled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(CadastreLoadError, match='CadastreDownload')` and executes: Calls `load_cadastre_parcels(Path('untrusted.json.gz'))` for its validation or side effect.

**Action**

- Calls `Path`, `load_cadastre_parcels`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(CadastreLoadError, match='CadastreDownload'): load_cadastre_parcels(Path('untrusted.json.gz'))`.

**Regression protected**

- Protects the exact `wrong public input type is controlled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `load_cadastre_parcels`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_physical_mutation_after_download_is_rejected_before_parsing`

**Signature**

```python
def test_physical_mutation_after_download_is_rejected_before_parsing(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `physical mutation after download is rejected before parsing` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'parcels.json.gz'`.
- Computes `download` from `_download(path)`.
- Computes `content` from `bytearray(path.read_bytes())`.
- Enters managed context(s) `patch('landscout.sources.cadastre_loader_fr.gpd.read_file', side_effect=AssertionError('parser must not run')), pytest.raises(CadastreLoadError, match='SHA|checksum|gzip')` and executes: Calls `load_cadastre_parcels(download)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `_download`, `_write_gzipped_geojson`, `bytearray`, `load_cadastre_parcels`, `path.read_bytes`, `path.write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.sources.cadastre_loader_fr.gpd.read_file', side_effect=AssertionError('parser must not run')), pytest.raises(CadastreLoadError, match='SHA|checksum|gzip'): load_cadastre_parcels(download)`.

**Regression protected**

- Protects the exact `physical mutation after download is rejected before parsing` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_download`, `_write_gzipped_geojson`, `bytearray`, `load_cadastre_parcels`, `patch`, `path.read_bytes`, `path.write_bytes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_physical_change_during_read_is_rejected_by_post_read_verification`

**Signature**

```python
def test_physical_change_during_read_is_rejected_by_post_read_verification(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `physical change during read is rejected by post read verification` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'parcels.json.gz'`.
- Computes `download` from `_download(path)`.
- Computes `original_read` from `gpd.read_file`.
- Enters managed context(s) `patch('landscout.sources.cadastre_loader_fr.gpd.read_file', side_effect=mutate_after_read), pytest.raises(CadastreLoadError, match='changed|SHA|size')` and executes: Calls `load_cadastre_parcels(download)` for its validation or side effect.

**Action**

- Calls `_download`, `_write_gzipped_geojson`, `gzip.compress`, `load_cadastre_parcels`, `original_read`, `path.write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.sources.cadastre_loader_fr.gpd.read_file', side_effect=mutate_after_read), pytest.raises(CadastreLoadError, match='changed|SHA|size'): load_cadastre_parcels(download)`.

**Regression protected**

- Protects the exact `physical change during read is rejected by post read verification` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_write_gzipped_geojson`, `gzip.compress`, `load_cadastre_parcels`, `original_read`, `patch`, `path.write_bytes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `id` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
