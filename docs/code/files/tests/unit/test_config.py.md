# `tests/unit/test_config.py`

## File identity

- Repository path: `tests/unit/test_config.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `config` contracts exercised in this file.
- Source SHA256: `5ab7e31a98262a2d35698c8e6c950b2998c438bd0050d9ecf2ac5cf80a952597`

## 1. Purpose

Provides complete unit and regression coverage for the `config` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from pathlib import Path`

### Third-party packages

- `import pytest`
- `import yaml`
- `from pydantic import ValidationError`

### Internal LandScout imports

- `from landscout.config import load_scan_config`

## 4. Contract taxonomy

### A. Python constants

#### `PROJECT_ROOT`

```python
PROJECT_ROOT = Path(__file__).parents[2]
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `SCAN_PATH`

```python
SCAN_PATH = PROJECT_ROOT / "configs/scans/bess_muret.yaml"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_config.py::_temporary_scan` (value argument/reference), `tests/unit/test_config.py::test_valid_config_loads` (value argument/reference), `tests/unit/test_config.py::test_invalid_commune_code_fails` (value argument/reference), `tests/unit/test_config.py::test_unknown_scan_fields_are_rejected` (value argument/reference), `tests/unit/test_config.py::test_canonical_france_commune_codes_are_accepted` (value argument/reference), `tests/unit/test_config.py::test_noncanonical_france_commune_codes_are_rejected` (value argument/reference), `tests/unit/test_config.py::test_aoi_requires_nonempty_unique_commune_codes` (value argument/reference).

#### `PROFILE_PATH`

```python
PROFILE_PATH = PROJECT_ROOT / "configs/profiles/bess_default_fr.yaml"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_config.py::test_negative_minimum_area_fails` (value argument/reference), `tests/unit/test_config.py::test_maximum_area_smaller_than_minimum_fails` (value argument/reference), `tests/unit/test_config.py::test_invalid_shape_threshold_fails` (value argument/reference), `tests/unit/test_config.py::test_invalid_calibration_percentage_fails` (value argument/reference), `tests/unit/test_config.py::test_invalid_calibration_sample_size_fails` (value argument/reference), `tests/unit/test_config.py::test_empty_calibration_metadata_fails` (value argument/reference), `tests/unit/test_config.py::test_enabled_shape_screening_requires_policy_values` (value argument/reference), `tests/unit/test_config.py::test_enabled_shape_screening_requires_complete_calibration` (value argument/reference), `tests/unit/test_config.py::test_shape_screening_can_be_disabled_without_policy_values` (value argument/reference), `tests/unit/test_config.py::test_unknown_scan_fields_are_rejected` (value argument/reference), `tests/unit/test_config.py::test_unknown_profile_fields_are_rejected` (value argument/reference), `tests/unit/test_config.py::test_parcel_numeric_contract_is_strict_and_finite` (value argument/reference), `tests/unit/test_config.py::test_calibration_sample_size_is_strict_positive_integer` (value argument/reference), `tests/unit/test_config.py::test_shape_enabled_is_strict_boolean` (value argument/reference), `tests/unit/test_config.py::test_canonical_france_commune_codes_are_accepted` (value argument/reference), `tests/unit/test_config.py::test_noncanonical_france_commune_codes_are_rejected` (value argument/reference), `tests/unit/test_config.py::test_aoi_requires_nonempty_unique_commune_codes` (value argument/reference), `tests/unit/test_config.py::test_scan_and_profile_identity_must_match` (value argument/reference), `tests/unit/test_config.py::test_profile_crs_contract_is_exact` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_yaml_data`

**Exact signature**

```python
def _yaml_data(path: Path) -> dict:
```

**Purpose**

Private `test` helper for yaml data; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict`.
- Every observed return expression is reproduced without truncation:
```python
yaml.safe_load(stream)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_config.py::_temporary_scan` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_invalid_commune_code_fails` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_negative_minimum_area_fails` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_maximum_area_smaller_than_minimum_fails` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_invalid_shape_threshold_fails` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_invalid_calibration_percentage_fails` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_invalid_calibration_sample_size_fails` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_empty_calibration_metadata_fails` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_enabled_shape_screening_requires_policy_values` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_enabled_shape_screening_requires_complete_calibration` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_shape_screening_can_be_disabled_without_policy_values` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_unknown_scan_fields_are_rejected` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_unknown_profile_fields_are_rejected` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_parcel_numeric_contract_is_strict_and_finite` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_calibration_sample_size_is_strict_positive_integer` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_shape_enabled_is_strict_boolean` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_canonical_france_commune_codes_are_accepted` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_noncanonical_france_commune_codes_are_rejected` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_aoi_requires_nonempty_unique_commune_codes` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_scan_and_profile_identity_must_match` via `_yaml_data`.
- direct call or construction: `tests/unit/test_config.py::test_profile_crs_contract_is_exact` via `_yaml_data`.

