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
| `provider` | `"RTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the configured source provider copied/compared as lineage. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `portal` | `"ODRE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `portal` under the exact parent path `<root>`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `api.base_url` | `"https://odre.opendatasoft.com/api/explore/v2.1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Pins the exact official HTTPS API origin/path used to build requests. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.sites.dataset_id` | `"postes-electriques-rte"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Selects the exact external dataset identity used in source URL/API/cache validation. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.sites.preferred_format` | `"geojson"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `preferred format` under the exact parent path `datasets.sites`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.overhead_lines.dataset_id` | `"lignes-aeriennes-rte-nv"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Selects the exact external dataset identity used in source URL/API/cache validation. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.overhead_lines.preferred_format` | `"geojson"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `preferred format` under the exact parent path `datasets.overhead_lines`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.underground_lines.dataset_id` | `"lignes-souterraines-rte-nv"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Selects the exact external dataset identity used in source URL/API/cache validation. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `datasets.underground_lines.preferred_format` | `"geojson"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `preferred format` under the exact parent path `datasets.underground_lines`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |
| `cache.max_age_hours` | `168` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `max age hours` under the exact parent path `cache`. | `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.sources.rte_odre_fr.load_rte_odre_source_config`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `f2b5ffb43b1e8a73e1396eda3d91b42fe9074bc348a94a61ea84c1c29e1a8649`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.sources.rte_odre_fr.load_rte_odre_source_config`.
- Owning Python module: `landscout.sources.rte_odre_fr`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

### `RteDatasetConfig`

**Source purpose:** Defines `RteDatasetConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `dataset_id` | `DatasetIdentifier` | `required` | `dataset_id: DatasetIdentifier` |
| `preferred_format` | `ExportFormat` | `required` | `preferred_format: ExportFormat` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- value/type reference: `landscout.sources.rte_odre_fr::_get_dataset_config` via `RteDatasetConfig`

**Exact class source**

```python
class RteDatasetConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    dataset_id: DatasetIdentifier
    preferred_format: ExportFormat
```

### `RteDatasetsConfig`

**Source purpose:** Defines `RteDatasetsConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `sites` | `RteDatasetConfig` | `required` | `sites: RteDatasetConfig` |
| `overhead_lines` | `RteDatasetConfig` | `required` | `overhead_lines: RteDatasetConfig` |
| `underground_lines` | `RteDatasetConfig` | `required` | `underground_lines: RteDatasetConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class RteDatasetsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    sites: RteDatasetConfig
    overhead_lines: RteDatasetConfig
    underground_lines: RteDatasetConfig
