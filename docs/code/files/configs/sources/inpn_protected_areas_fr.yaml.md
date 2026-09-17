# `configs/sources/inpn_protected_areas_fr.yaml`

## File identity

- Repository path: `configs/sources/inpn_protected_areas_fr.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Pins the PatriNat/MNHN/INPN EP 07/2026 archive identity, size, SHA256, URLs, and cache root.
- Source SHA256: `75e3e45003b66cff10a755dfd64c27d3066ba65e4807af6e17e82bd3eae03397`

## 1. Purpose

Pins the PatriNat/MNHN/INPN EP 07/2026 archive identity, size, SHA256, URLs, and cache root.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config` into `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig`. Runtime consumers include `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

All twelve fields are required and non-null; extra keys are rejected. Runtime values below describe the validated model, not YAML scalar syntax. The model has no list/dict/set fields.

| Exact YAML path | Runtime type and allowed domain | Checked-in role |
|---|---|---|
| `provider` | `Literal["PatriNat"]` | Exact provider lineage. |
| `authority` | `Literal["MNHN"]` | Exact publishing authority lineage. |
| `program` | `Literal["INPN"]` | Exact program lineage. |
| `dataset_id` | `Literal["EP"]` | Dataset identity and cache path component. |
| `dataset_name` | Exact literal `Base de référence des espaces protégés français` | Dataset label, not category interpretation. |
| `declared_version` | Strict `str`, month `01`–`12` followed by `/` and four digits | Checked-in `07/2026`; model grammar is not a literal July-only lock. Cache directory converts `/` to `-`. |
| `reference_page_url` | `HttpUrl`, then exact string equality to the reviewed PatriNat reference URL | Provenance only; downloader does not scrape this page. |
| `archive_url` | `HttpUrl`, then exact string equality to the reviewed assets.patrinat.fr EP ZIP URL | Initial transport destination; shared safe-HTTPS separately owns redirect/address safety. |
| `archive_filename` | `Literal["EP.zip"]` | Archive basename and metadata sidecar naming. |
| `expected_archive_size_bytes` | Strict positive `int`; bool, float and numeric text rejected | YAML pins `99835011` bytes; model accepts other positive pins only through explicit config input. |
| `expected_archive_sha256` | Strict lowercase 64-hex `str` | YAML pins `73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5`; physical bytes must match. |
| `cache_root` | `Path`, parsed from YAML text | `.cache/landscout/inpn/protected_areas`; relative paths are process-working-directory relative. No repository-root containment validator is declared on this field. |

The default YAML path is also process-working-directory relative. Config loading reads bytes, rejects duplicate YAML keys and validates the model; it does not compute a config-byte hash. Frozen models block ordinary reassignment, while public source boundaries still reconstruct/revalidate supplied exact model objects. File/link, snapshot and recovery checks are adapter operations, not a promise that every arbitrary `Path` is intrinsically confined by this Pydantic field.

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `75e3e45003b66cff10a755dfd64c27d3066ba65e4807af6e17e82bd3eae03397`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config`.
- Owning Python module: `landscout.sources.inpn_protected_areas_fr`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

### `InpnProtectedAreasSourceConfig`

