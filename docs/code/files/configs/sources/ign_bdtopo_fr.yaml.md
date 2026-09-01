# `configs/sources/ign_bdtopo_fr.yaml`

## File identity

- Repository path: `configs/sources/ign_bdtopo_fr.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Pins the IGN BD TOPO D031 archive identity, checksum/size, cache, logical layers, access, and coverage selection.
- Source SHA256: `fa3cc4e82f7c5a2a917a60508fdba6de37f0bde07d7da6b27f2cd00124e44a86`

## 1. Purpose

Pins the IGN BD TOPO D031 archive identity, checksum/size, cache, logical layers, access, and coverage selection.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_source_config` into `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`. Runtime consumers include `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `provider` | `"Institut national de l'information géographique et forestière (IGN)"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the configured source provider copied/compared as lineage. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `product` | `"BD TOPO"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `product` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `department_code` | `"31"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `department code` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `edition` | `"2026-06-15"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `edition` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `product_version` | `"3.5"` | `str` | source-declared default is true null; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `product version` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `projection` | `"EPSG:2154"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `projection` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `format` | `"GPKG"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `format` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `archive_format` | `"7z"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `archive format` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `source_url` | `"https://data.geopf.fr/telechargement/download/BDTOPO/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15.7z"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact source url; HTTPS/origin/path validation is defined by the consuming model. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `checksum_url` | `null` | `NoneType` | source-declared default is true null; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact checksum url; HTTPS/origin/path validation is defined by the consuming model. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `official_checksum_algorithm` | `"md5"` | `str` | source-declared default is true null; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official checksum algorithm` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `official_checksum` | `"24d4a50b7eae3c0d55bb55ffd5b525a6"` | `str` | source-declared default is true null; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official checksum` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `expected_archive_size_bytes` | `494818677` | `int` | source-declared default is true null; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; strict positive integer; Boolean rejected; exact physical archive pin | Pins the exact approved archive byte length. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `cache_max_age_hours` | `168` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `cache max age hours` under the exact parent path `<root>`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `logical_layers.electric_lines.class_label` | `"Ligne électrique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `logical_layers.electric_lines`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `logical_layers.electric_lines.match_tokens[0]` | `"ligne"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `logical_layers.electric_lines.match_tokens`; order and uniqueness are validated/consumed where required. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `logical_layers.electric_lines.match_tokens[1]` | `"électrique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `logical_layers.electric_lines.match_tokens`; order and uniqueness are validated/consumed where required. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `logical_layers.transformation_posts.class_label` | `"Poste de transformation"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `logical_layers.transformation_posts`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `logical_layers.transformation_posts.match_tokens[0]` | `"poste"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `logical_layers.transformation_posts.match_tokens`; order and uniqueness are validated/consumed where required. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `logical_layers.transformation_posts.match_tokens[1]` | `"transformation"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `logical_layers.transformation_posts.match_tokens`; order and uniqueness are validated/consumed where required. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `access.road_segments.class_label` | `"Tronçon de route"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `access.road_segments`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `access.road_segments.match_tokens[0]` | `"tronçon"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `access.road_segments.match_tokens`; order and uniqueness are validated/consumed where required. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `access.road_segments.match_tokens[1]` | `"route"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `access.road_segments.match_tokens`; order and uniqueness are validated/consumed where required. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `coverage.department_layer.class_label` | `"Département"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `class label` under the exact parent path `coverage.department_layer`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `coverage.department_layer.match_tokens[0]` | `"departement"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `coverage.department_layer.match_tokens`; order and uniqueness are validated/consumed where required. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |
| `coverage.department_layer.department_code_field` | `"code_insee"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `department code field` under the exact parent path `coverage.department_layer`. | `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_source_config`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `fa3cc4e82f7c5a2a917a60508fdba6de37f0bde07d7da6b27f2cd00124e44a86`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_source_config`.
- Owning Python module: `landscout.sources.ign_bdtopo_fr`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

### `IgnBdTopoLogicalLayerConfig`