```

### `RteOdreApiConfig`

**Source purpose:** Defines `RteOdreApiConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

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
class RteOdreApiConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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
```

### `RteOdreCacheConfig`

**Source purpose:** Defines `RteOdreCacheConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `max_age_hours` | `StrictNonNegativeFloat` | `required` | `max_age_hours: StrictNonNegativeFloat` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class RteOdreCacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    max_age_hours: StrictNonNegativeFloat
```

### `RteOdreSourceConfig`

**Source purpose:** Defines `RteOdreSourceConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `provider` | `Literal['RTE']` | `required` | `provider: Literal["RTE"]` |
| `portal` | `Literal['ODRE']` | `required` | `portal: Literal["ODRE"]` |
| `api` | `RteOdreApiConfig` | `required` | `api: RteOdreApiConfig` |
| `datasets` | `RteDatasetsConfig` | `required` | `datasets: RteDatasetsConfig` |
| `cache` | `RteOdreCacheConfig` | `required` | `cache: RteOdreCacheConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.rte_odre_fr import (
    RteDatasetConfig,
    RteOdreDatasetMetadata,
    RteOdreDownload,
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- value/type reference: `landscout.sources.rte_odre_fr::load_rte_odre_source_config` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::_validated_source_config` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::_get_dataset_config` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::_dataset_api_url` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::build_rte_odre_metadata_url` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::build_rte_odre_export_url` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::fetch_rte_odre_dataset_metadata` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::_load_cached_download` via `RteOdreSourceConfig`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `RteOdreSourceConfig`
- import: `tests.unit.test_rte_odre_fr::<module>` via `from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)`
- value/type reference: `tests.unit.test_rte_odre_fr::source_config` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_valid_source_config_loads` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_loaded_source_config_is_immutable` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_source_identity_is_exact` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cache_age_is_a_strict_finite_number` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_missing_dataset_id_fails` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_empty_base_url_fails` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_api_base_is_pinned_to_the_official_https_origin_and_path` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_cache_age_fails` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unsupported_export_format_fails` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_build_export_url` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_build_metadata_url` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_export_url_uses_configured_dataset_id` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_is_captured_without_fabrication` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_duplicate_json_keys` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_response_rejects_nonfinite_json_constants` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_successful_download` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_export_record_count_mismatch_is_rejected` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_unavailable_metadata_record_count_is_accepted` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_negative_source_record_count_is_rejected` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_fresh_cache_is_reused` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_untrusted_cache_metadata_is_rejected_and_refreshed` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_expired_cache_is_refreshed` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_http_failure_raises_and_cleans_temporary_files` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_failed_refresh_preserves_previous_valid_cache` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_refresh_preserves_previous_valid_cache` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_metadata_publication_failure_restores_previous_pair` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_geojson_download_is_rejected` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_null_feature_geometries_are_accepted` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_lineage_sidecar_records_integrity` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_invalid_cached_record_count_invalidates_cache` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_cached_export_summary_mismatch_invalidates_cache` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_corrupted_cached_export_triggers_refresh` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_broken_recovery_symlink_rejects_rte_before_network` via `RteOdreSourceConfig`
- value/type reference: `tests.unit.test_rte_odre_fr::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `RteOdreSourceConfig`

**Exact class source**

```python
class RteOdreSourceConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: Literal["RTE"]
    portal: Literal["ODRE"]
    api: RteOdreApiConfig
    datasets: RteDatasetsConfig
    cache: RteOdreCacheConfig
```

## 6. Functions and methods

Loader: `landscout.sources.rte_odre_fr.load_rte_odre_source_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `fetch_rte_odre_dataset_metadata`, `download_rte_odre_dataset`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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
provider: RTE
portal: ODRE

api:
  base_url: "https://odre.opendatasoft.com/api/explore/v2.1"

datasets:
  sites:
    dataset_id: "postes-electriques-rte"
    preferred_format: "geojson"

  overhead_lines:
    dataset_id: "lignes-aeriennes-rte-nv"
    preferred_format: "geojson"

  underground_lines:
    dataset_id: "lignes-souterraines-rte-nv"
    preferred_format: "geojson"

cache:
  max_age_hours: 168
```

### Authoritative raw-byte payload

- Raw byte length: `408`.
- Raw SHA256: `f2b5ffb43b1e8a73e1396eda3d91b42fe9074bc348a94a61ea84c1c29e1a8649` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
cHJvdmlkZXI6IFJURQpwb3J0YWw6IE9EUkUKCmFwaToKICBiYXNlX3VybDogImh0dHBzOi8vb2Ry
ZS5vcGVuZGF0YXNvZnQuY29tL2FwaS9leHBsb3JlL3YyLjEiCgpkYXRhc2V0czoKICBzaXRlczoK
ICAgIGRhdGFzZXRfaWQ6ICJwb3N0ZXMtZWxlY3RyaXF1ZXMtcnRlIgogICAgcHJlZmVycmVkX2Zv
cm1hdDogImdlb2pzb24iCgogIG92ZXJoZWFkX2xpbmVzOgogICAgZGF0YXNldF9pZDogImxpZ25l
cy1hZXJpZW5uZXMtcnRlLW52IgogICAgcHJlZmVycmVkX2Zvcm1hdDogImdlb2pzb24iCgogIHVu
ZGVyZ3JvdW5kX2xpbmVzOgogICAgZGF0YXNldF9pZDogImxpZ25lcy1zb3V0ZXJyYWluZXMtcnRl
LW52IgogICAgcHJlZmVycmVkX2Zvcm1hdDogImdlb2pzb24iCgpjYWNoZToKICBtYXhfYWdlX2hv
dXJzOiAxNjgK
```
