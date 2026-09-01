# `configs/profiles/bess_default_fr.yaml`

## File identity

- Repository path: `configs/profiles/bess_default_fr.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Defines the default French BESS parcel-area and shape-screening profile consumed by scan configuration.
- Source SHA256: `5126d21c94cc399f9318f988b6ba9b7a07d24006e542861e167c08c9ace39684`

## 1. Purpose

Defines the default French BESS parcel-area and shape-screening profile consumed by scan configuration.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.config.load_scan_config` into `landscout.config.BessProfile`. Runtime consumers include `landscout.config.load_scan_config via ProfileReference.path`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `country` | `"FR"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; must agree across scan and referenced profile; current configured identity is France/FR | Configures `country` under the exact parent path `<root>`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `technology` | `"BESS"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; must agree across scan and referenced profile; current configured identity is BESS | Configures `technology` under the exact parent path `<root>`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `parcel.min_area_m2` | `2000` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; parsed as float only after `_strict_finite_number`; Boolean rejected; must be finite and > 0; unit m² | Configures min area m2 in square metres. | `landscout.config.load_scan_config via ProfileReference.path` |
| `parcel.max_area_m2` | `15000` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; parsed as float only after `_strict_finite_number`; Boolean rejected; must be finite, > 0, and > min_area_m2; unit m² | Configures max area m2 in square metres. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.enabled` | `true` | `bool` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; strict Boolean model field; when true, all dependent shape-policy fields are required | Enables/disables the exact enabled behavior; Boolean coercion rules belong to the consuming model. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.min_width_m` | `15` | `int` | source-declared default is true null; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required and > 0 when shape screening is enabled; metres | Configures min width m in metres. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.max_length_width_ratio` | `10` | `int` | source-declared default is true null; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required and >= 1 when shape screening is enabled; dimensionless | Configures `max length width ratio` under the exact parent path `shape_screening`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.policy_version` | `"muret_empirical_v1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `policy version` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.method` | `"empirical_distribution"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `method` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.calibration_scope` | `"Muret 31395"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `calibration scope` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.sample_size` | `4013` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; strict positive integer; Boolean rejected | Configures `sample size` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.calibrated_at` | `"2026-08-11"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `calibrated at` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.target_retention_pct` | `90` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; strict finite number in (0, 100] | Configures target retention pct as a percentage. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.observed_retention_pct` | `90.65537` | `float` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; strict finite number in [0, 100] | Configures observed retention pct as a percentage. | `landscout.config.load_scan_config via ProfileReference.path` |
| `crs.storage` | `"EPSG:4326"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required exact EPSG:4326 | Configures `storage` under the exact parent path `crs`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `crs.calculation` | `"EPSG:2154"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required exact EPSG:2154 | Configures `calculation` under the exact parent path `crs`. | `landscout.config.load_scan_config via ProfileReference.path` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.config.load_scan_config (through ProfileReference.path)`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `5126d21c94cc399f9318f988b6ba9b7a07d24006e542861e167c08c9ace39684`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.config.load_scan_config (through ProfileReference.path)`.
- Owning Python module: `landscout.config`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

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

## 6. Functions and methods

Loader: `landscout.config.load_scan_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `landscout.config.load_scan_config via ProfileReference.path`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

## 9. Error handling

The owning Pydantic model rejects extra/missing/unsupported/coerced values according to the exact model/validators above; the loader translates YAML/path/model failures into its documented controlled error.

## 10. Side effects

Network I/O: none. Filesystem read: the loader reads this YAML. Filesystem write: none. Input mutation: none. GIS calculation: none. Hashing: none; this loader parses/validates configuration values but does not hash this file's bytes.

## 11. Security / trust boundaries

A configured URL/provider/hash is a source lock or provenance input. Physical authority requires the consuming source adapter's safe transport and byte/source revalidation.

## 12. GIS / CRS rules

Only explicit CRS fields impose GIS rules; configured storage/calculation CRS values are policy/configuration, not an implicit reprojection of data.

## 13. Provenance rules

The companion's Source SHA256 binds this checked-in file for documentation fidelity; that documentation digest is not attributed to the runtime loader. Source identities remain textual until the adapter validates physical bytes/content.

## 14. Business meaning

Thresholds and outcomes are policy/configuration values. They are never relabeled as measured geometry or legal conclusions.

## 15. Explicit non-goals

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior only where the runtime source actually computes a hash.

## 17. Change impact

Any YAML byte/value change requires policy/source review, consumer tests, generated artifacts where applicable, this companion SHA update, and only those runtime hashes whose documented algorithm actually includes these bytes or validated values.

## 18. Complete readable configuration and authoritative raw-byte snapshot

### Complete readable YAML

The following is the complete decoded UTF-8 configuration with line endings normalized to LF for stable Markdown display. Every character and logical line is present, but this readable fence is not the authority for original CR/LF byte positions.

```yaml
country: FR
technology: BESS

parcel:
  min_area_m2: 2000
  max_area_m2: 15000

shape_screening:
  enabled: true
  min_width_m: 15
  max_length_width_ratio: 10
  calibration:
    policy_version: "muret_empirical_v1"
    method: "empirical_distribution"
    calibration_scope: "Muret 31395"
    sample_size: 4013
    calibrated_at: "2026-08-11"
    target_retention_pct: 90
    observed_retention_pct: 90.655370

crs:
  storage: EPSG:4326
  calculation: EPSG:2154
```

### Authoritative raw-byte payload

- Raw byte length: `463`.
- Raw SHA256: `5126d21c94cc399f9318f988b6ba9b7a07d24006e542861e167c08c9ace39684` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
Y291bnRyeTogRlIKdGVjaG5vbG9neTogQkVTUwoKcGFyY2VsOgogIG1pbl9hcmVhX20yOiAyMDAw
CiAgbWF4X2FyZWFfbTI6IDE1MDAwCgpzaGFwZV9zY3JlZW5pbmc6CiAgZW5hYmxlZDogdHJ1ZQog
IG1pbl93aWR0aF9tOiAxNQogIG1heF9sZW5ndGhfd2lkdGhfcmF0aW86IDEwCiAgY2FsaWJyYXRp
b246CiAgICBwb2xpY3lfdmVyc2lvbjogIm11cmV0X2VtcGlyaWNhbF92MSIKICAgIG1ldGhvZDog
ImVtcGlyaWNhbF9kaXN0cmlidXRpb24iCiAgICBjYWxpYnJhdGlvbl9zY29wZTogIk11cmV0IDMx
Mzk1IgogICAgc2FtcGxlX3NpemU6IDQwMTMKICAgIGNhbGlicmF0ZWRfYXQ6ICIyMDI2LTA4LTEx
IgogICAgdGFyZ2V0X3JldGVudGlvbl9wY3Q6IDkwCiAgICBvYnNlcnZlZF9yZXRlbnRpb25fcGN0
OiA5MC42NTUzNzAKCmNyczoKICBzdG9yYWdlOiBFUFNHOjQzMjYKICBjYWxjdWxhdGlvbjogRVBT
RzoyMTU0Cg==
```
