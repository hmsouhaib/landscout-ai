# `src/landscout/config.py`

## File identity

- Repository path: `src/landscout/config.py`
- File type: Python source
- Primary responsibility: Loads and strictly validates scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.
- Layer / domain: `package/configuration` / `project`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `f9c9bc778b59669f54c095444efc87b18518572f920be4bc3f79ce37c487a044`

## 1. Purpose

Loads and strictly validates scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

## 2. Position in LandScout architecture

This file is a `package/configuration` artifact in the `project` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Annotated, Any` — required by the implementation paths and symbols documented below.

### Third-party

- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import ( BaseModel, BeforeValidator, ConfigDict, Field, StrictBool, StringConstraints, model_validator, )` — required by the implementation paths and symbols documented below.
- `from pydantic_core import PydanticCustomError` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- None.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

### `_ConfigModel`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid")`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `ParcelConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `min_area_m2` | `StrictPositiveFloat` | `required` | Metric area in square metres, derived only on an EPSG:2154 calculation geometry where applicable. |
| `max_area_m2` | `StrictPositiveFloat` | `required` | Metric area in square metres, derived only on an EPSG:2154 calculation geometry where applicable. |

**Validators and methods:**

- `validate_area_range` — `def validate_area_range(self) -> "ParcelConfig":`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `ShapeCalibrationConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `policy_version` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `method` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `calibration_scope` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `sample_size` | `StrictPositiveInt` | `required` | `StrictPositiveInt` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `calibrated_at` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `target_retention_pct` | `Annotated[StrictFiniteFloat, Field(gt=0, le=100, allow_inf_nan=False)]` | `required` | Percentage quantity with the domain and denominator validated by its stage. |
| `observed_retention_pct` | `Annotated[StrictFiniteFloat, Field(ge=0, le=100, allow_inf_nan=False)]` | `required` | Percentage quantity with the domain and denominator validated by its stage. |

**Validators and methods:**

- None.

### `ShapeScreeningConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `enabled` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `min_width_m` | `StrictPositiveFloat | None` | `None` | Metric distance or length in metres; the full field name identifies the measurement. |
| `max_length_width_ratio` | `StrictFiniteFloat | None` | `Field(default=None, ge=1, allow_inf_nan=False)` | `StrictFiniteFloat | None` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `calibration` | `ShapeCalibrationConfig | None` | `None` | `ShapeCalibrationConfig | None` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `validate_enabled_policy` — `def validate_enabled_policy(self) -> "ShapeScreeningConfig":`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `CrsConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `storage` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `calculation` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `validate_crs_contract` — `def validate_crs_contract(self) -> "CrsConfig":`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `BessProfile`

**Purpose:** Carries deterministic diagnostic/profile statistics without changing the underlying evidence rows.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `country` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `technology` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel` | `ParcelConfig` | `required` | `ParcelConfig` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `shape_screening` | `ShapeScreeningConfig` | `required` | `ShapeScreeningConfig` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `crs` | `CrsConfig` | `required` | `CrsConfig` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `ScanMetadata`

**Purpose:** Represents strict metadata used to reconstruct or validate a byte-bound cache/source object.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `name` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `country` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `technology` | `NonEmptyString` | `required` | `NonEmptyString` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `AoiConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `commune_codes` | `list[CommuneCode]` | `Field(min_length=1)` | `list[CommuneCode]` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `validate_unique_communes` — `def validate_unique_communes(self) -> "AoiConfig":`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `ProfileReference`

**Purpose:** Carries deterministic diagnostic/profile statistics without changing the underlying evidence rows.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `path` | `Path` | `required` | `Path` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `OutputConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `directory` | `Path` | `required` | `Path` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `ScanConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `scan` | `ScanMetadata` | `required` | `ScanMetadata` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `aoi` | `AoiConfig` | `required` | `AoiConfig` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `profile` | `ProfileReference` | `required` | `ProfileReference` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `output` | `OutputConfig` | `required` | `OutputConfig` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `LoadedScanConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_ConfigModel`.

**Model form and mutability:** class inheriting from `_ConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `scan_config` | `ScanConfig` | `required` | Validated configuration object or field controlling exact source/stage behavior. |
| `profile` | `BessProfile` | `required` | `BessProfile` state used by `src/landscout/config.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `profile_path` | `Path` | `required` | Filesystem path used for source, cache, artifact, or configuration access under the owning function's containment and link rules. |

**Validators and methods:**

- `validate_scan_profile_identity` — `def validate_scan_profile_identity(self) -> "LoadedScanConfig":`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

## 6. Functions and methods

### `_strict_finite_number`

**Signature**

```python
def _strict_finite_number(value: object) -> object:
```

**Purpose**

Implements strict finite number according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `isinstance(value, bool) or not isinstance(value, Real)`. When true: Raises `PydanticCustomError('strict_number', 'value must be a strict YAML number')`.
2. Checks `not isfinite(float(value))`. When true: Raises `ValueError('value must be finite')`.
3. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Real)` is true.
- Rejects or diverts the path when `not isfinite(float(value))` is true.