**Complete source-ordered implementation**

```python
def _yaml_data(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_yaml`

**Exact signature**

```python
def _write_yaml(path: Path, data: dict) -> None:
```

**Purpose**

Serializes yaml; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: `path.write_text`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_config.py::_temporary_scan` via `_write_yaml`.
- direct call or construction: `tests/unit/test_config.py::_load_temporary_profile` via `_write_yaml`.
- direct call or construction: `tests/unit/test_config.py::test_invalid_commune_code_fails` via `_write_yaml`.
- direct call or construction: `tests/unit/test_config.py::test_negative_minimum_area_fails` via `_write_yaml`.
- direct call or construction: `tests/unit/test_config.py::test_maximum_area_smaller_than_minimum_fails` via `_write_yaml`.
- direct call or construction: `tests/unit/test_config.py::test_unknown_scan_fields_are_rejected` via `_write_yaml`.
- direct call or construction: `tests/unit/test_config.py::test_canonical_france_commune_codes_are_accepted` via `_write_yaml`.
- direct call or construction: `tests/unit/test_config.py::test_noncanonical_france_commune_codes_are_rejected` via `_write_yaml`.
- direct call or construction: `tests/unit/test_config.py::test_aoi_requires_nonempty_unique_commune_codes` via `_write_yaml`.

**Complete source-ordered implementation**

```python
def _write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_temporary_scan`

**Exact signature**

```python
def _temporary_scan(tmp_path: Path, profile_path: Path) -> Path:
```

**Purpose**

Private `test` helper for temporary scan; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
scan_path
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `scan_data['profile']['path']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_config.py::_load_temporary_profile` via `_temporary_scan`.
- direct call or construction: `tests/unit/test_config.py::test_negative_minimum_area_fails` via `_temporary_scan`.
- direct call or construction: `tests/unit/test_config.py::test_maximum_area_smaller_than_minimum_fails` via `_temporary_scan`.
- direct call or construction: `tests/unit/test_config.py::test_missing_profile_fails` via `_temporary_scan`.

**Complete source-ordered implementation**

```python
def _temporary_scan(tmp_path: Path, profile_path: Path) -> Path:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(profile_path)
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)
    return scan_path
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_load_temporary_profile`

**Exact signature**

```python
def _load_temporary_profile(tmp_path: Path, profile_data: dict):
```

**Purpose**

Reads and validates temporary profile; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `unannotated`.
- Every observed return expression is reproduced without truncation:
```python
load_scan_config(_temporary_scan(tmp_path, profile_path))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_config.py::test_invalid_shape_threshold_fails` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_invalid_calibration_percentage_fails` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_invalid_calibration_sample_size_fails` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_empty_calibration_metadata_fails` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_enabled_shape_screening_requires_policy_values` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_enabled_shape_screening_requires_complete_calibration` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_shape_screening_can_be_disabled_without_policy_values` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_unknown_profile_fields_are_rejected` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_parcel_numeric_contract_is_strict_and_finite` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_calibration_sample_size_is_strict_positive_integer` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_shape_enabled_is_strict_boolean` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_scan_and_profile_identity_must_match` via `_load_temporary_profile`.
- direct call or construction: `tests/unit/test_config.py::test_profile_crs_contract_is_exact` via `_load_temporary_profile`.

**Complete source-ordered implementation**

```python
def _load_temporary_profile(tmp_path: Path, profile_data: dict):
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)
    return load_scan_config(_temporary_scan(tmp_path, profile_path))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_config_loads`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
