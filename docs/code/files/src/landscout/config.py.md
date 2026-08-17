# `src/landscout/config.py`

## File identity

- Repository path: `src/landscout/config.py`
- File type: Python source
- Layer: package/configuration
- Domain: project
- Responsibility: Loads and strictly validates scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.
- Source SHA256: `f9c9bc778b59669f54c095444efc87b18518572f920be4bc3f79ce37c487a044`

## 1. Purpose

Loads and strictly validates scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

## 2. Position in LandScout architecture

This file belongs to the **package/configuration** layer and the **project** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from math import isfinite`
- `from numbers import Real`
- `from pathlib import Path`
- `from typing import Annotated, Any`

### Third-party packages

- `import yaml`
- `from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    StrictBool,
    StringConstraints,
    model_validator,
)`
- `from pydantic_core import PydanticCustomError`
- `from pyproj import CRS`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

#### `NonEmptyString`

```python
NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
```

String constrained non-empty after the exact StringConstraints behavior in the declaration. Enforced/consumed by `src/landscout/config.py::ShapeCalibrationConfig` (type annotation), `src/landscout/config.py::CrsConfig` (type annotation), `src/landscout/config.py::BessProfile` (type annotation), `src/landscout/config.py::ScanMetadata` (type annotation).

#### `CommuneCode`

```python
CommuneCode = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^(?:\d{5}|2[AB]\d{3})$"),
]
```

Canonical French commune identity constrained by the exact regex in the declaration. Enforced/consumed by `src/landscout/config.py::AoiConfig` (type annotation).

#### `StrictFiniteFloat`

```python
StrictFiniteFloat = Annotated[float, BeforeValidator(_strict_finite_number)]
```

Non-Boolean real converted to float only after the named finite-number validator accepts it. Enforced/consumed by `src/landscout/config.py::ShapeCalibrationConfig` (type annotation), `src/landscout/config.py::ShapeScreeningConfig` (type annotation).

#### `StrictPositiveFloat`

```python
StrictPositiveFloat = Annotated[
    float,
    BeforeValidator(_strict_finite_number),
    Field(gt=0, allow_inf_nan=False),
]
```

StrictFiniteFloat plus a greater-than-zero Pydantic bound. Enforced/consumed by `src/landscout/config.py::ParcelConfig` (type annotation), `src/landscout/config.py::ShapeScreeningConfig` (type annotation).

#### `StrictPositiveInt`

```python
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
```

Strict integer greater than zero; Boolean and numeric coercions are rejected by Pydantic Field(strict=True, gt=0). Enforced/consumed by `src/landscout/config.py::ShapeCalibrationConfig` (type annotation).


### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `_ConfigModel`

**Purpose:** Validates the project contract carried by its explicit validators and inherited fields.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class _ConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
```

### `ParcelConfig`

**Purpose:** Configured lower and upper parcel-area screening thresholds in square metres; these are policy inputs, not measured geometry.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `min_area_m2` | `min_area_m2: StrictPositiveFloat` | Configured inclusive lower parcel-area screening threshold in square metres; not a measured parcel area. |
| `max_area_m2` | `max_area_m2: StrictPositiveFloat` | Configured inclusive upper parcel-area screening threshold in square metres; must exceed min_area_m2. |

**Validators (exact source)**

`validate_area_range`:

```python
def validate_area_range(self) -> "ParcelConfig":
        if self.max_area_m2 <= self.min_area_m2:
            raise ValueError("max_area_m2 must be greater than min_area_m2")
        return self
```

**Interface consumers**