**Source purpose:** Catalogue class label and normalized tokens used for layer discovery.

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

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_matching_layers` via `IgnBdTopoLogicalLayerConfig`

**Exact class source**

```python
class IgnBdTopoLogicalLayerConfig(BaseModel):
    """Catalogue class label and normalized tokens used for layer discovery."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    class_label: NonEmptyString
    match_tokens: tuple[NonEmptyString, ...] = Field(min_length=1)

    @field_validator("match_tokens")
    @classmethod
    def _unique_tokens(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(_normalize_words(token) for token in value)
        if any(not token for token in normalized):
            raise ValueError("Layer match tokens must contain letters or digits")
        if len(set(normalized)) != len(normalized):
            raise ValueError("Layer match tokens must be unique after normalization")
        return value
```

### `IgnBdTopoLogicalLayersConfig`

**Source purpose:** Defines `IgnBdTopoLogicalLayersConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `electric_lines` | `IgnBdTopoLogicalLayerConfig` | `required` | `electric_lines: IgnBdTopoLogicalLayerConfig` |
| `transformation_posts` | `IgnBdTopoLogicalLayerConfig` | `required` | `transformation_posts: IgnBdTopoLogicalLayerConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`

**Exact class source**

```python
class IgnBdTopoLogicalLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    electric_lines: IgnBdTopoLogicalLayerConfig
    transformation_posts: IgnBdTopoLogicalLayerConfig

    @model_validator(mode="after")
    def _different_token_sets(self) -> Self:
        electric = {
            _normalize_words(token) for token in self.electric_lines.match_tokens
        }
        posts = {
            _normalize_words(token) for token in self.transformation_posts.match_tokens
        }
        if electric == posts:
            raise ValueError("Logical layers must use different match tokens")
        return self
```

### `IgnBdTopoDepartmentLayerConfig`

**Source purpose:** Configured department layer and its observed identity field.

- Exact decorators: none.
- Exact bases: `IgnBdTopoLogicalLayerConfig`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `department_code_field` | `NonEmptyString` | `required` | `department_code_field: NonEmptyString` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`

**Exact class source**

```python
class IgnBdTopoDepartmentLayerConfig(IgnBdTopoLogicalLayerConfig):
    """Configured department layer and its observed identity field."""

    department_code_field: NonEmptyString
```

### `IgnBdTopoAccessConfig`

**Source purpose:** Configured factual transport layers loaded outside extraction metadata.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `road_segments` | `IgnBdTopoLogicalLayerConfig` | `required` | `road_segments: IgnBdTopoLogicalLayerConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class IgnBdTopoAccessConfig(BaseModel):
    """Configured factual transport layers loaded outside extraction metadata."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    road_segments: IgnBdTopoLogicalLayerConfig
```

### `IgnBdTopoCoverageConfig`

**Source purpose:** Defines `IgnBdTopoCoverageConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `department_layer` | `IgnBdTopoDepartmentLayerConfig` | `required` | `department_layer: IgnBdTopoDepartmentLayerConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`

**Exact class source**

```python
class IgnBdTopoCoverageConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    department_layer: IgnBdTopoDepartmentLayerConfig
```

### `IgnBdTopoSourceConfig`

