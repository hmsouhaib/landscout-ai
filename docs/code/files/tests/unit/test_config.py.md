# `tests/unit/test_config.py`

## File identity

- Repository path: `tests/unit/test_config.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `config` contracts exercised in this file.
- Source SHA256: `73c1455c23e98d6a24c3cc712ea14663542777082b6439e6d8ebbda8225e42f2`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for config; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `config` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `PROJECT_ROOT`

- Category: module constant or closed domain.
- Exact declaration:

```python
PROJECT_ROOT = Path(__file__).parents[2]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SCAN_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
SCAN_PATH = PROJECT_ROOT / "configs/scans/bess_muret.yaml"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PROFILE_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
PROFILE_PATH = PROJECT_ROOT / "configs/profiles/bess_default_fr.yaml"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_yaml_data`

**Purpose:** Implements `yaml data` within the file role: Provides complete unit and regression coverage for the `config` contracts exercised in this file.

**Exact signature**

```python
def _yaml_data(path: Path) -> dict:
```

- Exact decorators: none.
- Declared return annotation: `dict`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `yaml.safe_load(stream)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_config::_temporary_scan` via `_yaml_data`
- value/type reference: `tests.unit.test_config::_temporary_scan` via `_yaml_data`
- direct call: `tests.unit.test_config::test_trust_bearing_yaml_rejects_duplicate_mapping_keys` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_trust_bearing_yaml_rejects_duplicate_mapping_keys` via `_yaml_data`
- direct call: `tests.unit.test_config::test_invalid_commune_code_fails` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_invalid_commune_code_fails` via `_yaml_data`
- direct call: `tests.unit.test_config::test_negative_minimum_area_fails` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_negative_minimum_area_fails` via `_yaml_data`
- direct call: `tests.unit.test_config::test_maximum_area_smaller_than_minimum_fails` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_maximum_area_smaller_than_minimum_fails` via `_yaml_data`
- direct call: `tests.unit.test_config::test_invalid_shape_threshold_fails` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_invalid_shape_threshold_fails` via `_yaml_data`
- direct call: `tests.unit.test_config::test_invalid_calibration_percentage_fails` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_invalid_calibration_percentage_fails` via `_yaml_data`
- direct call: `tests.unit.test_config::test_invalid_calibration_sample_size_fails` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_invalid_calibration_sample_size_fails` via `_yaml_data`
- direct call: `tests.unit.test_config::test_empty_calibration_metadata_fails` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_empty_calibration_metadata_fails` via `_yaml_data`
- direct call: `tests.unit.test_config::test_enabled_shape_screening_requires_policy_values` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_enabled_shape_screening_requires_policy_values` via `_yaml_data`
- direct call: `tests.unit.test_config::test_enabled_shape_screening_requires_complete_calibration` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_enabled_shape_screening_requires_complete_calibration` via `_yaml_data`
- direct call: `tests.unit.test_config::test_shape_screening_can_be_disabled_without_policy_values` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_shape_screening_can_be_disabled_without_policy_values` via `_yaml_data`
- direct call: `tests.unit.test_config::test_unknown_scan_fields_are_rejected` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_unknown_scan_fields_are_rejected` via `_yaml_data`
- direct call: `tests.unit.test_config::test_unknown_profile_fields_are_rejected` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_unknown_profile_fields_are_rejected` via `_yaml_data`
- direct call: `tests.unit.test_config::test_parcel_numeric_contract_is_strict_and_finite` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_parcel_numeric_contract_is_strict_and_finite` via `_yaml_data`
- direct call: `tests.unit.test_config::test_calibration_sample_size_is_strict_positive_integer` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_calibration_sample_size_is_strict_positive_integer` via `_yaml_data`
- direct call: `tests.unit.test_config::test_shape_enabled_is_strict_boolean` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_shape_enabled_is_strict_boolean` via `_yaml_data`
- direct call: `tests.unit.test_config::test_canonical_france_commune_codes_are_accepted` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_canonical_france_commune_codes_are_accepted` via `_yaml_data`
- direct call: `tests.unit.test_config::test_noncanonical_france_commune_codes_are_rejected` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_noncanonical_france_commune_codes_are_rejected` via `_yaml_data`
- direct call: `tests.unit.test_config::test_aoi_requires_nonempty_unique_commune_codes` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_aoi_requires_nonempty_unique_commune_codes` via `_yaml_data`
- direct call: `tests.unit.test_config::test_scan_and_profile_identity_must_match` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_scan_and_profile_identity_must_match` via `_yaml_data`
- direct call: `tests.unit.test_config::test_profile_crs_contract_is_exact` via `_yaml_data`
- value/type reference: `tests.unit.test_config::test_profile_crs_contract_is_exact` via `_yaml_data`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.open` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_load` | `yaml.safe_load` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _yaml_data(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_yaml`