**Source purpose:** Strict identity of one reviewed PatriNat protected-areas snapshot.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `provider` | `Literal['PatriNat']` | `required` | `provider: Literal["PatriNat"]` |
| `authority` | `Literal['MNHN']` | `required` | `authority: Literal["MNHN"]` |
| `program` | `Literal['INPN']` | `required` | `program: Literal["INPN"]` |
| `dataset_id` | `Literal['EP']` | `required` | `dataset_id: Literal["EP"]` |
| `dataset_name` | `Literal['Base de référence des espaces protégés français']` | `required` | `dataset_name: Literal["Base de référence des espaces protégés français"]` |
| `declared_version` | `DeclaredVersion` | `required` | `declared_version: DeclaredVersion` |
| `reference_page_url` | `HttpUrl` | `required` | `reference_page_url: HttpUrl` |
| `archive_url` | `HttpUrl` | `required` | `archive_url: HttpUrl` |
| `archive_filename` | `Literal['EP.zip']` | `required` | `archive_filename: Literal["EP.zip"]` |
| `expected_archive_size_bytes` | `StrictPositiveInt` | `required` | `expected_archive_size_bytes: StrictPositiveInt` |
| `expected_archive_sha256` | `CanonicalSha256` | `required` | `expected_archive_sha256: CanonicalSha256` |
| `cache_root` | `Path` | `required` | `cache_root: Path` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validated_config` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::load_inpn_protected_areas_source_config` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_cache_directory` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_archive_path` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_download_metadata` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::download_inpn_protected_areas_archive` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_download` via `InpnProtectedAreasSourceConfig`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::extract_inpn_protected_areas_archive` via `InpnProtectedAreasSourceConfig`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_config` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_session` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download_with_session` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_checked_in_config_loads_with_exact_source_identity` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_invalid_expected_snapshot_integrity` via `InpnProtectedAreasSourceConfig`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_cache_setup_failure_is_controlled` via `InpnProtectedAreasSourceConfig`

**Exact class source**

```python
class InpnProtectedAreasSourceConfig(BaseModel):
    """Strict identity of one reviewed PatriNat protected-areas snapshot."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    provider: Literal["PatriNat"]
    authority: Literal["MNHN"]
    program: Literal["INPN"]
    dataset_id: Literal["EP"]
    dataset_name: Literal["Base de référence des espaces protégés français"]
    declared_version: DeclaredVersion
    reference_page_url: HttpUrl
    archive_url: HttpUrl
    archive_filename: Literal["EP.zip"]
    expected_archive_size_bytes: StrictPositiveInt
    expected_archive_sha256: CanonicalSha256
    cache_root: Path

    @model_validator(mode="after")
    def _pinned_official_urls(self) -> Self:
        if str(self.reference_page_url) != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("reference_page_url must be the reviewed PatriNat page")
        if str(self.archive_url) != OFFICIAL_ARCHIVE_URL:
            raise ValueError("archive_url must be the reviewed official EP archive")
        return self
```

### `_DownloadMetadata`

**Source purpose:** Defines `_DownloadMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `schema_version` | `Literal[1]` | `required` | `schema_version: Literal[1]` |
| `provider` | `Literal['PatriNat']` | `required` | `provider: Literal["PatriNat"]` |
| `authority` | `Literal['MNHN']` | `required` | `authority: Literal["MNHN"]` |
| `program` | `Literal['INPN']` | `required` | `program: Literal["INPN"]` |
| `dataset_id` | `Literal['EP']` | `required` | `dataset_id: Literal["EP"]` |
| `dataset_name` | `Literal['Base de référence des espaces protégés français']` | `required` | `dataset_name: Literal["Base de référence des espaces protégés français"]` |
| `declared_version` | `DeclaredVersion` | `required` | `declared_version: DeclaredVersion` |
| `reference_page_url` | `str` | `required` | `reference_page_url: str` |
| `archive_url` | `str` | `required` | `archive_url: str` |
| `filename` | `Literal['EP.zip']` | `required` | `filename: Literal["EP.zip"]` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `file_size` | `StrictPositiveInt` | `required` | `file_size: StrictPositiveInt` |
| `sha256` | `CanonicalSha256` | `required` | `sha256: CanonicalSha256` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.inpn_protected_areas_fr::_download_metadata` via `_DownloadMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_download_metadata` via `_DownloadMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_load_cached_download` via `_DownloadMetadata`

**Exact class source**