- import: `src/landscout/stages/filter_parcels.py::<module>` via `from landscout.config import ParcelConfig, ShapeScreeningConfig`.
- import: `tests/unit/test_filter_parcels.py::<module>` via `from landscout.config import ParcelConfig`.
- type annotation: `src/landscout/config.py::BessProfile` via `ParcelConfig`.
- type annotation: `src/landscout/stages/filter_parcels.py::filter_parcels_by_area` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::area_config` via `ParcelConfig`.
- constructor call: `tests/unit/test_filter_parcels.py::area_config` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_minimum_boundary_is_included` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_maximum_boundary_is_included` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_rejected_parcel_has_expected_reason` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_no_parcel_disappears` via `ParcelConfig`.
- constructor call: `tests/unit/test_filter_parcels.py::test_thresholds_come_from_config` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_missing_parcel_id_fails` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_null_parcel_id_fails` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_duplicate_parcel_id_fails` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_candidate_and_rejected_ids_do_not_overlap` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_exact_parcel_ids_are_preserved` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_valid_geometry_requires_strict_positive_finite_area` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_area_filter_requires_exact_non_empty_parcel_ids` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_plain_dataframe` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_duplicate_columns` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_malformed_spatial_envelope` via `ParcelConfig`.
- type annotation: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_noncanonical_geometry_status` via `ParcelConfig`.

**Exact class source**

```python
class ParcelConfig(_ConfigModel):
    min_area_m2: StrictPositiveFloat
    max_area_m2: StrictPositiveFloat

    @model_validator(mode="after")
    def validate_area_range(self) -> "ParcelConfig":
        if self.max_area_m2 <= self.min_area_m2:
            raise ValueError("max_area_m2 must be greater than min_area_m2")
        return self
```

### `ShapeCalibrationConfig`

**Purpose:** Validated provenance and retention statistics for the configured shape-screening calibration snapshot.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `policy_version` | `policy_version: NonEmptyString` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `method` | `method: NonEmptyString` | `ShapeCalibrationConfig.method` represents the `method` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `calibration_scope` | `calibration_scope: NonEmptyString` | `ShapeCalibrationConfig.calibration_scope` represents the `calibration_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `sample_size` | `sample_size: StrictPositiveInt` | Strict positive integer number of rows in the diagnostic/profile sample. |
| `calibrated_at` | `calibrated_at: NonEmptyString` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `target_retention_pct` | `target_retention_pct: Annotated[
        StrictFiniteFloat, Field(gt=0, le=100, allow_inf_nan=False)
    ]` | Configured target retention percentage in (0, 100]. |
| `observed_retention_pct` | `observed_retention_pct: Annotated[
        StrictFiniteFloat, Field(ge=0, le=100, allow_inf_nan=False)
    ]` | Recorded observed retention percentage in [0, 100]. |

**Interface consumers**

- import: `tests/unit/test_filter_shape.py::<module>` via `from landscout.config import ShapeCalibrationConfig, ShapeScreeningConfig`.
- type annotation: `src/landscout/config.py::ShapeScreeningConfig` via `ShapeCalibrationConfig`.
- constructor call: `tests/unit/test_filter_shape.py::_shape_config` via `ShapeCalibrationConfig`.

**Exact class source**

```python
class ShapeCalibrationConfig(_ConfigModel):
    policy_version: NonEmptyString
    method: NonEmptyString
    calibration_scope: NonEmptyString
    sample_size: StrictPositiveInt
    calibrated_at: NonEmptyString
    target_retention_pct: Annotated[
        StrictFiniteFloat, Field(gt=0, le=100, allow_inf_nan=False)
    ]
    observed_retention_pct: Annotated[
        StrictFiniteFloat, Field(ge=0, le=100, allow_inf_nan=False)
    ]