shape_screening = loaded.profile.shape_screening
calibration = shape_screening.calibration
```

**Action**

```python
loaded = load_scan_config(SCAN_PATH)
```

**Expected result**

```python
assert loaded.scan_config.aoi.commune_codes == ["31395"]
assert loaded.profile.technology == "BESS"
assert loaded.profile_path == PROFILE_PATH
assert shape_screening.enabled is True
assert shape_screening.min_width_m == 15
assert shape_screening.max_length_width_ratio == 10
assert calibration is not None
assert calibration.policy_version == "muret_empirical_v1"
assert calibration.method == "empirical_distribution"
assert calibration.calibration_scope == "Muret 31395"
assert calibration.sample_size == 4013
assert calibration.calibrated_at == "2026-08-11"
assert calibration.target_retention_pct == 90
assert calibration.observed_retention_pct == 90.655370
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_config_loads() -> None:
    loaded = load_scan_config(SCAN_PATH)

    assert loaded.scan_config.aoi.commune_codes == ["31395"]
    assert loaded.profile.technology == "BESS"
    assert loaded.profile_path == PROFILE_PATH

    shape_screening = loaded.profile.shape_screening
    assert shape_screening.enabled is True
    assert shape_screening.min_width_m == 15
    assert shape_screening.max_length_width_ratio == 10

    calibration = shape_screening.calibration
    assert calibration is not None
    assert calibration.policy_version == "muret_empirical_v1"
    assert calibration.method == "empirical_distribution"
    assert calibration.calibration_scope == "Muret 31395"
    assert calibration.sample_size == 4013
    assert calibration.calibrated_at == "2026-08-11"
    assert calibration.target_retention_pct == 90
    assert calibration.observed_retention_pct == 90.655370
```

### `test_invalid_commune_code_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
scan_data = _yaml_data(SCAN_PATH)
scan_data["aoi"]["commune_codes"] = ["3139"]
scan_path = tmp_path / "scan.yaml"
_write_yaml(scan_path, scan_data)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        load_scan_config(scan_path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_invalid_commune_code_fails(tmp_path: Path) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["aoi"]["commune_codes"] = ["3139"]
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError):
        load_scan_config(scan_path)
```

### `test_negative_minimum_area_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["parcel"]["min_area_m2"] = -1
profile_path = tmp_path / "profile.yaml"
_write_yaml(profile_path, profile_data)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_negative_minimum_area_fails(tmp_path: Path) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"]["min_area_m2"] = -1
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)

    with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))
```

### `test_maximum_area_smaller_than_minimum_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["parcel"]["max_area_m2"] = 1000
profile_path = tmp_path / "profile.yaml"
_write_yaml(profile_path, profile_data)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_maximum_area_smaller_than_minimum_fails(tmp_path: Path) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"]["max_area_m2"] = 1000
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)

    with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))
```

### `test_missing_profile_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
missing_profile = tmp_path / "missing.yaml"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(FileNotFoundError):
        load_scan_config(_temporary_scan(tmp_path, missing_profile))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_missing_profile_fails(tmp_path: Path) -> None:
    missing_profile = tmp_path / "missing.yaml"

    with pytest.raises(FileNotFoundError):
        load_scan_config(_temporary_scan(tmp_path, missing_profile))
