# `src/landscout/config.py`

## File identity

- Repository path: `src/landscout/config.py`
- File type: Python source
- Layer: configuration boundary
- Domain: scan/profile configuration
- Responsibility: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.
- Source SHA256: `e598e0d9a849856eb005b5f4876ce4f61de6428759159e0561c2f60f46e0d0c0`

## 1. STEP 7F.1A.4 contract delta

- Moves scan/profile YAML to strict duplicate-safe decoding, freezes decision-input models, converts nested collections to immutable values, and reconstructs models at public boundaries.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

The file belongs to the **configuration boundary** layer and **scan/profile configuration** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from math import isfinite`
- `from numbers import Real`
- `from pathlib import Path`
- `from typing import Annotated, Any`

### Third-party packages

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

- `from landscout.common.strict_yaml import loads_strict_yaml`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `NonEmptyString`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CommuneCode`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
CommuneCode = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^(?:\d{5}|2[AB]\d{3})$"),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `StrictFiniteFloat`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
StrictFiniteFloat = Annotated[float, BeforeValidator(_strict_finite_number)]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `StrictPositiveFloat`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
StrictPositiveFloat = Annotated[
    float,
    BeforeValidator(_strict_finite_number),
    Field(gt=0, allow_inf_nan=False),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `StrictPositiveInt`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `_ConfigModel`

**Source purpose:** Defines `_ConfigModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _ConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `ParcelConfig`

**Source purpose:** Defines `ParcelConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `min_area_m2` | `StrictPositiveFloat` | `required` | `min_area_m2: StrictPositiveFloat` |
| `max_area_m2` | `StrictPositiveFloat` | `required` | `max_area_m2: StrictPositiveFloat` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- import: `landscout.stages.filter_parcels::<module>` via `from landscout.config import ParcelConfig, ShapeScreeningConfig`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_area` via `ParcelConfig`
- import: `tests.unit.test_filter_parcels::<module>` via `from landscout.config import ParcelConfig`
- constructor call: `tests.unit.test_filter_parcels::area_config` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::area_config` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_minimum_boundary_is_included` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_maximum_boundary_is_included` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_rejected_parcel_has_expected_reason` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_no_parcel_disappears` via `ParcelConfig`
- constructor call: `tests.unit.test_filter_parcels::test_thresholds_come_from_config` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_thresholds_come_from_config` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_revalidates_mutated_config_before_frame_work` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_missing_parcel_id_fails` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_null_parcel_id_fails` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_duplicate_parcel_id_fails` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_candidate_and_rejected_ids_do_not_overlap` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_exact_parcel_ids_are_preserved` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_requires_strict_positive_finite_area` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_with_forged_positive_area_is_rejected` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_invalid_geometry_with_recorded_area_is_rejected` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_parcel_id_must_match_its_canonical_source_identity_fields` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_requires_exact_non_empty_parcel_ids` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_plain_dataframe` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_duplicate_columns` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_malformed_spatial_envelope` via `ParcelConfig`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_noncanonical_geometry_status` via `ParcelConfig`

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

**Source purpose:** Defines `ShapeCalibrationConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `policy_version` | `NonEmptyString` | `required` | `policy_version: NonEmptyString` |
| `method` | `NonEmptyString` | `required` | `method: NonEmptyString` |
| `calibration_scope` | `NonEmptyString` | `required` | `calibration_scope: NonEmptyString` |
| `sample_size` | `StrictPositiveInt` | `required` | `sample_size: StrictPositiveInt` |
| `calibrated_at` | `NonEmptyString` | `required` | `calibrated_at: NonEmptyString` |
| `target_retention_pct` | `Annotated[StrictFiniteFloat, Field(gt=0, le=100, allow_inf_nan=False)]` | `required` | `target_retention_pct: Annotated[<br>        StrictFiniteFloat, Field(gt=0, le=100, allow_inf_nan=False)<br>    ]` |
| `observed_retention_pct` | `Annotated[StrictFiniteFloat, Field(ge=0, le=100, allow_inf_nan=False)]` | `required` | `observed_retention_pct: Annotated[<br>        StrictFiniteFloat, Field(ge=0, le=100, allow_inf_nan=False)<br>    ]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- import: `tests.unit.test_filter_shape::<module>` via `from landscout.config import ShapeCalibrationConfig, ShapeScreeningConfig`
- constructor call: `tests.unit.test_filter_shape::_shape_config` via `ShapeCalibrationConfig`
- value/type reference: `tests.unit.test_filter_shape::_shape_config` via `ShapeCalibrationConfig`

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

**Source purpose:** Defines `ShapeScreeningConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `enabled` | `StrictBool` | `required` | `enabled: StrictBool` |
| `min_width_m` | `StrictPositiveFloat \| None` | `None` | `min_width_m: StrictPositiveFloat \| None = None` |
| `max_length_width_ratio` | `StrictFiniteFloat \| None` | `Field(<br>        default=None, ge=1, allow_inf_nan=False<br>    )` | `max_length_width_ratio: StrictFiniteFloat \| None = Field(<br>        default=None, ge=1, allow_inf_nan=False<br>    )` |
| `calibration` | `ShapeCalibrationConfig \| None` | `None` | `calibration: ShapeCalibrationConfig \| None = None` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- import: `landscout.stages.filter_parcels::<module>` via `from landscout.config import ParcelConfig, ShapeScreeningConfig`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_shape` via `ShapeScreeningConfig`
- import: `tests.unit.test_filter_shape::<module>` via `from landscout.config import ShapeCalibrationConfig, ShapeScreeningConfig`
- constructor call: `tests.unit.test_filter_shape::_shape_config` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::_shape_config` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::shape_config` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_exact_width_and_ratio_boundaries_are_retained` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_revalidates_mutated_config_before_frame_work` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_rejected_parcel_has_expected_primary_reason` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_rejection_reason_precedence_is_deterministic` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_shape_error_precedence_does_not_inspect_metrics` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_enabled_outputs_record_active_policy_metadata` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_enabled_partition_preserves_exact_ids_and_crs` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_filter_does_not_mutate_input` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_missing_required_column_fails` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_null_parcel_id_fails` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_duplicate_parcel_id_fails` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_unknown_crs_fails` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_unexpected_or_null_shape_status_fails` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_non_finite_known_metric_on_valid_row_fails` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_strict_positive_width` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_ratio_at_least_one` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_negative_ratio_cannot_pass_permissive_thresholds` via `ShapeScreeningConfig`
- constructor call: `tests.unit.test_filter_shape::test_disabled_policy_is_an_exact_passthrough` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_disabled_policy_is_an_exact_passthrough` via `ShapeScreeningConfig`
- constructor call: `tests.unit.test_filter_shape::test_valid_shape_requires_complete_metrics_even_when_screening_disabled` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_complete_metrics_even_when_screening_disabled` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_rejects_every_incomplete_metric_form` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_plain_dataframe` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_duplicate_columns` via `ShapeScreeningConfig`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_unreadable_crs` via `ShapeScreeningConfig`

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

**Source purpose:** Defines `CrsConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `storage` | `NonEmptyString` | `required` | `storage: NonEmptyString` |
| `calculation` | `NonEmptyString` | `required` | `calculation: NonEmptyString` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

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

**Source purpose:** Defines `BessProfile`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `country` | `NonEmptyString` | `required` | `country: NonEmptyString` |
| `technology` | `NonEmptyString` | `required` | `technology: NonEmptyString` |
| `parcel` | `ParcelConfig` | `required` | `parcel: ParcelConfig` |
| `shape_screening` | `ShapeScreeningConfig` | `required` | `shape_screening: ShapeScreeningConfig` |
| `crs` | `CrsConfig` | `required` | `crs: CrsConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.config::load_scan_config` via `BessProfile`

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

**Source purpose:** Defines `ScanMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `name` | `NonEmptyString` | `required` | `name: NonEmptyString` |
| `country` | `NonEmptyString` | `required` | `country: NonEmptyString` |
| `technology` | `NonEmptyString` | `required` | `technology: NonEmptyString` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class ScanMetadata(_ConfigModel):
    name: NonEmptyString
    country: NonEmptyString
    technology: NonEmptyString
```

### `AoiConfig`

**Source purpose:** Defines `AoiConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `commune_codes` | `tuple[CommuneCode, ...]` | `Field(min_length=1)` | `commune_codes: tuple[CommuneCode, ...] = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class AoiConfig(_ConfigModel):
    commune_codes: tuple[CommuneCode, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_unique_communes(self) -> "AoiConfig":
        if len(set(self.commune_codes)) != len(self.commune_codes):
            raise ValueError("commune_codes must not contain duplicates")
        return self
```

### `ProfileReference`

**Source purpose:** Defines `ProfileReference`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `path` | `Path` | `required` | `path: Path` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class ProfileReference(_ConfigModel):
    path: Path
```

### `OutputConfig`

**Source purpose:** Defines `OutputConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `directory` | `Path` | `required` | `directory: Path` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class OutputConfig(_ConfigModel):
    directory: Path
```

### `ScanConfig`

**Source purpose:** Defines `ScanConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `scan` | `ScanMetadata` | `required` | `scan: ScanMetadata` |
| `aoi` | `AoiConfig` | `required` | `aoi: AoiConfig` |
| `profile` | `ProfileReference` | `required` | `profile: ProfileReference` |
| `output` | `OutputConfig` | `required` | `output: OutputConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.config::load_scan_config` via `ScanConfig`

**Exact class source**

```python
class ScanConfig(_ConfigModel):
    scan: ScanMetadata
    aoi: AoiConfig
    profile: ProfileReference
    output: OutputConfig
```

### `LoadedScanConfig`

**Source purpose:** Defines `LoadedScanConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_ConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `scan_config` | `ScanConfig` | `required` | `scan_config: ScanConfig` |
| `profile` | `BessProfile` | `required` | `profile: BessProfile` |
| `profile_path` | `Path` | `required` | `profile_path: Path` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.config::load_scan_config` via `LoadedScanConfig`
- value/type reference: `landscout.config::load_scan_config` via `LoadedScanConfig`

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


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_strict_finite_number`

**Purpose:** Implements `strict finite number` within the file role: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

**Exact signature**

```python
def _strict_finite_number(value: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `PydanticCustomError(<br>            "strict_number",<br>            "value must be a strict YAML number",<br>        )` under lexical guard `isinstance(value, bool) or not isinstance(value, Real)`.
  - `ValueError("value must be finite")` under lexical guard `not isfinite(float(value))`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PydanticCustomError` | `pydantic_core.PydanticCustomError` |
| `isfinite` | `math.isfinite` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `ParcelConfig.validate_area_range`

**Purpose:** Implements `validate area range` within the file role: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

**Exact signature**

```python
def validate_area_range(self) -> "ParcelConfig":
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `'ParcelConfig'`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("max_area_m2 must be greater than min_area_m2")` under lexical guard `self.max_area_m2 <= self.min_area_m2`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
def validate_area_range(self) -> "ParcelConfig":
        if self.max_area_m2 <= self.min_area_m2:
            raise ValueError("max_area_m2 must be greater than min_area_m2")
        return self
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `ShapeScreeningConfig.validate_enabled_policy`

**Purpose:** Implements `validate enabled policy` within the file role: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

**Exact signature**

```python
def validate_enabled_policy(self) -> "ShapeScreeningConfig":
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `'ShapeScreeningConfig'`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(f"enabled shape screening requires: {formatted}")` under lexical guard `missing`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `required_values.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `CrsConfig.validate_crs_contract`

**Purpose:** Implements `validate crs contract` within the file role: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

**Exact signature**

```python
def validate_crs_contract(self) -> "CrsConfig":
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `'CrsConfig'`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(f"{field} CRS is unreadable")`.
  - `ValueError(f"{field} CRS must be EPSG:{expected}")` under lexical guard `not observed.equals(CRS.from_epsg(expected))`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `observed.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `model_validator` | `pydantic.model_validator` |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `AoiConfig.validate_unique_communes`

**Purpose:** Implements `validate unique communes` within the file role: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

**Exact signature**

```python
def validate_unique_communes(self) -> "AoiConfig":
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `'AoiConfig'`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("commune_codes must not contain duplicates")` under lexical guard `len(set(self.commune_codes)) != len(self.commune_codes)`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
def validate_unique_communes(self) -> "AoiConfig":
        if len(set(self.commune_codes)) != len(self.commune_codes):
            raise ValueError("commune_codes must not contain duplicates")
        return self
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `LoadedScanConfig.validate_scan_profile_identity`

**Purpose:** Implements `validate scan profile identity` within the file role: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

**Exact signature**

```python
def validate_scan_profile_identity(self) -> "LoadedScanConfig":
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `'LoadedScanConfig'`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("scan country must equal profile country")` under lexical guard `self.scan_config.scan.country != self.profile.country`.
  - `ValueError("scan technology must equal profile technology")` under lexical guard `self.scan_config.scan.technology != self.profile.technology`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
def validate_scan_profile_identity(self) -> "LoadedScanConfig":
        if self.scan_config.scan.country != self.profile.country:
            raise ValueError("scan country must equal profile country")
        if self.scan_config.scan.technology != self.profile.technology:
            raise ValueError("scan technology must equal profile technology")
        return self
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_load_yaml`

**Purpose:** Implements `load yaml` within the file role: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

**Exact signature**

```python
def _load_yaml(path: Path) -> dict[str, Any]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, Any]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `content`
- Explicit raise paths:
  - `TypeError(f"Expected a YAML mapping in {path}")` under lexical guard `type(content) is not dict`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.config::load_scan_config` via `_load_yaml`
- value/type reference: `landscout.config::load_scan_config` via `_load_yaml`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _load_yaml(path: Path) -> dict[str, Any]:
    content = loads_strict_yaml(path.read_bytes())
    if type(content) is not dict:
        raise TypeError(f"Expected a YAML mapping in {path}")
    return content
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_resolve_profile_path`

**Purpose:** Implements `resolve profile path` within the file role: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

**Exact signature**

```python
def _resolve_profile_path(scan_path: Path, profile_path: Path) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `scan_path` | positional-or-keyword | `Path` | `required` |
| `profile_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `profile_path`
  - `project_root / profile_path`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.config::load_scan_config` via `_resolve_profile_path`
- value/type reference: `landscout.config::load_scan_config` via `_resolve_profile_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_path.is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `scan_path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _resolve_profile_path(scan_path: Path, profile_path: Path) -> Path:
    if profile_path.is_absolute():
        return profile_path

    resolved_scan_path = scan_path.resolve()
    project_root = resolved_scan_path.parents[2]
    return project_root / profile_path
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `load_scan_config`

**Purpose:** Implements `load scan config` within the file role: Strictly loads duplicate-safe, frozen/deeply immutable scan, profile, parcel, CRS, shape-screening, AOI, and output configuration.

**Exact signature**

```python
def load_scan_config(path: Path) -> LoadedScanConfig:
```

- Exact decorators: none.
- Declared return annotation: `LoadedScanConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `LoadedScanConfig(<br>        scan_config=scan_config,<br>        profile=profile,<br>        profile_path=profile_path,<br>    )`
- Explicit raise paths:
  - `FileNotFoundError(f"Profile file does not exist: {profile_path}")` under lexical guard `not profile_path.is_file()`.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `tests.unit.test_config::<module>` via `from landscout.config import load_scan_config`
- direct call: `tests.unit.test_config::_load_temporary_profile` via `load_scan_config`
- value/type reference: `tests.unit.test_config::_load_temporary_profile` via `load_scan_config`
- direct call: `tests.unit.test_config::test_valid_config_loads` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_valid_config_loads` via `load_scan_config`
- direct call: `tests.unit.test_config::test_loaded_scan_and_profile_models_are_immutable` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_loaded_scan_and_profile_models_are_immutable` via `load_scan_config`
- direct call: `tests.unit.test_config::test_invalid_commune_code_fails` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_invalid_commune_code_fails` via `load_scan_config`
- direct call: `tests.unit.test_config::test_negative_minimum_area_fails` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_negative_minimum_area_fails` via `load_scan_config`
- direct call: `tests.unit.test_config::test_maximum_area_smaller_than_minimum_fails` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_maximum_area_smaller_than_minimum_fails` via `load_scan_config`
- direct call: `tests.unit.test_config::test_missing_profile_fails` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_missing_profile_fails` via `load_scan_config`
- direct call: `tests.unit.test_config::test_unknown_scan_fields_are_rejected` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_unknown_scan_fields_are_rejected` via `load_scan_config`
- direct call: `tests.unit.test_config::test_canonical_france_commune_codes_are_accepted` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_canonical_france_commune_codes_are_accepted` via `load_scan_config`
- direct call: `tests.unit.test_config::test_noncanonical_france_commune_codes_are_rejected` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_noncanonical_france_commune_codes_are_rejected` via `load_scan_config`
- direct call: `tests.unit.test_config::test_aoi_requires_nonempty_unique_commune_codes` via `load_scan_config`
- value/type reference: `tests.unit.test_config::test_aoi_requires_nonempty_unique_commune_codes` via `load_scan_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `ScanConfig.model_validate` | `landscout.config.ScanConfig.model_validate` |
| `_load_yaml` | `landscout.config._load_yaml` |
| `_resolve_profile_path` | `landscout.config._resolve_profile_path` |
| `profile_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `FileNotFoundError` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessProfile.model_validate` | `landscout.config.BessProfile.model_validate` |
| `LoadedScanConfig` | `landscout.config.LoadedScanConfig` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `profile_path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: none at module scope.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from math import isfinite
from numbers import Real
from pathlib import Path
from typing import Annotated, Any

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    StrictBool,
    StringConstraints,
    model_validator,
)
from pydantic_core import PydanticCustomError
from pyproj import CRS

from landscout.common.strict_yaml import loads_strict_yaml

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
CommuneCode = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^(?:\d{5}|2[AB]\d{3})$"),
]


def _strict_finite_number(value: object) -> object:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise PydanticCustomError(
            "strict_number",
            "value must be a strict YAML number",
        )
    if not isfinite(float(value)):
        raise ValueError("value must be finite")
    return value


StrictFiniteFloat = Annotated[float, BeforeValidator(_strict_finite_number)]
StrictPositiveFloat = Annotated[
    float,
    BeforeValidator(_strict_finite_number),
    Field(gt=0, allow_inf_nan=False),
]
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]


class _ConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class ParcelConfig(_ConfigModel):
    min_area_m2: StrictPositiveFloat
    max_area_m2: StrictPositiveFloat

    @model_validator(mode="after")
    def validate_area_range(self) -> "ParcelConfig":
        if self.max_area_m2 <= self.min_area_m2:
            raise ValueError("max_area_m2 must be greater than min_area_m2")
        return self


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


class BessProfile(_ConfigModel):
    country: NonEmptyString
    technology: NonEmptyString
    parcel: ParcelConfig
    shape_screening: ShapeScreeningConfig
    crs: CrsConfig


class ScanMetadata(_ConfigModel):
    name: NonEmptyString
    country: NonEmptyString
    technology: NonEmptyString


class AoiConfig(_ConfigModel):
    commune_codes: tuple[CommuneCode, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_unique_communes(self) -> "AoiConfig":
        if len(set(self.commune_codes)) != len(self.commune_codes):
            raise ValueError("commune_codes must not contain duplicates")
        return self


class ProfileReference(_ConfigModel):
    path: Path


class OutputConfig(_ConfigModel):
    directory: Path


class ScanConfig(_ConfigModel):
    scan: ScanMetadata
    aoi: AoiConfig
    profile: ProfileReference
    output: OutputConfig


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


def _load_yaml(path: Path) -> dict[str, Any]:
    content = loads_strict_yaml(path.read_bytes())
    if type(content) is not dict:
        raise TypeError(f"Expected a YAML mapping in {path}")
    return content


def _resolve_profile_path(scan_path: Path, profile_path: Path) -> Path:
    if profile_path.is_absolute():
        return profile_path

    resolved_scan_path = scan_path.resolve()
    project_root = resolved_scan_path.parents[2]
    return project_root / profile_path


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