```

### `ShapeScreeningConfig`

**Purpose:** Optional shape-screening policy thresholds and observed-retention evidence used by the parcel shape filter.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `enabled` | `enabled: StrictBool` | Strict Boolean switch; when true the width, ratio, and calibration fields are all mandatory. |
| `min_width_m` | `min_width_m: StrictPositiveFloat \| None = None` | Configured minimum parcel-width policy threshold in metres; not an observed width. |
| `max_length_width_ratio` | `max_length_width_ratio: StrictFiniteFloat \| None = Field(
        default=None, ge=1, allow_inf_nan=False
    )` | Configured maximum shape-policy length/width ratio; dimensionless and at least 1. |
| `calibration` | `calibration: ShapeCalibrationConfig \| None = None` | Optional calibration evidence; required when shape screening is enabled and absent permitted when disabled. |

**Validators (exact source)**

`validate_enabled_policy`:

```python
def validate_enabled_policy(self) -> "ShapeScreeningConfig":
        if not self.enabled:
            return self

        required_values = {
            "min_width_m": self.min_width_m,
            "max_length_width_ratio": self.max_length_width_ratio,
            "calibration": self.calibration,
        }
        missing = [name for name, value in required_values.items() if value is None]
        if missing:
            formatted = ", ".join(missing)
            raise ValueError(f"enabled shape screening requires: {formatted}")
        return self
```

**Interface consumers**

- import: `src/landscout/stages/filter_parcels.py::<module>` via `from landscout.config import ParcelConfig, ShapeScreeningConfig`.
- import: `tests/unit/test_filter_shape.py::<module>` via `from landscout.config import ShapeCalibrationConfig, ShapeScreeningConfig`.
- type annotation: `src/landscout/config.py::BessProfile` via `ShapeScreeningConfig`.
- type annotation: `src/landscout/stages/filter_parcels.py::filter_parcels_by_shape` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::_shape_config` via `ShapeScreeningConfig`.
- constructor call: `tests/unit/test_filter_shape.py::_shape_config` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::shape_config` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_exact_width_and_ratio_boundaries_are_retained` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_rejected_parcel_has_expected_primary_reason` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_rejection_reason_precedence_is_deterministic` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_shape_error_precedence_does_not_inspect_metrics` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_enabled_outputs_record_active_policy_metadata` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_enabled_partition_preserves_exact_ids_and_crs` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_filter_does_not_mutate_input` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_missing_required_column_fails` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_null_parcel_id_fails` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_duplicate_parcel_id_fails` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_unknown_crs_fails` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_unexpected_or_null_shape_status_fails` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_non_finite_known_metric_on_valid_row_fails` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_valid_shape_requires_strict_positive_width` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_valid_shape_requires_ratio_at_least_one` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_negative_ratio_cannot_pass_permissive_thresholds` via `ShapeScreeningConfig`.
- constructor call: `tests/unit/test_filter_shape.py::test_disabled_policy_is_an_exact_passthrough` via `ShapeScreeningConfig`.
- constructor call: `tests/unit/test_filter_shape.py::test_valid_shape_requires_complete_metrics_even_when_screening_disabled` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_valid_shape_rejects_every_incomplete_metric_form` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_shape_filter_rejects_plain_dataframe` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_shape_filter_rejects_duplicate_columns` via `ShapeScreeningConfig`.
- type annotation: `tests/unit/test_filter_shape.py::test_shape_filter_rejects_unreadable_crs` via `ShapeScreeningConfig`.

**Exact class source**

```python
class ShapeScreeningConfig(_ConfigModel):
    enabled: StrictBool
    min_width_m: StrictPositiveFloat | None = None
    max_length_width_ratio: StrictFiniteFloat | None = Field(
        default=None, ge=1, allow_inf_nan=False
    )
    calibration: ShapeCalibrationConfig | None = None

    @model_validator(mode="after")
    def validate_enabled_policy(self) -> "ShapeScreeningConfig":
        if not self.enabled:
            return self

        required_values = {
            "min_width_m": self.min_width_m,
            "max_length_width_ratio": self.max_length_width_ratio,
            "calibration": self.calibration,
        }
        missing = [name for name, value in required_values.items() if value is None]
        if missing:
            formatted = ", ".join(missing)
            raise ValueError(f"enabled shape screening requires: {formatted}")
        return self
```

### `CrsConfig`

**Purpose:** Canonical storage and calculation CRS identities required by the configured profile.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `storage` | `storage: NonEmptyString` | Configured storage CRS, required to be exactly EPSG:4326. |
| `calculation` | `calculation: NonEmptyString` | Configured metric calculation CRS, required to be exactly EPSG:2154. |

