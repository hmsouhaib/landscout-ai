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
| `country` | `"FR"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); must agree across scan and referenced profile; current configured identity is France/FR | Configures `country` under the exact parent path `<root>`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `technology` | `"BESS"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); must agree across scan and referenced profile; current configured identity is BESS | Configures `technology` under the exact parent path `<root>`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `parcel.min_area_m2` | `2000` | `int` | annotation `<class 'float'>`; required; BeforeValidator(func=<function _strict_finite_number at 0x00000204E7039080>, json_schema_input_type=PydanticUndefined), Gt(gt=0), _PydanticGeneralMetadata(allow_inf_nan=False); strict non-Boolean finite number; > 0; square metres | Configures min area m2 in square metres. | `landscout.config.load_scan_config via ProfileReference.path` |
| `parcel.max_area_m2` | `15000` | `int` | annotation `<class 'float'>`; required; BeforeValidator(func=<function _strict_finite_number at 0x00000204E7039080>, json_schema_input_type=PydanticUndefined), Gt(gt=0), _PydanticGeneralMetadata(allow_inf_nan=False); strict non-Boolean finite number; > min_area_m2; square metres | Configures max area m2 in square metres. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.enabled` | `true` | `bool` | annotation `<class 'bool'>`; required; Strict(strict=True); strict Boolean model field; when true, all dependent shape-policy fields are required | Enables/disables the exact enabled behavior; Boolean coercion rules belong to the consuming model. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.min_width_m` | `15` | `int` | annotation `Optional[Annotated[float, BeforeValidator(func=<function _strict_finite_number at 0x00000204E7039080>, json_schema_input_type=PydanticUndefined), FieldInfo(annotation=NoneType, required=True, metadata=[Gt(gt=0), _PydanticGeneralMetadata(allow_inf_nan=False)])]]`; default=None; no inline Field metadata; required and > 0 when shape screening is enabled; metres | Configures min width m in metres. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.max_length_width_ratio` | `10` | `int` | annotation `Optional[Annotated[float, BeforeValidator(func=<function _strict_finite_number at 0x00000204E7039080>, json_schema_input_type=PydanticUndefined)]]`; default=None; Ge(ge=1), _PydanticGeneralMetadata(allow_inf_nan=False); required and >= 1 when shape screening is enabled; dimensionless | Configures `max length width ratio` under the exact parent path `shape_screening`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.policy_version` | `"muret_empirical_v1"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `policy version` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.method` | `"empirical_distribution"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `method` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.calibration_scope` | `"Muret 31395"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `calibration scope` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.sample_size` | `4013` | `int` | annotation `<class 'int'>`; required; Strict(strict=True), Gt(gt=0); strict positive integer; Boolean rejected | Configures `sample size` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.calibrated_at` | `"2026-08-11"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `calibrated at` under the exact parent path `shape_screening.calibration`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.target_retention_pct` | `90` | `int` | annotation `<class 'float'>`; required; BeforeValidator(func=<function _strict_finite_number at 0x00000204E7039080>, json_schema_input_type=PydanticUndefined), Gt(gt=0), Le(le=100), _PydanticGeneralMetadata(allow_inf_nan=False); strict finite number in (0, 100] | Configures target retention pct as a percentage. | `landscout.config.load_scan_config via ProfileReference.path` |
| `shape_screening.calibration.observed_retention_pct` | `90.65537` | `float` | annotation `<class 'float'>`; required; BeforeValidator(func=<function _strict_finite_number at 0x00000204E7039080>, json_schema_input_type=PydanticUndefined), Ge(ge=0), Le(le=100), _PydanticGeneralMetadata(allow_inf_nan=False); strict finite number in [0, 100] | Configures observed retention pct as a percentage. | `landscout.config.load_scan_config via ProfileReference.path` |
| `crs.storage` | `"EPSG:4326"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); required exact EPSG:4326 | Configures `storage` under the exact parent path `crs`. | `landscout.config.load_scan_config via ProfileReference.path` |
| `crs.calculation` | `"EPSG:2154"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); required exact EPSG:2154 | Configures `calculation` under the exact parent path `crs`. | `landscout.config.load_scan_config via ProfileReference.path` |

## 5. Classes / models / dataclasses

Authoritative owning model: `landscout.config.BessProfile`. The checked-in file currently validates as `BessProfile`.

```python
class _ConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

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
    commune_codes: list[CommuneCode] = Field(min_length=1)

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
```

## 6. Functions and methods

Loader: `landscout.config.load_scan_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, byte hashing, and cross-field validation.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `landscout.config.load_scan_config via ProfileReference.path`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

## 9. Error handling

The owning Pydantic model rejects extra/missing/unsupported/coerced values according to the exact model/validators above; the loader translates YAML/path/model failures into its documented controlled error.

## 10. Side effects

Network I/O: none. Filesystem read: the loader reads this YAML. Filesystem write: none. Input mutation: none. GIS calculation: none. Hashing: loaders that expose config identity hash these exact bytes.

## 11. Security / trust boundaries

A configured URL/provider/hash is a source lock or provenance input. Physical authority requires the consuming source adapter's safe transport and byte/source revalidation.

## 12. GIS / CRS rules

Only explicit CRS fields impose GIS rules; configured storage/calculation CRS values are policy/configuration, not an implicit reprojection of data.

## 13. Provenance rules

The file's SHA256 binds this exact policy/configuration snapshot. Source identities remain textual until the adapter validates physical bytes/content.

## 14. Business meaning

Thresholds and outcomes are policy/configuration values. They are never relabeled as measured geometry or legal conclusions.

## 15. Explicit non-goals

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior.

## 17. Change impact

Any YAML byte/value change requires policy/source review, affected config/result hashes, consumer tests, generated artifacts where applicable, and this companion SHA update.
