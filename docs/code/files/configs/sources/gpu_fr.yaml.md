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
| `provider` | `"Géoportail de l'Urbanisme"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the configured source provider copied/compared as lineage. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `portal` | `"Géoportail de l'Urbanisme"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `portal` under the exact parent path `<root>`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `country` | `"FR"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; must agree across scan and referenced profile; current configured identity is France/FR | Configures `country` under the exact parent path `<root>`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `api.base_url` | `"https://www.geoportail-urbanisme.gouv.fr/api"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Pins the exact official HTTPS API origin/path used to build requests. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `download.strategy` | `"partition"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `strategy` under the exact parent path `download`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `download.partition_template` | `"DU_{code_insee}"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `partition template` under the exact parent path `download`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `cache.max_age_hours` | `168` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `max age hours` under the exact parent path `cache`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `pilot.commune_code` | `"31395"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; strict canonical French INSEE code: five digits or 2A/2B plus three digits, according to the owning model | Configures `commune code` under the exact parent path `pilot`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.zoning.class_label` | `"Zone urba"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.zoning`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.zoning.match_tokens[0]` | `"zone_urba"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.zoning.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_surface.class_label` | `"Prescription surfacique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.prescription_surface`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_surface.match_tokens[0]` | `"prescription_surf"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.prescription_surface.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_line.class_label` | `"Prescription linéaire"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.prescription_line`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_line.match_tokens[0]` | `"prescription_lin"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.prescription_line.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_point.class_label` | `"Prescription ponctuelle"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.prescription_point`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.prescription_point.match_tokens[0]` | `"prescription_pct"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.prescription_point.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_surface.class_label` | `"Information surfacique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.information_surface`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_surface.match_tokens[0]` | `"info_surf"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.information_surface.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_line.class_label` | `"Information linéaire"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.information_line`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_line.match_tokens[0]` | `"info_lin"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.information_line.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_point.class_label` | `"Information ponctuelle"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `spatial_layers.information_point`. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |
| `spatial_layers.information_point.match_tokens[0]` | `"info_pct"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `spatial_layers.information_point.match_tokens`; order and uniqueness are validated/consumed where required. | `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.sources.gpu_fr.load_gpu_source_config`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `f069bf398c752380ca58c90504aa34c322376d52422fd237805e67f2f7829066`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.sources.gpu_fr.load_gpu_source_config`.
- Owning Python module: `landscout.sources.gpu_fr`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

### `GpuApiConfig`

**Source purpose:** Defines `GpuApiConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `base_url` | `HttpUrl` | `required` | `base_url: HttpUrl` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class GpuApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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
```

### `GpuDownloadConfig`

**Source purpose:** Defines `GpuDownloadConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `strategy` | `DownloadStrategy` | `required` | `strategy: DownloadStrategy` |
| `partition_template` | `NonEmptyString` | `required` | `partition_template: NonEmptyString` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class GpuDownloadConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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
```

### `GpuCacheConfig`

**Source purpose:** Defines `GpuCacheConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `max_age_hours` | `float` | `Field(ge=0, allow_inf_nan=False)` | `max_age_hours: float = Field(ge=0, allow_inf_nan=False)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class GpuCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    max_age_hours: float = Field(ge=0, allow_inf_nan=False)

    @field_validator("max_age_hours", mode="before")
    @classmethod
    def _strict_finite_number(cls, value: object) -> object:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or type(value) not in {int, float}
        ):
            raise ValueError("max_age_hours must be an exact finite number")
        if not math.isfinite(value):
            raise ValueError("max_age_hours must be finite")
        return value
```

### `GpuPilotConfig`

**Source purpose:** Defines `GpuPilotConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `commune_code` | `CommuneCode` | `required` | `commune_code: CommuneCode` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class GpuPilotConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    commune_code: CommuneCode
```

### `GpuLogicalLayerConfig`

**Source purpose:** Defines `GpuLogicalLayerConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `class_label` | `NonEmptyString` | `required` | `class_label: NonEmptyString` |
| `match_tokens` | `tuple[NonEmptyString, ...]` | `Field(min_length=1)` | `match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.sources.gpu_fr::_layer_config` via `GpuLogicalLayerConfig`

**Exact class source**

```python
class GpuLogicalLayerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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
```

### `GpuSpatialLayersConfig`

