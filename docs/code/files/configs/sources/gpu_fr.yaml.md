# `configs/sources/gpu_fr.yaml`

## File identity

- Repository path: `configs/sources/gpu_fr.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Pins the official GPU API/cache/pilot identity and logical spatial-layer discovery rules.
- Source SHA256: `f069bf398c752380ca58c90504aa34c322376d52422fd237805e67f2f7829066`

## 1. Purpose

Pins the official GPU API/cache/pilot identity and logical spatial-layer discovery rules.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.sources.gpu_fr.load_gpu_source_config` into `landscout.sources.gpu_fr.GpuSourceConfig`. Runtime consumers include `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `provider` | `"Géoportail de l'Urbanisme"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the configured source provider copied/compared as lineage. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `portal` | `"Géoportail de l'Urbanisme"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `portal` under the exact parent path `<root>`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `country` | `"FR"` | `str` | annotation `Literal['FR']`; required; no inline Field metadata; must agree across scan and referenced profile; current configured identity is France/FR | Configures `country` under the exact parent path `<root>`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `api.base_url` | `"https://www.geoportail-urbanisme.gouv.fr/api"` | `str` | annotation `<class 'pydantic.networks.HttpUrl'>`; required; no inline Field metadata; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Pins the exact official HTTPS API origin/path used to build requests. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `download.strategy` | `"partition"` | `str` | annotation `Literal['partition']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `strategy` under the exact parent path `download`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `download.partition_template` | `"DU_{code_insee}"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `partition template` under the exact parent path `download`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `cache.max_age_hours` | `168` | `int` | annotation `<class 'float'>`; required; Ge(ge=0), _PydanticGeneralMetadata(allow_inf_nan=False); integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `max age hours` under the exact parent path `cache`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `pilot.commune_code` | `"31395"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=None, max_length=None, pattern='^[0-9]{5}$', ascii_only=None); strict canonical French INSEE code: five digits or 2A/2B plus three digits, according to the owning model | Configures `commune code` under the exact parent path `pilot`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.zoning.class_label` | `"Zone urba"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.zoning`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.zoning.match_tokens[0]` | `"zone_urba"` | `str` | annotation `tuple[Annotated[str, StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None)], ...]`; required; MinLen(min_length=1); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.zoning.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_surface.class_label` | `"Prescription surfacique"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.prescription_surface`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_surface.match_tokens[0]` | `"prescription_surf"` | `str` | annotation `tuple[Annotated[str, StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None)], ...]`; required; MinLen(min_length=1); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.prescription_surface.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_line.class_label` | `"Prescription linéaire"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.prescription_line`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_line.match_tokens[0]` | `"prescription_lin"` | `str` | annotation `tuple[Annotated[str, StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None)], ...]`; required; MinLen(min_length=1); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.prescription_line.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_point.class_label` | `"Prescription ponctuelle"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.prescription_point`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_point.match_tokens[0]` | `"prescription_pct"` | `str` | annotation `tuple[Annotated[str, StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None)], ...]`; required; MinLen(min_length=1); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.prescription_point.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_surface.class_label` | `"Information surfacique"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.information_surface`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_surface.match_tokens[0]` | `"info_surf"` | `str` | annotation `tuple[Annotated[str, StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None)], ...]`; required; MinLen(min_length=1); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.information_surface.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_line.class_label` | `"Information linéaire"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.information_line`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_line.match_tokens[0]` | `"info_lin"` | `str` | annotation `tuple[Annotated[str, StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None)], ...]`; required; MinLen(min_length=1); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.information_line.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_point.class_label` | `"Information ponctuelle"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.information_point`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_point.match_tokens[0]` | `"info_pct"` | `str` | annotation `tuple[Annotated[str, StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None)], ...]`; required; MinLen(min_length=1); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.information_point.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |

## 5. Classes / models / dataclasses

Authoritative owning model: `landscout.sources.gpu_fr.GpuSourceConfig`. The checked-in file currently validates as `GpuSourceConfig`.

```python
class GpuApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    base_url: HttpUrl

    @field_validator("base_url")
    @classmethod
    def _official_api(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlparse(str(value))
        if (
            parsed.scheme != "https"
            or parsed.hostname != "www.geoportail-urbanisme.gouv.fr"
            or parsed.port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path.rstrip("/") != "/api"
            or parsed.params
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("GPU API URL must use the exact official HTTPS /api base")
        return value

class GpuDownloadConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    strategy: DownloadStrategy
    partition_template: NonEmptyString

    @field_validator("partition_template")
    @classmethod
    def _valid_partition_template(cls, value: str) -> str:
        if value != value.strip() or value.count("{code_insee}") != 1:
            raise ValueError(
                "partition_template must contain exactly one {code_insee} placeholder"
            )
        try:
            rendered = value.format(code_insee="31395")
        except (KeyError, ValueError) as error:
            raise ValueError("partition_template is malformed") from error
        if not rendered or "/" in rendered or "\\" in rendered:
            raise ValueError("partition_template must render one safe path component")
        return value

class GpuCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    max_age_hours: float = Field(ge=0, allow_inf_nan=False)

class GpuPilotConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commune_code: CommuneCode

class GpuLogicalLayerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    class_label: NonEmptyString
    match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)

    @field_validator("match_tokens")
    @classmethod
    def _unique_tokens(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(value) for value in values)
        if any(not value for value in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(normalized) != len(set(normalized)):
            raise ValueError("Layer match tokens must be unique after normalization")
        return values

class GpuSpatialLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    zoning: GpuLogicalLayerConfig
    prescription_surface: GpuLogicalLayerConfig
    prescription_line: GpuLogicalLayerConfig
    prescription_point: GpuLogicalLayerConfig
    information_surface: GpuLogicalLayerConfig
    information_line: GpuLogicalLayerConfig
    information_point: GpuLogicalLayerConfig

class GpuSourceConfig(BaseModel):
    """Strict configuration for official French GPU ingestion."""

    model_config = ConfigDict(extra="forbid")

    provider: NonEmptyString
    portal: NonEmptyString
    country: Literal["FR"]
    api: GpuApiConfig
    download: GpuDownloadConfig
    cache: GpuCacheConfig
    pilot: GpuPilotConfig
    spatial_layers: GpuSpatialLayersConfig
```

## 6. Functions and methods

Loader: `landscout.sources.gpu_fr.load_gpu_source_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, byte hashing, and cross-field validation.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior.

## 17. Change impact

Any YAML byte/value change requires policy/source review, affected config/result hashes, consumer tests, generated artifacts where applicable, and this companion SHA update.