**Purpose:** Implements `write yaml` within the file role: Provides complete unit and regression coverage for the `config` contracts exercised in this file.

**Exact signature**

```python
def _write_yaml(path: Path, data: dict) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `data` | positional-or-keyword | `dict` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_config::_temporary_scan` via `_write_yaml`
- value/type reference: `tests.unit.test_config::_temporary_scan` via `_write_yaml`
- direct call: `tests.unit.test_config::_load_temporary_profile` via `_write_yaml`
- value/type reference: `tests.unit.test_config::_load_temporary_profile` via `_write_yaml`
- direct call: `tests.unit.test_config::test_invalid_commune_code_fails` via `_write_yaml`
- value/type reference: `tests.unit.test_config::test_invalid_commune_code_fails` via `_write_yaml`
- direct call: `tests.unit.test_config::test_negative_minimum_area_fails` via `_write_yaml`
- value/type reference: `tests.unit.test_config::test_negative_minimum_area_fails` via `_write_yaml`
- direct call: `tests.unit.test_config::test_maximum_area_smaller_than_minimum_fails` via `_write_yaml`
- value/type reference: `tests.unit.test_config::test_maximum_area_smaller_than_minimum_fails` via `_write_yaml`
- direct call: `tests.unit.test_config::test_unknown_scan_fields_are_rejected` via `_write_yaml`
- value/type reference: `tests.unit.test_config::test_unknown_scan_fields_are_rejected` via `_write_yaml`
- direct call: `tests.unit.test_config::test_canonical_france_commune_codes_are_accepted` via `_write_yaml`
- value/type reference: `tests.unit.test_config::test_canonical_france_commune_codes_are_accepted` via `_write_yaml`
- direct call: `tests.unit.test_config::test_noncanonical_france_commune_codes_are_rejected` via `_write_yaml`
- value/type reference: `tests.unit.test_config::test_noncanonical_france_commune_codes_are_rejected` via `_write_yaml`
- direct call: `tests.unit.test_config::test_aoi_requires_nonempty_unique_commune_codes` via `_write_yaml`
- value/type reference: `tests.unit.test_config::test_aoi_requires_nonempty_unique_commune_codes` via `_write_yaml`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_dump` | `yaml.safe_dump` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_temporary_scan`

**Purpose:** Implements `temporary scan` within the file role: Provides complete unit and regression coverage for the `config` contracts exercised in this file.

**Exact signature**