**Source purpose:** Strict, reproducible description of one official IGN package.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `provider` | `Literal["Institut national de l'information géographique et forestière (IGN)"]` | `required` | `provider: Literal[<br>        "Institut national de l'information géographique et forestière (IGN)"<br>    ]` |
| `product` | `Literal['BD TOPO']` | `required` | `product: Literal["BD TOPO"]` |
| `department_code` | `DepartmentCode` | `required` | `department_code: DepartmentCode` |
| `edition` | `EditionString` | `required` | `edition: EditionString` |
| `product_version` | `NonEmptyString \| None` | `None` | `product_version: NonEmptyString \| None = None` |
| `projection` | `Projection` | `required` | `projection: Projection` |
| `format` | `PackageFormat` | `required` | `format: PackageFormat` |
| `archive_format` | `ArchiveFormat` | `required` | `archive_format: ArchiveFormat` |
| `source_url` | `HttpUrl` | `required` | `source_url: HttpUrl` |
| `checksum_url` | `HttpUrl \| None` | `None` | `checksum_url: HttpUrl \| None = None` |
| `official_checksum_algorithm` | `ChecksumAlgorithm \| None` | `None` | `official_checksum_algorithm: ChecksumAlgorithm \| None = None` |
| `official_checksum` | `HexChecksum \| None` | `None` | `official_checksum: HexChecksum \| None = None` |
| `expected_archive_size_bytes` | `StrictPositiveInt \| None` | `None` | `expected_archive_size_bytes: StrictPositiveInt \| None = None` |
| `cache_max_age_hours` | `StrictNonNegativeFloat` | `required` | `cache_max_age_hours: StrictNonNegativeFloat` |
| `logical_layers` | `IgnBdTopoLogicalLayersConfig` | `required` | `logical_layers: IgnBdTopoLogicalLayersConfig` |
| `access` | `IgnBdTopoAccessConfig` | `required` | `access: IgnBdTopoAccessConfig` |
| `coverage` | `IgnBdTopoCoverageConfig` | `required` | `coverage: IgnBdTopoCoverageConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoArchiveIntegrity,
    IgnBdTopoCoverageConfig,
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDepartmentLayerConfig,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoElectricityData,
    IgnBdTopoError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoLayerSelection,
    IgnBdTopoLayerSummary,
    IgnBdTopoLoadedLayer,
    IgnBdTopoLogicalLayerConfig,
    IgnBdTopoLogicalLayersConfig,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_source_config` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validated_source_config` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_archive_filename` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::validate_ign_bdtopo_archive` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::discover_ign_bdtopo_layers` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_department_coverage_layer` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_road_layer` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_discover_configured_physical_roles` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validated_layer_source_config` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_archive_config_lineage` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_electricity` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_roads` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::load_ign_bdtopo_department_coverage` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_electricity_data` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_road_data` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_revalidate_ign_bdtopo_department_coverage` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.apply_road_vehicle_proxy_policy::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::apply_ign_road_vehicle_proxy_policy` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.assess_grid_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_configured_coverage_identity` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_coverage_summary` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::assess_road_proximity_coverage` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.enrich_grid_proximity::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
)`
- value/type reference: `landscout.stages.enrich_grid_proximity::enrich_parcel_grid_proximity` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.enrich_road_proximity::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.enrich_road_proximity::enrich_parcel_road_proximity` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `IgnBdTopoSourceConfig`
- value/type reference: `landscout.stages.normalize_access_ign::normalize_ign_roads` via `IgnBdTopoSourceConfig`
- import: `landscout.stages.normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_electricity_data,
    _validate_layer_summary_contract,
)`
- value/type reference: `landscout.stages.normalize_grid_ign::normalize_ign_electricity` via `IgnBdTopoSourceConfig`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `IgnBdTopoSourceConfig`
- import: `tests.unit.test_ign_bdtopo_fr::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_synthetic_config` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::_extracted_fixture` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::source_config` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_valid_source_config_loads` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_loaded_ign_source_config_and_nested_models_are_frozen` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_revalidates_a_tampered_config_before_network` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_invalid_department_coverage_config_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_required_source_field_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_invalid_source_configuration_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unknown_source_config_field_is_rejected` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_successful_archive_download_persists_sha256` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_fresh_cache_is_reused_without_network` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_recovery_backup_rejects_cache_before_network` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_expired_cache_is_refreshed` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_failed_refresh_preserves_valid_cache` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_corrupt_refresh_preserves_valid_cache` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_official_checksum_mismatch_is_rejected` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_unsafe_parent_archive_member_is_rejected` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_real_layer_names_are_listed_and_discovered` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_electric_line_layer_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_transformation_post_layer_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_electric_line_layers_fail` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_synthetic_archive_extracts_and_discovers_required_layers` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_schema_v3_extraction_metadata_binds_complete_physical_inventory` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_rejects_forged_download_lineage_before_archive_open` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_same_size_geopackage_tamper_invalidates_extraction_cache` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_forged_extraction_metadata_never_returns_cache_hit` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_linked_extraction_metadata_never_returns_cache_hit` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_sha_is_not_trusted` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_malformed_geopackage_size_is_not_trusted` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_default_extraction_path_is_short_and_content_addressed` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_loader_retains_both_layer_counts` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_discovery_loads_selected_physical_layer` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_physical_layer_cannot_collide_with_electricity_roles` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_road_role` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_physical_layer_cannot_collide_with_electricity_roles` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_electricity_physical_layers_must_be_distinct` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_road_layer_fails_safely` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_ambiguous_road_layer_fails_safely` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_wrong_archive_config_department` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_changed_layer_inventory` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_geographic_crs` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_preserves_lambert93_lines_unchanged` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_stale_extraction_backup_blocks_before_7z_open` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_part_link_is_rejected_without_touching_target` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_download_cache_reader_rejects_noncanonical_json_and_refreshes` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_extraction_cache_reader_rejects_noncanonical_json_and_rebuilds` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_loader_selects_configured_identity` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_one_authoritative_feature` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_requires_configured_identity_field` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_missing_department_coverage_layer_fails` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_department_coverage_layer_discovery_must_be_unambiguous` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_direct_consumers_reject_same_inventory_content_tampering` via `IgnBdTopoSourceConfig`
- value/type reference: `tests.unit.test_ign_bdtopo_fr::test_road_loader_rejects_source_change_after_physical_read` via `IgnBdTopoSourceConfig`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- import: `tests.unit.test_normalize_grid_ign::<module>` via `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`