**Validators (exact source)**

`validate_crs_contract`:

```python
def validate_crs_contract(self) -> "CrsConfig":
        for field, value, expected in (
            ("storage", self.storage, 4326),
            ("calculation", self.calculation, 2154),
        ):
            try:
                observed = CRS.from_user_input(value)
            except Exception as error:
                raise ValueError(f"{field} CRS is unreadable") from error
            if not observed.equals(CRS.from_epsg(expected)):
                raise ValueError(f"{field} CRS must be EPSG:{expected}")
        return self
```

**Interface consumers**

- type annotation: `src/landscout/config.py::BessProfile` via `CrsConfig`.

**Exact class source**

```python
class CrsConfig(_ConfigModel):
    storage: NonEmptyString
    calculation: NonEmptyString

    @model_validator(mode="after")
    def validate_crs_contract(self) -> "CrsConfig":
        for field, value, expected in (
            ("storage", self.storage, 4326),
            ("calculation", self.calculation, 2154),
        ):
            try:
                observed = CRS.from_user_input(value)
            except Exception as error:
                raise ValueError(f"{field} CRS is unreadable") from error
            if not observed.equals(CRS.from_epsg(expected)):
                raise ValueError(f"{field} CRS must be EPSG:{expected}")
        return self
```

### `BessProfile`

**Purpose:** Validated French BESS profile combining parcel screening thresholds, CRS identities, provenance, and limitations.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `country` | `country: NonEmptyString` | Profile country identity; LoadedScanConfig requires it to equal ScanMetadata.country. |
| `technology` | `technology: NonEmptyString` | Profile technology identity; LoadedScanConfig requires it to equal ScanMetadata.technology. |
| `parcel` | `parcel: ParcelConfig` | Nested parcel-area screening policy containing the configured square-metre lower and upper bounds. |
| `shape_screening` | `shape_screening: ShapeScreeningConfig` | Nested optional shape-screening policy and its calibration evidence. |
| `crs` | `crs: CrsConfig` | Nested storage/calculation CRS contract fixed to EPSG:4326 and EPSG:2154 respectively. |

**Interface consumers**

- type annotation: `src/landscout/config.py::LoadedScanConfig` via `BessProfile`.

**Exact class source**

```python
class BessProfile(_ConfigModel):
    country: NonEmptyString
    technology: NonEmptyString
    parcel: ParcelConfig
    shape_screening: ShapeScreeningConfig
    crs: CrsConfig
```

### `ScanMetadata`

**Purpose:** Validated identity and provenance metadata for one configured LandScout scan.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `name` | `name: NonEmptyString` | Non-empty human-readable identity of the configured scan. |
| `country` | `country: NonEmptyString` | Scan country identity that must equal the loaded BESS profile country. |
| `technology` | `technology: NonEmptyString` | Scan technology identity that must equal the loaded BESS profile technology. |

**Interface consumers**

- type annotation: `src/landscout/config.py::ScanConfig` via `ScanMetadata`.

**Exact class source**

```python
class ScanMetadata(_ConfigModel):
    name: NonEmptyString
    country: NonEmptyString
    technology: NonEmptyString
```

### `AoiConfig`

**Purpose:** Validated non-empty unique list of canonical French commune codes defining the scan area of interest.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `commune_codes` | `commune_codes: list[CommuneCode] = Field(min_length=1)` | Non-empty ordered list of unique canonical French INSEE commune codes defining the scan area of interest. |

**Validators (exact source)**

`validate_unique_communes`:

```python
def validate_unique_communes(self) -> "AoiConfig":
        if len(set(self.commune_codes)) != len(self.commune_codes):
            raise ValueError("commune_codes must not contain duplicates")
        return self
```

**Interface consumers**

- type annotation: `src/landscout/config.py::ScanConfig` via `AoiConfig`.

**Exact class source**

```python
class AoiConfig(_ConfigModel):
    commune_codes: list[CommuneCode] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_unique_communes(self) -> "AoiConfig":
        if len(set(self.commune_codes)) != len(self.commune_codes):
            raise ValueError("commune_codes must not contain duplicates")
        return self
```