**Exceptions**

- Explicitly raises: `PydanticCustomError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PydanticCustomError`, `ValueError`, `float`, `isfinite`, `isinstance`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `ParcelConfig.validate_area_range`

**Signature**

```python
def validate_area_range(self) -> "ParcelConfig":
```

**Purpose**

Validates and rejects malformed area range according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `'ParcelConfig'`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `self.max_area_m2 <= self.min_area_m2`. When true: Raises `ValueError('max_area_m2 must be greater than min_area_m2')`.
2. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `self.max_area_m2 <= self.min_area_m2` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `model_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `ShapeScreeningConfig.validate_enabled_policy`

**Signature**

```python
def validate_enabled_policy(self) -> "ShapeScreeningConfig":
```

**Purpose**

Validates and rejects malformed enabled policy according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `'ShapeScreeningConfig'`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `not self.enabled`. When true: Returns `self`.
2. Computes `required_values` from `{'min_width_m': self.min_width_m, 'max_length_width_ratio': self.max_length_width_ratio, 'calibration': self.calibration}`.
3. Computes `missing` from `[name for name, value in required_values.items() if value is None]`.
4. Checks `missing`. When true: Computes `formatted` from `', '.join(missing)`. Raises `ValueError(f'enabled shape screening requires: {formatted}')`.
5. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `missing` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `ValueError`, `model_validator`, `required_values.items`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `CrsConfig.validate_crs_contract`

**Signature**

```python
def validate_crs_contract(self) -> "CrsConfig":
```

**Purpose**

Validates and rejects malformed crs contract according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `'CrsConfig'`. Observed return expression(s): `self`.

**Algorithm**

1. Iterates `(field, value, expected)` over `(('storage', self.storage, 4326), ('calculation', self.calculation, 2154))`. For each value: Runs guarded operation: Computes `observed` from `CRS.from_user_input(value)`. Handles `Exception`. Checks `not observed.equals(CRS.from_epsg(expected))`. When true: Raises `ValueError(f'{field} CRS must be EPSG:{expected}')`.
2. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `not observed.equals(CRS.from_epsg(expected))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `CRS.from_user_input`, `ValueError`, `model_validator`, `observed.equals`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `AoiConfig.validate_unique_communes`

**Signature**

```python
def validate_unique_communes(self) -> "AoiConfig":
```

**Purpose**

Validates and rejects malformed unique communes according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `'AoiConfig'`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `len(set(self.commune_codes)) != len(self.commune_codes)`. When true: Raises `ValueError('commune_codes must not contain duplicates')`.
2. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `len(set(self.commune_codes)) != len(self.commune_codes)` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `len`, `model_validator`, `set`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `LoadedScanConfig.validate_scan_profile_identity`

**Signature**

```python
def validate_scan_profile_identity(self) -> "LoadedScanConfig":
```

**Purpose**

Validates and rejects malformed scan profile identity according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `'LoadedScanConfig'`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `self.scan_config.scan.country != self.profile.country`. When true: Raises `ValueError('scan country must equal profile country')`.
2. Checks `self.scan_config.scan.technology != self.profile.technology`. When true: Raises `ValueError('scan technology must equal profile technology')`.
3. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `self.scan_config.scan.country != self.profile.country` is true.
- Rejects or diverts the path when `self.scan_config.scan.technology != self.profile.technology` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `model_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_load_yaml`

**Signature**

```python
def _load_yaml(path: Path) -> dict[str, Any]:
```

**Purpose**

