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
| `profile.path` | `"configs/profiles/bess_default_fr.yaml"` | `Path` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `path` under the exact parent path `profile`. | `landscout.config.load_scan_config` |
| `output.directory` | `"outputs"` | `Path` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `directory` under the exact parent path `output`. | `landscout.config.load_scan_config` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.config.load_scan_config`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## Runtime interpretation reviewed for DOCS.CONTINUITY.1

`aoi.commune_codes` becomes the ordered immutable tuple `('31395',)` after validation. `profile.path` and `output.directory` become Path values; only the profile file is resolved/read here. Loading does not create `outputs`, run a scan, fetch communes, or prove a commune exists.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `6da68dfa5442b7b856687d5c9d5b0db10a2a2f799a2d7b8b35342573d54c65ba`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.config.load_scan_config`.
- Owning Python module: `landscout.config`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

### `_ConfigModel`

**Source purpose:** Shared Pydantic base: reject undeclared fields and ordinary attribute reassignment. Deep immutability additionally comes from nested frozen models and the AOI tuple, not from `frozen=True` alone.

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

### `ScanMetadata`

**Source purpose:** Required nonempty trimmed `name`, `country`, and `technology` labels. A name identifies the scan; the remaining labels must match the selected profile when a `LoadedScanConfig` is built. No scheduling or scan execution is implemented here.

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

**Source purpose:** Nonempty, duplicate-free ordered tuple of strictly string-valued commune codes matching the declared French identifier pattern. YAML sequences become tuples without sorting or stripping individual codes, so no mutable input-list alias remains.

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

**Source purpose:** Required filesystem `Path` reference to the profile. Pydantic accepts path-like input; the loader, not this model, resolves relative paths and checks file existence.

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

**Source purpose:** Required output-directory `Path` declaration. Loading does not resolve it, create the directory, check writability, or export any artifact.

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

**Source purpose:** Required nested `scan`, `aoi`, `profile`, and `output` declarations. The envelope is configuration, not an orchestrated pipeline or proof that all referenced communes have been downloaded.

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

**Source purpose:** Retains the validated `scan_config`, loaded `profile`, and selected `profile_path`; rejects mismatched country or technology. No source-config object or deterministic configuration hash is created by this loader.

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

## 6. Functions and methods

Loader: `landscout.config.load_scan_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `landscout.config.load_scan_config`. Scan loading resolves `ProfileReference.path` relative to the assumed repository root three ancestors above the scan file. This file does not call the road policy loader.

## 9. Error handling

The owning Pydantic model rejects extra/missing/unsupported/coerced values according to the exact model/validators above; this loader propagates filesystem errors, strict YAML errors and Pydantic ValidationError without a single source-adapter wrapper.

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
scan:
  name: bess_muret
  country: FR
  technology: BESS

aoi:
  commune_codes:
    - "31395"

profile:
  path: configs/profiles/bess_default_fr.yaml

output:
  directory: outputs
```

### Authoritative raw-byte payload

- Raw byte length: `181`.
- Raw SHA256: `6da68dfa5442b7b856687d5c9d5b0db10a2a2f799a2d7b8b35342573d54c65ba` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
c2NhbjoKICBuYW1lOiBiZXNzX211cmV0CiAgY291bnRyeTogRlIKICB0ZWNobm9sb2d5OiBCRVNT
Cgphb2k6CiAgY29tbXVuZV9jb2RlczoKICAgIC0gIjMxMzk1IgoKcHJvZmlsZToKICBwYXRoOiBj
b25maWdzL3Byb2ZpbGVzL2Jlc3NfZGVmYXVsdF9mci55YW1sCgpvdXRwdXQ6CiAgZGlyZWN0b3J5
OiBvdXRwdXRzCg==
```