**Exact class source**

```python
class IgnBdTopoSourceConfig(BaseModel):
    """Strict, reproducible description of one official IGN package."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: Literal[
        "Institut national de l'information géographique et forestière (IGN)"
    ]
    product: Literal["BD TOPO"]
    department_code: DepartmentCode
    edition: EditionString
    product_version: NonEmptyString | None = None
    projection: Projection
    format: PackageFormat
    archive_format: ArchiveFormat
    source_url: HttpUrl
    checksum_url: HttpUrl | None = None
    official_checksum_algorithm: ChecksumAlgorithm | None = None
    official_checksum: HexChecksum | None = None
    expected_archive_size_bytes: StrictPositiveInt | None = None
    cache_max_age_hours: StrictNonNegativeFloat
    logical_layers: IgnBdTopoLogicalLayersConfig
    access: IgnBdTopoAccessConfig
    coverage: IgnBdTopoCoverageConfig

    @field_validator("edition")
    @classmethod
    def _valid_edition_date(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError as error:
            raise ValueError("edition must be a valid ISO calendar date") from error
        return value

    @model_validator(mode="after")
    def _consistent_package_and_checksum(self) -> Self:
        path = unquote(urlparse(str(self.source_url)).path)
        if Path(path).suffix.casefold() != f".{self.archive_format}":
            raise ValueError("source_url extension does not match archive_format")

        has_algorithm = self.official_checksum_algorithm is not None
        has_checksum = self.official_checksum is not None
        if has_algorithm != has_checksum:
            raise ValueError(
                "official_checksum_algorithm and official_checksum must be set together"
            )
        if (
            self.official_checksum_algorithm == "md5"
            and len(self.official_checksum or "") != 32
        ):
            raise ValueError(
                "An official MD5 checksum must contain 32 hexadecimal digits"
            )
        if (
            self.official_checksum_algorithm == "sha256"
            and len(self.official_checksum or "") != 64
        ):
            raise ValueError(
                "An official SHA256 checksum must contain 64 hexadecimal digits"
            )
        if self.checksum_url is not None and not has_checksum:
            raise ValueError(
                "checksum_url requires a pinned official checksum and algorithm"
            )
        return self
```

### `_CacheMetadata`

**Source purpose:** Defines `_CacheMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `schema_version` | `Literal[1]` | `required` | `schema_version: Literal[1]` |
| `provider` | `str` | `required` | `provider: str` |
| `product` | `str` | `required` | `product: str` |
| `department_code` | `str` | `required` | `department_code: str` |
| `edition` | `str` | `required` | `edition: str` |
| `product_version` | `str \| None` | `required` | `product_version: str \| None` |
| `projection` | `str` | `required` | `projection: str` |
| `package_format` | `str` | `required` | `package_format: str` |
| `archive_format` | `str` | `required` | `archive_format: str` |
| `source_url` | `str` | `required` | `source_url: str` |
| `checksum_url` | `str \| None` | `required` | `checksum_url: str \| None` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `filename` | `str` | `required` | `filename: str` |
| `file_size` | `StrictPositiveInt` | `required` | `file_size: StrictPositiveInt` |
| `sha256` | `CanonicalSha256` | `required` | `sha256: CanonicalSha256` |
| `official_checksum_algorithm` | `ChecksumAlgorithm \| None` | `required` | `official_checksum_algorithm: ChecksumAlgorithm \| None` |
| `official_checksum` | `str \| None` | `required` | `official_checksum: str \| None` |
| `official_checksum_validated` | `StrictBool` | `required` | `official_checksum_validated: StrictBool` |
| `spatial_role` | `SpatialRole` | `required` | `spatial_role: SpatialRole` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.ign_bdtopo_fr::_cache_metadata_from_download` via `_CacheMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_cache_metadata_from_download` via `_CacheMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_download_from_metadata` via `_CacheMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_download` via `_CacheMetadata`

**Exact class source**

```python
class _CacheMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    provider: str
    product: str
    department_code: str
    edition: str
    product_version: str | None
    projection: str
    package_format: str
    archive_format: str
    source_url: str
    checksum_url: str | None
    download_timestamp: str
    filename: str
    file_size: StrictPositiveInt
    sha256: CanonicalSha256
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: StrictBool
    spatial_role: SpatialRole

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("IGN cache schema version must be an exact integer")
        return value
```

