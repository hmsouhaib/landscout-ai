# `tests/unit/test_config.py`

## File identity

- Repository path: `tests/unit/test_config.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `config` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `5ab7e31a98262a2d35698c8e6c950b2998c438bd0050d9ecf2ac5cf80a952597`

## 1. Purpose

Provides complete unit and regression coverage for the `config` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `import pytest` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import ValidationError` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.config import load_scan_config` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `PROJECT_ROOT` | `Path(__file__).parents[2]` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SCAN_PATH` | `PROJECT_ROOT / "configs/scans/bess_muret.yaml"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PROFILE_PATH` | `PROJECT_ROOT / "configs/profiles/bess_default_fr.yaml"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_yaml_data`

**Signature**

```python
def _yaml_data(path: Path) -> dict:
```

**Purpose**

Implements yaml data according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict`. Observed return expression(s): `yaml.safe_load(stream)`.

**Algorithm**

1. Enters managed context(s) `path.open(encoding='utf-8')` and executes: Returns `yaml.safe_load(stream)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `path.open`, `yaml.safe_load`.

**Known repository callers**

- `tests/unit/test_config.py` — `_temporary_scan`
- `tests/unit/test_config.py` — `test_aoi_requires_nonempty_unique_commune_codes`
- `tests/unit/test_config.py` — `test_calibration_sample_size_is_strict_positive_integer`
- `tests/unit/test_config.py` — `test_canonical_france_commune_codes_are_accepted`
- `tests/unit/test_config.py` — `test_empty_calibration_metadata_fails`
- `tests/unit/test_config.py` — `test_enabled_shape_screening_requires_complete_calibration`
- `tests/unit/test_config.py` — `test_enabled_shape_screening_requires_policy_values`
- `tests/unit/test_config.py` — `test_invalid_calibration_percentage_fails`
- `tests/unit/test_config.py` — `test_invalid_calibration_sample_size_fails`
- `tests/unit/test_config.py` — `test_invalid_commune_code_fails`
- `tests/unit/test_config.py` — `test_invalid_shape_threshold_fails`
- `tests/unit/test_config.py` — `test_maximum_area_smaller_than_minimum_fails`
- `tests/unit/test_config.py` — `test_negative_minimum_area_fails`
- `tests/unit/test_config.py` — `test_noncanonical_france_commune_codes_are_rejected`
- `tests/unit/test_config.py` — `test_parcel_numeric_contract_is_strict_and_finite`
- `tests/unit/test_config.py` — `test_profile_crs_contract_is_exact`
- `tests/unit/test_config.py` — `test_scan_and_profile_identity_must_match`
- `tests/unit/test_config.py` — `test_shape_enabled_is_strict_boolean`
- `tests/unit/test_config.py` — `test_shape_screening_can_be_disabled_without_policy_values`
- `tests/unit/test_config.py` — `test_unknown_profile_fields_are_rejected`
- `tests/unit/test_config.py` — `test_unknown_scan_fields_are_rejected`

**Tests**

- `tests/unit/test_config.py::test_aoi_requires_nonempty_unique_commune_codes`
- `tests/unit/test_config.py::test_calibration_sample_size_is_strict_positive_integer`
- `tests/unit/test_config.py::test_canonical_france_commune_codes_are_accepted`
- `tests/unit/test_config.py::test_empty_calibration_metadata_fails`
- `tests/unit/test_config.py::test_enabled_shape_screening_requires_complete_calibration`
- `tests/unit/test_config.py::test_enabled_shape_screening_requires_policy_values`
- `tests/unit/test_config.py::test_invalid_calibration_percentage_fails`
- `tests/unit/test_config.py::test_invalid_calibration_sample_size_fails`
- `tests/unit/test_config.py::test_invalid_commune_code_fails`
- `tests/unit/test_config.py::test_invalid_shape_threshold_fails`
- `tests/unit/test_config.py::test_maximum_area_smaller_than_minimum_fails`
- `tests/unit/test_config.py::test_negative_minimum_area_fails`
- `tests/unit/test_config.py::test_noncanonical_france_commune_codes_are_rejected`
- `tests/unit/test_config.py::test_parcel_numeric_contract_is_strict_and_finite`
- `tests/unit/test_config.py::test_profile_crs_contract_is_exact`
- `tests/unit/test_config.py::test_scan_and_profile_identity_must_match`
- `tests/unit/test_config.py::test_shape_enabled_is_strict_boolean`
- `tests/unit/test_config.py::test_shape_screening_can_be_disabled_without_policy_values`
- `tests/unit/test_config.py::test_unknown_profile_fields_are_rejected`
- `tests/unit/test_config.py::test_unknown_scan_fields_are_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_yaml`