```python
class _DownloadMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    provider: Literal["PatriNat"]
    authority: Literal["MNHN"]
    program: Literal["INPN"]
    dataset_id: Literal["EP"]
    dataset_name: Literal["Base de référence des espaces protégés français"]
    declared_version: DeclaredVersion
    reference_page_url: str
    archive_url: str
    filename: Literal["EP.zip"]
    download_timestamp: str
    file_size: StrictPositiveInt
    sha256: CanonicalSha256

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int or value != DOWNLOAD_METADATA_SCHEMA_VERSION:
            raise ValueError("Download metadata schema_version must be exact integer 1")
        return value

    @field_validator("reference_page_url")
    @classmethod
    def _exact_reference_page(cls, value: str) -> str:
        if value != OFFICIAL_REFERENCE_PAGE_URL:
            raise ValueError("Cached reference page identity differs")
        return value

    @field_validator("archive_url")
    @classmethod
    def _exact_archive_url(cls, value: str) -> str:
        if value != OFFICIAL_ARCHIVE_URL:
            raise ValueError("Cached archive URL identity differs")
        return value

    @field_validator("download_timestamp")
    @classmethod
    def _aware_utc_timestamp(cls, value: str) -> str:
        _validate_utc_timestamp(value)
        return value
```

### `_ExtractedFileMetadata`

**Source purpose:** Defines `_ExtractedFileMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `relative_path` | `str` | `required` | `relative_path: str` |
| `file_size` | `StrictNonNegativeInt` | `required` | `file_size: StrictNonNegativeInt` |
| `sha256` | `CanonicalSha256` | `required` | `sha256: CanonicalSha256` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.sources.inpn_protected_areas_fr::_ExtractionMetadata._deterministic_files` via `_ExtractedFileMetadata`
- constructor call: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `_ExtractedFileMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `_ExtractedFileMetadata`

**Exact class source**

```python
class _ExtractedFileMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    relative_path: str
    file_size: StrictNonNegativeInt
    sha256: CanonicalSha256

    @field_validator("relative_path")
    @classmethod
    def _canonical_path(cls, value: str) -> str:
        _validate_inventory_relative_path(value)
        return value
```

### `_ExtractionMetadata`

**Source purpose:** Defines `_ExtractionMetadata`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |
| `schema_version` | `Literal[1]` | `required` | `schema_version: Literal[1]` |
| `archive_sha256` | `CanonicalSha256` | `required` | `archive_sha256: CanonicalSha256` |
| `archive_size` | `StrictPositiveInt` | `required` | `archive_size: StrictPositiveInt` |
| `files` | `tuple[_ExtractedFileMetadata, ...]` | `Field(min_length=1)` | `files: tuple[_ExtractedFileMetadata, ...] = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `_ExtractionMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_extraction_metadata` via `_ExtractionMetadata`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_validate_extraction_cache` via `_ExtractionMetadata`

**Exact class source**

```python
class _ExtractionMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    archive_sha256: CanonicalSha256
    archive_size: StrictPositiveInt
    files: tuple[_ExtractedFileMetadata, ...] = Field(min_length=1)

    @field_validator("schema_version", mode="before")
    @classmethod
    def _strict_schema_version(cls, value: object) -> object:
        if type(value) is not int or value != EXTRACTION_METADATA_SCHEMA_VERSION:
            raise ValueError(
                "Extraction metadata schema_version must be exact integer 1"
            )
        return value

    @field_validator("files")
    @classmethod
    def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
        paths = tuple(item.relative_path for item in value)
        if paths != tuple(sorted(paths)) or len(set(paths)) != len(paths):
            raise ValueError(
                "Extraction inventory must be unique and lexically ordered"
            )
        return value
```

## 6. Functions and methods

Loader: `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime acquisition consumers are `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` and `validate_inpn_protected_areas_extraction`. Catalog, attribute, geometry and bundle boundaries reuse the same config and lower source revalidation. Road policies and scan `ProfileReference` are unrelated loaders.

## 9. Error handling

The owning Pydantic model rejects extra/missing/unsupported/coerced values according to the exact model/validators above; the loader translates YAML/path/model failures into its documented controlled error.

## 10. Side effects

Network I/O: none. Filesystem read: the loader reads this YAML. Filesystem write: none. Input mutation: none. GIS calculation: none. Hashing: none; this loader parses/validates configuration values but does not hash this file's bytes.