**Source purpose:** Defines `GpuSpatialLayersConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `zoning` | `GpuLogicalLayerConfig` | `required` | `zoning: GpuLogicalLayerConfig` |
| `prescription_surface` | `GpuLogicalLayerConfig` | `required` | `prescription_surface: GpuLogicalLayerConfig` |
| `prescription_line` | `GpuLogicalLayerConfig` | `required` | `prescription_line: GpuLogicalLayerConfig` |
| `prescription_point` | `GpuLogicalLayerConfig` | `required` | `prescription_point: GpuLogicalLayerConfig` |
| `information_surface` | `GpuLogicalLayerConfig` | `required` | `information_surface: GpuLogicalLayerConfig` |
| `information_line` | `GpuLogicalLayerConfig` | `required` | `information_line: GpuLogicalLayerConfig` |
| `information_point` | `GpuLogicalLayerConfig` | `required` | `information_point: GpuLogicalLayerConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class GpuSpatialLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    zoning: GpuLogicalLayerConfig
    prescription_surface: GpuLogicalLayerConfig
    prescription_line: GpuLogicalLayerConfig
    prescription_point: GpuLogicalLayerConfig
    information_surface: GpuLogicalLayerConfig
    information_line: GpuLogicalLayerConfig
    information_point: GpuLogicalLayerConfig
```

### `GpuSourceConfig`

**Source purpose:** Strict configuration for official French GPU ingestion.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `provider` | `GpuOfficialSourceIdentity` | `required` | `provider: GpuOfficialSourceIdentity` |
| `portal` | `GpuOfficialSourceIdentity` | `required` | `portal: GpuOfficialSourceIdentity` |
| `country` | `Literal['FR']` | `required` | `country: Literal["FR"]` |
| `api` | `GpuApiConfig` | `required` | `api: GpuApiConfig` |
| `download` | `GpuDownloadConfig` | `required` | `download: GpuDownloadConfig` |
| `cache` | `GpuCacheConfig` | `required` | `cache: GpuCacheConfig` |
| `pilot` | `GpuPilotConfig` | `required` | `pilot: GpuPilotConfig` |
| `spatial_layers` | `GpuSpatialLayersConfig` | `required` | `spatial_layers: GpuSpatialLayersConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuConfigError,
    GpuDiscoveryError,
    GpuDocumentMetadata,
    GpuDownloadError,
    GpuError,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    GpuSpatialLayerReference,
    GpuSpatialSourceFileIntegrity,
    GpuValidatedSpatialLayerSource,
    GpuWrittenFile,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    ingest_gpu_planning_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    revalidate_gpu_spatial_layer_source,
    revalidate_gpu_spatial_layer_sources,
    validate_gpu_archive,
)`
- value/type reference: `landscout.sources.gpu_fr::load_gpu_source_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_validated_source_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_partition` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_api_url` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_document_list_url` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::build_gpu_partition_download_url` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_written_files` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::discover_current_gpu_document` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_document_for_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_layer_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_discover_logical_layer` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_configured_logical_references` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_extraction_for_config` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::_validate_gpu_planning_document_config_identity` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::inspect_gpu_planning_document` via `GpuSourceConfig`
- value/type reference: `landscout.sources.gpu_fr::ingest_gpu_planning_document` via `GpuSourceConfig`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_gpu_document` via `GpuSourceConfig`
- import: `tests.unit.test_enrich_planning_features::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- value/type reference: `tests.unit.test_enrich_planning_features::_planning_document` via `GpuSourceConfig`
- import: `tests.unit.test_gpu_fr::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)`
- value/type reference: `tests.unit.test_gpu_fr::_config` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_invalid_config_values_are_rejected` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_source_identity_is_exact` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_cache_age_rejects_coercion_and_nonfinite` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_gpu_source_config_identity_is_deterministic_and_content_bound` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_unknown_config_field_is_rejected` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_missing_zoning_layer_fails_clearly` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::test_ambiguous_zoning_layer_fails_clearly` via `GpuSourceConfig`
- value/type reference: `tests.unit.test_gpu_fr::_config_with_shared_role_token` via `GpuSourceConfig`
- import: `tests.unit.test_index_planning_regulation::<module>` via `from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)`
- value/type reference: `tests.unit.test_index_planning_regulation::_document` via `GpuSourceConfig`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `GpuSourceConfig`

**Exact class source**

```python
class GpuSourceConfig(BaseModel):
    """Strict configuration for official French GPU ingestion."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: GpuOfficialSourceIdentity
    portal: GpuOfficialSourceIdentity
    country: Literal["FR"]
    api: GpuApiConfig
    download: GpuDownloadConfig
    cache: GpuCacheConfig
    pilot: GpuPilotConfig
    spatial_layers: GpuSpatialLayersConfig
```

## 6. Functions and methods

Loader: `landscout.sources.gpu_fr.load_gpu_source_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `discover_current_gpu_document`, `download_gpu_document`, `discover_gpu_spatial_layers`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior only where the runtime source actually computes a hash.

## 17. Change impact

Any YAML byte/value change requires policy/source review, consumer tests, generated artifacts where applicable, this companion SHA update, and only those runtime hashes whose documented algorithm actually includes these bytes or validated values.

## 18. Complete readable configuration and authoritative raw-byte snapshot

### Complete readable YAML

The following is the complete decoded UTF-8 configuration with line endings normalized to LF for stable Markdown display. Every character and logical line is present, but this readable fence is not the authority for original CR/LF byte positions.

```yaml
provider: "Géoportail de l'Urbanisme"
portal: "Géoportail de l'Urbanisme"
country: FR