**Signature**

```python
def _write_yaml(path: Path, data: dict) -> None:
```

**Purpose**

Writes yaml according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `data` (`dict`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `path.write_text(yaml.safe_dump(data), encoding='utf-8')` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `path.write_text`, `yaml.safe_dump`.

**Known repository callers**

- `tests/unit/test_config.py` — `_load_temporary_profile`
- `tests/unit/test_config.py` — `_temporary_scan`
- `tests/unit/test_config.py` — `test_aoi_requires_nonempty_unique_commune_codes`
- `tests/unit/test_config.py` — `test_canonical_france_commune_codes_are_accepted`
- `tests/unit/test_config.py` — `test_invalid_commune_code_fails`
- `tests/unit/test_config.py` — `test_maximum_area_smaller_than_minimum_fails`
- `tests/unit/test_config.py` — `test_negative_minimum_area_fails`
- `tests/unit/test_config.py` — `test_noncanonical_france_commune_codes_are_rejected`
- `tests/unit/test_config.py` — `test_unknown_scan_fields_are_rejected`

**Tests**

- `tests/unit/test_config.py::test_aoi_requires_nonempty_unique_commune_codes`
- `tests/unit/test_config.py::test_canonical_france_commune_codes_are_accepted`
- `tests/unit/test_config.py::test_invalid_commune_code_fails`
- `tests/unit/test_config.py::test_maximum_area_smaller_than_minimum_fails`
- `tests/unit/test_config.py::test_negative_minimum_area_fails`
- `tests/unit/test_config.py::test_noncanonical_france_commune_codes_are_rejected`
- `tests/unit/test_config.py::test_unknown_scan_fields_are_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_temporary_scan`

**Signature**

```python
def _temporary_scan(tmp_path: Path, profile_path: Path) -> Path:
```

**Purpose**

Implements temporary scan according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `profile_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `scan_path`.

**Algorithm**

1. Computes `scan_data` from `_yaml_data(SCAN_PATH)`.
2. Computes `scan_data['profile']['path']` from `str(profile_path)`.
3. Computes `scan_path` from `tmp_path / 'scan.yaml'`.
4. Calls `_write_yaml(scan_path, scan_data)` for its validation or side effect.
5. Returns `scan_path`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_write_yaml`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_write_yaml`, `_yaml_data`, `str`.

**Known repository callers**

- `tests/unit/test_config.py` — `_load_temporary_profile`
- `tests/unit/test_config.py` — `test_maximum_area_smaller_than_minimum_fails`
- `tests/unit/test_config.py` — `test_missing_profile_fails`
- `tests/unit/test_config.py` — `test_negative_minimum_area_fails`

**Tests**

- `tests/unit/test_config.py::test_maximum_area_smaller_than_minimum_fails`
- `tests/unit/test_config.py::test_missing_profile_fails`
- `tests/unit/test_config.py::test_negative_minimum_area_fails`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_load_temporary_profile`

**Signature**

```python
def _load_temporary_profile(tmp_path: Path, profile_data: dict):
```

**Purpose**

Loads temporary profile according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `profile_data` (`dict`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `unannotated`. Observed return expression(s): `load_scan_config(_temporary_scan(tmp_path, profile_path))`.

**Algorithm**

1. Computes `profile_path` from `tmp_path / 'profile.yaml'`.
2. Calls `_write_yaml(profile_path, profile_data)` for its validation or side effect.
3. Returns `load_scan_config(_temporary_scan(tmp_path, profile_path))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_write_yaml`, `load_scan_config`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_temporary_scan`, `_write_yaml`, `load_scan_config`.

**Known repository callers**

- `tests/unit/test_config.py` — `test_calibration_sample_size_is_strict_positive_integer`
- `tests/unit/test_config.py` — `test_empty_calibration_metadata_fails`
- `tests/unit/test_config.py` — `test_enabled_shape_screening_requires_complete_calibration`
- `tests/unit/test_config.py` — `test_enabled_shape_screening_requires_policy_values`
- `tests/unit/test_config.py` — `test_invalid_calibration_percentage_fails`
- `tests/unit/test_config.py` — `test_invalid_calibration_sample_size_fails`
- `tests/unit/test_config.py` — `test_invalid_shape_threshold_fails`
- `tests/unit/test_config.py` — `test_parcel_numeric_contract_is_strict_and_finite`
- `tests/unit/test_config.py` — `test_profile_crs_contract_is_exact`
- `tests/unit/test_config.py` — `test_scan_and_profile_identity_must_match`
- `tests/unit/test_config.py` — `test_shape_enabled_is_strict_boolean`
- `tests/unit/test_config.py` — `test_shape_screening_can_be_disabled_without_policy_values`
- `tests/unit/test_config.py` — `test_unknown_profile_fields_are_rejected`

**Tests**

- `tests/unit/test_config.py::test_calibration_sample_size_is_strict_positive_integer`
- `tests/unit/test_config.py::test_empty_calibration_metadata_fails`
- `tests/unit/test_config.py::test_enabled_shape_screening_requires_complete_calibration`
- `tests/unit/test_config.py::test_enabled_shape_screening_requires_policy_values`
- `tests/unit/test_config.py::test_invalid_calibration_percentage_fails`
- `tests/unit/test_config.py::test_invalid_calibration_sample_size_fails`
- `tests/unit/test_config.py::test_invalid_shape_threshold_fails`
- `tests/unit/test_config.py::test_parcel_numeric_contract_is_strict_and_finite`
- `tests/unit/test_config.py::test_profile_crs_contract_is_exact`
- `tests/unit/test_config.py::test_scan_and_profile_identity_must_match`
- `tests/unit/test_config.py::test_shape_enabled_is_strict_boolean`
- `tests/unit/test_config.py::test_shape_screening_can_be_disabled_without_policy_values`
- `tests/unit/test_config.py::test_unknown_profile_fields_are_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_config_loads`

**Signature**

```python
def test_valid_config_loads() -> None:
```

**Purpose**

Protects the `valid config loads` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `loaded` from `load_scan_config(SCAN_PATH)`.
- Computes `shape_screening` from `loaded.profile.shape_screening`.
- Computes `calibration` from `shape_screening.calibration`.

**Action**

- Calls `load_scan_config`.

**Expected result**

- Direct assertions: `assert loaded.scan_config.aoi.commune_codes == ['31395']`; `assert loaded.profile.technology == 'BESS'`; `assert loaded.profile_path == PROFILE_PATH`; `assert shape_screening.enabled is True`; `assert shape_screening.min_width_m == 15`; `assert shape_screening.max_length_width_ratio == 10`; `assert calibration is not None`; `assert calibration.policy_version == 'muret_empirical_v1'`; `assert calibration.method == 'empirical_distribution'`; `assert calibration.calibration_scope == 'Muret 31395'`; `assert calibration.sample_size == 4013`; `assert calibration.calibrated_at == '2026-08-11'`; `assert calibration.target_retention_pct == 90`; `assert calibration.observed_retention_pct == 90.65537`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid config loads` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_scan_config`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_commune_code_fails`

**Signature**

```python
def test_invalid_commune_code_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `invalid commune code fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `scan_data` from `_yaml_data(SCAN_PATH)`.
- Computes `scan_data['aoi']['commune_codes']` from `['3139']`.
- Computes `scan_path` from `tmp_path / 'scan.yaml'`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `load_scan_config(scan_path)` for its validation or side effect.

**Action**

- Calls `_write_yaml`, `_yaml_data`, `load_scan_config`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): load_scan_config(scan_path)`.

**Regression protected**

- Protects the exact `invalid commune code fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_yaml`, `_yaml_data`, `load_scan_config`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_negative_minimum_area_fails`

**Signature**

```python
def test_negative_minimum_area_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `negative minimum area fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['parcel']['min_area_m2']` from `-1`.
- Computes `profile_path` from `tmp_path / 'profile.yaml'`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `load_scan_config(_temporary_scan(tmp_path, profile_path))` for its validation or side effect.

**Action**

- Calls `_temporary_scan`, `_write_yaml`, `_yaml_data`, `load_scan_config`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): load_scan_config(_temporary_scan(tmp_path, profile_path))`.

**Regression protected**

- Protects the exact `negative minimum area fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_temporary_scan`, `_write_yaml`, `_yaml_data`, `load_scan_config`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_maximum_area_smaller_than_minimum_fails`

**Signature**

```python
def test_maximum_area_smaller_than_minimum_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `maximum area smaller than minimum fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['parcel']['max_area_m2']` from `1000`.
- Computes `profile_path` from `tmp_path / 'profile.yaml'`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `load_scan_config(_temporary_scan(tmp_path, profile_path))` for its validation or side effect.

**Action**

- Calls `_temporary_scan`, `_write_yaml`, `_yaml_data`, `load_scan_config`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): load_scan_config(_temporary_scan(tmp_path, profile_path))`.

**Regression protected**

- Protects the exact `maximum area smaller than minimum fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_temporary_scan`, `_write_yaml`, `_yaml_data`, `load_scan_config`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_profile_fails`

