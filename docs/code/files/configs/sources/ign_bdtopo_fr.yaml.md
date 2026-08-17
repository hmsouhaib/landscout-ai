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

## 5. Classes / models / dataclasses

Authoritative owning model: `landscout.sources.ign_bdtopo_fr.IgnBdTopoSourceConfig`. The checked-in file currently validates as `IgnBdTopoSourceConfig`.

```python
class IgnBdTopoLogicalLayerConfig(BaseModel):
    """Catalogue class label and normalized tokens used for layer discovery."""

    model_config = ConfigDict(extra="forbid")

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

class IgnBdTopoLogicalLayersConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    electric_lines: IgnBdTopoLogicalLayerConfig
    transformation_posts: IgnBdTopoLogicalLayerConfig

    @model_validator(mode="after")
    def _different_token_sets(self) -> Self:
        electric = {
            _normalize_words(token) for token in self.electric_lines.match_tokens
        }
        posts = {
            _normalize_words(token)
            for token in self.transformation_posts.match_tokens
        }
        if electric == posts:
            raise ValueError("Logical layers must use different match tokens")
        return self

class IgnBdTopoDepartmentLayerConfig(IgnBdTopoLogicalLayerConfig):
    """Configured department layer and its observed identity field."""

    department_code_field: NonEmptyString

class IgnBdTopoAccessConfig(BaseModel):
    """Configured factual transport layers loaded outside extraction metadata."""

    model_config = ConfigDict(extra="forbid")

    road_segments: IgnBdTopoLogicalLayerConfig

class IgnBdTopoCoverageConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    department_layer: IgnBdTopoDepartmentLayerConfig

class IgnBdTopoSourceConfig(BaseModel):
    """Strict, reproducible description of one official IGN package."""

    model_config = ConfigDict(extra="forbid")

    provider: NonEmptyString
    product: NonEmptyString
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
    expected_archive_size_bytes: int | None = Field(default=None, gt=0)
    cache_max_age_hours: float = Field(ge=0, allow_inf_nan=False)
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
        if self.official_checksum_algorithm == "md5" and len(
            self.official_checksum or ""
        ) != 32:
            raise ValueError("An official MD5 checksum must contain 32 hexadecimal digits")
        if self.official_checksum_algorithm == "sha256" and len(
            self.official_checksum or ""
        ) != 64:
            raise ValueError(
                "An official SHA256 checksum must contain 64 hexadecimal digits"
            )
        if self.checksum_url is not None and not has_checksum:
            raise ValueError(
                "checksum_url requires a pinned official checksum and algorithm"
            )
        return self

class _CacheMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

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
    file_size: int
    sha256: str
    official_checksum_algorithm: ChecksumAlgorithm | None
    official_checksum: str | None
    official_checksum_validated: bool
    spatial_role: SpatialRole

class _ExtractionMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[2]
    archive_sha256: CanonicalSha256
    geopackage_relative_path: str
    geopackage_size_bytes: StrictPositiveInt
    geopackage_sha256: CanonicalSha256
    all_layer_names: tuple[str, ...]
    electric_lines_layer: str
    transformation_posts_layer: str
    spatial_role: SpatialRole
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