### `_ExtractedEntryMetadata`

**Source purpose:** Defines `_ExtractedEntryMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `relative_path` | `str` | `required` | `relative_path: str` |
| `kind` | `Literal['file', 'directory']` | `required` | `kind: Literal["file", "directory"]` |
| `size_bytes` | `int \| None` | `Field(default=None, strict=True, ge=0)` | `size_bytes: int \| None = Field(default=None, strict=True, ge=0)` |
| `sha256` | `CanonicalSha256 \| None` | `None` | `sha256: CanonicalSha256 \| None = None` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.ign_bdtopo_fr::_inventory_extracted_tree` via `_ExtractedEntryMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_inventory_extracted_tree` via `_ExtractedEntryMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extracted_inventory` via `_ExtractedEntryMetadata`

**Exact class source**

```python
class _ExtractedEntryMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    relative_path: str
    kind: Literal["file", "directory"]
    size_bytes: int | None = Field(default=None, strict=True, ge=0)
    sha256: CanonicalSha256 | None = None
```

### `_ExtractionMetadata`

**Source purpose:** Defines `_ExtractionMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `schema_version` | `Literal[3]` | `required` | `schema_version: Literal[3]` |
| `archive_sha256` | `CanonicalSha256` | `required` | `archive_sha256: CanonicalSha256` |
| `geopackage_relative_path` | `str` | `required` | `geopackage_relative_path: str` |
| `geopackage_size_bytes` | `StrictPositiveInt` | `required` | `geopackage_size_bytes: StrictPositiveInt` |
| `geopackage_sha256` | `CanonicalSha256` | `required` | `geopackage_sha256: CanonicalSha256` |
| `all_layer_names` | `tuple[str, ...]` | `required` | `all_layer_names: tuple[str, ...]` |
| `electric_lines_layer` | `str` | `required` | `electric_lines_layer: str` |
| `transformation_posts_layer` | `str` | `required` | `transformation_posts_layer: str` |
| `road_segments_layer` | `str` | `required` | `road_segments_layer: str` |
| `department_layer` | `str` | `required` | `department_layer: str` |
| `extracted_entries` | `tuple[_ExtractedEntryMetadata, ...]` | `required` | `extracted_entries: tuple[_ExtractedEntryMetadata, ...]` |
| `spatial_role` | `SpatialRole` | `required` | `spatial_role: SpatialRole` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.sources.ign_bdtopo_fr::_validate_extraction_envelope` via `_ExtractionMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::_load_cached_extraction` via `_ExtractionMetadata`
- constructor call: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_ExtractionMetadata`
- value/type reference: `landscout.sources.ign_bdtopo_fr::extract_ign_bdtopo_archive` via `_ExtractionMetadata`

**Exact class source**

```python
class _ExtractionMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[3]
    archive_sha256: CanonicalSha256
    geopackage_relative_path: str
    geopackage_size_bytes: StrictPositiveInt
    geopackage_sha256: CanonicalSha256
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    road_segments_layer: str
    department_layer: str
    extracted_entries: tuple[_ExtractedEntryMetadata, ...]
    spatial_role: SpatialRole

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int:
            raise ValueError("IGN extraction schema version must be an exact integer")
        return value
```

## 6. Functions and methods

Loader: `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_source_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `download_ign_bdtopo_archive`, `load_ign_bdtopo_electricity`, `load_ign_bdtopo_roads`, `load_ign_bdtopo_department_coverage`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior only where the runtime source actually computes a hash.

## 17. Change impact

Any YAML byte/value change requires policy/source review, consumer tests, generated artifacts where applicable, this companion SHA update, and only those runtime hashes whose documented algorithm actually includes these bytes or validated values.

## 18. Complete readable configuration and authoritative raw-byte snapshot

### Complete readable YAML

The following is the complete decoded UTF-8 configuration with line endings normalized to LF for stable Markdown display. Every character and logical line is present, but this readable fence is not the authority for original CR/LF byte positions.