Loads yaml according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, Any]`. Observed return expression(s): `content`.

**Algorithm**

1. Enters managed context(s) `path.open(encoding='utf-8')` and executes: Computes `content` from `yaml.safe_load(stream)`.
2. Checks `not isinstance(content, dict)`. When true: Raises `TypeError(f'Expected a YAML mapping in {path}')`.
3. Returns `content`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(content, dict)` is true.

**Exceptions**

- Explicitly raises: `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `TypeError`, `isinstance`, `path.open`, `yaml.safe_load`.

**Known repository callers**

- `src/landscout/config.py` — `load_scan_config`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_resolve_profile_path`

**Signature**

```python
def _resolve_profile_path(scan_path: Path, profile_path: Path) -> Path:
```

**Purpose**

Resolves profile path according to the exact implementation and guards in this file.

**Inputs**

- `scan_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `profile_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `project_root / profile_path`; `profile_path`.

**Algorithm**

1. Checks `profile_path.is_absolute()`. When true: Returns `profile_path`.
2. Computes `resolved_scan_path` from `scan_path.resolve()`.
3. Computes `project_root` from `resolved_scan_path.parents[2]`.
4. Returns `project_root / profile_path`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `profile_path.is_absolute`, `scan_path.resolve`.

**Known repository callers**

- `src/landscout/config.py` — `load_scan_config`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `load_scan_config`

**Signature**

```python
def load_scan_config(path: Path) -> LoadedScanConfig:
```

**Purpose**

Loads scan config according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `LoadedScanConfig`. Observed return expression(s): `LoadedScanConfig(scan_config=scan_config, profile=profile, profile_path=profile_path)`.

**Algorithm**

1. Computes `scan_path` from `path.resolve()`.
2. Computes `scan_config` from `ScanConfig.model_validate(_load_yaml(scan_path))`.
3. Computes `profile_path` from `_resolve_profile_path(scan_path, scan_config.profile.path)`.
4. Checks `not profile_path.is_file()`. When true: Raises `FileNotFoundError(f'Profile file does not exist: {profile_path}')`.
5. Computes `profile` from `BessProfile.model_validate(_load_yaml(profile_path))`.
6. Returns `LoadedScanConfig(scan_config=scan_config, profile=profile, profile_path=profile_path)`.

**Validation and invariants**

- Rejects or diverts the path when `not profile_path.is_file()` is true.

**Exceptions**

- Explicitly raises: `FileNotFoundError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_load_yaml`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessProfile.model_validate`, `FileNotFoundError`, `LoadedScanConfig`, `ScanConfig.model_validate`, `_load_yaml`, `_resolve_profile_path`, `path.resolve`, `profile_path.is_file`.

**Known repository callers**

- `tests/unit/test_config.py` — `_load_temporary_profile`
- `tests/unit/test_config.py` — `test_aoi_requires_nonempty_unique_commune_codes`
- `tests/unit/test_config.py` — `test_canonical_france_commune_codes_are_accepted`
- `tests/unit/test_config.py` — `test_invalid_commune_code_fails`
- `tests/unit/test_config.py` — `test_maximum_area_smaller_than_minimum_fails`
- `tests/unit/test_config.py` — `test_missing_profile_fails`
- `tests/unit/test_config.py` — `test_negative_minimum_area_fails`
- `tests/unit/test_config.py` — `test_noncanonical_france_commune_codes_are_rejected`
- `tests/unit/test_config.py` — `test_unknown_scan_fields_are_rejected`
- `tests/unit/test_config.py` — `test_valid_config_loads`

**Tests**

- `tests/unit/test_config.py::test_aoi_requires_nonempty_unique_commune_codes`
- `tests/unit/test_config.py::test_canonical_france_commune_codes_are_accepted`
- `tests/unit/test_config.py::test_invalid_commune_code_fails`
- `tests/unit/test_config.py::test_maximum_area_smaller_than_minimum_fails`
- `tests/unit/test_config.py::test_missing_profile_fails`
- `tests/unit/test_config.py::test_negative_minimum_area_fails`
- `tests/unit/test_config.py::test_noncanonical_france_commune_codes_are_rejected`
- `tests/unit/test_config.py::test_unknown_scan_fields_are_rejected`
- `tests/unit/test_config.py::test_valid_config_loads`

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

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

This file contributes to LandScout's `project` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- This project file does not implement a business algorithm.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