```python
def _temporary_scan(tmp_path: Path, profile_path: Path) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `profile_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `scan_path`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_config::_load_temporary_profile` via `_temporary_scan`
- value/type reference: `tests.unit.test_config::_load_temporary_profile` via `_temporary_scan`
- direct call: `tests.unit.test_config::test_negative_minimum_area_fails` via `_temporary_scan`
- value/type reference: `tests.unit.test_config::test_negative_minimum_area_fails` via `_temporary_scan`
- direct call: `tests.unit.test_config::test_maximum_area_smaller_than_minimum_fails` via `_temporary_scan`
- value/type reference: `tests.unit.test_config::test_maximum_area_smaller_than_minimum_fails` via `_temporary_scan`
- direct call: `tests.unit.test_config::test_missing_profile_fails` via `_temporary_scan`
- value/type reference: `tests.unit.test_config::test_missing_profile_fails` via `_temporary_scan`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_yaml` | `tests.unit.test_config._write_yaml` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `scan_data["profile"]["path"] = str(profile_path)` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_load_temporary_profile`

**Purpose:** Implements `load temporary profile` within the file role: Provides complete unit and regression coverage for the `config` contracts exercised in this file.

**Exact signature**

```python
def _load_temporary_profile(tmp_path: Path, profile_data: dict):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `profile_data` | positional-or-keyword | `dict` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `load_scan_config(_temporary_scan(tmp_path, profile_path))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_config::test_invalid_shape_threshold_fails` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_invalid_shape_threshold_fails` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_invalid_calibration_percentage_fails` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_invalid_calibration_percentage_fails` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_invalid_calibration_sample_size_fails` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_invalid_calibration_sample_size_fails` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_empty_calibration_metadata_fails` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_empty_calibration_metadata_fails` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_enabled_shape_screening_requires_policy_values` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_enabled_shape_screening_requires_policy_values` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_enabled_shape_screening_requires_complete_calibration` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_enabled_shape_screening_requires_complete_calibration` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_shape_screening_can_be_disabled_without_policy_values` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_shape_screening_can_be_disabled_without_policy_values` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_unknown_profile_fields_are_rejected` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_unknown_profile_fields_are_rejected` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_parcel_numeric_contract_is_strict_and_finite` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_parcel_numeric_contract_is_strict_and_finite` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_calibration_sample_size_is_strict_positive_integer` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_calibration_sample_size_is_strict_positive_integer` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_shape_enabled_is_strict_boolean` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_shape_enabled_is_strict_boolean` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_scan_and_profile_identity_must_match` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_scan_and_profile_identity_must_match` via `_load_temporary_profile`
- direct call: `tests.unit.test_config::test_profile_crs_contract_is_exact` via `_load_temporary_profile`
- value/type reference: `tests.unit.test_config::test_profile_crs_contract_is_exact` via `_load_temporary_profile`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_yaml` | `tests.unit.test_config._write_yaml` |
| `load_scan_config` | `landscout.config.load_scan_config` |
| `_temporary_scan` | `tests.unit.test_config._temporary_scan` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _load_temporary_profile(tmp_path: Path, profile_data: dict):
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)
    return load_scan_config(_temporary_scan(tmp_path, profile_path))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_config_loads`

**Purpose:** Regression invariant: valid config loads. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_config_loads() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert loaded.scan_config.aoi.commune_codes == ("31395",)`
  - `assert loaded.profile.technology == "BESS"`
  - `assert loaded.profile_path == PROFILE_PATH`
  - `assert shape_screening.enabled is True`
  - `assert shape_screening.min_width_m == 15`
  - `assert shape_screening.max_length_width_ratio == 10`
  - `assert calibration is not None`
  - `assert calibration.policy_version == "muret_empirical_v1"`
  - `assert calibration.method == "empirical_distribution"`
  - `assert calibration.calibration_scope == "Muret 31395"`
  - `assert calibration.sample_size == 4013`
  - `assert calibration.calibrated_at == "2026-08-11"`
  - `assert calibration.target_retention_pct == 90`
  - `assert calibration.observed_retention_pct == 90.655370`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_scan_config` | `landscout.config.load_scan_config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_config_loads() -> None:
    loaded = load_scan_config(SCAN_PATH)

    assert loaded.scan_config.aoi.commune_codes == ("31395",)
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_trust_bearing_yaml_rejects_duplicate_mapping_keys`

**Purpose:** Regression invariant: trust bearing yaml rejects duplicate mapping keys. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_trust_bearing_yaml_rejects_duplicate_mapping_keys(
    tmp_path: Path,
    document: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("document", ["scan", "profile"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `document` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises((TypeError, ValueError), match="(?i)duplicate")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_dump` | `yaml.safe_dump` |
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `profile_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `action` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text`<br>`profile_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `scan_data["profile"]["path"] = str(PROFILE_PATH)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_trust_bearing_yaml_rejects_duplicate_mapping_keys(
    tmp_path: Path,
    document: str,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    if document == "scan":
        duplicate = yaml.safe_dump(scan_data, sort_keys=False) + yaml.safe_dump(
            {"scan": scan_data["scan"]}, sort_keys=False
        )
        path = tmp_path / "scan.yaml"
        path.write_text(duplicate, encoding="utf-8")
        action = lambda: load_scan_config(path)
    else:
        profile_data = _yaml_data(PROFILE_PATH)
        duplicate = yaml.safe_dump(profile_data, sort_keys=False) + yaml.safe_dump(
            {"parcel": profile_data["parcel"]}, sort_keys=False
        )
        profile_path = tmp_path / "profile.yaml"
        profile_path.write_text(duplicate, encoding="utf-8")
        action = lambda: load_scan_config(_temporary_scan(tmp_path, profile_path))

    with pytest.raises((TypeError, ValueError), match="(?i)duplicate"):
        action()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_loaded_scan_and_profile_models_are_immutable`

**Purpose:** Regression invariant: loaded scan and profile models are immutable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_loaded_scan_and_profile_models_are_immutable() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="frozen")`
  - `pytest.raises(AttributeError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_scan_config` | `landscout.config.load_scan_config` |
| `pytest.raises` | `pytest.raises` |
| `loaded.scan_config.aoi.commune_codes.append` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `loaded.scan_config.scan.name = "mutated"`<br>`loaded.profile.parcel.min_area_m2 = 1.0`<br>`loaded.scan_config.aoi.commune_codes.append("75056")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_loaded_scan_and_profile_models_are_immutable() -> None:
    loaded = load_scan_config(SCAN_PATH)

    with pytest.raises(ValidationError, match="frozen"):
        loaded.scan_config.scan.name = "mutated"
    with pytest.raises(ValidationError, match="frozen"):
        loaded.profile.parcel.min_area_m2 = 1.0
    with pytest.raises(AttributeError):
        loaded.scan_config.aoi.commune_codes.append("75056")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_commune_code_fails`

**Purpose:** Regression invariant: invalid commune code fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_commune_code_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `_write_yaml` | `tests.unit.test_config._write_yaml` |
| `pytest.raises` | `pytest.raises` |
| `load_scan_config` | `landscout.config.load_scan_config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `scan_data["aoi"]["commune_codes"] = ["3139"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_commune_code_fails(tmp_path: Path) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["aoi"]["commune_codes"] = ["3139"]
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError):
        load_scan_config(scan_path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_negative_minimum_area_fails`

**Purpose:** Regression invariant: negative minimum area fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_negative_minimum_area_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `_write_yaml` | `tests.unit.test_config._write_yaml` |
| `pytest.raises` | `pytest.raises` |
| `load_scan_config` | `landscout.config.load_scan_config` |
| `_temporary_scan` | `tests.unit.test_config._temporary_scan` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["parcel"]["min_area_m2"] = -1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_negative_minimum_area_fails(tmp_path: Path) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"]["min_area_m2"] = -1
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)

    with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_maximum_area_smaller_than_minimum_fails`

**Purpose:** Regression invariant: maximum area smaller than minimum fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_maximum_area_smaller_than_minimum_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `_write_yaml` | `tests.unit.test_config._write_yaml` |
| `pytest.raises` | `pytest.raises` |
| `load_scan_config` | `landscout.config.load_scan_config` |
| `_temporary_scan` | `tests.unit.test_config._temporary_scan` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["parcel"]["max_area_m2"] = 1000` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_maximum_area_smaller_than_minimum_fails(tmp_path: Path) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"]["max_area_m2"] = 1000
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)

    with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_profile_fails`

**Purpose:** Regression invariant: missing profile fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_profile_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(FileNotFoundError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `load_scan_config` | `landscout.config.load_scan_config` |
| `_temporary_scan` | `tests.unit.test_config._temporary_scan` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_profile_fails(tmp_path: Path) -> None:
    missing_profile = tmp_path / "missing.yaml"

    with pytest.raises(FileNotFoundError):
        load_scan_config(_temporary_scan(tmp_path, missing_profile))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_shape_threshold_fails`

**Purpose:** Regression invariant: invalid shape threshold fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_shape_threshold_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("min_width_m", -1),
        ("min_width_m", 0),
        ("max_length_width_ratio", 0),
        ("max_length_width_ratio", 0.999),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `invalid_value` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["shape_screening"][field] = invalid_value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_shape_threshold_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"][field] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_calibration_percentage_fails`

**Purpose:** Regression invariant: invalid calibration percentage fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_calibration_percentage_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("target_retention_pct", -1),
        ("target_retention_pct", 0),
        ("target_retention_pct", 100.001),
        ("observed_retention_pct", -0.001),
        ("observed_retention_pct", 100.001),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `invalid_value` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["shape_screening"]["calibration"][field] = invalid_value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_calibration_percentage_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"][field] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_calibration_sample_size_fails`

**Purpose:** Regression invariant: invalid calibration sample size fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_calibration_sample_size_fails(
    tmp_path: Path, invalid_value: int
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("invalid_value", [-1, 0])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `invalid_value` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["shape_screening"]["calibration"]["sample_size"] = invalid_value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_calibration_sample_size_fails(
    tmp_path: Path, invalid_value: int
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"]["sample_size"] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_empty_calibration_metadata_fails`

**Purpose:** Regression invariant: empty calibration metadata fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_empty_calibration_metadata_fails(tmp_path: Path, field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "field",
    ["policy_version", "method", "calibration_scope", "calibrated_at"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["shape_screening"]["calibration"][field] = "   "` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_empty_calibration_metadata_fails(tmp_path: Path, field: str) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"][field] = "   "

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_enabled_shape_screening_requires_policy_values`

**Purpose:** Regression invariant: enabled shape screening requires policy values. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_enabled_shape_screening_requires_policy_values(
    tmp_path: Path, field: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "field", ["min_width_m", "max_length_width_ratio", "calibration"]
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="enabled shape screening requires")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_enabled_shape_screening_requires_policy_values(
    tmp_path: Path, field: str
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    del profile_data["shape_screening"][field]

    with pytest.raises(ValidationError, match="enabled shape screening requires"):
        _load_temporary_profile(tmp_path, profile_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_enabled_shape_screening_requires_complete_calibration`

**Purpose:** Regression invariant: enabled shape screening requires complete calibration. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_enabled_shape_screening_requires_complete_calibration(
    tmp_path: Path, field: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "field",
    [
        "policy_version",
        "method",
        "calibration_scope",
        "sample_size",
        "calibrated_at",
        "target_retention_pct",
        "observed_retention_pct",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_enabled_shape_screening_requires_complete_calibration(
    tmp_path: Path, field: str
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    del profile_data["shape_screening"]["calibration"][field]

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_screening_can_be_disabled_without_policy_values`

**Purpose:** Regression invariant: shape screening can be disabled without policy values. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_screening_can_be_disabled_without_policy_values(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert shape_screening.enabled is False`
  - `assert shape_screening.min_width_m is None`
  - `assert shape_screening.max_length_width_ratio is None`
  - `assert shape_screening.calibration is None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["shape_screening"] = {"enabled": False}` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_scan_fields_are_rejected`

**Purpose:** Regression invariant: unknown scan fields are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_scan_fields_are_rejected(
    tmp_path: Path,
    section: str | None,
    field: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("section", "field"),
    [(None, "unknown"), ("aoi", "unexpected"), ("profile", "unexpected")],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `section` | positional-or-keyword | `str \| None` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match=field)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_yaml` | `tests.unit.test_config._write_yaml` |
| `pytest.raises` | `pytest.raises` |
| `load_scan_config` | `landscout.config.load_scan_config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `scan_data["profile"]["path"] = str(PROFILE_PATH)`<br>`target[field] = "value"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_profile_fields_are_rejected`

**Purpose:** Regression invariant: unknown profile fields are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_profile_fields_are_rejected(
    tmp_path: Path,
    section: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("section", ["parcel", "crs", "shape_screening"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `section` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="unexpected")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data[section]["unexpected"] = "value"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_numeric_contract_is_strict_and_finite`

**Purpose:** Regression invariant: parcel numeric contract is strict and finite. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_numeric_contract_is_strict_and_finite(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("min_area_m2", 0),
        ("max_area_m2", -1),
        ("max_area_m2", float("nan")),
        ("max_area_m2", float("inf")),
        ("max_area_m2", "15000"),
        ("min_area_m2", True),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["parcel"][field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_calibration_sample_size_is_strict_positive_integer`

**Purpose:** Regression invariant: calibration sample size is strict positive integer. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_calibration_sample_size_is_strict_positive_integer(
    tmp_path: Path,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", [True, "4013", 0, -1])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["shape_screening"]["calibration"]["sample_size"] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_enabled_is_strict_boolean`

**Purpose:** Regression invariant: shape enabled is strict boolean. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_enabled_is_strict_boolean(tmp_path: Path, value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", ["true", 1, 0])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["shape_screening"]["enabled"] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_shape_enabled_is_strict_boolean(tmp_path: Path, value: object) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["enabled"] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_canonical_france_commune_codes_are_accepted`

**Purpose:** Regression invariant: canonical france commune codes are accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_canonical_france_commune_codes_are_accepted(
    tmp_path: Path,
    code: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("code", ["31395", "75056", "2A004", "2B033"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `code` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert load_scan_config(scan_path).scan_config.aoi.commune_codes == (code,)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_yaml` | `tests.unit.test_config._write_yaml` |
| `load_scan_config` | `landscout.config.load_scan_config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `scan_data["profile"]["path"] = str(PROFILE_PATH)`<br>`scan_data["aoi"]["commune_codes"] = [code]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

    assert load_scan_config(scan_path).scan_config.aoi.commune_codes == (code,)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_noncanonical_france_commune_codes_are_rejected`

**Purpose:** Regression invariant: noncanonical france commune codes are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_noncanonical_france_commune_codes_are_rejected(
    tmp_path: Path,
    code: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "code",
    ["", "3139", "313950", "ABCDE", "2C004", "2a004", " 31395 ", 31395],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `code` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_yaml` | `tests.unit.test_config._write_yaml` |
| `pytest.raises` | `pytest.raises` |
| `load_scan_config` | `landscout.config.load_scan_config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `scan_data["profile"]["path"] = str(PROFILE_PATH)`<br>`scan_data["aoi"]["commune_codes"] = [code]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_aoi_requires_nonempty_unique_commune_codes`

**Purpose:** Regression invariant: aoi requires nonempty unique commune codes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_aoi_requires_nonempty_unique_commune_codes(
    tmp_path: Path,
    codes: list[str],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("codes", [[], ["31395", "31395"]])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `codes` | positional-or-keyword | `list[str]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_yaml` | `tests.unit.test_config._write_yaml` |
| `pytest.raises` | `pytest.raises` |
| `load_scan_config` | `landscout.config.load_scan_config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `scan_data["profile"]["path"] = str(PROFILE_PATH)`<br>`scan_data["aoi"]["commune_codes"] = codes` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_scan_and_profile_identity_must_match`

**Purpose:** Regression invariant: scan and profile identity must match. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_scan_and_profile_identity_must_match(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [("country", "BE"), ("technology", "SOLAR")],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match=field)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data[field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_crs_contract_is_exact`

**Purpose:** Regression invariant: profile crs contract is exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_crs_contract_is_exact(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [("storage", "EPSG:3857"), ("calculation", "EPSG:4326"), ("storage", "bad")],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="CRS\|crs\|storage\|calculation")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_yaml_data` | `tests.unit.test_config._yaml_data` |
| `pytest.raises` | `pytest.raises` |
| `_load_temporary_profile` | `tests.unit.test_config._load_temporary_profile` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `profile_data["crs"][field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **24**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_valid_config_loads` | none | none | 14 | Proves valid config loads using the exact source reproduced in section 7. |
| `test_trust_bearing_yaml_rejects_duplicate_mapping_keys` | pytest.mark.parametrize("document", ["scan", "profile"]) | pytest.raises((TypeError, ValueError), match="(?i)duplicate") | 0 | Proves trust bearing yaml rejects duplicate mapping keys using the exact source reproduced in section 7. |
| `test_loaded_scan_and_profile_models_are_immutable` | none | pytest.raises(ValidationError, match="frozen"); pytest.raises(ValidationError, match="frozen"); pytest.raises(AttributeError) | 0 | Proves loaded scan and profile models are immutable using the exact source reproduced in section 7. |
| `test_invalid_commune_code_fails` | none | pytest.raises(ValidationError) | 0 | Proves invalid commune code fails using the exact source reproduced in section 7. |
| `test_negative_minimum_area_fails` | none | pytest.raises(ValidationError) | 0 | Proves negative minimum area fails using the exact source reproduced in section 7. |
| `test_maximum_area_smaller_than_minimum_fails` | none | pytest.raises(ValidationError) | 0 | Proves maximum area smaller than minimum fails using the exact source reproduced in section 7. |
| `test_missing_profile_fails` | none | pytest.raises(FileNotFoundError) | 0 | Proves missing profile fails using the exact source reproduced in section 7. |
| `test_invalid_shape_threshold_fails` | pytest.mark.parametrize(<br>    ("field", "invalid_value"),<br>    [<br>        ("min_width_m", -1),<br>        ("min_width_m", 0),<br>        ("max_length_width_ratio", 0),<br>        ("max_length_width_ratio", 0.999),<br>    ],<br>) | pytest.raises(ValidationError) | 0 | Proves invalid shape threshold fails using the exact source reproduced in section 7. |
| `test_invalid_calibration_percentage_fails` | pytest.mark.parametrize(<br>    ("field", "invalid_value"),<br>    [<br>        ("target_retention_pct", -1),<br>        ("target_retention_pct", 0),<br>        ("target_retention_pct", 100.001),<br>        ("observed_retention_pct", -0.001),<br>        ("observed_retention_pct", 100.001),<br>    ],<br>) | pytest.raises(ValidationError) | 0 | Proves invalid calibration percentage fails using the exact source reproduced in section 7. |
| `test_invalid_calibration_sample_size_fails` | pytest.mark.parametrize("invalid_value", [-1, 0]) | pytest.raises(ValidationError) | 0 | Proves invalid calibration sample size fails using the exact source reproduced in section 7. |
| `test_empty_calibration_metadata_fails` | pytest.mark.parametrize(<br>    "field",<br>    ["policy_version", "method", "calibration_scope", "calibrated_at"],<br>) | pytest.raises(ValidationError) | 0 | Proves empty calibration metadata fails using the exact source reproduced in section 7. |
| `test_enabled_shape_screening_requires_policy_values` | pytest.mark.parametrize(<br>    "field", ["min_width_m", "max_length_width_ratio", "calibration"]<br>) | pytest.raises(ValidationError, match="enabled shape screening requires") | 0 | Proves enabled shape screening requires policy values using the exact source reproduced in section 7. |
| `test_enabled_shape_screening_requires_complete_calibration` | pytest.mark.parametrize(<br>    "field",<br>    [<br>        "policy_version",<br>        "method",<br>        "calibration_scope",<br>        "sample_size",<br>        "calibrated_at",<br>        "target_retention_pct",<br>        "observed_retention_pct",<br>    ],<br>) | pytest.raises(ValidationError) | 0 | Proves enabled shape screening requires complete calibration using the exact source reproduced in section 7. |
| `test_shape_screening_can_be_disabled_without_policy_values` | none | none | 4 | Proves shape screening can be disabled without policy values using the exact source reproduced in section 7. |
| `test_unknown_scan_fields_are_rejected` | pytest.mark.parametrize(<br>    ("section", "field"),<br>    [(None, "unknown"), ("aoi", "unexpected"), ("profile", "unexpected")],<br>) | pytest.raises(ValidationError, match=field) | 0 | Proves unknown scan fields are rejected using the exact source reproduced in section 7. |
| `test_unknown_profile_fields_are_rejected` | pytest.mark.parametrize("section", ["parcel", "crs", "shape_screening"]) | pytest.raises(ValidationError, match="unexpected") | 0 | Proves unknown profile fields are rejected using the exact source reproduced in section 7. |
| `test_parcel_numeric_contract_is_strict_and_finite` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("min_area_m2", 0),<br>        ("max_area_m2", -1),<br>        ("max_area_m2", float("nan")),<br>        ("max_area_m2", float("inf")),<br>        ("max_area_m2", "15000"),<br>        ("min_area_m2", True),<br>    ],<br>) | pytest.raises(ValidationError) | 0 | Proves parcel numeric contract is strict and finite using the exact source reproduced in section 7. |
| `test_calibration_sample_size_is_strict_positive_integer` | pytest.mark.parametrize("value", [True, "4013", 0, -1]) | pytest.raises(ValidationError) | 0 | Proves calibration sample size is strict positive integer using the exact source reproduced in section 7. |
| `test_shape_enabled_is_strict_boolean` | pytest.mark.parametrize("value", ["true", 1, 0]) | pytest.raises(ValidationError) | 0 | Proves shape enabled is strict boolean using the exact source reproduced in section 7. |
| `test_canonical_france_commune_codes_are_accepted` | pytest.mark.parametrize("code", ["31395", "75056", "2A004", "2B033"]) | none | 1 | Proves canonical france commune codes are accepted using the exact source reproduced in section 7. |
| `test_noncanonical_france_commune_codes_are_rejected` | pytest.mark.parametrize(<br>    "code",<br>    ["", "3139", "313950", "ABCDE", "2C004", "2a004", " 31395 ", 31395],<br>) | pytest.raises(ValidationError) | 0 | Proves noncanonical france commune codes are rejected using the exact source reproduced in section 7. |
| `test_aoi_requires_nonempty_unique_commune_codes` | pytest.mark.parametrize("codes", [[], ["31395", "31395"]]) | pytest.raises(ValidationError) | 0 | Proves aoi requires nonempty unique commune codes using the exact source reproduced in section 7. |
| `test_scan_and_profile_identity_must_match` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [("country", "BE"), ("technology", "SOLAR")],<br>) | pytest.raises(ValidationError, match=field) | 0 | Proves scan and profile identity must match using the exact source reproduced in section 7. |
| `test_profile_crs_contract_is_exact` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [("storage", "EPSG:3857"), ("calculation", "EPSG:4326"), ("storage", "bad")],<br>) | pytest.raises(ValidationError, match="CRS\|crs\|storage\|calculation") | 0 | Proves profile crs contract is exact using the exact source reproduced in section 7. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from landscout.config import load_scan_config

PROJECT_ROOT = Path(__file__).parents[2]
SCAN_PATH = PROJECT_ROOT / "configs/scans/bess_muret.yaml"
PROFILE_PATH = PROJECT_ROOT / "configs/profiles/bess_default_fr.yaml"


def _yaml_data(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def _write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data), encoding="utf-8")


def _temporary_scan(tmp_path: Path, profile_path: Path) -> Path:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(profile_path)
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)
    return scan_path


def _load_temporary_profile(tmp_path: Path, profile_data: dict):
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)
    return load_scan_config(_temporary_scan(tmp_path, profile_path))


def test_valid_config_loads() -> None:
    loaded = load_scan_config(SCAN_PATH)

    assert loaded.scan_config.aoi.commune_codes == ("31395",)
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


@pytest.mark.parametrize("document", ["scan", "profile"])
def test_trust_bearing_yaml_rejects_duplicate_mapping_keys(
    tmp_path: Path,
    document: str,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    if document == "scan":
        duplicate = yaml.safe_dump(scan_data, sort_keys=False) + yaml.safe_dump(
            {"scan": scan_data["scan"]}, sort_keys=False
        )
        path = tmp_path / "scan.yaml"
        path.write_text(duplicate, encoding="utf-8")
        action = lambda: load_scan_config(path)
    else:
        profile_data = _yaml_data(PROFILE_PATH)
        duplicate = yaml.safe_dump(profile_data, sort_keys=False) + yaml.safe_dump(
            {"parcel": profile_data["parcel"]}, sort_keys=False
        )
        profile_path = tmp_path / "profile.yaml"
        profile_path.write_text(duplicate, encoding="utf-8")
        action = lambda: load_scan_config(_temporary_scan(tmp_path, profile_path))

    with pytest.raises((TypeError, ValueError), match="(?i)duplicate"):
        action()


def test_loaded_scan_and_profile_models_are_immutable() -> None:
    loaded = load_scan_config(SCAN_PATH)

    with pytest.raises(ValidationError, match="frozen"):
        loaded.scan_config.scan.name = "mutated"
    with pytest.raises(ValidationError, match="frozen"):
        loaded.profile.parcel.min_area_m2 = 1.0
    with pytest.raises(AttributeError):
        loaded.scan_config.aoi.commune_codes.append("75056")


def test_invalid_commune_code_fails(tmp_path: Path) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["aoi"]["commune_codes"] = ["3139"]
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError):
        load_scan_config(scan_path)


def test_negative_minimum_area_fails(tmp_path: Path) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"]["min_area_m2"] = -1
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)

    with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))


def test_maximum_area_smaller_than_minimum_fails(tmp_path: Path) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"]["max_area_m2"] = 1000
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)

    with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))


def test_missing_profile_fails(tmp_path: Path) -> None:
    missing_profile = tmp_path / "missing.yaml"

    with pytest.raises(FileNotFoundError):
        load_scan_config(_temporary_scan(tmp_path, missing_profile))


@pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("min_width_m", -1),
        ("min_width_m", 0),
        ("max_length_width_ratio", 0),
        ("max_length_width_ratio", 0.999),
    ],
)
def test_invalid_shape_threshold_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"][field] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("target_retention_pct", -1),
        ("target_retention_pct", 0),
        ("target_retention_pct", 100.001),
        ("observed_retention_pct", -0.001),
        ("observed_retention_pct", 100.001),
    ],
)
def test_invalid_calibration_percentage_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"][field] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize("invalid_value", [-1, 0])
def test_invalid_calibration_sample_size_fails(
    tmp_path: Path, invalid_value: int
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"]["sample_size"] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    "field",
    ["policy_version", "method", "calibration_scope", "calibrated_at"],
)
def test_empty_calibration_metadata_fails(tmp_path: Path, field: str) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"][field] = "   "

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    "field", ["min_width_m", "max_length_width_ratio", "calibration"]
)
def test_enabled_shape_screening_requires_policy_values(
    tmp_path: Path, field: str
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    del profile_data["shape_screening"][field]

    with pytest.raises(ValidationError, match="enabled shape screening requires"):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    "field",
    [
        "policy_version",
        "method",
        "calibration_scope",
        "sample_size",
        "calibrated_at",
        "target_retention_pct",
        "observed_retention_pct",
    ],
)
def test_enabled_shape_screening_requires_complete_calibration(
    tmp_path: Path, field: str
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    del profile_data["shape_screening"]["calibration"][field]

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


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


@pytest.mark.parametrize(
    ("section", "field"),
    [(None, "unknown"), ("aoi", "unexpected"), ("profile", "unexpected")],
)
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


@pytest.mark.parametrize("section", ["parcel", "crs", "shape_screening"])
def test_unknown_profile_fields_are_rejected(
    tmp_path: Path,
    section: str,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data[section]["unexpected"] = "value"

    with pytest.raises(ValidationError, match="unexpected"):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("min_area_m2", 0),
        ("max_area_m2", -1),
        ("max_area_m2", float("nan")),
        ("max_area_m2", float("inf")),
        ("max_area_m2", "15000"),
        ("min_area_m2", True),
    ],
)
def test_parcel_numeric_contract_is_strict_and_finite(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"][field] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize("value", [True, "4013", 0, -1])
def test_calibration_sample_size_is_strict_positive_integer(
    tmp_path: Path,
    value: object,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"]["sample_size"] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize("value", ["true", 1, 0])
def test_shape_enabled_is_strict_boolean(tmp_path: Path, value: object) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["enabled"] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize("code", ["31395", "75056", "2A004", "2B033"])
def test_canonical_france_commune_codes_are_accepted(
    tmp_path: Path,
    code: str,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    scan_data["aoi"]["commune_codes"] = [code]
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    assert load_scan_config(scan_path).scan_config.aoi.commune_codes == (code,)


@pytest.mark.parametrize(
    "code",
    ["", "3139", "313950", "ABCDE", "2C004", "2a004", " 31395 ", 31395],
)
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


@pytest.mark.parametrize("codes", [[], ["31395", "31395"]])
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


@pytest.mark.parametrize(
    ("field", "value"),
    [("country", "BE"), ("technology", "SOLAR")],
)
def test_scan_and_profile_identity_must_match(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data[field] = value

    with pytest.raises(ValidationError, match=field):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    ("field", "value"),
    [("storage", "EPSG:3857"), ("calculation", "EPSG:4326"), ("storage", "bad")],
)
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
