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

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `provider` | `"PatriNat"` | `str` | annotation `Literal['PatriNat']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the configured source provider copied/compared as lineage. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `authority` | `"MNHN"` | `str` | annotation `Literal['MNHN']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the configured publishing/oversight authority retained as source identity. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `program` | `"INPN"` | `str` | annotation `Literal['INPN']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the official source program retained as identity. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `dataset_id` | `"EP"` | `str` | annotation `Literal['EP']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Selects the exact external dataset identity used in source URL/API/cache validation. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `dataset_name` | `"Base de référence des espaces protégés français"` | `str` | annotation `Literal['Base de référence des espaces protégés français']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Records the exact human-readable external dataset name. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `declared_version` | `"07/2026"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=None, to_upper=None, to_lower=None, strict=True, min_length=None, max_length=None, pattern='^(?:0[1-9]|1[0-2])/\\d{4}$', ascii_only=None); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Pins the declared source snapshot version and contributes to cache/source identity. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `reference_page_url` | `"https://www.patrinat.fr/fr/page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353"` | `str` | annotation `<class 'pydantic.networks.HttpUrl'>`; required; no inline Field metadata; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Records the official reference-page provenance URL; it is not the archive bytes. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `archive_url` | `"https://assets.patrinat.fr/files/donnees/ep/EP.zip"` | `str` | annotation `<class 'pydantic.networks.HttpUrl'>`; required; no inline Field metadata; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Pins the official HTTPS archive location; transport safety and adapter origin/path checks still apply. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `archive_filename` | `"EP.zip"` | `str` | annotation `Literal['EP.zip']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Pins the portable archive basename used by cache/source validation. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `expected_archive_size_bytes` | `99835011` | `int` | annotation `<class 'int'>`; required; Strict(strict=True), Gt(gt=0); strict positive integer; Boolean rejected; exact physical archive pin | Pins the exact approved archive byte length. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `expected_archive_sha256` | `"73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5"` | `str` | annotation `<class 'str'>`; required; StringConstraints(strip_whitespace=None, to_upper=None, to_lower=None, strict=True, min_length=None, max_length=None, pattern='^[0-9a-f]{64}$', ascii_only=None); strict lowercase 64-character hexadecimal SHA256; exact physical archive pin | Pins the lowercase SHA256 of the approved archive bytes. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |
| `cache_root` | `".cache/landscout/inpn/protected_areas"` | `str` | annotation `<class 'pathlib.Path'>`; required; no inline Field metadata; required safe cache path under the owning adapter contract | Selects the repository-relative cache root; containment/link/recovery checks apply at runtime. | `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive` |

## 5. Classes / models / dataclasses

Authoritative owning model: `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig`. The checked-in file currently validates as `InpnProtectedAreasSourceConfig`.

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
            raise ValueError("Extraction metadata schema_version must be exact integer 1")
        return value

    @field_validator("files")
    @classmethod
    def _deterministic_files(
        cls, value: tuple[_ExtractedFileMetadata, ...]
    ) -> tuple[_ExtractedFileMetadata, ...]:
        paths = tuple(item.relative_path for item in value)
        if paths != tuple(sorted(paths)) or len(set(paths)) != len(paths):
            raise ValueError("Extraction inventory must be unique and lexically ordered")
        return value
```

## 6. Functions and methods

Loader: `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, byte hashing, and cross-field validation.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior.

## 17. Change impact

Any YAML byte/value change requires policy/source review, affected config/result hashes, consumer tests, generated artifacts where applicable, and this companion SHA update.