```yaml
provider: "Institut national de l'information géographique et forestière (IGN)"
product: "BD TOPO"
department_code: "31"
edition: "2026-06-15"
product_version: "3.5"
projection: "EPSG:2154"
format: "GPKG"
archive_format: "7z"
source_url: "https://data.geopf.fr/telechargement/download/BDTOPO/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15.7z"
checksum_url: null
official_checksum_algorithm: "md5"
official_checksum: "24d4a50b7eae3c0d55bb55ffd5b525a6"
expected_archive_size_bytes: 494818677
cache_max_age_hours: 168

logical_layers:
  electric_lines:
    class_label: "Ligne électrique"
    match_tokens:
      - "ligne"
      - "électrique"

  transformation_posts:
    class_label: "Poste de transformation"
    match_tokens:
      - "poste"
      - "transformation"

access:
  road_segments:
    class_label: "Tronçon de route"
    match_tokens:
      - "tronçon"
      - "route"

coverage:
  department_layer:
    class_label: "Département"
    match_tokens:
      - "departement"
    department_code_field: "code_insee"
```

### Authoritative raw-byte payload

- Raw byte length: `1084`.
- Raw SHA256: `fa3cc4e82f7c5a2a917a60508fdba6de37f0bde07d7da6b27f2cd00124e44a86` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
cHJvdmlkZXI6ICJJbnN0aXR1dCBuYXRpb25hbCBkZSBsJ2luZm9ybWF0aW9uIGfDqW9ncmFwaGlx
dWUgZXQgZm9yZXN0acOocmUgKElHTikiCnByb2R1Y3Q6ICJCRCBUT1BPIgpkZXBhcnRtZW50X2Nv
ZGU6ICIzMSIKZWRpdGlvbjogIjIwMjYtMDYtMTUiCnByb2R1Y3RfdmVyc2lvbjogIjMuNSIKcHJv
amVjdGlvbjogIkVQU0c6MjE1NCIKZm9ybWF0OiAiR1BLRyIKYXJjaGl2ZV9mb3JtYXQ6ICI3eiIK
c291cmNlX3VybDogImh0dHBzOi8vZGF0YS5nZW9wZi5mci90ZWxlY2hhcmdlbWVudC9kb3dubG9h
ZC9CRFRPUE8vQkRUT1BPXzMtNV9UT1VTVEhFTUVTX0dQS0dfTEFNQjkzX0QwMzFfMjAyNi0wNi0x
NS9CRFRPUE9fMy01X1RPVVNUSEVNRVNfR1BLR19MQU1COTNfRDAzMV8yMDI2LTA2LTE1Ljd6Igpj
aGVja3N1bV91cmw6IG51bGwKb2ZmaWNpYWxfY2hlY2tzdW1fYWxnb3JpdGhtOiAibWQ1IgpvZmZp
Y2lhbF9jaGVja3N1bTogIjI0ZDRhNTBiN2VhZTNjMGQ1NWJiNTVmZmQ1YjUyNWE2IgpleHBlY3Rl
ZF9hcmNoaXZlX3NpemVfYnl0ZXM6IDQ5NDgxODY3NwpjYWNoZV9tYXhfYWdlX2hvdXJzOiAxNjgK
CmxvZ2ljYWxfbGF5ZXJzOgogIGVsZWN0cmljX2xpbmVzOgogICAgY2xhc3NfbGFiZWw6ICJMaWdu
ZSDDqWxlY3RyaXF1ZSIKICAgIG1hdGNoX3Rva2VuczoKICAgICAgLSAibGlnbmUiCiAgICAgIC0g
IsOpbGVjdHJpcXVlIgoKICB0cmFuc2Zvcm1hdGlvbl9wb3N0czoKICAgIGNsYXNzX2xhYmVsOiAi
UG9zdGUgZGUgdHJhbnNmb3JtYXRpb24iCiAgICBtYXRjaF90b2tlbnM6CiAgICAgIC0gInBvc3Rl
IgogICAgICAtICJ0cmFuc2Zvcm1hdGlvbiIKCmFjY2VzczoKICByb2FkX3NlZ21lbnRzOgogICAg
Y2xhc3NfbGFiZWw6ICJUcm9uw6dvbiBkZSByb3V0ZSIKICAgIG1hdGNoX3Rva2VuczoKICAgICAg
LSAidHJvbsOnb24iCiAgICAgIC0gInJvdXRlIgoKY292ZXJhZ2U6CiAgZGVwYXJ0bWVudF9sYXll
cjoKICAgIGNsYXNzX2xhYmVsOiAiRMOpcGFydGVtZW50IgogICAgbWF0Y2hfdG9rZW5zOgogICAg
ICAtICJkZXBhcnRlbWVudCIKICAgIGRlcGFydG1lbnRfY29kZV9maWVsZDogImNvZGVfaW5zZWUi
Cg==
```