```

### `test_invalid_shape_threshold_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `invalid_value`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["shape_screening"][field] = invalid_value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_invalid_shape_threshold_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"][field] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_invalid_calibration_percentage_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `invalid_value`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["shape_screening"]["calibration"][field] = invalid_value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_invalid_calibration_percentage_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"][field] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_invalid_calibration_sample_size_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `invalid_value`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["shape_screening"]["calibration"]["sample_size"] = invalid_value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_invalid_calibration_sample_size_fails(
    tmp_path: Path, invalid_value: int
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"]["sample_size"] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_empty_calibration_metadata_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["shape_screening"]["calibration"][field] = "   "
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_empty_calibration_metadata_fails(tmp_path: Path, field: str) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"][field] = "   "

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_enabled_shape_screening_requires_policy_values`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
del profile_data["shape_screening"][field]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError, match="enabled shape screening requires"):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_enabled_shape_screening_requires_policy_values(
    tmp_path: Path, field: str
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    del profile_data["shape_screening"][field]

    with pytest.raises(ValidationError, match="enabled shape screening requires"):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_enabled_shape_screening_requires_complete_calibration`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
del profile_data["shape_screening"]["calibration"][field]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_enabled_shape_screening_requires_complete_calibration(
    tmp_path: Path, field: str
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    del profile_data["shape_screening"]["calibration"][field]

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_shape_screening_can_be_disabled_without_policy_values`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["shape_screening"] = {"enabled": False}
loaded = _load_temporary_profile(tmp_path, profile_data)
shape_screening = loaded.profile.shape_screening
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert shape_screening.enabled is False
assert shape_screening.min_width_m is None
assert shape_screening.max_length_width_ratio is None
assert shape_screening.calibration is None
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_shape_screening_can_be_disabled_without_policy_values(
    tmp_path: Path,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"] = {"enabled": False}

    loaded = _load_temporary_profile(tmp_path, profile_data)

    shape_screening = loaded.profile.shape_screening
    assert shape_screening.enabled is False
    assert shape_screening.min_width_m is None
    assert shape_screening.max_length_width_ratio is None
    assert shape_screening.calibration is None
```

### `test_unknown_scan_fields_are_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `section`.

**Setup**

```python
scan_data = _yaml_data(SCAN_PATH)
scan_data["profile"]["path"] = str(PROFILE_PATH)
target = scan_data if section is None else scan_data[section]
target[field] = "value"
scan_path = tmp_path / "scan.yaml"
_write_yaml(scan_path, scan_data)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError, match=field):
        load_scan_config(scan_path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unknown_scan_fields_are_rejected(
    tmp_path: Path,
    section: str | None,
    field: str,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    target = scan_data if section is None else scan_data[section]
    target[field] = "value"
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError, match=field):
        load_scan_config(scan_path)
```

### `test_unknown_profile_fields_are_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `section`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data[section]["unexpected"] = "value"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError, match="unexpected"):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unknown_profile_fields_are_rejected(
    tmp_path: Path,
    section: str,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data[section]["unexpected"] = "value"

    with pytest.raises(ValidationError, match="unexpected"):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_parcel_numeric_contract_is_strict_and_finite`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["parcel"][field] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_parcel_numeric_contract_is_strict_and_finite(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"][field] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_calibration_sample_size_is_strict_positive_integer`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["shape_screening"]["calibration"]["sample_size"] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_calibration_sample_size_is_strict_positive_integer(
    tmp_path: Path,
    value: object,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"]["sample_size"] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_shape_enabled_is_strict_boolean`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["shape_screening"]["enabled"] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_shape_enabled_is_strict_boolean(tmp_path: Path, value: object) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["enabled"] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_canonical_france_commune_codes_are_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `code`.

**Setup**

```python
scan_data = _yaml_data(SCAN_PATH)
scan_data["profile"]["path"] = str(PROFILE_PATH)
scan_data["aoi"]["commune_codes"] = [code]
scan_path = tmp_path / "scan.yaml"
_write_yaml(scan_path, scan_data)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert load_scan_config(scan_path).scan_config.aoi.commune_codes == [code]
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_canonical_france_commune_codes_are_accepted(
    tmp_path: Path,
    code: str,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    scan_data["aoi"]["commune_codes"] = [code]
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    assert load_scan_config(scan_path).scan_config.aoi.commune_codes == [code]
```

### `test_noncanonical_france_commune_codes_are_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `code`.

**Setup**

```python
scan_data = _yaml_data(SCAN_PATH)
scan_data["profile"]["path"] = str(PROFILE_PATH)
scan_data["aoi"]["commune_codes"] = [code]
scan_path = tmp_path / "scan.yaml"
_write_yaml(scan_path, scan_data)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        load_scan_config(scan_path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_noncanonical_france_commune_codes_are_rejected(
    tmp_path: Path,
    code: object,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    scan_data["aoi"]["commune_codes"] = [code]
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError):
        load_scan_config(scan_path)
```

### `test_aoi_requires_nonempty_unique_commune_codes`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `codes`.

**Setup**

```python
scan_data = _yaml_data(SCAN_PATH)
scan_data["profile"]["path"] = str(PROFILE_PATH)
scan_data["aoi"]["commune_codes"] = codes
scan_path = tmp_path / "scan.yaml"
_write_yaml(scan_path, scan_data)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        load_scan_config(scan_path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_aoi_requires_nonempty_unique_commune_codes(
    tmp_path: Path,
    codes: list[str],
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    scan_data["aoi"]["commune_codes"] = codes
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError):
        load_scan_config(scan_path)
```

### `test_scan_and_profile_identity_must_match`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data[field] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError, match=field):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_scan_and_profile_identity_must_match(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data[field] = value

    with pytest.raises(ValidationError, match=field):
        _load_temporary_profile(tmp_path, profile_data)
```

### `test_profile_crs_contract_is_exact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
profile_data = _yaml_data(PROFILE_PATH)
profile_data["crs"][field] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError, match="CRS|crs|storage|calculation"):
        _load_temporary_profile(tmp_path, profile_data)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_profile_crs_contract_is_exact(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["crs"][field] = value

    with pytest.raises(ValidationError, match="CRS|crs|storage|calculation"):
        _load_temporary_profile(tmp_path, profile_data)
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
