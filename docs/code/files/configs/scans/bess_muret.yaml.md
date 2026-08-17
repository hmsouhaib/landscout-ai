# `configs/scans/bess_muret.yaml`

## File identity

- Repository path: `configs/scans/bess_muret.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Defines the Muret scan identity, AOI, profile reference, and output root.
- Source SHA256: `6da68dfa5442b7b856687d5c9d5b0db10a2a2f799a2d7b8b35342573d54c65ba`

## 1. Purpose

Defines the Muret scan identity, AOI, profile reference, and output root.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.config.load_scan_config` into `landscout.config.ScanConfig`. Runtime consumers include `landscout.config.load_scan_config`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `scan.name` | `"bess_muret"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `name` under the exact parent path `scan`. | `landscout.config.load_scan_config` |
| `scan.country` | `"FR"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; must agree across scan and referenced profile; current configured identity is France/FR | Configures `country` under the exact parent path `scan`. | `landscout.config.load_scan_config` |
| `scan.technology` | `"BESS"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; must agree across scan and referenced profile; current configured identity is BESS | Configures `technology` under the exact parent path `scan`. | `landscout.config.load_scan_config` |
| `aoi.commune_codes[0]` | `"31395"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; non-empty ordered collection of unique canonical commune codes | Ordered configured member of `aoi.commune_codes`; order and uniqueness are validated/consumed where required. | `landscout.config.load_scan_config` |
| `profile.path` | `"configs/profiles/bess_default_fr.yaml"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `path` under the exact parent path `profile`. | `landscout.config.load_scan_config` |
| `output.directory` | `"outputs"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `directory` under the exact parent path `output`. | `landscout.config.load_scan_config` |

## 5. Classes / models / dataclasses

Authoritative owning model: `landscout.config.ScanConfig`. The checked-in file currently validates as `LoadedScanConfig`.

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

Loader: `landscout.config.load_scan_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `landscout.config.load_scan_config`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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