### `ProfileReference`

**Purpose:** Repository-relative reference to the separately validated BESS profile YAML.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `path` | `path: Path` | Repository-relative or absolute path resolved by load_scan_config to the separately parsed BESS profile YAML. |

**Interface consumers**

- type annotation: `src/landscout/config.py::ScanConfig` via `ProfileReference`.

**Exact class source**

```python
class ProfileReference(_ConfigModel):
    path: Path
```

### `OutputConfig`

**Purpose:** Configured output directory path for the scan; it does not itself create or write that directory.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `directory` | `directory: Path` | Configured output directory path retained by scan configuration; this model does not create the directory. |

**Interface consumers**

- type annotation: `src/landscout/config.py::ScanConfig` via `OutputConfig`.

**Exact class source**

```python
class OutputConfig(_ConfigModel):
    directory: Path
```

### `ScanConfig`

**Purpose:** Validated scan metadata, area of interest, profile reference, and output path from the scan YAML.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `scan` | `scan: ScanMetadata` | Nested scan identity metadata. |
| `aoi` | `aoi: AoiConfig` | Nested area-of-interest commune-code configuration. |
| `profile` | `profile: ProfileReference` | Nested path reference used to resolve and load the BESS profile YAML. |
| `output` | `output: OutputConfig` | Nested output-directory configuration. |

**Interface consumers**

- type annotation: `src/landscout/config.py::LoadedScanConfig` via `ScanConfig`.

**Exact class source**

```python
class ScanConfig(_ConfigModel):
    scan: ScanMetadata
    aoi: AoiConfig
    profile: ProfileReference
    output: OutputConfig
```

### `LoadedScanConfig`

**Purpose:** Validated combination of ScanConfig, the resolved BessProfile, and its physical profile path with matching country/technology identities.

**Kind:** Pydantic model.

**Inheritance:** `_ConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `scan_config` | `scan_config: ScanConfig` | Validated scan YAML model retained with the loaded result. |
| `profile` | `profile: BessProfile` | Separately validated BESS profile whose country/technology must match the scan metadata. |
| `profile_path` | `profile_path: Path` | Resolved physical path of the profile YAML that produced profile. |

**Validators (exact source)**

`validate_scan_profile_identity`:

```python
def validate_scan_profile_identity(self) -> "LoadedScanConfig":
        if self.scan_config.scan.country != self.profile.country:
            raise ValueError("scan country must equal profile country")
        if self.scan_config.scan.technology != self.profile.technology:
            raise ValueError("scan technology must equal profile technology")
        return self
```

**Interface consumers**

- type annotation: `src/landscout/config.py::load_scan_config` via `LoadedScanConfig`.
- constructor call: `src/landscout/config.py::load_scan_config` via `LoadedScanConfig`.

**Exact class source**

```python
class LoadedScanConfig(_ConfigModel):
    scan_config: ScanConfig
    profile: BessProfile
    profile_path: Path

    @model_validator(mode="after")
    def validate_scan_profile_identity(self) -> "LoadedScanConfig":
        if self.scan_config.scan.country != self.profile.country:
            raise ValueError("scan country must equal profile country")
        if self.scan_config.scan.technology != self.profile.technology:
            raise ValueError("scan technology must equal profile technology")
        return self
```


## 6. Functions and methods

### `_strict_finite_number`

**Exact signature**

```python
def _strict_finite_number(value: object) -> object:
```

**Purpose**

Private `project` helper for strict finite number; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Real)`.
- Guard with a raise path: `not isfinite(float(value))`.
- Explicit raise expressions: `PydanticCustomError('strict_number', 'value must be a strict YAML number')`, `ValueError('value must be finite')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `src/landscout/config.py::<module>` via `BeforeValidator(_strict_finite_number)`.

**Complete source-ordered implementation**

```python
def _strict_finite_number(value: object) -> object:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise PydanticCustomError(
            "strict_number",
            "value must be a strict YAML number",
        )
    if not isfinite(float(value)):
        raise ValueError("value must be finite")
    return value