api:
  base_url: "https://www.geoportail-urbanisme.gouv.fr/api"

download:
  strategy: partition
  partition_template: "DU_{code_insee}"

cache:
  max_age_hours: 168

pilot:
  commune_code: "31395"

spatial_layers:
  zoning:
    class_label: "Zone urba"
    match_tokens:
      - "zone_urba"
  prescription_surface:
    class_label: "Prescription surfacique"
    match_tokens:
      - "prescription_surf"
  prescription_line:
    class_label: "Prescription linéaire"
    match_tokens:
      - "prescription_lin"
  prescription_point:
    class_label: "Prescription ponctuelle"
    match_tokens:
      - "prescription_pct"
  information_surface:
    class_label: "Information surfacique"
    match_tokens:
      - "info_surf"
  information_line:
    class_label: "Information linéaire"
    match_tokens:
      - "info_lin"
  information_point:
    class_label: "Information ponctuelle"
    match_tokens:
      - "info_pct"
```

### Authoritative raw-byte payload

- Raw byte length: `1013`.
- Raw SHA256: `f069bf398c752380ca58c90504aa34c322376d52422fd237805e67f2f7829066` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
cHJvdmlkZXI6ICJHw6lvcG9ydGFpbCBkZSBsJ1VyYmFuaXNtZSIKcG9ydGFsOiAiR8Opb3BvcnRh
aWwgZGUgbCdVcmJhbmlzbWUiCmNvdW50cnk6IEZSCgphcGk6CiAgYmFzZV91cmw6ICJodHRwczov
L3d3dy5nZW9wb3J0YWlsLXVyYmFuaXNtZS5nb3V2LmZyL2FwaSIKCmRvd25sb2FkOgogIHN0cmF0
ZWd5OiBwYXJ0aXRpb24KICBwYXJ0aXRpb25fdGVtcGxhdGU6ICJEVV97Y29kZV9pbnNlZX0iCgpj
YWNoZToKICBtYXhfYWdlX2hvdXJzOiAxNjgKCnBpbG90OgogIGNvbW11bmVfY29kZTogIjMxMzk1
IgoKc3BhdGlhbF9sYXllcnM6CiAgem9uaW5nOgogICAgY2xhc3NfbGFiZWw6ICJab25lIHVyYmEi
CiAgICBtYXRjaF90b2tlbnM6CiAgICAgIC0gInpvbmVfdXJiYSIKICBwcmVzY3JpcHRpb25fc3Vy
ZmFjZToKICAgIGNsYXNzX2xhYmVsOiAiUHJlc2NyaXB0aW9uIHN1cmZhY2lxdWUiCiAgICBtYXRj
aF90b2tlbnM6CiAgICAgIC0gInByZXNjcmlwdGlvbl9zdXJmIgogIHByZXNjcmlwdGlvbl9saW5l
OgogICAgY2xhc3NfbGFiZWw6ICJQcmVzY3JpcHRpb24gbGluw6lhaXJlIgogICAgbWF0Y2hfdG9r
ZW5zOgogICAgICAtICJwcmVzY3JpcHRpb25fbGluIgogIHByZXNjcmlwdGlvbl9wb2ludDoKICAg
IGNsYXNzX2xhYmVsOiAiUHJlc2NyaXB0aW9uIHBvbmN0dWVsbGUiCiAgICBtYXRjaF90b2tlbnM6
CiAgICAgIC0gInByZXNjcmlwdGlvbl9wY3QiCiAgaW5mb3JtYXRpb25fc3VyZmFjZToKICAgIGNs
YXNzX2xhYmVsOiAiSW5mb3JtYXRpb24gc3VyZmFjaXF1ZSIKICAgIG1hdGNoX3Rva2VuczoKICAg
ICAgLSAiaW5mb19zdXJmIgogIGluZm9ybWF0aW9uX2xpbmU6CiAgICBjbGFzc19sYWJlbDogIklu
Zm9ybWF0aW9uIGxpbsOpYWlyZSIKICAgIG1hdGNoX3Rva2VuczoKICAgICAgLSAiaW5mb19saW4i
CiAgaW5mb3JtYXRpb25fcG9pbnQ6CiAgICBjbGFzc19sYWJlbDogIkluZm9ybWF0aW9uIHBvbmN0
dWVsbGUiCiAgICBtYXRjaF90b2tlbnM6CiAgICAgIC0gImluZm9fcGN0Igo=
```
