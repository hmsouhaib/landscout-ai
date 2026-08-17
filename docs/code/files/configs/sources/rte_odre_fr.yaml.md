# `configs/sources/rte_odre_fr.yaml`

## File identity

- Repository path: `configs/sources/rte_odre_fr.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Pins the official ODRÉ API/cache identity and exact RTE dataset IDs/formats.
- Source SHA256: `f2b5ffb43b1e8a73e1396eda3d91b42fe9074bc348a94a61ea84c1c29e1a8649`

## 1. Purpose

Pins the official ODRÉ API/cache identity and exact RTE dataset IDs/formats.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.sources.rte_odre_fr.load_rte_odre_source_config` into `landscout.sources.rte_odre_fr.RteOdreSourceConfig`. Runtime consumers include `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `provider` | `"RTE"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the configured source provider copied/compared as lineage. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `portal` | `"ODRE"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None, ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `portal` under the exact parent path `<root>`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `api.base_url` | `"https://odre.opendatasoft.com/api/explore/v2.1"` | `str` | annotation `<class 'pydantic.networks.HttpUrl'>`; required; no inline Field metadata; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Pins the exact official HTTPS API origin/path used to build requests. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.sites.dataset_id` | `"postes-electriques-rte"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern='^[A-Za-z0-9][A-Za-z0-9_-]*$', ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Selects the exact external dataset identity used in source URL/API/cache validation. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.sites.preferred_format` | `"geojson"` | `str` | annotation `Literal['geojson']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `preferred format` under the exact parent path `datasets.sites`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.overhead_lines.dataset_id` | `"lignes-aeriennes-rte-nv"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern='^[A-Za-z0-9][A-Za-z0-9_-]*$', ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Selects the exact external dataset identity used in source URL/API/cache validation. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.overhead_lines.preferred_format` | `"geojson"` | `str` | annotation `Literal['geojson']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `preferred format` under the exact parent path `datasets.overhead_lines`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.underground_lines.dataset_id` | `"lignes-souterraines-rte-nv"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern='^[A-Za-z0-9][A-Za-z0-9_-]*$', ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Selects the exact external dataset identity used in source URL/API/cache validation. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.underground_lines.preferred_format` | `"geojson"` | `str` | annotation `Literal['geojson']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `preferred format` under the exact parent path `datasets.underground_lines`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `cache.max_age_hours` | `168` | `int` | annotation `<class 'float'>`; required; Ge(ge=0), _PydanticGeneralMetadata(allow_inf_nan=False); integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `max age hours` under the exact parent path `cache`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |

## 5. Classes / models / dataclasses

Authoritative owning model: `landscout.sources.rte_odre_fr.RteOdreSourceConfig`. The checked-in file currently validates as `RteOdreSourceConfig`.

```python
class RteDatasetConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    dataset_id: DatasetIdentifier
    preferred_format: ExportFormat

class RteDatasetsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sites: RteDatasetConfig
    overhead_lines: RteDatasetConfig
    underground_lines: RteDatasetConfig

class RteOdreApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    base_url: HttpUrl

    @field_validator("base_url")
    @classmethod
    def _official_api_origin(cls, value: HttpUrl) -> HttpUrl:
        parsed = urlsplit(str(value))
        if (
            parsed.scheme != "https"
            or parsed.hostname != "odre.opendatasoft.com"
            or parsed.port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path.rstrip("/") != "/api/explore/v2.1"
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("RTE/ODRE API must use the exact official HTTPS origin")
        return value

class RteOdreCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    max_age_hours: float = Field(ge=0, allow_inf_nan=False)

class RteOdreSourceConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    provider: NonEmptyString
    portal: NonEmptyString
    api: RteOdreApiConfig
    datasets: RteDatasetsConfig
    cache: RteOdreCacheConfig
```

## 6. Functions and methods

Loader: `landscout.sources.rte_odre_fr.load_rte_odre_source_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, byte hashing, and cross-field validation.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior.

## 17. Change impact

Any YAML byte/value change requires policy/source review, affected config/result hashes, consumer tests, generated artifacts where applicable, and this companion SHA update.