```

**Business boundary**

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

### `ParcelConfig.validate_area_range`

**Exact signature**

```python
def validate_area_range(self) -> "ParcelConfig":
```

**Purpose**

Rejects malformed or inconsistent area range; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `'ParcelConfig'`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `self.max_area_m2 <= self.min_area_m2`.
- Explicit raise expressions: `ValueError('max_area_m2 must be greater than min_area_m2')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def validate_area_range(self) -> "ParcelConfig":
        if self.max_area_m2 <= self.min_area_m2:
            raise ValueError("max_area_m2 must be greater than min_area_m2")
        return self
```

**Business boundary**

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

### `ShapeScreeningConfig.validate_enabled_policy`

**Exact signature**

```python
def validate_enabled_policy(self) -> "ShapeScreeningConfig":
```

**Purpose**

Rejects malformed or inconsistent enabled policy; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `'ShapeScreeningConfig'`.
- Every observed return expression is reproduced without truncation:
```python
self

self
```

**Validation and exceptions**

- Guard with a raise path: `missing`.
- Explicit raise expressions: `ValueError(f'enabled shape screening requires: {formatted}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def validate_enabled_policy(self) -> "ShapeScreeningConfig":
        if not self.enabled:
            return self

        required_values = {
            "min_width_m": self.min_width_m,
            "max_length_width_ratio": self.max_length_width_ratio,
            "calibration": self.calibration,
        }
        missing = [name for name, value in required_values.items() if value is None]
        if missing:
            formatted = ", ".join(missing)
            raise ValueError(f"enabled shape screening requires: {formatted}")
        return self
```

**Business boundary**

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

### `CrsConfig.validate_crs_contract`

**Exact signature**

```python
def validate_crs_contract(self) -> "CrsConfig":
```

**Purpose**

Rejects malformed or inconsistent crs contract; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `'CrsConfig'`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `not observed.equals(CRS.from_epsg(expected))`.
- Explicit raise expressions: `ValueError(f'{field} CRS is unreadable')`, `ValueError(f'{field} CRS must be EPSG:{expected}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def validate_crs_contract(self) -> "CrsConfig":
        for field, value, expected in (
            ("storage", self.storage, 4326),
            ("calculation", self.calculation, 2154),
        ):
            try:
                observed = CRS.from_user_input(value)
            except Exception as error:
                raise ValueError(f"{field} CRS is unreadable") from error
            if not observed.equals(CRS.from_epsg(expected)):
                raise ValueError(f"{field} CRS must be EPSG:{expected}")
        return self
```

**Business boundary**

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

### `AoiConfig.validate_unique_communes`

**Exact signature**

```python
def validate_unique_communes(self) -> "AoiConfig":
```

**Purpose**

Rejects malformed or inconsistent unique communes; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `'AoiConfig'`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `len(set(self.commune_codes)) != len(self.commune_codes)`.
- Explicit raise expressions: `ValueError('commune_codes must not contain duplicates')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def validate_unique_communes(self) -> "AoiConfig":
        if len(set(self.commune_codes)) != len(self.commune_codes):
            raise ValueError("commune_codes must not contain duplicates")
        return self
```

**Business boundary**

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

### `LoadedScanConfig.validate_scan_profile_identity`

**Exact signature**

```python
def validate_scan_profile_identity(self) -> "LoadedScanConfig":
```

**Purpose**

Rejects malformed or inconsistent scan profile identity; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `'LoadedScanConfig'`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `self.scan_config.scan.country != self.profile.country`.
- Guard with a raise path: `self.scan_config.scan.technology != self.profile.technology`.
- Explicit raise expressions: `ValueError('scan country must equal profile country')`, `ValueError('scan technology must equal profile technology')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def validate_scan_profile_identity(self) -> "LoadedScanConfig":
        if self.scan_config.scan.country != self.profile.country:
            raise ValueError("scan country must equal profile country")
        if self.scan_config.scan.technology != self.profile.technology:
            raise ValueError("scan technology must equal profile technology")
        return self
```

**Business boundary**

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

### `_load_yaml`

**Exact signature**

```python
def _load_yaml(path: Path) -> dict[str, Any]:
```

**Purpose**

Reads and validates yaml; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `dict[str, Any]`.
- Every observed return expression is reproduced without truncation:
```python
content
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(content, dict)`.
- Explicit raise expressions: `TypeError(f'Expected a YAML mapping in {path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.open`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/config.py::load_scan_config` via `_load_yaml`.

**Complete source-ordered implementation**

```python
def _load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        content = yaml.safe_load(stream)
    if not isinstance(content, dict):
        raise TypeError(f"Expected a YAML mapping in {path}")
    return content
```

**Business boundary**

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

### `_resolve_profile_path`

**Exact signature**

```python
def _resolve_profile_path(scan_path: Path, profile_path: Path) -> Path:
```

**Purpose**

Resolves profile path; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
project_root / profile_path

profile_path
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/config.py::load_scan_config` via `_resolve_profile_path`.

**Complete source-ordered implementation**

```python
def _resolve_profile_path(scan_path: Path, profile_path: Path) -> Path:
    if profile_path.is_absolute():
        return profile_path

    resolved_scan_path = scan_path.resolve()
    project_root = resolved_scan_path.parents[2]
    return project_root / profile_path
```

**Business boundary**

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

### `load_scan_config`

**Exact signature**

```python
def load_scan_config(path: Path) -> LoadedScanConfig:
```

**Purpose**

Reads and validates scan config; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `LoadedScanConfig`.
- Every observed return expression is reproduced without truncation:
```python
LoadedScanConfig(scan_config=scan_config, profile=profile, profile_path=profile_path)
```

**Validation and exceptions**

- Guard with a raise path: `not profile_path.is_file()`.
- Explicit raise expressions: `FileNotFoundError(f'Profile file does not exist: {profile_path}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: `profile_path.is_file`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `tests/unit/test_config.py::<module>` via `from landscout.config import load_scan_config`.
- direct call: `tests/unit/test_config.py::_load_temporary_profile` via `load_scan_config`.
- direct call: `tests/unit/test_config.py::test_valid_config_loads` via `load_scan_config`.
- direct call: `tests/unit/test_config.py::test_invalid_commune_code_fails` via `load_scan_config`.
- direct call: `tests/unit/test_config.py::test_negative_minimum_area_fails` via `load_scan_config`.
- direct call: `tests/unit/test_config.py::test_maximum_area_smaller_than_minimum_fails` via `load_scan_config`.
- direct call: `tests/unit/test_config.py::test_missing_profile_fails` via `load_scan_config`.
- direct call: `tests/unit/test_config.py::test_unknown_scan_fields_are_rejected` via `load_scan_config`.
- direct call: `tests/unit/test_config.py::test_canonical_france_commune_codes_are_accepted` via `load_scan_config`.
- direct call: `tests/unit/test_config.py::test_noncanonical_france_commune_codes_are_rejected` via `load_scan_config`.
- direct call: `tests/unit/test_config.py::test_aoi_requires_nonempty_unique_commune_codes` via `load_scan_config`.

**Complete source-ordered implementation**

```python
def load_scan_config(path: Path) -> LoadedScanConfig:
    scan_path = path.resolve()
    scan_config = ScanConfig.model_validate(_load_yaml(scan_path))
    profile_path = _resolve_profile_path(scan_path, scan_config.profile.path)
    if not profile_path.is_file():
        raise FileNotFoundError(f"Profile file does not exist: {profile_path}")

    profile = BessProfile.model_validate(_load_yaml(profile_path))
    return LoadedScanConfig(
        scan_config=scan_config,
        profile=profile,
        profile_path=profile_path,
    )
```

**Business boundary**

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.


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

The module contributes to the project flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