## 11. Security / trust boundaries

A configured URL/provider/hash is a source lock or provenance input. Physical authority requires the consuming source adapter's safe transport and byte/source revalidation.

## 12. GIS / CRS rules

This config declares no CRS or geometry field. Acquisition neither opens spatial datasets nor transforms geometry.

## 13. Provenance rules

The companion's Source SHA256 binds this checked-in file for documentation fidelity; that documentation digest is not attributed to the runtime loader. Source identities remain textual until the adapter validates physical bytes/content.

## 14. Business meaning

This source lock declares no thresholds, environmental outcomes, category rules or authorization. Its version, URLs and expected archive integrity identify bytes only.

## 15. Explicit non-goals

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior only where the runtime source actually computes a hash.

## 17. Change impact

Any YAML byte/value change requires policy/source review, consumer tests, generated artifacts where applicable, this companion SHA update, and only those runtime hashes whose documented algorithm actually includes these bytes or validated values.

## 18. Complete readable configuration and authoritative raw-byte snapshot

### Complete readable YAML

The following is the complete decoded UTF-8 configuration with line endings normalized to LF for stable Markdown display. Every character and logical line is present, but this readable fence is not the authority for original CR/LF byte positions.

```yaml
provider: "PatriNat"
authority: "MNHN"
program: "INPN"
dataset_id: "EP"
dataset_name: "Base de référence des espaces protégés français"
declared_version: "07/2026"
reference_page_url: "https://www.patrinat.fr/fr/page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353"
archive_url: "https://assets.patrinat.fr/files/donnees/ep/EP.zip"
archive_filename: "EP.zip"
expected_archive_size_bytes: 99835011
expected_archive_sha256: "73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5"
cache_root: ".cache/landscout/inpn/protected_areas"
```

### Authoritative raw-byte payload

- Raw byte length: `571`.
- Raw SHA256: `75e3e45003b66cff10a755dfd64c27d3066ba65e4807af6e17e82bd3eae03397` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
cHJvdmlkZXI6ICJQYXRyaU5hdCIKYXV0aG9yaXR5OiAiTU5ITiIKcHJvZ3JhbTogIklOUE4iCmRh
dGFzZXRfaWQ6ICJFUCIKZGF0YXNldF9uYW1lOiAiQmFzZSBkZSByw6lmw6lyZW5jZSBkZXMgZXNw
YWNlcyBwcm90w6lnw6lzIGZyYW7Dp2FpcyIKZGVjbGFyZWRfdmVyc2lvbjogIjA3LzIwMjYiCnJl
ZmVyZW5jZV9wYWdlX3VybDogImh0dHBzOi8vd3d3LnBhdHJpbmF0LmZyL2ZyL3BhZ2UtdGVtcG9y
YWlyZS1kZS10ZWxlY2hhcmdlbWVudC1kZXMtcmVmZXJlbnRpZWxzLWRlLWRvbm5lZXMtbGllcy1s
aW5wbi03MzUzIgphcmNoaXZlX3VybDogImh0dHBzOi8vYXNzZXRzLnBhdHJpbmF0LmZyL2ZpbGVz
L2Rvbm5lZXMvZXAvRVAuemlwIgphcmNoaXZlX2ZpbGVuYW1lOiAiRVAuemlwIgpleHBlY3RlZF9h
cmNoaXZlX3NpemVfYnl0ZXM6IDk5ODM1MDExCmV4cGVjdGVkX2FyY2hpdmVfc2hhMjU2OiAiNzM2
ODhiYzM3MjA1YTVlN2Y1OWUyMDY1YTBiODFmYzhjZjJhMjQyYmRlYzVkN2QyNzg2ZjA4MzY3MWM0
YWJlNSIKY2FjaGVfcm9vdDogIi5jYWNoZS9sYW5kc2NvdXQvaW5wbi9wcm90ZWN0ZWRfYXJlYXMi
Cg==
```