**Signature**

```python
def test_missing_profile_fails(tmp_path: Path) -> None:
```

**Purpose**

Protects the `missing profile fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `missing_profile` from `tmp_path / 'missing.yaml'`.
- Enters managed context(s) `pytest.raises(FileNotFoundError)` and executes: Calls `load_scan_config(_temporary_scan(tmp_path, missing_profile))` for its validation or side effect.

**Action**

- Calls `_temporary_scan`, `load_scan_config`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(FileNotFoundError): load_scan_config(_temporary_scan(tmp_path, missing_profile))`.

**Regression protected**

- Protects the exact `missing profile fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_temporary_scan`, `load_scan_config`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_shape_threshold_fails`

**Signature**

```python
def test_invalid_shape_threshold_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
```

**Purpose**

Protects the `invalid shape threshold fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`, `invalid_value`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['shape_screening'][field]` from `invalid_value`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `invalid shape threshold fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_calibration_percentage_fails`

**Signature**

```python
def test_invalid_calibration_percentage_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
```

**Purpose**

Protects the `invalid calibration percentage fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`, `invalid_value`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['shape_screening']['calibration'][field]` from `invalid_value`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `invalid calibration percentage fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_calibration_sample_size_fails`

**Signature**

```python
def test_invalid_calibration_sample_size_fails(
    tmp_path: Path, invalid_value: int
) -> None:
```

**Purpose**

Protects the `invalid calibration sample size fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `invalid_value`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['shape_screening']['calibration']['sample_size']` from `invalid_value`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `invalid calibration sample size fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_empty_calibration_metadata_fails`

**Signature**

```python
def test_empty_calibration_metadata_fails(tmp_path: Path, field: str) -> None:
```

**Purpose**

Protects the `empty calibration metadata fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['shape_screening']['calibration'][field]` from `' '`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `empty calibration metadata fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_enabled_shape_screening_requires_policy_values`

**Signature**

```python
def test_enabled_shape_screening_requires_policy_values(
    tmp_path: Path, field: str
) -> None:
```

**Purpose**

Protects the `enabled shape screening requires policy values` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`.
- Contains 2 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Enters managed context(s) `pytest.raises(ValidationError, match='enabled shape screening requires')` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError, match='enabled shape screening requires'): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `enabled shape screening requires policy values` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_enabled_shape_screening_requires_complete_calibration`

**Signature**

```python
def test_enabled_shape_screening_requires_complete_calibration(
    tmp_path: Path, field: str
) -> None:
```

**Purpose**

Protects the `enabled shape screening requires complete calibration` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`.
- Contains 2 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `enabled shape screening requires complete calibration` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_screening_can_be_disabled_without_policy_values`

**Signature**

```python
def test_shape_screening_can_be_disabled_without_policy_values(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `shape screening can be disabled without policy values` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['shape_screening']` from `{'enabled': False}`.
- Computes `loaded` from `_load_temporary_profile(tmp_path, profile_data)`.
- Computes `shape_screening` from `loaded.profile.shape_screening`.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: `assert shape_screening.enabled is False`; `assert shape_screening.min_width_m is None`; `assert shape_screening.max_length_width_ratio is None`; `assert shape_screening.calibration is None`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `shape screening can be disabled without policy values` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_scan_fields_are_rejected`

**Signature**

```python
def test_unknown_scan_fields_are_rejected(
    tmp_path: Path,
    section: str | None,
    field: str,
) -> None:
```

**Purpose**

Protects the `unknown scan fields are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `section`, `field`.
- Contains 6 explicit setup/context statement(s).
- Computes `scan_data` from `_yaml_data(SCAN_PATH)`.
- Computes `scan_data['profile']['path']` from `str(PROFILE_PATH)`.
- Computes `target` from `scan_data if section is None else scan_data[section]`.
- Computes `target[field]` from `'value'`.
- Computes `scan_path` from `tmp_path / 'scan.yaml'`.
- Enters managed context(s) `pytest.raises(ValidationError, match=field)` and executes: Calls `load_scan_config(scan_path)` for its validation or side effect.

**Action**

- Calls `_write_yaml`, `_yaml_data`, `load_scan_config`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError, match=field): load_scan_config(scan_path)`.

**Regression protected**

- Protects the exact `unknown scan fields are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_yaml`, `_yaml_data`, `load_scan_config`, `pytest.mark.parametrize`, `pytest.raises`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_profile_fields_are_rejected`

**Signature**

```python
def test_unknown_profile_fields_are_rejected(
    tmp_path: Path,
    section: str,
) -> None:
```

**Purpose**

Protects the `unknown profile fields are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `section`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data[section]['unexpected']` from `'value'`.
- Enters managed context(s) `pytest.raises(ValidationError, match='unexpected')` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError, match='unexpected'): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `unknown profile fields are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_numeric_contract_is_strict_and_finite`

**Signature**

```python
def test_parcel_numeric_contract_is_strict_and_finite(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `parcel numeric contract is strict and finite` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['parcel'][field]` from `value`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`, `float`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `parcel numeric contract is strict and finite` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `float`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_calibration_sample_size_is_strict_positive_integer`

**Signature**

```python
def test_calibration_sample_size_is_strict_positive_integer(
    tmp_path: Path,
    value: object,
) -> None:
```

**Purpose**

Protects the `calibration sample size is strict positive integer` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['shape_screening']['calibration']['sample_size']` from `value`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `calibration sample size is strict positive integer` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shape_enabled_is_strict_boolean`

**Signature**

```python
def test_shape_enabled_is_strict_boolean(tmp_path: Path, value: object) -> None:
```

**Purpose**

Protects the `shape enabled is strict boolean` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['shape_screening']['enabled']` from `value`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `shape enabled is strict boolean` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_canonical_france_commune_codes_are_accepted`

**Signature**

```python
def test_canonical_france_commune_codes_are_accepted(
    tmp_path: Path,
    code: str,
) -> None:
```

**Purpose**

Protects the `canonical france commune codes are accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `code`.
- Contains 4 explicit setup/context statement(s).
- Computes `scan_data` from `_yaml_data(SCAN_PATH)`.
- Computes `scan_data['profile']['path']` from `str(PROFILE_PATH)`.
- Computes `scan_data['aoi']['commune_codes']` from `[code]`.
- Computes `scan_path` from `tmp_path / 'scan.yaml'`.

**Action**

- Calls `_write_yaml`, `_yaml_data`, `load_scan_config`.

**Expected result**

- Direct assertions: `assert load_scan_config(scan_path).scan_config.aoi.commune_codes == [code]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `canonical france commune codes are accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_yaml`, `_yaml_data`, `load_scan_config`, `pytest.mark.parametrize`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_noncanonical_france_commune_codes_are_rejected`

**Signature**

```python
def test_noncanonical_france_commune_codes_are_rejected(
    tmp_path: Path,
    code: object,
) -> None:
```

**Purpose**

Protects the `noncanonical france commune codes are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `code`.
- Contains 5 explicit setup/context statement(s).
- Computes `scan_data` from `_yaml_data(SCAN_PATH)`.
- Computes `scan_data['profile']['path']` from `str(PROFILE_PATH)`.
- Computes `scan_data['aoi']['commune_codes']` from `[code]`.
- Computes `scan_path` from `tmp_path / 'scan.yaml'`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `load_scan_config(scan_path)` for its validation or side effect.

**Action**

- Calls `_write_yaml`, `_yaml_data`, `load_scan_config`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): load_scan_config(scan_path)`.

**Regression protected**

- Protects the exact `noncanonical france commune codes are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_yaml`, `_yaml_data`, `load_scan_config`, `pytest.mark.parametrize`, `pytest.raises`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_aoi_requires_nonempty_unique_commune_codes`

**Signature**

```python
def test_aoi_requires_nonempty_unique_commune_codes(
    tmp_path: Path,
    codes: list[str],
) -> None:
```

**Purpose**

Protects the `aoi requires nonempty unique commune codes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `codes`.
- Contains 5 explicit setup/context statement(s).
- Computes `scan_data` from `_yaml_data(SCAN_PATH)`.
- Computes `scan_data['profile']['path']` from `str(PROFILE_PATH)`.
- Computes `scan_data['aoi']['commune_codes']` from `codes`.
- Computes `scan_path` from `tmp_path / 'scan.yaml'`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `load_scan_config(scan_path)` for its validation or side effect.

**Action**

- Calls `_write_yaml`, `_yaml_data`, `load_scan_config`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): load_scan_config(scan_path)`.

**Regression protected**

- Protects the exact `aoi requires nonempty unique commune codes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_yaml`, `_yaml_data`, `load_scan_config`, `pytest.mark.parametrize`, `pytest.raises`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_scan_and_profile_identity_must_match`

**Signature**

```python
def test_scan_and_profile_identity_must_match(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
```

**Purpose**

Protects the `scan and profile identity must match` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data[field]` from `value`.
- Enters managed context(s) `pytest.raises(ValidationError, match=field)` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError, match=field): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `scan and profile identity must match` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_crs_contract_is_exact`

**Signature**

```python
def test_profile_crs_contract_is_exact(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
```

**Purpose**

Protects the `profile crs contract is exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `profile_data` from `_yaml_data(PROFILE_PATH)`.
- Computes `profile_data['crs'][field]` from `value`.
- Enters managed context(s) `pytest.raises(ValidationError, match='CRS|crs|storage|calculation')` and executes: Calls `_load_temporary_profile(tmp_path, profile_data)` for its validation or side effect.

**Action**

- Calls `_load_temporary_profile`, `_yaml_data`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError, match='CRS|crs|storage|calculation'): _load_temporary_profile(tmp_path, profile_data)`.

**Regression protected**

- Protects the exact `profile crs contract is exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_temporary_profile`, `_yaml_data`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `aoi` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `calibration` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `commune_codes` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `crs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `enabled` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `max_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `min_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parcel` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `path` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sample_size` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `shape_screening` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `unexpected` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
